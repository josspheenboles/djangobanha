from django.db import models
from track.models import Track
from django.shortcuts import redirect
from django.urls import reverse_lazy
# accsess class method or cerate object
# Create your models here.
class Trainee(models.Model):
    id=models.AutoField(primary_key=True)#not appear
    name=models.CharField(max_length=100,null=False)#charfile max100 required
    email=models.EmailField(unique=True)#email files
    createdate=models.DateField(auto_now_add=True)
    # stor path in db & file in media
    image = models.ImageField(upload_to='trainee/imgs',null=True)#filefiled
    Active=models.BooleanField(default=True)
    #fk to track model note --->object of track
    track=models.ForeignKey(to=Track,on_delete=models.CASCADE)
    # test=models.IntegerField()

    @classmethod
    def getalltrainee(cls):
        return  cls.objects.filter(Active=True)
    @classmethod
    def gettraineebyid(cls,id):
        return cls.objects.get(id=id)
    @staticmethod
    def removeoldimage(oldimagepath):
        import os
        if(os.path.exists(oldimagepath)):
            os.remove()
    @classmethod
    def updatetrainee(cls,id,name,email,newimagem,trackid):

        oldobj = Trainee.gettraineebyid(id=id)
        oldobj.name = name
        oldobj.email =email
        oldimage=oldobj.image
        oldobjimage = newimagem
        oldobjimage.track = Track.gettrackbyid(trackid)
        oldobj.save()
        Trainee.removeoldimage('trainee/img'+str(oldimage))
    @staticmethod
    def gotoalltraineesroute():
        return redirect('alltrainees')
    @staticmethod
    def reversgotoalltraineesrout():
        return reverse_lazy('alltrainees')
    def getimageurl(self):
        return '/media/'+str(self.image)