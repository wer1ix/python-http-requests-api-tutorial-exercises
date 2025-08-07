import requests

request = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

items = request.json()
posts = items['posts'][0]['author']['name']

print(posts)