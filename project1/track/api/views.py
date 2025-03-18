from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def helloworld(request):
    return Response(
        data={'msg':'hello python tracks'},
        status=status.HTTP_200_OK
    )