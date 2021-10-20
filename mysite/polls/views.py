from django.shortcuts import render
from .forms import ContactForm
from . import models

# Create your views here.


def index(request):
	if request.method=='POST':
		#print("Helo")
		#formValue = request.POST
		form = ContactForm(request.POST)
		#print(form)
		if form.is_valid():
			form.save()
			# p = models.Employee(form)
   #          p.save()

		#print(formValue)
	form = ContactForm()
	return render(request, 'polls/list.html', {'form': form})