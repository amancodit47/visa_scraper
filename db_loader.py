# import sqlite3

# def init_db(db_name="jobs.db"):
#     conn = sqlite3.connect(db_name)
#     cursor = conn.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS filtered_jobs (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             company TEXT,
#             title TEXT,
#             location TEXT,
#             posting_time TEXT,
#             job_type TEXT,
#             description TEXT,
#             work_setting TEXT,
#             apply_link TEXT,
#             scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#         )
#     """)
#     conn.commit()
#     conn.close()


# def insert_jobs(jobs, db_name="jobs.db"):
#     conn = sqlite3.connect(db_name)
#     cursor = conn.cursor()

#     for job in jobs:
#         cursor.execute("""
#             INSERT INTO filtered_jobs (
#                 company, title, location, posting_time,
#                 job_type, description, work_setting, apply_link
#             ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#         """, (
#             job.get("company"),
#             job.get("title"),
#             job.get("location"),
#             job.get("posting_time"),
#             job.get("job_type"),
#             job.get("description"),
#             job.get("work_setting"),
#             job.get("apply_link")
#         ))
    
#     conn.commit()
#     conn.close()
# import sqlite3

# def insert_jobs(jobs, db_name="jobs.db"):
#     conn = sqlite3.connect(db_name)
#     cursor = conn.cursor()

#     # Create table with unique constraint to avoid duplicates
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS job_listings (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         company TEXT,
#         title TEXT,
#         location TEXT,
#         posting_time TEXT,
#         job_type TEXT,
#         description TEXT,
#         work_setting TEXT,
#         apply_link TEXT UNIQUE
#     )
#     """)

#     for job in jobs:
#         try:
#             cursor.execute("""
#             INSERT OR IGNORE INTO job_listings (
#                 company, title, location, posting_time,
#                 job_type, description, work_setting, apply_link
#             ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#             """, (
#                 job.get("company"),
#                 job.get("title"),
#                 job.get("location"),
#                 job.get("posting_time"),
#                 job.get("job_type"),
#                 job.get("description"),
#                 job.get("work_setting"),
#                 job.get("apply_link")
#             ))
#         except Exception as e:
#             print(f"⚠️ Skipping duplicate or invalid job: {e}")
#             continue

#     conn.commit()
#     conn.close()
#     print("💾 Job listings saved to jobs.db successfully.")
import sqlite3

def init_db():
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT,
            title TEXT,
            location TEXT,
            posting_time TEXT,
            job_type TEXT,
            description TEXT,
            work_setting TEXT,
            apply_link TEXT UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def insert_jobs(jobs):
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    for job in jobs:
        try:
            cursor.execute('''
                INSERT OR IGNORE INTO jobs (company, title, location, posting_time, job_type, description, work_setting, apply_link)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                job['company'], job['title'], job['location'], job['posting_time'],
                job['job_type'], job['description'], job['work_setting'], job['apply_link']
            ))
        except Exception as e:
            print(f"Error inserting job: {e}")
    conn.commit()
    conn.close()
