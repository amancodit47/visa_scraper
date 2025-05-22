# 🧰 VisaFriendly Data Engineer Job Scraper

## 🌐 Overview
This project is a take-home assessment for the **Data Engineer Intern** position at **VisaFriendly**.  
The system is designed to scrape the latest "Data Engineer" job listings, filter them by H-1B sponsoring companies, and store the structured results in an SQLite database. The entire workflow is automated to run every hour.

---

## 🚀 Tech Stack

- **Python 3**
- **SerpAPI** (Google Jobs API)
- **SQLite** (lightweight, SQL-compatible database)
- **pandas** (data transformation)
- **requests** (HTTP API interaction)
- **python-dotenv** (secret management)
- **Windows Task Scheduler** (for hourly automation)

---

## ✅ Features

### 🔍 Web Scraping
Fetches "Data Engineer" job postings from **Google Jobs** within the **last 1 hour** using SerpAPI.

### 🧠 Data Extraction
Each job listing includes:
- ✅ Job Title  
- ✅ Company Name  
- ✅ Location  
- ✅ Job Type (Full-Time, Contract, Internship)  
- ✅ Work Setting (Remote, Hybrid, Onsite)  
- ✅ Job Description  
- ✅ Application Link (if available)  
- ✅ Posting Time  

### 🎯 H-1B Sponsorship Filtering
Filters job listings based on a list of verified **H-1B sponsoring companies** (CSV-based).

### 🗃️ Structured Database Storage
Filtered jobs are saved to an **SQLite database (`jobs.db`)** using a clean, normalized schema.  
Duplicate prevention is handled via hashing of job attributes or uniqueness constraints.

### 🔁 Hourly Automation
Scheduled to run every hour using **Windows Task Scheduler**:
- Avoids duplicate entries  
- Continuously fetches new listings  
- Fully autonomous

---

## 📁 Project Structure

```bash
WEB_SCRAPPER/
├── __pycache__/                # Cached Python bytecode
├── .env                        # Contains SerpAPI key (excluded from Git)
├── db_loader.py                # Handles database insertion
├── h1bcompanies_list.csv       # List of H-1B sponsoring companies
├── jobs.db                     # SQLite database file
├── output.csv                  # Optional: Raw scraped job data
├── read_jobs.py                # Utility to read and inspect DB contents
├── readme.md                   # Project documentation (this file)
├── requirements.txt            # Project dependencies
└── scrape_jobs.py              # Main pipeline: scrape → filter → load
⚙️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/amancodit47/visa_scraper.git
cd visa_scraper/WEB_SCRAPPER
2. Install Python Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Add SerpAPI Key
Create a .env file in the root directory:

ini
Copy
Edit
SERPAPI_API_KEY=your_api_key_here
Alternatively, you can hardcode it in scrape_jobs.py (not recommended for security reasons).

4. Run the Pipeline Manually
bash
Copy
Edit
python scrape_jobs.py
5. View Stored Jobs
bash
Copy
Edit
python read_jobs.py
🤖 Setting Up Automation (Windows)
To run the script hourly, set up Windows Task Scheduler:

Open Task Scheduler

Click Create Basic Task

Set Trigger to Daily → Repeat every 1 hour

Under Actions, choose Start a Program

Set Program/script to:

pgsql
Copy
Edit
path\to\python.exe
And Add arguments:

pgsql
Copy
Edit
path\to\scrape_jobs.py
Done! Your scraper is now on autopilot.

👨‍💻 Author
Aman

GitHub: @amancodit47

Email: amancodit2004@gmail.com