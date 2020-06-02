import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#https://data.boston.gov/dataset/existing-bike-network
#https://bostonopendata-boston.opendata.arcgis.com/datasets/boston-street-segments
bike_network = pd.read_csv("Existing_Bike_Network.csv")
street_info = pd.read_csv("Boston_Street_Segments.csv")
pd.pandas.set_option('display.max_columns', None)

#Take the bike map network to show total bike lane miles
total_bike = bike_network['Shape__Length'].sum()/5280
print("Total Bike Lane Miles in Boston (miles):\n", total_bike)

#Show total # of roads in Boston, in miles
total_road = street_info['SHAPElen'].sum()/5280
print("Total Road Lane Miles in Boston (miles):\n", total_road)

#Show bike lanes by type
bike_type = (bike_network.groupby('ExisFacil')['Shape__Length'].sum()/5280).reset_index(drop=False)
bike_type = bike_type.sort_values(by=['Shape__Length'], ascending=False)
x = bike_type['ExisFacil'].tolist()
y = bike_type['Shape__Length'].tolist()
pos = np.arange(len(y))
plt.bar(pos,y)
plt.xlabel('Bike Type')
plt.ylabel('Bike Length (miles)')
ticks = plt.xticks(pos, x, rotation = (65))
plt.show()

#For all roads in Boston, what is the length by speed. 
road_speed = (street_info.groupby('SPEEDLIMIT')['SHAPElen'].sum()/5280).reset_index(drop=False)
print(road_speed)
x2 = road_speed['SPEEDLIMIT'].tolist()
y2 = road_speed['SHAPElen'].tolist()
pos2 = np.arange(len(y2))
plt.bar(pos2,y2)
plt.xlabel('Speed Limit')
plt.ylabel('Road Length (miles)')
ticks2 = plt.xticks(pos2, x2, rotation = (65))
plt.show()

#How many of Boston's roads have a sub-25mph speed limit?
sub_25 = road_speed.loc[road_speed['SPEEDLIMIT'] <30, 'SHAPElen'].sum()
print(sub_25)

#Show history of Bike Lane installation by year
bike_year = (bike_network.groupby('InstallDat')['Shape__Length'].sum()/5280).reset_index(drop=False)
x1 = bike_year['InstallDat'].tolist()
y1 = bike_year['Shape__Length'].tolist()
pos1 = np.arange(len(y1))
plt.bar(pos1,y1)
plt.xlabel('Year')
plt.ylabel('Bike Length (miles)')
ticks1 = plt.xticks(pos1, x1, rotation = (65))
plt.show()
