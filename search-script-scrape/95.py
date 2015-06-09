# Since 2002, the most commonly occurring winning number in New York's Lottery Mega Millions

import requests
import csv
url = "https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD"
txt = requests.get(url).text
# save the file temporarily
f = open("/tmp/lottery.csv", "w")
f.write(txt)
f.close()
###
# reopen (yes, this is wasteful, but whatever)
f = open("/tmp/lottery.csv", "r")
rows = list(csv.DictReader(f))

countthis = []
for r in rows:
	a = r['Winning Numbers']
	countthis.append(a)

from collections import Counter
count = Counter(countthis)
count.most_common()