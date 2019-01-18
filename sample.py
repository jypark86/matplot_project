#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

vector_set = []
for i in range(100):
														#x = np.random.normal(0,1)
	y = 0.1 + 0.2 + np.random.normal(0,1)
	vector_set.append([0,y])
	
														#x_data = [v[0] for v in vector_set]
y_data = [v[1] for v in vector_set]

plt.plot(y_data)
plt.show()
