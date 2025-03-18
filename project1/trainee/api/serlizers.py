from rest_framework import serializers
from ..models import *
class Trainee_ser(serializers.ModelSerializer):
    class Meta:
        model=Trainee
        fields='__all__'