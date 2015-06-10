
from lxml import html




import requests


justices = {'A':'Samuel Alito', 'AS': 'Antonin Scalia', 'B':'Stephen Breyer', 'D': 'Decree', 'EK': 'Elena Kagan', 'G': 'Ruth Bader Ginsburg', 'K': 'Anthony Kennedy', 'PC': 'Per Curiam', 'R': 'John Roberts', 'SS': 'Sonia Sotomayor', 'T': 'Clarence Thomas'}


response = requests.get('http://www.supremecourt.gov/opinions/slipopinions.aspx')


doc = html.fromstring(response.text)


link = doc.cssselect('center td')[4]


print(justices[link.text])
