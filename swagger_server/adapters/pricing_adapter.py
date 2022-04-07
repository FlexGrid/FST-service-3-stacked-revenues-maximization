from swagger_server.models.job_submitted import JobSubmitted
from swagger_server.models.pricing_data import PricingData
from swagger_server.models.pricing_job_result import PricingJobResult
from swagger_server.models.pricing_params import PricingParams
from swagger_server.adapters.central_db_adapter import CentralDBAdapter
import json
from flask import abort, url_for

from workers.tasks import pricing, get_task_info


def get_pricing_adapter(job_id):
    task = get_task_info(job_id)

    return PricingJobResult.from_dict({
        'job_id': job_id,
        'status': task.status,
        'date_done': task.date_done.strftime('%Y-%m-%dT%H:%M:%SZ') if task.date_done else None,
        'result': task.result if task.status == "SUCCESS" else None,
        'error': str(task.result) if task.status == "FAILURE" else None,
        'traceback': task.traceback,
    })


def post_pricing_adapter(pricing_params):
    assert isinstance(pricing_params, PricingParams)

    print(f"The object is {pricing_params}")

    result = run_algorithm(pricing_params)

    return JobSubmitted.from_dict({
        "job_id": result.id,
        'href': url_for(
            '.swagger_server_controllers_pricing_ucs42_controller_pricing_get',
            job_id=result.id
        )
    })


def run_algorithm(flex_offer_params):

    # prosumers = []
    # for i in range(10):
    #     prosumers += [ f'user_{i+1}_Low', f'user_{i+1}_Medium', f'user_{i+1}_High']

    db_adapter = CentralDBAdapter()
    dr_prosumer_data = db_adapter.get_dr_prosumers(flex_offer_params.dr_prosumers,
                                                   flex_offer_params.start_datetime, flex_offer_params.end_datetime)
    # dr_prosumer_data = CentralDBClient().get_dr_prosumers(prosumers,

    print(json.dumps(dr_prosumer_data, indent=4, sort_keys=True))

    if len(dr_prosumer_data) != len(flex_offer_params.dr_prosumers):
        # raise  ValueError("Missing prosumer")
        abort(500, description="Missing data for at least one prosumer in centrail db")

    offer_nsteps = -1
    T = -1
    delta_shift = {}
    delta_ev = {}
    for idx_prosumer, prosumer in enumerate(dr_prosumer_data):
        if T < 0:
            T = len(prosumer["curtailable_loads"])
        elif T != len(prosumer["curtailable_loads"]):
            abort(500, description="Number of datapoints for each prosumer is different")

        for load in prosumer["curtailable_loads"]:
            n = len(load["flexibility"])
            if n > 0:
                if offer_nsteps < 0:
                    offer_nsteps = n
                elif offer_nsteps != n:
                    abort(
                        500, description="Number of bid curve points for each curtailable load timestamp is different")

        for idx_device, device in enumerate(prosumer['shiftable_devices']):
            for load_entry in device['load_entries']:
                if not (idx_prosumer, idx_device) in delta_shift:
                    delta_shift[idx_prosumer,
                                idx_device] = load_entry['price_euro_per_kw']

                if delta_shift[idx_prosumer, idx_device] != load_entry['price_euro_per_kw']:
                    abort(
                        500, description=f"price should be constant for each device prosumer: {prosumer['name']} device: {device['name']}")

        for idx_ev, ev in enumerate(prosumer['EVs']):
            for load_entry in ev['load_entries']:
                if not (idx_prosumer, idx_ev) in delta_ev:
                    delta_ev[idx_prosumer,
                             idx_ev] = load_entry['price_euro_per_kw']

                if delta_ev[idx_prosumer, idx_ev] != load_entry['price_euro_per_kw']:
                    abort(
                        500, description=f"price should be constant for each ev. prosumer: {prosumer['name']} ev: {ev['name']}")

    flex_request_data = db_adapter.get_flex_request(flex_offer_params.flex_request,
                                                    flex_offer_params.start_datetime, flex_offer_params.end_datetime)

    if len(flex_request_data['data_points']) != T:
        abort(
            500, description=f"Number of datapoints in flex_request_data is {len(flex_request_data['data_points'])} but T = {T}")

    bid_nsteps = -1
    for bid_data_point in flex_request_data['data_points']:
        if bid_nsteps < 0:
            bid_nsteps = len(bid_data_point['flexibility'])
        elif bid_nsteps != len(bid_data_point['flexibility']):
            abort(500, description="Number of bid_steps is inconsistent")

    if not 0 in flex_offer_params.gamma_values:
        flex_offer_params.gamma_values = [0] + flex_offer_params.gamma_values

    return pricing.delay(flex_offer_params.profit_margin,
                         flex_offer_params.gamma_values,
                         flex_offer_params.start_datetime,
                         dr_prosumer_data,
                         flex_request_data,
                         flex_offer_params.callback.url if flex_offer_params.callback else None,
                         flex_offer_params.callback.headers if flex_offer_params.callback else None)
