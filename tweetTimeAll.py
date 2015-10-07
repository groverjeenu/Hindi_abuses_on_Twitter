
allList = open("result/resultHindi.txt")
allDict = dict()
for i in allList:
	allDict[i.split('\t')[11]] =  i
print len(allDict)
print allDict['566922845565886464']
print allDict['566922845565886464'].split('\t')[14]

hours = dict()
days = dict()


abuseData = open("hindiAbuseAllTime.txt","w")
for i in allDict.keys():
	t =allDict[i].split('\t')[14]
	if t[0:3] in days.keys():
		days[t[0:3]] = days[t[0:3]]+1
	else:
		days[t[0:3]]=1


	d= int(t[11:13]+t[14:16]+t[17:19])
	d= d+53000
	d = d%240000
	d= '%0*d' % (6,d)
	if str(d)[0:2] in hours.keys():
		hours[str(d)[0:2]]= hours[str(d)[0:2]]+1
	else:
		hours[str(d)[0:2]] = 1


	abuseData.write(i+'\t'+t+'\n')
	
		
count1 = 0
dayData = open("hindiAbuseAllDays.txt","w")
for i in sorted(days.keys()):
	dayData.write(i+'\t'+str(days[i])+'\n')
	count1 = count1 + days[i]
print count1
count1=0
hourData = open("hindiAbuseAllHours.txt","w")
for i in sorted(hours.keys()):
	hourData.write(i+'\t'+str(hours[i])+'\n')
	count1 = count1 + hours[i]
print count1