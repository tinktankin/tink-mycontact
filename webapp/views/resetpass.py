from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from webapp.views import forgotpass

User = get_user_model()


class ResetPassword(View):
    def get(self, request):
        return render(request, 'webapp/resetpass.html')

    def post(self, request):
        OTP = request.POST.get('otp')
        email=request.POST.get('email')
        newpassword = request.POST.get('password')
        if (OTP==forgotpass.otp):
            u = User.objects.get(email=email)
            u.set_password(newpassword)
            u.save()
            return HttpResponse("password changed succesfully")
        else:
            return HttpResponse("OTP incorrect")