from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import json

infile = open('eq_data_30_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eq_data = json.load(infile)  # converts content of file into dictionary object

json.dump(eq_data, outfile, indent=4)

# Need to pull out the mag and coordinates... mag is key word of dictionary "properties"
# inside LIST features, which is a list of dictionaries... each earthquake in list is a dictionary

list_of_eqs = eq_data["features"]

mags = []  # empty list
lons = []
lats = []

mags, lons, lats, hover_text = [], [], [], []

for eq in list_of_eqs:  # eq is a dictionary
    mag = eq["properties"]["mag"]
    mags.append(mag)
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    title = eq['properties']['title']
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)


print(mags[:5])  # this created a LISt of magnitudes
print(lons[:5])
print(lats[:5])


data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
        'size': [5 * mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar':{'title': 'Magnitude'}
    }
}]

my_layout = Layout(title='Global Earthquake 30 Days')

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='globalearthquake1.html')
