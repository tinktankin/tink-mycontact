from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
import subprocess as sb
from django.contrib.auth.models import User
from webapp.models import Contact

class ContactDetail(View):
    def get(self, request):
        cont_instance = Contact.objects.all()
        return render(request, 'webapp/contactDetail.html',
                      {'cont_instance': cont_instance})

    def post(self, request):
        cont_instance = Contact.objects.all()
        # Code to upload files
        file1 = request.FILES['fileUpload']
        try: # checking if system is UNIX/LINUX based and saving selected file accordingly
            path=sb.getoutput('pwd')
            if  path=="'pwd' is not recognized as an internal or external command,\noperable program or batch file.":
                raise Exception
            sb.getoutput('mkdir '+ path+'/'+'.files')#creating a hidden directory to store files
            sb.getoutput('mkdir '+ path+'/'+'.files/'+str(request.user))# creting hidden directory
            write=open(path+'/'+'.files/'+str(request.user)+'/'+str(file1),'wb')
        except: # if system is not UNIX/LINUX based i.e. for windows and saving selected file accordingly
            path=sb.getoutput("cd")
            #path.replace(' ','/ ')
            sb.getoutput('mkdir "'+ path+'"\\'+'.files')#creating a hidden directory to store files
            sb.getoutput('mkdir "'+ path+'"\\'+'.files'+'\\'+str(request.user))
            write=open(path+'\\'+'.files'+'\\'+str(request.user)+"\\"+str(file1),'wb')
        # Code to copy selected file into .files folder
        for data in file1.readlines():
            write.write(data)
        return render(request, 'webapp/contactDetail.html',{'cont_instance': cont_instance}
