from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
# Restfullview restrication method
@api_view(['POST'])
def helloworld(requset):
    print(requset.data)
    if('name' in requset.data):
        return Response(
            data=requset.data,
            status=status.HTTP_200_OK

        )
    else:
        return Response(
            data={'error':'name must b send'},
            status=status.HTTP_400_BAD_REQUEST
        )