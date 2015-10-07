t = int(raw_input())
dic = {}

while(t ):
	n = int(raw_input())
	count =0
	for i in range(1,n*n+1):
		if(i%n == 1):
			val = [int(j) for j in str(raw_input()).split()]
		#print val
		dic[val[(i%n -1 ,n-1)[i%n == 0]]]= [(i/n+1,i/n)[i%n==0],(n,i%n)[i%n!=0]]
		#print dic[val[(i%n -1 ,n-1)[i%n == 0]]]
	#print dic
	for i in range(1,n*n):
		#print i
		count  = count + abs(dic[i+1][0]-dic[i][0]) + abs(dic[i+1][1]- dic[i][1])
	print count

	t = t-1	
N