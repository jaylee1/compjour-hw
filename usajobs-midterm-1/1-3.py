import requests

tot = 0
a=['China', 'South Africa', 'Tajikistan']
for country in a:
	BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
	atts = {"Country": country, 'NumberOfJobs': 1}
	resp = requests.get(BASE_USAJOBS_URL, params = atts)
	data = resp.json()
	print("%s has %s job listings." % (country, data['TotalJobs']))
	tot += int(data['TotalJobs'])
print("Together, they have ", tot, " total job listings.")