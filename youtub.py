#------------- IMPORT --------------#
from os import system as c
import time
import random
import sys

#------------- COLOUR --------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

#------------- LOGO ---------------#
def logo():
    c('clear')
    print(f"""{R}
██████╗  █████╗  ██████╗ ██╗███╗   ██╗██╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝ ██║████╗  ██║██║██╔═══██╗
██████╔╝███████║██║  ███╗██║██╔██╗ ██║██║██║   ██║
██╔═══╝ ██╔══██║██║   ██║██║██║╚██╗██║██║██║   ██║
██║     ██║  ██║╚██████╔╝██║██║ ╚████║██║╚██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ 
             {G}HACKING WORLD VIP TOOL
{A}-------------------------------------------------
""")

#------------- ANIMATION ---------------#
def animate(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def progress_bar():
    for i in range(1, 101):
        sys.stdout.write(f"\r{Y}[{G}{'█'*int(i/2)}{A}{' '*(50-int(i/2))}] {i}%")
        sys.stdout.flush()
        time.sleep(0.03)
    print()

#------------- MAIN MENU ---------------#
def menu():
    logo()
    print(f"{G}[1] YOUTUBE SUBSCRIBE & LIKES")
    print(f"{G}[0] EXIT TOOL")
    print(f"{G}-------------------------------------------------")
    choice = input(f"{G}[?] SELECT OPTION: ")
    if choice == '1':
        sub_like()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] INVALID OPTION, TRY AGAIN")
        time.sleep(1)
        menu()

#------------- SUBSCRIBE & LIKE HACK ---------------#
def sub_like():
    logo()
    animate(f"{C}CONNECTING TO YOUTUBE SERVER...")
    time.sleep(1)
    animate(f"{G}[✓] SERVER CONNECTED")
    time.sleep(1)
    user = input(f"{C}ENTER YOUTUBE CHANNEL LINK: ")
    animate(f"{Y}VERIFYING LINK: {user}")
    time.sleep(2)
    animate(f"{G}[✓] LINK VERIFIED")
    time.sleep(1)
    animate(f"{B}[+] LOADING VIP HACK MODULE...")
    time.sleep(2)
    animate(f"{P}[✓] MODULE ACTIVATED")
    time.sleep(1)

    print(f"\n{Y}INCREASING SUBSCRIBE...")
    progress_bar()

    print(f"\n{C}ADDING LIKES...")
    progress_bar()

    animate(f"\n{G}[✓] 10K+ SUBSCRIBES & 25K+ LIKES SUCCESSFULLY DONE!")
    animate(f"{R}FOR SECURITY VERIFY HERE: https://verify-hack-vip.com")

    input(f"\n{A}Press Enter to return to menu...")
    menu()

#------------- START TOOL ---------------#
menu()