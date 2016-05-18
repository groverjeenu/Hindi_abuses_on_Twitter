#from __future__ import absolute_import, print_function

import tweepy
import codecs
import os
import time
import json
from requests.packages.urllib3.contrib import pyopenssl
pyopenssl.inject_into_urllib3()


authorizationConstants = {
	"apiKey" : ##give ur api key,
	"apiSecret" : ##give ur api secret,
	"accessToken" : ##,
	"accessSecret" : ##
}

def authorize():
	auth = tweepy.OAuthHandler(authorizationConstants["apiKey"], authorizationConstants["apiSecret"])
	auth.set_access_token(authorizationConstants["accessToken"], authorizationConstants["accessSecret"])
	api = tweepy.API(auth_handler=auth,proxy="https://10.3.100.207:8080")
	return api

api = authorize()
#
#api.update_status(status="i love jeenu")
trends1 = api.trends_place(23424848)
data = trends1[0] 
# grab the trends
trends = data['trends']
# grab the name from each trend
names = [trend['name'] for trend in trends]
# put all the names together with a ' ' separating them
print names
trendsName = ' '.join(names).encode("utf-8").strip()
print(trendsName)
#user = api.get_user("twitter")
print(api.me().name)
#print trends1
