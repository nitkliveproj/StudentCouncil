from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

def profile_pic_path(instance,filename):
  return '/'.join(['profile_pics',instance.rollno,filename])
class Profile(models.Model):
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
    DESIGNATION = [('PR','President'),
                   ('VP','Vice President'),
                   ('GS','General Secretary'),
                   ('JU','Joint Secretary UG'),
                   ('JP','Joint Secretary PG'),
                   ('GR','PG/PhD Girls\' Representative'),
                   ('TU','Technical Secretary UG'),
                   ('TP','Technical Secretary PG'),
                   ('CU','Cultural Secretary UG'),
                   ('CP','Cultural Secretary PG'),
                   ('EC','Engineer Convenor'),
                   ('IC','Incident Convenor'),
                   ('IT','Incident Treasurer'),
                   ('ET','Engineer Treasurer'),
                   ('EJ','Engineer Joint Convenor'),
                   ('IJ','Incident Joint Convenor'),
                  ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rollno = models.CharField(max_length = 8)
    branch = models.CharField(max_length = 2,choices = BRANCH_LIST)
    post = models.CharField(max_length = 2,choices = DESIGNATION)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.FileField(upload_to=profile_pic_path,null=True,blank=True)
    birth_date = models.DateField(null=True, blank=True)
    hostel_block = models.CharField(max_length = 20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '9876543210'. Up to 10 digits allowed.")
    phone_num = models.CharField(max_length=10, validators = [phone_regex],blank=True)

    def __str__(self):
    	return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


  