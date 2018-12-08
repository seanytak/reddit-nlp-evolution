from typing import List, Tuple

import pandas as pd
import praw


def search_index(subreddit: str, category='',
                 max_threads=5) -> List[praw.submissions]:
    """Wrapper function around subreddit.<category>(limit=max_threads)

    Args:
        subreddit (str): Name of the subreddit to scrape from.
        category (str): Category to scrape from (hot, new, top, controversial, gilded). Defaults to new.
        max_threads (int): Maximum number of threads that can be scraped at once. Defaults to 5.

    Returns:
        List[praw.submissions]: List of threads that were scraped.
    """
    if category == "hot":
        return subreddit.hot(limit=max_threads)
    elif category == "new":
        return subreddit.new(limit=max_threads)
    elif category == "top":
        return subreddit.top(limit=max_threads)
    elif category == "controversial":
        return subreddit.controversial(limit=max_threads)
    elif category == "gilded":
        return subreddit.gilded(limit=max_threads)


def scrape_subreddit(reddit: praw.Reddit,
                     subreddit: str,
                     category='new',
                     thread_count=5
                     ) -> List[Tuple[pd.DataFrame, pd.DataFrame]]:
    """Scrape a given subreddit's section for a given number of threads.
    
    Args:
        reddit (praw.Reddit): Reddit instance from Python Reddit API Wrapper (praw).
        subreddit (str): Name of the subreddit to scrape from.
        category (str): Category to scrape from (hot, new, top, controversial, gilded). Defaults to new.
        thread_count (int): Number of threads to scrape at a time. Defaults to 5

    Returns:
        List[Tuple[pd.DataFrame, pd.DataFrame]]: List of threads with a tuple containing two pandas DataFrames
            First DataFrame contains the submission (Reddit Thread) attributes
            Second DataFrame contains the comments (Reddit Comments) attributes
    """
    subreddit = reddit.subreddit(subreddit)
    submissions = search_index(
        subreddit, category=category, max_threads=thread_count)

    reddit_threads = []
    for submission in submissions:
        # Get 1D List of comment objects
        comments = submission.comments._comments

        # Turn list of Comment objects to list of dictionaries of comment objects
        comments = [vars(comment) for comment in comments]

        # Turn 1D list of comment dictionaries into Pandas DataFrame
        comments = pd.DataFrame(comments)
        submission = pd.DataFrame([vars(submission)])

        reddit_threads.append((submission, comments))
    return reddit_threads