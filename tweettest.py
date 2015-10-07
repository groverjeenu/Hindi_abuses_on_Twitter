from __future__ import print_function
import urllib2
proxy = urllib2.ProxyHandler({'http': '10.3.100.207:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
import tweepy
import codecs
import os
import bitly_api
import time
 
authorizationConstants = {
	"apiKey" : ""##give ur api key,
	"apiSecret" : ""##give ur api secret,
	"accessToken" : ""##your access token, you may require it for jst crawling,
	"accessSecret" : ""##your access token , youmay not require it fr jst crwling
}

# Define your API information

BITLYAPI_USER = "asalways"
BITLYAPI_KEY = "R_ff26640a9a5a42da887c92a9a6c96c94"
SLEEPTIME = 180

b = bitly_api.Connection(BITLYAPI_USER,BITLYAPI_KEY)
screenNameIndex = 13

gmessage = "We're doing a project on twitter.Plz fill this form to mark your contribution.Will take only 1 min"

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
path = "/home/prabhat/Desktop/SocialComputingProject/"
#path = "/home/prabhat/Desktop"
#filename = raw_input()
#doForAFile(path,filename,api)
#print(getUniqueURL("Ashis"))
fileds = open(path+"india.txt","a")
def getTweets():
	api = authorize()
	tweets = tweepy.Cursor(api.search, q='india',lang='hi').items()
	for tweet in tweets:
		try:
			print (tweet,file=fileds)
		except:
			pass

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



getNamefromUserId()
