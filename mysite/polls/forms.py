from django import forms

class ContactForm(forms.Form):

	CHOICES=[('Male','Male'),
         ('Female','Female')]

	
	name = forms.CharField(max_length=100)
	mobile = forms.CharField(max_length=100)
	email = forms.EmailField(max_length=100)
	Gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
