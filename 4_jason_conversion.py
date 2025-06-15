import pandas as pd
df = pd.read_csv("C:\\Users\\18SS0\\OneDrive\\Desktop\\Main\\Programming\\python\\Projects Using python\\Sentiment Analysis\\meme-hype-dataset\\cleaned_memes.csv")

df['Readable Time'] = pd.to_datetime(df["Created Time"])

df = df[df["Title"].str.len() > 10]    # Remove titles too short
df = df[df["Title"].str.len() < 300]   # Remove junk spam

df["Source"] = "Reddit"

df.to_json("cleaned_memes.json", orient="records", lines=True)

