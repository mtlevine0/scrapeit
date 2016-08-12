import peewee as pw
import os
import datetime
import properties

myDB = pw.MySQLDatabase(properties.d["database"], host=os.getenv('IP', 'localhost'), 
    port=3306, user=properties.d["dbUser"], passwd=properties.d["dbPass"])

class Image(pw.Model):
    fileName = pw.CharField(max_length=255)
    imageID = pw.FixedCharField(max_length=7, primary_key=True)
    createdDate = pw.DateTimeField(default=datetime.datetime.now)
    viewCount = pw.IntegerField(default=0)
    
    class Meta:
        database = myDB
        
class Album(pw.Model):
    albumName = pw.CharField(max_length=255)
    albumID = pw.FixedCharField(max_length=7, primary_key=True)
    createdDate = pw.DateTimeField(default=datetime.datetime.now)
    viewCount = pw.IntegerField(default=0)
    imageID = pw.ForeignKeyField(Image)
    
    class Meta:
        database = myDB


# when you're ready to start querying, remember to connect
myDB.connect()
myDB.create_tables([Image, Album], safe=True)