""" 
A script to identify the most retweeted tweets from curated user lists

"""
import tweepy
import pandas as pd
import json

# Connect to Twitter API

auth = tweepy.OAuthHandler("bZjygvWPWHA5M4o7AHTrMnKjV", "R8lSiVHIkCeg2RDn74uaN0zteI3aLz6NnHi9RWj0T7D2ILHmLl" )
auth.set_access_token("365249100-ygySokQkQrh8z4pWAZyGonQxVw0eA3lucuS1aJCU", "BqNmTdXhRgqNBPmmr4UFg0eLtyVetxshWxEUVoBJAbAIM")
api = tweepy.API(auth)

# Store tweet timelines from list members as a dictionary of "ResultSet" objects

the_lists =  {"gaming" : "Blockchain-gaming", "gurus": "Cryptogurus", "eth" : "ETH", "econ" : "Economics", "ai": "AI", "btc" :  "Bitcoin", "space" :  "Space", "systems" : "Systems"}

for slug in the_lists.keys():
    the_lists[slug] = api.list_timeline(screen_name='@shingaithornton', slug = the_lists[slug], owner_screen_name='@shingaithornton', include_rts = 'false', count = 10000)
   
   
# Isolate json of tweepy "status" objects, add them into a list of dictionaries

gaming_tweets, gurus_tweets, eth_tweets, econ_tweets, ai_tweets, btc_tweets, space_tweets, systems_tweets = [],[],[],[],[],[],[],[]

for each_list in the_lists.values():
    for each_json_tweet in each_list:
        
        if each_list == the_lists['gaming']:
            gaming_tweets.append(each_json_tweet._json)
            
        elif each_list == the_lists['gurus']:
            gurus_tweets.append(each_json_tweet._json)

        elif each_list == the_lists['eth']:
            eth_tweets.append(each_json_tweet._json)
            
        elif each_list == the_lists['econ']:    
            econ_tweets.append(each_json_tweet._json)    
            
        elif each_list == the_lists['ai']:    
            ai_tweets.append(each_json_tweet._json)
        
        elif each_list == the_lists['btc']:
           btc_tweets.append(each_json_tweet._json)
            
        elif each_list == the_lists['space']:
            space_tweets.append(each_json_tweet._json)
        
        elif each_list == the_lists['systems']:
            systems_tweets.append(each_json_tweet._json)
            
# Write dictionaries of tweets into text files
                  
def make_txt(listname, tweets):
    with open('tweet_json_' + str(listname) + '.txt', 'w') as file:
        file.write(json.dumps(tweets, indent=4))
            
make_txt('gaming', gaming_tweets)
make_txt('gurus', gurus_tweets)
make_txt('eth', eth_tweets)
make_txt('econ', econ_tweets)
make_txt('ai', ai_tweets)
make_txt('btc', btc_tweets)
make_txt('space', space_tweets)
make_txt('systems', systems_tweets)
    
# Set up dataframes from text files

gaming_list, gurus_list, eth_list, econ_list, ai_list, btc_list, space_list, systems_list  = [],[],[],[],[],[],[],[]  

def make_list(listname, textfile):
    
   with open(textfile, encoding='utf-8') as json_file:
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
            
            listname.append({'text': str(text),
                                 'retweet_count': int(retweet_count),
                                 'url': str(url),
                                 'combo': (int(retweet_count) + int(favorite_count)),
                                 'user_name': str(user_name),
                                 'created_at': str(created_at)
                                })  

make_list(gaming_list, 'tweet_json_gaming.txt')
make_list(gurus_list, 'tweet_json_gurus.txt')
make_list(eth_list, 'tweet_json_eth.txt')
make_list(econ_list, 'tweet_json_econ.txt')
make_list(ai_list, 'tweet_json_ai.txt')
make_list(btc_list, 'tweet_json_btc.txt')
make_list(space_list, 'tweet_json_space.txt')
make_list(systems_list, 'tweet_json_systems.txt')
   
# Create dataframes

def make_DF(listname):
    listname =  pd.DataFrame(listname, columns = 
                           ['text', 'retweet_count', 'combo', 'url', 'user_name', 'created_at'])
    listname = listname.nlargest(50, ['retweet_count'])
    return listname

eth_df, gaming_df, gurus_df, econ_df, ai_df, btc_df, space_df, systems_df = make_DF(eth_list), make_DF(gaming_list), make_DF(gurus_list), make_DF(econ_list), make_DF(ai_list), make_DF(btc_list), make_DF(space_list), make_DF(systems_list)
