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

from pirc522 import RFID
from assets import rfidread
import assets


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


x = 1

if x == 1:


    currNote = random.choice(choices(note)
    noteToPlay = currNote + toneToPlay

    play(note, instrument)

    rfidread(cards[currNote])

    if win == True:
        print 'great'
    else:
        print 'NOPE'