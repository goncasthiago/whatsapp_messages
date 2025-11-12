import api

api = api.DatabaseConnector()

# Get all contacts
contacts = api.get_contacts()
print(f"Todos os contatos {contacts.data}")  # Print the retrieved contacts data

#Add a new contact
print("\n\nAdicionando novo contato...")
contacts = api.insert_contact("Thiago Debia", "+5511111111111", True)

# Get all contacts
contacts = api.get_contacts()
print("\n\nContatos após adição:")
print(contacts.data)  # Print the retrieved contacts data

contacts = api.get_contact_by_name("Thiago Debia")
print("\n\nContato buscado pelo nome 'Thiago Debia':")
print(contacts.data)  # Print the retrieved contacts data



