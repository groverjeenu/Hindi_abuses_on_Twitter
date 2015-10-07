import os.path
variations = dict()

'''
variations['a'] = "a!@#$%^&*"
variations['b']= "b!@#$%^&*36"
variations['c'] ="c!@#$%^&*"
variations['d'] ="d!!@#$%^&*"
variations['e']= "e!@#$%^&*"
variations['f']= "f!@#$%^&*"
variations['g']= "g!@#$%^&*9"
variations['h']= "h!@#$%^&*"
variations['i']= "i!@#$%^&*"
variations['j']= "j!@#$%^&*"
variations['k']= "k!@#$%^&*"
variations['l']= "l!@#$%^&*"
variations['m']= "m!@#$%^&*"
variations['n']= "n!@#$%^&*"
variations['o']= "o!@#$%^&*0"
variations['p']= "p!@#$%^&*"
variations['q']= "q!@#$%^&*"
variations['r']= "r!@#$%^&*"
variations['s']= "s!@#$%^&*5"
variations['t']= "t!@#$%^&*+"
variations['u']= "u!@#$%^&*"
variations['v']= "v!@#$%^&*"
variations['w']= "w!@#$%^&*"
variations['x']= "x!@#$%^&*"
variations['y']= "y!@#$%^&*"
variations['z']= "z!@#$%^&*"
variations['0']="0o"
variations['1']="1li"
variations['2']="2"
variations['3']="3"
variations['4']="4"
variations['5']="5s"
variations['6']="6"
variations['7']="7"
variations['8']="8"
variations['9']="9g"'''






def check(s1,s2):
    if (variations[s1].find(s2) >= 0 ):
        return True
    return False    


def edit_distance(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            if(check(s1[i-1],s2[j-1])):
                cost = 0
            else :
                cost =1 
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]



def getFiles(folder,List,path):
    ppath = path+"/"+folder
    if os.path.isdir(ppath):
        for files in os.listdir(ppath):
            getFiles(files,List,ppath)
    else:
        List.append(ppath)        



def do(filename,abuseFile):
    frequencies = open("EnglishFrequencies.txt","a")
    dataFile = open(filename)
    abuses = open(abuseFile)
    for abuse in abuses:
        abuse = abuse.split('\n')[0].lower()
        tweets = open(filename)
        for row in tweets:
            tweet = row.split('\t')[2].split('\n')[0].lower()
            #print tweet
            if (len(abuse.split(' '))>1 and tweet.find(abuse)!= -1):
                frequencies.write(abuse+'\t'+abuse+'\t'+filename+'\t'+row)
                print abuse
            else :
                for word in tweet.split(' '):
                    if(len(abuse.split(' '))==1):
                        count =0
                        i=0 
                        for i in range(0,len(word)):
                            if word[i]=='!' or word[i]=='@' or word[i]=='#' or word[i]=='$' or word[i]=='%' or word[i]=='^' or word[i]=='&' or word[i]=='*' :
                                count = count +1
                        if(count == 0):
                            if(word == abuse):
                                frequencies.write(abuse+'\t'+word+'\t'+filename+'\t'+row)
                                print word
                        

                        if((len(abuse)-count)>0 and count!=0):
                            val = edit_distance(abuse,word)
                            if(val ==0):
                                frequencies.write(abuse+'\t'+word+'\t'+filename+'\t'+row)
                                print abuse +" "+word #+ " count = "+str(count) +" "+str(len(abuse))
        tweets.close()
    frequencies.close()

#abuseFolder = open("abuseFolder")
#tweetFolder = open("tweetFolder")

abuseFiles = []
tweetFiles =[]
path = "/home/jg/Documents/socialComputing"
getFiles("abuseFolder/EnglishSwears.txt",abuseFiles,path)
getFiles("tweetFolder/EN",tweetFiles,path)

print abuseFiles
print tweetFiles

#do("aapsweep_TOTAL_CME.txt" ,"HindiSwears.txt")
for i in abuseFiles:
    for j in tweetFiles:
        do(j,i)






