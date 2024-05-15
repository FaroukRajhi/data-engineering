#!/bin/bash

# Extract reading with get_tem_API from the sensor
# Append reading to temperature.log

get_tem_API >> temperature.log

# Buffer last hour of readings
tail -60 temperature.log > temperature.log

# Call get_stats.py to aggregate the readings
# get_stats.py:
# Reads temperatures from file
# Calculates temperature stats
# writes temperature stats to file

python3 get_stats.py temperature.log temp_stats.csv

# Load the stats using load_stats_api
load_stats_api temp_stats.csv
