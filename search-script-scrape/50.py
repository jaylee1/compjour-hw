# In the most recently transcribed Supreme Court argument, the number of times laughter broke out
import requests
import csv
url = "http://www.supremecourt.gov/oral_arguments/argument_transcripts/14-185_6kg7.pdf"
txt = requests.get(url).text

newtxt = txt.split(" ")

totes = 0

for w in newtxt:
	if w == '(Laughter.)':
		totes += 1