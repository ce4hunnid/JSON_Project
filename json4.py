from plotly.graph_objs import Scattergeo, Layout  # BrightnessReport1
from plotly import offline
import json

infile2 = open('us_fires_9_14.json', 'r')


fire_data2 = json.load(infile2)


brightness2 = []
lons2 = []
lats2 = []

brightness2, lons2, lats2,  = [], [], [],

for rec in fire_data2:
    br = rec['brightness']
    if br > 450:

        brightness2.append(br)

        lon = rec["longitude"]
        lat = rec["latitude"]

        lons2.append(lon)
        lats2.append(lat)

data2 = [{
    'type': 'scattergeo',
    'lon': lons2,
    'lat': lats2,


    'marker': {
        'size': [.03 * br for br in brightness2],
        'color':brightness2,
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar':{'title': 'Brightness'}
    }
}]

my_layout2 = Layout(title='US Fires - 9/14/2020 through 9/20/2020')

fig = {'data': data2, 'layout': my_layout2}

offline.plot(fig, filename='us_fires_9_14.html')
