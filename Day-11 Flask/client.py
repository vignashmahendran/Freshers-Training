import requests
import json
ip="http://127.0.0.1:5000"
name=input("Enter name To get : ")
respose=requests.get(ip+"/"+name)
try:
    print(respose.json())
except Exception:
    print("name Not exist")
