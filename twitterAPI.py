"""
    FileName:       Twitter-API
    Author:         Devavrat Kalam
    Language:       Python3
    Description:    Code to get started with Twitter API.
                    Prints covid19 tweets
"""

# Import libraries
import json
import tweepy

# Open config file and set your Twitter App's unique keys with Reddit's API
with open("config.JSON") as f:
    data = json.load(f)
    auth = tweepy.OAuthHandler(data["API_KEY"], data["API_SECRETE_KEY"])
    auth.set_access_token(data["ACCESS_TOKEN"], data["ACCESS_TOKEN_SECRETE"])
    api = tweepy.API(auth)

# Print covid19 tweets from Twitter
covidTweets = api.search(q='covid19', lang='en', rpp=5)
for tweet in covidTweets:
    print(tweet.text, "\n")