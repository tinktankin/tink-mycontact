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
		r="^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
		if (re.search(r,email)==None):
			return HttpResponse('<script language="JavaScript">alert("Invaild mail id");window.location="http://127.0.0.1:8000/signup"</script>')
		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			return HttpResponse("Not Authorized")
