import tweepy
import telegram
import time
import os

# Twitter API keys
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Telegram API token
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# Setup Twitter API client
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitter_api = tweepy.API(auth)

# Setup Telegram bot
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Function to check for new tweets
def check_tweets():
    last_seen_id = None
    while True:
        try:
            tweets = twitter_api.user_timeline(screen_name='0xMoei', since_id=last_seen_id, tweet_mode='extended')
            for tweet in reversed(tweets):
                bot.send_message(chat_id=CHAT_ID, text=tweet.full_text)
                last_seen_id = tweet.id
            time.sleep(60)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    check_tweets()
