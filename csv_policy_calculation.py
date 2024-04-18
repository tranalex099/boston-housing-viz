import csv

inflation_dict = dict()

reader = csv.DictReader(open('inflation_rates.csv'))
for row in reader:
    inflation_dict[row['Year']] = row['Inflation Rate']

def inflation_adjustment(price, original_year, new_year = 2024):
    year = original_year
    new_price = float(price)
    while int(year) < new_year:
        new_price = new_price * (1+(float(inflation_dict[year])/100))
        year = str(int(year) + 1)
    return str(int(new_price))

property_thresholds = []
property_percentages = []
year_property = 2000
total_property_tax = 0

transfer_thresholds = []
transfer_percentages = []
year_transfer = 2000
total_property_tax = 0

def progressive_tax(price, thresholds, percentages):
    taxes = 0
    for i in range(len(percentages)):
        if i == len(thresholds)-1 or price < thresholds[i+1]:
            taxes += (price-thresholds[i])*[percentages[i]]
        else:
            taxes += (thresholds[i+1] - thresholds[i]) * percentages[i]
    return taxes
        

reader = csv.DictReader(open('boston_residential_sales.csv'))
new_fields = ['transfer_tax', 'property_tax']
writer = csv.DictWriter(open('policies_boston_residential_sales.csv', 'w'), fieldnames=reader.fieldnames+new_fields)
writer.writeheader()
for row in reader:
    sale_year = row['date'][0:4]
    sale_price = row['price']
    if sale_year >= year_transfer:
        transfer_tax = progressive_tax(sale_price, transfer_thresholds, transfer_percentages)
        adjusted_transfer_tax = inflation_adjustment(transfer_tax, sale_year)
        total_property_tax += adjusted_transfer_tax
    else:
        transfer_tax = 0
    row['transfer_tax'] = transfer_tax
    yr = year_property
    while yr <= curr_year:
    writer.writerow(row)