print("Impact.Py - Copyright OblivionCreator 2021. This product is open source and must not be distributed without proper attribution, and may not be used for any commercial purposes.\nRequires Discord Nitro to use!\nPlease enter the word you would like to convert to IMPACT.")

cont = True

def conv(word):
    chars = list(word)
    finalString = ""

    for c in chars:
        c = c.lower()
        if c in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j" ,"k" , "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
            finalString = f"{finalString}:Im{c.upper()}:"
        else:
            finalString = f"{finalString}{c}"

    print(f"Here\'s your impact text!\n{finalString}\nTo exit the program, type 'exit', or if you wish to convert more text, enter the text you wish to convert.")

while cont == True:

    word = input()

    if word.lower() == 'exit':
        exit(1)
    else:
        conv(word)

