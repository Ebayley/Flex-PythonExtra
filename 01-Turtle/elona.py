import turtle

#for x in range(4):
    #turtle.forward(100)
    #turtle.right(90)
    #turtle.forward(100)
    #turtle.right(90)
    #turtle.forward(100)
    #turtle.right(90)
    #turtle.forward(100)
    #turtle.left(45)

#als je de laatste turtle.righ(90) verwijderd maakt heet een raampje.
#omdat hij dan niet rechts gaat oom een vierhoek te maken, maar doorgaat. 

#als je de laatste turtle.right(90) verandert met turtle.right(45) dan worden het twee vierkantjes aan elkaar schuin over twee andere vierkantjes.

#als je de laatste turtle.right(90) verandert met turtle.left(45) dan worden het twee vierkantjes aan elkaar schuin over twee andere vierkantjes alleen dan anders.


turtle.reset()

for x in range(8):
    turtle.pencolor("#DD307A")
    turtle.pensize(3)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(45)

for x in range(4):
    turtle.pencolor("#982054")
    turtle.pensize(5)
    turtle.forward(200)
    turtle.right(135)
    turtle.forward(283)
    turtle.right(135)
    turtle.forward(200)

for x in range(4):
    turtle.pencolor("#FFC5DE")
    #turtle.pencolor("#641C3B")
    turtle.pensize(6)
    turtle.right(45)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(135)
    turtle.forward(283)

for x in range(4):
    #turtle.pencolor("#FFC5DE")
    turtle.pencolor("#641C3B")
    turtle.pensize(6)
    turtle.left(45)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(135)
    turtle.forward(283)

turtle.done()












