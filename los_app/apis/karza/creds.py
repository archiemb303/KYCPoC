import json
import http.client
# from tests_cred.credentials.get_credentials import get_cred
from los_app.apis.karza.getcredentials.credentials.get_credentials import get_cred


class KarzaKeys():
    # Get api key,api url and test api url
    cred = get_cred()
    api_key = cred['api_key']
    test_api_url = cred['test_api_url']
    api_url = cred['api_url']

    def make_api_call(self, request):
        conn = http.client.HTTPSConnection(self.test_api_url)
        headers = {'content-type': "application/json", 'x-karza-key': self.api_key}

        api_endpoint_url = request['api_endpoint_url']
        payload = json.dumps(request['payload'])
        # payload = "{\"consent\":\"<<Y/N>>\",\"pan\":\"BXXXXXXXXR\"}"

        conn.request("POST", api_endpoint_url, payload, headers)
        # conn.request("POST", "/v2/pan", payload, headers)

        res = conn.getresponse()
        data = res.read()

        output_json = dict(zip(['request_details', 'response_details'],
                               [payload, data.decode("utf-8")]))

        return output_json

    def make_api_call_2(self, request):
        import requests
        url = f"https://self.test_api_url{request['api_endpoint_url']}"

        # payload = "{\"consent\":\"Y\",\"pan\":\"AKVPA3378G\"}"
        payload = json.dumps(request['payload'])
        headers = {'content-type': 'application/json', 'x-karza-key': self.api_key}
        response = requests.request("POST", url, data=payload, headers=headers)

        output_json = dict(zip(['request_details', 'response_details'],
                               [payload, response.text]))

        return output_json

    def make_api_call_3(self, request):
        import http.client

        conn = http.client.HTTPSConnection(self.api_url)
        headers = {'content-type': "application/json", 'x-karza-key': self.api_key}

        api_endpoint_url = request['api_endpoint_url']
        payload = json.dumps(request['payload'])
        # payload = "{\"consent\":\"<<Y/N>>\",\"pan\":\"BXXXXXXXXR\"}"

        conn.request("POST", api_endpoint_url, payload, headers)
        # conn.request("POST", "/v2/pan", payload, headers)

        res = conn.getresponse()
        data = res.read()

        output_json = dict(zip(['request_details', 'response_details'],
                               [payload, data.decode("utf-8")]))

        return output_json
