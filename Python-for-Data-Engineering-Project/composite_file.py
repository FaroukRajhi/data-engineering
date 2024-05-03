import glob
import pandas as pd

list_csv = glob.glob('*.csv')
list_csv:['exercise03_car_sales_data.csv']

list_json = glob.glob('*.json')
list_json:['person.json']

print(list_csv)
print(list_json)
    