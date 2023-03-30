import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates = data[0]['rates']

filename = 'rates.csv'

with open(filename, mode = 'w', newline = '') as file:
    writer = csv.writer(file, delimiter = ';')
    writer.writerow(['currency', 'code', 'bid', 'ask'])
    for row in rates:
        writer.writerow([row['currency'], row['code'], row['ask'], row['bid']])

