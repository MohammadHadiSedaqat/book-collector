<div align="center">

# 📖 OpenLibrary Book Fetcher
### ⚡ Python Backend • API Integration • CSV Export

![Python](https://img.shields.io/badge/Python-3.7+-blueviolet?style=for-the-badge&logo=python)
![Data Live](https://img.shields.io/badge/Data-Live-red?style=for-the-badge)
![API Access](https://img.shields.io/badge/OpenLibrary-API-orange?style=for-the-badge)
![CSV Ready](https://img.shields.io/badge/CSV-Ready-green?style=for-the-badge)
![Modular](https://img.shields.io/badge/Modular-Code-purple?style=for-the-badge)

A lightweight Python backend script to fetch book data from OpenLibrary, filter modern publications (after 2000), and export structured results to a neat CSV file.

</div>

---

## ✨ Overview

This project demonstrates a **real-world backend workflow**:

1. Fetch live book data from an API  
2. Filter based on publishing year  
3. Transform raw JSON to structured data  
4. Export results to a **readable CSV file**

Perfect for learning **API handling, data processing, and modular Python scripting**.

---

## 🎯 Core Features

- Fetch up to 50 books per query from OpenLibrary  
- Filter out books published **before 2000**  
- Extract important fields:
  - 📌 **Title**  
  - 🌐 **Language**  
  - 📅 **First Publish Year**  
  - 💻 **Ebook Access**  
  - 🏷️ **Edition Count**  
  - ✍️ **Author(s)**  
- Export results into a **well-formatted CSV file**  
- Modular, easy-to-read Python functions  

---

## ⚡ How It Works

### 1️⃣ Fetch Data
The script sends a GET request to the OpenLibrary API and retrieves book data related to a Python query.

### 2️⃣ Filter Data
Books are filtered according to:

- Availability of a publish year  
- Year of publication after **2000**

### 3️⃣ Transform Data
Selected records are transformed to include:

- Title  
- Language  
- Publish Year  
- Ebook Access Status  
- Edition Count  
- Author Names  

### 4️⃣ Export Data
The processed books are saved into a **formatted CSV file** (`books_file.csv`) for easy reading and further use.

---

## ⚙️ Requirements

- Python 3.7+  
- `requests` library

Install dependencies with:

```bash
pip install requests
