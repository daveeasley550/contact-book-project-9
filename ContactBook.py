from peewee import CharField, IntegerField, Model, PostgresqlDatabase, TextField

db = PostgresqlDatabase('contact', user= 'davideasley', password= '', host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Contact(BaseModel):
    name = CharField()
    phone = CharField()
    email = CharField()


db.create_tables([Contact])

mom = Contact(name = 'Mom', phone = '1234567890', email = 'mom@mommail.com')
print(mom.name, mom.phone, mom.email)
mom.save()
