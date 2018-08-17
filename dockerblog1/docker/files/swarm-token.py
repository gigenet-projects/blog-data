#!/bin/python
from sys import argv, exit
from subprocess import Popen, PIPE

try:
    if 'manager' in argv[1] or 'worker' in argv[1]:
        process = Popen(['docker', 'swarm', 'join-token', '%s' % argv[1]], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
    else:
        raise Exception()
    for idx, obj in enumerate(stdout.split(" ")):
        if obj == "--token":
            token=stdout.split(" ")[idx+1]
            break
    if token:
        print token
    else:
        raise Exception()
except:
    exit("Failed to get a proper token.")
