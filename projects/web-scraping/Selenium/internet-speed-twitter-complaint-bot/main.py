from InternetClass import InternetSpeedTwitterBot
import os
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
INTERNET_SPEED_DRIVER_PATH = "https://www.speedtest.net/"
# INTERNET_SPEED_DRIVER_PATH = "https://www.google.com/"
TWITTER_DRIVER_PATH = "https://x.com/home"
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
TWITTER_USERNAME = os.environ["TWITTER_USERNAME"]

internet = InternetSpeedTwitterBot(driver_path=INTERNET_SPEED_DRIVER_PATH)
internet.get_internet_speed()

twitter = internet.tweet_at_provider(TWITTER_DRIVER_PATH)
