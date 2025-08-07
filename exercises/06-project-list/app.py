import requests

request = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")

data = request.json()
print(data[1]['name'])