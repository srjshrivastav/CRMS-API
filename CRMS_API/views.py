from .serializer import CriminalSerializer, LoginSerializer, PoliceSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Criminal, Police


# from CRMS_API import serializer

# Create your views here.
class AddPolice(APIView):


    def post(self, request, format=None):
        serializer = PoliceSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,data="Successfull created")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Authenticate(APIView):

    def post(self,request,format=None):
        serializer = LoginSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            police  = Police.objects.get(email = serializer.data.get("email"))
            if police is not None and police.password == serializer.data.get("password"):
                return Response(status=status.HTTP_201_CREATED,data=PoliceSerializer(police).data)
            return Response(status=status.HTTP_201_CREATED,data="Invalid credentials")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SearchCriminal(APIView):

    def get(self,request,format="simple"):
        if(format=='simple'):
            query = request.query_params.get("name")
            search_results = Criminal.objects.filter(first_name__icontains = query)
            return Response(data = CriminalSerializer(search_results,many=True).data)
        return Response(status=200)

class AddFir(APIView):
    def post(self,request):
        return Response()




