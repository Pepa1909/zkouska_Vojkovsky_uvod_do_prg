# Úvod
print("Dobrý den, tento program umí vypočítat četnosti všech znaků v zadaném textu.")

text_input = str(input("Zadejte text ke zpracování: "))

slovnik = {}

# For cyklus kontroluje každý znak v textu.
# Pokud znak ve slovníku je, započítá ho a pokud se znak obejví poprvé, vytvoří si ho jako novou hodnotu
for znak in text_input:
    if znak in slovnik:
        slovnik[znak] += 1
    else:
        slovnik[znak] = 1

print("V následujícím seznamu naleznete četnosti znaků v zadaném textu.")
print(slovnik)