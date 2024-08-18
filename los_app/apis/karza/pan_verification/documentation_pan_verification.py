from drf_yasg import openapi


SAMPLE_INPUT = {
    "pan_yes": "Y",
    "pan_number": "ABCDE1234F"
   
}

SAMPLE_RESPONSE_SUCCESS = {
    "APIName": "Karza PAN Validation",
    "endpoint_url": "/v2/pan",
    "Request": "{\"consent\": \"Y\", \"pan\": \"ABCDE1234F\"}",
    "Response": "{\"result\":{\"pan\":\"ABCDE1234F\",\"name\":\"John Doe\",\"panStatus\":\"Valid\",\"dob\":\"1980-01-01\",\"message\":\"Verification Successful\",\"status_code\":\"101\"}}",
    "CallTime": "2024-08-18 12:34:56.789012",
    "CallDuration": 1.234567
}

OPERATIONS_DESCRIPTION = """ 
This function will call a 3rd party API to validate the PAN number and return the verification status.
**endpoint url:** baseurl/v2/pan/
"""

INPUT_PROPERTIES_DESCRIPTION = {
    "pan_yes": openapi.Schema(
        type=openapi.TYPE_STRING,
        description="User consent for PAN verification",
        example="Y"
    ),
    "pan_number": openapi.Schema(
        type=openapi.TYPE_STRING,
        description="PAN number to be verified",
        example="ABCDE1234F"
    )
   
}

REQUIRED_LIST = ['pan_yes', 'pan_number']

RESPONSE_DESCRIPTION = {
    '200': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description='Output if API successfully verifies the PAN number',
        properties={
            "APIName": openapi.Schema(type=openapi.TYPE_STRING, description="Name of the API", example="Karza PAN Validation"),
            "endpoint_url": openapi.Schema(type=openapi.TYPE_STRING, description="Endpoint URL", example="/v2/pan"),
            "Request": openapi.Schema(type=openapi.TYPE_STRING, description="Request sent to the API", example="{\"consent\": \"Y\", \"pan\": \"ABCDE1234F\"}"),
            "Response": openapi.Schema(type=openapi.TYPE_STRING, description="Response from the API", example="{\"result\":{\"pan\":\"ABCDE1234F\",\"name\":\"John Doe\",\"panStatus\":\"Valid\",\"dob\":\"1980-01-01\",\"message\":\"Verification Successful\",\"status_code\":\"101\"}}"),
            "CallTime": openapi.Schema(type=openapi.TYPE_STRING, description="Time of the API call", example="2024-08-18 12:34:56.789012"),
            "CallDuration": openapi.Schema(type=openapi.TYPE_NUMBER, description="Duration of the API call in seconds", example=1.234567)
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
        description='Output if PAN verification fails',
        properties={
            "Status": openapi.Schema(type=openapi.TYPE_INTEGER, description="Status code of API output", example=404),
            "Message": openapi.Schema(type=openapi.TYPE_STRING, description="Description of API output status", example="PAN not found")
        }
    )
}

API_LOGIC = """ 
Step 1: Validate the access token.
Step 2: Send the PAN number and consent to the 3rd party API.
Step 3: Capture and store the response from the 3rd party API.
Step 4: Return the PAN verification status and details.
"""

# ################ Swagger Descriptions End here  #####################
