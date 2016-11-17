==========================
Introduction
==========================

.. *Hotword* - `Maya`

.. Training:

.. 1. Collect 10 samples of 'Maya'
.. 2. Compute MFCC (25ms window and 10ms hop) and store

.. Testing:

.. 1. Input chunks of 1 sec at 100ms hop (In real time)
.. 2. Extract MFCC for chunks (25ms window and 10ms hop)
.. 3. Apply DTW on input chunk and 'Maya' samples stored
.. 4. Threshold DTW score

**What is Hotword Detection?**

Hotword detection refers to the task of detecting a predetermined target word from the input speech uttered by a user. In other words, given a speech segment uttered by a user, our job is to determine whether a particular word is present in this segment or not. This task is in itself a very challenging task due to the high variability in speech utterances across different speakers in terms of accents, speaking styles, speech rate etc. In this module, we have built an hotword detection system which can be used for a variety of applications such as to enable personal assistants like 'Cortana' and 'Siri'. Our module uses Dynamic Time Warping(DTW) algorithm to match the features of test utterances with the stored features of target word. 

**Module Features**

1. Mel Frequency Cepstral Coefficients(MFCC): Our feature extraction module extracts MFCC vectors from input speech utterance which are later used in pattern matching. An excellent tutorial on MFCC feature vectors can be found here: `MFCC tutorial by James Lyons <http://www.practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs/>`_

2. Choice of selecting any hotword: Our module is flexible in terms of hotword choice due to the presence of both training as well as testing functionality. Any hotword can be selected word during the training phase during which 10 utterances are used to generate target templates. During testing, utterances recorded from users are matched against these templates to determine presence/absence of hotword.

3. Variable sampling frequency support: No fixed sampling rate is set in our module.

4. Use of Voice Activity Detector(VAD) during recordings: Due to the ubiquitous presence of background noise while recording, a VAD based on energy is used to segment out the relevant speech parts which are then passed on for further processing.

5. Personalization using automatic DTW thresholding: 

**Installation**

This project is on pypi.

To install from pypi:: 

	pip install hotword_detection

	
From this repository::

	git clone https://github.com/sakethgsharma/HotWordDetection.git
	python setup.py install

**Prerequisites**

1. PortAudio: PortAudio is a free, cross-platform, open-source, audio I/O library. It provides a very simple API for recording and/or playing sounds using a simple callback function or a blocking read/write interface. Instructions on how to install PortAudio can be found at <http://portaudio.com/docs/v19-doxydocs/>

2. multimedia-jack package: To install this package in Ubuntu, use the following command::

	sudo apt-get install multimedia-jack
