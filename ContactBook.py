from peewee import *

db = PostgresqlDatabase('contact', user= 'davideasley', password= '', host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    name = CharField()
    phone = IntegerField()
    email= CharField()

db.create_tables([Contact])

mom = Contact.get(Contact.name == "Mom", Contact.phone == "5551111234", Contact.email == "mom@mommail.com")
print(mom.name, mom.phone, mom.email)
mom.save()
