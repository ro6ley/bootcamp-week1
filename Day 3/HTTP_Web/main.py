#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is a simple command line interface to the Twitter API using the Tweepy Library.

Usage:
    twitter_cli user <username>
    twitter_cli search <query>
    twitter_cli timeline <username>
    twitter_cli followers <username>
    twitter_cli friends <username>
    twitter_cli (-i | --interactive)
    twitter_cli (-h | --help)
    twitter_cli quit

Options:
    -i, --interactive     :  runs the script in interactive mode
    -h, --help            :  prints this help message
    user <username>       :  prints a user details from a given username
    search <query>        :  prints search results for a particular query
    timeline <username>   :  prints the last tweets of a user
    followers <username>  :  prints the usernames of the followers of a particular user
    friends <username>    :  prints the usernames of the people a user follows
    quit                  : exit interactive mode
"""

import sys
import os
import cmd
from docopt import docopt, DocoptExit
from twitter_cli import *


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyTwitterCLI(cmd.Cmd):
    prompt = 'twitter_CLI >>> '
    file = None
    print(__doc__)

    @docopt_cmd
    def do_user(self, args):
        """Usage: user <username>"""
        get_user_details(args["<username>"])

    @docopt_cmd
    def do_search(self, args):
        """Usage: search <query>"""
        search_users(args["<query>"])

    @docopt_cmd
    def do_timeline(self, args):
        """Usage: timeline <username>"""
        get_user_tweets(args["<username>"])

    @docopt_cmd
    def do_followers(self, args):
        """Usage: followers <username>"""
        get_user_followers(args["<username>"])

    @docopt_cmd
    def do_friends(self, args):
        """Usage: friends <username>"""
        get_user_friends(args["<username>"])

    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyTwitterCLI().cmdloop()

print(opt)
