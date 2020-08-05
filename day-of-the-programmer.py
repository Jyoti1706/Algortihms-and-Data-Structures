#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    month_days = {'jan':31,'mar':31,'apr':30,'may':31,'jun':30,'july':31,'aug':31}
    year_1918 = 0
    if year < 1918:
        if year%4 == 0:
            month_days['feb'] = 29
        else:
            month_days['feb'] = 28
    elif year > 1918:
        if (year%400 == 0) or ((year%4 == 0) and (not(year%100 == 0))):
            month_days['feb'] = 29
        else:
            month_days['feb'] = 28
    else:
        year_1918 = 13
        month_days['feb'] = 28
    sum_days = 0
    for i in month_days.values():
        sum_days = sum_days+i
    #print("Debugging -- " + str(sum_days))
    programmer_day = 256
    day_left = programmer_day - sum_days + year_1918
    the_day = ""
    month = 9
    if day_left < 31:
        the_day = str(day_left)+".0"+str(month)+"."+str(year)
    else:
        the_day = str(day_left-30)+"."+str(month+1)+"."+str(year)
    return the_day








if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
