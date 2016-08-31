import datetime

import peewee as pw
from playhouse.pool import PooledMySQLDatabase
import bcrypt

import properties

myDB = PooledMySQLDatabase(properties.d["database"], max_connections=32, stale_timeout=300, user=properties.d["dbUser"])

class User(pw.Model):
    username = pw.CharField(max_length=255, primary_key=True)
    email = pw.CharField(max_length=512)
    passwordHash = pw.CharField(max_length=512)
    createdDate = pw.DateTimeField(default=datetime.datetime.now)
    active = pw.BooleanField(default=True)
    
    @classmethod    
    def _hashPassword(self, password):
        return bcrypt.hashpw(password, bcrypt.gensalt())
        
    @classmethod
    def add(self, username, password, email):
        return self.create(username=username, passwordHash=self._hashPassword(password), email=email)

    def checkPassword(self, password):
        return bcrypt.checkpw(password, self.passwordHash)

    class Meta:
        database = myDB

# when you're ready to start querying, remember to connect
myDB.connect()
myDB.create_tables([User], safe=True)