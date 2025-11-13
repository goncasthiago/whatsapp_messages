import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()
import api

zapi = api.ZapiConnector()

response = zapi.send_message("5511111111111", "Testando uma api do Whatsapp!!")
print(f"Response from ZapiConnector: {response}")




