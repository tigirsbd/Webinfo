import os
import time
import sys
os.system("clear")
lg="""\033[1;32;40m
 _    _ _           _     
| |  | | |         (_)    
| |  | | |__   ___  _ ___ \033[1;36;40m
| |/\| | '_ \ / _ \| / __|
\  /\  / | | | (_) | \__ \ 
 \/  \/|_| |_|\___/|_|___/"""
for i in lg:
	sys.stdout.write(i)
	sys.stdout.flush()
	time.sleep(0.1)
me=input("\n\nPress Enter: ")
time.sleep(0.2)
os.system("clear")
print("\033[1;32;40m\nExmple:google.com")
while True:
	url=input("\033[1;36;40m\n\n[+] Enter website:  \033[1;32;40m")
	time.sleep(0.2)
	os.system("whois %s"%(url))
	u=input("\033[1;34;40m\n\npress Enter: ")
	os.system("clear")