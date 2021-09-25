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
         url = "https://github.com/someguy/brilliant/blob/master/somefile.txt"
directory = getcwd()
filename = directory + 'somefile.txt'
r = requests.get(url)

f = open(filename,'w')
f.write(r.content)

        

 


        
