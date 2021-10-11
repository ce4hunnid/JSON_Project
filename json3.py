from plotly.graph_objs import Scattergeo, Layout  # BrightnessReport1
from plotly import offline
import json

infile = open('us_fires_9_1.json', 'r')


fire_data = json.load(infile)


brightness = []
lons = []
lats = []

brightness, lons, lats, hover_text = [], [], [], []

for rec in fire_data:
    br = rec['brightness']
    if br > 450:

        brightness.append(br)

        lon = rec["longitude"]
        lat = rec["latitude"]

        lons.append(lon)
        lats.append(lat)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,


    'marker': {
        'size': [.03 * br for br in brightness],
        'color':brightness,
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar':{'title': 'Brightness'}
    }
}]

my_layout = Layout(title='US Fires - 9/1/2020 through 9/13/2020')

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='us_fires_9_1.html')
