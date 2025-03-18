from rest_framework import serializers

class Track_ser(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)#pk
    name=serializers.CharField(max_length=50)
