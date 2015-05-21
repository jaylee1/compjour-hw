import json
import requests
import os
from datetime import datetime
from operator import itemgetter
CA_FILE = 'data-hold/california.json'
if not os.path.exists(CA_FILE):
    print("Can't find", CA_FILE, "so fetching remote copy")
    resp = requests.get("http://stash.compjour.org/data/usajobs/california-all.json")
    f = open(CA_FILE, 'w')
    f.write(resp.text)
    f.close()
rawdata = open(CA_FILE).read()
jdata = json.loads(rawdata)
jobs = jdata['jobs']




def get_ca_cities(val):
	x = []
	for a in val:
		zzz = a.split(';')
	for z in zzz:
		if 'California' in z:
			x.append(z)
	return float(x)


t = []
for job in jobs:
	t.append(job['Locations'])

cal = []
for y in t:
	z = y.split(';')
	for a in z:
		if 'California' in a:
			p = a.split(',')
			cal.append(p[0])

dic = {}
for city in cal:
	if city in dic:
		dic[city] += 1
	else:
		dic[city] = 1

vdata = dic.items()

sorteddata = sorted(vdata, key = itemgetter(1), reverse = True)

cdata = []
cdata = [['City', 'Jobs']]

for b in sorteddata:
	cdata.append(b)


with open("sample.html") as f:
    htmlstr = f.read()
tablerows = []
for d in cdata:
    tablerows.append("<tr><td>%s</td><td>%s</td></tr>" % (d[0], d[1]))

tablerows = "\n".join(tablerows)
#
with open("2-15.html", "w") as f:
    htmlstr = htmlstr.replace('#CHART_DATA#', str(cdata))
    htmlstr = htmlstr.replace('#TABLE_ROWS#', tablerows)
    f.write(htmlstr)