from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator

# Create your views here.
def home(request):
    return HttpResponse("سلام! این صفحه اصلی است.")



class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            current_site = get_current_site(request).domain
            activation_link = f"http://{current_site}/activate/{uid}/{token}/"

            # ارسال ایمیل (موقتاً در کنسول نمایش بده)
            send_mail(
                subject='فعالسازی حساب',
                message=f'برای فعال‌سازی حسابت این لینک رو باز کن:\n{activation_link}',
                from_email='ihuacir21@gmail.com',
                recipient_list=[user.email],
                fail_silently=False,
            )

            return Response({'message': 'ثبت‌نام موفق بود. لینک فعال‌سازی ایمیل شد.'}, status=201)
        return Response(serializer.errors, status=400)
    


from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator

class ActivateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uid, token):
        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError):
            return Response({'error': 'کاربر نامعتبر'}, status=400)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'message': 'حساب فعال شد ✅'}, status=200)
        else:
            return Response({'error': 'توکن نامعتبر یا منقضی شده'}, status=400)


from rest_framework.permissions import IsAuthenticated

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'username': request.user.username,
            'email': request.user.email,
        })


