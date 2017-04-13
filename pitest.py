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
from pp.py import bcolors


pi = "/home/pi/perfectPitch/sounds/"

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

x = 0
while mode == '1':

	
	welcome = 'Welcome to the perfect pitch workshop.\n If you reach level 10 you will be thought of as an amazing person\n If you are a baby well... congrats \n\n'
	rules = 'For each tone played you will place the corresponding block on the pad.\n If you get the answer correct you get a point. If you get it incorrect you loose a point.\n The game gets progressively harder the more points you get.\n '
	#######  MODES  ######

	##### Relitive mode, allows for reference tone to be played  
	relitiveMode = False

	#### Octive hints #####
	hints = False

	##### Repeating ######
	repeating = False

	##### Training mode #######
	training = False

	if x == 10:
		if training == True:
			level = -10
		else:
			level = 0


	### easy, same tone (4) and same instrument randomly picked ####
	while level == 0:
		print welcome
		time.sleep(1)
		print rules
		if relitiveMode == True:
			print 'This is a Flute playing C6'
			play( 'C4' , 'Flutenonvib')
		
		level += 1







