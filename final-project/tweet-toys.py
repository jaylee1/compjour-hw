#IMPORTING JSON MATERIAL

import requests
import json
data_url = 'http://www.saferproducts.gov/RestWebServices/Recall?Title=Child&format=json'
data = json.loads(requests.get(data_url).text)
## data is the list with all the json

## If you want the first 100 (or however many) characters of the title
txt = (data[0]['Title'])
if len(txt) > 100:
        txt = txt[0:98] + '...'
#print(txt)

## If you want all the Descriptions
#for num in range(0, len(data)):
        #print(data[num]['Description'])

## If you want all the recall dates in YYYY-MM-DD
#for num in range(0, len(data)):
        #date = (data[num]['RecallDate'][:10])
        #print(date)

## For the URL of press release
url = (data[0]['URL'])
        #print(url)

## To get ONE of the image urls (I don't think we need to automate to get more than one)
## For num in range(0, len(data)):
        #print(data[num]['Images'][0]['URL'])



#CONSTRUCTING OUR TWEET
tweet = txt + " " + url
print(tweet)



#IMPORTING TWEEPY
import tweepy

CONSUMER_KEY = "7wQ71COzIJBULQfqipHAcD2Vp"
CONSUMER_SECRET = "i94KfBSa20IvJBCmWpAoEGRJkcL8W1pSXYjYrMmfN0vYc4dey3"
ACCESS_TOKEN = "3316695911-Ldb6PbZKvEZwCmE3bO1WSMzLgprC9qITD7AUFrf"
ACCESS_TOKEN_SECRET = "ZqN0yvfDqNFP4BfG0coutJ6hOtuL39UW6qWCfwSsNPsmV"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#ACTUALLY TWEETING
api.update_status(status = tweet)