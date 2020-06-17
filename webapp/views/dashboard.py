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
		return HttpResponse("Logged In")
		