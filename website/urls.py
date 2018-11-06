from django.urls import path
from . import views

urlpatterns=[
	path('',views.home,name='home'),
	path('logout',views.log_out, name='logout'),
	path('pwdchange',views.pwdchange, name='pwdchange'),
	path('blog/<int:id>',views.blog_detail,name='detail'),
	path('blog',views.blog_List,name='List'),
	path('MinuteOfMeetings',views.mom_list,name='MoM'),
	path('senate_reports',views.senate_reports,name='senate_reports'),
	path('MoUs',views.MoUs,name='MoUs'),
	path('nitk_life',views.nitkLife,name='nitk_life'),
	path('Calender1',views.Calender1,name='Calender1'),
	path('represent/',views.represent,name='represent'),
	path('announcements',views.announcements,name='announcements'),
	path('faq',views.faq,name='faq'),
	path('sugg/',views.sugg,name='sugg'),
	path('message',views.message,name='message'),
	path('represent2/',views.represent2,name='represent2'),
	path('represent3',views.represent3,name='represent3'),
	path('devlop/',views.devlop,name='devlop'),


]
