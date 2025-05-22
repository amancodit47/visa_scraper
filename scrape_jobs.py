# import requests
# import pandas as pd
# import datetime

# SERPAPI_API_KEY = "YOUR API KEY"

# def extract_job_type(highlights):
#     if isinstance(highlights, list):
#         for section in highlights:
#             if 'title' in section and section['title'].lower() == 'job type':
#                 return section.get('items', [""])[0]
#     return ""

# def extract_work_setting(highlights):
#     if isinstance(highlights, list):
#         for section in highlights:
#             if 'title' in section and section['title'].lower() in ['work setting', 'workplace type']:
#                 return section.get('items', [""])[0]
#     return ""

# def scrape_data_engineer_jobs():
#     params = {
#         "engine": "google_jobs",
#         "q": "Data Engineer",
#         "location": "United States",
#         "api_key": SERPAPI_API_KEY,
#     }

#     response = requests.get("https://serpapi.com/search", params=params)

#     if response.status_code != 200:
#         print("❌ Error: Failed to fetch data from SerpAPI")
#         return []

#     results = response.json()
#     job_results = results.get("jobs_results", [])

#     if not job_results:
#         print("⚠️ No jobs returned from SerpAPI.")
#         print("🔍 Full response from SerpAPI:")
#         print(results)
#         return []

#     jobs = []
#     for job in job_results:
#         try:
#             company = job.get("company_name", "")
#             title = job.get("title", "")
#             location = job.get("location", "")
#             job_desc = job.get("description", "")
#             job_link = job.get("apply_options", [{}])[0].get("link", "")
#             job_highlights = job.get("job_highlights", [])
#             posting_time = job.get("detected_extensions", {}).get("posted_at", "N/A")

#             jobs.append({
#                 "company": company,
#                 "title": title,
#                 "location": location,
#                 "posting_time": posting_time,
#                 "job_type": extract_job_type(job_highlights),
#                 "description": job_desc,
#                 "work_setting": extract_work_setting(job_highlights),
#                 "apply_link": job_link
#             })
#         except Exception as e:
#             print(f"⚠️ Error parsing job: {e}")
#             continue

#     return jobs

# def filter_jobs_by_h1b_sponsorship(jobs, sponsoring_companies):
#     sponsoring_companies_lower = [c.lower() for c in sponsoring_companies]

#     filtered_jobs = []
#     for job in jobs:
#         company_name = job.get("company", "").lower()
#         if any(sponsor in company_name for sponsor in sponsoring_companies_lower):
#             filtered_jobs.append(job)

#     return filtered_jobs

# def load_h1b_sponsoring_companies(csv_path):
#     try:
#         df = pd.read_csv(csv_path)
#         return df["EMPLOYER_NAME"].dropna().astype(str).str.strip().tolist()
#     except Exception as e:
#         print(f"⚠️ Error reading H-1B companies from CSV: {e}")
#         return []

# if __name__ == "__main__":
#     csv_path = "h1bcompanies_list.csv"
#     h1b_sponsoring_companies = load_h1b_sponsoring_companies(csv_path)

#     job_listings = scrape_data_engineer_jobs()
    
#     if not job_listings:
#         print("🚫 No job listings found.")
#     else:
#         print("Companies found in scraped jobs:")
#         for job in job_listings:
#             print("-", job.get("company", "N/A"))

#         filtered_listings = filter_jobs_by_h1b_sponsorship(job_listings, h1b_sponsoring_companies)

#         if not filtered_listings:
#             print("🚫 No job listings from H-1B sponsoring companies found.")
#         else:
#             print(f"✅ Found {len(filtered_listings)} job(s) from H-1B sponsoring companies:\n")
#             for idx, job in enumerate(filtered_listings, 1):
#                 print(f"\n📌 Job {idx}:")
#                 for k, v in job.items():
#                     print(f"{k}: {v}")
# import requests
# import pandas as pd
# import datetime
# from db_loader import init_db, insert_jobs  # 🔗 Step 3: Import DB functions

# SERPAPI_API_KEY = "27e19eb8727a780fee46d52f054a94746aca86173cb17dab78ee0675b4ee2cac"

# def extract_job_type(highlights):
#     if isinstance(highlights, list):
#         for section in highlights:
#             if 'title' in section and section['title'].lower() == 'job type':
#                 return section.get('items', [""])[0]
#     return ""

# def extract_work_setting(highlights):
#     if isinstance(highlights, list):
#         for section in highlights:
#             if 'title' in section and section['title'].lower() in ['work setting', 'workplace type']:
#                 return section.get('items', [""])[0]
#     return ""

# def scrape_data_engineer_jobs():
#     params = {
#         "engine": "google_jobs",
#         "q": "Data Engineer",
#         "location": "United States",
#         "api_key": SERPAPI_API_KEY,
#     }

#     response = requests.get("https://serpapi.com/search", params=params)

#     if response.status_code != 200:
#         print("❌ Error: Failed to fetch data from SerpAPI")
#         return []

#     results = response.json()
#     job_results = results.get("jobs_results", [])

#     if not job_results:
#         print("⚠️ No jobs returned from SerpAPI.")
#         print("🔍 Full response from SerpAPI:")
#         print(results)
#         return []

#     jobs = []
#     for job in job_results:
#         try:
#             company = job.get("company_name", "")
#             title = job.get("title", "")
#             location = job.get("location", "")
#             job_desc = job.get("description", "")
#             job_link = job.get("apply_options", [{}])[0].get("link", "")
#             job_highlights = job.get("job_highlights", [])
#             posting_time = job.get("detected_extensions", {}).get("posted_at", "N/A")

#             jobs.append({
#                 "company": company,
#                 "title": title,
#                 "location": location,
#                 "posting_time": posting_time,
#                 "job_type": extract_job_type(job_highlights),
#                 "description": job_desc,
#                 "work_setting": extract_work_setting(job_highlights),
#                 "apply_link": job_link
#             })
#         except Exception as e:
#             print(f"⚠️ Error parsing job: {e}")
#             continue

#     return jobs

# def filter_jobs_by_h1b_sponsorship(jobs, sponsoring_companies):
#     sponsoring_companies_lower = [c.lower() for c in sponsoring_companies]

#     filtered_jobs = []
#     for job in jobs:
#         company_name = job.get("company", "").lower()
#         if any(sponsor in company_name for sponsor in sponsoring_companies_lower):
#             filtered_jobs.append(job)

#     return filtered_jobs

# def load_h1b_sponsoring_companies(csv_path):
#     try:
#         df = pd.read_csv(csv_path)
#         return df["EMPLOYER_NAME"].dropna().astype(str).str.strip().tolist()
#     except Exception as e:
#         print(f"⚠️ Error reading H-1B companies from CSV: {e}")
#         return []

# if __name__ == "__main__":
#     csv_path = "h1bcompanies_list.csv"
#     h1b_sponsoring_companies = load_h1b_sponsoring_companies(csv_path)

#     job_listings = scrape_data_engineer_jobs()

#     if not job_listings:
#         print("🚫 No job listings found.")
#     else:
#         print("Companies found in scraped jobs:")
#         for job in job_listings:
#             print("-", job.get("company", "N/A"))

#         filtered_listings = filter_jobs_by_h1b_sponsorship(job_listings, h1b_sponsoring_companies)

#         if not filtered_listings:
#             print("🚫 No job listings from H-1B sponsoring companies found.")
#         else:
#             print(f"✅ Found {len(filtered_listings)} job(s) from H-1B sponsoring companies:\n")
#             for idx, job in enumerate(filtered_listings, 1):
#                 print(f"\n📌 Job {idx}:")
#                 for k, v in job.items():
#                     print(f"{k}: {v}")

#             # 🟢 Step 3: Save to SQLite
#             init_db()
#             insert_jobs(filtered_listings)
#             print("\n💾 Job listings saved to jobs.db successfully.")
# import requests
# import pandas as pd
# import datetime
# from db_loader import init_db, insert_jobs

# SERPAPI_API_KEY = "27e19eb8727a780fee46d52f054a94746aca86173cb17dab78ee0675b4ee2cac"

# def extract_job_type(highlights):
#     if isinstance(highlights, list):
#         for section in highlights:
#             if 'title' in section and section['title'].lower() == 'job type':
#                 return section.get('items', [""])[0]
#     return ""

# def extract_work_setting(highlights):
#     if isinstance(highlights, list):
#         for section in highlights:
#             if 'title' in section and section['title'].lower() in ['work setting', 'workplace type']:
#                 return section.get('items', [""])[0]
#     return ""

# def scrape_data_engineer_jobs():
#     params = {
#         "engine": "google_jobs",
#         "q": "Data Engineer",
#         "location": "United States",
#         "api_key": SERPAPI_API_KEY,
#     }

#     response = requests.get("https://serpapi.com/search", params=params)

#     if response.status_code != 200:
#         print("❌ Error: Failed to fetch data from SerpAPI")
#         return []

#     results = response.json()
#     job_results = results.get("jobs_results", [])

#     if not job_results:
#         print("⚠️ No jobs returned from SerpAPI.")
#         print("🔍 Full response from SerpAPI:")
#         print(results)
#         return []

#     jobs = []
#     for job in job_results:
#         try:
#             company = job.get("company_name", "")
#             title = job.get("title", "")
#             location = job.get("location", "")
#             job_desc = job.get("description", "")
#             job_link = job.get("apply_options", [{}])[0].get("link", "")
#             job_highlights = job.get("job_highlights", [])
#             posting_time = job.get("detected_extensions", {}).get("posted_at", "N/A")

#             jobs.append({
#                 "company": company,
#                 "title": title,
#                 "location": location,
#                 "posting_time": posting_time,
#                 "job_type": extract_job_type(job_highlights),
#                 "description": job_desc,
#                 "work_setting": extract_work_setting(job_highlights),
#                 "apply_link": job_link
#             })
#         except Exception as e:
#             print(f"⚠️ Error parsing job: {e}")
#             continue

#     return jobs

# def filter_jobs_by_h1b_sponsorship(jobs, sponsoring_companies):
#     sponsoring_companies_lower = [c.lower() for c in sponsoring_companies]

#     filtered_jobs = []
#     for job in jobs:
#         company_name = job.get("company", "").lower()
#         if any(sponsor in company_name for sponsor in sponsoring_companies_lower):
#             filtered_jobs.append(job)

#     return filtered_jobs

# def load_h1b_sponsoring_companies(csv_path):
#     try:
#         df = pd.read_csv(csv_path)
#         return df["EMPLOYER_NAME"].dropna().astype(str).str.strip().tolist()
#     except Exception as e:
#         print(f"⚠️ Error reading H-1B companies from CSV: {e}")
#         return []

# if __name__ == "__main__":
#     csv_path = "h1bcompanies_list.csv"
#     h1b_sponsoring_companies = load_h1b_sponsoring_companies(csv_path)

#     job_listings = scrape_data_engineer_jobs()

#     if not job_listings:
#         print("🚫 No job listings found.")
#     else:
#         print("Companies found in scraped jobs:")
#         for job in job_listings:
#             print("-", job.get("company", "N/A"))

#         filtered_listings = filter_jobs_by_h1b_sponsorship(job_listings, h1b_sponsoring_companies)

#         if not filtered_listings:
#             print("🚫 No job listings from H-1B sponsoring companies found.")
#         else:
#             print(f"✅ Found {len(filtered_listings)} job(s) from H-1B sponsoring companies:\n")
#             for idx, job in enumerate(filtered_listings, 1):
#                 print(f"\n📌 Job {idx}:")
#                 for k, v in job.items():
#                     print(f"{k}: {v}")

#             init_db()
#             insert_jobs(filtered_listings)
#             print("\n💾 Job listings saved to jobs.db successfully.")
import requests
import pandas as pd
import datetime
from db_loader import init_db, insert_jobs  # Make sure this module exists

# SerpAPI key
SERPAPI_API_KEY = "27e19eb8727a780fee46d52f054a94746aca86173cb17dab78ee0675b4ee2cac"

def extract_job_type(highlights):
    if isinstance(highlights, list):
        for section in highlights:
            if 'title' in section and section['title'].lower() == 'job type':
                return section.get('items', [""])[0]
    return ""

def extract_work_setting(highlights):
    if isinstance(highlights, list):
        for section in highlights:
            if 'title' in section and section['title'].lower() in ['work setting', 'workplace type']:
                return section.get('items', [""])[0]
    return ""

def scrape_data_engineer_jobs():
    params = {
        "engine": "google_jobs",
        "q": "Data Engineer",
        "location": "United States",
        "api_key": SERPAPI_API_KEY,
    }

    response = requests.get("https://serpapi.com/search", params=params)

    if response.status_code != 200:
        print("❌ Error: Failed to fetch data from SerpAPI")
        return []

    results = response.json()
    job_results = results.get("jobs_results", [])

    if not job_results:
        print("⚠️ No jobs returned from SerpAPI.")
        print("🔍 Full response from SerpAPI:")
        print(results)
        return []

    jobs = []
    for job in job_results:
        try:
            company = job.get("company_name", "")
            title = job.get("title", "")
            location = job.get("location", "")
            job_desc = job.get("description", "")
            job_link = job.get("apply_options", [{}])[0].get("link", "")
            job_highlights = job.get("job_highlights", [])
            posting_time = job.get("detected_extensions", {}).get("posted_at", "N/A")

            jobs.append({
                "company": company,
                "title": title,
                "location": location,
                "posting_time": posting_time,
                "job_type": extract_job_type(job_highlights),
                "description": job_desc,
                "work_setting": extract_work_setting(job_highlights),
                "apply_link": job_link
            })
        except Exception as e:
            print(f"⚠️ Error parsing job: {e}")
            continue

    return jobs

def filter_jobs_by_h1b_sponsorship(jobs, sponsoring_companies):
    sponsoring_companies_lower = [c.lower() for c in sponsoring_companies]

    filtered_jobs = []
    for job in jobs:
        company_name = job.get("company", "").lower()
        if any(sponsor in company_name for sponsor in sponsoring_companies_lower):
            filtered_jobs.append(job)

    return filtered_jobs

def load_h1b_sponsoring_companies(csv_path):
    try:
        df = pd.read_csv(csv_path)
        return df["EMPLOYER_NAME"].dropna().astype(str).str.strip().tolist()
    except Exception as e:
        print(f"⚠️ Error reading H-1B companies from CSV: {e}")
        return []

if __name__ == "__main__":
    csv_path = "h1bcompanies_list.csv"
    h1b_sponsoring_companies = load_h1b_sponsoring_companies(csv_path)

    job_listings = scrape_data_engineer_jobs()

    if not job_listings:
        print("🚫 No job listings found.")
    else:
        print("Companies found in scraped jobs:")
        for job in job_listings:
            print("-", job.get("company", "N/A"))

        filtered_listings = filter_jobs_by_h1b_sponsorship(job_listings, h1b_sponsoring_companies)

        if not filtered_listings:
            print("🚫 No job listings from H-1B sponsoring companies found.")
        else:
            print(f"✅ Found {len(filtered_listings)} job(s) from H-1B sponsoring companies:\n")
            for idx, job in enumerate(filtered_listings, 1):
                print(f"\n📌 Job {idx}:")
                for k, v in job.items():
                    print(f"{k}: {v}")

            # Save to SQLite
            init_db()
            insert_jobs(filtered_listings)
            print("\n💾 Job listings saved to jobs.db successfully.")

            # Save to CSV
            df = pd.DataFrame(filtered_listings)
            df.to_csv("output.csv", index=False, encoding="utf-8")
            print("📁 Job listings also saved to output.csv")
