from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def alltrainees(req):
    #get all trainees
    context={'trainees':Trainee.objects.filter(Active=True)}
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
                               image=req.FILES['trimg'],
                               )
    return render(req,'trainee/add.html')
def update(req,id):
    context={}
    #get trainee data
    context['oldtr']=Trainee.objects.get(id=id)
    if(req.method=='POST'):
        print(req.POST['trtrack'])# 1
        Trainee.objects.filter(id=id).update(
            name=req.POST['trname'],
            email=req.POST['tremail'],
            image=req.FILES['trimg'],

        )
        return redirect('alltrainees')
    return render(req,'trainee/update.html',context)
def deletetr(req,id):
    #hard delete--->no
    # Trainee.objects.filter(id=id).delete()
    #soft Delete
    Trainee.objects.filter(id=id).update(Active=False)
    # return HttpResponseRedirect('/Trainee/')
    return redirect('alltrainees')