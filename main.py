import requests
from bs4 import BeautifulSoup

response_situation = requests.get("https://openlibrary.org/search.json?q=python&limit=50")
print("situation: " + str(response_situation.status_code))

data = response_situation.json()
books_info = data['docs'][:50]

books = [b for b in books_info if 'first_publish_year' in b and b['first_publish_year'] > 2000]
for result in books:
    print(result)