from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Blog, MinuteOfMeeting,reports_db, Calender, Representatives, Announcements,Faq,councilmess,developers,Suggestions

# Create your views here.
def home(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			return render(request,'website/home.html')
		else:
			return render(request,'website/home.html',{'login':'failed'})
	else:
		if request.user.is_authenticated:
			a=Announcements.objects.all()
			b=Blog.objects.all()
			context={'b_set':b, 
					 'a_set':a}
			return render(request,'website/home.html',context)
			
		else:
			a=Announcements.objects.all()
			b=Blog.objects.all()
			context={'b_set':b, 
					 'a_set':a}
			return render(request,'website/home.html',context)
			
	
	
@login_required(login_url="/")
def pwdchange(request):
	if request.method == "POST":
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		if password1 and password2 and password2 == password1 :
			user = request.user
			user.set_password(password1)
			user.save()
			return render(request,'website/home.html')
		else:
			return render(request,'website/home.html',{'change':'failed'})
	else:
		return render(request,'website/home.html')

@login_required(login_url="/")
def log_out(request):
	logout(request)
	request.session.clear()
	return redirect('home')

def blog_detail(request,id=None):
    instance=get_object_or_404(Blog,id=id)
    context={
        'instance':instance,
        'title':instance.title,
    }
    return render(request,'website/blog_detail.html',context)

def blog_List(request):
    queryset_list= Blog.objects.all().order_by("-timestamp","-update")
    paginator = Paginator(queryset_list, 5)
    page_request_var ="page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context={
        'queryset':queryset,
        'page_request_var':page_request_var


    }
    return render(request,'website/blog_list.html',context)


def mom_list(request):
	queryset_list = MinuteOfMeeting.objects.all().order_by("-timestamp")
	return render(request,'website/mom_list.html',{'queryset':queryset_list})


def senate_reports(request):
	reports=reports_db.objects.all()
	return render(request,'website/senate_reports.html',{'report_set':reports})


def MoUs(request):
	return render(request,'website/MoUs.html')


def nitkLife(request):
	return render(request,'website/nitk_life.html')


def Calender1(request):
	cal = Calender.objects.get(Calender="Academic Calender")
	return redirect(cal.pdf.url)


def represent(request):
	rcore=Representatives.objects.filter(repcat='CM')
	rteame=Representatives.objects.filter(repcat='TE')
	rteami=Representatives.objects.filter(repcat='TI')
	rtec=Representatives.objects.filter(repcat='SE')
	rca=Representatives.objects.filter(repcat='CA')
	rfr=Representatives.objects.filter(repcat='FR')
	rsr=Representatives.objects.filter(repcat='SR')
	rta=Representatives.objects.filter(repcat='TR')
	rf=Representatives.objects.filter(repcat='RF')
	rpg=Representatives.objects.filter(repcat='PG')

	context1={
	'coremem':rcore,
	'teamengi':rteame,
	'teaminci':rteami,
	'tsecre':rtec,
	'culmni':rca,
	'firstr':rfr,
	'secondr':rsr,
	'thirdr':rta,
	'fourthr':rf,
	'pgr':rpg,
	}
	return render(request,'website/represent.html',context1)


def announcements(request):
	ann=Announcements.objects.all()
	return render(request,'website/announcements.html',{'ann_set':ann})


def faq(request):
	a=Faq.objects.all()
	return render(request,'website/faq.html',{'faq_set':a})


def sugg(request):
    if request.method == 'POST':
        post = Suggestions()
        post.name = request.POST.get('name')
        post.department = request.POST.get('section')
        post.rollno = request.POST.get('rollnumber')
        post.mobno = request.POST.get('mobile')
        post.problem = request.POST.get('problem')
        post.answer = request.POST.get('solution')
        post.email = request.POST.get('email')
        post.save()
        return render(request,'website/sugg.html')

    else:
        return render(request,'website/sugg.html')


def message(request):
	mess=councilmess.objects.all()
	return render(request,'website/message.html',{'message_set':mess})


def represent2(request):
	rcore=Representatives.objects.filter(repcat='CM')
	rteame=Representatives.objects.filter(repcat='TE')
	rteami=Representatives.objects.filter(repcat='TI')
	rtec=Representatives.objects.filter(repcat='SE')
	rca=Representatives.objects.filter(repcat='CA')
	rfr=Representatives.objects.filter(repcat='FR')
	rsr=Representatives.objects.filter(repcat='SR')
	rta=Representatives.objects.filter(repcat='TR')
	rf=Representatives.objects.filter(repcat='RF')
	rpg=Representatives.objects.filter(repcat='PG')

	context1={
	'coremem':rcore,
	'teamengi':rteame,
	'teaminci':rteami,
	'tsecre':rtec,
	'culmni':rca,
	'firstr':rfr,
	'secondr':rsr,
	'thirdr':rta,
	'fourthr':rf,
	'pgr':rpg,
	}
	return render(request,'website/represent2.html',context1)


def represent3(request):
	return render(request,'website/represent3.html')


def aboutus(request):
	return render(request,'website/aboutus.html')


def devlop(request):
    a=developers.objects.all()
    return render(request, 'website/aboutus.html', {'queryset': a})