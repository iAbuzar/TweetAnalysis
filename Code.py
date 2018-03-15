import tweepy
from textblob import TextBlob

consumer_key="CONSUMER_KEY"
consumer_access="CONSUMER_ACCESS"

access_token="ACCESS_TOKEN"
access_token_secret="ACCESS_TOKEN_SECRET"

auth=tweepy.OAuthHandler(consumer_key,consumer_access)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

publicTweet=api.search("ANY_STRING")

for tweet in publicTweet:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
