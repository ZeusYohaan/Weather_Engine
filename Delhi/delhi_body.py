import time
import subprocess
import multiprocessing 

def data_engine():
    file_path = 'C:\Coding Folders\Pyhton_Projects\Pollution_Checker\Delhi\data_engine.py'
    interval = 600 
    while True:
        subprocess.Popen(['python', file_path])
        time.sleep(interval)

def plot_engine():
    file_path = 'C:\Coding Folders\Pyhton_Projects\Pollution_Checker\Delhi\plot_engine.py'
    interval = 3600
    while True:
        subprocess.Popen(['python', file_path])        
        time.sleep(interval)

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=data_engine)
    process2 = multiprocessing.Process(target=plot_engine)

    process1.start()
    process2.start()

    process1.join()
    process2.join()
