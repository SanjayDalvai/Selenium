import requests

p={"page":2}
resp = requests.get("https://reqres.in/api/users",params=p)

json_resp = resp.json()

print(json_resp['total_pages'])
assert json_resp['total_pages'] == 2 , 'total pages dosent match'


print(json_resp['total'])
assert json_resp['total'] == 12 , 'total dosent match'

print(json_resp["data"][0]["email"])
assert (json_resp["data"][0]["email"]).endswith("reqres.in"), "email format is not matching"

print(json_resp["data"][4]["first_name"])
assert (json_resp["data"][4]["first_name"]) != None
