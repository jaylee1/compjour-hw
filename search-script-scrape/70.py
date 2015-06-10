import requests
import json 
response = requests.get('https://open.whitehouse.gov/api/views/i9g8-9web/rows.json?accessType=DOWNLOAD')
data = response.json()
print(data['meta']['view']['columns'][10]['cachedContents']['largest'])