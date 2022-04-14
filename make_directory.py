from pathlib import Path


def make_directory(folder_name):
    Path(folder_name).mkdir(parents=True, exist_ok=True)
