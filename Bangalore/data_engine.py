import geocoder as g
import csv
import requests

api_key = 'dd0609d63277bb1a4d281cd767b3d12f6e35d043'
city_name = g.ip('me').city
city_name='Bengaluru'
url = f'https://api.waqi.info/feed/{city_name}/?token={api_key}'

def clean_data(data_dict):
    d_val = {}
    d1 = data_dict['data']['iaqi']
    d2 = data_dict['data']['time']
    for i in d1.keys():
        d_val[i] = d1[i]['v']
    time_val = d2['s']
    d_val['time'] = time_val
    return d_val

def write_data(file_name, data_dict):
    with open(file_name, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data_dict.keys())
        writer.writerow(data_dict)

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    # print(data)
    cleaned_data = clean_data(data)
    write_data('C:\Coding Folders\Pyhton_Projects\Pollution_Checker\Bangalore\engine_output.csv', cleaned_data)

print('Data has been written to "engine_output.csv".')
