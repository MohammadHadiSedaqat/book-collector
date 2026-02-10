import requests
import csv

library_url = "https://openlibrary.org/search.json?q=python&limit=58"
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

with open("books_file.csv", "w", newline="") as csvfile:
    csvfile.write(f"{"Title":<75} {"Language":<30} {"Publish Year":<15} {"Ebook Access":<25} {"Author"}\n")
    csvfile.write("-"*180 +"\n")

    for book in requested_books:
        csvfile.write(f"{book['title']:<75} {book['language']:<30} {book['publish_year']:<15} {str(book['ebook_access']):<25} {book['author']}\n")