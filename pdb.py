import os

os.system("pip install serial esptool")

import serial  # Renommer le module 'serial'
import subprocess

import time

port = ""

print("======================")
print("Paxo Debug Bridge")
print("V1 from 31/08/2023")
print("by eletrixtime")
print("Type help for command")
print("======================")


def flash_firmware(port, firmware_path, baudrate=115200):
    try:

        os.system(f'python esptool/esptool.py --port COM{port}  write_flash 0 {firmware_path} ')
        
    except subprocess.CalledProcessError or FileNotFoundError as e :
        print("ERROR OCCURED IN FLASHING OS !"+ e)
    print("OS FLASHED SUCCESSFULLY !")
def readcmd(text):
    if text.lower() == "help":
        print("List of command : ")
        print("HELP : show list of commands!")
        print("CONNECT : Connect to the paxo debug interface")
        print("FLASH : flashing a fimware")
        print("INFO : Get info")
    elif text.lower() == "connect":
        global port
        print("Type the port")

        port = input("Port number : ")
    elif text.lower() == "credits":
        print("PDB (paxo debug bridge)")
        print("coded by eletrixtime")
        print("For the paxo project")
        print("Available here : https://discord.gg/GKh4VMk7MS")
    elif text.lower() == "flash":
        print("⚠️ WARNING ⚠️")
        print("This feature CAN destroy your paxo and corrupt the system if you know what you did type yes if you want to return to safety type no! NOTE: This will delete all data") # MERCI GOOGLE TRADUCTION
        if input("YES OR NO: ").lower() == "yes":
            
            if port == "":
                print("Please select a port (use connect !)")
            else:
                flash_firmware(port=port,firmware_path=input("Please enter .bin path ! : "))
        elif input("YES OR NO: ").lower() == "no":
            print("Returning to security !")
    elif text.lower() == "info":
        print("INFORMATIONS OF THE PAXO DEBUG INTERFACE/BRIDGE")
        try:
            print("Port select : COM"+ port)
        except UnboundLocalError:
            print("Port selected : N/A")
        print("PaxoPhone version : SOON")
    else:
        print("Command not found! Type help for command list!")


def main():
    text1 = 0
    text1 = input("PDB >> ")
    readcmd(text=text1)
    main()

main()