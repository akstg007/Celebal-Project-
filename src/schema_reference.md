# `patients` table schema (db/hospital.db)

Used later as the schema description injected into the NLP-to-SQL agent's prompt.

| Column                | Type     | Notes                                              |
|------------------------|----------|-----------------------------------------------------|
| patient_id             | INTEGER  | Primary key, auto-generated                        |
| name                   | TEXT     | Patient full name, title-cased                     |
| age                    | INTEGER  | 1–119                                               |
| gender                 | TEXT     | 'Male' or 'Female'                                  |
| blood_type             | TEXT     | e.g. 'A+', 'O-', 'AB+'                              |
| medical_condition      | TEXT     | 'Cancer', 'Obesity', 'Diabetes', 'Asthma', 'Hypertension', 'Arthritis' |
| date_of_admission      | DATE     | ISO format YYYY-MM-DD                               |
| doctor                 | TEXT     | Attending doctor's full name                        |
| hospital                | TEXT     | Hospital/clinic name                                 |
| insurance_provider      | TEXT     | 'Blue Cross', 'Medicare', 'Aetna', 'UnitedHealthcare', 'Cigna' |
| billing_amount          | REAL     | USD, always > 0                                      |
| room_number             | INTEGER  | Room number                                          |
| admission_type          | TEXT     | 'Urgent', 'Emergency', 'Elective'                    |
| discharge_date          | DATE     | ISO format YYYY-MM-DD                                |
| medication              | TEXT     | Prescribed medication                                |
| test_results            | TEXT     | 'Normal', 'Inconclusive', 'Abnormal'                 |
| length_of_stay_days     | INTEGER  | Derived: discharge_date - date_of_admission          |

**Row count:** 54,860 (after cleaning/dedup from raw 55,500)

**Indexes:** medical_condition, doctor, hospital, date_of_admission

**Important for SQL generation prompt (Day 3):**
- This is a **read-only** analytics table. The agent must only ever generate `SELECT` statements.
- Categorical values are case-sensitive as listed above (e.g. always `'Diabetes'` not `'diabetes'`).
- `hospital` is a synthetic company-style name per admission (not a small fixed list) — don't assume it's a small enum.
