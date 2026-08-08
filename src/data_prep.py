"""
Day 1 - Data Preparation
Cleans the raw Kaggle healthcare_dataset.csv and loads it into a local
SQLite database (db/hospital.db) that the NLP-to-SQL agent will query later.

Run:
    python src/data_prep.py
"""

import pandas as pd
import sqlite3
from pathlib import Path

RAW_CSV = Path(__file__).parent.parent / "data" / "healthcare_dataset.csv"
DB_PATH = Path(__file__).parent.parent / "db" / "hospital.db"
TABLE_NAME = "patients"


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Standardise column names to snake_case (easier for SQL + prompting)
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Strip whitespace on all string/object columns
    str_cols = df.select_dtypes(include="object").columns
    for c in str_cols:
        df[c] = df[c].astype(str).str.strip()

    # Fix inconsistent name casing e.g. "LesLie TErRy" -> "Leslie Terry"
    df["name"] = df["name"].str.title()

    # Standardise categorical text casing
    for c in ["gender", "blood_type", "medical_condition", "admission_type",
              "test_results", "insurance_provider", "doctor", "hospital", "medication"]:
        if c in df.columns:
            df[c] = df[c].str.strip()

    df["medical_condition"] = df["medical_condition"].str.title()
    df["admission_type"] = df["admission_type"].str.title()
    df["test_results"] = df["test_results"].str.title()

    # Parse dates
    df["date_of_admission"] = pd.to_datetime(df["date_of_admission"], errors="coerce")
    df["discharge_date"] = pd.to_datetime(df["discharge_date"], errors="coerce")

    # Drop exact duplicate rows
    before = len(df)
    df = df.drop_duplicates()
    print(f"Dropped {before - len(df)} duplicate rows")

    # Drop rows with broken dates or negative/absurd values, if any
    df = df.dropna(subset=["date_of_admission", "discharge_date"])
    df = df[(df["age"] > 0) & (df["age"] < 120)]
    df = df[df["billing_amount"] > 0]

    # Add a clean primary key
    df = df.reset_index(drop=True)
    df.insert(0, "patient_id", df.index + 1)

    # Derived column that's genuinely useful for SQL questions later
    df["length_of_stay_days"] = (df["discharge_date"] - df["date_of_admission"]).dt.days

    return df


def load_to_sqlite(df: pd.DataFrame, db_path: Path, table_name: str):
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    # Helpful indexes for faster + more reliable agent queries
    cur = conn.cursor()
    cur.execute(f"CREATE INDEX IF NOT EXISTS idx_condition ON {table_name}(medical_condition)")
    cur.execute(f"CREATE INDEX IF NOT EXISTS idx_doctor ON {table_name}(doctor)")
    cur.execute(f"CREATE INDEX IF NOT EXISTS idx_hospital ON {table_name}(hospital)")
    cur.execute(f"CREATE INDEX IF NOT EXISTS idx_admission_date ON {table_name}(date_of_admission)")
    conn.commit()
    conn.close()


def print_schema_summary(df: pd.DataFrame):
    print("\n=== FINAL SCHEMA ===")
    for col, dtype in df.dtypes.items():
        print(f"  {col:22s} {dtype}")
    print(f"\nTotal rows: {len(df)}")


if __name__ == "__main__":
    print(f"Reading raw CSV from {RAW_CSV} ...")
    raw = pd.read_csv(RAW_CSV)
    print(f"Raw shape: {raw.shape}")

    cleaned = clean_data(raw)
    print_schema_summary(cleaned)

    load_to_sqlite(cleaned, DB_PATH, TABLE_NAME)
    print(f"\nLoaded '{TABLE_NAME}' table into {DB_PATH}")
