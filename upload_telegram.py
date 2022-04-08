import os
import time
import random

from dotenv import load_dotenv
load_dotenv()

import telegram
bot = telegram.Bot(token=os.environ['TELEGRAM_SPACE_API'])
posting = True
while posting == True:
    DIR = './images'
    bot.send_photo(chat_id='@Space_pictures_original', photo=open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb')) #('tests/test.png', 'rb'))
    time.sleep(86400)