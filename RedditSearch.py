import praw
import json
import os
from pprint import pprint
import apikeys

apikeys.setkeys()

client_id = os.environ['reddit_client']
client_secret = os.environ['reddit_secret']
username = os.environ['reddit_username']
password = os.environ['reddit_password']

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,
                     # username=username, password=password,
                     user_agent='CampSearch 0.1')

# Testing
# for submission in reddit.subreddit('learnpython').hot(limit=10): print(submission.title)

# 'Search' documentation:
# https://www.reddit.com/wiki/search

'''
Might need to specify certain subreddits?
So which ones should I target?
Astronomy
space
festivals
solareclipse
eclipse2017
telescopes
Oregon-related?
'''

cred = reddit.subreddit('Astronomy').search('oregon',
                                            sort='new',
                                            time_filter='year',
                                            syntax='plain')
# How to limit this search by recency?

#ids = []
#for stuff in cred:
#    ids.append(stuff)
# Returns a list of Submissions

# Get comment tree ids for a particular Submission
# ids[0].comments.list()

# Return a shortlink URL
# ids[0].shortlink

# Read text of certain comments
# ids[0].comments[0].body

# Let's return more info, including link, time, etc.
# vars(ids[0])
# Relevant: title, shortlink, score...anything else? time is UTC thing

for each in cred:
    print(each.title)
    #print(each.shortlink)
    #print(each.score)
    #print()

# print('Hey!')


'''
JUNK CODE

new_sub = reddit.subreddit('solareclipse')
comments_raw = new_sub.get_comments(new_sub, limit=count)

posts = reddit.search('Oregon', subreddit='Astronomy',sort=None, syntax=None,period=None,limit=None)
title=[]
for post in posts:
    title.append(post.title)
print len(title)
'''
