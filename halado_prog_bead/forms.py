from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
	username = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=200)
	firstname = forms.CharField(max_length=30)
	lastname = forms.CharField(max_length=30)

	class Meta:
		model = User
		fields = ('firstname', 'lastname', 'username', 'email', 'password1', 'password2',)
