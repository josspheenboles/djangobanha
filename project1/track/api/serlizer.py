from rest_framework import serializers
from ..models import Track
class Track_ser(serializers.Serializer):

    id=serializers.IntegerField(read_only=True)#pk
    name=serializers.CharField(max_length=50)

    @classmethod
    def serlize_all(cls):
        return  cls(Track.getalltracks(),many=True).data

    @classmethod
    def getbid(cls,id):
        return Track_ser(instance=Track.gettrackbyid(id)).data
    @classmethod
    def delete(cls,id):
        Track.objects.filter(id=id).delete()
        return True
    def create(self, validated_data):
        obj=Track()
        obj.name=validated_data['name']
        obj.save()
        return obj

