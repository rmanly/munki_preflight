#!/usr/local/munki/munki-python

import subprocess
import sys

try:
    if sys.argv[1] == 'checkandinstallatstartup':
        cmd = ["/usr/bin/pmset", "-a", "sleep", "x", "displaysleep", "0", "disksleep", "0"]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except IndexError:
    sys.exit("We didn't get passed a munki runtype!") 
