# 🚀 Professional Web Scraper

A production-style web scraping and data processing pipeline built with Python.

This project demonstrates how to build a scalable, maintainable, and reusable scraper system with structured data extraction, database storage, analytics, and multiple export formats.

---

## 📌 Overview

Professional Web Scraper is a modular scraping framework designed to extract product data from websites and process it through a complete data pipeline.

The project includes:

- Multi-page scraping
- Structured data extraction
- Async database storage
- Data analytics
- CSV / Excel / JSON export
- CLI interface
- Automated testing
- Docker support

The architecture is designed to be reusable. New websites can be supported by creating new scraper implementations without changing the core pipeline.

---

# ✨ Features

## Web Scraping

- ✅ Multi-page crawling with pagination support
- ✅ HTML parsing with BeautifulSoup
- ✅ Product information extraction
- ✅ Retry mechanism
- ✅ Timeout handling
- ✅ Custom User-Agent support
- ✅ Modular scraper architecture


## Data Processing

- ✅ Structured data models
- ✅ Async SQLAlchemy integration
- ✅ SQLite database storage
- ✅ Duplicate prevention using product URL
- ✅ Analytics generation


## Export

- ✅ CSV export
- ✅ Excel export
- ✅ JSON export


## Development

- ✅ Clean architecture
- ✅ Environment configuration
- ✅ Logging system
- ✅ CLI commands
- ✅ Docker support
- ✅ Docker Compose
- ✅ Automated tests

---

# 🏗 Architecture

The project follows a layered architecture:

```
CLI
 |
 v
Application Pipeline
 |
 v
Scraper Layer
 |
 v
Parser Layer
 |
 v
Storage Service
 |
 v
Database
 |
 +----------------+
 |                |
 v                v
Analytics       Export
                 |
                 +--> CSV
                 +--> Excel
                 +--> JSON
```

---

# 🔄 Data Pipeline

```
Website
   |
   v
HTTP Client
   |
   v
Scraper
   |
   v
Parser
   |
   v
Book Model
   |
   v
Database Storage
   |
   +----------------+
   |                |
   v                v
Analytics        Export
```

---

# 📊 Extracted Data

Each product contains:

```json
{
    "title": "A Light in the Attic",
    "price": 51.77,
    "availability": "In stock",
    "rating": 3,
    "product_url": "https://books.toscrape.com/..."
}
```

---

# 🛠 Technologies

- Python 3.14
- BeautifulSoup4
- Requests
- SQLAlchemy 2
- SQLite
- Pandas
- OpenPyXL
- APScheduler
- Pytest
- Docker
- Docker Compose

---

# 📂 Project Structure

```
Professional-Web-Scraper/

├── app.py
├── cli.py
├── config.py
├── database.py
├── scheduler_runner.py

├── scrapers/
│   ├── base_scraper.py
│   └── example_scraper.py

├── services/
│   ├── http_client.py
│   ├── storage_service.py
│   ├── export_service.py
│   ├── analytics_service.py
│   ├── book_service.py
│   └── cli_service.py

├── models/
│   └── book.py

├── storage/
│   └── models.py

├── tests/

├── exports/

├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/Mohammad-amin007/professional-web-scraper.git
```

Move into project:

```bash
cd Professional-Web-Scraper
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔧 Configuration

Create a `.env` file:

```env
SCRAPER_BASE_URL=https://books.toscrape.com/

SCRAPER_TIMEOUT=15

SCRAPER_RETRY_COUNT=3

LOG_LEVEL=INFO
```

---

# ▶️ Usage

## Run Full Scraper Pipeline

```bash
python cli.py scrape
```

This will:

1. Crawl all pages
2. Extract product data
3. Store records in database
4. Run analytics
5. Generate exports


---

## Show Analytics

```bash
python cli.py analytics
```

Example:

```
Total books: 1000
Average price: £35.07

Most expensive:
The Perfect Play (£59.99)

Cheapest:
An Abundance of Katherines (£10.00)
```

---

## Export Data

```bash
python cli.py export
```

Generated files:

```
exports/

├── books.csv
├── books.xlsx
└── books.json
```

---

# 🐳 Docker

Build container:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

Run in background:

```bash
docker compose up -d
```

Stop:

```bash
docker compose down
```

---

# 🧪 Testing

Run test suite:

```bash
pytest -q
```

Current test result:

```
11 passed
```

Tests include:

- HTTP Client
- Scraper Parser
- Pagination
- Storage Service
- Analytics Service
- CSV Export
- Excel Export
- JSON Export

---

# 📈 Example Output

```
Total books: 1000

Average price: £35.07

Most expensive:
The Perfect Play (Play by Play #1)
£59.99

Cheapest:
An Abundance of Katherines
£10.00


CSV exported successfully

Excel exported successfully

JSON exported successfully
```

---

# 🚀 Future Improvements

Planned improvements:

- PostgreSQL support
- Redis caching
- Parallel scraping workers
- REST API integration
- Web dashboard
- Advanced monitoring
- Distributed scraping architecture

---

# 👨‍💻 Author

Mohammad Amin

Python Developer

Built with Python and modern backend development practices.