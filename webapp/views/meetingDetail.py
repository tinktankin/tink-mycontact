from django.views import View
from django.shortcuts import render
from django.http import HttpResponse


class MeetingDetail(View):
    def get(self, request):
        return render(request, 'webapp/meetingDetail.html')

    def post(self, request):
        return render(request, 'webapp/meetingDetail.html')
