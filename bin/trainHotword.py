import sys
import os

if not (os.path.exists('./train_audio')):
	os.mkdir('./train_audio')
sys.path.append(os.path.abspath('./hotword_detection'))
import wordRecorder as wr
import time

wRec = wr.wordRecorder()
filelist = [ f for f in os.listdir("./train_audio/") if f.endswith(".wav") ]
for f in filelist:
    os.remove("./train_audio/" + f)
print("Record hotword instances...")
for i in range(10):
	print("Sample" + str(i))
	wRec.record2File("./train_audio/" + str(int(time.time())) + ".wav")

