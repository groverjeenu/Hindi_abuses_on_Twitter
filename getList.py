import csv
dataFile = open ("Survey Form (Responses) - Form Responses 1.csv")
reader = csv.reader(dataFile, delimiter =',')
dataList = []
for row in reader:
	for i in range (4,5):
		for content in row[i].replace(";",",").replace("\n",",").split(","):
			dataList.append(content.lower().strip())
dataList =  list(set(dataList))
dataList.sort()

resultFile = open("englishAbuses.txt","w+")
for word in dataList:
	resultFile.write(word +'\n')
print dataList		