from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .selizer import Custom_User_Serlizer
from .models import CustomUser
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model#
from django.utils.encoding import force_str,force_bytes
from django.utils.http import urlsafe_base64_decode
from .utills import accounttoken
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail



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
# def Registerview(requestobj):
#     #in template html & python
#     # return render(requestobj,'home.html')
#     return render(requestobj,'Register.html')
#     # return HttpResponse('<h1>Registerview</h1>')

@api_view(['POST'])
def Registerview(request):
    customuserobjSer= Custom_User_Serlizer(data= request.data)
    if(customuserobjSer.is_valid()):
        user=customuserobjSer.save()
        #prepare email
        subject='Confirmation Email'
        # message render html verify_email
        # render(req,'pathtempl',con)
        message=render_to_string('myaccount/verification_email.html',
                                 {
                                     'user':user,
                                     'domain':request.get_host(),
                                     #encrypted
                                     'uid':urlsafe_base64_decode(force_bytes(user.pk)),
                                     'token':accounttoken.make_token(user),
                                 })
        #send email
        send_mail(subject,message,'noreplay@gmail.com',[user.email])
        return Response(
            data=customuserobjSer.data,
            status=status.HTTP_201_CREATED
        )
    else:
        return Response(
            data={'errors':customuserobjSer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def verify_email(req,uid,token):
    # decode
    uiddecoded=force_str(urlsafe_base64_decode(uid))
    user=get_object_or_404(CustomUser,pk=uiddecoded)
    # if uid exists & tokn valid
    if( user is not None and accounttoken.check_token(user,token)):
        #     update user--->email-confirm=True
        user.email_confirm=True
        user.save()
        #return response
        return Response(
            data={'msg':'email confirmed'},
            status=status.HTTP_200_OK
        )
    #else
        #return not accept
        return Response(
            data={'msg':'invalid tokem'},
            status=status.HTTP_406_NOT_ACCEPTABLE
        )