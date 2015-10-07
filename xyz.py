abuses = open("hindiSwears.txt")
output = open("HindiSwears.txt","w+")
List = []
Lists = [] 
for row in abuses:
	row = row.strip().lower()
	List.append(row)

Lists = list(set(List))
Lists.sort()
for i in Lists:
	output.write(i+'\n')
output.close()
