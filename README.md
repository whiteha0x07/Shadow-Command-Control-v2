# Shadow-Command-Control-v2

This is the SC2 (Shadow Command & control) server version 2. This version has made significant improvements from that last version (currently archived) which has the main features such as a main navigation menu, passive backdoor listener and better command execution on the backdoor. The main file is c2.py and conhandler.py and shellspawn.py are dependency files.

<img width="677" alt="Screenshot 2023-08-11 at 9 28 02 PM" src="https://github.com/whiteha0x07/Shadow-Command-Control-v2/assets/141960592/d6381cd0-6892-4b79-b5e7-52ed3bb4380d">

SC2 is made strictly for educational purposes and is not meant to be used maliciously or as a profession tool for pentesting. 

# List of all Improvments & Updates 

~Listener module seperated from the main user interface along with passive listener on boot. 

~Formatting (mostly) in JSON files. C2 server is able to read system Information of compromised systems connected to server. 

~Backdoor sleeper capabilites reworked; will stay dormant listening for shell connection request without crashing. 

~Added command line interface, able to run various commands.

~Backdoor rarely crashes unless an abnormal command is sent from the C2 

~Added a logging feature that automatically stores the system information and IP address in a folder in the same directory.

# Updates to come with SC2 v3 

~Custom SC2 installer and settings configuration file

~Global commands; sends commands to all active systems connected to the C2

~Server side connection authentication 

~New commands [Nspy, Exfiltrator, Key logger etc.]

~Custom generation of backdoors 

~Options for enabling connection through TOR or VPS

This repository is meant as a tutorial and guide for beginners looking to learn how to progam hacking software; you can find the explanation here: https://medium.com/@whiteha0x07mania/programming-a-malicious-backdoor-and-c2-server-in-python-eda6e6a57257

~Compatabilility with Metasploit and other hacking frameworks 




