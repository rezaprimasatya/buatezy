from rest_framework import serializers
from .models import Bank,Account, AccountMeta, AccountTransaction, TransferAmount, TransferRequest, SystemConfig, SystemApp
 
class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
 
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class AccountMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountMeta
        fields = '__all__'
 
class AccountTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTransaction
        fields = '__all__'

class TransferAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferAmount
        fields = '__all__'
 
class TransferRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferRequest
        fields = '__all__'

class SystemConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemConfig
        fields = '__all__'
 
class SystemAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemApp
        fields = '__all__'