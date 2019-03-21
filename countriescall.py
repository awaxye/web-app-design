import requests

countries = {"one": "Spain", "two": "Sweden"}
r = requests.post("http://vcm-7631.vm.duke.edu:5000/compare", json=countries)
print(r.json())

URL="http://vcm-7631.vm.duke.edu:5000"
r2 = requests.get(URL+"/regions")
print(r2.json())


