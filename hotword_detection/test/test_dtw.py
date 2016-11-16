import sys
import os, random

sys.path.append(os.path.abspath('.'))

from hotword_detection import dtw
import numpy as np

def test_dtw_list():
        temp = dtw.DTW(distFunc=dtw.euclideanDistance)
        no_of_test = 100

        def isDistanceZero(x):
                assert(x==0)

        for i in range(no_of_test):
                N = random.randint(1, 50)
		test_list = np.random.random_sample((200, N))
                dist = temp.compute_distance(test_list, test_list)
                yield isDistanceZero, dist

if __name__=="__main__":
	test_dtw_list()
