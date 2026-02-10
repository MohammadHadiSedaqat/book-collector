import requests
import csv

library_url ="https://openlibrary.org/search.json?q=python&limit=58"
response_situation = requests.get(library_url)

print("status: " + str(response_situation.status_code))
data = response_situation.json()
books_info = data['docs']

books_over_2000 = [book for book in books_info if 'first_publish_year' in book and book['first_publish_year'] > 2000]
# for result in books_over_2000:
#     print(result)

requested_books = []
for book in books_over_2000:
    requested_books.append({
        "title": book.get('title'),
        "language": ",".join(book.get('language', [])),
        "publish_year": book.get('first_publish_year'),
        "ebook_access": book.get('ebook_access'),
        "author": ",".join(book.get('author_name', [])),
    })

# for book in requested_books:
#     print(book["title"], book["language"], book["publish_year"], book["ebook_access"], book["author"])

keys = ["title", "language", "publish_year", "ebook_access", "author"]

with open('books.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=keys)
    writer.writeheader()
    writer.writerows(requested_books)