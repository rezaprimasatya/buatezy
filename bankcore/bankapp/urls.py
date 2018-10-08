from django.conf.urls import url
from rest_framework import routers
from bankcore.bankapp.views import BankViewSet,AccountViewSet,AccountMetaViewSet,AccountTransactionViewSet,TransferAmountViewSet,TransferRequestViewSet,SystemConfigViewSet,SystemAppViewSet, CustomView
from rest_framework_swagger.views import get_swagger_view
 

router = routers.DefaultRouter()
router.register(r'banks', BankViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'accountmetas', AccountMetaViewSet)
router.register(r'accounttransactions', AccountTransactionViewSet)
router.register(r'transferamounts', TransferAmountViewSet)
router.register(r'transactionrequests', TransferRequestViewSet)
router.register(r'systemconfigs', SystemConfigViewSet)
router.register(r'systemapps', SystemAppViewSet)

schema_view = get_swagger_view(title='Bank Service API') 

urlpatterns = [
    url(r'customview', CustomView.as_view()),
    url(r'^docs/', schema_view),
]

urlpatterns += router.urls
 