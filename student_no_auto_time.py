#!/usr/bin/python

from sys import argv
from time import localtime

no_run_hours = [7, 8, 9, 10, 11, 12, 13, 14, 15]

now = localtime()

(current_weekday, current_hour, current_min) = now[6], now[3], now[4]

try:
    if argv[1] == 'auto':
        # allow auto to run on Saturday and Sunday
        if current_weekday == 5 or current_weekday == 6:
            exit()
        # allow times in 15:xx after 15:15
        elif current_hour == 15 and current_min >= 15:
            exit()
        # disallow munki auto run for all other hours in list
        elif current_hour in no_run_hours:
            exit(1)
except IndexError:
    # somehow we didn't get passed a runtype
    exit(2) 
