import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
state_name = 'Hawaii'
atts = {"CountrySubdivision": state_name, 'NumberOfJobs': 1}
resp = requests.get(BASE_USAJOBS_URL, params = atts)
data = resp.json()
haw_tot = data['TotalJobs']
state_name = 'Alaska'
atts = {"CountrySubdivision": state_name, 'NumberOfJobs': 1}
resp = requests.get(BASE_USAJOBS_URL, params = atts)
data = resp.json()
ala_tot = data['TotalJobs']
ala_num = int(ala_tot)
haw_num = int(haw_tot)
tot = ala_num + haw_num
print("Alaska has " + ala_tot + " job listings.")
print("Hawaii has " + haw_tot + " job listings.")
print("Together, they have ", tot, " total job listings.")