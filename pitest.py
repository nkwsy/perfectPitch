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
hints = False


####### RFID UTIL  ##########
def rfidread(targetTag):

    run = True
    rdr = RFID()
    util = rdr.util()
    util.debug = True

    rdr.wait_for_tag()

    (error, data) = rdr.request()
    if not error:
        print("\nDetected: " + format(data, "02x"))

    (error, uid) = rdr.anticoll()
    if not error:
        tag = (str(uid[2])+str(uid[3]))
        print(str(uid[2])+str(uid[3]))
        
        if targetTag == tag:
            print 'TRUE'
            win = True
        else:
            print 'False'
            win = False

    time.sleep(1)


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
cards['A'] = '23159'
cards['Ab'] = '4598'
cards['B'] = '63145'
cards['Bb'] = '5691'
cards['C'] = '63222'
cards['D'] = '41131'
cards['Db'] = 'XXXX'
cards['E'] = '41194'
cards['Eb'] = 'XXXX'
cards['F'] = '67148'
cards['G'] = '77217'
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
	

	instrumentToPlay = 'Flutenonvib'
	toneToPlay = '4'
	#playC5()
	play( 'C4' , instrumentToPlay)


	if hints == True:
		print toneToPlay



	rfidread(cards['C'])
	if win == True:
		print "FUCK YEAH!!!"
	if win == False:
		print bcolors.FAIL + random.choice(insult) + bcolors.ENDC






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