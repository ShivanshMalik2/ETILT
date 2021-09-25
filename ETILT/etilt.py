import subprocess 
from datetime import datetime                                                                  
import requests

now = datetime.now()

consoletime = now.strftime("%H:%M:%S")

#While & if loops for initiating
while True:
    x = 1
    if x == 1:

        Yourl = f"{Elit_ConsoleINPT}"

        # Var's
        ClsClear = "clear"
        Elit_ConsoleINPT = input("Etilt_Console>> ")
        r = requests.get(url, allow_redirects=True)

        #ClearOutTerminal
        if Elit_ConsoleINPT == ClsClear:
         subprocess.run("cls", shell=True) 
         print("Elist Console was cleared at " + {consoletime})
            
            
         if Elit_ConsoleINPT == "download":
         DownloadInput = input("Enter the URL you want to download from: ")
         if DownloadInput.endswith == ".txt":
          r = requests.get(DownloadInput, allow_redirects=True)
          open('DownloadInput', 'wb').write(r.content)



        

 


        
