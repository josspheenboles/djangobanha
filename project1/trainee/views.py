from django.shortcuts import render
from .models import *
# Create your views here.
def alltrainees(req):
    return render(req,'trainee/all.html')
def add(req):
    if(req.method=='POST'):
        trname=req.POST['trname']
        tremail=req.POST['tremail']
        #upload image
        trimg=req.FILES.get('trimg')
        obj=Trainee()
        obj.name=trname
        obj.email=tremail
        obj.image=req.POST['trimg']
        obj.save()
    return render(req,'trainee/add.html')
def update(req,id):
    return render(req,'trainee/update.html')
def deletetr(req,id):
    return render(req,'trainee/update.html')