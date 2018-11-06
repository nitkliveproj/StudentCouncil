from django.shortcuts import render,redirect
from django.db import connection
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import *

# Create your views here.
@login_required(login_url="/")
def profile(request):
	if request.user.is_authenticated:
		return render(request,'profiles/profile.html')
	else:
		return redirect('home')

@login_required(login_url="/")
def edit(request):
	if request.method == "POST":
		user = User.objects.get(username=request.user.username)
		profile = Profile.objects.get(user=request.user)
		name = request.POST['name'].split(' ')
		user.first_name = name[0]
		if len(name) > 1 :
			user.last_name = ''
			for i in range(1,len(name)):
				user.last_name += name[i]
				user.last_name += ' '
		else :
			user.last_name = ''

		user.username = request.POST.get('username',user.username)
		user.email = request.POST.get('email',user.email)
		profile.rollno = request.POST.get('rollno',profile.rollno)
		profile.branch = request.POST.get('branch',profile.branch)
		profile.birth_date = datetime.strptime(request.POST.get('birth_date',profile.birth_date),"%Y-%m-%d").date()
		profile.hostel_block = request.POST.get('hostel_block',profile.hostel_block)
		profile.phone_num = request.POST.get('phone_num',profile.phone_num)
		profile.bio = request.POST.get('bio',profile.bio)
		profile.save()
		user.profile = profile
		user.save()
		login(request,user)
		return render(request,'profiles/profile.html')
	else:
		return render(request,'profiles/edit.html')