import requests
import jsonpath



resp = requests.get("https://randomusers.me/api/?results=2")

code = resp.status_code
print(code)
#assert code == 200 , "Response Code dosent Match"

#print(resp.text)
#print(resp.content):p
#print(resp.json())
# print(type(resp.headers))
# print(resp.headers)
# print(resp.cookies)
# print(resp.url)
