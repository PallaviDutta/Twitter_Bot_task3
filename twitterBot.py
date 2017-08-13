
from pal_my_keys import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
import tweepy as ty
import random


def setTwitterAuth():
    """
    obtains authorization from twitter API
    """
    # sets the auth tokens for twitter using tweepy
    auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = ty.API(auth)
    return api


def tweetHelloWorld(api):
    """
    this method tweets hello world to twitter with your bot, Hello World!
    """
    api.update_status("This is an automated tweet"
                      " using a bot! Hello, World! #{}"
                      .format(random.randint(0, 10000)))


