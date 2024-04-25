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

property_thresholds = [500000, 1000000]
property_percentages = [0.03, 0.06]
year_property = 2000
total_property_tax = 0

transfer_thresholds = [1000000]
transfer_percentages = [0.05]
year_transfer = 2000
total_transfer_tax = 0

def progressive_tax(price, thresholds, percentages):
    taxes = 0
    for i in range(len(percentages)):
        if i == len(thresholds)-1 or price < thresholds[i+1]:
            taxes += (price-thresholds[i])*(percentages[i])
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
    if int(sale_year) >= year_transfer:
        transfer_tax = progressive_tax(int(sale_price), transfer_thresholds, transfer_percentages)
        adjusted_transfer_tax = inflation_adjustment(transfer_tax, sale_year)
        total_transfer_tax += int(adjusted_transfer_tax)
    else:
        transfer_tax = 0
    row['transfer_tax'] = adjusted_transfer_tax
    if row['yearbuilt'] == '':
        year_built = 0
    else:
        year_built = int(row['yearbuilt'])
    if year_built < year_property:
        yr = str(year_property)
    else:
        yr = str(year_built)
    prop_tax = 0
    while int(yr) <= 2024:
        yr_val = inflation_adjustment(sale_price, sale_year, int(yr))
        yr_prop_tax = progressive_tax(int(yr_val), property_thresholds, property_percentages)
        prop_tax += int(inflation_adjustment(yr_prop_tax, yr, 2024))
        yr += str(int(yr)+1)
    total_property_tax += prop_tax
    row['property_tax'] = prop_tax
    writer.writerow(row)

print("transfer tax: ", total_transfer_tax)
print("property tax: ", total_property_tax)