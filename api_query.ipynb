import requests
import pandas as pd
import csv
f = open('just_country_codes.csv', 'r', errors='ignore')
data = f.read()
cc_elements = data.split("\n")
payload = {'since':'2019-01-01', 'limit':'1000'}
#may need to run saudi arabia and UAE standalone with a limit of 10,000
#cc_elements = ['SA','AE']
list_cc_codes = []
list_confirmed =[]
list_confirmed_false = []

for i in range(len(cc_elements)):
    payload['probe_cc'] = cc_elements[i]
    r = requests.get('https://api.ooni.io/api/v1/measurements', params=payload)
    results = r.json()
    measurement_list = results['results']
    list_cc_codes.append(cc_elements[i])
    print (cc_elements[i])
    confirmed_count = 0
    confirmed_false_count = 0
    for i in range(len(measurement_list)):
        item1 = measurement_list[i]
        if item1['confirmed'] == True:
            confirmed_count += 1
        else: confirmed_false_count += 1

    list_confirmed.append(confirmed_count)
    list_confirmed_false.append(confirmed_false_count)

print (list_cc_codes)
print (list_confirmed)
print (list_confirmed_false)

with open('censored_countries.csv','w') as outcsv:
    writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    for i in range(len(list_cc_codes)):
        writer.writerow([list_cc_codes[i], list_confirmed[i], list_confirmed_false[i]])
