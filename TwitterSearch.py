from twitter import *
import json
import os
import apikeys

# 'apikeys' is another Python script, not incl. in the repo
# It sets the required environmental variables that
# contain the Twitter API keys/tokens
# ex: `os.environ['twitter_consumer_secret'] = 'gobbledygook'`

def gettweets(term):
    apikeys.setkeys()

    # OAuth tokens grabbed from my environment, amazingly!
    auth = OAuth(
        consumer_key = os.environ['twitter_consumer_key'],
        consumer_secret = os.environ['twitter_consumer_secret'],
        token = os.environ['twitter_token'],
        token_secret = os.environ['twitter_token_secret']
    )

    t = Twitter(auth=auth)

    # Do a search!
    res = t.search.tweets(q='''%s''' % term)

    # If no results, print that
    if res['statuses'] == []:
        print('No results found!')


    # Iterate through each tweet/status
    # Currently just prints in the CLI, later want to write to file
    for tweet in res['statuses']:
        try:
            # Read in one line of the file, convert it into a json object
            # print(tweet['id'] # This is the tweet's id
            print(tweet['created_at']) # when the tweet posted
            print(tweet['text']) # content of the tweet

            # print(tweet['user']['id'] # id of the user who posted the tweet
            print(tweet['user']['name']) # name of the user, e.g. "Wei Xu"
            # print(tweet['user']['screen_name'] # name of the user account, e.g. "cocoweixu"
            print()

        except:
            # read in a line is not in JSON format (sometimes error occured)
            print('Iterating on the results didnt seem to work')
            continue


def main():
    term = input('What term would you like to search for?\nUse quotation marks if desired\n')
    gettweets(term)


if __name__ == '__main__':
    main()
