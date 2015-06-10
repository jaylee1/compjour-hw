# The California city whose city manager earns the most total wage per population of its city in 2012

import requests
import csv
url = "http://transparentcalifornia.com/export/2012-cities.csv"
txt = requests.get(url).text
# save the file temporarily
f = open("/tmp/cities2012.csv", "w")
f.write(txt)
f.close()
###
# reopen (yes, this is wasteful, but whatever)
f = open("/tmp/cities2012.csv", "r")
rows = list(csv.DictReader(f))
winnercity = rows[1]['Agency']
winnermoney = rows[1]['Total Pay & Benefits']
for r in rows:
	if r['Job Title'] == 'City Manager':
		challenger = r['Total Pay & Benefits']
		if challenger >= winnermoney:
			winnercity = r['Agency']

print(winnercity)