import pandas as pd

df = pd.read_csv("aqidataset.csv")

print("===== BEFORE CLEANING =====")
print("Shape:", df.shape)
print("Missing values:\n", df.isna().sum())
print("Duplicates:", df.duplicated().sum())

df = df.drop_duplicates()
df = df.dropna()

text_cols = ["country", "state", "city", "station", "pollutant_id"]

for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.lower()

df["last_update"] = pd.to_datetime(df["last_update"], errors="coerce")

df = df.dropna(subset=["last_update"])

df = df[(df["latitude"] >= -90) & (df["latitude"] <= 90)]
df = df[(df["longitude"] >= -180) & (df["longitude"] <= 180)]

print("\n===== AFTER CLEANING =====")
print("Shape:", df.shape)
print("Missing values:\n", df.isna().sum())
print("Duplicates:", df.duplicated().sum())

df.to_csv("aqi_dataset_cleaned.csv", index=False)

print("\nClean dataset saved successfully!")