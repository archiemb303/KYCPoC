"""
url:'http://sarcipilot-env2.eba-gabcd68p.ap-south-1.elasticbeanstalk.com/kyc/bank_account_verification/'
Request Body:

{
  "consent": "Y",
  "ifsc": "ICIC0000169",
  "accountNumber": "016901649306",
  "refreshtoken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYXNkZmxqc2RmbGtnaHQ0dWtmZ2tsamRmaHNnZGZnaGtsbnNkZmdlaHdma2phc3VkZiIsImV4cCI6MTY1MjM2OTE5NywiaWF0IjoxNjUyMjgyNzk3fQ.OfWd1V9JLS1WMa-eETZ5cx5uoHtBbC5pF1IdB4Uv_eo"
}

Response:
[
    {
        "APIName": "Bank AC Verification",
        "endpoint_url": "/v2/bankacc",
        "Request": "{\"consent\": \"Y\", \"ifsc\": \"ICIC0000169\", \"accountNumber\": \"016901649306\"}",
        "Response": "{\"result\":{\"accountNumber\":\"016901649306\",\"ifsc\":\"ICIC0000169\",\"accountName\":\"ASFAHAN M MULLA\",\"bankResponse\":\"Transaction Successful\",\"bankTxnStatus\":true},\"request_id\":\"782062b5-4d21-4078-a7f4-72cf594c760d\",\"status-code\":\"101\"}",
        "CallTime": "2022-05-11 16:38:06.678553",
        "CallDuration": 2.716971
    },
    {
        "Status": 200,
        "Message": "User logged in successfully",
        "Payload": {
            "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYXNkZmxqc2RmbGtnaHQ0dWtmZ2tsamRmaHNnZGZnaGtsbnNkZmdlaHdma2phc3VkZiIsImV4cCI6MTY1MjI4NDY4NiwiaWF0IjoxNjUyMjgzNDg2fQ.uP4vjrybQUteDCWe5RtJUloA6Nyp9tVM3-R6Vld5f2Y",
            "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYXNkZmxqc2RmbGtnaHQ0dWtmZ2tsamRmaHNnZGZnaGtsbnNkZmdlaHdma2phc3VkZiIsImV4cCI6MTY1MjM2OTg4NiwiaWF0IjoxNjUyMjgzNDg2fQ.tfiMcapItsb6n6265pMEb5e6Ov-wIJWnMr1Ox1m1tBw"
        }
    }
]
"""