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

vowel = {'a','e','i','o','u'}

variations = {}
variations['a'] = {'a','','ae','i','e','o','u','ea'}
variations['b']=  {'b','6','bh' ,'13'}
variations['c']={'c','','s'}
variations['d'] = {'d','dh','dh','da','da','di','de','th'}
variations['e'] = {'e','ae','a','i','o','u','','ea'}
variations['f'] = {'f','ph'}
variations['g'] ={'g','j','ga','','ji','je' }
variations['h'] = {'h','ha','hai','he','han','hi',''}
variations['i'] = {'i','ii','e','ae','a','o','u','','ea'}
variations['j'] = {'j','ja','g'}
variations['k']= {'k','ka','ke','ki','ko','ku','ch'}
variations['l']= {'l','la','1'}
variations['m'] ={'m','ma','me','am',''}
variations['n'] = {'n','na','ne'}
variations['o'] = {'o','oh','u','a','i','e','','oe','oi','oa','oy'}
variations['p'] = {'p','pi','pe','pea','pae'}
variations['q'] = {'q','qu','k','kyu'}
variations['r'] = {'r','re','ri','ra','ro','ru','d','rh','ar','rae','rea'}
variations['s']= {'s','c','sh','se','si','sa','so','su','','5'}
variations['t'] = {'t','th','the','ta','ti','te','tha'}
variations['u'] = {'u','o','e','a','i','yu','you','yo',''}
variations['v']={'v','we','vi','vhi','bhi','b','bi','be','vh','w','va','vaa',''}
variations['w'] ={'w','v','vh','','va'}
variations['x']={'x','aks','ex','ax','oks',''}
variations['y'] ={'y','vai','ya','ye','yi','yh','yeh','yo','yu','','j','jhe','je'}
variations['z'] = {'z','j','je','ji','az','s','y'}
variations[' ']={' ','  ','   ','    ','     ',''}
variations['0']={'0','o'}
variations['1']={'1','i','l'}
variations['2']={'2'}
variations['3']={'3'}
variations['4']={'4'}
variations['5']={'5','s'}
variations['6']={'6'}
variations['7']={'7'}
variations['8']={'8'}
variations['9']={'9'}


def check(s1,s2):
    if (variations[s1].issuperset({s2}) ):
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


def reformed_edit_dist(s1,s2):
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
            if(i>=1 and j>=2):
                if(check(s1[i-1],s2[j-2:j])):
                    cost = 0
                else :
                    cost =2 
                tbl[i,j] = min(tbl[i, j-2]+2, tbl[i-1, j]+1,tbl[i-1,j-2]+cost,tbl[i,j])
            
            if(i>=2 and j>=1):
                if (check(s2[j-1],s1[i-2:i])):
                    cost = 0
                else :
                    cost =2
                tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-2, j]+2,tbl[i-2,j-1]+cost,tbl[i,j])
            if(vowel.issuperset({s1[i-1]})):
                tbl[i,j] = min (tbl[i-1,j],tbl[i,j])
            if(vowel.issuperset({s2[j-1]})):
                tbl[i,j] = min(tbl[i,j-1],tbl[i,j])
            


    return tbl[i,j]





def getFiles(folder,List,path):
    ppath = path+"/"+folder
    if os.path.isdir(ppath):
        for files in os.listdir(ppath):
            getFiles(files,List,ppath)
    else:
        List.append(ppath) 

print reformed_edit_dist('gada','gadh')      

'''

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
'''





