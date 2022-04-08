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
    check_for_errors(response)
    filename = os.path.split(urllib.parse.urlsplit(urllib.parse.unquote(img_url)).path)[1]
    filepath = get_file_path(folder_name, filename)
    with open(filepath, 'wb') as file:
        file.write(response.content)

def get_file_path(folder_name, filename):
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    return os.path.join(folder_name, filename)