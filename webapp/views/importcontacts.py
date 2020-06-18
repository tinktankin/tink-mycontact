from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

from csv import DictReader
from webapp.models import Contact
from django.db.utils import IntegrityError

class ImportContacts(View):
	"""
	Url: /import-contacts
	Offers to the user to import from File, Google or LinkedIn
	"""
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('login')
		return render(request, 'webapp/importcontacts.html')

class ImportFromFile(View):
	"""
	Url: /import-from-file
	Imports contact from CSV Files
	Assumes that CSV file column names are the same as Contact model names
	"""
	def get(self, request):
		return redirect('import-contacts')

	def post(self, request):
		if not request.user.is_authenticated:
			return redirect('login')
		try:
			file = request.FILES['file'].read().decode('utf-8').splitlines()
			records = DictReader(file)

			for data in records:
				try:
					obj = Contact.objects.create(user=request.user, **dict(data))
				except IntegrityError:
					pass # Ideally, should update fields

			return HttpResponse("Imported")
		except:
			return HttpResponse("Error")