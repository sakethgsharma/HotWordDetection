import numpy as np
from scipy.fftpack import dct
import time
import timeit

class MFCC:
	def __init__(self, alpha=0.95, N=256, fs=8000, eps=10e-6, frame_dur=0.025, hop_dur=0.01, mel_filter_file='mel_filters.csv'):
		self.alpha = alpha   #Preemphasis parameter
		self.N = N	     # No of FFT points	
		self.eps = eps       # eps to avoid mathematical errors
		self.mfcc_frame_length = round(fs*frame_dur)  #frame length for mfcc
		self.hop_length = round(hop_dur*fs)           #hop length for mfcc 
		self.mel_fb_sq_weights = np.genfromtxt(mel_filter_file, delimiter=',')**2  #mel filter energies
	
	def compute_mfcc(self, input_frame):
		self.windowed_frame = input_frame * np.hamming(len(input_frame)) #Hamming Windowing input frame
		self.pre_frame = self.windowed_frame - self.alpha*np.concatenate((np.full(1, 0), self.windowed_frame[:-1])) #Preemphasis
		self.fft_frame = np.fft.rfft(self.pre_frame,self.N) #Computing FFT
		self.mel_frame = np.log(np.dot(self.mel_fb_sq_weights,(np.abs(self.fft_frame)**2)) + self.eps)  #Passing through mel and taking log
		self.mel_frame_normalized = self.mel_frame / np.sum(self.mel_fb_sq_weights, axis=1)     #normalizing by filter energies
		self.dct_frame = dct(self.mel_frame_normalized)     #Computing DCT 
		return self.dct_frame[0:13]    # Returning first 13 DCT coefficients

#temp = MFCC()
#y = temp.compute_mfcc(np.random.random(200))
#print(np.shape(y))
#print(y)
def test_mfcc_first_coefficient():
	temp = MFCC()
	no_of_test = 100
	input_matrix = np.random.random_sample((no_of_test,200))
	
	def first_coeff_greater_than_0(x):
		assert(x>0)
	
	for i in range(no_of_test):
		input_frame = input_matrix[i]
		coeffs = temp.compute_mfcc(input_frame)
		yield first_coeff_greater_than_0, coeffs[0]
