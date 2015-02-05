#!/usr/bin/python

import time
import sys

no_fly_list = [7, 8, 9, 10, 11, 12, 13, 14]

if time.localtime()[3] in no_fly_list and sys.argv[1] == 'auto':
    exit(1)
