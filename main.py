import requests

api = "7e548c30caf54a6f9ecd700b9fc51f28"
url = f"https://newsapi.org/v2/everything?q=tesla& \
sortBy=publishedAt&apiKey={api}"

request = requests.get(url)
content = request.json()
articles = content["articles"]
for article in articles:
    print(article["title"])