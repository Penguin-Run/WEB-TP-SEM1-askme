from django import forms
from app.models import Question, Profile
from django.contrib.auth.models import User

class CreateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class CreateProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput())

class AskForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']

