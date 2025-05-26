from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import View
from django.shortcuts import render


class ServiceListAPI(APIView):
    def get(self, request):
        services = [
            {
                "name": "GPT",
                "description": "پردازش متن و مدل زبانی",
                "endpoint": "/gpt/"
            },
            {
                "name": "Vision",
                "description": "پردازش تصویر و تشخیص اشیاء",
                "endpoint": "/vision/"
            },
            {
                "name": "User Service",
                "description": "مدیریت کاربران و احراز هویت",
                "endpoint": "/user/"
            },
            {
                "name": "Subscription",
                "description": "مدیریت اشتراک و محدودیت‌ها",
                "endpoint": "/subscription/"
            }
        ]
        return Response(services)



class HomeView(View):
    def get(self , request):
        return render(request, 'core/index.html')
        pass
    
class ServiceListHTML(View):
    def get(self, request):
        services = [
            {
                "name": "GPT",
                "description": "پردازش متن و مدل زبانی",
                "endpoint": "/gpt/"
            },
            {
                "name": "Vision",
                "description": "پردازش تصویر و تشخیص اشیاء",
                "endpoint": "/vision/"
            },
            {
                "name": "User Service",
                "description": "مدیریت کاربران",
                "endpoint": "/user/"
            },
            {
                "name": "Subscription",
                "description": "مدیریت اشتراک",
                "endpoint": "/subscription/"
            }
        ]
        return render(request, 'core/index.html', {'services': services})
