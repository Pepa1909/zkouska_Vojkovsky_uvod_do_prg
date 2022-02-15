def counts():

    """Counts the number of unique characters in the input text; returns a dictionary"""

    adict = {}
    input_text = str(input("Zadejte text ke zpracování: ")).lower()

    # For loop iterates over every character in input text
    # If a character already is a key in the dictionary, add 1 to value; if it's a new character, make a new key and set its value to 1
    for char in input_text:
        if char in adict:
            adict[char] += 1
        else:
            adict[char] = 1

    print("V následujícím slovníku naleznete četnosti znaků v zadaném textu:")
    return adict

# Starting info
print("Dobrý den, tento program umí vypočítat četnosti všech znaků v zadaném textu.")

# Main application
print(counts())