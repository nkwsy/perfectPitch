import serial
import math
import pyaudio
import wave
import random
import time

import sys
#### convert aif to wav in terminal using ffmpeg by typing:
###### for f in *.aiff; do ffmpeg -i "$f" "${f%.aiff}.wav"; done


def play(note, instrument):
	#define stream chunk   
	chunk = 1024  

	#open a wav format music  
	f = wave.open(r"/Users/me/projects/perfectpitch/" + instrument + "/" + note + ".wav","rb")  
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
############# tone randomizer
tone = ['2', '3', '4']
note = ['A', 'B', 'C', 'D']
instrument = []

###### Arduino ##################
arduinoSerialData = serial.Serial('/dev/cu.usbmodem1411', 9600)
x = 2

# a = 'Card UID: 04 17 9F 0A D7 49 80'
# b = 'Card UID: 04 3F 91 0A D7 49 80'
# c = 'Card UID: 04 3F DE 0A D7 49 80'
# d = 'Card UID: 04 29 83 0A D7 49 80'
# e = 'Card UID: 04 29 C2 0A D7 49 80'
# f = 'Card UID: 04 43 94 0A D7 49 80'
# g = 'Card UID: 04 4D D9 0A D7 49 80'
cards = {}
cards['a'] = 'Card UID: 04 17 9F 0A D7 49 80'
cards['b'] = 'Card UID: 04 3F 91 0A D7 49 80'
cards['c'] = 'Card UID: 04 3F DE 0A D7 49 80'
cards['d'] = 'Card UID: 04 29 83 0A D7 49 80'
cards['e'] = 'Card UID: 04 29 C2 0A D7 49 80'
cards['f'] = 'Card UID: 04 43 94 0A D7 49 80'
cards['g'] = 'Card UID: 04 4D D9 0A D7 49 80'


#cards = [a, b, c, d, e, f, g]
while x == 1 :
	if (arduinoSerialData.inWaiting()>0):

		myData = arduinoSerialData.readline()
		print myData

		myd = myData.splitlines()
		for item in myd:
			if item == a: 
				print 'A'
				play('A4', 'horn')
			if item == b: 
				print 'B'
				play('B4', 'horn')
			if item == c: 
				print 'C'
				play('C4', 'horn')
			if item == d: 
				print 'D'
				play('D4', 'horn')
			if item == e: 
				print 'E'
				play('E4', 'horn')
			if item == f: 
				print 'F'
				play('F4', 'horn')
			if item == g: 
			 	print 'G'
			 	play('G4', 'horn')


			else:
				print 'NONE'
win = True

while x == 2:

	#playC5()
	if (arduinoSerialData.inWaiting()>0):
		if win == True:
			currNote = random.choice(note)
			noteToPlay = currNote + random.choice(tone)
			print noteToPlay
			play( noteToPlay , 'horn')

			win = False
		elif win == False:

			myData = arduinoSerialData.readline()
			myd = myData.splitlines()  
			print 'What tone is that?'
			print 'Scan the proper card'
			#time.sleep(5)
			for item in myd:

				if item == cards[currNote.lower()]: 
					#print 'C'
					play( noteToPlay, 'horn')
					print 'great job \n !!!!!'
					win = True	

				# elif item in cards:
				# 	print 'tete'
				# return
				else:
					print 'NONE'

# while  x == 3:
# 	play(G4, horn)


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
