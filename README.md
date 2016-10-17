# HotWordDetection

1. Hotword - 'Maya'
Training:
1. Collect 10 samples of 'Maya'
2. Compute MFCC (25ms window and 10ms hop) and store

Testing:
1. Input chunks of 1 sec at 100ms hop (In real time)
2. Extract MFCC for chunks (25ms window and 10ms hop)
3. Apply DTW on input chunk and 'Maya' samples stored
4. Threshold DTW score
 
