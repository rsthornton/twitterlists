""" 
Creating a Pandas dataframe with recent tweets from a list

"""

# Connect to Twitter API
import tweepy
import pandas as pd
import json

auth = tweepy.OAuthHandler("bZjygvWPWHA5M4o7AHTrMnKjV", "R8lSiVHIkCeg2RDn74uaN0zteI3aLz6NnHi9RWj0T7D2ILHmLl" )
auth.set_access_token("365249100-ygySokQkQrh8z4pWAZyGonQxVw0eA3lucuS1aJCU", "BqNmTdXhRgqNBPmmr4UFg0eLtyVetxshWxEUVoBJAbAIM")
api = tweepy.API(auth)



# Store timeline of tweets from list members as "ResultSet" objects
ethereum = api.list_timeline(list_id='1054920788019572736', include_rts = 'false', count = 50)

#Isolate json of tweepy status objects, add them into a list

eth_list_of_dicts = []
for each_json_tweet in ethereum:
    eth_list_of_dicts.append(each_json_tweet._json)
    
    
# Write list into a text file
with open('tweet_json_ethereum.txt', 'w') as file:
    file.write(json.dumps(eth_list_of_dicts, indent=4))
    
#Create DataFrame from text file

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
    #create dataframe
    ethereum_DF = pd.DataFrame(my_demo_list, columns = 
                              ['tweet_id', 'text', 'favorite_count', 'retweet_count', 'created_at', 'user_name', 'screen_name'])
    
        
    

    
    







