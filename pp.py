import serial
import math
import pyaudio
import wave

import sys


def playA5():
	#define stream chunk   
	chunk = 1024  

	#open a wav format music  
	f = wave.open(r"/Users/me/projects/perfectpitch/Piano.ff.A5.wav","rb")  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
	                channels = f.getnchannels(),  
	                rate = f.getframerate(),  
	                output = True)  
	#read data  
	data = f.readframes(chunk)  

	#play stream  
	while data:  
	    stream.write(data)  
	    data = f.readframes(chunk)  

	#stop stream  
	stream.stop_stream()  
	stream.close()  

	#close PyAudio  
	p.terminate()

def playB5():
	#define stream chunk   
	chunk = 1024  

	#open a wav format music  
	f = wave.open(r"/Users/me/projects/perfectpitch/Piano.ff.B5.wav","rb")  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
	                channels = f.getnchannels(),  
	                rate = f.getframerate(),  
	                output = True)  
	#read data  
	data = f.readframes(chunk)  

	#play stream  
	while data:  
	    stream.write(data)  
	    data = f.readframes(chunk)  

	#stop stream  
	stream.stop_stream()  
	stream.close()  

	#close PyAudio  
	p.terminate()  

def playC5():
	#define stream chunk   
	chunk = 1024  

	#open a wav format music  
	f = wave.open(r"/Users/me/projects/perfectpitch/Piano.ff.C5.wav","rb")  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
	                channels = f.getnchannels(),  
	                rate = f.getframerate(),  
	                output = True)  
	#read data  
	data = f.readframes(chunk)  

	#play stream  
	while data:  
	    stream.write(data)  
	    data = f.readframes(chunk)  

	#stop stream  
	stream.stop_stream()  
	stream.close()  

	#close PyAudio  
	p.terminate()  

def playD5():
	#define stream chunk   
	chunk = 1024  

	#open a wav format music  
	f = wave.open(r"/Users/me/projects/perfectpitch/Piano.ff.D5.wav","rb")  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
	                channels = f.getnchannels(),  
	                rate = f.getframerate(),  
	                output = True)  
	#read data  
	data = f.readframes(chunk)  

	#play stream  
	while data:  
	    stream.write(data)  
	    data = f.readframes(chunk)  

	#stop stream  
	stream.stop_stream()  
	stream.close()  

	#close PyAudio  
	p.terminate()  

def playE5():
	#define stream chunk   
	chunk = 1024  

	#open a wav format music  
	f = wave.open(r"/Users/me/projects/perfectpitch/Piano.ff.E5.wav","rb")  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
	                channels = f.getnchannels(),  
	                rate = f.getframerate(),  
	                output = True)  
	#read data  
	data = f.readframes(chunk)  

	#play stream  
	while data:  
	    stream.write(data)  
	    data = f.readframes(chunk)  

	#stop stream  
	stream.stop_stream()  
	stream.close()  

	#close PyAudio  
	p.terminate()  

def playF5():
	#define stream chunk   
	chunk = 1024  

	#open a wav format music  
	f = wave.open(r"/Users/me/projects/perfectpitch/Piano.ff.F5.wav","rb")  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
	                channels = f.getnchannels(),  
	                rate = f.getframerate(),  
	                output = True)  
	#read data  
	data = f.readframes(chunk)  

	#play stream  
	while data:  
	    stream.write(data)  
	    data = f.readframes(chunk)  

	#stop stream  
	stream.stop_stream()  
	stream.close()  

	#close PyAudio  
	p.terminate()  

def playG5():
	#define stream chunk   
	chunk = 1024  

	#open a wav format music  
	f = wave.open(r"/Users/me/projects/perfectpitch/Piano.ff.G5.wav","rb")  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
	                channels = f.getnchannels(),  
	                rate = f.getframerate(),  
	                output = True)  
	#read data  
	data = f.readframes(chunk)  

	#play stream  
	while data:  
	    stream.write(data)  
	    data = f.readframes(chunk)  

	#stop stream  
	stream.stop_stream()  
	stream.close()  

	#close PyAudio  
	p.terminate()  
#playA5()

arduinoSerialData = serial.Serial('/dev/cu.usbmodem1411', 9600)
x = 1

a = 'Card UID: 04 17 9F 0A D7 49 80'
b = 'Card UID: 04 3F 91 0A D7 49 80'
c = 'Card UID: 04 3F DE 0A D7 49 80'
d = 'Card UID: 04 29 83 0A D7 49 80'
e = 'Card UID: 04 29 C2 0A D7 49 80'
f = 'Card UID: 04 43 94 0A D7 49 80'
g = 'Card UID: 04 4D D9 0A D7 49 80'
while x == 1 :
	if (arduinoSerialData.inWaiting()>0):

		myData = arduinoSerialData.readline()
		print myData
		# myd = myData.split()
		# print myd[2:8]
		# uid = myd[2:8]
		myd = myData.splitlines()
		# print myd
		for item in myd:
			if item == a: 
				print 'A'
				playA5()
			if item == b: 
				print 'B'
				playB5()				
			if item == c: 
				print 'C'
				playC5()			
			if item == d: 
				print 'D'
				playD5()
			if item == e: 
				print 'E'
				playE5()
			if item == f: 
				print 'F'
				playF5()
			if item == g: 
				print 'G'
				playG5()


			else:
				print 'NONE'




# PyAudio = pyaudio.PyAudio
# BITRATE = 16000 #number of frames per second/frameset.      
# FREQUENCY = 261.63 #Hz, waves per second, 261.63=C4-note.
# LENGTH = 3 #seconds to play sound

# NUMBEROFFRAMES = int(BITRATE * LENGTH)
# RESTFRAMES = NUMBEROFFRAMES % BITRATE
# WAVEDATA = ''    


# for x in xrange(NUMBEROFFRAMES):
#  WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

# #fill remainder of frameset with silence
# for x in xrange(RESTFRAMES): 
#  WAVEDATA = WAVEDATA+chr(128)

# p = PyAudio()
# stream = p.open(format = p.get_format_from_width(1), 
#                 channels = 1, 
#                 rate = BITRATE, 
#                 output = True)
# stream.write(WAVEDATA)
# stream.stop_stream()
# stream.close()
# p.terminate()

		