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

usage = """
        This is a simple command line interface to the Twitter API using the Tweepy Library.

        Usage:

            python twitter_cli.py [OPTIONS] [USERNAME|QUERY]

            options:
                --user [username]       :  prints a user details from a given username
                --search [query]        :  prints search results for a particular query
                --timeline [username]   :  prints the last tweets of a user
                --followers [username]  :  prints the usernames of the followers of a particular user
                --friends [username]    :  prints the usernames of the people a user follows
                --help                  :  prints this usage message

        Examples:
            To get NaiRobley's details:

                python twitter_cli.py --user NaiRobley

            To get the usernames of NaiRobley's followers:

                python twitter_cli.py --followers NaiRobley

            To search for users called 'Robley':

                python twitter_cli.py --search Robley
        """


def get_user_details(username):
    """
    This function receives a usernames and returns the following details of the user if they exist:
     - Name
     - Username
     - Location
     - Friends
     - Followers count
    """
    user = api.get_user(username)
    print('\n{}\'s details:'.format(username))
    print('\tName: ' + user.name)
    print('\tUsername: ' + user.screen_name)
    print('\tLocation: ' + user.location)
    print('\tFriends: ' + str(user.friends_count))
    print('\tFollowers Count: ' + str(user.followers_count))
    print('')


def get_user_tweets(username):
    """
    This function prints the latest tweets of a particular user given the username
    """
    timeline = api.user_timeline(username)
    print('\n{}\'s latest tweets:'.format(username))
    for tweet in timeline:
        print('\t'+tweet.text)
        print('')


def search_users(query):
    """
    This function receives a query from the user and prints the results of the search
    """
    results = api.search_users(query)
    print('\nThe search for {} has returned the following results:'.format(query))
    for result in results:
        print('\t'+result.screen_name)
    print('')
    return results


def get_user_friends(username):
    """
    This function receives a username and returns the usernames of the users the user follows
    """
    results = api.friends(username)
    print('\n{} follows:'.format(username))
    for result in results:
        print('\t'+result.screen_name)
    print('')


def get_user_followers(username):
    """
    This function receives a username and returns the usernames of the users that follow the user
    """
    results = api.followers(username)
    print('\n{}\'s followers:'.format(username))
    for result in results:
        print('\t'+result.screen_name)
    print('')


def main():
    """
    This is the main function that receives arguments from the command line and calls the respectful functions
    """
    if len(sys.argv) <= 2:
        print(usage)
    elif len(sys.argv) > 2:
        if sys.argv[1] == "--user":
            if sys.argv[2]:
                try:
                    get_user_details(sys.argv[2])
                except TweepError:
                    print("Check the username you provided and try again and try again")
            else:
                print("Usage: python twitter_on_cli.py --user [username]")

        elif sys.argv[1] == "--search":
            if sys.argv[2]:
                try:
                    search_results = search_users(sys.argv[2])
                except TweepError:
                    print("Check the query you provided and try again and try again")
            else:
                print("Usage: python twitter_on_cli.py --search [name]")

        elif sys.argv[1] == "--timeline":
            if sys.argv[2]:
                try:
                    get_user_tweets(sys.argv[2])
                except TweepError:
                    print("Check the username you have provided and try again")
            else:
                print("Usage: python twitter_on_cli.py --timeline [username]")

        elif sys.argv[1] == "--followers":
            if sys.argv[2]:
                try:
                    get_user_followers(sys.argv[2])
                except TweepError:
                    print("Check the username you have provided and try again")
            else:
                print("Usage: python twitter_on_cli.py --followers [username]")

        elif sys.argv[1] == "--friends":
            if sys.argv[2]:
                try:
                    get_user_friends(sys.argv[2])
                except TweepError:
                    print("Check the username you provided and try again")
            else:
                print("Usage: python twitter_on_cli.py --friends [username]")

        elif sys.argv[1] == "--help":
            print(usage)

        else:
            print(usage)


if __name__ == '__main__':
    main()
