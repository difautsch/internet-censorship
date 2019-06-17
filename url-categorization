import csv
import requests

payload = {'since':'2019-01-01', 'limit':'1000', 'confirmed':'true', 'probe_cc': 'IR'}
input_cc = ['IR','IN','SA','AE','MY','RO','RU']
country_codes = []
input_url = []
test_name = []

for i in range(len(input_cc)):
    payload['probe_cc'] = input_cc[i]
    r = requests.get('https://api.ooni.io/api/v1/measurements', params=payload)
    results = r.json()
    measurement_list = results['results']
    confirmed_count = 0
    confirmed_false_count = 0
    for y in range(len(measurement_list)):
        country_codes.append(input_cc[i])
        input_url.append(measurement_list[y]['input'])
        test_name.append(measurement_list[y]['test_name'])
print (len(country_codes), len(input_url), len(test_name))

sexy_words = ['sex','porn','adult','girls','penis','date','dating','amateur','panties','69','love','playboy','xxx','erotic']
gay_words = ['gay','queer','penis','lesbian','feminist','grindr']
gambling_words = ['casino','gambling','bet','sport','slot']
news = ['facebook','google','bbc','datpiff','freedom','cbs','twitter','pinterest','tor','yahoo','reddit']
religion = ['muslim','islam','hindu','arab','jew','israel','judaism']
drugs = ['cannabis','marijuana','weed','420','psychedelics','psy']

urls = []
url_types = []
country_codes_1 = []


for i,x in enumerate(input_url):
        for y in sexy_words:
            if y in x:
                rls.append(x)
                url_types.append('sexy')
                country_codes_1.append(country_codes[i])
        for y in gay_words:
            if y in x:
                urls.append(x)
                url_types.append('gay')
                country_codes_1.append(country_codes[i])
        for y in gambling_words:
            if y in x:
                urls.append(x)
                url_types.append('gambling')
                country_codes_1.append(country_codes[i])
        for y in news:
            if y in x:
                urls.append(x)
                url_types.append('news')
                country_codes_1.append(country_codes[i])
        for y in religion:
            if y in x:
                urls.append(x)
                url_types.append('religion')
                country_codes_1.append(country_codes[i])
        for y in drugs:
            if y in x:
                urls.append(x)
                url_types.append('drugs')
                country_codes_1.append(country_codes[i])
print (len(urls), len(url_types), len(country_codes_1))
print (len(input_url), len(country_codes))

with open('all_url_analysis.csv','w') as outcsv:
    writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    for i in range(len(country_codes)):
         writer.writerow([country_codes[i], urls[i], test_name[i]])
