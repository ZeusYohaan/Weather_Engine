import matplotlib.pyplot as plt
import numpy as np
import csv
from datetime import datetime

fl1="C:\Coding Folders\Pyhton_Projects\Pollution_Checker\Bangalore\engine_output.csv"
fl2="C:\Coding Folders\Pyhton_Projects\Pollution_Checker\Delhi\engine_output.csv"
fl3="C:\Coding Folders\Pyhton_Projects\Pollution_Checker\Kolkata\engine_output.csv"

def convert_data(lst):
    return [float(x) for x in lst]

def remove_duplicates(arr):
    unique_tuples = set(map(tuple, arr))
    unique_arr = [list(t) for t in unique_tuples]
    return np.array(unique_arr)

def read_file(filename):
    data=[]
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
            if row == []:
                data.remove(row)
    data=np.array(data[1:])
    data=remove_duplicates(data)
    data=sorted(data, key=lambda x:x[-1])
    return data

def plot_data(dict, name):
    time=list(dict.keys())
    t_l=time[-1]
    t_l=t_l.replace(" ","_").replace(":", "")
    label=time[0][0]
    updated_time_list = []

    for time in time:
        k = time.split(' ')
        updated_time_list.append(k[1])
    time=updated_time_list
    l1=[]
    l2=[]
    l3=[]
    for i in dict.values():
        l1.append(i[0])
        l2.append(i[1])
        l3.append(i[2])
    l1=convert_data(l1)
    l2=convert_data(l2)
    l3=convert_data(l3)
    plt.plot(time, l1, label='Bangalore')
    plt.plot(time, l2, label='Delhi')
    plt.plot(time, l3, label='Kolkata')
    plt.xlabel('Timeline')
    plt.ylabel('Parameter-Value')
    plt.legend()
    plt.title(label)
    file_str="combined_data"+t_l
    plt.savefig(f"C:\Coding Folders\Pyhton_Projects\Pollution_Checker\Combined\{name}\{file_str}")
    plt.clf()

    

def sort_data(multiple_arr, ind):
    dict={}
    for i in multiple_arr:
        for j in i:
            dict[j[-1]]=[]
    for i in multiple_arr:
        for k in i:
            for j in dict.keys():
                if k[-1]==j:
                    l=dict[j]
                    l.append(k[ind])
    for i in list(dict.keys()):
        if len(dict[i]) != len(multiple_arr):
            del dict[i]
    return dict

def read_data():
    b_np=read_file(fl1)
    d_np=read_file(fl2)
    k_np=read_file(fl3)
    mul_arr=[b_np, d_np, k_np]
    co_d=sort_data(mul_arr, 0)
    plot_data(co_d, 'CO')
    no2_d=sort_data(mul_arr, 3)
    plot_data(no2_d, 'NO2')
    so2_d=sort_data(mul_arr, -5)
    plot_data(so2_d, 'SO2')
    o3_d=sort_data(mul_arr, 4)
    plot_data(o3_d, "O3")
    pm10_d=sort_data(mul_arr, -7)
    plot_data(pm10_d, 'PM10')
    pm25_d=sort_data(mul_arr, -6)
    plot_data(pm25_d, 'PM25')
    print(o3_d)
read_data()




    # lot_data(final_data, 'CO', 0, c_name)
    # plot_data(final_data, 'NO2', 3, c_name)
    # plot_data(final_data, 'SO2', -5, c_name)
    # plot_data(final_data, 'O3', 4, c_name)
    # plot_data(final_data, 'PM25', -6, c_name)
    # plot_data(final_data, 'PM10', -7, c_name)
