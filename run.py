import ConfigParser
import tweepy


def configurations():

    # creating config objects
    config = ConfigParser.RawConfigParser()
    config.read('config.cfg')

    # getting twitter properties
    TWITTER_API_KEY = config.get('Twitter', 'API_KEY')
    TWITTER_API_SECRET = config.get('Twitter', 'API_SECRET')
    TWITTER_ACCESS_TOKEN = config.get('Twitter', 'ACCESS_TOKEN')
    TWITTER_ACCESS_TOKEN_SECRET = config.get('Twitter', 'ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    return api

if __name__ == "__main__":
    configurations()