from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from .forms import TraineeForm
from .models import Track
import track.views
from .models import Trainee
from .forms import TraineeForm
# Create your views here.
def add(req):
    # print()
    context={}
    form=TraineeForm()
    context['form']=form
    if(req.method=='POST'):
        #form handel back end validation
        #populate data to form
        #get data inserted by end user & assign to form object
        form=TraineeForm(data=req.POST,files=req.FILES)
        if(form.is_bound  and form.is_valid()):
            Trainee.objects.create(
                name=form.fileds['trname'],
                email=req.POST['tremail'],
                track=Track.gettrackbyid(req.POST['trtrack']),
                image=req.FILES['trimag']
            )
            print(form.fileds)
        else:
            context['error']=form.errors#'form not loaded with data'
    return render(req,'trainee/addFomr.html',context)
def alltrainees(req):
    #get all trainees
    context={'trainees':Trainee.getalltrainee()}
    return render(req,'trainee/all.html',context)

def addtr(req):

    context={'form':Traineeformmodel()}
    context['tracks']=Track.getalltracks()
    if(req.method=='POST'):

        # if('trimg' in req.FILES.keys()):
            objectoftrack=Track.gettrackbyid(req.POST['track'])
            Trainee.objects.create(name=req.POST['name'],email=req.POST['email'],

                                   track=objectoftrack
                                   )
        # else:
        #     context['Error']='Must upload profie image'
    return render(req,'trainee/addFomr.html',context)
def update(req,id):
    context={'tracks':Track.getalltracks()}
    #get trainee data
    context['oldtr']=Trainee.gettraineebyid(id=id)

    if(req.method=='POST'):
        # oldobj=get_object_or_404(Trainee,id=id)#return error 404
        # oldobj=Trainee.objects.get(id=id)#fire exeptopn if id not exsis
        #django object upload trainee/imgs--->update upload
        #oldimganame===newimagename
        #get inatnace --->old.imge=ne
        # check oldimage in path--->remove
        Trainee.updatetrainee(id,req.POST['trname'],req.POST['tremail'],
                              req.FILES['trimg'],req.POST['trtrack'])
        # oldobj=Trainee.gettraineebyid(id=id)
        # oldobj.name=req.POST['trname']
        # oldobj.email=req.POST['tremail']
        # oldobjimage=req.FILES['trimg']
        # oldobjimage.track=Track.gettrackbyid(req.POST['trtrack'])
        # #update old object reupload image
        # oldobj.save()
        # Trainee.objects.filter(id=id).update(
        #     name=req.POST['trname'],
        #     email=req.POST['tremail'],
        #     image=req.FILES['trimg'],
        #     track=Track.gettrackbyid(req.POST['trtrack'])
        #
        # )
        return redirect('alltrainees')
    return render(req,'trainee/update.html',context)
def deletetr(req,id):
    #hard delete--->no
    # Trainee.objects.filter(id=id).delete()
    #soft Delete
    Trainee.objects.filter(id=id).update(Active=False)
    # return HttpResponseRedirect('/Trainee/')
    return redirect('alltrainees')