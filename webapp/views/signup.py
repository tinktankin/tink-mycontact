from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import User, Verification
from secrets import token_urlsafe
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail

class SignUp(View):
	"""
	Url: signup
	View for user signing up using email.
	GET: Form prompting email.
	POST: Sends a verification token to email and updates Verification model.
	"""
	def get(self, request):
		return render(request, 'webapp/signup.html')

	def post(self, request):
		email = request.POST.get('email')
		if User.objects.filter(email=email).exists():
			return HttpResponse("User Already Exists")

		token = token_urlsafe(20)
		domain = get_current_site(request).domain
		verification_url = 'http://{}/verify?email={}&token={}'.format(domain, email, token)
		message = """
		Thank you signing up!
		Verify your link using the link below.
		Click Here: {}
		""".format(verification_url)
		try:
			send_mail('Signup Vertification', message, 'Team ICMS', [email], fail_silently=False, html_message=None)
			obj = Verification(email=email, token=token)
			obj.save()
			return HttpResponse("Vertification Link Sent! Please Check Your Email!")
		except Exception as e:
			print(e)
			return HttpResponse("Something Went Wrong!")
			