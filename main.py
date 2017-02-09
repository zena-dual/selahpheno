# coding: utf-8
# http://www.antun.net/tips/api/twitter.html

import WordProcesser
import twitter
import Data
import unicodedata

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

    for message in t_userstream.user():
        if "in_reply_to_screen_name" in message.keys() and \
           message["in_reply_to_screen_name"] == m_id:
            message_text = message["text"].split(" ")

            if is_japanese(message_text[1]):
                reply = "@" + message['user']['screen_name'] + " " + \
                        wp.returnSurface(message_text[1])
            elif message_text[1].isalpha():
                reply = "@" + message['user']['screen_name'] + " " + \
                        wp.returnMeaning(message_text[1])
                
            t.statuses.update(status=reply)
