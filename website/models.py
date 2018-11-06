from django.conf import settings
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import datetime
# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, default=1 ,on_delete=False)
    title=models.CharField(max_length=150)
    image=models.ImageField(upload_to='blog_pics',null=True,blank=True)
    content = models.TextField()
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
    update=models.DateTimeField(auto_now=True,auto_now_add=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail",kwargs={'id':self.id})

class MinuteOfMeeting(models.Model):
    title=models.CharField(max_length=150,null=True)
    pdf=models.FileField(upload_to='M.O.M.s',null=True,blank=True)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
    def __str__(self):
        return self.title + ' ' + str(self.timestamp.date())

class reports_db(models.Model):
	report = models.CharField(max_length=50)
	document = models.FileField(upload_to='Documents',null=True,blank=True)
	
	def __str__(self):
		return self.report

class Calender(models.Model):
	Calender = models.CharField(max_length=50)
	pdf = models.FileField(upload_to='Calender',null=True,blank=True)
	def __str__(self):
		return self.Calender

class Representatives(models.Model):
    CAT_LIST = [('CM', 'Core Member'),
                   ('TE', 'Team Engi'),
                   ('TI', 'Team Inci'),
                   ('SE', 'Technical Secreatories'),
                   ('CA', 'Cultural and Alumni Secreatories'),
                   ('FR', 'First Year Class Representatives'),
                   ('SR', 'Second Year Class Representatives'),
                   ('TR', 'Third Year Class Representatives'),
                   ('RF', 'Fourth Year Class Representatives'),
                   ('PG', 'PG Class Representatives'),
                  ]
    repname=models.CharField(max_length = 20,default="")
    rep_roll_no=models.CharField(max_length=8,default="")
    repemail=models.EmailField(max_length =40,default="")
    rep_mob_mo=models.IntegerField(default=0)
    reppost=models.CharField(max_length = 30,default="")
    rep_course=models.CharField(max_length=10,default="")
    repimage=models.FileField(upload_to='rep_img',null=True,blank=True)
    rep_department=models.CharField(max_length=40,default="")
    rep_yearsofstudy=models.CharField(max_length=10,default="")
    repcat=models.CharField(max_length=2,default="",choices=CAT_LIST)
    rep_degree=models.CharField(max_length=2,default="")



    def __str__(self):
     return self.repname

class Announcements(models.Model):
     heading=models.CharField(max_length = 50,default="")
     postdate=models.DateTimeField(default="")
     content=models.TextField(default="")
     contact=models.IntegerField(default="")
     eventdate=models.DateTimeField(default=datetime.datetime.now)
     def __str__(self):
        return self.heading

class Suggestions(models.Model):
     DEPT_LIST = [('IN', 'Infrastructure'),
                   ('HM', 'Hostels Maintainence'),
                   ('MF', 'Mess Food'),
                   ('AC', 'Academics'),
                   ('SP', 'Sports'),
                   ('SA', 'Students Activities'),
                   ('OT', 'Others'),
                  ]
     name=models.CharField(max_length = 30,default="")
     department=models.CharField(max_length =2,choices=DEPT_LIST,default="" )
     rollno=models.IntegerField(default="")
     mobno=models.IntegerField(default="")
     problem=models.TextField(default="")
     answer=models.TextField(default="")
     email=models.EmailField(default="")

     def __str__(self):
      return self.problem


class Faq(models.Model):
    question=models.TextField(default="")
    answer=models.TextField(default="")

    def __str__(self):
        return self.question

class councilmess(models.Model):
    message=models.TextField(default="")

class developers(models.Model):
   name=models.CharField(default="",max_length=250)
   image=models.FileField(upload_to='dev_img',null=True,blank=True) 
   department=models.CharField(default="",max_length=250)
   mobno=models.IntegerField(default="")

   def __str__(self):
      return self.name
