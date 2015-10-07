from __future__ import print_function
import json
import sys
import codecs
import urllib
import binascii
#import requests

def main():
   path = "delhidecides_1.txt"
   file = codecs.open(path,'r','utf-8')
   path1 = "DELHI.txt"
   i = 0
   with codecs.open(path1,'w','utf-8') as testfile:
      for row in file:
         i = i+1
         try:
            s = list(map(str,row.split('\t')))
            #print(s[2])
            s2 = s[2].split(' ')
            s2[0] = s2[0].encode('utf-8')

            s3 = binascii.b2a_qp(s2[0])
            s2[0] = s3.decode('utf-8')
            #print(s2[0])
            req = "http://api.namsor.com/onomastics/api/json/gender/"+s2[0]+"/"+s2[1]+"/in"
            ans = urllib.urlopen(req).read().decode("utf-8")
            d = json.loads(ans)
            gen = d['gender']
            scale = d['scale']
            s1 = list(map(str,row.split('\t')))
            if gen != None:
               print(s1[0],end = '\t',file=testfile)
               print(s1[1],end = '\t',file=testfile)
               print(s1[2],end = '\t\t',file=testfile)
               print(gen,'\t\t',file=testfile)
               print(scale,file=testfile)
            #print(i)
            #print(gen)
         except:
            pass
            #print(req)
         #print(s)
         #r = requests.get("https://api.genderize.io/?name=nidhi")
         #print(r.content)
      print(i)
if __name__ == "__main__":main()
    
