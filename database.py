import peewee as pw
import os
import datetime
import properties
from playhouse.pool import PooledMySQLDatabase

myDB = PooledMySQLDatabase(properties.d["database"], max_connections=32, stale_timeout=300, user=properties.d["dbUser"])

class User(pw.Model):
    username = pw.FixedCharField(max_length=255, primary_key=True)
    passwordHash = pw.CharField(max_length=512)
    createdDate = pw.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = myDB

# when you're ready to start querying, remember to connect
myDB.connect()
myDB.create_tables([User], safe=True)