import numpy as np
from scipy.fftpack import dct
import time
import timeit
alpha=0.95
N=256
MFCC_FRAME_LENGTH=200
eps=10e-6

mel_fb_weights=np.genfromtxt('mel_filters.csv',delimiter=',')
mel_fb_sq_weights=mel_fb_weights**2

def preemphasis(input_frame,alpha):
	return input_frame - alpha*np.concatenate((np.full(1, 0), input_frame[:-1]))

def windowing(input_frame):
	return input_frame * np.hamming(len(input_frame))

def compute_fft(input_frame):
	return np.fft.rfft(input_frame,N)

def mel_fb_pass(input_frame):
	return np.log(np.dot(mel_fb_sq_weights,(np.abs(input_frame)**2)) + eps)

def compute_dct(input_frame):
	return dct(input_frame)

start_time=time.time()
#np.log(np.dot(np.random.random([23,200]),np.random.random(200)**2))
y = compute_dct(mel_fb_pass(compute_fft(windowing(preemphasis(np.random.random(MFCC_FRAME_LENGTH),alpha)))))

#print(np.shape(y))
print(time.time()-start_time)


