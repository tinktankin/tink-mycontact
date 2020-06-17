from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import logout

class LogoutUser(View):
	"""
	Url: logout
	Logs out the current user.
	GET:  
	"""
	def get(self, request):
		logout(request)
		return redirect('login') # Should redirect to home page