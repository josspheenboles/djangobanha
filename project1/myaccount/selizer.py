from rest_framework import serializers
from .models import CustomUser

class Custom_User_Serlizer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'

