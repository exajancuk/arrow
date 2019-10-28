import os
from time import sleep


i ="\033[32;1m"
y ="\033[36;1m"
x ="\033[0m"
os.system("clear")
print(i+'\t  Shorcut for help you')
print(y+'\t    Exajancuk')

print(i+'+'*40)
print('\nProses..')
sleep(1)
print(y+'\n[!] making termux properties directory..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(i+'[!]Success !')
sleep(1)
print(y+'\n[!] Making setup file..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
exajnck = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
exajnck.write(key)
exajnck.close()
sleep(1)
print(i+'[!] Success !')
sleep(1)
print(y+'\n[!] Setting up..')
sleep(2)
os.system('termux-reload-settings')
print(i+'[!] Successfully !! ^^'+x+'\n\nJangan lupa like, Coment & Subscribe\nExajancuk channel, \nTerimakasih \n\n')


#Ini cuma shortcut untuk membantu.
