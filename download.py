import requests
import os
import urllib.parse


from pathlib import Path


def check_for_errors(response):
    response.raise_for_status()
    if response.history:
        raise requests.HTTPError()


def download_image(img_url, folder_name):
    response = requests.get(img_url)
    response.raise_for_status()
    filename = os.path.split(urllib.parse.urlsplit(
        urllib.parse.unquote(img_url)).path)[1]
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    filepath = os.path.join(folder_name, filename)
    with open(filepath, 'wb') as file:
        file.write(response.content)

