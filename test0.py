#!/usr/bin/python

file = open("/home/vsi/python_sample_file/result",'r')

vector_1 = []

vector_2 = []
vector_3 = []
vector_4 = []
vector_5 = []
vector_6 = []
vector_7 = []
vector_8 = []
vector_9 = []
vector_10 = []

while 1:
#for i in range(10):
	read_data = file.readline()
	if not read_data: break
	
	split_data = read_data.split(",")
	
	vector_1.append(split_data[0])
	vector_2.append(split_data[1])
	vector_3.append(split_data[2])
	vector_4.append(split_data[3])
	vector_5.append(split_data[4])
	vector_6.append(split_data[5])
	vector_7.append(split_data[6])
	vector_8.append(split_data[7])
	vector_9.append(split_data[8])
	vector_10.append(split_data[9])

#print(vector_1)
#print(vector_2)
#print(vector_3)
#print(vector_4)
#print(vector_5)
#print(vector_6)
#print(vector_7)
#print(vector_8)
#print(vector_9)
#print(vector_10)
	
index = [vector_1,vector_2,vector_3,vector_4,vector_5,vector_6,vector_7,vector_8,vector_9,vector_10]

for i, name in enumerate(index):
	print(i, name)
