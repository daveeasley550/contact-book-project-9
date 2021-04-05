from peewee import CharField, IntegerField, Model, PostgresqlDatabase, TextField

db = PostgresqlDatabase('contact', user='davideasley',
                        password='', host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone = CharField()
    email = CharField()


db.create_tables([Contact])

# mom = Contact(first_name = 'Mom', last_name = 'pascale', phone = '1234567890', email = 'mom@mommail.com').save()
# jen = Contact(first_name = 'Jen', last_name = 'easley', phone = '1134567890', email = 'jen@jenmail.com').save()

print("Hello, and welcome to your contacts")

want_all_answer = str(
    input('Would you like to see all of your contacts? y or n: ')).lower()

def all_contacts(want_all_answer):
    contacts = Contact.select()
    if want_all_answer == "y":
        for contact in contacts:
            print(f'Full Name: {contact.first_name} {contact.last_name}, Phone: {contact.phone}, Email: {contact.email}')
    else:
       search_contacts(contacts)

def search_contacts(contacts):
    search_answer = str(
        input('Would you like to search your contacts by name? y or n: ')).lower()
    if search_answer == 'y':
        search_name = str(
            input('Which first name would you like to search for?: ')).lower()
        result = contacts.select().where(Contact.first_name == search_name) 
        for contact in result:
            print(f'Full Name: {contact.first_name} {contact.last_name}, Phone: {contact.phone}, Email: {contact.email}')
    else:
      contact_add(contacts)

def contact_add(contacts):
    add_answer = str(input('Would you like to add a contact? y or n: ' )).lower()
    if add_answer == 'y':
        new_first_name = str(input('What is the new first name?: ' )).lower()
        new_last_name = str(input('What is the new last name?: ' )).lower()
        new_phone = str(input('What is the new phone number?: ' ))
        new_email = str(input('What is the new email address?: ' )).lower()
        new_contact = Contact(first_name = new_first_name, last_name= new_last_name, phone = new_phone, email = new_email ).save()
        for contact in contacts:
             print(f'Full Name: {contact.first_name} {contact.last_name}, Phone: {contact.phone}, Email: {contact.email}')

    else:
       delete_contact(contacts)


# def update_contacts(contacts):
#     update_question = str(input('Would you like to edit a contact? y or n: ')).lower()  
#     if update_question == 'y':
#         update_person = str(input('Which contact would you like to contact by first name?: '))
#         new_first_name = str(input('What is the new first name?: ' )).lower()
#         new_last_name = str(input('What is the new last name?: ' )).lower()
#         new_phone = str(input('What is the new phone number?: ' ))
#         new_email = str(input('What is the new email address?: ' )).lower()
#         result = contacts.where(Contact.first_name == update_person)
#         result = Contact.update(first_name = new_first_name, last_name= new_last_name, phone = new_phone, email = new_email )
#     else:
#       delete_contact(contacts)

def delete_contact(contacts):
    update_question = str(input('Would you like to delete a contact? y or n: ')).lower()  
    if update_question == 'y':
       update_person = str(input('Which contact would you like to delete by first name?: '))
       result = Contact.delete().where(Contact.first_name == update_person).execute()

    
 

all_contacts(want_all_answer)
