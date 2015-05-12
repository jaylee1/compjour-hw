import json
with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

def myfoo(thing):
    name = thing[1]
    return name

sorted_data = sorted(intl_data, key = myfoo, reverse = True)


for d in sorted_data:
	if d[1] > 10:
		print(d)