from django.db import models
from .user import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Contact(models.Model):
	score_matrix=models.FloatField(default=0)
	#matrix_type=models.RadioField(max_length=30, default=None, null=True, blank=True)
	contact_type = models.CharField(max_length=30, default=None, null=True, blank=True)
	full_name = models.CharField(max_length=30, default=None, null=True, blank=True)
	first_name = models.CharField(max_length=30, default=None, null=True, blank=True)
	middle_name = models.CharField(max_length=30, default=None, null=True, blank=True)
	last_name = models.CharField(max_length=30, default=None, null=True, blank=True)
	company = models.CharField(max_length=30, default=None, null=True, blank=True)
	designation = models.CharField(max_length=30, default=None, null=True, blank=True)
	email = models.EmailField(max_length=60, default=None, null=True, blank=True)
	phone = models.CharField(max_length=30, default=None, null=True, blank=True)
	location = models.CharField(max_length=30, default=None, null=True, blank=True)
	gender = models.CharField(max_length=30, default=None, null=True, blank=True)
	title = models.CharField(max_length=30, default=None, null=True, blank=True)
	dept = models.CharField(max_length=30, default=None, null=True, blank=True)
	university = models.CharField(max_length=30, default=None, null=True, blank=True)
	degree = models.CharField(max_length=30, default=None, null=True, blank=True)
	passing_year = models.CharField(max_length=30, default=None, null=True, blank=True)
	college = models.CharField(max_length=30, default=None, null=True, blank=True)
	linkedin_url = models.CharField(max_length=30, default=None, null=True, blank=True)
	facebook_url = models.CharField(max_length=30, default=None, null=True, blank=True)
	skype_id = models.CharField(max_length=30, default=None, null=True, blank=True)
	industry = models.CharField(max_length=30, default=None, null=True, blank=True)
	country = models.CharField(max_length=30, default=None, null=True, blank=True)
	state = models.CharField(max_length=30, default=None, null=True, blank=True)
	zip_code = models.CharField(max_length=30, default=None, null=True, blank=True)
	key_skills = models.CharField(max_length=100, default=None, null=True, blank=True)
	total_exp = models.CharField(max_length=30, default=None, null=True, blank=True)
	years_in_business = models.CharField(max_length=30, default=None, null=True, blank=True)
	cin_no = models.CharField(max_length=30, default=None, null=True, blank=True)
	turnover = models.CharField(max_length=30, default=None, null=True, blank=True)
	incorporation_date = models.CharField(max_length=30, default=None, null=True, blank=True)
	employees = models.CharField(max_length=30, default=None, null=True, blank=True)
	ctc = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf01 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf02 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf03 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf04 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf05 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf06 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf07 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf08 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf09 = models.CharField(max_length=30, default=None, null=True, blank=True)
	udf010 = models.CharField(max_length=30, default=None, null=True, blank=True)

	user = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		unique_together = ['email', 'phone', 'user'] # Needs Verification

#scoring matrix calculation for basic matrix_type
def basic(instance):
	score=0
	if instance.full_name=='':
		if instance.first_name!='' :
			score+=10
		if  instance.last_name!='':
			score+=10
	else:
		score+=20
	if instance.company!='':
		score+=20
	if instance.designation!='':
		score+=20
	if instance.email!='':
		score+=20
	if instance.phone!='':
		score+=20
	return score

#scoring matrix calculation for Biz matrix_type
def biz(instance):
	score=0
	if instance.full_name=='':
		if instance.first_name!='' :
			score+=10
		if  instance.last_name!='':
			score+=10
	else:
		score+=20
	if instance.company!='':
		score+=20
	if instance.designation!='':
		score+=15
	if instance.email!='':
		score+=5
	if instance.phone!='':
		score+=20
	if instance.location!='':
		score+=5
	if instance.title!='':
		score+=15
	return score

#scoring matrix calculation for HR matrix_type
def hr(instance):
	score=0
	if instance.full_name=='':
		if instance.first_name!='' :
			score+=5
		if  instance.last_name!='':
			score+=5
	else:
		score+=10
	if instance.company!='':
		score+=5
	if instance.designation!='':
		score+=10
	if instance.email!='':
		score+=20
	if instance.phone!='':
		score+=5
	if instance.location!='':
		score+=5
	if instance.key_skills!='':
		score+=15
	if instance.total_exp!='':
		score+=15
	if instance.ctc!='':
		score+=15
	return score

def new(instance):
    pass
@receiver(post_save, sender=Contact)
def calculate_score_matrix(sender, instance, created, **kwargs):
	try:
		if created:
			#print(instance.matrix_type)
			instance.score_matrix = basic(instance)
			instance.save()
			print('Score matrix calculated')
		else:
			instance.score_matrix = basic(instance)
			instance.save()
			print('Score matrix calculated')
	except:
		pass
