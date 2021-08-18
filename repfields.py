age = 24
print("My age is " + str(age) + " years") # shows string coersion

print("My age is {0} years".format(age)) # uses .format to use replacement fields

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))


# String formatting can be used in replacement fields
for i in range (1, 13):
      print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3)) # ** means multiplied by

#output is correct, but ugly, so we can indicate width of each field to improve readability:
for i in range (1, 13):
      print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3)) # :digit is the width of the field

for i in range (1, 13):
      print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i**2, i**3)) #< justified; ^ centers the value

print()
print()

print("Pi is approximately {0:12}".format(22/7))


