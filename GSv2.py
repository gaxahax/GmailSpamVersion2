import smtplib
import os
import sys
from colorama import Fore, Back, Style
import time
os.system('apt update && apt upgrade -y')
os.system('pkg update -y')
os.system('pkg upgrade -y')
os.system('clear')
os.system('pip install colorma')

#warning
time.sleep(2)
print(Fore.RED + 'YOU')
time.sleep(0.5)
print(Fore.RED + 'DONT')
time.sleep(0.5)
print(Fore.RED + 'HAVE')
time.sleep(0.5)
print(Fore.RED + 'TO')
time.sleep(0.5)
print(Fore.RED + 'USE')
time.sleep(1)
print(Fore.RED + '@GMAIL.COM')
time.sleep(1)
print(Fore.RED + '!!!')
time.sleep(2)
os.system('clear')

#logo
print(Fore.RED + "░██████╗░░██████╗██╗░░░██╗██████╗░")
print(Fore.RED + "██╔════╝░██╔════╝██║░░░██║╚════██╗")
print(Fore.WHITE + "██║░░██╗░╚█████╗░╚██╗░██╔╝░░███╔═╝")
print(Fore.WHITE + "██║░░╚██╗░╚═══██╗░╚████╔╝░██╔══╝░░")
print(Fore.GREEN + "╚██████╔╝██████╔╝░░╚██╔╝░░███████╗")
print(Fore.GREEN + "░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝")
print(Fore.BLUE + "GMAIL SPAM V2 - - - BY GAXA - - -")



#TARGETING
mail = '@gmail.com'
toaddrs = input("\n\nPLEASE ENTER TARGET GMAIL: ") + mail
fromaddrs = input("PLEASE ENTER YOUR GMAIL: ") + mail
Password = input('PLEASE ENTER SMTP CODE: ')
sub = input('PLEASE ENTER SUBJECT: ')
message = input('PLEASE ENTER MESSAGE: ')
num_iterations = int(input('Number of mails: '))

#LOGIN
with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(fromaddrs, Password)

    for i in range(num_iterations):
        subject = 'Subject: ' + sub + '\n\n'
        content = subject + message
        smtpserver.sendmail(fromaddrs, toaddrs, content)
        print(Fore.RED + str(i+1) + " MAIL SUCCESSFULLY SENT.")
    #WAITING...
        if (i+1) % 75 == 0:
            print(Fore.YELLOW + "Waiting 3 minutes...")
            time.sleep(180)

