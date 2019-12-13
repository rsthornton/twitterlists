""" 
A script to identify the most retweeted tweets from a specified list of users

"""

import tweepy
import pandas as pd
import json
# Connect to Twitter API


auth = tweepy.OAuthHandler("bZjygvWPWHA5M4o7AHTrMnKjV", "R8lSiVHIkCeg2RDn74uaN0zteI3aLz6NnHi9RWj0T7D2ILHmLl" )
auth.set_access_token("365249100-ygySokQkQrh8z4pWAZyGonQxVw0eA3lucuS1aJCU", "BqNmTdXhRgqNBPmmr4UFg0eLtyVetxshWxEUVoBJAbAIM")
api = tweepy.API(auth)

# Store timeline of tweets from list members as a list of "ResultSet" objects

  
gaming_list = api.list_timeline(screen_name='@shingaithornton', slug = "Blockchain-gaming", owner_screen_name='@shingaithornton', include_rts = 'false', count = 10000)
eth_list = api.list_timeline(screen_name='@shingaithornton', slug = "ETH", owner_screen_name='@shingaithornton', include_rts = 'false', count = 10000)
econ_list = api.list_timeline(screen_name='@shingaithornton', slug = "Economics", owner_screen_name='@shingaithornton', include_rts = 'false', count = 10000)

twitter_lists = [gaming_list, eth_list, econ_list]


# Isolate json of tweepy "status" objects, add them into a list of dictionaries

my_list_of_dicts = []

gaming_dict = []
eth_dict = []
econ_dict = []

for each_list in twitter_lists:
    for each_json_tweet in each_list:
        
        if each_list == gaming_list:    
            gaming_dict.append(each_json_tweet._json)
        
        elif each_list == eth_list:
            eth_dict.append(each_json_tweet._json)
            
        elif each_list == econ_list:
            econ_dict.append(each_json_tweet._json)
            
      
# Write dictionaries of tweets into text files
with open('tweet_json_gaming.txt', 'w') as file:
    file.write(json.dumps(gaming_dict, indent=4))
    
with open('tweet_json_eth.txt', 'w') as file:
    file.write(json.dumps(eth_dict, indent=4))

with open('tweet_json_econ.txt', 'w') as file:
    file.write(json.dumps(econ_dict, indent=4))    
    
# Set up dataframes from text files

my_eth_list = []
with open('tweet_json_eth.txt', encoding='utf-8') as json_file:
    all_data = json.load(json_file)
    for each_dictionary in all_data:
        text = each_dictionary['text']
        retweet_count = each_dictionary['retweet_count']
        favorite_count = each_dictionary['favorite_count']
        user_name = each_dictionary['user']['name']
        created_at = each_dictionary['created_at']
        
        try:
            url = each_dictionary['entities']['urls'][0]['url']
        except:
            url = 'none'
        
        my_eth_list.append({'text': str(text),
                             'retweet_count': int(retweet_count),
                             'url': str(url),
                             'combo': (int(retweet_count) + int(favorite_count)),
                             'user_name': str(user_name),
                             'created_at': str(created_at)
                            })

my_gaming_list = []
with open('tweet_json_gaming.txt', encoding='utf-8') as json_file:
    all_data = json.load(json_file)
    for each_dictionary in all_data:
        text = each_dictionary['text']
        retweet_count = each_dictionary['retweet_count']
        favorite_count = each_dictionary['favorite_count']
        user_name = each_dictionary['user']['name']
        created_at = each_dictionary['created_at']
        
        try:
            url = each_dictionary['entities']['urls'][0]['url']
        except:
            url = 'none'
        
        my_gaming_list.append({'text': str(text),
                             'retweet_count': int(retweet_count),
                             'url': str(url),
                             'combo': (int(retweet_count) + int(favorite_count)),
                             'user_name': str(user_name),
                             'created_at': str(created_at)
                            })    
my_econ_list = []
with open('tweet_json_econ.txt', encoding='utf-8') as json_file:
    all_data = json.load(json_file)
    for each_dictionary in all_data:
        text = each_dictionary['text']
        retweet_count = each_dictionary['retweet_count']
        favorite_count = each_dictionary['favorite_count']
        user_name = each_dictionary['user']['name']
        created_at = each_dictionary['created_at']
        
        try:
            url = each_dictionary['entities']['urls'][0]['url']
        except:
            url = 'none'
        
        my_econ_list.append({'text': str(text),
                             'retweet_count': int(retweet_count),
                             'url': str(url),
                             'combo': (int(retweet_count) + int(favorite_count)),
                             'user_name': str(user_name),
                             'created_at': str(created_at)
                            })    
    
# Create dataframe
ethereum_DF = pd.DataFrame(my_eth_list, columns = 
                           ['text', 'retweet_count', 'combo', 'url', 'user_name', 'created_at'])

gaming_DF = pd.DataFrame(my_gaming_list, columns = 
                           ['text', 'retweet_count', 'combo', 'url', 'user_name', 'created_at'])

econ_DF = pd.DataFrame(my_econ_list, columns = 
                           ['text', 'retweet_count', 'combo', 'url', 'user_name', 'created_at'])

# Dataframe of 10 most retweeted tweets

top_eth_retweets = ethereum_DF.nlargest(50, ['retweet_count'])

top_gaming_retweets = gaming_DF.nlargest(50, ['retweet_count'])

top_econ_retweets = econ_DF.nlargest(50, ['retweet_count'])
