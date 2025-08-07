import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
x = response.json()

print(f"Current time: {x['hours']} hrs {x['minutes']} min and {x['seconds']} sec")
