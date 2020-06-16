from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import User, Verification

class Verify(View):
	"""
	Url: verify/?<email>&<token>
	View to verify signup url and create new user

	GET: Checks verification token and renders form for user creation.
	POST: Checks verification token and creates new user.
	"""
	def get(self, request):
		email = request.GET.get('email')
		token = request.GET.get('token')
		obj = Verification.objects.get(pk=email, token=token, is_verified=False)
		if obj.token == token:
			return render(request, 'webapp/verify.html')
		else:
			return HttpResponse("Invalid Token")

	def post(self, request):
		email = request.GET.get('email')
		token = request.GET.get('token')
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		try:
			obj = Verification.objects.get(pk=email, token=token, is_verified=False)
			print(obj)
		except Exception as e:
			print(e)
			return HttpResponse("Invalid Token")

		if password1 != password2:
			return HttpResponse("Passwords Do Not Match!")

		try:
			newUser = User.objects.create_user(email=email, password=password1)
			newUser.first_name = fname
			newUser.last_name = lname
			newUser.save()
			obj.is_verified = True
			obj.save()
			return HttpResponse("User Created!") # Should Redirect to Dashboard
		except Exception as e:
			print(e)
			return HttpResponse("User Creation Error")
