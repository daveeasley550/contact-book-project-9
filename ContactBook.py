from peewee import CharField, IntegerField, Model, PostgresqlDatabase, TextField

db = PostgresqlDatabase('contact', user='davideasley',
                        password='', host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Contact(BaseModel):
    name = CharField()
    phone = CharField()
    email = CharField()


db.create_tables([Contact])

# mom = Contact(name = 'Mom', phone = '1234567890', email = 'mom@mommail.com').save()
# jen = Contact(name = 'Jen', phone = '1134567890', email = 'jen@jenmail.com').save()

# print(mom.name, mom.phone, mom.email)


print("Hello, and welcome to your contacts")

want_all_answer = str(
    input('Would you like to see all of your contacts? y or n: ')).lower()
# search_answer = str(input('Would you like to search your contacts by name? y or n: ' )).lower()
# search_name = str(input('Which name would you like to search for?: ' )).lower()


def all_contacts(want_all_answer):
    contacts = Contact.select()
    if want_all_answer == "y":
        for contact in contacts:
            print(f'{contact.name}, {contact.phone}, {contact.email}')
    else:
       search_contacts(contacts)


def search_contacts(contacts):
    search_answer = str(
        input('Would you like to search your contacts by name? y or n: ')).lower()
    if search_answer == 'y':
        search_name = str(
            input('Which name would you like to search for?: ')).lower()
        result = contacts.where(Contact.name== search_name) ##doesn't work right
        print(result)
    else:
      contact_add(contacts)

def contact_add(contacts):
    add_answer = str(input('Would you like to add a contact? y or n: ' )).lower()
    if add_answer == 'y':
        new_name = str(input('What is the new name?: ' )).lower()
        new_phone = str(input('What is the new phone number?: ' ))
        new_email = str(input('What is the new email address?: ' )).lower()
        new_name = Contact(name = new_name, phone = new_phone, email = new_email ).save()
# mom = Contact(name = 'Mom', phone = '1234567890', email = 'mom@mommail.com').save()


# def update_contacts(contacts):
#     update_question = str(input('Would you like to edit a contact? y or n: ')).lower()  
#     if update_question == 'y':
#         update_person = str(input('Which contact would you like to contact by name?: '))
#         new_name = str(input('What is the new name?: '))
#         new_phone = str(input('What is the new phone number?: '))
#         new_email = str(input('What is the new email?: '))




all_contacts(want_all_answer)
