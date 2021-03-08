## Youtube downloader

This script will create a very simple webpage where you can search for videos in youtube (youtube-search lib) and play / download them (youtube-dl) created with Flask.

## Set up

Put this into a .env file
```
source venv/bin/activate
export APP_SETTINGS="config.DevelopmentConfig"
export FLASK_APP=app.py
export FLASK_ENV=development
```

And run
```
source .env
flask run
```

## DISCLAIMER

This is not intended to be a tool to download unlicenced content, but rather an exercise to show how easy is to build apps using Flask and python libraries.