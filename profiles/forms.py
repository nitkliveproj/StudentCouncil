from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class UserForm(forms.Form):
	username = forms.CharField(max_length=20)
	name = forms.CharField(max_length=50)
	email = forms.EmailField()

class ProfileForm(forms.Form):
	BRANCH_LIST = [('CH', 'Chemical Engineering'),
                   ('CO', 'Computer Engineering'),
                   ('CV', 'Civil Engineering'),
                   ('EC', 'Electronics and Communications Engineering'),
                   ('EE', 'Elelctrical and Electronics Engineering'),
                   ('IT', 'Information Technology'),
                   ('ME', 'Mechanical Engineering'),
                   ('MN', 'Mining Engineering'),
                   ('MT', 'Materials and Metallurgical Engineering'),
                  ]
	rollno = forms.CharField(max_length=8)
	branch = forms.ChoiceField(choices = BRANCH_LIST)
	birth_date = forms.DateField()
	hostel_block = forms.CharField(max_length=20)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '9876543210'. Up to 10 digits allowed.")
	phone_num = forms.CharField(max_length=10)
	bio = forms.CharField(max_length=500)