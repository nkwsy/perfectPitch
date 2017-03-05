import serial
import math
import pyaudio
import wave
import random
import time
# import multiprocessing

import sys
#### convert aif to wav in terminal using ffmpeg by typing:
###### for f in *.aif; do ffmpeg -i "$f" "${f%.aiff}.wav"; done

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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

sounds = {}
sounds['horn'] = ['2', '3', '4']
sounds['AltoFluteVib'] = ['3', '4', '5']
sounds['AltoSaxNoVib'] = ['3', '4']
sounds['AltoSaxvib'] = ['3', '4']
sounds['BassClarinet'] = ['2','3','4','5']
sounds['BassFlute'] = ['3','4','5']
sounds['Bassoon'] = ['2','3','4']
sounds['BbClarinet'] = ['3','4','5','6']
sounds['EbClarinet'] = ['3','4','5','6']
sounds['Flutenonvib'] = ['4','5','6']
sounds['SopSax'] = ['3','4','5']
sounds['SopSaxVib'] = ['3','4','5']
sounds['trumpet'] = ['3','4','5']

tone = ['2', '3', '4']
note = ['A', 'Ab' 'B', 'Bb', 'C', 'D', 'Db',  'E', 'Eb',  'F','G', 'Gb']
instrument = ['AltoFluteVib', 'AltoSaxNoVib', 'AltoSaxvib', 'BassClarinet', 'BassFlute', 'Bassoon', 'BbClarinet', 'EbClarinet', 'EbClarinet']

###### Arduino ##################
arduinoSerialData = serial.Serial('/dev/cu.usbmodem1411', 9600)
# x = input('Enter dificulty level 1-5 :')

# a = 'Card UID: 04 17 9F 0A D7 49 80'
# b = 'Card UID: 04 3F 91 0A D7 49 80'
# c = 'Card UID: 04 3F DE 0A D7 49 80'
# d = 'Card UID: 04 29 83 0A D7 49 80'
# e = 'Card UID: 04 29 C2 0A D7 49 80'
# f = 'Card UID: 04 43 94 0A D7 49 80'
# g = 'Card UID: 04 4D D9 0A D7 49 80'
cards = {}
cards['A'] = 'Card UID: 04 17 9F 0A D7 49 80'
cards['Ab'] = ''
cards['B'] = 'Card UID: 04 3F 91 0A D7 49 80'
cards['Bb'] = ''
cards['C'] = 'Card UID: 04 3F DE 0A D7 49 80'
cards['D'] = 'Card UID: 04 29 83 0A D7 49 80'
cards['Db'] = ''
cards['E'] = 'Card UID: 04 29 C2 0A D7 49 80'
cards['Eb'] = ''
cards['F'] = 'Card UID: 04 43 94 0A D7 49 80'
cards['G'] = 'Card UID: 04 4D D9 0A D7 49 80'
cards['Gb'] = ''

x = 4
#cards = [a, b, c, d, e, f, g]
while x == 1 :
	if (arduinoSerialData.inWaiting()>0):

		myData = arduinoSerialData.readline()
		print myData

		myd = myData.splitlines()
		for item in myd:
			if item == cards['a']: 
				print 'A'
				play('A4', 'horn')
			if item == cards['b']: 
				print 'B'
				play('B4', 'horn')
			if item == cards['c']: 
				print 'C'
				play('C4', 'horn')
			if item == cards['d']: 
				print 'D'
				play('D4', 'horn')
			if item == cards['e']: 
				print 'E'
				play('E4', 'horn')
			if item == cards['f']: 
				print 'F'
				play('F4', 'horn')
			if item == cards['g']: 
			 	print 'G'
			 	play('G4', 'horn')


			else:
				print 'NONE'
win = True
toneToPlay = random.choice(tone)
### easy, same tone and instrument ####
while x == 2:
	
	instrumentToPlay = random.choice(sounds.keys())

	#playC5()
	if (arduinoSerialData.inWaiting()>0):
		if win == True:
			currNote = random.choice(note)
			noteToPlay = currNote + toneToPlay
			instrumentToPlay = random.choice(instrument)
			#print noteToPlay
			play( noteToPlay , instrumentToPlay)

			win = False
			print bcolors.BOLD + 'What tone is that?' + bcolors.ENDC
			print bcolors.HEADER +'Scan the proper card' + bcolors.ENDC
		elif win == False:

			myData = arduinoSerialData.readline()
			myd = myData.splitlines()  

			#time.sleep(5)
			for item in myd:

				if item == cards[currNote]: 
					#print 'C'
					play( noteToPlay, 'horn')
					print bcolors.WARNING + 'great job \n !!!!!' + bcolors.ENDC
					print noteToPlay
					win = True	

				# elif item in cards:
				# 	print 'tete'
				# return
				else:
					number = random.randint(1, 30)
					if number == 1:
						print bcolors.WARNING + 'YOU SUCK\n' + bcolors.ENDC
					if number == 2:
						print bcolors.FAIL + 'YOUR A LOOSER\n' + bcolors.ENDC
					if number == 3:
						print bcolors.UNDERLINE + 'TONE DEF IDIOT\n' + bcolors.ENDC
					if number == 4:	
						print bcolors.FAIL + 'MELLON TELLER!!\n' + bcolors.ENDC
					if number == 5:
						print bcolors.HEADER + 'Try Again!\n' + bcolors.ENDC

### Medium 
while x == 3:
	instrumentToPlay = random.choice(instrument)
	#playC5()
	if (arduinoSerialData.inWaiting()>0):
		if win == True:
			currNote = random.choice(note)
			noteToPlay = currNote + random.choice(tone)
	
			#print noteToPlay
			play( noteToPlay , instrumentToPlay)

			win = False
			print bcolors.BOLD + 'What tone is that?' + bcolors.ENDC
			print bcolors.HEADER +'Scan the proper card' + bcolors.ENDC
		elif win == False:

			myData = arduinoSerialData.readline()
			myd = myData.splitlines()  

			#time.sleep(5)
			for item in myd:

				if item == cards[currNote.lower()]: 
					#print 'C'
					play( noteToPlay, 'horn')
					print bcolors.WARNING + 'great job \n !!!!!' + bcolors.ENDC
					print noteToPlay
					win = True	

				# elif item in cards:
				# 	print 'tete'
				# return
				else:
					number = random.randint(1, 30)
					if number == 1:
						print bcolors.WARNING + 'YOU SUCK\n' + bcolors.ENDC
					if number == 2:
						print bcolors.FAIL + 'YOUR A LOOSER\n' + bcolors.ENDC
					if number == 3:
						print bcolors.UNDERLINE + 'TONE DEF IDIOT\n' + bcolors.ENDC
					if number == 4:	
						print bcolors.FAIL + 'MELLON TELLER!!\n' + bcolors.ENDC
					if number == 5:
						print bcolors.HEADER + 'Try Again!\n' + bcolors.ENDC


### Hard 
while x == 4:

	#playC5()
	if (arduinoSerialData.inWaiting()>0):
		if win == True:
			currNote = random.choice(note)
			instrumentToPlay = random.choice(sounds.keys())
			toneToPlay = random.choice(sounds[instrumentToPlay])
			noteToPlay = currNote + toneToPlay
			

			#instrumentToPlay = random.choice(instrument)	
			#print noteToPlay
			play( noteToPlay , instrumentToPlay)

			win = False
			print bcolors.BOLD + 'What tone is that?' + bcolors.ENDC
			print bcolors.HEADER +'Scan the proper card' + bcolors.ENDC
		elif win == False:

			myData = arduinoSerialData.readline()
			myd = myData.splitlines()  

			#time.sleep(5)
			for item in myd:

				if item == cards[currNote]: 
					#print 'C'
					play( noteToPlay, 'horn')
					print bcolors.WARNING + 'great job \n !!!!!' + bcolors.ENDC
					print noteToPlay
					win = True	

				# elif item in cards:
				# 	print 'tete'
				# return
				else:
					number = random.randint(1, 30)
					if number == 1:
						print bcolors.WARNING + 'YOU SUCK\n' + bcolors.ENDC
					if number == 2:
						print bcolors.FAIL + 'YOUR A LOOSER\n' + bcolors.ENDC
					if number == 3:
						print bcolors.UNDERLINE + 'TONE DEF IDIOT\n' + bcolors.ENDC
					if number == 4:	
						print bcolors.FAIL + 'MELLON TELLER!!\n' + bcolors.ENDC
					if number == 5:
						print bcolors.HEADER + 'Try Again!\n' + bcolors.ENDC
#todo add easy modes, start with 2 diff notes, then progresively add note, then add octives with prompt on which its in. then remove prompt. then add diff instruments, the
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
