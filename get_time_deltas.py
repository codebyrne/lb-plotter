#! /usr/bin/python3
'''
This module will create a list of time deltas given a list of datetime strings
that are provided in a file, one per line, assuming they are in ascending
order.
'''

import os, sys
from datetime import datetime

def get_dtm_data(filename):
    '''
    Returns an array of dtm strings, given the filename
    '''

    try:
        datestamp_array = []
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                for line in f.readlines():
                    datestamp_array.append(line.strip())
    
    except Exception as e:
        print("Error reading datestamps: %s" % str(e))
    
    return datestamp_array

def calculate_deltas(dtm_array):
    '''
    Return the time deltas, given an array of datetime strings.
    '''

    deltas_array = []
    previous_dtm = ""

    try:
        for dtm in dtm_array:
            if previous_dtm != "":
                d1 = datetime.strptime(dtm, "%Y-%m-%d %H:%M:%S.%f")
                d2 = datetime.strptime(previous_dtm, "%Y-%m-%d %H:%M:%S.%f")

                deltas_array.append(get_sec(str(d1 - d2)))

            previous_dtm = dtm
    
    except Exception as e:
        print("Error calculating deltas: %s" % str(e))

    return deltas_array

def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename_param = sys.argv[1]
    else:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(0)
    
    datestamps = get_dtm_data(filename_param)
    deltas = calculate_deltas(datestamps)
    for value in deltas:
        print(value)