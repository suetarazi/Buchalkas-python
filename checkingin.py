parrot = ("Norwegian Blue").casefold()
#.casefold() is the same as .tolower in C-sharp

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")

