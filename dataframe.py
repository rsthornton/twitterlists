""" 

1. Creating a Pandas dataframe with recent tweets from a list 
2. Identifying the most favorited and retweeted tweets in the dataframe


"""

import tweepy
import pandas as pd
import json

#Connect to Twitter API
API, API_secret = input("Enter your Consumer API Key: "), input("Enter your API Secret Key: ")
Access, Access_secret = input("Enter your Access token: "), input("Enter your Access token secret: ")
auth = tweepy.OAuthHandler(API, API_secret)
auth.set_access_token(Access, Access_secret)
api = tweepy.API(auth)

# Store timeline of tweets from list members as "ResultSet" objects
ethereum = api.list_timeline(list_id='1054920788019572736', include_rts = 'false', count = 50)

# Isolate json of tweepy "status" objects, add them into a list of dictionaries

eth_list_of_dicts = []
for each_json_tweet in ethereum:
    eth_list_of_dicts.append(each_json_tweet._json)
    
    
# Write list of tweets into a text file
with open('tweet_json_ethereum.txt', 'w') as file:
    file.write(json.dumps(eth_list_of_dicts, indent=4))
    
# Set up dataframe from information in text file 

my_demo_list = []
with open('tweet_json_ethereum.txt', encoding='utf-8') as json_file:
    all_data = json.load(json_file)
    for each_dictionary in all_data:
        tweet_id = each_dictionary['id']
        text = each_dictionary['text']
        favorite_count = each_dictionary['favorite_count']
        retweet_count = each_dictionary['retweet_count']
        created_at = each_dictionary['created_at']
        user_name = each_dictionary['user']['name']
        screen_name = each_dictionary['user']['screen_name']
        my_demo_list.append({'tweet_id': str(tweet_id),
                             'text': str(text),
                             'favorite_count': int(favorite_count),
                             'retweet_count': int(retweet_count),
                             'created_at': created_at,
                             'user_name': str(user_name),
                             'screen_name': str(screen_name)
                            })
# Create dataframe
ethereum_DF = pd.DataFrame(my_demo_list, columns = 
                           ['tweet_id', 'text', 'favorite_count', 'retweet_count', 'created_at', 'user_name', 'screen_name'])


# Dataframe of 10 most favorited tweets
topfavorites = ethereum_DF.nlargest(10, ['favorite_count'])


# Dataframe of 10 most retweeted tweets

topretweets = ethereum_DF.nlargest(10, ['retweet_count'])
