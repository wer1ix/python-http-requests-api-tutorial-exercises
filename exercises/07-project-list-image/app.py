import requests

request = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")

data = request.json()
last_item = data[-1]
last_image = last_item['images'][-1]
print(last_image)