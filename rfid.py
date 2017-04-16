
import signal
import time
import sys

from pirc522 import RFID

# run = True
# rdr = RFID()
# util = rdr.util()
# util.debug = True

# print("Starting")
# while run:
#     rdr.wait_for_tag()

#     (error, data) = rdr.request()
#     if not error:
#         print("\nDetected: " + format(data, "02x"))

#     (error, uid) = rdr.anticoll()
#     if not error:
#         print("Card read UID: "+str(uid[2])+str(uid[3]))
#     time.sleep(1)
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



def rfidread(targetTag)

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
        else:
            print 'False'
    time.sleep(1)

rfidread(cards['A'])
