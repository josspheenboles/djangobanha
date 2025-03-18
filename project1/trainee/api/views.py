from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from .serlizers import Trainee_ser
from rest_framework import generics
from ..models import Trainee
from rest_framework.viewsets import  ViewSet,ModelViewSet

@api_view(['GET'])
def info(req):
    return Response(
        data={'\\':'list all trainee',
                                    'id\\':'return trainee by id'
                                    },
        status=status.HTTP_103_EARLY_HINTS

    )

class TraineeModelViewSet(ModelViewSet):
    queryset = Trainee.getalltrainee()
    serializer_class = Trainee_ser


class Trainee_List_Create_G(generics.ListCreateAPIView):
    queryset = Trainee.getalltrainee()
    serializer_class = Trainee_ser
class Trainee_get_update_delete_G(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainee.getalltrainee()#reatrive active only
    serializer_class = Trainee_ser
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

class Trainee_get_update_delete(APIView):
    def get(self,request,id):
        return Response(
            data=Trainee_ser.getbyid(id),
            status=status.HTTP_200_OK
        )
    def dispatch(self,req,id):
        pass

    def delet(self,req,id):
        pass

    def put(self,req,id):
        pass

