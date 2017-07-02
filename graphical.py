

import socket
import sys
from Tkinter import *
from threading import *

hote = "localhost"
port = int(sys.argv[1])
global ig
ig = Tk()

global serponse
global iinterface

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))

def parse(resp):
        i = 0
        nt = []
        new = resp.split(";")
        while i < (len(new)):
                nt.append(new[i].split(","))
                i += 1
        return nt

resp = parse("0,0,2,3;0,1,2,2;1,0,4,5;1,1,2,1")
    
class interface(Frame):
        grille = []
        def __init__(self, fenetre, **kwargs):
                Frame.__init__(self, ig, width=10000, height=10000, **kwargs)
                self.pack(fill=BOTH)
                print len(resp)
                i = 0
                while i < len(resp):
                        print i
                        self.grille.append(Label(self, text=("P" + resp[i][3] + ", F" + resp[i][2])))
                        self.grille[i].grid(row=int(resp[i][1]), column=int(resp[i][0]))
                        i += 1

iinterface = interface(ig)

#class affichage(Thread):
#        def __init__(self):
#                Thread.__init__(self)
#        def run(self):
                
class recept(Thread):
        def __init__(self):
                Thread.__init__(self)
        def run(self):
                while True:
                        socket.listen(5)
                        client, address = socket.accept()
                        response = client.recv(1000000)
                        serponse = parse(response)
                        if serponse != "":
                                print serponse
                        
                        
#thread_1 = affichage()
thread_2 = recept()

#thread_1.start()
thread_2.start()

#thread_1.join()
thread_2.join()

iinterface.mainloop()

socket.close
#interface.destroy()
