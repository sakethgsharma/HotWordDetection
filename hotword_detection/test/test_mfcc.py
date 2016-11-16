import sys
import os

sys.path.append(os.path.abspath('.'))
from hotword_detection import mfcc
import numpy as np

def test_mfcc_first_coefficient():
        temp = mfcc.MFCC()
        no_of_test = 100
        input_matrix = np.random.random_sample((no_of_test,200))

        def first_coeff_greater_than_0(x):
                assert(x>0)

        for i in range(no_of_test):
                input_frame = input_matrix[i]
                coeffs = temp.compute_mfcc(input_frame, include_dc=True)
                yield first_coeff_greater_than_0, coeffs[0]

def test_hz2mel_mel2hz():
	temp = mfcc.MFCC()
	no_of_test = 100
	input_freq = np.random.random_sample(no_of_test)
	
	def isEqual(pred_hz, actual_hz):
                assert(np.abs(pred_hz-actual_hz) < 0.001)
	
	for i in range(no_of_test):
                pred_hz = temp.mel2hz(temp.hz2mel(input_freq[i]))
                yield isEqual, pred_hz, input_freq[i]	

if __name__=="__main__":
	test_mfcc_first_coefficient()
	test_hz2mel_mel2hz()
