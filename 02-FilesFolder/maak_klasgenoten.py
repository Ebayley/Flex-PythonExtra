bestand = open("klasgenoten.txt", "w")

bestand.write("Sam,\nScott,\nJelani,\nTimo,\nKaan,\nRemy,\nLeon,\nColin,\nMichelle,\nNikay,\nJayden");

bestand.close()

bestand2 = open("klasgenoten.txt", "r")

inhoud = bestand2.read()

print(inhoud)
