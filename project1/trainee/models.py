from django.db import models
from track.models import Track


# Create your models here.
class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)
    email=models.EmailField(unique=True)
    createdate=models.DateField(auto_now_add=True)
    # stor path in db & file in media
    image = models.ImageField(upload_to='trainee/imgs',null=True)
    Active=models.BooleanField(default=True)
    #fk to track model note --->object of track
    track=models.ForeignKey(to=Track,on_delete=models.CASCADE)

    @classmethod
    def getalltrainee(cls):
        return  cls.objects.filter(Active=True)
    @classmethod
    def gettraineebyid(cls,id):
        return cls.objects.get(id=id)