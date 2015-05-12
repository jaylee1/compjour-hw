import json
with open("data-hold/domestic-jobcount.json") as f:
    domestic_data = json.loads(f.read())

# using standard for loop
sorted_data = sorted(domestic_data)
for d in sorted_data:
	if d[1] < 100:
		print(d)