from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bank,Account, AccountMeta, AccountTransaction, TransferAmount, TransferRequest, SystemConfig, SystemApp
from .serializers import BankSerializer, AccountSerializer, AccountMetaSerializer, AccountTransactionSerializer, TransferAmountSerializer, TransferRequestSerializer, SystemConfigSerializer, SystemAppSerializer

 
class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
 
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountMetaViewSet(viewsets.ModelViewSet):
    queryset = AccountMeta.objects.all()
    serializer_class = AccountMetaSerializer
 
class AccountTransactionViewSet(viewsets.ModelViewSet):
    queryset = AccountTransaction.objects.all()
    serializer_class = AccountTransactionSerializer

class TransferAmountViewSet(viewsets.ModelViewSet):
    queryset = TransferAmount.objects.all()
    serializer_class = TransferAmountSerializer
 
class TransferRequestViewSet(viewsets.ModelViewSet):
    queryset = TransferRequest.objects.all()
    serializer_class = TransferRequestSerializer

class SystemConfigViewSet(viewsets.ModelViewSet):
    queryset = SystemConfig.objects.all()
    serializer_class = SystemConfigSerializer
 
class SystemAppViewSet(viewsets.ModelViewSet):
    queryset = SystemApp.objects.all()
    serializer_class = SystemAppSerializer

class CustomView(APIView):
    def get(self, request, format=None):
        return Response("Some Get Response ")
    
    def post(self, request, format=None):
        return Response("Some Post Response")