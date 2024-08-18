
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import random
import requests
from drf_yasg.utils import swagger_auto_schema
from los_app.apis.cashfree.aadhar_ocr.documentation_aadhaar_ocr import *
import base64
import random
import requests
import tempfile



class AadhaarOcr(APIView):

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
            "x-client-id": "CF10053789CR060QNPU07S7391HJSG",
            "x-client-secret": "cfsk_ma_test_929e495f9601df900f1c6a7f7ea3a1cb_ac558e12"
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
