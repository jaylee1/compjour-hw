import requests

dic = {}
a=['California', 'Florida', 'New York', 'Maryland']
for state_name in a:
	BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
	atts = {"CountrySubdivision": state_name, 'NumberOfJobs': 1}
	resp = requests.get(BASE_USAJOBS_URL, params = atts)
	data = resp.json()
	dic[state_name] = data['TotalJobs']
	print("%s has %s job listings." % (state_name, data['TotalJobs']))
print(dic)