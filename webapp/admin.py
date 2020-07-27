from django.contrib import admin

from webapp.models import Contact, Group, User, Verification, ContactForm, Meeting

# Register your models here.
admin.site.register(User)
admin.site.register(Verification)
admin.site.register(Contact)
admin.site.register(Group)
admin.site.register(ContactForm)
admin.site.register(Meeting)
