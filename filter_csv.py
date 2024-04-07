import csv

reader = csv.DictReader(open('new_boston_residential_sales.csv'))
fields = ['full_address', 'lon', 'lat', 'adjusted_price', 'first_year_payment', 'yearly_payments', 'down_payment']
writer = csv.DictWriter(open('filtered_boston_residential_sales.csv', 'w'), fieldnames=fields)
writer.writeheader()
for row in reader:
    record = dict()
    record['full_address'] = row['address'] + ', ' + row['city'] + ', ' + row['zip']
    for field in fields[1:]:
        record[field] = row[field]
    writer.writerow(record)