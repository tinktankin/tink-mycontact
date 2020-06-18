from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

class Dashboard(View):
	"""
	Url: dashboard
	"""
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('login')
		print(request.user.id, request.user.email)
		return HttpResponse("Logged In")
