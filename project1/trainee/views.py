from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def alltrainees(req):
    #get all trainees
    context={'trainees':Trainee.objects.all()}
    return render(req,'trainee/all.html',context)
def add(req):
    if(req.method=='POST'):
        # trname=req.POST['trname']
        # tremail=req.POST['tremail']
        # #upload image
        # trimg=req.FILES['trimg']
        # obj=Trainee()
        # obj.name=trname
        # obj.email=tremail
        # obj.image=trimg
        # obj.save()
        Trainee.objects.create(name=req.POST['trname'],email=req.POST['tremail'],
                               image=req.FILES['trimg'])
    return render(req,'trainee/add.html')
def update(req,id):
    return render(req,'trainee/update.html')
def deletetr(req,id):
    #hard delete--->no
    # Trainee.objects.filter(id=id).delete()
    #soft Delete

    # return HttpResponseRedirect('/Trainee/')
    return redirect('alltrainees')