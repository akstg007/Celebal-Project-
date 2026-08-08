"""
Day 1 - Manual test queries against the SQLite DB.

Why this matters: these Q -> SQL pairs are your ground truth. On Day 3,
you'll feed the *same* natural-language questions to the NLP-to-SQL agent
and compare its generated SQL / answers against what you know is correct.

Run:
    python src/sample_queries.py
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "db" / "hospital.db"

# (natural language question, hand-written SQL, short note)
TEST_QUERIES = [
    (
        "How many patients were admitted for Diabetes?",
        "SELECT COUNT(*) FROM patients WHERE medical_condition = 'Diabetes';",
    ),
    (
        "What is the average billing amount for Emergency admissions?",
        "SELECT AVG(billing_amount) FROM patients WHERE admission_type = 'Emergency';",
    ),
    (
        "Who are the top 5 doctors by number of patients treated?",
        """SELECT doctor, COUNT(*) as patient_count
           FROM patients GROUP BY doctor ORDER BY patient_count DESC LIMIT 5;""",
    ),
    (
        "What is the average length of stay for Cancer patients?",
        "SELECT AVG(length_of_stay_days) FROM patients WHERE medical_condition = 'Cancer';",
    ),
    (
        "How many patients have abnormal test results, broken down by gender?",
        """SELECT gender, COUNT(*) FROM patients
           WHERE test_results = 'Abnormal' GROUP BY gender;""",
    ),
    (
        "Which insurance provider has the highest total billing amount?",
        """SELECT insurance_provider, SUM(billing_amount) as total_billing
           FROM patients GROUP BY insurance_provider ORDER BY total_billing DESC LIMIT 1;""",
    ),
    (
        "List patients over age 70 admitted urgently, limit 5.",
        """SELECT name, age, medical_condition, hospital FROM patients
           WHERE age > 70 AND admission_type = 'Urgent' LIMIT 5;""",
    ),
    (
        "What are the most common medications prescribed for Asthma?",
        """SELECT medication, COUNT(*) as freq FROM patients
           WHERE medical_condition = 'Asthma' GROUP BY medication ORDER BY freq DESC;""",
    ),
    (
        "How many unique hospitals are in the dataset?",
        "SELECT COUNT(DISTINCT hospital) FROM patients;",
    ),
    (
        "What is the average age of patients by blood type?",
        "SELECT blood_type, AVG(age) FROM patients GROUP BY blood_type;",
    ),
]


def run_all():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    for i, (question, sql) in enumerate(TEST_QUERIES, 1):
        print(f"\n[{i}] Q: {question}")
        print(f"    SQL: {sql.strip()}")
        try:
            cur.execute(sql)
            rows = cur.fetchall()
            preview = rows[:5]
            print(f"    Result ({len(rows)} rows): {preview}")
        except Exception as e:
            print(f"    ERROR: {e}")

    conn.close()


if __name__ == "__main__":
    run_all()
