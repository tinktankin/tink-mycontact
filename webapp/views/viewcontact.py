from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import Contact

class ViewContact(request):
    cont_instance = Contact.objects.all()
    return render(request, 'view.html', {'cont_instance':cont_instance})
