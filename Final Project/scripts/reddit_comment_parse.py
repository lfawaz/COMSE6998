import datetime
import pandas as pd
import praw
import time
import requests
import requests.auth
import redApi

subreddit_list = ['yahoo','samsung','GalaxyNote7']

r = redApi.getPraw()
for subreddit in subreddit_list:
# Loop through all subreddits
    subreddit_posts = r.get_subreddit(subreddit).get_top_from_year(limit=None)

    df = pd.DataFrame()
    df_file =  subreddit+'_top_posts.csv'
    for post in subreddit_posts:
    # Loop through top posts in each subreddit
        subid = post.id
        submission = r.get_submission(submission_id = subid)

        comments = redApi.getComments(submission)
        
        for comment in comments:
        # Loop through all comments in each post
            if comment['data']['replies'] == "":
                text = comment[u'data'][u'body']
                timestamp = comment[u'data'][u'created_utc']
            else:
                text = comment[u'data'][u'replies'][u'data'][u'children'][0][u'data'][u'body']
                timestamp = comment[u'data'][u'replies'][u'data'][u'children'][0][u'data'][u'created_utc']
            timestamp = datetime.datetime.fromtimestamp(
                           int(timestamp)
                        ).strftime('%Y-%m-%d %H:%M:%S')
            df = df.append({'title': post.title,'comment': text, 'date': timestamp}, ignore_index=True)
    df.to_csv(df_file, encoding='utf-8')
