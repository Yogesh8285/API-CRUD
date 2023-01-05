from django.db import models

# Create your models here.

class UserInfo(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    username = models.CharField(max_length=30,primary_key = True)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=30)
    
    class Meta:
        db_table = "UserInfo"

class Student(models.Model):
    sid = models.IntegerField(primary_key = True)
    username = models.ForeignKey(to = 'Myapp.UserInfo',on_delete=models.CASCADE)
    sname = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    class Meta:
        db_table = "Student"
    
        
    # def __str__(self):
    #     return self.UserInfo
