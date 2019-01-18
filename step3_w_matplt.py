#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import time
from random import *

def main():

	vector_set = []
	plt.ylim((0,100))
	file = open("/home/vsi/python_sample_file/vsi_sample",'w')	# open file
	
	for i in range(10):
		k = randint(1,100)
#		vector_set.append(i)
		vector_set.append(k)
		new_vector_set = vector_set[0:10]
	
	file.write(str(vector_set) + "\n") # save init data
#	file.write("/".join(vector_set) + "\n") # save init data

	plt.plot(new_vector_set)

	plt.ion()
	plt.show()
	plt.pause(0.001)

	for i in range(50):
		
		file = open("/home/vsi/python_sample_file/vsi_sample",'a') # open file again (append data)

		plt.ylim((0,100))
		k = randint(1,100)
		vector_set.append(k)
		new_vector_set = vector_set[i+1:i+11]

		file.write(str(vector_set) + "\n")	# save appending data
		file.close()	# file close
	
		plt.clf()
		plt.plot(new_vector_set)
	
		plt.ion()
		plt.pause(0.001)
		plt.show()

	plt.show(block=True)
#	time.sleep(1)

if __name__ == '__main__':
	main()
