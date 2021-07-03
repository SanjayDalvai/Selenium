import requests
import jsonpath

#requests.get method fetches the URL and saves in variable resp
resp = requests.get("https://randomusers.me/api/?results=2")

#resp.json() will produce json format and saves in resp_json variable
resp_json = resp.json()


#To get the Usrename and prints the same
username_1 = resp_json["results"][0]["username"]
print(username_1)


#To get the email and prints the same
email_1 = resp_json["results"][0]["login"]["email"]
print(email_1)


#To get the password and prints the same
password_1 = resp_json["results"][0]["login"]["password"]
print(password_1)
