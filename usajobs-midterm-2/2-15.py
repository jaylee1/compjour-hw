import json
import requests
import os
from datetime import datetime
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
	for loc in val:
		if 'California' in loc:
			x.append[loc]
	return float(x)

loc = []
for job in jobs:
	loc.append(job['Locations'])

cal = []
