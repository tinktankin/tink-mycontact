from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import Contact

class AddContacts(request):
    if request.method == 'POST':
        contact_type = request.POST.get('contact_type')
        full_name = request.POST.get('full_name')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        cont_instance = Contact(contact_type=contact_type, full_name=full_name, first_name=first_name, middle_name=middle_name, last_name=last_name)
        cont_instance.save()
    return render(request, 'add.htm')

    
