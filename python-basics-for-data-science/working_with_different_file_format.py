# Reading CSV Files
import pandas as pd
file = 'exercise03_car_sales_data.csv'

df= pd.read_csv(file)
print(df)

# Reading CSV Files
import json

with open('sample_json.json', 'r') as openfile:
    json_object = json.load(openfile)

print(json_object)

# Reading XML Files
import xml.etree.ElementTree as etree

tree = etree.parse("sample_xml.xml")
root = tree.getroot()
print(root)    

# Check documentation for more details about methods