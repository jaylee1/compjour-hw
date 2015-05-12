import json
with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

mylist = []

def myfoo(thing):
    name = thing[1]
    return name

sorted_data = sorted(intl_data, key = myfoo, reverse = True)

for num in range(0,9):
	mylist.append(sorted_data[num])

others = 0

for d in range(10, len(sorted_data)):
	others += sorted_data[d][1]
mylist.append(["Others", others])
print(mylist)