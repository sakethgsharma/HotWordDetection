======================
HotWord Detection
======================

This library provides functionality for detecting a hotword in given audio file using MFCC features and Dynamic Time Warping (DTW) pattern matching algorithm.

Installation
============

This `project is on pypi <https://pypi.python.org/pypi/hotword_detection/1.1>`_

To install from pypi:: 

	pip install hotword_detection

	
From this repository::

	git clone https://github.com/sakethgsharma/HotWordDetection.git


Usage
======

*Example scripts*

For training a hotword, run::
	
	python bin/trainHotword.py

For testing, run::
	
	python bin/checkHotword.py

*Supported features*

- Mel Frequency Cepstral Coefficients
- Choice of selecting any suitable hot word through appropriate training paradigm
- Supports variable sampling frequencies
- Amplitude based Voice Activity Detector(VAD) used during recordings to remove extraneous noise
- Personalization using automatic DTW thresholding

MFCC Features
=============

MFCC vectors are used in this module since they are the most commonly extracted features used for speech recognition systems. 

=============	===========	
Parameter 	Description	
=============	===========	
alpha		Parameter used in pre-emphasis filtering. Should be any value between 0 and 1.
N 		Number of FFT points.
fs 		Sampling frequency of stored audio file.
frame_dur	Duration of 1 speech frame.
num_filters	Number of filters used in the Mel filterbank.
lower_freq	Lower frequency bound used for constructing filterbank.
upper_freq	Upper frequency bound used for constructing filterbank. Should be less than fs/2.
=============	===========

Dynamic Time Warping
======================

Dynamic time warping (DTW) is an algorithm for measuring similarity between two temporal sequences which may vary in speed.

Reference
=========

`MFCC tutorial <http://www.practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs/>`_
`DTW Wiki <http://en.wikipedia.org/wiki/Dynamic_time_warping>`_
