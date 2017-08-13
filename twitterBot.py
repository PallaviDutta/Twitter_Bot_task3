
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


def getTimeline(api, user):
    """
    this method gets the last 100 tweets from the user's timeline. This returns
    a list of tweet objects, check Twitter's docs to learn more about them.
    """
    tweets = api.user_timeline(user.screen_name, count=100)
    tweets = [tweet for tweet in tweets]
    # this will print out the FULL contents of the first tweet object in the
    # list. This is useful to see the data fields available to use for other
    # methods you may want to make.
    print(tweets[0])
    return tweets


def getLastTweet(api, user):
    api.update_status("My last tweet is as"
                      " follows...#{}".format(random.randint(0, 10000)))
    tweets = getTimeline(api, user)
    # take the tweets and remake the list with *only* their text values
    tweets = [tweet.text for tweet in tweets]

    # this print statement will put out the last 100 tweets if you want to see
    # see them. Remember, this one is text only and will be a lot less messy.
    # print(tweets)

    # try catch for various errors that are possible with the api.
    try:
        # should not be possible...but anywho
        if len(tweets) == 1:
            api.update_status("This shouldn't be possible...#{}!"
                              .format(random.randint(0, 10000)))
        else:
            tweet = tweets[0]
            # wait a minute...
            api.update_status(tweet[:14] + "...wait, my last tweet was about"
                              " tweeting my last tweet, do'oh! #{}".
                              format(random.randint(0, 10000)))
    except ty.RateLimitError:
        print("You've hit the API limit! Try your bot in about an hour.")
    except ty.TweepError as e:
        print("You've hit another error. This could be a lot of things, but "
              "I'll leave that to you to debug. The error is {}".format(e))

