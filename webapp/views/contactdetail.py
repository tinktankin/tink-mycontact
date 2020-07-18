from django.views import View
from django.shortcuts import render
from django.http import HttpResponse


class ContactDetail(View):
    def get(self, request):
        return render(request, 'webapp/contactDetail.html')
