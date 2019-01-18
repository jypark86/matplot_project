#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import time
from random import *

def main():

	file_1 = open("/home/vsi/python_sample_file/project_sample_1",'r')
	file_2 = open("/home/vsi/python_sample_file/result",'w')

#	while 1:
	for i in range(5):
		
		read_data = file_1.readline()
		if not read_data: break

		split_data = read_data.replace('=',' ').replace(',','').replace(' \n','').split(" ")	# data parsing
#		print(split_data)
#		print(type(split_data))	# list
	
		file_2.write(str(split_data)+"\n")
	
	file_1.close()
	file_2.close()
	
	file_3 = open("/home/vsi/python_sample_file/result",'r')

# make matrix	
	read_data = file_3.read().splitlines()

	for i in range(25):
			if(i % 2) == 0):
				replace_data = read_data[i]
	arr = np.array(replace_data)
	print(arr)

	file_3.close()



if __name__ == '__main__':
	main()
