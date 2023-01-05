from django.contrib import admin

# Register your models here.
from .models import UserInfo
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','username','email','password']


from .models import Student
@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ['sid','sname','city','username',]