import requests

url = "https://assets.breatheco.de/apis/fake/sample/random-status.php"

for _ in range (10):
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        print(response.text)
    else:
        print("Something went wrong")