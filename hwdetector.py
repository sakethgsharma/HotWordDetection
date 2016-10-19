import alsaaudio
import numpy as np
import thread

SAMPLING_RATE = 8000
CHANNEL_MONO = 1
MFCC_HOP_SAMPLES = int(SAMPLING_RATE*0.01)
MFCC_FRAME_LENGTH = int(SAMPLING_RATE*0.025)

print(MFCC_FRAME_LENGTH)

def acquire_input():
	input_buffer = np.zeros(shape=MFCC_FRAME_LENGTH)
        while True:
		l,data = input_device.read()
		if l:
			input_array = np.fromstring(data,dtype=np.float32)
			input_buffer = np.roll(input_buffer,-MFCC_HOP_SAMPLES)
			input_buffer[-MFCC_HOP_SAMPLES:] = input_array
			output_device.write(input_array.tostring())

input_device = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NORMAL)
input_device.setchannels(CHANNEL_MONO)
input_device.setrate(SAMPLING_RATE)
input_device.setformat(alsaaudio.PCM_FORMAT_FLOAT_LE)
input_device.setperiodsize(MFCC_HOP_SAMPLES)

output_device = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, alsaaudio.PCM_NORMAL)
output_device.setchannels(CHANNEL_MONO)
output_device.setrate(SAMPLING_RATE)
output_device.setformat(alsaaudio.PCM_FORMAT_FLOAT_LE)
output_device.setperiodsize(MFCC_HOP_SAMPLES)

try:
	thread.start_new_thread(acquire_input,())
except:
	print("Error: unable to start thread")

while True:
#	print(np.max(input_buffer))
	pass
