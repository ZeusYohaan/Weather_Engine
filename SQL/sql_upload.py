import pyodbc
import csv
import datetime

server = 'DESKTOP-E0NOB13'
database = 'Weather_Engine'
username = 'YoUser'
password = '2004'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(connection_string)
curr = conn.cursor()

def check_table_exists(tableName):
    sql_query=f"SELECT COUNT(*) FROM INFORMATION.SCHEMA WHERE TABLE_NAME={tableName}"
    curr.execute(sql_query)
    table_count=curr.fetchone()[0]
    return table_count

def create_table(tableName):
    #CO,dew,H,NO2,O3,Pressure,pm10,pm25,SO2,Temp,W,WG,Time 
    sql_query=f'''CREATE TABLE {tableName}(
                CO VARCHAR(50),
                dew VARCHAR(50),
                H VARCHAR(50),
                NO2 VARCHAR(50),
                O3 VARCHAR(50),
                Pressure VARCHAR(50),
                pm10 VARCHAR(50),
                pm25 VARCHAR(50),
                SO2 VARCHAR(50),
                Temp VARCHAR(50),
                W VARCHAR(50),
                WG VARCHAR(50),
                Time VARCHAR(50)
                )'''
    curr.execute(sql_query)
    curr.commit()

def write_csv_sql(fileName, tableName):
    clear_query=f"DELETE FROM {tableName}"
    curr.execute(clear_query)
    curr.commit()

    with open(fileName) as read_curr:
        csv_data= csv.reader(read_curr)
        next(csv_data)
        for row in csv_data:
            CO,dew,H,NO2,O3,Pressure,pm10,pm25,SO2,Temp,W,WG,Time = row
            sql_query=f'''
                        INSERT INTO ? (CO,dew,H,NO2,O3,Pressure,pm10,pm25,SO2,Temp,W,WG,Time)
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
                        '''
            curr.execute(sql_query, (tableName,CO,dew,H,NO2,O3,Pressure,pm10,pm25,SO2,Temp,W,WG,Time))
            curr.commit()
    return 0

def execute_create_table(city_name, csv_file):
    curr_date=str(datetime.datetime.now().date())
    table_name = city_name+curr_date

    tb_count = check_table_exists(table_name)
    if tb_count==0:
        create_table(table_name)
        write_csv_sql(csv_file, table_name)
    else:
        write_csv_sql(csv_file, table_name)


