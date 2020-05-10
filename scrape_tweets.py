def get_usernames():
    usernames = []
    usernames.append("@JerryBrownGov")
    return usernames


def scrape_tweets(usernames):
    import GetOldTweets3 as got
    max_count = 10

    tweetCriteria = got.manager.TweetCriteria().setUsername(
        usernames[0]).setMaxTweets(max_count)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    user_tweets = [[tweet.date, tweet.text] for tweet in tweets]

    print(user_tweets[0][1])


def main():
    # append venv libraries to path before importing
    import os
    import sys
    sys.path.append(os.getcwd() + ('/venv/bin/'))

    # scrape usernames from
    usernames = get_usernames()
    scrape_tweets(usernames)


if __name__ == "__main__":
    main()
