# TweetScraper

Twitter scraper for UCLA DataRes Spring 2020 coronavirus article. Scrapes tweets from state governors and senators, and outputs data in .txt format.

## Usage

Download dependencies

```
python -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Generate scraped data

```
python scrape_tweets.py
```

## Built With

* [GetOldTweets3](https://pypi.org/project/GetOldTweets3/) - python3 library for accessing old tweets
