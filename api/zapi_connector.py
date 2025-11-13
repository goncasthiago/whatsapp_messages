import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

ulr_base = str(os.environ.get("ZAPI_URL"))
id = os.environ.get("ZAPI_ID_DA_INSTANCIA")
token = os.environ.get("ZAPI_TOKEN")
client_token = os.environ.get("ZAPI_CLIENT_TOKEN")

class ZapiConnector:
    def __init__(self):
        self.zapi_url = ulr_base
        self.client_token = client_token

    def send_message(self, phone, message):
        payload = json.dumps({
            "phone": phone,
            "message": message,
            "delayMessage": 5,
            "delayTyping": 5
        })
        headers = {
            "Content-Type": "application/json",
            "Client-Token": self.client_token
        }
        try:
            response = requests.request("POST", self.zapi_url, headers=headers, data=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print("Error sending message:", e)
            return {"error": str(e)}
    
    def get_keys(self):
        return {
            "zapi_url": self.zapi_url,
            "client_token": self.client_token
        }
    
    