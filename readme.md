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
- Stores results in jobs.db.
- Runs every hour using Task Scheduler.

## How to Run
1. Set your SerpAPI API key in scrape_jobs.py
2. Run manually:

# Daily List of Visa-Sponsored Data Engineering Job Opportunities Updated Hourly

| Company          | Job Title        | Location                        | Added        | Visa Sponsorship | Link                                                                                  |
|------------------|------------------|--------------------------------|--------------|------------------|---------------------------------------------------------------------------------------|
| Speakap          | Data Engineering | Amsterdam, Netherlands          | May 20, 2025 | Yes              | [Apply](https://jobs.speakap.com/o/frontend-developer)                               |
| N26              | Data Engineering | Berlin, Germany                | May 19, 2025 | Yes              | [Apply](https://n26.com/en-eu/careers/positions/6683900)                            |
| N26              | Data Engineering | Berlin, Germany                | May 19, 2025 | Yes              | [Apply](https://n26.com/en-eu/careers/positions/6744192)                            |
| Mistral AI       | Data Engineering | Paris 🇫🇷 / London 🇬🇧 / Palo Alto 🇺🇸 | May 18, 2025 | Yes              | [Apply](https://jobs.lever.co/mistral/df3d4b5c-4910-42c8-8fe8-5fd114b2961a)         |
| Mistral AI       | Data Engineering | Paris 🇫🇷 / London 🇬🇧          | May 18, 2025 | Yes              | [Apply](https://jobs.lever.co/mistral/07447e1d-7900-46d4-b61b-186f2f76847f)         |
| Mistral AI       | Data Engineering | Paris 🇫🇷 / London 🇬🇧          | May 18, 2025 | Yes              | [Apply](https://jobs.lever.co/mistral/675b7f06-a76b-4144-af0c-4dd3282ef489)         |
| Mistral AI       | Data Engineering | Palo Alto, USA                 | May 18, 2025 | Yes              | [Apply](https://jobs.lever.co/mistral/ef2d793d-fe94-4707-9535-b662c5a8c59c)         |
| Mistral AI       | Data Engineering | Paris, France                 | May 18, 2025 | Yes              | [Apply](https://jobs.lever.co/mistral/a1854159-922e-4de7-adb6-7c1b608c147f)         |
| Mistral AI       | Data Engineering | Paris 🇫🇷 / London 🇬🇧 / Singapore | May 18, 2025 | Yes              | [Apply](https://jobs.lever.co/mistral/77f6fd1b-65cf-45d8-9b68-594c62732f62)         |
| Mistral AI       | Data Engineering | Paris                         | May 18, 2025 | Yes              | [Apply](https://jobs.lever.co/mistral/9f6e6513-fd9e-411b-b558-540bc12b2fe4)         |
| Mistral AI       | Data Engineering | Paris, France                 | May 18, 2025 | Yes              | [Apply](https://jobs.lever.co/mistral/e1a37c33-fdec-41cf-bb92-35646e283fa8)         |
| Mistral AI       | Data Engineering | Palo Alto, USA                | May 18, 2025 | Yes              | [Apply](https://jobs.lever.co/mistral/3db45045-b1a5-4c5d-9608-0aa7fb66f2df)         |
| Mistral AI       | Data Engineering | Palo Alto, USA                | May 18, 2025 | Yes              | [Apply](https://jobs.lever.co/mistral/b5b565a0-533a-43c3-b232-114138422cb0)         |
| Optiver          | Data Engineering | Amsterdam, Netherlands         | May 10, 2025 | Yes              | [Apply](https://optiver.com/working-at-optiver/career-opportunities/7475519002/)     |
| Robin AI         | Data Engineering | London, United Kingdom         | May 10, 2025 | Yes              | [Apply](https://www.robinai.com/open-positions?ashby_jid=0c8ba130-9f6a-4a32-8d1f-08b3364f9e8c/) |
| Robin AI         | Data Engineering | London, United Kingdom         | May 10, 2025 | Yes              | [Apply](https://www.robinai.com/open-positions?ashby_jid=19292bff-1586-4bbd-b593-69b5a0c5263e/) |
| Optiver          | Data Engineering | Amsterdam, Netherlands         | May 10, 2025 | Yes              | [Apply](https://optiver.com/working-at-optiver/career-opportunities/7790567002/)     |
| Optiver          | Data Engineering | Amsterdam, Netherlands         | May 10, 2025 | Yes              | [Apply](https://optiver.com/working-at-optiver/career-opportunities/7694007002/)     |
| Optiver          | Data Engineering | Amsterdam, Netherlands         | May 10, 2025 | Yes              | [Apply](https://optiver.com/working-at-optiver/career-opportunities/7746651002/)     |
| Optiver          | Data Engineering | Amsterdam, Netherlands         | May 10, 2025 | Yes              | [Apply](https://optiver.com/working-at-optiver/career-opportunities/7684971002/)     |
| Optiver          | Data Engineering | Amsterdam, Netherlands         | May 10, 2025 | Yes              | [Apply](https://optiver.com/working-at-optiver/career-opportunities/7790593002/)     |
| Optiver          | Data Engineering | Amsterdam, Netherlands         | May 10, 2025 | Yes              | [Apply](https://optiver.com/working-at-optiver/career-opportunities/7790505002/)     |
| Optiver          | Data Engineering | Amsterdam, Netherlands         | May 10, 2025 | Yes              | [Apply](https://optiver.com/working-at-optiver/career-opportunities/7790490002/)     |
| Optiver          | Data Engineering | Amsterdam, Netherlands         | May 10, 2025 | Yes              | [Apply](https://optiver.com/working-at-optiver/career-opportunities/7640612002/)     |
| Recharge         | Data Engineering | Amsterdam, Netherlands         | May 10, 2025 | Yes              | [Apply](https://company.recharge.com/vacancies/senior-fullstack-engineer-1/)        |
| Recharge         | Data Engineering | Amsterdam, Netherlands         | May 10, 2025 | Yes              | [Apply](https://company.recharge.com/vacancies/senior-business-analyst/)             |
| Recharge         | Data Engineering | Amsterdam, Netherlands         | May 10, 2025 | Yes              | [Apply](https://company.recharge.com/vacancies/lead-marketing-automation/)          |
| Recharge         | Data Engineering | Amsterdam, Netherlands         | May 10, 2025 | Yes              | [Apply](https://company.recharge.com/vacancies/staff-software-engineer-2/)          |
| Hapag-Lloyd AG   | Data Engineering | Gdansk, Poland                | April 25, 2025| Yes              | [Apply](https://www.linkedin.com/jobs/view/4148246703)                             |
| Byborg Enterprises| Data Engineering | Neudorf-Weimershof, Luxembourg | April 25, 2025| Yes              | [Apply](https://jobs.smartrecruiters.com/DoclerHolding/744000035188883-content-marketing-manager) |
| Langham Recruitment| Data Engineering | London, United Kingdom         | April 25, 2025| Yes              | [Apply](https://www.linkedin.com/jobs/view/4146351784)                             |
| MODE Recruitment | Data Engineering | Frankfurt, Germany            | April 25, 2025| Yes              | [Apply](https://www.linkedin.com/jobs/view/4148245932)                             |
| MODE Recruitment | Data Engineering | Frankfurt, Germany            | April 25, 2025| Yes              | [Apply](https://www.linkedin.com/jobs/view/4148245729)                             |
| MODE Recruitment | Data Engineering | Munich, Germany              | April 25, 2025| Yes              | [Apply](https://www.linkedin.com/jobs/view/4148246703)                             |
| Sunday GmbH      | Data Engineering | Hamburg, Germany             | April 20, 2025| Yes              | [Apply](https://join.com/companies/sunday/13429301-marketing-artist-f-m-d)         |
| OpenAI           | Data Engineering | London, United Kingdom        | April 20, 2025| Yes              | [Apply](https://www.linkedin.com/jobs/view/4148246703)                             |
