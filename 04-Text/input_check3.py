import re

while True:

    invoer = input("Voer je telefoonnummer, postcode en kenteken in: ")

    patroon = "06-\d{8}|\d{4}[A-Z]{2}|[A-Z]{2}-\d{3}-[A-Z]{3}"
    matches = re.findall(patroon, invoer)
    
    if(len(matches) > 0):
        break

print("Bedankt nummer in juiste formaat:", matches)

#Mijn nummer is 06-16392749! en dit it mijn postcode: 2078KP. en dit is mijn kenteken SJ-123-ATB.
#(06-\d+[0-9])|(\d[0-9]{3}[A-Z]{2})
