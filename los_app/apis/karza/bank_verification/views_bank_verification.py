import datetime
import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from los_app.apis.karza.creds import get_cred
from los_app.apis.karza.bank_verification.documentation_bank_verification import *
from drf_yasg.utils import swagger_auto_schema

from los_app.apis.karza.creds import KarzaKeys


# Swagger
from drf_yasg.utils import swagger_auto_schema

# @permission_classes([AllowAny])
class BankVerificationAPI(APIView):

    @swagger_auto_schema(
        tags=["Karza"],
        manual_parameters=[openapi.Parameter('access_token', openapi.IN_HEADER, description="Access token for authentication", type=openapi.TYPE_STRING)],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=REQUIRED_LIST,
            properties=INPUT_PROPERTIES_DESCRIPTION
        ),
        operation_description=OPERATIONS_DESCRIPTION,
        responses=RESPONSE_DESCRIPTION
    )

    def post(self, request):
        """
        This function will call the 3rd party api, store the data, and redirect user to workflow details page
        :param request:
        :return:
        """
        input_json = request.data
        output_json = views_bank_verification_json(request, input_json)
        return Response(output_json)


def views_bank_verification_json(request, input_params):
    try:
        input_json, output_list = input_params, []
        cred = get_cred()
        input_json['token_secret_key_1'] = cred['token_secret_key_1']
        input_json['token_secret_key_2'] = cred['token_secret_key_2']
       
  
        api_name_var = "Bank AC Verification"
        endpoint_url_var = "/v2/bankacc"
        keys_obj = KarzaKeys()
        # access_token = generate_access_token(key_gen_var)
        # For every API Calling style initiate the params accordingly
        third_party_response = dict(zip(["APIName", "endpoint_url", "Request", "Response", "CallTime"],
                                        [api_name_var, endpoint_url_var, None, None, None]))
        timestamp_one = datetime.datetime.now()

        #####################################################################################
        # Call the third party API here
        call_params = dict(zip(["api_endpoint_url", "payload"],
                               [endpoint_url_var, None]))
        call_params['payload'] = dict(zip(["consent", "ifsc", "accountNumber"],
                                          [input_json['consent'], input_json['ifsc'], input_json['accountNumber']]))
        third_party_call_result = keys_obj.make_api_call(call_params)

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

     

        return output_list

    except Exception as ex:
        output_list=[dict(zip(["APIName", "endpoint_url", "Request", "Response", "CallTime"],
                              ["Bank AC Verification", "/v2/bankacc", None, f"Exception Encountered: {ex}", None]))]
        return output_list
