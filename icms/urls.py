"""icms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from webapp.views import (SignUp, Verify, LoginUser, LogoutUser, Dashboard,
                          ImportContacts, ForgotPassword, ResetPassword,
                          ImportFromFile, addcontact, viewcontact, AddContacts, ViewContact, ContactForm)

from django.conf import settings
from django.conf.urls.static import static
from webapp.views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name = 'home'),
    path('signup', SignUp.as_view()),
    path('verify', Verify.as_view()),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', LogoutUser.as_view(), name='logout'),
    url('', include('social_django.urls', namespace='social')),
    path('dashboard', Dashboard.as_view(), name='dashboard'),
    path('import-contacts', ImportContacts.as_view(), name='import-contacts'),
    path('forgotpass', ForgotPassword.as_view(), name='forgotpass'),
    path('resetpass', ResetPassword.as_view(), name='resetpass'),
    path('import-from-file', ImportFromFile.as_view()),
    path('addcontact', AddContacts.as_view(), name = 'addcontact'),
    path('viewcontact',ViewContact.as_view()),
    path('contactform', ContactForm.as_view(), name='contactform'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
