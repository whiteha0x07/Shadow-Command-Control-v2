# Shadow-Command-Control-v2

This is the SC2 (Shadow Command & control) server version 2. This version has made significant improvements from that last version (currently archived) which has the main features such as a main navigation menu, passive backdoor listener and better command execution on the backdoor.

![Uploading Screenshot 2023-08-11 at 9.18.04 PM.png…]()

# List of all Improvments & Updates 

~Listener module seperated from the main user interface along with passive listener on boot. 

~Formatting (mostly) in JSON files. C2 server is able to read system Information of compromised systems connected to server. 

~Backdoor sleeper capabilites reworked; will stay dormant listening for shell connection request without crashing. 

~Added command line interface, able to run various commands.

~Backdoor rarely crashes unless an abnormal command is sent from the C2 

~Added a logging feature that automatically stores the system information and IP address in a folder in the same directory.

