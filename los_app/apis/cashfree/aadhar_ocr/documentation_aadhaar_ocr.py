from drf_yasg import openapi

SAMPLE_INPUT = {
    "aadhaar_front_image": "aadhaar_front.jpg",  # Front image is required
}

SAMPLE_RESPONSE_SUCCESS = {
    "name": "JOHN DOE",
    "yob": "1997",
    "gender": "Male",
    "uid": "XXXX-XXXX-3717",
    "valid": True,
    "status": "VALID",
    "reference_id": "11749",
    "verification_id": "397204",
    "message": "Aadhaar card is valid"
}

OPERATIONS_DESCRIPTION = """ 
This function will verify the Aadhaar card details using the front image.
**endpoint url:** baseurl/kyc/aadhaar_verification/
"""

INPUT_PROPERTIES_DESCRIPTION = {
    "aadhaar_front_image": openapi.Schema(
        type=openapi.TYPE_STRING,
        description="Base64 encoded front image of the Aadhaar card",
        example="aadhaar_front_image_base64_string",
    ),
}

REQUIRED_LIST = ['aadhaar_front_image']

RESPONSE_DESCRIPTION = {
    '200': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description='Output if API successfully verifies the Aadhaar card',
        properties={
            "name": openapi.Schema(type=openapi.TYPE_STRING, description="Name on the Aadhaar card", example="JOHN DOE"),
            "yob": openapi.Schema(type=openapi.TYPE_STRING, description="Year of Birth", example="1997"),
            "gender": openapi.Schema(type=openapi.TYPE_STRING, description="Gender", example="Male"),
            "uid": openapi.Schema(type=openapi.TYPE_STRING, description="Masked Aadhaar Number", example="XXXX-XXXX-3717"),
            "valid": openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Validation Status", example=True),
            "status": openapi.Schema(type=openapi.TYPE_STRING, description="Verification Status", example="VALID"),
            "reference_id": openapi.Schema(type=openapi.TYPE_STRING, description="Reference ID", example="11749"),
            "verification_id": openapi.Schema(type=openapi.TYPE_STRING, description="Verification ID", example="397204"),
            "message": openapi.Schema(type=openapi.TYPE_STRING, description="Message", example="Aadhaar card is valid"),
        }
    ),
    '401': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description='Output if authentication fails',
        properties={
            "Status": openapi.Schema(type=openapi.TYPE_INTEGER, description="Status code of API output", example=401),
            "Message": openapi.Schema(type=openapi.TYPE_STRING, description="Description of API output status", example="Authentication failed")
        }
    ),
    '404': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description='Output if Aadhaar verification fails',
        properties={
            "Status": openapi.Schema(type=openapi.TYPE_INTEGER, description="Status code of API output", example=404),
            "Message": openapi.Schema(type=openapi.TYPE_STRING, description="Description of API output status", example="Aadhaar not found")
        }
    )
}

API_LOGIC = """ 
Step 1: Validate the access token.
Step 2: Send the Aadhaar front image for OCR verification.
Step 3: Return the verification status and details.
"""
