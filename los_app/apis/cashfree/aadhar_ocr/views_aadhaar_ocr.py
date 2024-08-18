
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import random
import requests
from drf_yasg.utils import swagger_auto_schema
# from los_app.apis.cashfree.aadhar_ocr.documentation_aadhaar_ocr import aadhaar_verification_schema
import base64
import random
import requests
import tempfile
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse, OpenApiExample

from django.conf import settings

cashfree_client_id = settings.CASHFREE_CLIENT_ID
cashfree_client_secret = settings.CASHFREE_CLIENT_SECRET


class AadhaarOcr(APIView):

   
    @extend_schema(
        summary="Verify Aadhaar Card",
        description="This endpoint verifies the Aadhaar card details using the front image.",
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'aadhaar_front_image': {
                        'type': 'string',
                        'description': 'Base64 encoded front image of the Aadhaar card',
                        'example': 'aadhaar_front_image_base64_string'
                    }
                },
                'required': ['aadhaar_front_image']
            }
        },
        responses={
            200: {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'JOHN DOE'},
                    'yob': {'type': 'string', 'example': '1997'},
                    'gender': {'type': 'string', 'example': 'Male'},
                    'uid': {'type': 'string', 'example': 'XXXX-XXXX-3717'},
                    'valid': {'type': 'boolean', 'example': True},
                    'status': {'type': 'string', 'example': 'VALID'},
                    'reference_id': {'type': 'string', 'example': '11749'},
                    'verification_id': {'type': 'string', 'example': '397204'},
                    'message': {'type': 'string', 'example': 'Aadhaar card is valid'},
                },
                'description': 'Output if API successfully verifies the Aadhaar card'
            },
            401: {
                'type': 'object',
                'properties': {
                    'Status': {'type': 'integer', 'example': 401},
                    'Message': {'type': 'string', 'example': 'Authentication failed'},
                },
                'description': 'Output if authentication fails'
            },
            404: {
                'type': 'object',
                'properties': {
                    'Status': {'type': 'integer', 'example': 404},
                    'Message': {'type': 'string', 'example': 'Aadhaar not found'},
                },
                'description': 'Output if Aadhaar verification fails'
            }
        },
        tags=["Cashfree"]
    )
    def post(self, request):
        """
        This function will call the 3rd party api,
        """
        input_json = request.data
        output_json = views_aadhar_orc_json(request, input_json)
        return Response(output_json)


def views_aadhar_orc_json(request, input_params):
    try:
        input_json, output_list = input_params, []
        api_name_var = "Cashfree Aadhar OCR"
        full_url = "https://sandbox.cashfree.com/verification/document/aadhaar"

        front_image_base64 = input_json.get("aadhaar_front_image", None)
        
        if front_image_base64:
            front_image_data = base64.b64decode(front_image_base64)
            with tempfile.NamedTemporaryFile(delete=False) as temp_front_file:
                temp_front_file.write(front_image_data)
                temp_front_file_path = temp_front_file.name
        
        # The verification ID to be sent
        random_verification_id = random.randint(100000, 999999)
        verification_id = str(random_verification_id)

        # Prepare the files and data
        files = {
            "front_image": open(temp_front_file_path, "rb"), 
        }
        data = {
            "verification_id": verification_id,
        }

        # Headers
        headers = {
            "accept": "application/json",
            "x-client-id": cashfree_client_id,
            "x-client-secret":  cashfree_client_secret
        }

        # Sending the request
        response = requests.post(full_url, files=files, data=data, headers=headers)
        response = response.json()

        output_list=[dict(zip(["APIName", "Response", "Message"],
                              [api_name_var, response, "Success"]))]

     
        return output_list

    except Exception as ex:
        output_list=[dict(zip(["APIName", "endpoint_url", "Request", "Response", "CallTime"],
                              [api_name_var, "", None, f"Exception Encountered: {ex}", None]))]
        return output_list
