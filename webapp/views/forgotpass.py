from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from webapp.models import User, Verification
from secrets import token_urlsafe
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
import random as r

otp=""
otp+=str(r.randint(100000,999999))


class ForgotPassword(View):
    def get(self, request):
        return render(request, 'webapp/forgotpass.html')
    
    def post(self, request):

        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            token = token_urlsafe(20)
            domain = get_current_site(request).domain
            user_url = 'http://{}/verify?email={}&token={}'.format(domain, email, token)
            message = 'Enter '+otp+' and your new password to reset password'.format(user_url)
            try:
                send_mail('OTP for reset password', message, 'Team ICMS', [email], fail_silently=False, html_message=None)
                obj = Verification(email=email, token=token)
                obj.save()
                return redirect('resetpass')
            except Exception as e:
                print(e)
                return HttpResponse("Something Went Wrong!")
        else:
            return HttpResponse("User doesn't exists")