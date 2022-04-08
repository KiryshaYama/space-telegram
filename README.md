# Space-telegram


These are three scripts:
- `fetch_spacex.py` download images from last lounch [SpaceX api](https://api.spacexdata.com/v4/launches/latest)
- `fetch_nasa_apod.py` download 30 randon images from [NASA APOD api](https://api.nasa.gov/#apod)
- `fetch_nasa_epic.py` download Earth images taken 2 days ago from [NASA EPIC api](https://api.nasa.gov/#epic)
- `upload_telegram.py` prepare downloaded images and upload them to telegram channel

### How to install


SpaceX images downloading does not require any keys. 
NASA images downloading you need api-key. Put them into
`.env` file, and assign api-key to the `NASA_API_KEY` variable.
To upload images you need telegram token. Put them into
`.env` file, and assign token to the `TELEGRAM_SPACE_API` variable.
Put posting period into
`.env` file, and assign period to the `POSTING_PERIOD` variable.
It should look like this:

```
NASA_API_KEY='Your_API-Key'
TELEGRAM_SPACE_API='Your_telegram_token'
POSTING_PERIOD='Your posting_period'
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

Run scripts in command line:
```
python3 fetch_spacex.py
python3 fetch_nasa_apod.py
python3 fetch_nasa_epic.py
python3 upload_telegram.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).