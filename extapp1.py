import requests
import json

URL = "http://127.0.0.1:8000/usercreate/"
print('''
    1.Fetch Record
    2.Add New Record
    3.Update Record
    4.Delete Record
    5.Exit'''
    )
ch = 0
while(ch !=5):
    ch = int(input("Enter ur choice :"))
    if(ch == 1):
        def get_data(uname = None):
            data = {}

            if uname is not None:
                data = {'username': uname}
            json_data = json.dumps(data)

            r = requests.get(url= URL, data=json_data)

            data = r.json()
            print(data)
        n = input()
        if(len(n) == 0):
            get_data()
        else:
            get_data(n)
    elif(ch == 2):
        def post_data():
            data = [{
                'fname':'amol',
                'lname': 'khairnar',
                'username': 'afyy',
                'email': 'yk@gmail.com',
                'password':'yogesh@123'},
                {
                'fname':'mayury',
                'lname': 'khairnar',
                'username': 'wevfg',
                'email': 'yk@gmail.com',
                'password':'yogesh@123'}]

            json_data = json.dumps(data)
            r = requests.post(url = URL, data = json_data)
            data = r.json()
            print(data)
        post_data()

    elif(ch == 3):
        def update_data():
            data = {
                'fname':'asdf',
                'username': 'amol',
                'email': 'yk@gmail.com',
                'password':'yogesh@123'}

            json_data = json.dumps(data)
            r = requests.put(url = URL, data = json_data)
            data = r.json()
            print(data)
        update_data()
    elif(ch == 4):
        def delete_data():
            data = {'username':'amol'}
            json_data = json.dumps(data)
            r = requests.delete(url = URL ,data = json_data)
            data = r.json()
            print(data)
        delete_data()
    elif(ch == 5):
        print("thanks...!")