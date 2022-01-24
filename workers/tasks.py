import dateutil.parser
import time
from celery.result import AsyncResult
from celery import Celery
import numpy as np
import simplejson
import json
import requests
import traceback

from BRTP.BRTP_portfolio import dr_portfolio

app = Celery('tasks', backend='rpc://')

app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.broker_transport_options = {'visibility_timeout': 3600}
app.conf.result_backend = 'redis://localhost:6379/0'


# @app.task
# def add(x, y):
#     time.sleep(30)
#     raise Exception("Oops")
#     return x + y


def get_task_info(hash):
    return AsyncResult(hash, app=app)


@app.task
def pricing(profit_margin, gamma_values, start_datetime, dr_prosumer_data, flex_request_data, callback_url, callback_headers):
    auw_vs_gamma = 0
    uw_bar = 0
    flex_revenues = 0
    flex_quantity = 0
    final_ecc = 1
    n_users = len(dr_prosumer_data)

    T = -1
    pr = profit_margin
    G_VALUES = np.array(gamma_values)

    offer_nsteps = -1

    nshift_per_user = np.zeros([n_users, 1], dtype=int)
    nevs_per_user = np.zeros([n_users, 1], dtype=int)

    for idx, prosumer in enumerate(dr_prosumer_data):
        if T < 0:
            T = len(prosumer["curtailable_loads"])
        elif T != len(prosumer["curtailable_loads"]):
            raise ValueError(
                "Number of datapoints for each prosumer is different")
        for load in prosumer["curtailable_loads"]:
            n = len(load["flexibility"])
            if n > 0:
                if offer_nsteps < 0:
                    offer_nsteps = n
                elif offer_nsteps != n:
                    raise ValueError(
                        "Number of bid curve points for each curtailable load timestamp is different")
        nshift_per_user[idx, 0] = len(prosumer["shiftable_devices"])
        nevs_per_user[idx, 0] = len(prosumer["EVs"])

    shiftable_consumption = np.zeros(
        [np.amax(nshift_per_user), T, n_users], dtype=float)
    evs_consumption = np.zeros(
        [np.amax(nevs_per_user), T, n_users], dtype=float)
    charge_limit = np.zeros([n_users, np.amax(nevs_per_user)], dtype=int)
    desired_start_times = np.zeros(
        [n_users, np.amax(nshift_per_user) + np.amax(nevs_per_user)], dtype=int)
    desired_finish_times = np.zeros(
        [n_users, np.amax(nshift_per_user) + np.amax(nevs_per_user)], dtype=int)
    deadlines = np.zeros(
        [n_users, np.amax(nshift_per_user) + np.amax(nevs_per_user)], dtype=int)
    delta = np.zeros([n_users, np.amax(nshift_per_user) +
                      np.amax(nevs_per_user)], dtype=float)
    desired_x = np.zeros([n_users, T], dtype=float)
    baseload = np.zeros([n_users, T], dtype=float)
    curtailable_bids = np.zeros([n_users * offer_nsteps, 2 * T], dtype=float)

    for idx_prosumer, prosumer in enumerate(dr_prosumer_data):
        for idx_device, device in enumerate(prosumer['shiftable_devices']):
            for load_entry in device['load_entries']:
                print("load_entry['timestamp']", load_entry['timestamp'])

                print("start_datetime",
                      start_datetime)
                t = (dateutil.parser.isoparse(
                    load_entry['timestamp']) - dateutil.parser.isoparse(start_datetime)).total_seconds() / 3600
                d = (dateutil.parser.isoparse(
                    load_entry['deadline']) - dateutil.parser.isoparse(start_datetime)).total_seconds() / 3600

                shiftable_consumption[idx_device,  round(
                    t), idx_prosumer] = load_entry['kw']
                if not desired_start_times[idx_prosumer, idx_device] > 0:
                    desired_start_times[idx_prosumer,
                                        idx_device] = round(t) + 1
                deadlines[idx_prosumer, idx_device] = round(d) + 1
                desired_finish_times[idx_prosumer, idx_device] = round(t) + 1

                if not delta[idx_prosumer, idx_device] > 0:
                    delta[idx_prosumer, idx_device] = load_entry['price_euro_per_kw']

                if delta[idx_prosumer, idx_device] != load_entry['price_euro_per_kw']:
                    raise ValueError(
                        500, description=f"price should be constant for each device prosumer: {prosumer['name']} device: {device['name']}")

        for idx_ev, ev in enumerate(prosumer['EVs']):
            charge_limit[idx_prosumer, idx_ev] = round(ev['charge_limit'])
            for load_entry in ev['load_entries']:
                # print("load_entry['timestamp']", load_entry['timestamp'])

                # print("start_datetime",start_datetime)
                t = (dateutil.parser.isoparse(
                    load_entry['timestamp']) - dateutil.parser.isoparse(start_datetime)).total_seconds() / 3600
                d = (dateutil.parser.isoparse(
                    load_entry['deadline']) - dateutil.parser.isoparse(start_datetime)).total_seconds() / 3600
                # charge_limit[idx_prosumer, 0] = int(d)
                evs_consumption[idx_ev,  round(
                    t), idx_prosumer] = load_entry['kw']
                if not desired_start_times[idx_prosumer, np.amax(nshift_per_user) + idx_ev] > 0:
                    desired_start_times[idx_prosumer, np.amax(
                        nshift_per_user) + idx_ev] = round(t) + 1
                deadlines[idx_prosumer, np.amax(
                    nshift_per_user) + idx_ev] = round(d) + 1
                desired_finish_times[idx_prosumer, np.amax(
                    nshift_per_user) + idx_ev] = round(t) + 1

                if not delta[idx_prosumer, np.amax(nshift_per_user) + idx_ev] > 0:
                    delta[idx_prosumer, np.amax(
                        nshift_per_user) + idx_ev] = load_entry['price_euro_per_kw']

                if delta[idx_prosumer, np.amax(nshift_per_user) + idx_ev] != load_entry['price_euro_per_kw']:
                    raise ValueError(
                        f"price should be constant for each ev. prosumer: {prosumer['name']} ev: {ev['name']}")

        for idx_curltailable_load, curltailable_load in enumerate(prosumer['curtailable_loads']):
            t = (dateutil.parser.isoparse(
                curltailable_load['timestamp']) - dateutil.parser.isoparse(start_datetime)).total_seconds() / 3600
            desired_x[idx_prosumer, round(
                t)] = curltailable_load['desired_consumption_kw']
            baseload[idx_prosumer, round(
                t)] = curltailable_load['base_load_kw']

            for idx_flex, flex in enumerate(curltailable_load['flexibility']):
                curtailable_bids[idx_prosumer * offer_nsteps +
                                 idx_flex, 2 * round(t)] = flex['price_euro_per_kw']
                curtailable_bids[idx_prosumer * offer_nsteps +
                                 idx_flex, 2 * round(t) + 1] = flex['quantity_kw']

    duration = desired_finish_times - desired_start_times + 1

    E_mat_shifts = np.sum(shiftable_consumption, axis=1).transpose()
    E_mat_evs = np.sum(evs_consumption, axis=1).transpose()
    E_matrix = np.concatenate((E_mat_shifts, E_mat_evs), axis=1)

    if len(flex_request_data['data_points']) != T:
        raise ValueError(
            f"Number of datapoints in flex_request_data is {len(flex_request_data['data_points'])} but T = {T}")

    bid_nsteps = -1
    for bid_data_point in flex_request_data['data_points']:
        if bid_nsteps < 0:
            bid_nsteps = len(bid_data_point['flexibility'])
        elif bid_nsteps != len(bid_data_point['flexibility']):
            raise ValueError("Number of bid_steps is inconsistent")

    flex_request = np.zeros([bid_nsteps, 2 * T])

    for bid_data_point in flex_request_data['data_points']:
        t = (dateutil.parser.isoparse(
            bid_data_point['timestamp']) - dateutil.parser.isoparse(start_datetime)).total_seconds() / 3600
        for idx_flex, flex in enumerate(bid_data_point['flexibility']):
            flex_request[idx_flex, 2 * round(t)] = flex['price_euro_per_kw']
            flex_request[idx_flex, 2 * round(t) + 1] = flex['quantity_kw']

    # print(json.dumps(flex_request_data, indent=4, sort_keys=True))

    print("auw_vs_gamma", auw_vs_gamma)
    print("uw_bar", uw_bar)
    print("flex_revenues", flex_revenues)
    print("flex_quantity", flex_quantity)
    print("final_ecc", final_ecc)
    print("n_users", n_users)
    print("T", T)
    print("offer_nsteps", offer_nsteps)
    print("bid_nsteps", bid_nsteps)
    print("pr", pr)
    print("G_VALUES", G_VALUES)
    print("nshift_per_user", nshift_per_user)
    print("nshift_cons", "UNUSED")
    print("shiftable_consumption", shiftable_consumption)
    print("nevs_per_user", nevs_per_user)
    print("nevs_cons", "UNUSED")
    print("evs_consumption", evs_consumption)
    print("charge_limit", charge_limit)
    print("desired_start_times", desired_start_times)
    print("deadlines", deadlines)
    print("desired_finish_times", desired_finish_times)
    print("duration", duration)
    print("E_matrix", E_matrix)
    print("delta", delta)
    print("desired_x", desired_x)
    print("baseload", baseload)
    print("curtailable_bids", curtailable_bids)
    print("flex_request", flex_request)

    # Initialization of KPIs
    AUW_BRTP = np.zeros(np.size(G_VALUES), dtype=float)
    TC_BRTP = np.zeros(np.size(G_VALUES), dtype=float)
    BB_BRTP = np.zeros(np.size(G_VALUES), dtype=float)
    uw_bar_plot = np.zeros((np.size(G_VALUES), n_users), dtype=float)
    FLEX_Q = np.zeros(np.size(G_VALUES), dtype=float)
    FLEX_R = np.zeros(np.size(G_VALUES), dtype=float)
    fairness_ratio = np.zeros((np.size(G_VALUES), n_users+1))
    fairness_ratio_avrg = np.zeros(np.size(G_VALUES))
    FINALCONS = np.zeros((np.size(G_VALUES), T), dtype=float)
    ITER = -1

    for gamma in G_VALUES:
        aggr_flex = dr_portfolio(n_users, T, offer_nsteps, bid_nsteps, pr, gamma, None, None, nshift_per_user, None, shiftable_consumption,
                                 nevs_per_user, None, evs_consumption, charge_limit, desired_start_times, deadlines, desired_finish_times, duration, E_matrix, delta, desired_x, baseload, curtailable_bids, flex_request, auw_vs_gamma, None, None, None, None)

        # Run BRTP Algorithm
        [AUW, TC, BB, UW, FlexQ, FlexSuppliersRevenues,
            x, initial_x] = aggr_flex.Run_BRTP()
        print("\n\n************ RESULTS ************\n")
        print("AUW", AUW)
        print("TC", TC)
        print("BB", BB)
        print("UW", UW)
        print("FlexQ", FlexQ)
        print("FlexSuppliersRevenues", FlexSuppliersRevenues)
        print("x", x)
        print("initial_x", initial_x)
        print([AUW, TC, BB, UW, FlexQ, FlexSuppliersRevenues, x, initial_x])

        AUW_BRTP[ITER] = AUW
        TC_BRTP[ITER] = TC
        BB_BRTP[ITER] = BB
        uw_bar_plot[ITER, :] = np.ndarray.copy(UW)
        FLEX_Q[ITER] = FlexQ
        FLEX_R[ITER] = FlexSuppliersRevenues
        FINALCONS[ITER, :] = np.sum(np.sum(x, axis=0), axis=1)

    # Final Metrics
    AUW_BRTP_x = 1+np.divide((AUW_BRTP[0]-AUW_BRTP), AUW_BRTP[0])
    TC_BRTP_x = np.divide(TC_BRTP, TC_BRTP[0])

    print("\n\n************ RESULTS TOTAL ************\n")

    print("AUW_BRTP", AUW_BRTP)
    print("TC_BRTP", TC_BRTP)
    print("BB_BRTP", BB_BRTP)
    print("uw_bar_plot", uw_bar_plot)
    print("FLEX_Q", FLEX_Q)
    print("FLEX_R", FLEX_R)
    print("FINALCONS", FINALCONS)
    print("",)
    print("",)

    plot_bars = np.zeros((np.size(G_VALUES), n_users))
    for i in range(np.size(G_VALUES)):
        plot_bars[i, :] = 1 + \
            np.divide(uw_bar_plot[0, :]-uw_bar_plot[i, :], uw_bar_plot[0, :])

    result = json.loads(simplejson.dumps({
        'raw_data': {
            "AUW_BRTP": AUW_BRTP.tolist(),
            "TC_BRTP": TC_BRTP.tolist(),
            "BB_BRTP": BB_BRTP.tolist(),
            "uw_bar_plot": uw_bar_plot.tolist(),
            "FLEX_Q": FLEX_Q.tolist(),
            "FLEX_R": FLEX_R.tolist(),
            "FINALCONS": FINALCONS.tolist()
        },
        'plots': {
            'AUW_vs_GAMMA': {
                'title': "Ratio between AUW with B-RTP and AUW with RTP as a function of γ",
                'xlabel': "γ",
                'ylabel': "AUW with B-RTP(γ) / AUW with RTP (γ = 0)",
                'serries': [{'xvalues': G_VALUES.tolist(),
                             'yvalues': AUW_BRTP_x.tolist(),
                             'legend': f"γ = {G_VALUES[i]} {'(RTP)' if i == 0 else ''}"
                             }],
                'plot_type': 'scatter',
            },
            'UW_BAR': [{
                'xlabel': 'Users',
                'ylabel': 'UW with B-RTP(γ)/UW with RTP',
                'serries': [{'xvalues': (np.arange(np.size(row))+1).tolist(),
                             'yvalues': row.tolist()}],
                'plot_type': 'bar',

            } for i, row in enumerate(plot_bars)],
            'FLEX_REVENUES': {
                'xlabel': "γ",
                'ylabel': 'Flexibility Revenues (€)',
                'serries': [{'xvalues': G_VALUES.tolist(),
                             'yvalues': FLEX_R.tolist()}],
                'plot_type': 'bar',

            },
            'FLEX_QUANTITY': {
                'xlabel': "γ",
                'ylabel': 'Flexibility Quantity Delivered (kW)',
                'serries': [{'xvalues': G_VALUES.tolist(),
                             'yvalues': FLEX_Q.tolist()}],
                'plot_type': 'bar',

            },
            'FINAL_ECC': [{
                'title': "Initial vs Final ECC (γ = {})".format(gamma),
                'xlabel': 'Time (h)',
                'ylabel': 'Power Consumption (kW)',
                'serries': [{'xvalues': (np.arange(T)+1).tolist(),
                             'yvalues': np.sum(np.sum(initial_x, axis=0), axis=1).tolist(),
                             'legend': "Initial ECC", },
                            {'xvalues': (np.arange(T)+1).tolist(),
                             'yvalues': FINALCONS.tolist() if np.size(
                                G_VALUES) == 1 else FINALCONS[counter, :].tolist(),
                             'legend': "Final ECC", }],
                'plot_type': 'scatter',

            } for counter, gamma in enumerate(G_VALUES)]
        }
    }, ignore_nan=True))

    if callback_url is not None:
        try:
            post_result = requests.post(callback_url,
                          data=json.dumps(result),
                          headers=callback_headers)
            result['callback_result'] = str(post_result)
        except requests.exceptions.RequestException as e:
            print(e)
            print(traceback.format_exc())
            result['callback_result'] = str(e)
    return result
