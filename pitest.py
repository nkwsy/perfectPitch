import math
import pyaudio
import wave
import random
import time
import multiprocessing
from pirc522 import RFID
import signal
import time
import sys
from assets import bcolors


pi = "/home/pi/perfectPitch/sounds/"

#RFID 
rdr = RFID()
util = rdr.util()
# Set util debug to true - it will print what's going on
util.debug = True

win = False
def play(note, instrument):
	#define stream chunk   
	chunk = 1024  

	#open a wav format music  
	f = wave.open(r"/home/pi/perfectPitch/sounds/" + instrument + "/" + note + ".wav","rb")  
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

def assess(item, currNote, instrumentToPlay, score):
	if item == cards[currNote]: 
		#print 'C'
		play( noteToPlay, instrumentToPlay)
		print bcolors.WARNING + 'great job \n !!!!!' + bcolors.ENDC
		print noteToPlay
		win = True	
		#score += 1
		return True

	elif item in cards.values():

		#score -= 1
		print bcolors.FAIL + random.choice(insult) + bcolors.ENDC
		print bcolors.BOLD + 'Try Again!\n' + bcolors.ENDC
		print 'this is the' +item
		return 'wrong'				
	else:

		return False

############# tone randomizer
sounds = {}
sounds['horn'] = ['2', '3', '4']
sounds['AltoFluteVib'] = [ '4', '5']
sounds['AltoSaxNoVib'] = [ '4']
sounds['AltoSaxvib'] = ['3', '4']
sounds['BassClarinet'] = ['3','4','5']
sounds['BassFlute'] = ['3','4','5']
sounds['Bassoon'] = ['2','4']
sounds['BbClarinet'] = ['4','5','6']
sounds['EbClarinet'] = ['4','5','6']
sounds['Flutenonvib'] = ['4','5','6']
sounds['SopSax'] = ['4','5']
sounds['SopSaxVib'] = ['4','5']
sounds['trumpet'] = ['4','5']

tone = ['2', '3', '4']
note = ['A', 'Ab', 'B', 'Bb', 'C', 'D', 'E', 'F','G']
 #['A', 'Ab' 'B', 'Bb', 'C', 'D', 'Db',  'E', 'Eb',  'F','G', 'Gb']
instrument = ['AltoFluteVib', 'AltoSaxNoVib', 'AltoSaxvib', 'BassClarinet', 'BassFlute', 'Bassoon', 'BbClarinet', 'EbClarinet', 'EbClarinet']

insult = ['YOU SUCK','YOUR A LOSER', 'TONE DEF IDIOT', 'MELLON TELLER!!', 'you are useless', 'I have never met anyone more disapointing than you']


cards = {}
cards['A'] = 'Card UID: 04 17 9F 0A D7 49 80'
cards['Ab'] = 'Card UID: 04 2D 62 0A D7 49 80'
cards['B'] = 'Card UID: 04 3F 91 0A D7 49 80'
cards['Bb'] = 'Card UID: 04 38 5B 0A D7 49 80'
cards['C'] = 'Card UID: 04 3F DE 0A D7 49 80'
cards['D'] = 'Card UID: 04 29 83 0A D7 49 80'
cards['Db'] = 'XXXX'
cards['E'] = 'Card UID: 04 29 C2 0A D7 49 80'
cards['Eb'] = 'XXXX'
cards['F'] = 'Card UID: 04 43 94 0A D7 49 80'
cards['G'] = 'Card UID: 04 4D D9 0A D7 49 80'
cards['Gb'] = 'XXXX'



# x = input('Enter dificulty level 1-5 :')
score = 0
mode = input('Enter mode 1= Beginer, 2= Tone training 3= beast mode 4= Practice  :')


while mode == '4' :
	currNote = random.choice(note)
	instrumentToPlay = random.choice(sounds.keys())
	toneToPlay = random.choice(sounds[instrumentToPlay])
	noteToPlay = currNote + toneToPlay
	print currNote
	print instrumentToPlay
	print toneToPlay
	print noteToPlay

	print bcolors.HEADER + instrumentToPlay + ' in ' + bcolors.BOLD + noteToPlay + bcolors.ENDC

	#instrumentToPlay = random.choice(instrument)	
	#print noteToPlay
	play( noteToPlay , instrumentToPlay)




while mode == 1:
	rdr.wait_for_tag()
	# Request tag
	(error, data) = rdr.request()
	# print toneToPlay
	instrumentToPlay = 'Flutenonvib'
	toneToPlay = '4'
	#playC5()
	play( 'C4' , instrumentToPlay)

	#myData = (error, data) = 
	myData = rdr.request()
	print data
	if not error:
		print("\nDetected")
		(error, uid) = rdr.anticoll()
		#if not error:
		# Print UID
		util.read_out(4)
		print util.read_out(4)
		#print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))

		#print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
		# if win == True:

		# 	##### Use tone 
		# 	currNote = random.choice(note)
		# 	noteToPlay = currNote + toneToPlay
		# 	# instrumentToPlay = random.choice(instrument)
		# 	print noteToPlay
		# 	if correct == True:
		# 		score += 1
		# 		print 'Your score is  ' + str(score)
		# 	if correct == False:
		# 		correct = True
		# 	if score == 10:
		# 		level = 2
		# 	if score < -5:
		# 		score = 0
		# 	if score < 10:
		# 		play( noteToPlay , 'Flutenonvib')
		# 		win = False
		# 	score += 1
		# 	print 'Your score is  ' + str(score)
		# 	play( noteToPlay , instrumentToPlay)

		# 	win = False
		# 	print bcolors.BOLD + 'What tone is that?' + bcolors.ENDC
		# 	print bcolors.HEADER +'Scan the proper card' + bcolors.ENDC
		# elif win == 'wrong':
		# 	score -= 1
		# 	win = False
		# elif win == False:

		# 	myd = myData.splitlines(data)  
		# 	for item in myd:
		# 		win = assess(item, currNote, instrumentToPlay, score)