import requests

def get_titles():
    titles = []
    request = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    items = request.json()
    for post in items['posts']:
        titles.append(post['title'])
    
    return titles

print(get_titles())