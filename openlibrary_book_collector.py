"""
Fetching books from openlibrary,
with after 2000 publish year,
by saving them into a csv file.
"""

import requests

LIBRARY_URL = "https://openlibrary.org/search.json?q=python&limit=58"

def filter_book_func(books_info):
    books_over_2000 = [book for book in books_info
                       if 'first_publish_year' in book
                       and book['first_publish_year'] > 2000]
    return books_over_2000

def requested_books_items_func(books_over_2000):
    requested_books = []
    for book in books_over_2000:
        requested_books.append({
            "title": book.get('title'),
            "language": ",".join(book.get('language', [])),
            "publish_year": book.get('first_publish_year'),
            "ebook_access": book.get('ebook_access'),
            "edition_count": book.get('edition_count'),
            "author": ",".join(book.get('author_name', [])),
        })
    return requested_books

def save_into_csv_func(requested_books):
    with open("books_file.csv", "w", newline="", encoding="utf-8") as csvfile:
        csvfile.write(f"{'Title':<75}{'Language':<30}"
                      f"{'Publish Year':<15}{'Ebook Access':<25}"
                      f"{'Edition Count':<15}{'Author'}\n")
        csvfile.write("-" * 180 + "\n")

        for book in requested_books:
            csvfile.write(f"{book['title']:<75}"
                          f"{book['language']:<30}{book['publish_year']:<15}"
                          f"{str(book['ebook_access']):<25}"
                          f"{book['edition_count']:<15}{book['author']}\n")
        csvfile.close()

def main():
    try:
        response_situation = requests.get(LIBRARY_URL, timeout=10)
        print("status: " + str(response_situation.status_code))
        data = response_situation.json()
    except requests.exceptions.Timeout:
        print("Not finding...")
        data = {"docs": []}
    except requests.exceptions.RequestException as e:
        data = {"docs": []}
        print(e)

    books_info = data['docs']
    books_over_2000 = filter_book_func(books_info)
    requested_books = requested_books_items_func(books_over_2000)
    save_into_csv_func(requested_books)

if __name__ == "__main__":
    main()
