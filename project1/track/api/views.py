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

@api_view(['GET'])
def getall(reaquest):
    # tracks=Track.getalltracks()
    # jsontrack=Track_ser(tracks,many=True)
    return Response(
        data={'tracks':Track_ser.serlize_all(
        )}
    )