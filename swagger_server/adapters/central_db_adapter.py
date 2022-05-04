import base64
import json
from itsdangerous import exc
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from flask import abort
import codecs


class CentralDBAdapter:

    token = {}

    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv(
            "CENTRAL_DB_BASE_URL") or 'https://db.flexgrid-project.eu'
        self.token = None

    def get_token(self):

        # print(f"headers: {headers} user {os.environ.get('NORDPOOL_USERNAME')} pass {os.environ.get('NORDPOOL_PASSWORD')}")
        __class__.token = json.loads(
            requests.post(os.environ.get("CENTRAL_DB_BASE_URL") + "/oauth/token", data={
                'grant_type': 'password',
                'client_id': os.environ.get("CENTRAL_DB_CLIENT_ID"),
                'username': os.environ.get("CENTRAL_DB_USERNAME"),
                'password': os.environ.get("CENTRAL_DB_PASSWORD"),
            },
            ).content)
        __class__.token['acquired_at'] = datetime.utcnow()

    def have_valid_token(self):
        return __class__.token and 'acquired_at' in __class__.token and 'expires_in' in __class__.token and (__class__.token['acquired_at'] + timedelta(seconds=__class__.token['expires_in'] - 30) > datetime.utcnow())

    def auth_headers(self):

        if os.environ.get("SAMPLE_DATA"):
            return {'Authorization': f"Bearer XXXXXXX"}

        if not self.have_valid_token():
            self.get_token()

        return {'Authorization': f"Bearer {__class__.token['access_token']}"}

    def get_collection(self, collection, where_params):
        url = f"{self.base_url}/{collection}"

        if os.environ.get("SET_SAMPLE_DATA") or os.environ.get("SAMPLE_DATA"):
            file_path = f"./sample_data/{url.replace('/', '_')}"

        headers = self.auth_headers()

        if os.environ.get("SAMPLE_DATA"):
            with open(file_path, "rb") as infile:
                return json.load(infile)

        result = []
        params = {'where': json.dumps(where_params)}
        while True:
            print("url", url)
            # print("params", params)
            # print("where_params", where_params)

            response = requests.request("GET",
                                        url,
                                        headers=headers,
                                        params=params)

            # print(response.text)
            response.raise_for_status()
            resp_json = json.loads(response.text)
            result.extend(resp_json["_items"])
            if not 'next' in resp_json['_links']:
                break
            url = f"{self.base_url}/{resp_json['_links']['next']['href']}"
            params = {}

        if os.environ.get("SET_SAMPLE_DATA"):
            with open(file_path, "wb") as outfile:
                json.dump(result, codecs.getwriter('utf-8')
                          (outfile), ensure_ascii=False,  indent=4)

        return result

    def get_load_entries(self, prosumer_ids, start_timestamp, end_timestamp):
        return self.get_collection('load_entries', {"prosumer_id": {"$in": prosumer_ids},
                                                    "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})

    def get_curtailable_loads(self, prosumer_ids, start_timestamp, end_timestamp):
        return self.get_collection('curtailable_loads', {"prosumer_id": {"$in": prosumer_ids},
                                                         "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})

    def get_flex_request_data_points(self, flex_request_id, start_timestamp, end_timestamp):
        return self.get_collection('flex_request_data_points', {"flex_request_id": flex_request_id,
                                                                "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
    def get_flex_offer_data_points(self, flex_offer_id, start_timestamp, end_timestamp):
        return self.get_collection('flex_offer_data_points', {"flex_offer_id": flex_offer_id,
                                                                "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})

    def get_objects(self, collection, names):
        return self.get_collection(collection, {"name": {"$in": names}})

    def get_dr_prosumers(self, prosumer_names, start_timestamp, end_timestamp):
        dr_prosumers = self.get_objects('dr_prosumers', prosumer_names)

        dr_prosumer_ids = {prosumer['_id']
            : prosumer for prosumer in dr_prosumers}
        # print(dr_prosumer_ids)
        curtailable_loads = self.get_curtailable_loads(list(dr_prosumer_ids.keys()), start_timestamp.strftime(
            '%Y-%m-%dT%H:%M:%SZ'), end_timestamp.strftime('%Y-%m-%dT%H:%M:%SZ'))

        # print(curtailable_loads)
        load_entries = self.get_load_entries(list(dr_prosumer_ids.keys()), start_timestamp.strftime(
            '%Y-%m-%dT%H:%M:%SZ'), end_timestamp.strftime('%Y-%m-%dT%H:%M:%SZ'))
        # print(load_entries)

        for load in curtailable_loads:
            prosumer = dr_prosumer_ids[load["prosumer_id"]]
            if "curtailable_loads" not in prosumer:
                prosumer["curtailable_loads"] = []
            prosumer["curtailable_loads"] += [load]

        for load in load_entries:
            arr = dr_prosumer_ids[load["prosumer_id"]
                                  ][load["type"]][load["offset"]]
            if "load_entries" not in arr:
                arr["load_entries"] = []
            arr["load_entries"] += [load]

        dr_prosumer_names = {prosumer['name']: prosumer for prosumer in dr_prosumers}

        res = []
        for p in prosumer_names:
            if p not in dr_prosumer_names:
                abort(
                    400, description=f"No data for dr_prosumer {p} at specified time range")

            for dev in dr_prosumer_names[p]['shiftable_devices']:
                if not 'load_entries' in dev:
                    dev['load_entries'] = []
            for ev in dr_prosumer_names[p]['EVs']:
                if not 'load_entries' in ev:
                    ev['load_entries'] = []
            res.append(dr_prosumer_names[p])
        return res

    def get_flex_request(self, flex_request_name, start_timestamp, end_timestamp):
        flex_requests = self.get_objects('flex_requests', [flex_request_name])

        if len(flex_requests) != 1:
            abort(
                400, description=f"error obtaining data for flex_requestL: '{flex_request_name}, found: {len(flex_requests)}'")

        flex_request = flex_requests[0]

        flex_request['data_points'] = self.get_flex_request_data_points(flex_request['_id'], start_timestamp.strftime(
            '%Y-%m-%dT%H:%M:%SZ'), end_timestamp.strftime('%Y-%m-%dT%H:%M:%SZ'))

        return flex_request

    def get_flex_offer(self, flex_offer_name, start_timestamp, end_timestamp):
        flex_offers = self.get_objects('flex_offers', [flex_offer_name])

        if len(flex_offers) != 1:
            abort(
                400, description=f"error obtaining data for flex_offers: '{flex_offer_name}, found: {len(flex_offers)}'")

        flex_offer = flex_offers[0]

        flex_offer['data_points'] = self.get_flex_offer_data_points(flex_offer['_id'], start_timestamp.strftime(
            '%Y-%m-%dT%H:%M:%SZ'), end_timestamp.strftime('%Y-%m-%dT%H:%M:%SZ'))

        return flex_offer