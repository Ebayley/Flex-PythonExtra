import re

while True:

    invoer = input("Voer je telefoonnummer in: ")

    # Het klopt dat er een "r" voor de regular expression staat, zo voorkom je gedoe met speciale tekens
    patroon = "(06-\d+[0-9])|(\d[0-9]{3}[A-Z]{2})"
    matches = re.findall(patroon, invoer)
    
    # Als we matches hebben voor de regular expression springen we uit de while
    if(len(matches) > 0):
        break

# Hier kom je pas uit als het telefoonnumer in het juiste formaat ingevoerd is.
print("Bedankt nummer in juiste formaat:", matches[0])

#strings: 06-12345678 en 06-12345678
