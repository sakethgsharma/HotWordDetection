import wordRecorder as wr
import hwDetector as hd

wrdRec = wr.wordRecorder()
hwDet = hd.hwDetector()

print("Speak a word")
wrdRec.record2File("demo.wav")
print(hwDet.isHotword("demo.wav"))
