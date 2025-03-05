from http.client import HTTPResponse

from django.shortcuts import render

# Create your views here.
def Loginview(request):
    print(request,type(request))
    return HTTPResponse('<h1>hi python track</h1>')#document.write