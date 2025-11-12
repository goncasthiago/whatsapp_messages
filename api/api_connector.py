import os
import json
from dotenv import load_dotenv
from supabase import create_client, Client
from supabase.client import ClientOptions
load_dotenv()

url = str(os.environ.get("SUPABASE_BASE_URL"))
key = str(os.environ.get("SUPABASE_API_KEY"))

class DatabaseConnector:
    def __init__(self):
        self.supabase: Client = create_client(
            url,
            key,
            options=ClientOptions(
                postgrest_client_timeout=10,
                storage_client_timeout=10,
                schema="public",
            )
        )

    def get_contacts(self):
        response = (
            self.supabase.table("contacts")
            .select("*")
            .execute()
        )
        return response
    
    def insert_contact(self, contact_name, phone_number, opt_in = True ):
        try:
            response = (
            self.supabase.table("contacts")
            .insert({"display_name": contact_name,
                     "phone_number": phone_number,
                     "opt_in": opt_in})
            .execute()
            
        )
        
        except Exception as e:
            err_info = e.args[0] if e.args else {"message": str(e)}
            '''response = {"key": err_info["key"],
                        "hint": err_info["hint"],
                        "code": err_info["code"],
                        "message": err_info["message"]}
            '''
            print("Erro ao inserir contato:", err_info)
            return err_info
        return response

    def get_contact_by_name(self, name):
        response = (
            self.supabase.table("contacts")
            .select("*")
            .eq("display_name", name)
            .execute()
        )
        return response




