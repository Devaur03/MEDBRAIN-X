import pandas as pd

# Example: Load admissions data
admissions = pd.read_csv("data/raw/mimic-iv-clinical-database-demo-2.2/hosp/admissions.csv.gz")

# Example: Load ICU stays data
icustays = pd.read_csv("data/raw/mimic-iv-clinical-database-demo-2.2/icu/icustays.csv.gz")

# Show first few rows
print(admissions.head())
print(icustays.head())
