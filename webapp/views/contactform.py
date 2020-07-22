from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from webapp.models import User, ContactForm as form


class ContactForm(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        return render(request, 'webapp/contactform.html', {'owner': request.user})

    def post(self, request):
        owner = request.user
        contact_type = str(request.POST["radiobtn"])
        url = request.POST.get('url')
        contactform = form(owner=owner, contact_type=contact_type, url=url)
        contactform.save()
        return HttpResponse('Contact form added successfully')
