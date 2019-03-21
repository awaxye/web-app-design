import requests

r = requests.get("https://api.github.com/repos/awaxye/BME547/branches")
print(r)
answer = r.json()
print(answer)
for branch in answer:
    print(branch["name"])