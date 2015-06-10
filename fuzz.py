#Author: 	Aaron Huber
#Date:		5/2015

#This python script is a simple fuzzer.

import sys
import subprocess

badstr=[]

for i in range(1, 1000, 1):
	badstr.append("A" * i)

try:
	for bad in badstr:
		print "Trying string of length %i" % len(bad)
		subprocess.check_output("./password %s" % bad, shell=True)

except Exception as e:
	print e
	print "****************"
	print "TANGO DOWN"
	print "****************"