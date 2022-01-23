# Úvod
print("Dobrý den, tento jednoduchý program umí vypočítat četnost všech znaků v zadaném textu.")

slovo = input("Zadejte text ke zpracování: ")

slovnik = {}

# For cyklus projede každý znak v textu.
# Pokud znak ve slovníku je, započítá ho a pokud se znak obejví poprvé, vytvoří si ho jako novou hodnotu
for znak in slovo:
    if znak in slovnik:
        slovnik[znak] += 1
    else:
        slovnik[znak] = 1

print(slovnik)