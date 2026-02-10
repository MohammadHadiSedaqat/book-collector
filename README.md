# OpenLibrary Book Collector

A simple Python script for fetcاing books from OpenLibrary, with after 2000 publish year, and save the results into a nicely formatted CSV file.

## Features
- Fetches 50 books from OpenLibrary based on a search query (default: "python").
- Filters out books which published before 2000.
- Collects key information: Title, Language, Publish Year, Ebook Access, and Author(s).
- Saving data into a CSV file (books_file.csv) with spacing.

## Requirements
- Python 3.7+
- 'requests' library

You can install the required library using:
```bash
pip install requests
```

And run the script through:
```bash
python openlibrary_book_collector.py
```
