from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def alltrainees(req):
    #get all trainees
    context={'trainees':Trainee.getalltrainee()}
    return render(req,'trainee/all.html',context)
def add(req):
    context={}
    context['tracks']=Track.getalltracks()
    if(req.method=='POST'):
        if('trimg' in req.FILES.keys()):
            objectoftrack=Track.gettrackbyid(req.POST['trtrack'])
            Trainee.objects.create(name=req.POST['trname'],email=req.POST['tremail'],
                                   image=req.FILES['trimg'],
                                   track=objectoftrack
                                   )
        else:
            context['Error']='Must upload profie image'
    return render(req,'trainee/add.html',context)
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