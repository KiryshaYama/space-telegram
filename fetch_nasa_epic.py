import requests
import datetime
import os

from pathlib import Path
from download import download_image
from dotenv import load_dotenv


def fetch_nasa_epic(folder_name, api_key):
    date = datetime.date.today() - datetime.timedelta(days=2)
    params = {'api_key': api_key}
    imgs_url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}"
    response = requests.get(imgs_url, params=params)
    response.raise_for_status()
    imgs_response = response.json()
    for img_response in imgs_response:
        filename = img_response['image']
        img_link = f'https://api.nasa.gov/EPIC/archive/natural/' \
                    f'{date.strftime("%Y/%m/%d")}/png/{filename}.png'
        download_image(img_link, folder_name, params)


def main():
    load_dotenv()
    folder_name = './images'
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    fetch_nasa_epic(folder_name, api_key=os.environ['NASA_API_KEY'])

if __name__ == '__main__':
    main()
