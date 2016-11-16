import numpy as np
from scipy.fftpack import dct
import time
import timeit

class MFCC:
	def __init__(self, alpha=0.95, N=256, fs=8000, eps=10e-6, frame_dur=0.025):
		self.alpha = alpha   #Preemphasis parameter
		self.N = N	     # No of FFT points	
		self.eps = eps       # eps to avoid mathematical errors
		self.fs = fs
		self.mfcc_frame_length = round(fs*frame_dur)  #frame length for mfcc
		self.prev_frame = np.zeros((14,))
		self.prev_prev_frame = np.zeros((14,))

	def generate_filter_bank(self, num_filters=23, lower_freq=300, upper_freq=3800):
		"""Compute a Mel-filterbank. The filters are stored in the rows, the columns correspond
    		to fft bins. The filters are returned as an array of size nfilt * (nfft/2 + 1)
    		"""
    		self.highfreq = upper_freq
    		assert self.highfreq <= self.fs/2, "highfreq is greater than samplerate/2"
    
    		# compute points evenly spaced in mels
    		self.lowmel = self.hz2mel(lower_freq)
    		self.highmel = self.hz2mel(upper_freq)
    		self.melpoints = np.linspace(self.lowmel,self.highmel,num_filters+2)
    		self.bin = np.floor((self.N+1)*self.mel2hz(self.melpoints)/self.fs)

		self.fbank = np.zeros([num_filters,self.N/2+1])
    		for j in range(0,num_filters):
        		for i in range(int(self.bin[j]), int(self.bin[j+1])):
            			self.fbank[j,i] = (i - self.bin[j]) / (self.bin[j+1]-self.bin[j])
        		for i in range(int(self.bin[j+1]), int(self.bin[j+2])):
            			self.fbank[j,i] = (self.bin[j+2]-i) / (self.bin[j+2]-self.bin[j+1])
		return self.fbank
		
		
	def hz2mel(self, hz):
    		return 2595 * np.log10(1+hz/700.0)
    
	def mel2hz(self, mel):
    		return 700*(10**(mel/2595.0)-1)
	
	def compute_mfcc(self, input_frame, include_dc=False):
		self.windowed_frame = input_frame * np.hamming(len(input_frame)) #Hamming Windowing input frame
		self.pre_frame = self.windowed_frame - self.alpha*np.concatenate((np.full(1, 0), self.windowed_frame[:-1])) #Preemphasis
		self.fft_frame = np.fft.rfft(self.pre_frame,self.N) #Computing FFT
		self.mel_fb_sq_weights = self.generate_filter_bank()**2
		self.mel_frame = np.log(np.dot(self.mel_fb_sq_weights,(np.abs(self.fft_frame)**2)) + self.eps)  #Passing through mel and taking log
		self.mel_frame_normalized = self.mel_frame / np.sum(self.mel_fb_sq_weights, axis=1)     #normalizing by filter energies
		self.dct_frame = dct(self.mel_frame_normalized)     #Computing DCT 
		self.delta = self.dct_frame[0:14] - self.prev_frame
		self.double_delta = self.dct_frame[0:14] - self.prev_prev_frame
		self.coeffs = np.append(self.dct_frame[0:14], [self.delta[1:14], self.double_delta[1:14]])
		self.prev_prev_frame = self.prev_frame
		self.prev_frame = self.dct_frame[0:14]
		if (include_dc):
			return self.coeffs  	# Returning 39 MFCC coefficients
		else:
			return self.coeffs[1:40]

#temp = MFCC()
#y = temp.compute_mfcc(np.random.random(200))
#fbank = temp.generate_filter_bank()
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
		coeffs = temp.compute_mfcc(input_frame, include_dc=True)
		yield first_coeff_greater_than_0, coeffs[0]
