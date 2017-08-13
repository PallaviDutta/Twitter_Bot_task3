
import tweepy as ty
import random


CONSUMER_KEY="DdugkADlTTPwOxjRkVhWAXqXJ"
CONSUMER_SECRET="pAWrNFKfg6GoJ5FG88UmzihivWJzCUgeHyRM6zvZNhk85vFJXj"
ACCESS_TOKEN="790019103649955840-pc0jp8OIKF7Ct23aE7LJ1qA2UEdXWKg"
ACCESS_SECRET="xtvhSi0oabLNS58mO9w1Wf9YDqwnHM3I0bOvXpvjTNrkK"



def setTwitterAuth():
    auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = ty.API(auth)
    return api


def tweetHelloWorld(api):
    api.update_status("This is an automated tweet"
                      .format(random.randint(0, 10000)))


def getTimeline(api, user):
    tweets = api.user_timeline(user.screen_name, count=100)
    tweets = [tweet for tweet in tweets]
    print(tweets[0])
    return tweets


def getLastTweet(api, user):
    api.update_status("My last tweet is as"
                      " follows...#{}".format(random.randint(0, 10000)))
    tweets = getTimeline(api, user)
    tweets = [tweet.text for tweet in tweets]

    # try catch for various errors that are possible with the api.
    try:
        if len(tweets) == 1:
            api.update_status("This shouldn't be possible...#{}!"
                              .format(random.randint(0, 10000)))
        else:
            tweet = tweets[0]
            api.update_status(tweet[:14] + "...wait, my last tweet was about"
                              " tweeting my last tweet, do'oh! #{}".
                              format(random.randint(0, 10000)))
    except ty.RateLimitError:
        print("You've hit the API limit! Try your bot in about an hour.")
    except ty.TweepError as e:
        print("You've hit another error. This could be a lot of things, but {}".format(e))


def searchTweet(api, searchTerm):
    searchResults = [status for status in ty.
                     Cursor(api.search, q=searchTerm).items(100)]
    searchTweetID = searchResults[0].id
    likedStatus = api.create_favorite(searchTweetID)
    api.update_status("Liked tweet with #IOT!".format(random.randint(0, 10000)))

def likeTweetOfUser(api,boltuser,user) :
    tweet = api.user_timeline(boltuser, count=1)
    tweetID=tweet[0].id
    likedTweet=api.create_favorite(tweetID)
    api.update_status("Liked tweet")



def replyHelloWorld(api, searchResults):
    randomTweet = searchResults[random.randint(0, len(searchResults) - 1)]
    tweet = ("@{} This is a demo search for 'hello world' with a botT, hello"
             " world! #{}".format(randomTweet.user.screen_name,
                                  random.randint(0, 10000)))
    tweetID = randomTweet.id
    api.update_status(tweet, tweetID)


if __name__ == "__main__":
    api = setTwitterAuth()
    user = api.me()
    print(user.screen_name)

    api.update_status("I have {} followers and follow {} accounts #{} LATESTT 2!!!"
                      .format(user.followers_count, user.friends_count,
                              random.randint(0, 10000)))

    getTimeline(api, user)

    search = "#IOT"
    searchTweet(api, search)


    likeTweetOfUser(api, "@boltiot", user)
