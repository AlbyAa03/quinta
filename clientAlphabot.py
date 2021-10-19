import threading as thr
import socket as sck

indirizzo = ("192.168.0.120",5012)
s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.connect(indirizzo)

class MandaMessaggi(thr.Thread):
    def __init__(self,s):
        thr.Thread.__init__(self,daemon=True)
        self.s = s
    
    def run(self):
        while True:
            messaggio = str(input("->"))
            s.sendall(f"{messaggio}".encode())
        
    
    
            
    
def main():
    client = MandaMessaggi(s)
    client.start()
    s.sendall("libero?".encode())
    while True:
        
        messaggio = s.recv(4096)
        messaggio = messaggio.decode()
        if(messaggio == "Dispositivo già accoppiato" or messaggio == "disaccoppiato"):
            break
        print(f"\nmessaggio : {messaggio}\n->",end="")
        
if __name__ == '__main__':
    main()