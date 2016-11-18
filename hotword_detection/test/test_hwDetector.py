import sys
import os, random

sys.path.append(os.path.abspath('.'))

from hotword_detection import hwDetector as hd
import numpy as np

def test_hwDetector():
	htDet = hd.hwDetector()
	def checkTrue(x):
		assert x == True
	trainDir = "./train_audio"	
	for file_name in os.listdir(trainDir):
		if file_name.endswith(".wav"):
			TF = htDet.isHotword(trainDir + "/" + file_name)
			yield checkTrue, TF

if __name__=="__main__":
	test_hwDetector()
