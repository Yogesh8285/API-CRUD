
from django.contrib import admin
from django.urls import path,include 
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup",views.signup),
    path("login",views.login),
    path("",views.masterpage),
    path("signout",views.signout),
    path ('userinfo/',views.userinfo),
    path('userlist/',views.userlist),
    path('usercreate/',views.usercreate),
    path('addstudent/',views.addstudent),
]
