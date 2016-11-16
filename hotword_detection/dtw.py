import numpy as np
import math

def euclideanDistance(a,b):
        return np.sqrt(np.abs(np.sum(np.dot(a,a) - np.dot(b,b))))

class DTW:
        def __init__(self, distFunc=euclideanDistance):
                self.distFunc = distFunc 

        def compute_distance(self, reference, test):
                if (type(reference) is str):
	                reference = list(reference)
        	if (type(test) is str):
                	test = list(test)
	        if (type(reference) is list):
	                reference = np.array(reference)
	        if (type(test) is list):
	                test = np.array(test)
	        DTW_matrix = np.empty([reference.shape[0],test.shape[0]])
	        DTW_matrix[:] = np.inf

	        DTW_matrix[0,0] = 0

	        for i in range(reference.shape[0]):
	                for j in range(test.shape[0]):
	                        cost=euclideanDistance(reference[i,:],test[j,:])
	                        r_index = i-1
	                        c_index = j-1
	                        if(r_index < 0):
	                                r_index = 0
	                        if(c_index < 0):
	                                c_index = 0
	                        DTW_matrix[i,j] = cost + min(DTW_matrix[r_index,j],DTW_matrix[i,c_index],DTW_matrix[r_index,c_index])
	        return DTW_matrix[-1,-1]/(test.shape[0]+reference.shape[0])
