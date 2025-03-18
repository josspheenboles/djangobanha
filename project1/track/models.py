from django.db import models

# Create your models here.
class Track(models.Model):
    id=models.AutoField(primary_key=True)
    #charfiled,emailfiled,url--->max_length
    name=models.CharField(max_length=50,
                          null=False)

    @classmethod
    def getalltracks(cls):
        return cls.objects.all()

    @classmethod
    def gettrackbyid(cls,id):
        return cls.objects.get(id=id)
    def __str__(self):
        return self.name
