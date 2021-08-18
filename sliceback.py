letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]  # goes up to but NOT including the stop value. Therefore, letter a won't print!
print(backwards + letters[0]) # this will allow 'a' to print, however there's a better way:
backwards = letters[25::-1] # Python will default all the way to the beginning of the string if you don't specify a step
print(backwards)
# Python Idiom = reversing a sequence: [::-1]
backwards = letters[::-1] # this is the BEST syntax
print(backwards)

# create a slice that produces 'qpo'
qpo_slice = letters[-10:-13:-1]
print(qpo_slice)

# slice the string to produce 'edcba'
edcba_slice = letters[4::-1]
print(edcba_slice)

# slice the string to produce the last 8 characters, in reverse order.
last_8_slice = letters[25:17:-1]  # letters[:-9:-1] is a cleaner solution!!!
print(last_8_slice)

#Common Python Idioms:
print(letters[-1:]) # prints the last letter of the sequence
print(letters[:1]) # prints the first letter of the sequence

# String Operators
# Sequence must be ordered.

string1 = "she's"
string2 = "eating"
string3 = "ice cream"

print(string1 + string2 + string3)
print("shes" "eating" "ice cream") # this is the same as the previous line
