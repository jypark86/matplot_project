#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import time
from random import *

def main():

	vector_set = []
	plt.ylim((0,100))
	
	for i in range(10):
		k = randint(1,100)
#		vector_set.append(i)
		vector_set.append(k)
		new_vector_set = vector_set[0:10]
	
#		print(new_vector_set)	# checking

	plt.plot(new_vector_set)

	plt.ion()
	plt.show()
	plt.pause(0.001)

	for i in range(50):

		plt.ylim((0,100))
		k = randint(1,100)
		vector_set.append(k)
		new_vector_set = vector_set[i+1:i+11]

		plt.clf()
		plt.plot(new_vector_set)
	
		plt.ion()
		plt.pause(0.001)
		plt.show()

	plt.show(block=True)
#	time.sleep(1)

if __name__ == '__main__':
	main()
