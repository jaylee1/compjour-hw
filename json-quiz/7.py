import requests
import json
durl = 'http://www.compjour.org/files/code/json-examples/earthquake.usgs-significant_month.json'
data = json.loads(requests.get(durl).text)
quakes = data['features']

#Task A
name = data['metadata']['title']
print("A.", name)

#Task B
print("B.", len(quakes))

#######################
# Task C
print("C.", max([q['properties']['mag'] for q in quakes]))

#Task D
x = 0
for d in quakes:
    if d['properties']['tsunami'] == 1:
        x += 1

print("D.", x)



#######################
# Task E
def get_mag(quake):
    return quake['properties']['mag']

q = min(quakes, key = get_mag)
print("E.", q['properties']['title'])

def felt(quake):
    return quake['properties']['felt']

q = max(quakes, key = felt)
print("F.", q['properties']['title'])



#######################
# Task G
import time
# the USGS time attribute is precise to the millisecond
# but we just need seconds:
qsecs = [q['properties']['time'] / 1000 for q in quakes]
# the feed was probably sorted in reverse chronological order, but
# just to make sure...
qsecs = sorted(qsecs, reverse = True)
tsec = qsecs[0] 
timeobj = time.gmtime(tsec)
print('G.', time.strftime('%Y-%m-%d %H:%M', timeobj))

#Task H

zsecs = [z['properties']['time'] / 1000 for z in quakes]
# the feed was probably sorted in reverse chronological order, but
# just to make sure...
zsecs = sorted(zsecs, reverse = True)
tsec = zsecs[5] 
timeobj = time.gmtime(tsec)
print('H.', time.strftime('%A, %B %d', timeobj))



#######################
# Task J
tobjs = [time.gmtime(s) for s in qsecs]
wdays = [s.tm_wday for s in tobjs]
x = [d for d in wdays if d in range(0, 6)]
print('I.', len(x))

#######################
#Task J
am = [s.tm_hour for s in tobjs]
x = [d for d in am if d in range(5, 9)]
print('J.', len(x))


#########################
# Task K
from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat /2 ) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers.
    return c * r

def distance_from_stanford(quake):
    stanford_lng = -122.166
    stanford_lat = 37.424
    coords = quake['geometry']['coordinates']
    lng = coords[0]
    lat = coords[1]
    return haversine(lng, lat, stanford_lng, stanford_lat)

q = max(quakes, key = distance_from_stanford)
print('K.', q['properties']['title'])

def distance_from_paris(quake):
    paris_lng = 2.3508
    paris_lat = 48.8567
    coords = quake['geometry']['coordinates']
    lng = coords[0]
    lat = coords[1]
    return haversine(lng, lat, paris_lng, paris_lat)

q = max(quakes, key = distance_from_paris)
print('L.', q['properties']['title'])


#########################
# Task M
basemap_url = 'https://maps.googleapis.com/maps/api/staticmap?zoom=1&size=500x400'
markers_str = 'markers=color:orange'
for q in quakes:
    coords = q['geometry']['coordinates']
    lng = str(coords[0])
    lat = str(coords[1])
    s = '%7C' + lat + ',' + lng
    markers_str += s

print('M.', basemap_url + '&' + markers_str)  

#Task N

orange = 'markers=color:orange'
red = 'markers=color:red'

for q in quakes:
    coords = q['geometry']['coordinates']
    lng = str(coords[0])
    lat = str(coords[1])
    s = '%7C' + lat + ',' + lng
    if q['properties']['mag'] >= 6:
        red += s
    else:
        orange += s

print('N.', basemap_url + '&' + orange + '&' + red)