import requests
import json

URL = "http://127.0.0.1:8000/usercreate/"

data = [{ 
    'fname': '5678',
    'lname': 'patil',
    'username': 'yrk',
    'email': 'nk@gmail.com',
    'password':'pawan@123'}]

json_data = json.dumps(data)

r = requests.post(url = URL , data = json_data)
# # print(json_data)
# # print(type(json_data))
data = r.json()
print(data)