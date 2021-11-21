#!/usr/local/munki/munki-python

import subprocess
import sys

try:
    if sys.argv[1] == 'checkandinstallatstartup':
        cmd = ["/usr/bin/pmset", "-a", "sleep", "0", "displaysleep", "0", "disksleep", "0"]
        subprocess.run(cmd, capture_output=True, check=True)
except IndexError:
    sys.exit("We didn't get passed a munki runtype!") 
except subprocess.CalledProcessError:
    sys.exit("pmset failed")
