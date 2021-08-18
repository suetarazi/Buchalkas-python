answer = 5

print("Please guess a number between 1-10: ")
guess = int(input())

if guess == answer:
    print("yup, you got it!")
else:
    if guess < answer:
        print("please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Yup!")
    else:
        print("Sorry, try again!")



# if guess != answer:
#     if guess < answer:
#         print("please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("yup, you got it!")
#     else:
#         print("Sorry, try again!")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("You guessed it!")
#     else:
#         print("Sorry you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Yup, you're right!")
#     else:
#         print("you have not guessed correctly")
# else:
#     print("You got it!")

