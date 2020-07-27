from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from webapp.models import Contact
from webapp.models import Meeting

class AddMeeting(LoginRequiredMixin,View):
    login_url = 'http://127.0.0.1:8000/login'
    redirect_field_name = 'http://127.0.0.1:8000/addmeeting'
    def get(self, request):
        return render(request, 'webapp/addMeeting.html')
    
    def get_js(self,request):
        return render(request, 'webapp/static/webapp/js/addMeeting.js')

    def post(self, request):
        title=request.POST.get('title')
        location=request.POST.get('location')
        notes=request.POST.get('notes')
        attendees=request.POST.get('attendees')
        #print('>>>>>>>>>>>>>>>>>>>>>>>>>',attendees)
        contact_names=list(Contact.objects.values_list('full_name','first_name','last_name'))
        #print(contact_names)
        flag=0
        for a in contact_names:
            if attendees in a:
                flag=1
                print('-----------------------',str(a[0]))
        if flag==0:
            return HttpResponse('<script language="JavaScript"> alert("Invalid name")</script>')
        meeting_time=request.POST.get('meeting-time')
        meet_instance =Meeting(title=title,location=location,notes=notes,attendees=attendees,date=meeting_time,user=request.user)
        #print(title,location,notes,attendees,meeting_time)
        meet_instance.save()
        return render(request, 'webapp/addMeeting.html')
