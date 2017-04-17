import wave
import time
import multiprocessing
from pirc522 import RFID
import signal
import time
import sys
import pyaudio
import random

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








class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'







def rfidread(targetTag):

    run = True
    rdr = RFID()
    util = rdr.util()
    util.debug = True

    rdr.wait_for_tag()
    (error, data) = rdr.request()
    def end_read(signal,frame):
	    global run
	    print("\nCtrl+C captured, ending read.")
	    run = False
	    rdr.cleanup()
	    sys.exit()

	signal.signal(signal.SIGINT, end_read)

    if not error:
        print("\nDetected: " + format(data, "02x"))

    (error, uid) = rdr.anticoll()
    if not error:
        tag = (str(uid[2])+str(uid[3]))
        print(str(uid[2])+str(uid[3]))
        
        if targetTag == tag:
            print 'TRUE'
            return True
        else:
            print 'False'
            return False

    time.sleep(1)