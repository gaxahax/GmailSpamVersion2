import os
import sys
import time
time.sleep(2)
os.system('clear')
print('''

 _______  _______ _________          _______
(  ____ \(  ____ \\__   __/|\     /|(  ____ )
| (    \/| (    \/   ) (   | )   ( || (    )|
| (_____ | (__       | |   | |   | || (____)|
(_____  )|  __)      | |   | |   | ||  _____)
      ) || (         | |   | |   | || (
/\____) || (____/\   | |   | (___) || )
\_______)(_______/   )_(   (_______)|/

########################GSv2-SETUP###########

''')

os.system('apt update && apt upgrade -y')
os.system('pkg update -y')
os.system('pkg upgrade -y')
os.system('pip install colorama')
os.system('clear')
start = input("Do you want to start the GSv2 tool? (y/n)\n>>>").lower()
print(start)
while not(start.isalpha() and start in "yn"):
        print("Wrong input!")
        print(start)
if start == 'y':
        print('Tool Starting...')
        time.sleep(2)
        os.system('cd ..')
        os.system('python GSv2.py')
if start == 'n':
        time.sleep(1)
        print("Leaving setup...")
        time.sleep(1)
        exit()
