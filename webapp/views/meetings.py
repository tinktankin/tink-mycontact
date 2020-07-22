from django.views import View
from django.shortcuts import render
from django.http import HttpResponse


class Meetings(View):
    def get(self, request):
        return render(request, 'webapp/meetings.html')

    def post(self, request):
        return render(request, 'webapp/meetings.html')
