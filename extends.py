dataFile = open("hindiAbuses.txt")
resultFile = open("hindiAbusesExtended.txt","a")

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
variations['j'] = {'j','ja','g','z'}
variations['k']= {'k','ka','ke','ki','ko','ku','ch'}
variations['l']= {'l','la','1'}
variations['m'] ={'m','ma','mai','me','am',''}
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



def genVariations(word, f,n,var):
	if(n==0 and len(var)>3):
		f.write(var+"\n")
	if (n!=0):
		for i in variations[''+word[len(word)-n]]:
			genVariations(word,f,n-1,var+i)

	





for row in dataFile:
	row = row.split("\n")[0]
	if (len(row.split())==1):
		if (len(row)>3):
			genVariations(row.lower(),resultFile,len(row),"")