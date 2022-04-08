import os

from dotenv import load_dotenv
load_dotenv()


import telegram
bot = telegram.Bot(token=os.environ['TELEGRAM_SPACE_API'])
bot.send_message(chat_id='@Space_pictures_original', text="I'm sorry Dave I'm afraid I can't do that.")