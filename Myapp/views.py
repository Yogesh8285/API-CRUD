from django.shortcuts import render,redirect
from .models import UserInfo,Student
from .serializers import UserInfoserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt 
import json

def userinfo(request):
    
    user = UserInfo.objects.get(username = 'kunal')
    serializer = UserInfoserializer(user)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

# Query Set - All Userdata retrive
def userlist(request):
    user = UserInfo.objects.all()
    serializer = UserInfoserializer(user,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

# this is for access data into third party app and save into database
@csrf_exempt
def usercreate(request):
    # convert to python  Dictionary
    json_data = json.loads(request.body)
    print(type(json_data))

# If GET read the data fom the database
    if(request.method == "GET"):
        # for i in range (len(json_data)):
        # strem = io.BytesIO(json_data)
        # pythondata = JSONParser().parse(strem)
        uname = json_data.get('username',None)
        if uname is not None:
            try:
                user = UserInfo.objects.get(username = uname)
                serializer = UserInfoserializer(user)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
                # return JsonResponse(serializer.data)
            except:
                j = {"msg":"Record not found"}
                json_data = JSONRenderer().render(j)
                return HttpResponse(json_data, content_type='application/json')
        else:
            user = UserInfo.objects.all()
            serializer = UserInfoserializer(user, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
            # return JsonResponse(serializer.data)

# elif PUT data Update
    elif(request.method =='PUT'):
        json_data = json.loads(request.body)
        uname = json_data.get('username')
        try:
            user = UserInfo.objects.get(username=uname)
            serializer = UserInfoserializer(user,data=json_data, partial=True)
            if(serializer.is_valid()):
                serializer.save()
                msg = {'msg':'Record Updated'}
                json_data = JSONRenderer().render(msg)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JsonResponse().render(serializer.errors)
            return HttpResponse(j, content_type='application/json')
        except:
            msg = {'msg':'Record Invalid'}
            return JsonResponse(msg )

# elif DELETE Record
    elif(request.method =='DELETE'):
        json_data = json.loads(request.body)
        uname = json_data.get('username')
        try:
            user = UserInfo.objects.get(username = uname)
            user.delete()
            msg = {'msg':'Record Delete'}
            return JsonResponse(msg , safe = False)
        except:
            msg = {'msg':'Record Invalid'}
            return JsonResponse(msg )

# else POST data add into database
    else:
        for i in json_data:
            serializer = UserInfoserializer(data = i)
            if(serializer.is_valid()):
                serializer.save()
        j = {"msg":"User Add"}
        json_data = JSONRenderer().render(j)
        return HttpResponse(json_data, content_type='application/json')

        json_data = JsonResponse().render(serializer.errors)
        return HttpResponse(j, content_type='application/json')

def masterpage(request):
    return render(request,"masterpage.html",{})
# Create your views here.
def signup(request):
    if(request.method == "GET"):
        return render(request,"signup.html",{})
    else:
        fname = request.POST["fname"] 
        lname = request.POST["lname"] 
        uname = request.POST["uname"] 
        email = request.POST["email"] 
        password = request.POST["pass"]
        list = ['!','@','#','$']
        for i in list:
            if(i in password):
                try:
                    user = UserInfo.objects.get(username = uname)
                    msg = "This username already present Plz enter diff username"
                    return render(request,"signup.html",{"msg":msg})
                except:
                    user = UserInfo()
                    user.fname = fname
                    user.lname = lname
                    user.username = uname
                    user.email = email
                    user.password = password
                    user.save()
                    return redirect(login)
        else:
            msg = "Add at last one special charecter (eg.!@#$)"
            return render(request,"signup.html",{"msg":msg})


        
def login(request):
    if(request.method == "GET"):
        u = UserInfo.objects.all()
        return render(request,"login.html",{"u":u})
    else:
        uname = request.POST["uname"] 
        password = request.POST["pass"]
        try:
            user = UserInfo.objects.get(username = uname,password = password)
            request.session["uname"] = uname
            return render(request,"wellcome.html",{'user':user})
        except:
            msg = "Userid and password Does not match"
            return render(request,"login.html",{"msg":msg})
        
def signout(request):
    request.session.clear()
    return redirect(masterpage)

def addstudent(request):
    if(request.method == "GET"):
        user = UserInfo.objects.all()
        return render(request,"addstudent.html",{'user':user})
    else:
        sid = request.POST["sid"]
        sname = request.POST["sname"]
        uname = request.POST["uname"]
        city = request.POST["city"]
        std = Student()
        std.sid = sid
        std.sname = sname
        std.city = city
        std.username_id = uname
        std.save()
        return redirect(masterpage)


            

