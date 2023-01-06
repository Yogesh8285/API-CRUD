from django.shortcuts import render,redirect
from .models import UserInfo,Student
from .serializers import UserInfoserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt 
import json
from django.utils.decorators import method_decorator
from rest_framework.views import View

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


@method_decorator(csrf_exempt,name='dispatch')
class User_Info(View):
        # this is for access data into third party app and save into database
        # convert to python  Dictionary
    def get(self,request,*args,**kwargs):
        json_data = json.loads(request.body)
        # If GET read the data fom the database
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
    def put(self,request,*args,**kwargs):
    # elif PUT data Update
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
    def delete(self,request,*args,**kwargs):
    # elif DELETE Record
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

    def post(self,request,*args,**kwargs):
    # else POST data add into database
        json_data = json.loads(request.body)
        for i in json_data:
            serializer = UserInfoserializer(data = i)
            if(serializer.is_valid()):
                serializer.save()
        j = {"msg":"User Add"}
        json_data = JSONRenderer().render(j)
        return HttpResponse(json_data, content_type='application/json')

        json_data = JsonResponse().render(serializer.errors)
        return HttpResponse(j, content_type='application/json')
