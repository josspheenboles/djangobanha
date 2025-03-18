from django.template.context_processors import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serlizer import *

@api_view(['GET'])
def helloworld(request):
    return Response(
        data={'msg':'hello python tracks'},
        status=status.HTTP_200_OK
    )

@api_view(['GET','POST'])
def getall(request):
    if(request.method=='GET'):
          return Response(
            data={'tracks':Track_ser.serlize_all()}
        )
    else:
        #get data from request
        jsondata= request.data
        #convert json to track_ser deserlization
        trackserobj=Track_ser(data=jsondata)
        #validate
        if(trackserobj.is_valid()):
            #save
            trackserobj.save()
            return Response(
                data=trackserobj.data,
                status=status.HTTP_201_CREATED
            )
        #else return error
        else:
            return Response(
                data={
                    'errors':trackserobj.errors}
                ,status=status.HTTP_400_BAD_REQUEST

            )

@api_view(['GET','PUT','DELETE','PATCH'])
def getbyid_update_delete(req,id):
    if(req.method=='GET'):
        return Response(
            data=Track_ser.getbid(id),
            status=status.HTTP_200_OK
        )
    elif(req.method=='DELETE'):
        if(Track_ser.delete(id)):
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                data={'msg':'no track to delete'}
            )

