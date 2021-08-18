print('We can use "quotes" in strings')
print('We can store' + ' concatinations in strings')
print('hello' + 'world')

hello = "Hello"
cat_name = "Pinot"
print(hello + ' ' + cat_name)

#title = input('Please enter your name')

#print("hello " + " " + title)

splitString = "This string has been \nsplit over \nseveral \nlines"
print(splitString)
#can also just print() to create a line space:
print()
print()
print()
tabbedString = "1\t2\t3\t4"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')

print("C:\\Users\\timbuchalkaa\\notes.txt")

age=14
name='Pinot'
real_age=14.5

print(type(age))
print(type(name))
print(type(real_age))

# Operator Precedence: PEMDAS from math class still holds true!

# f-strings2

age = 24
name = "Sue"
print(name + f" is {age} years old") # the f before the string makes this an f-string and basically works like a template literal :)
print()
print()

first = "john"
last = "cleese"
age = 78
print(first + last + str(age))

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5]) # slice starts at the first char and includes every 5th char



