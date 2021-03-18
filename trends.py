
import os
import tweepy as tw
import pandas as pd
import requests
from operator import itemgetter
from requests_oauthlib import OAuth1Session
from textblob import TextBlob
from wp import sendEmail
import re

r = requests.get('https://cybur.xyz', auth=('cocobtime', '!!!!Mutombo7'))
print(r.status_code)



consumer_key = "6d8DKJd40bk0vRYdMEAiVwkYZ"
consumer_secret ="Rbb8mQsAH1AauBrDCX0gSRwvBCWpjZ7JWnm4QUKNVRv0LlPiHE"


access_token = "96386626-HfbI5n0o8ukwYkQb2RubIGinJASegtWZH6vyujr6F"


access_token_secret = "TJBg4GV00QJthvUNHgrfXmYMbAiFaBXjcZa87p7QMMI8M"


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


#Make call on home timeline, print each tweets text


#WOEID of usa

def trends():
    

    woeid = 23424977
    data = api.trends_place(id = woeid, exclude = "hashtags") 


    trends = data[0]["trends"]

    trends = filter(itemgetter("tweet_volume"), trends)

    sorted_trends = sorted(trends, key=itemgetter("tweet_volume"), reverse=True)
            
    trends = '\n'.join(trend['name'] for trend in sorted_trends[:1])
    
   

    query = trends
    
    kk = query
    tweet =[]
    
    #clean the tweet and looping
    #adding the gloogle picture into it string
    #adding the grammaly
    


    #xx = api.search(q= f'{kk} -filter:retweets', count=40, lang="en")
    
    xx = tw.Cursor(api.search, q= f'{kk} -filter:retweets', count=40, lang="en").items(50)
    
    
    
    #xx = tw.Cursor(api.search, q="Nepal", result_type="recent", lang="en").items(5)
    for i in xx:
        
        
        i = re.sub(r"http\S+", "", (i.text))
        
        
        i =  re.sub('@[\w]+','',i)
        i =  re.sub('#[\w]+','',i)
        tweet.append(i)
        kk= i
        
        
  
        
        
      
    
  
    sendEmail(tweet,kk)




print('  ***** : @retweets  email send')
trends()

        
#above we are just getting the top trend in usa.
# now time to get them a loop and search twitter useful withthe info










