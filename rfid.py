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
wrong = 0

########################################
#### create logic to take instrument data and play challenge
#### TODO create blacklist of notes not on certain instruments, if random choice is on blacklist, do not use in challenge

def randomChoice(instrumentChoices, noteChoices, toneChoices):
    instrumentToPlay =  random.choice(instrumentChoices)
    toneToPlay = random.choice(toneChoices)
    noteToPlay = random.choice(noteChoices)
    soundToPlay = noteToPlay + toneToPlay

    assets.play(soundToPlay, instrumentToPlay)
    win = rfidread(cards[noteToPlay])

    if win == True:
        print 'great'
        # score += 1
        # print score
        return True
    else:
        print bcolors.FAIL + random.choice(insult) + bcolors.ENDC
        # score -= 1
        return False

    #return score
def answerRead(score, wrong):
    accuracy = (score/wrong)
    print 'Correct Answers : ' + score
    print 'Incorrect Answers : ' + wrong
    print 'Accuracy : ' + accuracy



########################################
# def postgresConnect:
#     #Define our connection string 
#     conn_string = "host='ec2-54-225-182-108.compute-1.amazonaws.com' dbname='dn7gu1epio9d7' user='arwewokxwekuka' port='5432' password='5d98586ca671123e05b3e11dcc22fa59790fbffdb9476550af9ced849d19e507'"
#     # print the connection string we will use to connect
#     print "Connecting to database\n   ->%s" % (conn_string)
#     # get a connection, if a connect cannot be made an exception will be raised here
#     conn = psycopg2.connect(conn_string)




x = 3

while x == 1:

    instrumentToPlay =  random.choice(instrumentChoices)
    toneToPlay = random.choice(toneChoices)
    noteToPlay = random.choice(noteChoices)
    soundToPlay = noteToPlay + toneToPlay

    assets.play(soundToPlay, instrumentToPlay)

    win = rfidread(cards[noteToPlay])

    if win == True:
        print 'great'
        score += 1
    else:
        print random.choice(insult)


while x == 2:
    if score < 3:
        instrumentChoices = ['Flutenonvib']
        noteChoices = ['C']
        toneChoices = ['4']

        instrumentToPlay =  random.choice(instrumentChoices)
        toneToPlay = random.choice(toneChoices)
        noteToPlay = random.choice(noteChoices)
        soundToPlay = noteToPlay + toneToPlay

        assets.play(soundToPlay, instrumentToPlay)

        win = rfidread(cards[noteToPlay])
        if win == True:
            print 'great'
            score += 1
            print score
        else:
            print random.choice(insult)
            wrong += 1

while x == 3:

    while score < 3:

        instrumentChoices = ['Flutenonvib']
        noteChoices = ['C']
        toneChoices = ['4']
        
        result = randomChoice(instrumentChoices, noteChoices, toneChoices)
        if result == True:
            score += 1
        if result == False:
            wrong += 1
        def answerRead(score, wrong)


    while score < 6:

        instrumentChoices = ['Flutenonvib']
        noteChoices = ['C', 'D']
        toneChoices = ['4']
        
        result = randomChoice(instrumentChoices, noteChoices, toneChoices)
        if result == True:
            score += 1
        if result == False:
            wrong += 1
        def answerRead(score, wrong)


    while score < 12:

        instrumentChoices = ['Flutenonvib']
        noteChoices = ['B', 'C', 'D']
        toneChoices = ['4']
        
        result = randomChoice(instrumentChoices, noteChoices, toneChoices)
        if result == True:
            score += 1
        if result == False:
            wrong += 1
        def answerRead(score, wrong)

    while score < 24:

        instrumentChoices = ['Flutenonvib', 'BbClarinet']
        noteChoices = ['B', 'C', 'D', 'E']
        toneChoices = ['4']
        
        result = randomChoice(instrumentChoices, noteChoices, toneChoices)
        if result == True:
            score += 1
        if result == False:
            wrong += 1
        def answerRead(score, wrong)

    
    while score < 48:

        instrumentChoices = ['Flutenonvib', 'BbClarinet', 'SopSaxVib']
        noteChoices = ['B', 'C', 'D', 'E', 'F']
        toneChoices = ['4']
        
        result = randomChoice(instrumentChoices, noteChoices, toneChoices)
        if result == True:
            score += 1
        if result == False:
            wrong += 1
        def answerRead(score, wrong)

    


