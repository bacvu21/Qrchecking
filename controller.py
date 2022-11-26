from pyfirmata import Arduino
import time 


port ='COM12'

pin = 11
pin1 = 10
pin2 = 9
pin3 = 8


board =Arduino(port)


def runRelay_on1():
    board.digital[pin].write(1)
def runRelay_on2():
    board.digital[pin1].write(1)
def runRelay_on3():
    board.digital[pin2].write(1)
def runRelay_on4():
    board.digital[pin3].write(1)
    
def runRelay_off():
    board.digital[pin].write(0)
    board.digital[pin1].write(0)
    board.digital[pin2].write(0)
    board.digital[pin3].write(0)
def runRelay_off1():
     board.digital[pin].write(0)
def runRelay_off2():
     board.digital[pin1].write(0)
def runRelay_off3():
     board.digital[pin2].write(0)
def runRelay_off4():
     board.digital[pin3].write(0)
    

def delay(n):
    
    time.sleep(n)
    runRelay_off()
    


    