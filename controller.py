from pyfirmata import Arduino

port ='COM13'

pin = 10


board =Arduino(port)


def runRelay_on():
    board.digital[pin].write(1)
    
def runRelay_off():
    board.digital[pin].write(0)


    