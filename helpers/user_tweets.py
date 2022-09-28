
from datetime import datetime, timezone
import tweepy


def get_user_tweets(client: tweepy.Client, user_name: str, start_date: datetime.astimezone, end_date: datetime.astimezone):
    """Get User's Tweets
    This endpoint/method returns Tweets composed by a single user,
    specified by the requested user ID

    :param user_name
    :return: [user tweets]
    """

    # Get user by username
    user = client.get_user(username=user_name)
    if not user.data:
        # if there is no user, return None
        return None
    user = user.data

    # Get user tweets
    # TODO: find a way to filter by hashtag here
    users_tweets = client.get_users_tweets(
        id=user.id,
        end_time=start_date,
        start_time=end_date
    )
    return users_tweets.data


def get_user_tweets_by_hashtag(client: tweepy.Client, user_name: str, start_date: datetime.astimezone, end_date: datetime.astimezone):
    """Get User's tweets which has the hashtag

    :param user_name
    """
    # call the get_user_tweets function
    users_tweets = get_user_tweets(client, user_name, start_date, end_date)
    if users_tweets:
        for tweet in users_tweets:
            # TODO: return len user tweets
            # TODO: if there is no way to filter by hashtag, then write a custom filter
            print(tweet.id)
            print(tweet.text)
