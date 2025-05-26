from django.urls import path
from .views import HomeView, ServiceListAPI, ServiceListHTML

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/services/', ServiceListAPI.as_view(), name='api-services'),
    path('services/', ServiceListHTML.as_view(), name='html-services'),
    ]
