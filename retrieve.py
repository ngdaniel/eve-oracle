import requests
import grequests
from requests_throttler import BaseThrottler
import json

locations = {}


'''
regions = json.loads(requests.get('https://public-crest.eveonline.com/regions/').text)
#for region in regions['items']:
region = regions['items'][0]
constellations = json.loads(requests.get('https://public-crest.eveonline.com/regions/' + region['id_str'] + '/').text)
print(region['id_str'])
for constellation in constellations['constellations']:
    systems = json.loads(requests.get('https://public-crest.eveonline.com/constellations/' + constellation['id_str'] + '/').text)
    reqs += [requests.get(system['href']) for system in systems['systems']]

with BaseThrottler(name='base-throttler', reqs_over_time=(150, 60)) as bt:
    throttled_requests = bt.multi_submit(reqs)
    for r in throttled_requests:
        print r.response.text
'''

def write(response, **kwargs):
    print response.text
    obj = json.loads(response.text)
    locations[obj['name']] = obj['position']

with open('data.json') as data_file:    
    data = json.load(data_file)

keys = data.keys()

for x in xrange(21):
    reqs = []
    for y in xrange(400):
        if x*400+y < len(keys):
            reqs.append(grequests.get('https://public-crest.eveonline.com/solarsystems/' + keys[x*400+y] + '/', hooks={'response': write}))
    print len(reqs)
    print grequests.map(reqs)

with open('data1.json', 'w') as outfile:
    json.dump(locations, outfile)

