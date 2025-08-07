import requests

def get_attachment_by_id(attachment_id):
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        for post in data["posts"]:
            if "attachments" in post:
                for attachment in post['attachments']:
                    if attachment['id'] == attachment_id:
                        return attachment['title']
        print("No attachment found") 

    else:
        print("Failed to fetch data from the endpoint.")

print(get_attachment_by_id(137))