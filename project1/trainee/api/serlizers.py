from rest_framework import serializers
from ..models import *
class Trainee_ser(serializers.ModelSerializer):
    class Meta:
        model=Trainee
        fields='__all__'
    @classmethod
    def getall(cls):
        return  cls(        Trainee.getalltrainee(),
                    many=True).data