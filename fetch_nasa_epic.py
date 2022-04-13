import requests
import datetime
import os

from download import download_image
from dotenv import load_dotenv


def fetch_nasa_epic(api_key):
    date = datetime.date.today() - datetime.timedelta(days=2)
    folder_name = './images'
    params = {'api_key': api_key}
    imgs_url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}"
    response = requests.get(imgs_url, params=params)
    imgs_response = response.json()
    for img_response in imgs_response:
        filename = img_response['image']
        img_link = f'https://api.nasa.gov/EPIC/archive/natural/' \
                   f'{date.strftime("%Y/%m/%d")}/png/{filename}.png'
        download_image(img_link, folder_name, params)


def main():
    load_dotenv()
    fetch_nasa_epic(api_key=os.environ['NASA_API_KEY'])

if __name__ == '__main__':
    main()
