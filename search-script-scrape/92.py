# The total amount paid by Rep. Aaron Schock to Lobair LLC, according to Congressional spending records in 2012-Q4, as compiled by the Sunlight Foundation

import requests
import csv
url = "http://assets.sunlightfoundation.com.s3.amazonaws.com/expenditures/house/2012Q4-detail.csv"
txt = requests.get(url).text
# save the file temporarily
f = open("/tmp/expenditures.csv", "w")
f.write(txt)
f.close()
###
# reopen (yes, this is wasteful, but whatever)
f = open("/tmp/expenditures.csv", "r")
rows = list(csv.DictReader(f))

totes = 0

for r in rows:
	if r['Office'] == 'Aaron Shock':
		if r['Payee'] == Lobair LLC:
			totes += xxx

print(totes)