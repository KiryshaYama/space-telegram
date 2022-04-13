import requests
import os

from download import download_image
from dotenv import load_dotenv


def fetch_nasa_apod(api_key):
    imgs_url = f"https://api.nasa.gov/planetary/apod"
    folder_name = './images'
    params = {'api_key': api_key, 'count': 3}
    response = requests.get(imgs_url, params=params)
    imgs_response = response.json()
    for img_response in imgs_response:
        if img_response['media_type'] == 'image':
            img_link = img_response['hdurl']
            download_image(img_link, folder_name)


def main():
    load_dotenv()
    fetch_nasa_apod(api_key=os.environ['NASA_API_KEY'])

if __name__ == '__main__':
    main()
