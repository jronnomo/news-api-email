import os
import requests
from send_email import send_email
from dotenv import load_dotenv

load_dotenv()
api = os.getenv("API")
topic = "crypto"
url = f"https://newsapi.org/v2/everything?q={topic}& \
sortBy=publishedAt&apiKey={api}&language=en"

request = requests.get(url)
content = request.json()
articles = content["articles"]

email_content = f"""\
Subject: Daily News Bites

Here are your list of news summaries:

"""

article_content = []
str_article_content = ""

for article in articles[:10]:
    title = article["title"]
    url = article["url"]
    description = article["description"]
    article_content.append(f"Title: {title}")
    article_content.append(f"Open full story here: {url}")
    article_content.append(f"Bite: {description}")
    article_content.append('\n')


str_article_content = "\n".join(article_content)
email_content = email_content + str_article_content
send_email(email_content.encode('utf-8'))
