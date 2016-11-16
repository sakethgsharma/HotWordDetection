import pyaudio
from array import array
import wave,sys
from struct import pack
fsock = open('out.log', 'w')
sys.stderr = fsock
class wordRecorder:
	def __init__(self, samplingFrequency = 8000, threshold = 14000):
		self.samplingFrequency = samplingFrequency
		self.threshold = threshold
	
	def isSilent(self, data):
	    return max(data) < self.threshold

	def normalize(self, data):
        	maxShort = 16384
    		scale = float(maxShort)/max(abs(i) for i in data)

		r = array('h')
    		for i in data:
        		r.append(int(i*scale))
    		return r

	def trimWord(self, data):
    		def trimStart(data):
        		snd_started = False
        		r = array('h')

        		for i in data:
				if not snd_started and abs(i)>self.threshold:
                			snd_started = True
                			r.append(i)

            			elif snd_started:
                			r.append(i)
        		return r

		data = trimStart(data)
		data.reverse()
		data = trimStart(data)
		data.reverse()
		return data

	def record(self):
    		p = pyaudio.PyAudio()
		stream = p.open(format=pyaudio.paInt16, channels=1, rate=self.samplingFrequency, input=True, output=False, frames_per_buffer=1024)

		num_silent = 0
		snd_started = False
		
		r = array('h')

		for i in range(int(self.samplingFrequency*2/1024)):
        		snd_data = array('h', stream.read(1024))
        		r.extend(snd_data)
		
		sample_width = p.get_sample_size(pyaudio.paInt16)
    		stream.stop_stream()
		stream.close()
		p.terminate()

    		r = self.normalize(r)
    		r = self.trimWord(r)
    		return sample_width, r

	def record2File(self, path):
    		sample_width, data = self.record()
    		data = pack('<' + ('h'*len(data)), *data)

		wf = wave.open(path, 'wb')
		wf.setnchannels(1)
		wf.setsampwidth(sample_width)
		wf.setframerate(self.samplingFrequency)
		wf.writeframes(data)
		wf.close()

