import numpy as np
import os
import scipy.io.wavfile as wv
import mfcc
import dtw

class hwDetector:
	def __init__(self, samplingFrequency = 8000, framePeriod = 25e-3, hopPeriod = 10e-3, trainDir="./train_audio/",thresh=6):
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
				(fs, data) = wv.read(trainDir + file_name)
				num_frames = int(data.shape[0]/self.hopLength) - int(np.ceil(self.frameLength/self.hopLength))

				MFCC_calculator = mfcc.MFCC()
				MFCC_MATRIX = np.empty([39, num_frames])
				for k in range(num_frames):
					MFCC_MATRIX[:,k] = MFCC_calculator.compute_mfcc(data[k*self.hopLength : k*self.hopLength + self.frameLength])
				self.referenceMFCC.append(MFCC_MATRIX)

		DTW_calculator = dtw.DTW()
		distance_list = [DTW_calculator.compute_distance(np.transpose(matrix),np.transpose(matrix2)) for matrix in self.referenceMFCC for matrix2 in self.referenceMFCC]
		self.thresh = np.mean(np.array((distance_list)))*1.2

	def distance(self, fileName):
		DTW_calculator = dtw.DTW()
		(fs, data) = wv.read(fileName)
		num_frames = int(data.shape[0]/self.hopLength) - int(np.ceil(self.frameLength/self.hopLength))
		if num_frames<=0:
			return 10000

		MFCC_calculator = mfcc.MFCC()
		MFCC_MATRIX = np.empty([39, num_frames])
		for k in range(num_frames):
			MFCC_MATRIX[:,k] = MFCC_calculator.compute_mfcc(data[k*self.hopLength : k*self.hopLength + self.frameLength])

		distance_list = [DTW_calculator.compute_distance(np.transpose(matrix),np.transpose(MFCC_MATRIX)) for matrix in self.referenceMFCC]
		return distance_list

	def isHotword(self,fileName):
		distances = np.array(self.distance(fileName))
		mean_dist = np.mean(distances)
		if (mean_dist < self.thresh):
			return True
		return False

