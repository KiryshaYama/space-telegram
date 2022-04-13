import os
import time
import random
import telegram
import argparse

from dotenv import load_dotenv


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Post photo to telegram channel'
    )
    parser.add_argument(
        'posting_period',
        type=int,
        help='post frequency in seconds'
    )
    return parser.parse_args()


def main():
    load_dotenv()
    args = parse_arguments()
    bot = telegram.Bot(token=os.environ['TELEGRAM_SPACE_API'])
    while True:
        DIR = './images'
        with open(os.path.join(DIR,
                               random.choice(os.listdir(DIR))), 'rb') as photo:
            bot.send_photo(os.environ['chat_id'], photo=photo)
        time.sleep(args.posting_period)


if __name__ == '__main__':
    main()
