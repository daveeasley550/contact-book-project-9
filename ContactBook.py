from peewee import *

db = PostgresqlDatabase('contact', user= 'davideasley', password= '', host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    name = CharField()
    phone = CharField()
    email= CharField()

