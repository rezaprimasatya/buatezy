from django.conf.urls import url
from rest_framework import routers
from bankcore.bankapp.views import BankViewSet, CustomView
from rest_framework_swagger.views import get_swagger_view
 
router = routers.DefaultRouter()
router.register(r'banks', BankViewSet)

schema_view = get_swagger_view(title='Bank Service API') 

urlpatterns = [
    url(r'customview', CustomView.as_view()),
    url(r'^docs/', schema_view),
]

urlpatterns += router.urls