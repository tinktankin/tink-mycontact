#Code to view uploaded documents
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
import subprocess as sb
class Documents(View):
    def get(self, request):
            #return render(request, 'webapp/documents.html')
    #def post(self, request):
        user=str(request.user)
        filelist=''
        try:
            path=sb.getoutput('pwd')
            if  path=="'pwd' is not recognized as an internal or external command,\noperable program or batch file.":
                raise Exception
            files=sb.getoutput('ls '+path+'/.files/'+user).split('\n')
            for name in files:
                filelist=filelist+name+'<br>'
            print(filelist)
        except:
            path=sb.getoutput('cd')
            print(path)
            files=sb.getoutput('dir '+path+"\\"+'.files'+'\\'+user).split('\n')
            print(user)
            print(files)
            for data in files:
                filelist=filelist+str(data)+'<br>'
        #cont_instance = Contact.objects.all()
        return HttpResponse(filelist)
