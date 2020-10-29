import re

emails = []

with open("tekstmetemails.txt", "r") as bestand:

    regel = bestand.readline()
   
    while regel:

        patroon = "([a-zA-Z0-9]+[.a-zA-Z0-9]+@[a-zA-Z0-9]+[.a-zA-Z]+)|([a-zA-Z0-9]+@[a-zA-Z0-9]+[.a-zA-Z]+)"

        
        gevonden = re.findall(patroon, regel)

        emails = gevonden
         
        print(emails)
        
        regel = bestand.readline()

