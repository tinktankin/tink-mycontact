from django.db import models

class Verification(models.Model):
	email = models.EmailField(default = None, max_length = 255, primary_key = True)
	token = models.CharField(null = True, max_length = 255)
	time = models.DateTimeField(auto_now_add = True)
	is_verified = models.BooleanField(default=False)

	def __str__(self): 
		return self.email 