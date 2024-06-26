import glob                         # this module helps in selecting files 
import pandas as pd                 # this module helps in processing CSV files
import xml.etree.ElementTree as ET  # this module helps in processing XML files.
from datetime import datetime

# CSV Extraction function
def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe
print(extract_from_csv('source1.csv'))

JSON Extract Function
def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process,lines=True)
    return dataframe
XML Extract Function
def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=["name", "height", "weight"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        dataframe = dataframe.append({"name":name, "height":height, "weight":weight}, ignore_index=True)
    return dataframe
Extract Function
    
    #process all csv files
    for csvfile in glob.glob("*.csv"):
        extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)
        
    #process all json files
    for jsonfile in glob.glob("*.json"):
        extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)
    
    #process all xml files
    for xmlfile in glob.glob("*.xml"):
        extracted_data = extracted_data.append(extract_from_xml(xmlfile), ignore_index=True)
        
    return extracted_data
def extract():
    extracted_data = pd.DataFrame(columns=['name','height','weight']) # create an empty data frame to hold extracted data
    
    #process all csv files
    for csvfile in glob.glob("*.csv"):
        extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)
        
    #process all json files
    for jsonfile in glob.glob("*.json"):
        extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)
    
    #process all xml files
    for xmlfile in glob.glob("*.xml"):
        extracted_data = extracted_data.append(extract_from_xml(xmlfile), ignore_index=True)
        
    return extracted_data
Transform
The transform function does the following tasks.

Convert height which is in inches to millimeter
Convert weight which is in pounds to kilograms
def transform(data):
        #Convert height which is in inches to millimeter
        #Convert the datatype of the column into float
        #data.height = data.height.astype(float)
        #Convert inches to meters and round off to two decimals(one inch is 0.0254 meters)
        data['height'] = round(data.height * 0.0254,2)
        
        #Convert weight which is in pounds to kilograms
        #Convert the datatype of the column into float
        #data.weight = data.weight.astype(float)
        #Convert pounds to kilograms and round off to two decimals(one pound is 0.45359237 kilograms)
        data['weight'] = round(data.weight * 0.45359237,2)
        return data
Loading
def load(targetfile,data_to_load):
    data_to_load.to_csv(targetfile)  
Logging
def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')
Running ETL Process
log("ETL Job Started")
log("Extract phase Started")
extracted_data = extract()
log("Extract phase Ended")
extracted_data
log("Transform phase Started")
transformed_data = transform(extracted_data)
log("Transform phase Ended")
transformed_data 
log("Load phase Started")
load(targetfile,transformed_data)
log("Load phase Ended")
log("ETL Job Ended")
Exercise
Using the example above complete the exercise below.

Download Files
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/datasource.zip
--2021-01-20 15:58:13--  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/datasource.zip
Resolving cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud (cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud)... 169.63.118.104
Connecting to cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud (cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud)|169.63.118.104|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4249 (4.1K) [application/zip]
Saving to: ‘datasource.zip’

datasource.zip      100%[===================>]   4.15K  --.-KB/s    in 0.001s  

2021-01-20 15:58:13 (8.09 MB/s) - ‘datasource.zip’ saved [4249/4249]

Unzip Files
!unzip datasource.zip -d dealership_data
Archive:  datasource.zip
  inflating: dealership_data/used_car_prices1.csv  
  inflating: dealership_data/used_car_prices2.csv  
  inflating: dealership_data/used_car_prices3.csv  
  inflating: dealership_data/used_car_prices1.json  
  inflating: dealership_data/used_car_prices2.json  
  inflating: dealership_data/used_car_prices3.json  
  inflating: dealership_data/used_car_prices1.xml  
  inflating: dealership_data/used_car_prices2.xml  
  inflating: dealership_data/used_car_prices3.xml  
About the Data
The file dealership_data contains CSV, JSON, and XML files for used car data which contain features named car_model, year_of_manufacture, price, and fuel.

Set Paths
tmpfile    = "dealership_temp.tmp"               # file used to store all extracted data
logfile    = "dealership_logfile.txt"            # all event logs will be stored in this file
targetfile = "dealership_transformed_data.csv"   # file where transformed data is stored
