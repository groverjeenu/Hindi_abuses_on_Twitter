
filename  = "aapsweep_TOTAL_CME.txt"
abuseFile = "hindiAbuses.txt"
dataFile = open(filename)
frequency = open("frequency.txt","w+")
myStats = {}

variations = dict()
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


for row in dataFile :
    parts = row.split('\t')
    tweet = parts[2].lower()
    tweet = tweet.split('\n')[0]
    #print tweet
    abuses = open(abuseFile)
    for abuse in abuses:
        s = abuse.split('\n')[0]
        if (tweet.find(s) != -1):
            #print 
            count =0
    abuses.close()

    
    words = tweet.split(' ')

    for word in words:
        abuses = open(abuseFile)
        for abuse in abuses:
            abuse  = abuse.split('\n')[0]
            if(len(abuse.split(' '))==1):
                count =0
                i=0 
                for i in range(0,len(word)):
                    if word[i]=='!' or word[i]=='@' or word[i]=='#' or word[i]=='$' or word[i]=='%' or word[i]=='^' or word[i]=='&' or word[i]=='*':
                        count = count +1
                if((len(abuse)-count)>0):
                    val = edit_distance(abuse,word)
                    if(val <2 and len(abuse)>5):
                        print abuse +" "+word #+ " count = "+str(count) +" "+str(len(abuse))
        abuses.close()



    



    



