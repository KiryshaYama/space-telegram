import requests
import datetime
import os

from download import download_image
from dotenv import load_dotenv
load_dotenv()

def fetch_nasa_epic():
    date = datetime.date.today() - datetime.timedelta(days=2)
    folder_name = './epic'
    api_key=os.environ['NASA_API_KEY']
    imgs_url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}?api_key={api_key}"
    response = requests.get(imgs_url)
    imgs_response = response.json()
    for img_response in imgs_response:
        filename = img_response['image']
        img_link = f'https://api.nasa.gov/EPIC/archive/natural/{date.strftime("%Y/%m/%d")}/png/{filename}.png?api_key={api_key}'
        download_image(img_link, folder_name)

def main():
    fetch_nasa_epic()

if __name__ == '__main__':
    main()