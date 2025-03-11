from django.db import models
# from track.models import Track


# Create your models here.
class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)
    email=models.EmailField(unique=True)
    createdate=models.DateField(auto_now_add=True)
    # stor path in db & file in media
    image = models.ImageField(upload_to='trainee/imgs')
    Active=models.BooleanField(default=True)
