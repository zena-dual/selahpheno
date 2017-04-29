# coding: utf-8
# http://www.antun.net/tips/api/twitter.html

import WordProcesser
import twitter
import Data
import unicodedata
from datetime import datetime

def is_japanese(string):
    for ch in string:
        name = unicodedata.name(ch) 
        if "CJK UNIFIED" in name \
        or "HIRAGANA" in name \
        or "KATAKANA" in name:
            return True
    return False

if __name__ == "__main__":
    wp = WordProcesser.WordProcesser()

    d = Data.Data()
    m_id = d.getMyId()
    auth = twitter.OAuth(consumer_key=d.getConsumerKey(),
                         consumer_secret=d.getConsumerSecret(),
                         token=d.getAccessTokenKey(),
                         token_secret=d.getAccessTokenSecret())

    t = twitter.Twitter(auth=auth)
    t_userstream = twitter.TwitterStream(auth=auth,
                                         domain='userstream.twitter.com')

    now = datetime.now()
    start_message = "ミクヴァの緋眼が起動されました．(" + \
                    str(now.year) + "/" + \
                    str(now.month) + "/" + \
                    str(now.day) + "/" + \
                    str(now.hour) + ":" + str(now.minute) + ")"
    t.statuses.update(status=start_message)

    for message in t_userstream.user():
        if "in_reply_to_screen_name" in message.keys() and \
           message["in_reply_to_screen_name"] == m_id:
            message_text = message["text"].split(" ")

            if message_text[0] == "@"+m_id:
                if len(message_text) > 2 and \
                   message_text[1] == "類義語":
                    if is_japanese(message_text[2]):
                        if wp.hasSurface(message_text[2]):
                            reply = "@" + message['user']['screen_name'] + " " + \
                                    wp.getSurface(message_text[2])
                        else:
                            reply = "@" + message['user']['screen_name'] + " " + \
                                    wp.getSynonymSurface(message_text[2])
                    elif message_text[2].isalpha():
                        reply = "@" + message['user']['screen_name'] + " " + \
                                wp.getSynonymMeaning(message_text[2])
                else:
                    if is_japanese(message_text[1]):
                        reply = "@" + message['user']['screen_name'] + " " + \
                                wp.getSurface(message_text[1])
                    elif message_text[1].isalpha():
                        reply = "@" + message['user']['screen_name'] + " " + \
                                wp.getMeaning(message_text[1])
                
                t.statuses.update(status=reply)
