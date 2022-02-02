from turtle import forward, left, exitonclick, right, speed, setpos, up, down

def vlocka(uroven, delka): 

    """Nakreslí Kochovu vločku zadané úrovně a zadaného rozměru."""

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

print("Dobrý den, tento program nakreslí Kochovu vločku. Úroveň i velikost si budete moci zvolit.")

uroven = int(input("Zadejte úroveň Kochovy vločky, kterou chcete vykreslit (úroveň vyšší než 4 již trvá dlouho): "))
velikost = float(input("Zadejte velikost Kochovy vločky (doporučená velikost je 200-500): "))

# Změna rychlosti, aby se vločka kreslila co nejrychleji a také změna výchozích souřadnic, aby větší vločky nebyly mimo monitor
speed(0)
up()
setpos(-200,100)
down()

# For cyklus zaručující, že vzniklý tvar bude opravdu vločka
for _ in range(3):
    vlocka(uroven,velikost)
    right(120)
exitonclick()