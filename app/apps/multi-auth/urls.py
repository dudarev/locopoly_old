# -*- coding: utf-8 -*-
"""
    urls
    ~~~~

    URL definitions.

    :copyright: 2009 by tipfy.org.
    :license: BSD, see LICENSE.txt for more details.
"""
from tipfy import Rule, import_string


def get_rules(app):
    """Returns a list of URL rules for the application. The list can be
    defined entirely here or in separate ``urls.py`` files.

    :param app:
        The WSGI application instance.
    :return:
        A list of class:`tipfy.Rule` instances.
    """
    rules = [
        Rule('/auth/home', endpoint='auth/home', handler='apps.multi-auth.handlers.HomeHandler'),
        Rule('/auth/login', endpoint='auth/login', handler='apps.multi-auth.handlers.LoginHandler'),
        Rule('/auth/logout', endpoint='auth/logout', handler='apps.multi-auth.handlers.LogoutHandler'),
        Rule('/auth/signup', endpoint='auth/signup', handler='apps.multi-auth.handlers.SignupHandler'),
        Rule('/auth/register', endpoint='auth/register', handler='apps.multi-auth.handlers.RegisterHandler'),

        Rule('/auth/facebook/', endpoint='auth/facebook', handler='apps.multi-auth.handlers.FacebookAuthHandler'),
        Rule('/auth/friendfeed/', endpoint='auth/friendfeed', handler='apps.multi-auth.handlers.FriendFeedAuthHandler'),
        Rule('/auth/google/', endpoint='auth/google', handler='apps.multi-auth.handlers.GoogleAuthHandler'),
        Rule('/auth/twitter/', endpoint='auth/twitter', handler='apps.multi-auth.handlers.TwitterAuthHandler'),
        Rule('/auth/yahoo/', endpoint='auth/yahoo', handler='apps.multi-auth.handlers.YahooAuthHandler'),

        Rule('/content', endpoint='content/index', handler='apps.multi-auth.handlers.ContentHandler'),
    ]

    return rules
