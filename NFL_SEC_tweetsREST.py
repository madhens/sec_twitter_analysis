# -*- coding: utf-8 -*-

import tweepy 
import jsonpickle

access_token = ''
access_token_secret = ''
consumer_key = ''
consumer_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print ("Problem Connecting to API")
    
max_tweets = 10000
tweets_per_query = 100    

search_query='#nfldraft AND #rolltide OR #godawgs OR #wareagle OR #hailstate OR #wooopig OR #geauxtigers OR #hottytoddy OR #spursup OR #anchordown OR #gogators OR #tamu OR #vols OR #mizzou OR #bbn'

tweet_count=0

with open('NFLREST_SEC_Tweets3.txt', 'w') as f:
    for tweet in tweepy.Cursor(api.search,q=search_query, since_id ='1121567957350375424').items(max_tweets):
        f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
        tweet_count += 1
    print("Downloaded {0} tweets".format(tweet_count))        
  
