#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import time
from random import *
import json									# json

def main():

#	json = json.loads(open('/home/vsi/python_sample_file/json_sample.json').read())
#	value = json['key']
#	print json['value']

	f= open("/home/vsi/python_sample_file/json_sample.json", 'r')

#	line= f.readline()
#	print(line)

#	lines= f.readlines()
#	for line in lines:
#		print(line)

	data= f.read()
	print(data)
	
	f.close()

if __name__ == '__main__':
	main()
