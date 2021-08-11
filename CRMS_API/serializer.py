from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Criminal, FIR, Police, PoliceStation

class PoliceStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceStation
        fields = ("station_name","address")



class PoliceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Police
        fields="__all__"


class PoliceGetSerializer(serializers.ModelSerializer):
    police_station = PoliceStationSerializer()
    class Meta:
        model = Police
        fields = ('first_name','middle_name',
        'last_name','date_of_birth',
        'gender','contact_no','address',
        'joining_date','photo','police_id','username','email'
        ,'post','police_station')

class CriminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criminal
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class FirSerializer(serializers.ModelSerializer):
    class Meta:
        model = FIR
        fields = '__all__'


class PoliceStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceStation
        fields = "__all__"