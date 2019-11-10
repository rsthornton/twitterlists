""" 
A script to identify the most retweeted tweets from a specified list of users

Available lists:

Blockchain_gaming
ETH
Economics 
AI
Bitcoin
Space
Systems
"""

import tweepy
import pandas as pd
import json

# Connect to Twitter API

#API, API_secret = input("Enter your Consumer API Key: "), input("Enter your API Secret Key: ")
#Access, Access_secret = input("Enter your Access token: "), input("Enter your Access token secret: ")
#auth = tweepy.OAuthHandler(API, API_secret)
#auth.set_access_token(Access, Access_secret)
#api = tweepy.API(auth)

auth = tweepy.OAuthHandler("bZjygvWPWHA5M4o7AHTrMnKjV", "R8lSiVHIkCeg2RDn74uaN0zteI3aLz6NnHi9RWj0T7D2ILHmLl" )
auth.set_access_token("365249100-ygySokQkQrh8z4pWAZyGonQxVw0eA3lucuS1aJCU", "BqNmTdXhRgqNBPmmr4UFg0eLtyVetxshWxEUVoBJAbAIM")
api = tweepy.API(auth)

# Store timeline of tweets from list members as "ResultSet" objects

my_slug = input("Enter a list name: ")
  
my_list = api.list_timeline(screen_name='@shingaithornton', slug = my_slug, owner_screen_name='@shingaithornton', include_rts = 'false', count = 10000)


# Isolate json of tweepy "status" objects, add them into a list of dictionaries

my_list_of_dicts = []
for each_json_tweet in my_list:
    my_list_of_dicts.append(each_json_tweet._json)
    
    
# Write list of tweets into a text file
with open('tweet_json_ethereum.txt', 'w') as file:
    file.write(json.dumps(my_list_of_dicts, indent=4))
    
# Set up dataframe from information in text file 

my_demo_list = []
with open('tweet_json_ethereum.txt', encoding='utf-8') as json_file:
    all_data = json.load(json_file)
    for each_dictionary in all_data:
        text = each_dictionary['text']
        retweet_count = each_dictionary['retweet_count']
        user_name = each_dictionary['user']['name']
        #url = each_dictionary['entities']['urls'][0]['url']
        created_at = each_dictionary['created_at']
        my_demo_list.append({'text': str(text),
                             'retweet_count': int(retweet_count),
                             #'url': str(url),
                             'user_name': str(user_name),
                             'created_at': str(created_at)
                            })
# Create dataframe
ethereum_DF = pd.DataFrame(my_demo_list, columns = 
                           ['text', 'retweet_count', 'user_name', 'created_at'])


# Dataframe of 10 most retweeted tweets

topretweets = ethereum_DF.nlargest(25, ['retweet_count'])
