from .serializer import CriminalSerializer, FirSerializer, LoginSerializer, PoliceGetSerializer, PoliceSerializer, PoliceStationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import fields, status
from .models import Criminal, FIR, Police


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
                return Response(status=status.HTTP_202_ACCEPTED,data=PoliceGetSerializer(police).data)
            return Response(status=status.HTTP_401_UNAUTHORIZED,data="Invalid credentials")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SearchCriminal(APIView):

    def get(self,request,format="simple"):
        if(format=='simple'):
            query = request.query_params.get("name")
            search_results = Criminal.objects.filter(first_name__icontains = query)
            return Response(data = CriminalSerializer(search_results,many=True,context={'request':request}).data)
        return Response(status=200)

class Fir(APIView):
    def post(self, request):
        serialized_fir = FirSerializer(data=request.data,context={'request': request})
        if serialized_fir.is_valid():
            serialized_fir.save()
            return Response(status=status.HTTP_201_CREATED,data="Successfull created")
        return Response(serialized_fir.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        query = request.query_params.get("criminal_id")
        try:
            criminal = Criminal.objects.get(criminal_id=query)
            firs = criminal.firOf.all()
            return Response(data = FirSerializer(firs,many=True,context={'request':request}).data)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT,data=[])
    

class PoliceStation(APIView):

    def post(self,request):
        serialized_station = PoliceStationSerializer(data=request.data,context={'request':request})
        if serialized_station.is_valid():
            serialized_station.save()
            return Response(status=status.HTTP_201_CREATED,data={"station Id":serialized_station.data.get('police_station_id')})
        return Response(status=status.HTTP_400_BAD_REQUEST,data="Failed")






