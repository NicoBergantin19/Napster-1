import hashlib, sys, unittest,socket, mysql.connector
from syslog import LOG_INFO
import random
import string
from os import fork

class Server:
    


    @staticmethod
    def session_generator(size=16, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))
    @staticmethod
    def Login(ip, porta):
        try:
            _sessionid=Server.session_generator()
            mycursor.execute(f"INSERT INTO PEER (SESSION_ID, IP, PORTA) VALUES ('{_sessionid}','{ip}','{porta}')")
            mydb.commit()
                
        except mysql.connector.Error as err:
            _sessionid="0000000000000000"
        client.send(("ALGI"+_sessionid).encode())

    @staticmethod
    def CercaPeer(sessionID):
        print("Inserisci il sessionID del peer ricercato")

    @staticmethod
    def Aggiungi(sessionID, md5, descrizione):
        print("Inserisci il file da aggiungere")

    @staticmethod
    def Delete(sessionID, md5):
        print("Inserisci il sessionID da eliminare")

    @staticmethod
    def Ricerca(sessionID, testo):
        print("Inserisci il file da cercare")

    @staticmethod
    def Logout(sessionID):
        print("Logout")

    @staticmethod
    def RegistraDownload(md5, sessionID):
        print("Registra Download")

    @staticmethod
    def Parser(pacchetto):

        if(pacchetto=="LOGI"):
            ip=client.recv(15).decode()
            porta=client.recv(5).decode()
            Server.Login(ip,porta)
        elif(pacchetto=="ADDF"):
            sessionId=client.recv(16).decode()
            md5=client.recv(32).decode()
            filename=client.recv(100).decode()
        elif(pacchetto=="DELF"):
            sessionId=client.recv(16).decode()
            md5=client.recv(32).decode()
        elif(pacchetto=="FIND"):
            sessionId=client.recv(16).decode()
            ricerca=client.recv(20).decode()

    
    
mydb = mysql.connector.connect(host="localhost",user="root",password="123",database="DIRECTORY")
mycursor = mydb.cursor()
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("",50000))

sock.listen(50)

while True:
    print("server in ascolto....\n")
    client,addr= sock.accept()
    pid=0
    if(pid==0):
        richiesta=client.recv(4).decode()
        Server.Parser(richiesta)
        client.close()
        exit()








