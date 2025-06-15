import praw
import csv

reddit = praw.Reddit(
    client_id="W0nHuS1fI2R05mwsD0KjYg",
    client_secret="gKUp-uAKZagCr6z-V8G6Cs5_AVfpaw",
    user_agent='memescraper/0.1 by Annual_Judge_1010',
)

subreddit = reddit.subreddit('wallstreetbets')

try:
    with open('memes.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title','Upvotes','Comments','Created Time', 'URL','Post ID','Created UTC','Author','Flair','Upvote Ratio','          Views','          Crossposts','          Permalink','          In self post','          Is video','          Is Image','          self text'])

        for post in subreddit.top(limit=10000):
            writer.writerow([
                post.title,
                post.score,
                post.num_comments,
                post.created_utc,
                post.url,
                post.id,
                post.created_utc,
                str(post.author),
                post.link_flair_text,
                post.upvote_ratio,
                post.view_count,
                post.num_crossposts,
                post.permalink,
                post.is_self,
                post.is_video,
                post.url.endswith(('.jpg', '.jpeg', '.png', '.gif')),
                post.selftext[:200]
            ])
except Exception as e:
    print("An error occurred:", e)
