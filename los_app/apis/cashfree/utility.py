import requests

def create_token():
    url = "https://sandbox.cashfree.com/gc/authorize"

    headers = {
        "x-client-id": "CF10053789CR060QNPU07S7391HJSG",  
        "x-client-secret": "cfsk_ma_test_929e495f9601df900f1c6a7f7ea3a1cb_ac558e12", 
        "x-api-version": "2023-03-01", 
        "Content-Type": "application/json", 
    }

    response = requests.post(url, headers=headers)
    response  = response.json()
    print(response)
   
    if response['subCode'] == "200":
        access_token = response['data']['token']   
    else:
        access_token = None
    
    return access_token
