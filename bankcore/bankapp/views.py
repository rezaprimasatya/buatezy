from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bank
from .serializers import BankSerializer

 
class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class CustomView(APIView):
    def get(self, request, format=None):
        return Response("Some Get Response ")
    
    def post(self, request, format=None):
        return Response("Some Post Response")