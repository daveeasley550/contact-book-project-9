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

# mom = Contact(first_name = 'mom', last_name = 'pascale', phone = '1234567890', email = 'mom@mommail.com').save()
# jen = Contact(first_name = 'jen', last_name = 'easley', phone = '1134567890', email = 'jen@jenmail.com').save()
# sam = Contact(first_name = 'sam', last_name = 'waka', phone = '1134567890', email = 'sam@sammail.com').save()
# jen = Contact(first_name = 'jerk', last_name = 'face', phone = '1134567890', email = 'jerk@facemail.com').save()
# jen = Contact(first_name = 'lil', last_name = 'dicky', phone = '1134567890', email = 'hiImDave@lildicky.com').save()

def contact_Book():
    print("Hello, and welcome to your contacts! please choose from the following... \n 1: Show all Contacts \n 2: Search for a Contact \n 3: Add a contact \n 4: Delete a contact \n 5: Update a contact \n 6: Quit")
    choice = int(input('Enter Number: '))
    if choice == 1:
        all_contacts()
    elif choice == 2:
        search_contacts()
    elif choice == 3:
        contact_add()
    elif choice == 4:
        delete_contact()
    elif choice == 5:
        update_contacts()
    

def all_contacts():
    contacts = Contact.select()
    for contact in contacts:
            print(f'Full Name: {contact.first_name} {contact.last_name}, Phone: {contact.phone}, Email: {contact.email}')
    
    
    contact_Book()

def search_contacts():
        search_name = str(
            input('Which first name would you like to search for?: '))
        result = Contact.select().where(Contact.first_name == search_name) 
        for contact in result:
            print(f'Full Name: {contact.first_name} {contact.last_name}, Phone: {contact.phone}, Email: {contact.email}')
        contact_Book()

def contact_add():
        new_first_name = str(input('What is the new first name?: ' )).lower()
        new_last_name = str(input('What is the new last name?: ' )).lower()
        new_phone = str(input('What is the new phone number?: ' ))
        new_email = str(input('What is the new email address?: ' )).lower()
        new_contact = Contact(first_name = new_first_name, last_name= new_last_name, phone = new_phone, email = new_email ).save()
        for contact in Contact:
             print(f'Full Name: {contact.first_name} {contact.last_name}, Phone: {contact.phone}, Email: {contact.email}')
        contact_Book()


def update_contacts():
        update_person = str(input('Which contact would you like to edit by first name?: '))
        new_first_name = str(input('What is the new first name?: ' )).lower()
        new_last_name = str(input('What is the new last name?: ' )).lower()
        new_phone = str(input('What is the new phone number?: ' ))
        new_email = str(input('What is the new email address?: ' )).lower()
        result = Contact.update(first_name = new_first_name, last_name= new_last_name, phone = new_phone, email = new_email ).where(Contact.first_name == update_person).execute()
        for contact in Contact:
            print(f'Full Name: {contact.first_name} {contact.last_name}, Phone: {contact.phone}, Email: {contact.email}')
        contact_Book()
  

def delete_contact():
       update_person = str(input('Which contact would you like to delete by first name?: '))
       result = Contact.delete().where(Contact.first_name == update_person).execute()
       print(f"Deleted: {update_person}")
       contact_Book()
 

contact_Book()