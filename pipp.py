#import serial
import math
import pyaudio
import wave
import random
import time
import multiprocessing
#import psycopg2

from pirc522 import RFID
import signal
import time

# #Define our connection string	
# conn_string = "host='ec2-54-225-182-108.compute-1.amazonaws.com' dbname='dn7gu1epio9d7' user='arwewokxwekuka' port='5432' password='5d98586ca671123e05b3e11dcc22fa59790fbffdb9476550af9ced849d19e507'"
# # print the connection string we will use to connect
# print "Connecting to database\n	->%s" % (conn_string)
# # get a connection, if a connect cannot be made an exception will be raised here
# conn = psycopg2.connect(conn_string)


home = "/Users/me/projects/perfectpitch/sounds/"
pi = "/home/pi/perfectpitch/sounds/"



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

###### RFID ##################
rdr = RFID()
util = rdr.util()

# Set util debug to true - it will print what's going on
util.debug = True

rfidstart= rdr.wait_for_tag()
# Request tag
(error, data) = rdr.request()


# a = 'Card UID: 04 17 9F 0A D7 49 80'
# b = 'Card UID: 04 3F 91 0A D7 49 80'
# c = 'Card UID: 04 3F DE 0A D7 49 80'
# d = 'Card UID: 04 29 83 0A D7 49 80'
# e = 'Card UID: 04 29 C2 0A D7 49 80'
# f = 'Card UID: 04 43 94 0A D7 49 80'
# g = 'Card UID: 04 4D D9 0A D7 49 80'
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


insult = ['YOU SUCK','YOUR A LOSER', 'TONE DEF IDIOT', 'MELLON TELLER!!', 'you are useless', 'I have never met anyone more disapointing than you']

x = 4
# x = input('Enter dificulty level 1-5 :')
score = 0
level = input('Enter dificulty level 1-5 :')



while x == 100 :
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

#cards = [a, b, c, d, e, f, g]
while x == 1 :
    # Wait for tag
    rdr.wait_for_tag()

    # Request tag
    (error, data) = rdr.request()

    if not error:
		myData = util.read_out()

		print myData

		myd = myData.splitlines()
		for item in myd:
			if item == cards['A']: 
				print 'A'
				play('A4', 'horn')
			if item == cards['B']: 
				print 'B'
				play('B4', 'horn')
			if item == cards['C']: 
				print 'C'
				play('C4', 'horn')
			if item == cards['D']: 
				print 'D'
				play('D4', 'horn')
			if item == cards['E']: 
				print 'E'
				play('E4', 'horn')
			if item == cards['F']: 
				print 'F'
				play('F4', 'horn')
			if item == cards['G']: 
			 	print 'G'
			 	play('G4', 'horn')


			else:
				print 'NONE'


# 

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


win = True
correct = True
toneToPlay = '4'
instrumentToPlay = random.choice(sounds.keys())



# ###### Multiprocessing  ###########
# p = multiprocessing.Process(name='musicnote',  target=play(note, instrument)) #, args=(id, bot)
# p.daemon = True
# p.start()

###commented out here to....
# ### easy, same tone (4) and same instrument randomly picked ####
# while x == 2:
# 	# print toneToPlay
# 	print instrumentToPlay
# 	print 'Your score is  ' + str(score)
# 	#playC5()
# 	if (arduinoSerialData.inWaiting()>0):
# 		if win == True:

# 			##### Use tone 
# 			currNote = random.choice(note)
# 			noteToPlay = currNote + toneToPlay
# 			# instrumentToPlay = random.choice(instrument)
# 			print noteToPlay
# 			play( noteToPlay , instrumentToPlay)

# 			win = False
# 			print bcolors.BOLD + 'What tone is that?' + bcolors.ENDC
# 			print bcolors.HEADER +'Scan the proper card' + bcolors.ENDC
# 		elif win == False:

# 			myData = (error, data) = rdr.request()

# 			myd = myData.splitlines()  

# 			#time.sleep(5)

# 			for item in myd:
# 				win = assess(item, currNote, instrumentToPlay, score)


# ### easy, same tone (4) and same instrument randomly picked ####
# while x == 3:
# 	# print toneToPlay
# 	print instrumentToPlay
# 	print 'Your score is  ' + str(score)
# 	#playC5()
# 	if (arduinoSerialData.inWaiting()>0):
# 		if win == True:

# 			##### Use tone 
# 			currNote = random.choice(note)
# 			noteToPlay = currNote + toneToPlay
# 			# instrumentToPlay = random.choice(instrument)
# 			print noteToPlay
# 			play( noteToPlay , instrumentToPlay)

# 			win = False
# 			print bcolors.BOLD + 'What tone is that?' + bcolors.ENDC
# 			print bcolors.HEADER +'Scan the proper card' + bcolors.ENDC
# 		elif win == False:

# 			myData = (error, data) = rdr.request()

# 			myd = myData.splitlines()  

# 			#time.sleep(5)

# 			for item in myd:
# 				win = assess(item, currNote, instrumentToPlay, score)


# ### Medium Same tone, random instrument 
# while x == 4:
# 	instrumentToPlay = random.choice(instrument)
# 	#playC5()
# 	if (arduinoSerialData.inWaiting()>0):
# 		if win == True:
# 			currNote = random.choice(note)
# 			noteToPlay = currNote + random.choice(tone)
	
# 			#print noteToPlay
# 			play( noteToPlay , instrumentToPlay)

# 			win = False
# 			print bcolors.BOLD + 'What tone is that?' + bcolors.ENDC
# 			print bcolors.HEADER +'Scan the proper card' + bcolors.ENDC
# 		elif win == False:

# 			myData = (error, data) = rdr.request()

# 			myd = myData.splitlines()  

# 			#time.sleep(5)
# 			for item in myd:
# 				win = assess(item, currNote, instrumentToPlay, score)


# ### Hard random tone, random instrument, 
# while x == 5:

# 	#playC5()
# 	if (arduinoSerialData.inWaiting()>0):
# 		if win == True:
# 			currNote = random.choice(note)
# 			instrumentToPlay = random.choice(sounds.keys())
# 			toneToPlay = random.choice(sounds[instrumentToPlay])
# 			noteToPlay = currNote + toneToPlay
			

# 			#instrumentToPlay = random.choice(instrument)	
# 			#print noteToPlay
# 			play( noteToPlay , instrumentToPlay)

# 			win = False
# 			print bcolors.BOLD + 'What tone is that?' + bcolors.ENDC
# 			print bcolors.HEADER +'Scan the proper card' + bcolors.ENDC
# 		elif win == False:

# 			myData = (error, data) = rdr.request()

# 			myd = myData.splitlines()  

# 			#time.sleep(5)
# 			for item in myd:
# 				win = assess(item, currNote, instrumentToPlay, score)


# ... here




######################
######################
#####  LEVELS  #######
######################
######################


#level = 'x'
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
training = True

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



##### Flute only, using 4 #######
while level == 1:
	rdr.wait_for_tag()
    # Request tag
	(error, data) = rdr.request()

	# print toneToPlay
	instrumentToPlay = 'Flutenonvib'
	toneToPlay = '4'
	#playC5()
	if not error:
		if win == True:

			##### Use tone 
			currNote = random.choice(note)
			noteToPlay = currNote + toneToPlay
			# instrumentToPlay = random.choice(instrument)
			print noteToPlay
			if correct == True:
				score += 1
				print 'Your score is  ' + str(score)
			if correct == False:
				correct = True
			if score == 10:
				level = 2
			if score < -5:
				score = 0
			if score < 10:
				play( noteToPlay , 'Flutenonvib')
				win = False
			score += 1
			print 'Your score is  ' + str(score)
			play( noteToPlay , instrumentToPlay)

			win = False
			print bcolors.BOLD + 'What tone is that?' + bcolors.ENDC
			print bcolors.HEADER +'Scan the proper card' + bcolors.ENDC
		elif win == 'wrong':
			score -= 1
			win = False
		elif win == False:
			myData = (error, data) = rdr.request()

			myd = myData.splitlines()  
			for item in myd:
				win = assess(item, currNote, instrumentToPlay, score)

####### Flute only LV 2 ####################
while level == 2:
	rdr.wait_for_tag()
    # Request tag
	(error, data) = rdr.request()
	# print toneToPlay
	instrumentChoices = ['Flutenonvib', 'AltoFluteVib']
	instrumentToPlay =  random.choice(instrumentChoices)
	noteChoices = ['4', '5']
	toneToPlay = random.choice(noteChoices)
	#playC5()
	if (arduinoSerialData.inWaiting()>0):
		if win == True:
			##### Use tone 
			currNote = random.choice(note)
			noteToPlay = currNote + toneToPlay
			# instrumentToPlay = random.choice(instrument)
			print noteToPlay
			if correct == True:
				score += 1
				print 'Your score is  ' + str(score)
			if correct == False:
				correct = True
			if score == 20:
				level = 3
			if score < -5:
				score = 0
			if score < 20:
				play( noteToPlay , instrumentToPlay)
				win = False
			score += 1
			print 'Your score is  ' + str(score)
			play( noteToPlay , instrumentToPlay)
			win = False
			print bcolors.BOLD + 'What tone is that?' + bcolors.ENDC
			print bcolors.HEADER +'Scan the proper card' + bcolors.ENDC
		elif win == 'wrong':
			score -= 1
			win = False
		elif win == False:
			myData = (error, data) = rdr.request()

			myd = myData.splitlines()  
			for item in myd:
				win = assess(item, currNote, instrumentToPlay, score)



####### LV 3 ####################
while level == 3:
	# print toneToPlay
	rdr.wait_for_tag()
    # Request tag
	(error, data) = rdr.request()
	instrumentChoices = ['Flutenonvib', 'AltoFluteVib', 'BassClarinet', 'BassFlute']
	instrumentToPlay =  random.choice(instrumentChoices)
	noteChoices = ['4', '5']
	toneToPlay = random.choice(noteChoices)
	#playC5()
	if (arduinoSerialData.inWaiting()>0):
		if win == True:
			##### Use tone 
			currNote = random.choice(note)
			noteToPlay = currNote + toneToPlay
			# instrumentToPlay = random.choice(instrument)
			print noteToPlay
			if correct == True:
				score += 1
				print 'Your score is  ' + str(score)
			if correct == False:
				correct = True
			if score == 30:
				level = 4
			if score < -5:
				score = 0
			if score < 30:
				play( noteToPlay , instrumentToPlay)
				win = False
			score += 1
			print 'Your score is  ' + str(score)
			play( noteToPlay , instrumentToPlay)

			win = False
			print bcolors.BOLD + 'What tone is that?' + bcolors.ENDC
			print bcolors.HEADER +'Scan the proper card' + bcolors.ENDC
		elif win == 'wrong':
			score -= 1
			win = False
		elif win == False:
			myData = (error, data) = rdr.request()

			myd = myData.splitlines()  
			for item in myd:
				win = assess(item, currNote, instrumentToPlay, score)



####### LV 4 ####################
while level == 4:
	rdr.wait_for_tag()
    # Request tag
	(error, data) = rdr.request()
    # print toneToPlay
	instrumentChoices = ['Flutenonvib', 'AltoFluteVib', 'BassClarinet', 'BassFlute', 'EbClarinet', 'SopSaxVib', 'trumpet']
	instrumentToPlay =  random.choice(instrumentChoices)
	noteChoices = ['4', '5']
	toneToPlay = random.choice(noteChoices)
	#playC5()
	if (arduinoSerialData.inWaiting()>0):
		if win == True:
			##### Use tone 
			currNote = random.choice(note)
			noteToPlay = currNote + toneToPlay
			# instrumentToPlay = random.choice(instrument)
			print noteToPlay
			if correct == True:
				score += 1
				print 'Your score is  ' + str(score)
			if correct == False:
				correct = True
			if score == 45:
				level = 3
			if score < -5:
				score = 0
			if score < 45:
				play( noteToPlay , instrumentToPlay)
				win = False
			score += 1
			print 'Your score is  ' + str(score)
			play( noteToPlay , instrumentToPlay)

			win = False
			print bcolors.BOLD + 'What tone is that?' + bcolors.ENDC
			print bcolors.HEADER +'Scan the proper card' + bcolors.ENDC
		elif win == 'wrong':
			score -= 1
			win = False
		elif win == False:
			myData = (error, data) = rdr.request()

			myd = myData.splitlines()  
			for item in myd:
				win = assess(item, currNote, instrumentToPlay, score)

# ####### LV 5 ####################
# while level == 5:
# 	#
# 	instrumentChoices = ['Flutenonvib', 'AltoFluteVib', 'BassClarinet', 'BassFlute', 'EbClarinet', 'SopSaxVib', 'trumpet']
	
# 	noteChoices = ['4', '5', '3']
# 	toneToPlay = random.choice(noteChoices)
# 	 #print toneToPlay
# 	instrumentToPlay = random.choice(instrument)

# 	#playC5()
# 	if (arduinoSerialData.inWaiting()>0):
# 		if win == True:
# 			##### Use tone 
# 			currNote = random.choice(note)
# 			noteToPlay = currNote + toneToPlay
# 			# instrumentToPlay = random.choice(instrument)
# 			print noteToPlay
# 			if correct == True:
# 				score += 1
# 				print 'Your score is  ' + str(score)
# 			if correct == False:
# 				correct = True
# 			if score == 45:
# 				level = 3
# 			if score < -5:
# 				score = 0
# 			if score < 45:
# 				play( noteToPlay , instrumentToPlay)
# 				win = False
# 			score += 1
# 			print 'Your score is  ' + str(score)
# 			play( noteToPlay , instrumentToPlay)

# 			win = False
# 			print bcolors.BOLD + 'What tone is that?' + bcolors.ENDC
# 			print bcolors.HEADER +'Scan the proper card' + bcolors.ENDC
# 		elif win == 'wrong':
# 			score -= 1
# 			win = False
# 		elif win == False:
# 			myData = (error, data) = rdr.request()

# 			myd = myData.splitlines()  
# 			for item in myd:
# 				win = assess(item, currNote, instrumentToPlay, score)

# ### easy, same tone (4) and same instrument randomly picked ####

# # ### easy, same tone (4) and same instrument randomly picked ####
# # while level == 3:
# # 	# print toneToPlay
# # 	print instrumentToPlay
# # 	print 'Your score is  ' + str(score)
# # 	#playC5()
# # 	if (arduinoSerialData.inWaiting()>0):
# # 		if win == True:

# # 			##### Use tone 
# # 			currNote = random.choice(note)
# # 			noteToPlay = currNote + toneToPlay
# # 			# instrumentToPlay = random.choice(instrument)
# # 			print noteToPlay
# # 			play( noteToPlay , instrumentToPlay)

# # 			win = False
# # 			print bcolors.BOLD + 'What tone is that?' + bcolors.ENDC
# # 			print bcolors.HEADER +'Scan the proper card' + bcolors.ENDC
# # 		elif win == False:

# # 			myData = (error, data) = rdr.request()

# # 			myd = myData.splitlines()  

# # 			#time.sleep(5)

# # 			for item in myd:
# # 				win = assess(item, currNote, instrumentToPlay, score)


# # ### Medium Same tone, random instrument 
# # while x == 4:
# # 	instrumentToPlay = random.choice(instrument)
# # 	#playC5()
# # 	if (arduinoSerialData.inWaiting()>0):
# # 		if win == True:
# # 			currNote = random.choice(note)
# # 			noteToPlay = currNote + random.choice(tone)
	
# # 			#print noteToPlay
# # 			play( noteToPlay , instrumentToPlay)

# # 			win = False
# # 			print bcolors.BOLD + 'What tone is that?' + bcolors.ENDC
# # 			print bcolors.HEADER +'Scan the proper card' + bcolors.ENDC
# # 		elif win == False:

# # 			myData = (error, data) = rdr.request()

# # 			myd = myData.splitlines()  

# # 			#time.sleep(5)
# # 			for item in myd:
# # 				win = assess(item, currNote, instrumentToPlay, score)


# # ### Hard random tone, random instrument, 
# # while x == 5:

# # 	#playC5()
# # 	if (arduinoSerialData.inWaiting()>0):
# # 		if win == True:
# # 			currNote = random.choice(note)
# # 			instrumentToPlay = random.choice(sounds.keys())
# # 			toneToPlay = random.choice(sounds[instrumentToPlay])
# # 			noteToPlay = currNote + toneToPlay
			

# # 			#instrumentToPlay = random.choice(instrument)	
# # 			#print noteToPlay
# # 			play( noteToPlay , instrumentToPlay)

# # 			win = False
# # 			print bcolors.BOLD + 'What tone is that?' + bcolors.ENDC
# # 			print bcolors.HEADER +'Scan the proper card' + bcolors.ENDC
# # 		elif win == False:

# # 			myData = (error, data) = rdr.request()

# # 			myd = myData.splitlines()  

# # 			#time.sleep(5)
# # 			for item in myd:
# # 				win = assess(item, currNote, instrumentToPlay, score)



# #########################
# ###### TRAINING #########
# #########################
# while level == -10:

# 	if (arduinoSerialData.inWaiting()>0):

# 		if win == True:
# 			print welcome
# 			print rules
# 			print 'Training mode'
# 			print 'Place C block on pad'
# 			noteToPlay = 'C4'
# 			if correct == True:
# 				score += 1
# 			if correct == False:
# 				correct = True
# 			print 'Your score is  ' + str(score)
# 			if score == 4:
# 				level = -9
# 				pass
# 			if score < -5:
# 				score = 0
# 			if score < 4:
# 				play( 'C4' , 'Flutenonvib')
# 				win = False

# 		elif win == 'wrong':
# 			correct = False
# 			win = False
# 		elif win == False:
# 			myData = (error, data) = rdr.request()

# 			myd = myData.splitlines()  
# 			for item in myd:
# 				win = assess(item, 'C', 'Flutenonvib', score)
# while level == -9:

# 	if (arduinoSerialData.inWaiting()>0):

# 		if win == True:
# 			print 'Training mode'
# 			print 'Place D block on pad'
# 			noteToPlay = 'D4'


# 			if correct == True:
# 				score += 1
# 			if correct == False:
# 				correct = True
# 			print 'Your score is  ' + str(score)
# 			if score == 6:
# 				level = -8
# 			if score < -5:
# 				score = 0
# 			if score < 6:
# 				play( noteToPlay , 'Flutenonvib')
# 				win = False

# 		elif win == 'wrong':
# 			correct = False
# 			win = False
# 		elif win == False:
# 			myData = (error, data) = rdr.request()

# 			myd = myData.splitlines()  
# 			for item in myd:
# 				win = assess(item, 'D', 'Flutenonvib', score)
# while level == -8:

# 	if (arduinoSerialData.inWaiting()>0):

# 		if win == True:

# 			print 'Training mode'
# 			print 'Place correct block block on pad'
# 			CorD = ['C', 'D']
# 			currNote = random.choice(CorD)
# 			noteToPlay = currNote + '4'
# 			score += 1
# 			print 'Your score is  ' + str(score)
# 			if score == 9:
# 				level = -7
# 			if score < -5:
# 				score = 0
# 			if score <9:
# 				play( noteToPlay , 'Flutenonvib')
# 				win = False

# 		elif win == 'wrong':
# 			score -= 1
# 			win = False
# 		elif win == False:
# 			myData = (error, data) = rdr.request()

# 			myd = myData.splitlines()  
# 			for item in myd:
# 				win = assess(item, currNote , 'Flutenonvib', score)

# while level == -7:

# 	if (arduinoSerialData.inWaiting()>0):

# 		if win == True:
# 			print 'Training mode'
# 			print bcolors.HEADER + 'Introduce E block' + bcolors.ENDC
# 			print 'Place Correct block on pad'
# 			CorD = ['C', 'D', 'E']
# 			currNote = random.choice(CorD)
# 			noteToPlay = currNote + '4'
# 			score += 1
# 			print 'Your score is  ' + str(score)
# 			if score == 13:
# 				level = -6
# 			if score < -5:
# 				score = 0
# 			if score <13:
# 				play( noteToPlay , 'Flutenonvib')
# 				win = False

# 		elif win == 'wrong':
# 			score -= 1
# 			win = False
# 		elif win == False:
# 			myData = (error, data) = rdr.request()

# 			myd = myData.splitlines()  
# 			for item in myd:
# 				win = assess(item, currNote, 'Flutenonvib', score)


# while level == -6:

# 	if (arduinoSerialData.inWaiting()>0):

# 		if win == True:
# 			print 'Training mode'
# 			print bcolors.HEADER + 'Introduce F block' + bcolors.ENDC
# 			print 'Place Correct block on pad'
# 			CorD = ['C', 'D', 'E', 'F']
# 			currNote = random.choice(CorD)
# 			noteToPlay = currNote + '4'
# 			score += 1
# 			print 'Your score is  ' + str(score)
# 			if score == 20:
# 				level = -5
# 			if score < -5:
# 				score = 0
# 			if score <20:
# 				play( noteToPlay , 'Flutenonvib')
# 				win = False

# 		elif win == 'wrong':
# 			score -= 1
# 			win = False
# 		elif win == False:
# 			myData = (error, data) = rdr.request()

# 			myd = myData.splitlines()  
# 			for item in myd:
# 				win = assess(item, currNote, 'Flutenonvib', score)

# while level == -5:

# 	if (arduinoSerialData.inWaiting()>0):

# 		if win == True:
# 			print 'Training mode'
# 			print bcolors.HEADER + 'Introduce G block' + bcolors.ENDC
# 			print 'Place Correct block on pad'
# 			CorD = ['C', 'D', 'E', 'F', 'G']
# 			currNote = random.choice(CorD)
# 			noteToPlay = currNote + '4'
# 			score += 1
# 			print 'Your score is  ' + str(score)
# 			if score == 30:
# 				level = -4
# 			if score < -5:
# 				score = 0
# 			if score < 30:
# 				play( noteToPlay , 'Flutenonvib')
# 				win = False

# 		elif win == 'wrong':
# 			score -= 1
# 			win = False
# 		elif win == False:
# 			myData = (error, data) = rdr.request()

# 			myd = myData.splitlines()  
# 			for item in myd:
# 				win = assess(item, currNote, 'Flutenonvib', score)

# while level == -4:

# 	if (arduinoSerialData.inWaiting()>0):

# 		if win == True:
# 			print 'Training mode'
# 			print bcolors.HEADER + 'Introduce A block' + bcolors.ENDC
# 			print 'Place Correct block on pad'
# 			CorD = ['A', 'C', 'D', 'E', 'F', 'G']
# 			currNote = random.choice(CorD)
# 			noteToPlay = currNote + '4'
# 			score += 1
# 			print 'Your score is  ' + str(score)
# 			if score == 40:
# 				level = -3
# 			if score < -5:
# 				score = 0
# 			if score < 40:
# 				play( noteToPlay , 'Flutenonvib')
# 				win = False

# 		elif win == 'wrong':
# 			score -= 1
# 			win = False
# 		elif win == False:
# 			myData = (error, data) = rdr.request()

# 			myd = myData.splitlines()  
# 			for item in myd:
# 				win = assess(item, currNote, 'Flutenonvib', score)


# while level == -3:

# 	if (arduinoSerialData.inWaiting()>0):

# 		if win == True:
# 			print 'Training mode'
# 			print bcolors.HEADER + 'Introduce B block' + bcolors.ENDC
# 			print 'Place Correct block on pad'
# 			CorD = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# 			currNote = random.choice(CorD)
# 			noteToPlay = currNote + '4'
# 			score += 1
# 			print 'Your score is  ' + str(score)
# 			if score == 50:
# 				level = -2
# 			if score < -5:
# 				score = 0
# 			if score < 50:
# 				play( noteToPlay , 'Flutenonvib')
# 				win = False

# 		elif win == 'wrong':
# 			score -= 1
# 			win = False
# 		elif win == False:
# 			myData = (error, data) = rdr.request()

# 			myd = myData.splitlines()  
# 			for item in myd:
# 				win = assess(item, currNote, 'Flutenonvib', score)
# while level == -2:

# 	if (arduinoSerialData.inWaiting()>0):

# 		if win == True:
# 			print 'Training mode'
# 			print bcolors.HEADER + 'Introduce new tones' + bcolors.ENDC
# 			print 'Place Correct block on pad'
# 			CorD = ['C']
# 			currNote = random.choice(CorD)
# 			trainingInstruments = ['trumpet', 'Flutenonvib']
# 			instrumentToPlay = random.choice(trainingInstruments)
# 			noteToPlay = currNote + '4'
# 			score += 1
# 			print 'Your score is  ' + str(score)
# 			if score == 54:
# 				level = -1
# 			if score < -5:
# 				score = 0
# 			if score < 54:
# 				play( noteToPlay , instrumentToPlay)
# 				win = False

# 		elif win == 'wrong':
# 			score -= 1
# 			win = False
# 		elif win == False:
# 			myData = (error, data) = rdr.request()

# 			myd = myData.splitlines()  
# 			for item in myd:
# 				win = assess(item, currNote, instrumentToPlay, score)

# while level == -1:

# 	if (arduinoSerialData.inWaiting()>0):

# 		if win == True:
# 			print 'Training mode'
# 			print bcolors.HEADER + 'Introduce A block' + bcolors.ENDC
# 			print 'Place Correct block on pad'
# 			CorD = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# 			currNote = random.choice(CorD)
# 			noteToPlay = currNote + '4'
# 			score += 1
# 			print 'Your score is  ' + str(score)
# 			if score == 70:
# 				print "Congradulations!!! You have completed training!"
# 				level = 0
# 			if score < -5:
# 				score = 0
# 			if score < 70:
# 				play( noteToPlay , instrumentToPlay)
# 				win = False

# 		elif win == 'wrong':
# 			score -= 1
# 			win = False
# 		elif win == False:
# 			myData = (error, data) = rdr.request()

# 			myd = myData.splitlines()  
# 			for item in myd:
# 				win = assess(item, currNote, instrumentToPlay, score)




# #todo add easy modes, start with 2 diff notes, then progresively add note, then add octives with prompt on which its in. then remove prompt. then add diff instruments, the
# # while  x == 3:
# # 	play(G4, horn)


# # PyAudio = pyaudio.PyAudio
# # BITRATE = 16000 #number of frames per second/frameset.      
# # FREQUENCY = 261.63 #Hz, waves per second, 261.63=C4-note.
# # LENGTH = 3 #seconds to play sound

# # NUMBEROFFRAMES = int(BITRATE * LENGTH)
# # RESTFRAMES = NUMBEROFFRAMES % BITRATE
# # WAVEDATA = ''    


# # for x in xrange(NUMBEROFFRAMES):
# #  WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

# # #fill remainder of frameset with silence
# # for x in xrange(RESTFRAMES): 
# #  WAVEDATA = WAVEDATA+chr(128)

# # p = PyAudio()
# # stream = p.open(format = p.get_format_from_width(1), 
# #                 channels = 1, 
# #                 rate = BITRATE, 
# #                 output = True)
# # stream.write(WAVEDATA)
# # stream.stop_stream()
# # stream.close()
# # p.terminate()
