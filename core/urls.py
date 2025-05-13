from django.urls import path
from .views import ServiceListAPI, ServiceListHTML

urlpatterns = [
    path('api/services/', ServiceListAPI.as_view(), name='api-services'),
    path('services/', ServiceListHTML.as_view(), name='html-services'),
    ]
