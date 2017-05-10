import tweepy
from tweepy.error import TweepError
import sys

# Twitter Consumer Key
consumer_key = 'J04qdnQ79EZYWjMaa0OyKcKXh'

# Twitter Consumer Secret
consumer_secret = 'PnuwWaxgWMNzRrH4KlNmzGxh9ahlR0oL3hZm5YBLgkHInhqdmN'

# Twitter Access Token
access_token = '3428706161-FR96devGPwqKR5J3lYrTg4hDCFgQ0ip8tjPOV0A'

# Twitter Access Token Secret
access_token_secret = 'vcX41s5kteTcxZSYVL0f1FVSAGPtlWtOZF9w6Oc2ix2Ua'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def get_user_details(username):
    """
    This function receives a usernames and returns the following details of the user if they exist:
     - Name
     - Username
     - Location
     - Friends
     - Followers count
    """
    try:
        user = api.get_user(username)
        print('\n{}\'s details:'.format(username))
        print('\tName: ' + user.name)
        print('\tUsername: ' + user.screen_name)
        print('\tLocation: ' + user.location)
        print('\tFriends: ' + str(user.friends_count))
        print('\tFollowers Count: ' + str(user.followers_count))
        print('')
    except TweepError:
        print("Check the username you provided or your connection and try again")


def get_user_tweets(username):
    """
    This function prints the latest tweets of a particular user given the username
    """
    try:
        timeline = api.user_timeline(username)
        print('\n{}\'s latest tweets:'.format(username))
        for tweet in timeline:
            print('\t' + tweet.text)
            print('')
    except TweepError:
        print("Check the username you provided or your connection and try again")


def search_users(query):
    """
    This function receives a query from the user and prints the results of the search
    """
    try:
        results = api.search_users(query)
        print('\nThe search for {} has returned the following results:'.format(query))
        for result in results:
            print('\t' + result.screen_name)
        print('')
        return results
    except TweepError:
        print("Check the query you provided or your connection and try again")


def get_user_friends(username):
    """
    This function receives a username and returns the usernames of the users the user follows
    """
    try:
        results = api.friends(username)
        print('\n{} follows:'.format(username))
        for result in results:
            print('\t' + result.screen_name)
        print('')
    except TweepError:
        print("Check the username you provided or your connection and try again")


def get_user_followers(username):
    """
    This function receives a username and returns the usernames of the users that follow the user
    """
    try:
        results = api.followers(username)
        print('\n{}\'s followers:'.format(username))
        for result in results:
            print('\t' + result.screen_name)
        print('')
    except TweepError:
        print("Check the username you provided or your connection and try again")
