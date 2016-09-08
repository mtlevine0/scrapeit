import datetime

import peewee as pw
from playhouse.pool import PooledMySQLDatabase
import bcrypt

import properties

myDB = PooledMySQLDatabase(properties.d["database"], max_connections=32, stale_timeout=300, user=properties.d["dbUser"], password=properties.d["dbPass"])

class BaseModel(pw.Model):
    class Meta:
        database=myDB

class User(BaseModel):
    username = pw.CharField(max_length=255)
    email = pw.CharField(max_length=512)
    passwordHash = pw.CharField(max_length=512)
    createdDate = pw.DateTimeField(default=datetime.datetime.now)
    active = pw.BooleanField(default=True)
    
    @classmethod    
    def _hashPassword(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
    @classmethod
    def add(self, username, password, email):
        return self.create(username=username, passwordHash=self._hashPassword(password), email=email)

    def checkPassword(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.passwordHash.encode('utf-8'))


class Scrape(BaseModel):
    uid = pw.ForeignKeyField(User)
    name = pw.CharField(max_length=255, default="New Scrape")
    
    @classmethod
    def add(self, uid, name):
        return self.create(uid=uid, name=name)
        
class Item(BaseModel):
    sid = pw.ForeignKeyField(Scrape)
    item_classification = pw.CharField(max_length=255)
    price = pw.CharField(max_length=255)
    url = pw.CharField(max_length=255)
    idhash = pw.CharField(max_length=255)
    create_date = pw.DateTimeField(default=datetime.datetime.now)#change this to be when it was posted
    

# when you're ready to start querying, remember to connect
myDB.connect()
#REMOVE WHEN PUSHED TO PRODUCTION
try:
    myDB.drop_table(Scrape)
except:
    pass
myDB.create_tables([User,Scrape,Item], safe=True)