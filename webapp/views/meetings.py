from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from webapp.models.meetings import Meeting


class Meetings(View):
    def get(self, request):
        meeting_model = Meeting.objects.all()
        return render(request, 'webapp/meetings.html', {'meeting_model': meeting_model})

    def post(self, request):
        return render(request, 'webapp/meetings.html')
    
    def delete(request, Meeting_id=None):
        meeting_model=Meeting.objects.get(id=Meeting_id)
        meeting_model.delete()
        return HttpResponse("Your meeting gets deleted")
