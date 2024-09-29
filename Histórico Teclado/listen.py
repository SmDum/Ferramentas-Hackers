from pynput.mouse import Listener

def writetofile(x,y):
    print('Posição Atual do Mouse: {0}'.format((x,y)))

with Listener(on_move=writetofile) as l:
    l.join()
