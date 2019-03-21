import requests

r = requests.get("http://vcm-7631.vm.duke.edu:5000/list")

print(r.json())


