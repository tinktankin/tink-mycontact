from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import Contact


class ViewContact(View):
    def get(self, request):
        cont_instance = Contact.objects.all()
        return render(request, 'webapp/view.html',
                      {'cont_instance': cont_instance})

    def post(self, request):
        cont_instance = Contact.objects.all()
        return render(request, 'webapp/view.html',
                      {'cont_instance': cont_instance})
