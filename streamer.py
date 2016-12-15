import requests, json
import settings # Contains the keys required
from requests_oauthlib import OAuth1
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

consumer_key = settings.consumer_key
consumer_secret = settings.consumer_secret
USER_OAUTH_TOKEN = settings.USER_OAUTH_TOKEN
USER_OAUTH_TOKEN_SECRET = settings.USER_OAUTH_TOKEN_SECRET

streamurl = 'https://stream.twitter.com/1.1/statuses/sample.json'
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(consumer_key, consumer_secret, USER_OAUTH_TOKEN, USER_OAUTH_TOKEN_SECRET)

r = requests.get(streamurl, auth=auth, stream=True)

def streamstart():
    print "starting stream 1"
    for line in r.iter_lines(chunk_size=1, decode_unicode=True):

        if line:
            f = open('stream', 'a')
            outstream = json.loads(line)
            if outstream.has_key('text'):
                t = outstream['text']
                f.write(t + '\n')
            # f.write(outstream['text'] + '\n')
        #     if outstream.has_key('text'):
        #         txt = outstream['text'].lower()
        #     #     # this will check the tweet body for the text "trump" after converting it
        #     #     # to lower and print it to the console if it exists
        #         if "trump" in txt:
        #             f.write(txt + '\n')
                    # print outstream['text']
            # checkoutput()


def checkoutput():

    if outstream.has_key('text'):
        # this will give me a constant stream of the text object
        txt = outstream['text'].lower()
        print(txt)
        # print "%s" % (data['text'])
        # this will check the tweet body for the text "trump" after converting it
        # to lower and print it to the console if it exists
        if "#" in txt:
            print (outstream['text'])
