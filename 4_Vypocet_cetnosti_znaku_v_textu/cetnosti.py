slovnik = {}
slovo = "rozmaryn"

for pismeno in slovo:
    if pismeno in slovnik:
        slovnik[pismeno] += 1
    else:
        slovnik[pismeno] = 1
# for klic, hodnota in slovnik.items():
#     print(f"slovo {slovo} obsahuje písmeno {klic} {hodnota}-krát")
print(slovnik)