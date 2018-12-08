from datetime import datetime
import os
import sqlite3
import time

import pandas as pd
import praw

from scrape import scrape_subreddit

reddit = praw.Reddit(
    client_id=str(os.environ['REDDIT_CLIENT_ID']).strip(),
    client_secret=str(os.environ['REDDIT_CLIENT_SECRET']).strip(),
    user_agent=str(os.environ['REDDIT_USER_AGENT']).strip(),
)

# print(type(os.environ['REDDIT_USER_AGENT']))
# print(os.environ['REDDIT_USER_AGENT'])

while True:
    threads = scrape_subreddit(reddit, subreddit='funny', category='hot', thread_count=5)
    for thread in threads:
        print(thread[0])
        print(thread[1])
        thread[0].to_csv(f'data/submission_{str(datetime.now())}.csv')
        thread[1].to_csv(f'data/comments_{str(datetime.now())}.csv')

    time.sleep(30)

# reddit.login(os.environ['REDDIT_USER'], os.environ['REDDIT_PASS'])

