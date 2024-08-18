
from drf_yasg import openapi

# Swagger Descriptions start here
HEADER_PARAMS = {
    'access_token': openapi.Parameter('access_token', openapi.IN_HEADER, description="Access token for authentication", type=openapi.TYPE_STRING),
}

SAMPLE_INPUT = {
    "consent": "Y",
    "ifsc": "ICIC0000169",
    "accountNumber": "016901649306",
}

SAMPLE_RESPONSE_SUCCESS = {
    "result": {
        "accountNumber": "016901649306",
        "ifsc": "ICIC0000169",
        "accountName": "ASFAHAN M MULLA",
        "bankResponse": "Transaction Successful",
        "bankTxnStatus": True
    },
    "request_id": "782062b5-4d21-4078-a7f4-72cf594c760d",
    "status_code": "101"
}

OPERATIONS_DESCRIPTION = """ 
This function will verify the bank account details and return the verification status.
**endpoint url:** baseurl/kyc/bank_account_verification/
"""

INPUT_PROPERTIES_DESCRIPTION = {
    "consent": openapi.Schema(
        type=openapi.TYPE_STRING,
        description="User consent for bank account verification",
        example="Y"
    ),
    "ifsc": openapi.Schema(
        type=openapi.TYPE_STRING,
        description="IFSC code of the bank",
        example="ICIC0000169"
    ),
    "accountNumber": openapi.Schema(
        type=openapi.TYPE_STRING,
        description="Bank account number",
        example="016901649306"
    )
  
}

REQUIRED_LIST = ['consent', 'ifsc', 'accountNumber']

RESPONSE_DESCRIPTION = {
    '200': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description='Output if API successfully verifies the bank account',
        properties={
            "APIName": openapi.Schema(type=openapi.TYPE_STRING, description="Name of the API", example="Bank AC Verification"),
            "endpoint_url": openapi.Schema(type=openapi.TYPE_STRING, description="Endpoint URL", example="/v2/bankacc"),
            "Request": openapi.Schema(type=openapi.TYPE_STRING, description="Request sent to the API", example="{\"consent\": \"Y\", \"ifsc\": \"ICIC0000169\", \"accountNumber\": \"016901649306\"}"),
            "Response": openapi.Schema(type=openapi.TYPE_STRING, description="Response from the API", example="{\"result\":{\"accountNumber\":\"016901649306\",\"ifsc\":\"ICIC0000169\",\"accountName\":\"ASFAHAN M MULLA\",\"bankResponse\":\"Transaction Successful\",\"bankTxnStatus\":true},\"request_id\":\"782062b5-4d21-4078-a7f4-72cf594c760d\",\"status-code\":\"101\"}"),
            "CallTime": openapi.Schema(type=openapi.TYPE_STRING, description="Time of the API call", example="2022-05-11 16:38:06.678553"),
            "CallDuration": openapi.Schema(type=openapi.TYPE_NUMBER, description="Duration of the API call in seconds", example=2.716971)
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
        description='Output if account verification fails',
        properties={
            "Status": openapi.Schema(type=openapi.TYPE_INTEGER, description="Status code of API output", example=404),
            "Message": openapi.Schema(type=openapi.TYPE_STRING, description="Description of API output status", example="Bank account not found")
        }
    )
}

API_LOGIC = """ 
Step 1: Validate the access token and refresh token.
Step 2: Fetch the account details using the IFSC code and account number.
Step 3: Verify the account details with the bank.
Step 4: Return the verification status and details.
"""

# ################ Swagger Descriptions End here  #####################
