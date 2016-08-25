import peewee as pw
import os
import datetime
import properties


myDB = pw.MySQLDatabase(properties.d["database"], host=os.getenv('IP', 'localhost'), 
    port=3306, user=properties.d["dbUser"], passwd=properties.d["dbPass"])

    
class BaseModel(pw.Model):
    class Meta:
        database=myDB
        
        
class User(BaseModel):
    username = pw.FixedCharField(max_length=255, unique=True)
    password = pw.CharField(max_length=255)
    createdDate = pw.DateTimeField(default=datetime.datetime.now)


class Scrape(BaseModel):
    uid = pw.ForeignKeyField(User)


# when you're ready to start querying, remember to connect
myDB.connect()
myDB.create_tables([User,Scrape], safe=True)