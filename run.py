from openpyxl import load_workbook
import json

wb = load_workbook(filename = '20210624.xlsx')
sheet = wb.active

master = {}
master['cities'] = {}
data = master['cities']

for row in sheet.iter_rows(min_row=2, max_col=4, values_only=True):
    ### data.add((row[0], row[1], row[3]))
    city = row[0]
    city = city.rstrip();

    district = row[1]
    district = district.rstrip();

    neighborhood = row[3]
    neighborhood = neighborhood.rstrip();
    
    if city not in data.keys():
        data[city] = {
            'districts': {}
        }

    if district not in data[city]['districts'].keys():
        data[city]['districts'][district] = {
            'neighborhoods': []
        }

    data[city]['districts'][district]['neighborhoods'].append(neighborhood)

with open('output.json', 'w') as outfile:
    json.dump(master, outfile)
