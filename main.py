import api
from time import sleep

supabase = api.DatabaseConnector()
zapi = api.ZapiConnector()

contacts_from_supabase = []

#Addind a new contacts
print("\n\nAdicionando novo contato...")
contacts = supabase.insert_contact("Thiago Debia", "+5511111111111", True)

print("\n\nAdicionando novo contato...")
contacts = supabase.insert_contact("Juliana", "+5511111111111", True)

print("\n\nAdicionando novo contato...")
contacts = supabase.insert_contact("Arthur", "+5511111111111", True)


# Get all contacts
contacts_from_supabase = supabase.get_contacts()
print("\n\nContatos após adição:")
print(contacts_from_supabase.data)  # Print the retrieved contacts data

# Get contact by name
#contacts_from_supabase = supabase.get_contact_by_name("Thiago Debia").data

# Send messages to all contacts
if contacts_from_supabase.data is None or len(contacts_from_supabase.data) == 0:
    print("Nenhum contato encontrado")
else:
    for contact in contacts_from_supabase.data:

        print(f"ID: {contact['id']}, Name: {contact['display_name']}, Phone: {contact['phone_number']}") # type: ignore 
        response = zapi.send_message( contact['phone_number'] , "Olá, esta é uma mensagem de teste enviada via ZapiConnector!") # type: ignore 
        print(f"Mensagem enviada para: {response}")
        sleep(2)




