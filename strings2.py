# The str data type
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])  # recall, strings are an array, so string[3] is the char at index 4 (arrays start counting at 0)
print(parrot[4])
print(parrot[9]) # this is the index of the space between Norwegian Blue
print(parrot[3])
print(parrot[6])
print(parrot[8])
print()
print()
print()
# can also index from the end of the string. So, parrot[-1] is the final 'e' on the end.
print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print()
print()
# can also subtract string length to end up with negative indexing:
print(parrot[3-14])
print(parrot[4-14])
print(parrot[9-14])
print(parrot[3-14])
print(parrot[6-14])
print(parrot[8-14])
print()
print()
# len(object) also returns the length of the string
print(parrot[3 - len(parrot)])

# SLICING:
print(parrot[0:6]) # returns index[0] up to but NOT including index[6]
# now we want to print 'we'
print(parrot[3:5])
# print the word 'blue'
print(parrot[10:14])

print(parrot[:])

print(parrot[-4:-2]) # Bl
print(parrot[-4:12]) # Bl

# can also use steps when slicing:

print(parrot[0:6:2])  # Nre
print(parrot[0:6:3])  # Nw

# a practical application:

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(values)
print([int(val) for val in values])

