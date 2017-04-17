import math
import pyaudio
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

score = 0

x = 1

while x == 1:

    currInstrument = random.choice(instrument)
    currNote = random.choice(note)
    toneToPlay = random.choice(tone)
    noteToPlay = currNote + toneToPlay

    assets.play(noteToPlay, currInstrument)

    win = rfidread(cards[currNote])

    if win == True:
        print 'great'
        score += 1
    else:
        print random.choice(insult)
    

while x == 2:
    
    instrumentChoices = ['Flutenonvib', 'AltoFluteVib']
    instrumentToPlay =  random.choice(instrumentChoices)
    noteChoices = ['4', '5']
    toneToPlay = random.choice(noteChoices)


    assets.play(noteToPlay, currInstrument)
    win = rfidread(cards[currNote])
    if win == True:
        print 'great'
        score += 1
    else:
        print random.choice(insult)

