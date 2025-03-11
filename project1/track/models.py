from django.db import models

# Create your models here.
class Track(models.Model):
    id=models.AutoField(primary_key=True)
    #charfiled,emailfiled,url--->max_length
    name=models.CharField(max_length=50,
                          null=False,db_column='Name')

    @classmethod
    def getalltracks(cls):
        return cls.objects.all()