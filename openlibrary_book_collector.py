"""
Fetching books from openlibrary,
with after 2000 publish year,
by saving them into a csv file.
"""

import requests

LIBRARY_URL = "https://openlibrary.org/search.json?q=python&limit=58"

try:
    response_situation = requests.get(LIBRARY_URL, timeout=5)
    print("status: " + str(response_situation.status_code))
    data = response_situation.json()
except requests.exceptions.Timeout:
    print("Not finding...")
    data = {"docs":[]}
except requests.exceptions.RequestException as e:
    data = {"docs": []}
    print(e)

books_info = data['docs']
books_over_2000 = [book for book in books_info
                   if 'first_publish_year' in book
                   and book['first_publish_year'] > 2000]

requested_books = []
for book in books_over_2000:
    requested_books.append({
        "title": book.get('title'),
        "language": ",".join(book.get('language', [])),
        "publish_year": book.get('first_publish_year'),
        "ebook_access": book.get('ebook_access'),
        "author": ",".join(book.get('author_name', [])),
    })

with open("books_file.csv", "w", newline="" ,encoding="utf-8") as csvfile:
    csvfile.write(f"{'Title':<75}{'Language':<30}"
                  f"{'Publish Year':<15}{'Ebook Access':<25}{'Author'}\n")
    csvfile.write("-" * 180 +"\n")

    for book in requested_books:
        csvfile.write(f"{book['title']:<75}"
                      f"{book['language']:<30}{book['publish_year']:<15}"
                      f"{str(book['ebook_access']):<25}{book['author']}\n")
    csvfile.close()
