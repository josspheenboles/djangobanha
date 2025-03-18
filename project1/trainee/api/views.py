from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from .serlizers import Trainee_ser
# Trainee has fk from track
class Trainee_List_Create(APIView):
    def get(self,req):
        return Response(
            data=Trainee_ser.getall(),
            status=HTTP_200_OK)

    def post(self,req):
        #get data
        #object ser
        serobj=Trainee_ser(data=req.data)
        #if valid
        if(serobj.is_valid()):
            #save
            serobj.save(            )
            return  Response(
                data=serobj.data,
                status=status.HTTP_201_CREATED
            )
        #else
        else:
            return Response(
                data={'errors':serobj.errors}
            )

