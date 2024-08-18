from drf_spectacular.utils import extend_schema, OpenApiExample
from drf_spectacular.types import OpenApiTypes

aadhaar_verification_schema = extend_schema(
    summary="Aadhaar Verification",
    description="""
        This function will verify the Aadhaar card details using the front image.
        **endpoint url:** baseurl/kyc/aadhaar_verification/
    """,
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
            'description': "Output if API successfully verifies the Aadhaar card",
        },
        401: {
            'type': 'object',
            'properties': {
                'Status': {'type': 'integer', 'example': 401},
                'Message': {'type': 'string', 'example': 'Authentication failed'},
            },
            'description': "Output if authentication fails",
            'examples': [
                OpenApiExample(
                    name="Authentication Failed",
                    value={"Status": 401, "Message": "Authentication failed"}
                )
            ]
        },
        404: {
            'type': 'object',
            'properties': {
                'Status': {'type': 'integer', 'example': 404},
                'Message': {'type': 'string', 'example': 'Aadhaar not found'},
            },
            'description': "Output if Aadhaar verification fails",
            'examples': [
                OpenApiExample(
                    name="Aadhaar Not Found",
                    value={"Status": 404, "Message": "Aadhaar not found"}
                )
            ]
        }
    },
    tags=["Aadhaar Verification"]
)
