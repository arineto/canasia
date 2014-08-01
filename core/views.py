from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from random import randint
from core.models import *
from core.forms import *

def home(request):
	if request.user.is_authenticated():
		return redirect('/overview/')

	error = None
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('/overview/')
			else:
				error = "Not active user"
		else:
			error = "Invalid username/password"

	return render(request, 'login.html', {'error':error})


def logout_aux(request):
	logout(request)
	return redirect('/')


@login_required
def overview(request, filter_value=None):
	countries = Country.objects.all()
	sectors = Sector.objects.all()
	
	try:
		country = Country.objects.get(name=filter_value)
		projects = Project.objects.filter(country=country)
	except:
		try:
			sector = Sector.objects.get(name=filter_value)
			projects = Project.objects.filter(sector=sector)
		except:
			projects = Project.objects.all()
	
	return render(request, 'overview.html', {'projects':projects, 'countries':countries, 'sectors':sectors})


def forgot_password(request):
	answer = None
	if request.method == "POST":
		email = request.POST.get("email")
		try:
			user = User.objects.get(email=email)
			new_password = randint(100000, 999999)
			message = "Hello, \nThis is an answer to password recovery. Please change your password for security reasons.\nNew Password: "+str(new_password)
			email = EmailMessage('Can Asia Footprint', message, to=[email])
			email.send()
			user.set_password(new_password)
			user.save()
			answer = "The password was sent to you email."
		except:
			answer = "There are no accounts registered in this email."

	return render(request, 'login.html', {'forgot_password':True, 'answer':answer})


@login_required
def change_password(request):
	error = None
	if request.method == 'POST':
		form = ChangePasswordForm(request.POST)
		if not request.user.check_password(request.POST.get('old_password')):
			error = "Wrong old password"
		else:
			if form.is_valid():
				request.user.set_password(request.POST.get('password1'))
				request.user.save()
				return redirect('/')
	else:
		form = ChangePasswordForm()
	return render(request, 'forms.html', {'change_password':True, 'form':form, 'error':error})
