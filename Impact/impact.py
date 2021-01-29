print("Impact.Py - Copyright OblivionCreator 2021. This product is open source and must not be distributed without proper attribution, and may not be used for any commercial purposes.\nPlease enter the word you would like to convert to IMPACT.\nRequires Discord Nitro to use!")
word = input()
chars = list(word)
finalString = ""

for c in chars:
    c = c.lower()
    if c in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j" ,"k" , "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
        finalString = f"{finalString}:Im{c.upper()}:"
    else:
        finalString = f"{finalString}{c}"

print(finalString)