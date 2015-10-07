from __future__ import print_function
import urllib2
import sys
proxy = urllib2.ProxyHandler({'http': '10.3.100.207:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
import tweepy
import codecs
import os
import bitly_api
import time
import json
 
'''authorizationConstants = {
	"apiKey" : "AiYoq6LcLJJFcXPaHYMpdG73S",##give ur api key,
	"apiSecret" : "DkxzxOu4amu2M8G0zYNADDoiccb9guEKH9XvPCKVXknV53JgDh",##give ur api secret,
	"accessToken" : "2466234678-mXejrabPZ8u2dpKzuOA8nvNWd2UuEznf4kBZP0w",
	"accessSecret" : "BkiWd5DHpN5zIQToZto4fXD5HMqWAywLdYkQcK2K9seig"
}'''
authorizationConstants = {}
authorizationConstants["apiKey"] = (sys.argv)[1]
authorizationConstants["apiSecret"] = (sys.argv)[2]
uthorizationConstants["accessToken"] = (sys.argv)[3]
uthorizationConstants["accessSecret"] = (sys.argv)[4]
# Define your API information

BITLYAPI_USER = "asalways"
BITLYAPI_KEY = "R_ff26640a9a5a42da887c92a9a6c96c94"
SLEEPTIME = 3600

b = bitly_api.Connection(BITLYAPI_USER,BITLYAPI_KEY)
screenNameIndex = 13

gmessage = "We're doing a project on twitter.Plz fill this form to mark your contribution.Will take only 1 min"

def getValue(d,key):
    if(key in d):
        if(key == "text"):
	    p = d[key].replace('\n',' ')
	    return p
	return d[key]
    return ""

def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()

def authorize():
	auth = tweepy.OAuthHandler(authorizationConstants["apiKey"], authorizationConstants["apiSecret"])
	auth.set_access_token(authorizationConstants["accessToken"], authorizationConstants["accessSecret"])
	api = tweepy.API(auth_handler=auth,proxy="https://10.3.100.207:8080")
	return api
 

def updatestatus(api,message):
	api.update_status(status=message)

def followUser(api,screenName):
	api.create_friendship(screenName)

def doForAFile(path,filename,api):
	print("processing file : "+filename)
	infile = codecs.open(path+"/"+filename,"r","utf-8")
	outfile = codecs.open(path+"/"+filename+"error.txt","w","utf-8")
	linecnt = 0
	infile = infile.readlines()
	print("line count with duplicates",len(infile))
	infile = list(set(infile))
	print("line count without duplicates",len(infile))
	for line in infile:		
		screenName = line[:-1]
		print(screenName)
		try:
			message = "@"+screenName+" "+gmessage+ " " + getUniqueURL(screenName)
			try: 
				linecnt = linecnt + 1
				print (linecnt)
				updatestatus(api,message)
				followUser(api,screenName)
			except Exception,e:
				print(line,file=outfile)
				print(e)
				time.sleep(SLEEPTIME)
		except Exception, e:
			print(line,file=outfile)
			print(e)
			time.sleep(SLEEPTIME)

	print("Line = "+str(linecnt)+" Completed file : "+filename)
	return

def doForAFolder(path,foldername,api):
	filelist = os.listdir(path+"/"+foldername)
	funclist =[]
	for sfile in filelist:
		funclist.append(doForAFile(path+"/"+foldername,sfile,api))
	return


def getUniqueURL(name):
	longurl = "https://docs.google.com/forms/d/1JQvY8iy8B_DO6gwVLX4IVyspjvEZ71wKc9kgghue7W4/viewform?entry.39850805="+name+"&entry.285275305"
	response = b.shorten(uri=longurl,preferred_domain = "j.mp")
	return response['url']


#path = "/home/prabhat/Desktop/compilers/SocialComputingProject"
#doForAFolder(path,"user_data",authorize())
#api = authorize()
#print(getUniqueURL("Ashs"))
#updatestatus(api,"@kgpyuvi "+gmessage)
#api.send_direct_message(screen_name="kgpyuvi",text="Ab ek baar unfollow kar")
#api = authorize()
path = "/home/du3/13CS30042/sc_jeenu/socialComputing/Topics/Politics/json/"
pathtwt = "/home/du3/13CS30042/sc_jeenu/socialComputing/Topics/Politics/Tweet_Data/processed/"
pathtwt_1 = "/home/du3/13CS30042/sc_jeenu/socialComputing/Topics/Politics/Tweet_Data/error/"
pathuser = "/home/du3/13CS30042/sc_jeenu/socialComputing/Topics/Politics/User_Data/processed/"
pathuser_1 = "/home/du3/13CS30042/sc_jeenu/socialComputing/Topics/Politics/User_Data/error/"
#path = "/home/prabhat/Desktop"
#filename = raw_input()
#doForAFile(path,filename,api)
#print(getUniqueURL("Ashis"))
file_name = (sys.argv)[5]
#print (file_name[0:-4])

fileds = codecs.open(path+file_name,"a","utf-8")
filetwt = codecs.open(pathtwt+file_name,"a","utf-8")
filetwt_1 = codecs.open(pathtwt_1+file_name,"a","utf-8")
fileuser = codecs.open(pathuser+file_name,"a","utf-8")
fileuser_1 = codecs.open(pathuser_1+file_name,"a","utf-8")

def getTweets():
	api = authorize()
	count = 0
	i = 0
	if(api.rate_limit_status() > 0):
		tweets = tweepy.Cursor(api.search, q=file_name[0:-4]).items()
		for tweet in tweets:
                    if(count<2500):
                        print(file_name,end = '\t')
                        print(i)
                        i = i+1
                        count = count + 1
                        json_str = json.dumps(tweet._json)
                        print (json_str,file=fileds)
                        json_str = json.loads(json_str)
                        l = json_str
                        datarow = [ getValue(l,"truncated"),getValue(l,"text"),l["user"]["id_str"] ,getValue(l,"in_reply_to_status_id"), getValue(l,"favorite_count"), getValue(l,"source"), getValue(l,"retweeted"), getValue(l,"coordinates"),  getValue(l,"in_reply_to_screen_name"), getValue(l,"in_reply_to_user_id"),  getValue(l,"retweet_count"), getValue(l,"id_str"), getValue(l,"in_reply_to_user_id_str"), getValue(l,"lang"), getValue(l,"created_at"),getValue(l,"in_reply_to_status_id_str"),getValue(l,"place") ]
                        try:
                            for data in datarow:
				print(data,end="\t",file=filetwt)
                            print("\n",file=filetwt)
                        except Exception ,e:
                            print ("Error : ",i)
                            print(json_str["id_str"],end="\n",file=filetwt_1)
                        
                            
                        l = json_str["user"]
                        datarow = [json_str["id_str"],getValue(l,"verified"),getValue(l,"created_at"),getValue(l,"favourites_count"),getValue(l,"followers_count"),getValue(l,"friends_count"),getValue(l,"id_str"),getValue(l,"lang"),getValue(l,"listed_count"),getValue(l,"statuses_count"),getValue(l,"description"),getValue(l,"location"),getValue(l,"name"),getValue(l,"screen_name"),getValue(l,"time_zone"),getValue(l,"url")]
		
                        try:
                            for data in datarow:
				print(data,end="\t",file=fileuser)
                            print("\n",file=fileuser)
                        except Exception ,e:
                            print ("Error : ",i)
                            print(l["id_str"],end="\n",file=fileuser_1)
                        
                    else:
                        print(file_name[0:-4])
                        print(i,end = ' ')
                        print(count)
          		time.sleep(SLEEPTIME)
                        count = 0			
	

def getUsersList():
	s = raw_input()
	sr = []
	while(s != "-1"):
		sr.append(s)
		s = raw_input()
	return sr
def getNamefromUserId():
	api = authorize()
	userIds = getUsersList()
	userIds = list(set(userIds))
	userIdname ={}
	ffile = open("somename.txt","w")
	for userid in userIds:
		try:
			user = api.get_user(userid)
			userIdname[userid] = user.name
			print (userid+"\t"+user.name,file=ffile)
		except:
			print (userid)
	
	# for userid in userIdname:
	# 	print (userid,"\t",userIdname[userid],file=ffile)


getTweets()
