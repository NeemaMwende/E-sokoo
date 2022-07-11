 
from codecs import strict_errors
from urllib import response
import requests
from requests.auth import HTTPBasicAuth
import json

def authenticate():
    key='ua6RLa25pVCa1AqllNdDdbLtrGsfoHt7'
    secret='qvaHDqLe4lMT5Qwn'

    api_sandbox_url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    # get request
    mpesa_response = requests.get(api_sandbox_url , auth=HTTPBasicAuth(key, secret))
    # retrieving text message
    str_response = mpesa_response.text

    # convert to dictionary
    dictionary_response = json.loads(str_response)

    # return
    return dictionary_response['access_token']






# url = ""

# querystring = {"grant_type":"client_credentials"}
# payload = ""
# headers = {
#     "Authorization": "Basic SWZPREdqdkdYM0FjWkFTcTdSa1RWZ2FTSklNY001RGQ6WUp4ZVcxMTZaV0dGNFIzaA=="
# }
# response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
# print(response.text)