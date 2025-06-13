import praw
import csv
from datetime import datetime

reddit = praw.Reddit(
    client_id="W0nHuS1fI2R05mwsD0KjYg",
    client_secret="gKUp-uAKZagCr6z-V8G6Cs5_AVfpaw",
    user_agent='memescraper/0.1 by Annual_Judge_1010',
)

subreddit = reddit.subreddit('wallstreetbets')
filename = f"memes_{datetime.now().strftime('%Y-%m-%d')}.csv"

with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Upvotes", "Created Time", "URL"])

        for post in subreddit.hot(limit=10000):
            writer.writerow([post.title, post.score, post.created_utc, post.url])

print(f"Saved: {filename}")
with open("log.txt", "a") as log:
    log.write(f"Scraped on {datetime.now()}\n")
