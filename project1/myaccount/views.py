from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
# normal function
#must httprequest >>> return Httpresoind
def Loginview(request):
    # print(request.method,request.is_ajax())
    print(request,type(request))
    obj=HttpResponse('<h1>hi python track</h1>')#document.write
    obj.write('<h2>seconde write</h2>')
    obj['content-type']='text/plain'

    # return HttpResponse('<h1>hi python track</h1>')#document.write
    return  obj
def Registerview(requestobj):
    #in template html & python
    # return render(requestobj,'home.html')
    return render(requestobj,'Register.html')
    # return HttpResponse('<h1>Registerview</h1>')