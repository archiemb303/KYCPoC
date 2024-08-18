import datetime
import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from los_app.apis.karza.creds import get_cred
# from los_app.apis.karza.pan_verification.documentation_pan_verification import *
from drf_spectacular.utils import extend_schema
from los_app.apis.karza.creds import KarzaKeys
class PANAuthentication(APIView):

  
    
    @extend_schema(
        summary="Validate PAN Number",
        description=(
            "This function will call a 3rd party API to validate the PAN number and return the verification status.\n"
            "**endpoint url:** /v2/pan/"
        ),
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'pan_yes': {
                        'type': 'string',
                        'description': 'User consent for PAN verification',
                        'example': 'Y'
                    },
                    'pan_number': {
                        'type': 'string',
                        'description': 'PAN number to be verified',
                        'example': 'ABCDE1234F'
                    }
                },
                'required': ['pan_yes', 'pan_number']
            }
        },
        responses={
            200: {
                'type': 'object',
                'properties': {
                    'APIName': {'type': 'string', 'example': 'Karza PAN Validation', 'description': 'Name of the API'},
                    'endpoint_url': {'type': 'string', 'example': '/v2/pan', 'description': 'Endpoint URL'},
                    'Request': {'type': 'string', 'example': '{"consent": "Y", "pan": "ABCDE1234F"}', 'description': 'Request sent to the API'},
                    'Response': {'type': 'string', 'example': '{"result":{"pan":"ABCDE1234F","name":"John Doe","panStatus":"Valid","dob":"1980-01-01","message":"Verification Successful","status_code":"101"}}', 'description': 'Response from the API'},
                    'CallTime': {'type': 'string', 'example': '2024-08-18 12:34:56.789012', 'description': 'Time of the API call'},
                    'CallDuration': {'type': 'number', 'example': 1.234567, 'description': 'Duration of the API call in seconds'}
                },
                'description': 'Output if API successfully verifies the PAN number'
            },
            401: {
                'type': 'object',
                'properties': {
                    'Status': {'type': 'integer', 'example': 401, 'description': 'Status code of API output'},
                    'Message': {'type': 'string', 'example': 'Authentication failed', 'description': 'Description of API output status'}
                },
                'description': 'Output if authentication fails'
            },
            404: {
                'type': 'object',
                'properties': {
                    'Status': {'type': 'integer', 'example': 404, 'description': 'Status code of API output'},
                    'Message': {'type': 'string', 'example': 'PAN not found', 'description': 'Description of API output status'}
                },
                'description': 'Output if PAN verification fails'
            }
        },
        tags=["Karza"]
    )

    def post(self, request):
        """
        This function will call the 3rd party api, store the data, and redirect user to workflow details page
        :param request:
        :return:
        """
        input_json = request.data
        output_json = views_pan_authentication_json(request, input_json)
        return Response(output_json)


def views_pan_authentication_json(request, input_params):
    try:
        input_json, output_list = input_params, []
        api_name_var = "Karza PAN Validation"
        endpoint_url_var = "/v2/pan"
        keys_obj = KarzaKeys()

        # For every API Calling style initiate the params accordingly
        third_party_response = dict(zip(["APIName", "endpoint_url", "Request", "Response", "CallTime"],
                                        [api_name_var, endpoint_url_var, None, None, None]))
        timestamp_one = datetime.datetime.now()

        #####################################################################################
        # Call the third party API here
        call_params = dict(zip(["api_endpoint_url", "payload"],
                               [endpoint_url_var, None]))
        call_params['payload'] = dict(zip(["consent", "pan"],
                                          [input_json['pan_yes'], input_json['pan_number']]))
        third_party_call_result = keys_obj.make_api_call(call_params)
        print(third_party_call_result)

        third_party_response['Request'] = third_party_call_result['request_details']
        third_party_response['Response'] = third_party_call_result['response_details']
        #####################################################################################

        timestamp_two = datetime.datetime.now()
        third_party_response['CallTime'] = dict(zip(['timestamp_one', 'timestamp_two','time_diff'],
                                                    [timestamp_one, timestamp_two,
                                                     (timestamp_two-timestamp_one).total_seconds()]))
        output_list.append(third_party_response)

        # Saving the results in the db
        third_party_response['CallDuration'] = third_party_response['CallTime']['time_diff']
        third_party_response['CallTime'] = str(third_party_response['CallTime']['timestamp_one'])
        insertion_params = dict(zip(['workflow_id', 'details'],
                                    [None, json.dumps(third_party_response)]))
        if 'workflow_id' in input_json:
            insertion_params['workflow_id'] = input_json['workflow_id']
            request.session['workflow_id'] = input_json['workflow_id']
       
        return output_list

    except Exception as ex:
        output_list=[dict(zip(["APIName", "endpoint_url", "Request", "Response", "CallTime"],
                              ["Karza PAN Validation method 1", "/v2/pan", None, f"Exception Encountered: {ex}", None]))]
        return output_list
