from django import forms


from .models import Suggestions

class SuggestionsForm(forms.ModelForm):
	class Meta:
		model = Suggestions
		fields = [
		'name',
		'department',
		'rollno',
		'mobno',
		'problem',
		'answer',
		'email'
		]