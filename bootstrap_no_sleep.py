#!/usr/bin/python

import subprocess
import sys

try:
    if sys.argv[1] == 'checkandinstallatstartup':
        cmd = ["/usr/bin/pmset", "-a", "sleep", "x", "displaysleep", "0", "disksleep", "0"]
            # not worth the time to setup communicate to capture and discard output etc
            subprocess.check_call(cmd)
except IndexError:
    sys.exit("We didn't get passed a munki runtype!") 
except subprocess.CalledProcessError:
    sys.exit("pmset failed")
