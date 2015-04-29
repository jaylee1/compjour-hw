import requests
import json
import os
data_url = 'http://www.compjour.org/files/code/json-examples/twitter-cspan-congress-list.json'
tempfilename = os.path.expandvars('%TEMP%\\congresslist.json')

if os.path.exists(tempfilename):
    tfile = open(tempfilename, "r")
    j = tfile.read()
else:    
    j = requests.get(data_url).text
    tfile = open(tempfilename, "w")
    tfile.write(j)

tfile.close()
accounts = json.loads(j)

print("A.", len(accounts))

x = 0
for a in accounts:
    if a['followers_count'] > 10000:
        x += 1

print("B.", x)

#############
## Task D:
counts = []
for a in accounts:
    counts.append(a['followers_count'])
maxval = sorted(counts, reverse = True)[0]
# alternatively:
# maxval = sorted([a['followers_count'] for a in accounts], reverse = True)[0]

## or:
# counts = []
# for a in accounts:
#    counts.append(a['followers_count'])
# maxval = max(counts)

## or:
# maxval = max(a['followers_count'] for a in accounts)
print("D.", maxval)

counting = []
for z in accounts:
    counting.append(z['statuses_count'])
mval = sorted(counting, reverse = True)[0]
# alternatively:
# maxval = sorted([a['followers_count'] for a in accounts], reverse = True)[0]

## or:
# counts = []
# for a in accounts:
#    counts.append(a['followers_count'])
# maxval = max(counts)

## or:
# maxval = max(a['followers_count'] for a in accounts)
print("E.", mval)



##############
## Task F:
from operator import itemgetter
y = sorted(accounts, key = itemgetter('followers_count'), reverse = True)
x = y[0]
# alternatively:
# x = max(accounts, key = itemgetter('followers_count'))
print("F.", x['screen_name'], 'has', x['followers_count'], 'followers')

# Task G:
# test = []
# for w in account:
# 	test.append(w)
# y = sorted(test, key = itemgetter('followers_count'), reverse = True)
# x = y[0]
# alternatively:
# # x = max(accounts, key = itemgetter('followers_count'))
# print("F.", x['screen_name'], 'has', x['followers_count'], 'followers')



###############
## Task H:
totes = 0
for a in accounts:
    totes += a['followers_count']

# alternatively
# totes = sum([a['followers_count'] for a in accounts])
print('H.', round(totes / len(accounts)))

# Task i
from operator import itemgetter
y = sorted(accounts, key = itemgetter('statuses_count'), reverse = True)
x = y[571/2]
print('I.', x['statuses_count'])