import sys
import os

sys.path.append(os.path.abspath('.'))
from hotword_detection import wordRecorder as wr
from hotword_detection import hwDetector as hd

wrdRec = wr.wordRecorder()
hwDet = hd.hwDetector()

print("Speak a word")
wrdRec.record2File("demo.wav")
print(hwDet.isHotword("demo.wav"))
