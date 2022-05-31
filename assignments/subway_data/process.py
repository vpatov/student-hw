import json
import geopy
from collections import defaultdict
from geopy.distance import geodesic

with open('subway_lines.geojson','r') as f:
    subway_lines = json.load(f)

with open('subway_stations.geojson','r') as f:
    subway_stations = json.load(f)

# Start at one end of the line. 
# For each point on the line, find the closest subway station on that line
# Set that subway station to current
# Keep going down the line, until the closest station is a different one
# Set current.next = new_station, set new_station.prev = current, set current = new_station
# Keep going until the end of the line

grouped_lines = defaultdict(list)

for feature in subway_lines['features']:
    props = feature['properties']
    geometry = feature['geometry']
    coordinates = geometry['coordinates']
    lines = props['name'].split('-')
    for line in lines:
        grouped_lines[line.strip()].extend(coordinates)
    
all_lines = defaultdict(list)
stations_by_line = defaultdict(list)

for feature in subway_stations['features']:
    coordinates = feature['geometry']['coordinates']
    props = feature['properties']
    line_name = props['line'].replace(' Express','')
    lines = line_name.split('-')
    for line in lines:
        # station_lines[line.strip()].append(feature)
        all_lines[line.strip()].append({
            'name': props['name'],
            'line': line,
            'objectid': props['objectid'],
            'coors': tuple(feature['geometry']['coordinates'])
        })


N_line = all_lines['N']
start = '469'

min_dist = float('inf')
min_objectid = None
for station in N_line:
    name, line, objectid, coors = [station[k] for k in ['name','line','objectid','coors']]
    if objectid == start:
        continue
    dist = geodesic()


nn_sorted = []


# for feature in N_lines:
#     props = 

    
    
