
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import random
import requests
from drf_yasg.utils import swagger_auto_schema
from los_app.apis.cashfree.bank_verification.documentation_bank_verification import *
import base64
import random
import requests
from los_app.apis.cashfree.utility import create_token



class BankVerification(APIView):

    @swagger_auto_schema(
        tags=["Cashfree"],
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
        This function will call the 3rd party api,
        """
        input_json = request.data
        output_json = Views_bank_verification_json(request, input_json)
        return Response(output_json)


def Views_bank_verification_json(request, input_params):
    try:
        input_json, output_list = input_params, []
        api_name_var = "Cashfree Bank Verification "

        name = input_json.get("name", None)
        phone = input_json.get("phone", None)
        bank_account = input_json.get("bank_account", None)
        ifsc = input_json.get("ifsc", None)
        user_id = input_json.get("user_id", None)

            
        url = "https://sandbox.cashfree.com/verification/bank-account/sync"

        payload = {
            "bank_account": bank_account,
            "ifsc":ifsc,
            "name": name,
            "phone": phone
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "x-client-id": "CF10053789CR060QNPU07S7391HJSG",
            "x-client-secret": "cfsk_ma_test_929e495f9601df900f1c6a7f7ea3a1cb_ac558e12"
        }

        response = requests.post(url, json=payload, headers=headers)

        response = response.json()

        output_list=[dict(zip(["APIName", "Response", "Message"],
                              [api_name_var, response, "Success"]))]

        return output_list

    except Exception as ex:
        output_list=[dict(zip(["APIName", "endpoint_url", "Request", "Response", "CallTime"],
                              [api_name_var, "", None, f"Exception Encountered: {ex}", None]))]
        return output_list
