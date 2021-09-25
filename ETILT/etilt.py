import subprocess 
from datetime import datetime
import requests
import random

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
        he = "help"
        helpgui = """
           Currently avaliable commands:
           help: You just ran this command lol, Opens the help menu.
           clear: clears the shell from commands and responses, Good to do for clean work.
           checkip: Run this to get your IP, Geolocation and other details.
           tell-time: Tells the time
           randomnum: Generates a random number between 1 - 100
           exit: Exits the ETILT Console
                  """
        rannum = "randomnum"
        secrecy = "secret"
        ex = "exit"

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

        if Etilt_ConsoleINPT == he:
            print(helpgui)

        if Etilt_ConsoleINPT == rannum:
         print("Random number between 1 - 100: ", random.randrange(1, 100))

        if Etilt_ConsoleINPT == secrecy:
            f= open("secret.txt","w+")
            for i in range(69):
             f.write("Never gonna give you up %d\r\n" % (i+1))
            f.close()

        if Etilt_ConsoleINPT == ex:
            print("Exiting ETILT Console...")
            exit()
