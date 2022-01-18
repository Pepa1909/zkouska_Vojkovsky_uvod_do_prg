from turtle import forward, left, exitonclick, right, speed, setpos, up, down

def vlocka(uroven, delka): 
    if uroven == 0:
        forward(delka)
        return
    vlocka(uroven-1,delka/3)
    left(60)
    vlocka(uroven-1,delka/3)
    right(120)
    vlocka(uroven-1,delka/3)
    left(60)
    vlocka(uroven-1,delka/3)

speed(0)
up()
setpos(-200,100)
down()
for _ in range(3):
    vlocka(3,350)
    right(120)
exitonclick()