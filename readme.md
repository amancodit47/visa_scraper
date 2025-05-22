# VisaFriendly Data Engineer Job Scraper

## Overview
This project scrapes "Data Engineer" job listings from Google Jobs, filters by H-1B sponsoring companies, and stores results in a SQLite database.

## Technologies Used
- Python
- SerpAPI (Google Jobs API)
- SQLite
- Windows Task Scheduler (for automation)
- pandas, requests, datetime

## Features
- Extracts job title, company, location, job type, work setting, description, apply link, and posting time.
- Filters by a list of H-1B sponsoring companies.
- Stores results in `jobs.db`.
- Runs every hour using Task Scheduler.

## How to Run
1. Set your SerpAPI API key in `scrape_jobs.py`
2. Run manually:
