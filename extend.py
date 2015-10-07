dataFile = open("hindiAbuses.txt")
resultFile = open("hindiAbusesExtended.txt","a")

variations = {}
variations['a'] = {'a','aa','aaa','','ae','i','e','o','u','ea'}
variations['b']=  {'b','bb','bbb','6','bh','bhh' ,'13'}
variations['c']={'c','cc','ccc','','s'}
variations['d'] = {'d','dd','ddd','dh','dhh','da','daa','di','de','th'}
variations['e'] = {'e','ee','eee','ae','a','i','o','u','','ea'}
variations['f'] = {'f','ff','fff','ph','phh'}
variations['g'] ={'g','j','ga','','gg','ggg','ji','jee' }
variations['h'] = {'h','ha','hai','he','han','haan','hi','hh','hhh',''}
variations['i'] = {'i','ii','e','ee','ae','a','o','u','iii','','ea'}
variations['j'] = {'j','jj','jjj','ja','g'}
variations['k']= {'k','kk','kkk','ka','ke','ki','ko','ku','ch'}
variations['l']= {'l','ll','lll','la','1'}
variations['m'] ={'m','ma','mai','me','mm','mmm','am',''}
variations['n'] = {'n','nn','nnn','na','ne'}
variations['o'] = {'o','oo','ooo','oooo','oh','ohh','u','a','i','e','','oe','oi','oa','oy'}
variations['p'] = {'p','pp','ppp','pi','pee','pe','pea','pae'}
variations['q'] = {'q','qq','qqq','qu','k','kyu'}
variations['r'] = {'r','rr','rrr','re','ri','ra','ro','ru','d','rh','ar','rae','rea'}
variations['s']= {'s','ss','sss','c','sh','shh','ssh','se','si','sa','so','su','','5'}
variations['t'] = {'t','tt','ttt','th','the','ta','ti','te','tha'}
variations['u'] = {'u','uu','uuu','o','e','a','i','yu','you','yoo','yo',''}
variations['v']={'v','we','vi','vhi','vv','vvv','bhi','b','bi','be','vh','w','va','vaa',''}
variations['w'] ={'w','ww','www','v','vh','','va',''}
variations['x']={'x','xx','xxx','aks','ex','ax','oks',''}
variations['y'] ={'y','yy','yyy','vai','ya','ye','yi','yh','yeh','yo','yu','','j','jhe','je'}
variations['z'] = {'z','zz','zzz','j','je','ji','az','s','y'}
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



def genVariations(word, f,n,var):
	if(n==0 and len(var)>3):
		f.write(var+"\n")
	if (n!=0):
		for i in variations[''+word[len(word)-n]]:
			genVariations(word,f,n-1,var+i)

	





for row in dataFile:
	row = row.split("\n")[0]
	if ( True):
		if (len(row)>3):
			genVariations(row.lower(),resultFile,len(row),"")