from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

class LoginUser(View):
	"""
	Url: login
	Logins the user using entered credentials.
	GET: Provides form for credentials input.
	POST: Authenticates the user, logins and redirects to dashboard if successful.
	"""
	def get(self, request):
		return render(request, 'webapp/login.html')

	def post(self, request):
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(username=email, password=password)
		if user is not None:
			print(user)
			login(request, user)
			return redirect('dashboard')
		else:
			return HttpResponse("Not Authorized")



			