======================
HotWord Detection
======================

This library provides functionality for detecting a hotword in given audio file using MFCC features and Dynamic Time Warping (DTW) pattern matching algorithm.
If you are not sure what MFCCs are, and would like to know more have a look at this 
`MFCC tutorial <http://www.practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs/>`_

Installation
============

This `project is on pypi <https://pypi.python.org/pypi/python_speech_features>`_

To install from pypi:: 

	pip install hotword_detection

	
From this repository::

	git clone https://github.com/sakethgsharma/HotWordDetection.git
	python setup.py install


Usage
=====

Supported features:

- Mel Frequency Cepstral Coefficients
- Choice of selecting any suitable hot word
- Supports variable sampling frequencies
- Personalization using automatic DTW thresholding

MFCC Features
=============

The default parameters should work fairly well for most cases.
	
=============	===========	==============
Parameter 	Description	Default Value
=============	===========	==============
alpha			Parameter used in pre-emphasis filtering. Should be any value between 0 and 1.	0.95
N 			Number of FFT points.	256
fs 			Sampling frequency of stored audio file.	8000
frame_dur		Duration of 1 speech frame	25 ms
num_filters		Number of filters used in the Mel filterbank	23
lower_freq		Lower frequency bound used for constructing filterbank	300
upper_freq		Upper frequency bound used for constructing filterbank. Should be less than fs/2	3800
=============	===========	================

Dynamic Time Warping
======================


Reference
=========
