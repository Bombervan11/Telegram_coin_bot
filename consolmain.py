
import os
import subprocess
import sys
from colorama import init, Fore, Back, Style
import time
x = 0
init()

def console_picture():
    print(Style.BRIGHT + Fore.YELLOW)
    print("██╗     ██╗████████╗███████╗ ██████╗ ██████╗ ██╗███╗   ██╗    ███████╗ █████╗ ██████╗ ███╗   ███╗")
    time.sleep(0.1)
    print("██║     ██║╚══██╔══╝██╔════╝██╔════╝██╔═══██╗██║████╗  ██║    ██╔════╝██╔══██╗██╔══██╗████╗ ████║")
    time.sleep(0.1)
    print("██║     ██║   ██║   █████╗  ██║     ██║   ██║██║██╔██╗ ██║    █████╗  ███████║██████╔╝██╔████╔██║")
    time.sleep(0.1)
    print("██║     ██║   ██║   ██╔══╝  ██║     ██║   ██║██║██║╚██╗██║    ██╔══╝  ██╔══██║██╔══██╗██║╚██╔╝██║")
    time.sleep(0.1)
    print("███████╗██║   ██║   ███████╗╚██████╗╚██████╔╝██║██║ ╚████║    ██║     ██║  ██║██║  ██║██║ ╚═╝ ██║")
    time.sleep(0.1)
    print("╚══════╝╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝")
    time.sleep(0.1)
    print("                                                                                                 ")
    time.sleep(0.2)
console_picture()
print("Press Enter to start...")
input()

while (True):
    print("  _   _              _      _                             _     ")
    time.sleep(0.01)
    print(" | \ | |            | |    | |                           | |    ")
    time.sleep(0.01)
    print(" |  \| |  ___ __  __| |_   | |  __ _  _   _  _ __    ___ | |__  ")
    time.sleep(0.01)
    print(" | . ` | / _ \\ \/ /| __|   | | / _` || | | || '_ \  / __|| '_ \ ")
    time.sleep(0.01)
    print(" | |\  ||  __/ >  < | |_   | || (_| || |_| || | | || (__ | | | |")
    time.sleep(0.01)
    print(" |_| \_| \___|/_/\_\ \__|  |_| \__,_| \__,_||_| |_| \___||_| |_|")
    time.sleep(0.1)
    print("                                                                ")
    process = subprocess.Popen([sys.executable, "bot_V2.py"])
    process.wait()
