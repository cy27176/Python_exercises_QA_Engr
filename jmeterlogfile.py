import pytz

timeStamp_i = 0
elapsed_i = 1
label_i = 2
responseCode_i = 3
responsemsg_i = 4
threadName_i = 5
dataType_i = 6
success_i = 7
failuremsg_i = 8
bytes_i = 9
sentBytes_i = 10
grpThreads_i = 11
allThreads_i = 12
URL_i = 13
Latency_i = 14
IdleTime_i = 15
Connect_i = 16

ROOT_PATH = '/Users/Lenovo/Downloads/Python_exercises_QA_Engr (5)/Updated_Python_exercises_QA_Engr'

import csv
from datetime import datetime

def read_csv_file(file_name):
    file = open(file_name)
    csv_reader = csv.reader(file)
    headers = next(csv_reader)
    return headers, csv_reader

def logtest():
    files_list = ['Jmeter_log1.jtl', 'Jmeter_log2.jtl']

    for file in files_list:
        headers, cvs_reader = read_csv_file(ROOT_PATH + '/' + file)
        # loop over lines
        for row in cvs_reader:
            # check the response codes
            if row[responseCode_i] != '200':
                label = row[label_i]
                response_code = row[responseCode_i]
                response_msg = row[responsemsg_i]
                failure_msg = row[failuremsg_i]
                time = row[timeStamp_i]
                time = datetime.fromtimestamp(int(time) / 1000.0, tz=pytz.timezone('PST8PDT')).strftime('%Y-%m-%d %H:%M:%S %Z')
                print(time, label, response_code, response_msg, failure_msg)


logtest()