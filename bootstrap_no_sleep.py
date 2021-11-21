#!/usr/local/munki/munki-python

import sys
from subprocess import run

try:
    if sys.argv[1] == 'checkandinstallatstartup':
        cmd = ["/usr/bin/pmset", "-a", "sleep", "x", "displaysleep", "0", "disksleep", "0"]
        run(cmd)
except IndexError:
    sys.exit("We didn't get passed a munki runtype!") 
