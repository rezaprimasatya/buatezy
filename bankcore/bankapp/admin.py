from django.contrib import admin
from .models import Bank,Account, AccountMeta, AccountTransaction, TransferAmount, TransferRequest, SystemConfig, SystemApp
 
admin.site.register(Bank)
admin.site.register(Account)
admin.site.register(AccountMeta)
admin.site.register(AccountTransaction)
admin.site.register(TransferAmount)
admin.site.register(TransferRequest)
admin.site.register(SystemConfig)
admin.site.register(SystemApp)
