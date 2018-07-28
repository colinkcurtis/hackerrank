#!/bin/python3
import os
import sys
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    
    if s.startswith('12'):
        
        if s.endswith('PM'):
            s = s[:-2]
            military_time_str = s
        else:
            s = s[:-2]
            standard_time_split = [x for x in s.split(':')]
            standard_time_split[0] = '00'
            military_time_str = ':'.join(standard_time_split)
            
    elif s.endswith('PM'):
        s = s[:-2]
        standard_time_split = [x for x in s.split(':')]
        new_hour_value = int(standard_time_split[0])
        new_hour_value += 12
        standard_time_split[0] = str(new_hour_value)
        military_time_str = ':'.join(standard_time_split)
    
    else:
        s = s[:-2]
        military_time_str = s
    return military_time_str

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()