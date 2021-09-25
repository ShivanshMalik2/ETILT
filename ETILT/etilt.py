import subprocess 
from datetime import datetime
import requests

#Console time get 
#While & if loops for initiating

while True:
    x = 1
    if x == 1:

        
        # Var's
        ClsClear = "clear"
        Etilt_ConsoleINPT = input("Etilt_Console>> ")
        TimeCheck = "tell-time"
        now = datetime.now()
        consoletime = now.strftime("%H:%M:%S") 
        DLSD = "download"
        ip = "checkip"
        ipurl = "http://ip-api.com/json/"



        #time OPT

        if Etilt_ConsoleINPT == TimeCheck:
            print(consoletime)
         

        #ClearOutTerminal

        if Etilt_ConsoleINPT == ClsClear:
         subprocess.run("cls", shell=True) 
         print("Elist Console was cleared at " + consoletime)


        if Etilt_ConsoleINPT == ip:
         response = requests.get(ipurl)
         print(response.json())

