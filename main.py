# coding: utf-8
# http://www.antun.net/tips/api/twitter.html

import WordClass
import codecs
import subprocess as sp
import twitter
import Data

if __name__ == "__main__":
    words_list = []

    lines = sp.check_output(["nkf","-w","dic-ongo.txt"]).decode("utf-8")
    lines = lines.replace("\r","").split("\n")

    for line in lines:
        if line == "" or line == "\n":
            continue
        words_list.append(WordClass.Word(line))

    d = Data.Data()
    m_id = d.getMyId()
    auth = twitter.OAuth(consumer_key=d.getConsumerKey(),
                         consumer_secret=d.getConsumerSecret(),
                         token=d.getAccessTokenKey(),
                         token_secret=d.getAccessTokenSecret())

    t = twitter.Twitter(auth=auth)
    t_userstream = twitter.TwitterStream(auth=auth,
                                         domain='userstream.twitter.com')

    for msg in t_userstream.user():
        print(type(msg))
        if "in_reply_to_screen_name" in msg.keys():
            if msg["in_reply_to_screen_name"] == __my_twitter_id:
                reply = "@" + msg['user']['screen_name'] + " " + \
                        "リプライに†感謝†"
                t.statuses.update(status=reply)
