from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import EmpDetails

class AddUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','email','username','password1','password2']

class AddEmpForm(forms.ModelForm):
	class Meta:
		model = EmpDetails
		fields = ['user_id', 'user_name','user_email', 'user_password', 'user_phone', 'user_address', 'user_image']


class UserUpdateForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','email','username','password1','password2']


class EmpUpdateForm(forms.ModelForm):
	class Meta:
		model = EmpDetails
		fields = ['user_id', 'user_name','user_email', 'user_password', 'user_phone', 'user_address', 'user_image']

