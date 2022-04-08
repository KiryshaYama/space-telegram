import requests
from download import download_image

def fetch_spacex_last_launch():
    imgs_url = "https://api.spacexdata.com/v4/launches/latest"
    folder_name='./images'
    response = requests.get(imgs_url)
    imgs_links = response.json()['links']['flickr']['original']
    for img_link in imgs_links:
        download_image(img_link, folder_name)

def main():
    fetch_spacex_last_launch()

if __name__ == '__main__':
    main()