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


#Return text from all tweets in ResultSet
tweet = 0
for tweetcount in ethereum:
    print (ethereum[tweet]._json['text'])
    tweet += 1
