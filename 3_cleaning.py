import pandas as pd
from datetime import datetime

# Load CSV
df = pd.read_csv("memes.csv")

# Strip extra spaces in column names
df.columns = df.columns.str.strip()

# Show cleaned column names (optional)
# print(df.columns)

# Drop duplicates
df = df.drop_duplicates()

# Convert created time from UNIX timestamp
df["Created Time"] = pd.to_datetime(df["Created UTC"], unit='s')

# Drop rows missing key data
df = df.dropna(subset=['Title', 'URL'])

# Filter by upvotes
df = df[df['Upvotes'] > 100]

# Save cleaned file
df.to_csv("cleaned_memes.csv", index=False)
print("✅ Cleaned dataset saved as cleaned_memes.csv")
