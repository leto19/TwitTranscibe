import json
import tweepy as tw
import logging
from setup import create_api
from time import ctime
import requests
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class YetziFaver(tw.StreamListener):
    def __init__(self,api):
        self.api = api
        self.me = api.me()
    def on_status(self, tweet):
        logger.info(f"processing tweet: {tweet.id}")
        print(tweet.text)
        print(tweet.urls)
        if not tweet.favorited and not hasattr(tweet, "retweeted_status"):
            try:
                tweet.favorite()
                logger.info(f"fav successful!")
            except Exception as e:
                logger.error("error on fav", exc_info=True)

    def on_error(self, status):
        logger.error("%s:code:%s"% (ctime(), status))


def get_id_from_at(at, api):
    user = api.get_user(screen_name = at)
    return user.id_str



def get_video():
    api = create_api()
    t = api.get_status("1273306678264344577")
    #t = get_tweet_by_id("1273671234585112582", api)

    bitrate = 0
    vid_url = t.extended_entities['media'][0]["video_info"]["variants"][0]

    for i in range(0, len(t.extended_entities['media'][0]["video_info"]["variants"])):
        if (t.extended_entities['media'][0]["video_info"]["variants"][i]["content_type"] == "video/mp4"):
            if (t.extended_entities['media'][0]["video_info"]["variants"][i]["bitrate"] > bitrate):
                bitrate = t.extended_entities['media'][0]["video_info"]["variants"][i]["bitrate"]
                print(bitrate)
                vid_url = t.extended_entities['media'][0]["video_info"]["variants"][i]

    dl_link = (vid_url['url'])
    file_write = 'files/vid.mp4'
    print("downloading file...")
    dict_responce = requests.get(
        dl_link, allow_redirects=True)  # get dict file
    print("writing %s to file..." % file_write)
    open(file_write, 'wb').write(
        dict_responce.content)  # write contents of dict

def main(users):
    api = create_api()

    """
    id_list = list()
    for u in users:
        id_list.append(get_id_from_at(u,api))
    print(id_list)
    
    tweet_listener = YetziFaver(api)
    stream = tw.Stream(api.auth, tweet_listener)
    stream.filter(follow=id_list)
    """

if __name__ == "__main__":
    get_video()
    #main(["178344886"])
    #main(["georgeclose","dril","YtzCrts"])

