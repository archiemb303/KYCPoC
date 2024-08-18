from drf_yasg import openapi

# Sample Input Structure
SAMPLE_INPUT = {
    "bank_account": "026291800001191",
    "ifsc": "YESB0000262",
    "name": "JOHN DOE",
    "user_id": "user123",
    "phone": "9876543210"
}

# Sample Success Response
SAMPLE_RESPONSE_SUCCESS = {
    "status": "SUCCESS",
    "account_name": "JOHN DOE",
    "bank_name": "ICICI Bank",
    "account_number": "016901649306",
    "ifsc": "ICIC0000169",
    "valid": True,
    "message": "Bank account is valid"
}

# Description of the API Operation
OPERATIONS_DESCRIPTION = """ 
This function verifies the bank account details using the account number, IFSC code, and account holder's name.
**endpoint url:** baseurl/verification/bank-account/async
"""

# Input Properties Description
INPUT_PROPERTIES_DESCRIPTION = {
    "bank_account": openapi.Schema(
        type=openapi.TYPE_STRING,
        description="Bank account number to be verified",
        example="026291800001191",
    ),
    "ifsc": openapi.Schema(
        type=openapi.TYPE_STRING,
        description="IFSC code of the bank branch",
        example="YESB0000262",
    ),
    "name": openapi.Schema(
        type=openapi.TYPE_STRING,
        description="Name of the account holder",
        example="JOHN DOE",
    ),
    "user_id": openapi.Schema(
        type=openapi.TYPE_STRING,
        description="Unique ID of the user",
        example="user123",
    ),
    "phone": openapi.Schema(
        type=openapi.TYPE_STRING,
        description="Phone number associated with the account holder",
        example="9876543210",
    ),
}

# Required Fields List
REQUIRED_LIST = ['bank_account', 'ifsc', 'name']

# Response Description
RESPONSE_DESCRIPTION = {
    '200': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description='Output if API successfully verifies the bank account',
        properties={
            "status": openapi.Schema(type=openapi.TYPE_STRING, description="Status of the verification", example="SUCCESS"),
            "account_name": openapi.Schema(type=openapi.TYPE_STRING, description="Name on the bank account", example="JOHN DOE"),
            "bank_name": openapi.Schema(type=openapi.TYPE_STRING, description="Name of the bank", example="ICICI Bank"),
            "account_number": openapi.Schema(type=openapi.TYPE_STRING, description="Bank account number", example="016901649306"),
            "ifsc": openapi.Schema(type=openapi.TYPE_STRING, description="IFSC code of the bank", example="ICIC0000169"),
            "valid": openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Validation status", example=True),
            "message": openapi.Schema(type=openapi.TYPE_STRING, description="Message", example="Bank account is valid"),
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
        description='Output if bank account verification fails',
        properties={
            "Status": openapi.Schema(type=openapi.TYPE_INTEGER, description="Status code of API output", example=404),
            "Message": openapi.Schema(type=openapi.TYPE_STRING, description="Description of API output status", example="Bank account not found")
        }
    )
}

# API Logic Description
API_LOGIC = """ 
Step 1: Validate the access token.
Step 2: Send the bank account details (account number, IFSC, and name) for verification.
Step 3: Return the verification status and details, including the name of the account holder and the bank.
"""
