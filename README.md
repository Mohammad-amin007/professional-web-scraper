# 🚀 Professional Web Scraper

A production-ready web scraping template built with Python.

This project demonstrates how to build a scalable, maintainable, and extensible web scraper using modern Python development practices.

It is designed as a reusable template for scraping different websites by simply implementing new scraper classes.

---

## ✨ Features

- ✅ Clean Architecture
- ✅ Object-Oriented Design
- ✅ Async SQLAlchemy
- ✅ SQLite Database
- ✅ Docker Support
- ✅ Docker Compose
- ✅ CLI Commands
- ✅ Scheduler
- ✅ HTTP Client with Retry
- ✅ Logging
- ✅ CSV Export
- ✅ Excel Export
- ✅ Environment Variables
- ✅ Unit Tests
- ✅ Production Ready Structure
## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/professional-web-scraper.git
```

Move into the project:

```bash
cd professional-web-scraper
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Create a `.env` file:

```text
SCRAPER_BASE_URL=https://books.toscrape.com/

SCRAPER_TIMEOUT=15

SCRAPER_RETRY_COUNT=3

LOG_LEVEL=INFO
```

---

## ▶️ Quick Start

Run the scraper:

```bash
python cli.py scrape
```

Show analytics:

```bash
python cli.py analytics
```

Export data:

```bash
python cli.py export
```
---

## 🐳 Running with Docker

Build the container:

```bash
docker compose build
```

Run the application:

```bash
docker compose up
```

Run in detached mode:

```bash
docker compose up -d
```

Stop containers:

```bash
docker compose down
```

---

## 📁 Project Structure

```text
Professional-Web-Scraper
│
├── app.py
├── cli.py
├── scheduler_runner.py
├── config.py
├── database.py
│
├── scrapers/
│   ├── base_scraper.py
│   └── example_scraper.py
│
├── services/
│   ├── analytics_service.py
│   ├── book_service.py
│   ├── cli_service.py
│   ├── export_service.py
│   └── storage_service.py
│
├── storage/
│   ├── models.py
│   └── scraper.db
│
├── models/
│   └── book.py
│
├── tests/
│
├── exports/
├── logs/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env.example
```
---

## 🏗 Architecture

The project follows a modular and layered architecture.

```text
CLI / Scheduler
        │
        ▼
Application Pipeline
        │
        ▼
Scrapers
        │
        ▼
Storage Services
        │
        ▼
Database
        │
        ▼
Analytics / Export
```

Each layer has a single responsibility, making the project easy to maintain and extend.

---

## 🛠 Technologies

- Python 3.14
- BeautifulSoup4
- Requests
- SQLAlchemy (Async)
- SQLite
- Pandas
- OpenPyXL
- Docker
- Docker Compose
- Pytest

---

## ✅ Testing

Run all tests:

```bash
pytest
```

Current test coverage includes:

- Scraper
- HTTP Client
- Storage Service
- Analytics Service

Example:

```text
========================
5 passed in 0.42s
========================
```
---

## 🚀 Roadmap

Future improvements planned for this template:

- [ ] Support multiple websites
- [ ] JSON Export
- [ ] REST API integration
- [ ] PostgreSQL support
- [ ] Redis caching
- [ ] Parallel scraping
- [ ] HTML reports
- [ ] Performance metrics

---

## 🧩 Using this as a Template

This project was designed to be reusable.

To scrape a new website:

1. Create a new scraper inside the `scrapers/` package.
2. Implement the `parse()` method.
3. Create or update the corresponding data model.
4. Run:

```bash
python cli.py scrape
```

The rest of the pipeline (storage, analytics, export, logging, scheduler, Docker, CLI) will continue to work without modification.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the project and submit a pull request.

---

## 📄 License

This project is released under the MIT License.