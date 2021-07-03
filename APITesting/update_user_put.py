import requests
#import jsonpath
import json

#p={"page":2}

mydata = open("data.json", "r").read()

resp = requests.put("https://reqres.in/api/users",data=json.loads(mydata))
print(resp)
print(resp.json())
print(resp.headers.get("Content-Type"))
assert resp.json()["job"]=='india'
