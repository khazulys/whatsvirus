import os
import time

#warna
aa='\033[1;34m'
bb='\033[1;33m'

def virus():
  virus='404.404.404.404.404.404.404.404.404.404.404.404'
  i=1000
  file=open('virus.txt','w')
  file.write(virus)

  vr=100
  while (vr < 1000):
     vr = vr + 1
     file.write(virus + str(vr) + '\n')

def banner():
  print ('''
 _  _    ___  _  _           _
| || |  / _ \| || |   /\   /(_)_ __ _   _ ___
| || |_| | | | || |_  \ \ / / | '__| | | / __|
|__   _| |_| |__   _|  \ V /| | |  | |_| \__ \
      |_|  \___/   |_|     \_/ |_|_|   \__,_|___/
     ''')
  print ('\x1b[5;37;41m	WhatsApp 404 Virus by kHazul\x1b[0m')
  print (aa+'[+]'+bb+'Processing creating virus 404')
  time.sleep(3)
  print (aa+'[+]'+bb+'Sucess. virus save in virus.txt')

if __name__=='__main__':
  os.system('cls' if os.name=='nt' else 'clear')
  banner()
  virus()
