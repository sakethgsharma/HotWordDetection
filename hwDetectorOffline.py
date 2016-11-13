import numpy as np
import scipy.io.wavfile as wv
import dtw
import mfcc

SAMPLING_RATE = 8000
CHANNEL_MONO = 1
MFCC_HOP_SAMPLES = int(SAMPLING_RATE*0.01)
MFCC_FRAME_LENGTH = int(SAMPLING_RATE*0.025)
INPUT = ["maya1","maya2","maya3","fake1","fake2","fake3","fake4"]
test_len = len(INPUT)
distance = np.zeros([test_len,test_len])

DTW_calculator =dtw.DTW()

for i in range(test_len):
	for j in range(test_len):
		(fs, data) = wv.read("./audio_maya/" + INPUT[i] + ".wav")
		num_frames = int(data.shape[0]/MFCC_FRAME_LENGTH)
		
		MFCC_calculator = mfcc.MFCC()
		MFCC_MATRIX = np.empty([39, num_frames])
		for k in range(num_frames):
			MFCC_MATRIX[:,k] = MFCC_calculator.compute_mfcc(data[k*MFCC_FRAME_LENGTH:(k+1)*MFCC_FRAME_LENGTH -1])

		(fs, data) = wv.read("./audio_maya/" + INPUT[j] + ".wav")
		num_frames = int(data.shape[0]/MFCC_FRAME_LENGTH)

		MFCC_calculator = mfcc.MFCC()
		MFCC_MATRIX2 = np.empty([39, num_frames])
		for k in range(num_frames):
		        MFCC_MATRIX2[:,k] = MFCC_calculator.compute_mfcc(data[k*MFCC_FRAME_LENGTH:(k+1)*MFCC_FRAME_LENGTH -1])

		distance[i,j] =DTW_calculator.compute_distance(np.transpose(MFCC_MATRIX),np.transpose(MFCC_MATRIX2))
#print(MFCC_MATRIX[:,0])
#print(MFCC_MATRIX2[:,0])

u_indices = distance > 10.7
l_indices = distance <= 10.7
distance[u_indices] = 0
distance[l_indices] = 1
print(distance)


