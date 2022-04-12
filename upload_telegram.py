import os
import time
import random
import telegram

from dotenv import load_dotenv

load_dotenv()
bot = telegram.Bot(token=os.environ['TELEGRAM_SPACE_API'])
posting = True
while posting is True:
    DIR = './images'
    bot.send_photo(chat_id='@Space_pictures_original',
                   photo=open(os.path.join(
                       DIR, random.choice(os.listdir(DIR))), 'rb'))
    time.sleep(int(os.environ['POSTING_PERIOD']))
