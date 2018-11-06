from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog,MinuteOfMeeting,reports_db,Calender,Representatives,Announcements,Suggestions,Faq,councilmess,developers

class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name' , 'last_name', 'email', )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True


class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    prepopulated_fields = {'username': ('first_name' , 'last_name', )}

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', ),
        }),
    )

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Blog)
admin.site.register(MinuteOfMeeting)
admin.site.register(reports_db)
admin.site.register(Calender)
admin.site.register(Representatives)
admin.site.register(Announcements)
admin.site.register(Suggestions)
admin.site.register(Faq)
admin.site.register(councilmess)
admin.site.register(developers)


