import os.path
import itertools
variation = dict()


variation['a'] = "a!@#$%^&*"
variation['b']= "b!@#$%^&*36"
variation['c'] ="c!@#$%^&*"
variation['d'] ="d!!@#$%^&*"
variation['e']= "e!@#$%^&*"
variation['f']= "f!@#$%^&*"
variation['g']= "g!@#$%^&*9"
variation['h']= "h!@#$%^&*"
variation['i']= "i!@#$%^&*"
variation['j']= "j!@#$%^&*"
variation['k']= "k!@#$%^&*"
variation['l']= "l!@#$%^&*"
variation['m']= "m!@#$%^&*"
variation['n']= "n!@#$%^&*"
variation['o']= "o!@#$%^&*0"
variation['p']= "p!@#$%^&*"
variation['q']= "q!@#$%^&*"
variation['r']= "r!@#$%^&*"
variation['s']= "s!@#$%^&*5"
variation['t']= "t!@#$%^&*+"
variation['u']= "u!@#$%^&*"
variation['v']= "v!@#$%^&*"
variation['w']= "w!@#$%^&*"
variation['x']= "x!@#$%^&*"
variation['y']= "y!@#$%^&*"
variation['z']= "z!@#$%^&*"
variation['0']="0o"
variation['1']="1li"
variation['2']="2"
variation['3']="3"
variation['4']="4"
variation['5']="5s"
variation['6']="6"
variation['7']="7"
variation['8']="8"
variation['9']="9g"


vowel = {'a','e','i','o','u'}
variations = {}
variations['a'] = {'a','','ae','i','e','o','u','ea','!','@','#','$','%','^','&','*'}
variations['b']=  {'b','6','bh' ,'13','!','@','#','$','%','^','&','*'}
variations['c']={'c','','s','!','@','#','$','%','^','&','*'}
variations['d'] = {'d','dh','dh','da','da','di','de','th','!','@','#','$','%','^','&','*'}
variations['e'] = {'e','ae','a','i','o','u','','ea','!','@','#','$','%','^','&','*'}
variations['f'] = {'f','ph','!','@','#','$','%','^','&','*'}
variations['g'] ={'g','j','ga','','ji','je' ,'!','@','#','$','%','^','&','*'}
variations['h'] = {'h','ha','hai','he','han','hi','','!','@','#','$','%','^','&','*'}
variations['i'] = {'i','ii','e','ae','a','o','u','','ea','!','@','#','$','%','^','&','*'}
variations['j'] = {'j','ja','g','z','!','@','#','$','%','^','&','*'}
variations['k']= {'k','ka','ke','ki','ko','ku','ch','!','@','#','$','%','^','&','*'}
variations['l']= {'l','la','1','!','@','#','$','%','^','&','*'}
variations['m'] ={'m','ma','mai','me','am','','!','@','#','$','%','^','&','*','!','@','#','$','%','^','&','*'}
variations['n'] = {'n','na','ne','!','@','#','$','%','^','&','*'}
variations['o'] = {'o','oh','u','a','i','e','','oe','oi','oa','oy','!','@','#','$','%','^','&','*'}
variations['p'] = {'p','pi','pe','pea','pae','!','@','#','$','%','^','&','*'}
variations['q'] = {'q','qu','k','kyu','!','@','#','$','%','^','&','*'}
variations['r'] = {'r','re','ri','ra','ro','ru','d','rh','ar','rae','rea','!','@','#','$','%','^','&','*'}
variations['s']= {'s','c','sh','se','si','sa','so','su','','5','!','@','#','$','%','^','&','*'}
variations['t'] = {'t','th','the','ta','ti','te','tha','!','@','#','$','%','^','&','*'}
variations['u'] = {'u','o','e','a','i','yu','you','yo','','!','@','#','$','%','^','&','*'}
variations['v']={'v','we','vi','vhi','bhi','b','bi','be','vh','w','va','vaa','','!','@','#','$','%','^','&','*'}
variations['w'] ={'w','v','vh','','va','!','@','#','$','%','^','&','*'}
variations['x']={'x','aks','ex','ax','oks','','!','@','#','$','%','^','&','*'}
variations['y'] ={'y','vai','ya','ye','yi','yh','yeh','yo','yu','','j','jhe','je','!','@','#','$','%','^','&','*'}
variations['z'] = {'z','j','je','ji','az','s','y','!','@','#','$','%','^','&','*'}
variations[' ']={' ',''}
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


def check2(s1,s2):
    if ((s1 >= 'a' and s1<='z') or (s1>='0' and s2<='9')):
        if (variations[s1].issuperset({s2})):
            return True
    return False    

def check(s1,s2):
    if (variation[s1].find(s2) >= 0 ):
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
            if(check2(s1[i-1],s2[j-1])):
                cost = 1
            else :
                cost =2
            tbl[i,j] = min(tbl[i, j-1]+2, tbl[i-1, j]+2, tbl[i-1, j-1]+cost)
            if(i>=1 and j>=2):
                if(check2(s1[i-1],s2[j-2:j])):
                    cost = 1
                else :
                    cost =4
                tbl[i,j] = min(tbl[i, j-2]+4, tbl[i-1, j]+2,tbl[i-1,j-2]+cost,tbl[i,j])
            
            if(i>=2 and j>=1):
                if (check2(s2[j-1],s1[i-2:i])):
                    cost = 1
                else :
                    cost =4
                tbl[i,j] = min(tbl[i, j-1]+2, tbl[i-2, j]+4,tbl[i-2,j-1]+cost,tbl[i,j])
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



def do(filename,abuseFile):
    frequencies = open("faltu.txt","a")
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
                        

                        if((len(abuse)-count)>0):
                            val = reformed_edit_dist(abuse,word)
                            if(val !=0):
                                if(len(abuse)/val >1.55):
                                    frequencies.write(abuse+'\t'+word+'\t'+filename+'\t'+row)
                                    print abuse +" "+word #+ " count = "+str(count) +" "+str(len(abuse))
        tweets.close()
    frequencies.close()

#abuseFolder = open("abuseFolder")
#tweetFolder = open("tweetFolder")


def reformed_do(filename,abuseFile):
    tweets=open(filename)
    frequencies = open("faltu2.txt","a")
    noAbuse=open("noGaali.txt","a")
    for tweet in tweets:
        row = tweet
        tweet = tweet.split('\t')[2].split('\n')[0].lower()
        found = 0
        abuses = open(abuseFile)
        for abuse in abuses:

            abuse = abuse.split('\n')[0].lower()
            found_a = 0

            if (len(abuse.split(' '))>1 ):
                if( tweet.find(abuse)!= -1):
                    frequencies.write(abuse+'\t'+abuse+'\t'+filename+'\t'+row)
                    found = found +1
                    found_a = found_a +1
                    print abuse
            else :

                for word in tweet.split(' '):
                    found_a_w=0
                    word=word.strip(' \t\n\r,.!-_')

                    #direct match
                    if(word == abuse):
                        frequencies.write(abuse+'\t'+word+'\t'+filename+'\t'+row)
                        found = found +1
                        found_a = found_a +1
                        found_a_w = found_a_w +1
                        print word

                    #count masking chars
                    if(found_a_w==0):
                        count =0
                        i=0 
                        for i in range(0,len(word)):
                            if word[i]=='!' or word[i]=='@' or word[i]=='#' or word[i]=='$' or word[i]=='%' or word[i]=='^' or word[i]=='&' or word[i]=='*' :
                                count = count +1

                        #if non zero masking chars, then find masked edit dist
                        if((len(abuse)-count)>0 and count!=0):
                            val = edit_distance(abuse,word)
                            if(val ==0):
                                frequencies.write(abuse+'\t'+word+'\t'+filename+'\t'+row)
                                found = found +1
                                found_a = found_a +1
                                found_a_w = found_a_w +1
                                print abuse +" "+word #+ " count = "+str(count) +" "+str(len(abuse))



                    if(found_a_w==0):
                        if(count == 0):# if zero masks

                            temp_word = word[0].join([word[ik+1] for ik in range(0,len(word)-1) if word[ik+1]!= word[ik]])
                            temp_abuse = abuse[0].join([abuse[ik+1] for ik in range(0,len(abuse)-1) if abuse[ik+1]!= abuse[ik]])
                            #compare words without repeated chars
                            if(temp_abuse==temp_word):
                                frequencies.write(abuse+'\t'+word+'\t'+filename+'\t'+row)
                                found = found +1
                                found_a = found_a +1
                                found_a_w = found_a_w +1
                                print abuse +" "+word+" "+temp_word

                    if(found_a_w==0):
                        value = reformed_edit_dist(abuse,word)
                        if((value !=0 and len(abuse)/value > 1.5) or value == 0):
                            frequencies.write(abuse+'\t'+word+'\t'+filename+'\t'+row)
                            print abuse +" "+word+"  reformed"
        abuses.close()
        if(found == 0):
            noAbuse.write(row+'\n')
    frequencies.close()
    noAbuse.close()









abuseFiles = []
tweetFiles =[]
path = "/home/jg/Documents/socialComputing"
getFiles("abuseFolder/HindiSwears.txt",abuseFiles,path)
getFiles("tweetFolder/HI/indvspak_TOTAL_HI.txt",tweetFiles,path)

print abuseFiles
print tweetFiles

#do("aapsweep_TOTAL_CME.txt" ,"HindiSnwears.txt")
for i in abuseFiles:
    for j in tweetFiles:
        reformed_do(j,i)






