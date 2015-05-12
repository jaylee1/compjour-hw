import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
resp = requests.get(BASE_USAJOBS_URL, params = {"CountrySubdivision": 'California', 'NumberOfJobs': 250})
data = resp.json()

mylist = []
for job in data['JobData']:
	mylist.append(job['OrganizationName'])

dic = {}
for org in mylist:
	if org in dic:
		dic[org] += 1
	else:
		dic[org] = 1
	

print(dic)