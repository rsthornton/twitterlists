"""
Resources:    
https://tweepy.readthedocs.io/en/latest/api.html#list-methods   
https://stackoverflow.com/questions/42542327/how-to-extract-information-from-tweepy-resultset
https://stackoverflow.com/questions/27900451/convert-tweepy-status-object-into-json
"""

# Connect to Twitter API
import tweepy

auth = tweepy.OAuthHandler("bZjygvWPWHA5M4o7AHTrMnKjV", "R8lSiVHIkCeg2RDn74uaN0zteI3aLz6NnHi9RWj0T7D2ILHmLl" )
auth.set_access_token("365249100-ygySokQkQrh8z4pWAZyGonQxVw0eA3lucuS1aJCU", "BqNmTdXhRgqNBPmmr4UFg0eLtyVetxshWxEUVoBJAbAIM")
api = tweepy.API(auth)



# Store timeline of tweets from list members as "ResultSet" objects
ethereum = api.list_timeline(list_id='1054920788019572736', include_rts = 'false', count = 50)
blockchain_gaming =  api.list_timeline(list_id="884466365532209153", include_rts = 'false', count = 50)

#return tweets from timeline as ResultSet object 

ethereum

#return text from 1st tweet in ResultSet

ethereum[0]._json['text']

#Return text, retweet count, favorite count, from all tweets in ResultSet
tweet = 0
for tweetdata in ethereum:
    print ('tweet text: ' + ethereum[tweet]._json['text'])
    print ('retweet count: ' + str(ethereum[tweet]._json['retweet_count']))
    print ('favorite count: ' + str(ethereum[tweet]._json['favorite_count']))
    print ('user name: ' + ethereum[tweet]._json['user']['name'])
    print ('screen name: ' + ethereum[tweet]._json['user']['screen_name'])
    tweet += 1
    
tweet = 0
for tweetdata in blockchain_gaming:
    print ('tweet text: ' + blockchain_gaming[tweet]._json['text'])
    print ('retweet count: ' + str(blockchain_gaming[tweet]._json['retweet_count']))
    print ('favorite count: ' + str(blockchain_gaming[tweet]._json['favorite_count']))
    print ('user name: ' + ethereum[tweet]._json['user']['name'])
    print ('screen name: ' + ethereum[tweet]._json['user']['screen_name'])
    tweet += 1
    
