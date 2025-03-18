from rest_framework import serializers
from ..models import Track
class Track_ser(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)#pk
    name=serializers.CharField(max_length=50)

    @classmethod
    def serlize_all(cls):
        return  cls(Track.getalltracks(),many=True).data