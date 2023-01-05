import json
a = {"fname": "Pavan", "lname": "patil", "username": "pawan12", "email": "nk@gmail.com", "password": "pawan@123"}, {"fname": "Mayur", "lname": "patil", "username": "mayur12", "email": "nk@gmail.com", "password": "mayur@123"}

j = json.dumps(a)
l = json.loads(j)
print(j)
print("-----------------")
print(l)
print("---------------------")
print(type(a))
print(type(j))
print(type(l))