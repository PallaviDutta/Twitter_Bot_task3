from pal_my_keys import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
import tweepy as ty
import random


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
    # set up authorization with twitter via tweepy
    api = setTwitterAuth()
    # tweet hello world!
    #tweetHelloWorld(api)

    # let's get the user object of your bot's account
    user = api.me()
    # let's print the user object so you can see the fields it has
    # print(user)

    # here's your username! Notice how we accessed it?
    print(user.screen_name)
    # Now let's use some of those fields to see your following/followers
    api.update_status("I have {} followers and follow {} accounts #{} LATESTT 2!!!"
                      .format(user.followers_count, user.friends_count,
                              random.randint(0, 10000)))
    # Now let's get the last tweet of yours...
    getTimeline(api, user)
    # getLastTweet(api, user)

    # let's search for the literal "hello world" <-- notice how I escape the
    # quotes below. This will get me the terms with that specific string.
    search = "#IOT"
    searchTweet(api, search)
    #api.update_status("Liked tweet with #IOT!")

    likeTweetOfUser(api, "@boltiot", user)
    # lets tweet at one of the tweets we found with search
    # replyHelloWorld(api, searchResults)