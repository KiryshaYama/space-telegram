import requests
import os
import urllib.parse


from pathlib import Path


def download_image(img_url, folder_name, params=None):
    response = requests.get(img_url, params=params)
    response.raise_for_status()
    filename = os.path.split(urllib.parse.urlsplit(
        urllib.parse.unquote(img_url)).path)[1]
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    filepath = os.path.join(folder_name, filename)
    with open(filepath, 'wb') as file:
        file.write(response.content)

