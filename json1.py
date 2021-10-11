from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import json

infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eq_data = json.load(infile)  # converts content of file into dictionary object

json.dump(eq_data, outfile, indent=4)

# Need to pull out the mag and coordinates... mag is key word of dictionary "properties"
# inside LIST features, which is a list of dictionaries... each earthquake in list is a dictionary

list_of_eqs = eq_data["features"]

mags = []  # empty list
lons = []
lats = []

for eq in list_of_eqs:  # eq is a dictionary
    mag = eq["properties"]["mag"]
    mags.append(mag)
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    lons.append(lon)
    lats.append(lat)


print(mags[0:5])  # this created a LISt of magnitudes
print(lons[0:5])
print(lats[0:5])


data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title='Global Earthquake 1 Day')

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='globalearthquake1.html')
