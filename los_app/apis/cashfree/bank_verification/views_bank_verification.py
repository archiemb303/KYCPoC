
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import random
import requests
from drf_spectacular.utils import extend_schema
# from los_app.apis.cashfree.bank_verification.documentation_bank_verification import *
import base64
import random
import requests
from django.conf import settings

cashfree_client_id = settings.CASHFREE_CLIENT_ID
cashfree_client_secret = settings.CASHFREE_CLIENT_SECRET

class BankVerification(APIView):

   
    @extend_schema(
        summary="Verify Bank Account Details",
        description="This endpoint verifies the bank account details using the account number, IFSC code, and account holder's name.",
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'bank_account': {
                        'type': 'string',
                        'description': 'Bank account number to be verified',
                        'example': '026291800001191'
                    },
                    'ifsc': {
                        'type': 'string',
                        'description': 'IFSC code of the bank branch',
                        'example': 'YESB0000262'
                    },
                    'name': {
                        'type': 'string',
                        'description': 'Name of the account holder',
                        'example': 'JOHN DOE'
                    },
                    'user_id': {
                        'type': 'string',
                        'description': 'Unique ID of the user',
                        'example': 'user123'
                    },
                    'phone': {
                        'type': 'string',
                        'description': 'Phone number associated with the account holder',
                        'example': '9876543210'
                    }
                },
                'required': ['bank_account', 'ifsc', 'name']
            }
        },
        responses={
            200: {
                'type': 'object',
                'properties': {
                    'status': {'type': 'string', 'example': 'SUCCESS', 'description': 'Status of the verification'},
                    'account_name': {'type': 'string', 'example': 'JOHN DOE', 'description': 'Name on the bank account'},
                    'bank_name': {'type': 'string', 'example': 'ICICI Bank', 'description': 'Name of the bank'},
                    'account_number': {'type': 'string', 'example': '016901649306', 'description': 'Bank account number'},
                    'ifsc': {'type': 'string', 'example': 'ICIC0000169', 'description': 'IFSC code of the bank'},
                    'valid': {'type': 'boolean', 'example': True, 'description': 'Validation status'},
                    'message': {'type': 'string', 'example': 'Bank account is valid', 'description': 'Message'},
                },
                'description': 'Output if API successfully verifies the bank account'
            },
            401: {
                'type': 'object',
                'properties': {
                    'Status': {'type': 'integer', 'example': 401, 'description': 'Status code of API output'},
                    'Message': {'type': 'string', 'example': 'Authentication failed', 'description': 'Description of API output status'},
                },
                'description': 'Output if authentication fails'
            },
            404: {
                'type': 'object',
                'properties': {
                    'Status': {'type': 'integer', 'example': 404, 'description': 'Status code of API output'},
                    'Message': {'type': 'string', 'example': 'Bank account not found', 'description': 'Description of API output status'},
                },
                'description': 'Output if bank account verification fails'
            }
        },
        tags=["Cashfree"]
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
            "x-client-id": cashfree_client_id,
            "x-client-secret":  cashfree_client_secret
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
