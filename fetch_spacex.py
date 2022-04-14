import requests

from make_directory import make_directory
from download import download_image


def fetch_spacex_last_launch(folder_name):
    imgs_url = "https://api.spacexdata.com/v4/launches/latest"
    response = requests.get(imgs_url)
    imgs_links = response.json()['links']['flickr']['original']
    for img_link in imgs_links:
        download_image(img_link, folder_name)


def main():
    folder_name = './images'
    make_directory(folder_name)
    fetch_spacex_last_launch(folder_name)


if __name__ == '__main__':
    main()
