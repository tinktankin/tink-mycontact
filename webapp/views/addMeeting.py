from django.views import View
from django.shortcuts import render
from django.http import HttpResponse


class AddMeeting(View):
    def get(self, request):
        return render(request, 'webapp/addMeeting.html')

    def post(self, request):
        return render(request, 'webapp/addMeeting.html')
