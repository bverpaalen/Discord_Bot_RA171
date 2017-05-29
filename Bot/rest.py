import requests
from requests.auth import HTTPDigestAuth
import json

def restCall(url):
    response = requests.get(url)
   
    if response.status_code == 200:
        dic = response.json()
        return dic
    else:
        print(response.status_code)
        return{}

