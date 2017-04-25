import sys
import tkinter
import winsound
import time
a=time.time()
for i in range(1000000):
    i*3.14; i/23.3
b=time.time()
print (b-a)
winsound.Beep(3200,100)
winsound.Beep(1200,100)