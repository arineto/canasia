from django.forms import ModelForm
from django import forms
from core.models import *

class ProjectForm(ModelForm):
	class Meta:
		model = Project
		exclude = ('latitude', 'longitude')

	def __init__(self, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs.update({'class' : 'form-control'})
		self.fields['company'].widget.attrs.update({'class' : 'form-control'})
		self.fields['country'].widget.attrs.update({'class' : 'form-control'})
		self.fields['sector'].widget.attrs.update({'class' : 'form-control'})
		self.fields['address'].widget.attrs.update({'class' : 'form-control'})
		self.fields['picture'].widget.attrs.update({'class' : 'form-control'})


class ChangePasswordForm(forms.Form):
	old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput)
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)
		self.fields['old_password'].widget.attrs.update({'class' : 'form-control'})
		self.fields['password1'].widget.attrs.update({'class' : 'form-control'})
		self.fields['password2'].widget.attrs.update({'class' : 'form-control'})

	def clean_password2(self):
	# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 != password2:
			raise forms.ValidationError("Confirmation must be equal to password.")
		return password2