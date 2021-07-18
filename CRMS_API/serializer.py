from rest_framework import serializers
from .models import Criminal, Police

class PoliceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Police
        fields = '__all__'




class CriminalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Criminal
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()