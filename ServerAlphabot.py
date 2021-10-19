import socket as sck
import threading as thr

indirizzo = ('localhost',5012)
s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.bind(indirizzo)


class Clients_class(thr.Thread):
    def __init__(self, s):
        thr.Thread.__init__(self)   
        self.s = s
        self.daemon = True
    
    def run(self):
        while True:
            connessione, indirizzo = s.accept()
            connessione.sendall("Dispositivo già accoppiato".encode())


def main():
    s.listen()
    connessione, indirizzo = s.accept()
    
    temp = Clients_class(s)
    temp.start()
    
    _ = (connessione.recv(4096)).decode()
    connessione.sendall(("controller accettato").encode())
    gestisciController(connessione)
        
    
def gestisciController(connessione):
    while True:
        messaggio = (connessione.recv(4096)).decode()
        if(messaggio == "esci"):
            connessione.sendall("disaccoppiato".encode())
            break
        elif(messaggio == "avanti"):
            print("avanti")
        elif(messaggio == "indietro"):
            print("indietro")
        elif(messaggio == "gira destra"):
            print("gira destra")
        elif(messaggio == "gira sinistra"):
            print("gira sinistra")
        else:
            print(f"comando {messaggio} non riconosciuto")
    
    
funzioni = {"F":forward()}
if __name__ == '__main__':
    main()