import numpy as np
import math

def euclidianDistance(a,b)
	return math.sqrt(a*a + b*b)


def distance(a,b):
	if(a != b):
		return 1
	else:
		return 0

def dtwDistance(a,b):
	if (type(a) is str):
		a = list(a)
	if (type(b) is str):
		b = list(b)
	if (type(a) is list):
		a = np.array(a)
	if (type(b) is list):
		b = np.array(b)
	DTW = np.empty([a.shape[0],b.shape[0]])
	DTW[:] = np.inf

	DTW[0,0] = 0
	
	for i in range(a.shape[0]):
		for j in range(b.shape[0]):
			cost = distance(a[i],b[j])
			r_index = i-1
			c_index = j-1
			if(r_index < 0):
				r_index = 0
			if(c_index < 0):
				c_index = 0
			DTW[i,j] = cost + min(DTW[r_index,j],DTW[i,c_index],DTW[r_index,c_index])
	return DTW[-1,-1]

