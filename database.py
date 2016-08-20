import peewee as pw
import os
import datetime
import properties

myDB = pw.MySQLDatabase(properties.d["database"], host=os.getenv('IP', 'localhost'), 
    port=3306, user=properties.d["dbUser"], passwd=properties.d["dbPass"])

class User(pw.Model):
    username = pw.FixedCharField(max_length=255, primary_key=True)
    password = pw.CharField(max_length=255)
    createdDate = pw.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = myDB


# when you're ready to start querying, remember to connect
myDB.connect()
myDB.create_tables([User], safe=True)