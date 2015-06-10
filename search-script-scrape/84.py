
from lxml import html




import requests


response = requests.get('https://www.federalregister.gov/')


doc = html.fromstring(response.text)


link = doc.cssselect('div#current_issue span')[0]


print(link.text)

