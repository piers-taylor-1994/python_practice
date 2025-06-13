from InternetSpeedTwitterBot import *

PROMISED_DOWN = 150.00
PROMISED_UP = 10.00

internet_speed_twitter_bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)
internet_speed_twitter_bot.get_internet_speed()

internet_speed_twitter_bot.tweet_at_provider()