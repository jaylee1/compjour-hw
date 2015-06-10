
from lxml import html




import request


response = requests ('http://www.regulations.gov/')


link = doc.csselect('.cellright') [6]


print(link.text)
