from django.db.models.fields import return_None
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def getalltracks(req):
    # return HttpResponse('<h1>getalltracks</h1>')
    return  render(req,'page1.html')
def addtrack(req):
    return HttpResponse('<h1>Add Track</h1>')
def updatetrack(req,id):
    return HttpResponse(f'<h1>update Track with id {id}</h1>')