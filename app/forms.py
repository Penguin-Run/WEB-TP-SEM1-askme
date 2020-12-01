from django import forms
from app.models import Question, Profile, Answer
from django.contrib.auth.models import User

class EditProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['user_name', 'email', 'image']

class CreateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['password'].widget = forms.PasswordInput()

class CreateProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput())

# TODO: добавить возможность добавить свой тэг (создание тэга)
class AskForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text', 'tags']

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['text']