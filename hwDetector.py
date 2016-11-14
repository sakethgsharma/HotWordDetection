import numpy as np
import os
import scipy.io.wavfile as wv
import mfcc
import dtw

class hwDetector:
	def __init__(self, samplingFrequency = 8000, framePeriod = 25e-3, hopPeriod = 10e-3, trainDir="./train_audio/",thresh=9.5):
		self.samplingFrequency = samplingFrequency
		self.framePeriod = framePeriod
		self.hopPeriod = hopPeriod
		self.trainDir = trainDir
		self.thresh = thresh
		self.hopLength = int(samplingFrequency * hopPeriod)
		self.frameLength = int(samplingFrequency * framePeriod)
		self.referenceMFCC = []
		for file_name in os.listdir(trainDir):
			if file_name.endswith(".wav"):
				print(file_name)
				(fs, data) = wv.read(trainDir + file_name)
				num_frames = int(data.shape[0]/self.hopLength) - int(np.ceil(self.frameLength/self.hopLength))

				MFCC_calculator = mfcc.MFCC()
				MFCC_MATRIX = np.empty([39, num_frames])
				for k in range(num_frames):
					MFCC_MATRIX[:,k] = MFCC_calculator.compute_mfcc(data[k*self.hopLength : k*self.hopLength + self.frameLength])
				self.referenceMFCC.append(MFCC_MATRIX)
#		print(self.referenceMFCC[-1][:,0])	
#		print(len(self.referenceMFCC))

	def distance(self, fileName):
		DTW_calculator = dtw.DTW()
		(fs, data) = wv.read(fileName)
		num_frames = int(data.shape[0]/self.hopLength) - int(np.ceil(self.frameLength/self.hopLength))

		MFCC_calculator = mfcc.MFCC()
		MFCC_MATRIX = np.empty([39, num_frames])
		for k in range(num_frames):
			MFCC_MATRIX[:,k] = MFCC_calculator.compute_mfcc(data[k*self.hopLength : k*self.hopLength + self.frameLength])

		distance_list = [DTW_calculator.compute_distance(np.transpose(matrix),np.transpose(MFCC_MATRIX)) for matrix in self.referenceMFCC]
		return distance_list

	def isHotword(self,fileName):
		distances = self.distance(fileName)
		for dist in distances:
			if(dist < self.thresh):
				return True
		return False

hDetect = hwDetector()
print(hDetect.isHotword("./fake_audio/fake2.wav"))

