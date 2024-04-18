import csv

inflation_dict = dict()

reader = csv.DictReader(open('inflation_rates.csv'))
for row in reader:
    inflation_dict[row['Year']] = row['Inflation Rate']

def inflation_adjustment(price, original_year, new_year = 2024):
    year = original_year
    new_price = float(price)
    while int(year) < 2024:
        new_price = new_price * (1+(float(inflation_dict[year])/100))
        year = str(int(year) + 1)
    return str(int(new_price))

def transaction_tax(price, sale_year, start_year, threshold, percentage):
    if price > threshold:
        if sale_year >= start_year:
            return (price-threshold)*percentage

def propery_tax(price, brackets):
    tax = 0
    for bracket in brackets:
        

reader = csv.DictReader(open('boston_residential_sales.csv'))
new_fields = ['adjusted_price', 'adjusted_mortgage', 'down_payment', 'yearly_payments', 'first_year_payment']
writer = csv.DictWriter(open('policies_boston_residential_sales.csv', 'w'), fieldnames=reader.fieldnames+new_fields)
writer.writeheader()
for row in reader:
    sale_year = row['date'][0:4]
    adjusted_price = inflation_adjustment(row['price'], sale_year)
    adjusted_mortgage = inflation_adjustment(row['mortgage'], sale_year)
    row['adjusted_price'] = adjusted_price
    row['adjusted_mortgage'] = adjusted_mortgage
    if int(adjusted_mortgage) > int(adjusted_price) or adjusted_mortgage == '0':
        adjusted_mortgage = str(int(float(adjusted_price) * 80/100))
    row['down_payment'] = str(int(down_payment(adjusted_price, adjusted_mortgage)))
    row['yearly_payments'] = str(int(mortgage_payment(adjusted_mortgage)))
    row['first_year_payment'] = str(int(mortgage_payment(adjusted_mortgage) + down_payment(adjusted_price, adjusted_mortgage)))
    writer.writerow(row)