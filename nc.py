import requests as rs
import pyautogui as pg
import time as t

from os import system

clrscreen = lambda : system('cls')

file_list = [
    'Client.java',
    'Clientfile.java',
    'eclient.java',
    'eserver.java',
    'httpclient.java',
    'httpserver.java',
    'ipclient.java',
    'ipserver.java',
    'Pingc.java',
    'Pings.java',
    'Server.java',
    'Serverfile.java',
    'swclient.java',
    'swserver.java',
    'UDPclient.java',
    'udpdnsclient.java',
    'udpdnsserver.java',
    'UDPserver.java'
]

c = 'y'
while c.lower() == 'y':

    for index, file in enumerate(file_list):
        print(f"{index} {file}")

    try:
        file_index = int(input("Enter the serial number to read the file: "))
    except:
        break

    file_ = file_list[file_index]
    url = 'https://rockleaks.netlify.app/nc/' + file_
    res = rs.get(url)
    
    file_content = res.content.decode('utf-8')
    print(f"{' Program Begins ':=^100} \n")
    print(file_content)    
    print(f"\n {' Program Ends ':=^100} \n")
    choice = input("Do you want to write this content in other file? (Y/N): ")

    if choice == 'y':
        pg.hotkey('win', 'r')
        pg.write("notepad")
        pg.press("enter")
        t.sleep(1)
        pg.write(file_content, interval = 0.0025)

    c = input("Do you want to try again? (Y/N): ")
    clrscreen()
clrscreen()