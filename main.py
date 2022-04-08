import requests
import os
import urllib.parse
import datetime
from pathlib import Path

def check_for_errors(response):
    response.raise_for_status()
    if response.history:
        raise requests.HTTPError()

def download_image(img_url, folder_name):
    response = requests.get(img_url)
    response.raise_for_status()
    check_for_errors(response)
    filename = os.path.split(urllib.parse.urlsplit(urllib.parse.unquote(img_url)).path)[1]
    filepath = get_file_path(folder_name, filename)
    with open(filepath, 'wb') as file:
        file.write(response.content)

def get_file_path(folder_name, filename):
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    return os.path.join(folder_name, filename)

def fetch_spacex_last_launch():
    imgs_url = "https://api.spacexdata.com/v4/launches/latest"
    folder_name='./spacex'
    response = requests.get(imgs_url)
    imgs_links = response.json()['links']['flickr']['original']
    for img_link in imgs_links:
        download_image(img_link, folder_name)

def fetch_nasa_apod():
    imgs_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    folder_name='./apod'
    params = {'count' : 30}
    response = requests.get(imgs_url, params=params)
    imgs_response = response.json()
    for img_response in imgs_response:
        if img_response['media_type'] == 'image':
            img_link = img_response['hdurl']
            download_image(img_link, folder_name)

def fetch_nasa_epic():
    date = datetime.date.today() - datetime.timedelta(days=2)
    folder_name = './epic'
    imgs_url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}?api_key=DEMO_KEY"
    response = requests.get(imgs_url)
    imgs_response = response.json()
    for img_response in imgs_response:
        filename = img_response['image']
        img_link = f'https://api.nasa.gov/EPIC/archive/natural/{date.strftime("%Y/%m/%d")}/png/{filename}.png?api_key=DEMO_KEY'
        download_image(img_link, folder_name)

def main():
    fetch_spacex_last_launch()
    fetch_nasa_apod()
    fetch_nasa_epic()

if __name__ == '__main__':
    main()