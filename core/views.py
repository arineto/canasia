from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db.models import Q
from random import randint
from core.models import *
from core.forms import *

def home(request):
	if request.user.is_authenticated():
		return redirect('/overview/')

	try:
		login_picture = LoginPicture.objects.all().order_by('-id')[0]
	except:
		login_picture = None

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

	return render(request, 'login.html', {'error':error, 'login_picture':login_picture})


def logout_aux(request):
	logout(request)
	return redirect('/')


@login_required
def overview(request, filter_value=None):
	countries = Country.objects.all().order_by('name')
	sectors = Sector.objects.all().order_by('name')
	data_tables = DataTable.objects.all()
	filter_country = None
	
	try:
		country = Country.objects.get(name=filter_value)
		projects = Project.objects.filter(country=country)
		filter_country = filter_value
	except:
		try:
			sector = Sector.objects.get(name=filter_value)
			projects = Project.objects.filter(sector=sector)
		except:
			projects = Project.objects.all()
	
	return render(request, 'overview.html', {'overview':True ,'projects':projects, 'countries':countries, 'sectors':sectors, "data_tables":data_tables,'filter_country':filter_country})


@login_required
def dashboard(request):
	search_value = None
	projects = Project.objects.all()
	
	if request.method == 'POST':
		search_value = request.POST.get('search')
		projects = projects.filter(
				Q(country__name__icontains=search_value) |
				Q(sector__name__icontains=search_value) |
				Q(company__icontains=search_value) |
				Q(title__icontains=search_value) |
				Q(address__icontains=search_value)
			).order_by('-id')
	
	return render(request, 'dashboard.html', {'search_value':search_value, 'projects':projects})


def forgot_password(request):
	answer = None
	try:
		login_picture = LoginPicture.objects.all().order_by('-id')[0]
	except:
		login_picture = None
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

	return render(request, 'login.html', {'forgot_password':True, 'answer':answer, 'login_picture':login_picture})


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


@login_required
def add_project(request):
	if request.method == "POST":
		form = ProjectForm(request.POST, request.FILES)
		lat = request.POST.get('latitude')
		lng = request.POST.get('longitude')
		if form.is_valid():
			project = form.save(commit=False)
			project.latitude = lat
			project.longitude = lng
			project.save()
			return redirect("/dashboard/")
	else:
		form = ProjectForm()

	return render(request, 'forms.html', {'form':form})


@login_required
def edit_project(request, project_id):
	instance = Project.objects.get(id=project_id)
	if request.method == "POST":
		form = ProjectForm(request.POST, request.FILES ,instance=instance)
		lat = request.POST.get('latitude')
		lng = request.POST.get('longitude')
		if form.is_valid():
			project = form.save(commit=False)
			project.latitude = lat
			project.longitude = lng
			project.save()
			return redirect("/dashboard/")
	else:
		form = ProjectForm(instance=instance)

	return render(request, 'forms.html', {'form':form})


@login_required
def delete_project(request, project_id):
	Project.objects.get(id=project_id).delete()
	return redirect('/dashboard/')
