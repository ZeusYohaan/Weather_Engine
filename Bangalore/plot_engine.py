import matplotlib.pyplot as plt
import csv

def parameter_process(list_param, name, date_param, time):
    plt.stem(date_param, list_param)
    plt.xlabel('Date-Time')
    plt.xticks(fontsize=5)
    plt.ylabel(name)
    time=time.replace(" ","_").replace(":", "")
    file_str = f'{name}_{str(time)}.png'
    plt.savefig(r'C:\Coding Folders\Pyhton_Projects\Pollution_Checker\Bangalore\{}\{}'.format(name, file_str))
    plt.clf()

def convert_data(lst):
    return [float(x) for x in lst]

def process_csv(filename):
    data = []
    time = []
    co = []
    o3 = []
    no2=[]
    so2=[]
    pm10=[]
    pm25=[]
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
            if row == []:
                data.remove(row)
    data = data[1:]
    for i in data:
        o3.append(i[4])
        no2.append(i[3])
        time.append(i[-1])
        pm25.append(i[-6])
        pm10.append(i[-7])
        so2.append(i[-5])
        co.append(i[0])
    co = convert_data(co)
    o3 = convert_data(o3)
    no2=convert_data(no2)
    pm25=convert_data(pm25)
    pm10=convert_data(pm10)
    so2=convert_data(so2)
    t=time[-1]
    parameter_process(co, 'Carbon-Monoxide', time, t)
    parameter_process(o3, 'Ozone', time, t)
    parameter_process(no2, 'Nitrogen-Dioxide', time, t)
    parameter_process(so2, 'Sulphur-Dioxide', time, t)
    parameter_process(pm10, 'PM10', time, t)
    parameter_process(pm25, 'PM25', time, t)
    stackplot(co, o3, no2, so2, pm10, pm25, xarray=time)

def stackplot(*yarrays, xarray):
    x = xarray
    plt.stackplot(x, *yarrays, labels=['CO', 'O3', 'NO2', 'So2', 'PM10', 'PM25'])
    plt.xlabel('Timeline')
    plt.legend(loc='upper right')
    plt.xticks(fontsize=5)
    time = x[-1]
    time = time.replace(" ", "_").replace(":", "")
    file_str = f'Stackplot_{str(time)}.png'
    plt.savefig(r'C:\Coding Folders\Pyhton_Projects\Pollution_Checker\Bangalore\mix\{}'.format(file_str))
    plt.clf()


process_csv(r'C:\Coding Folders\Pyhton_Projects\Pollution_Checker\Bangalore\engine_output.csv')
