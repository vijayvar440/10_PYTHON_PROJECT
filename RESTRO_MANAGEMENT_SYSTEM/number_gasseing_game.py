import random

number_to_guse = random.randint(1,100)
while True:
 try:
    guess = int(input('guess the number between 1 to 100:  '))
    if guess < number_to_guse:
      print("To low!")
    elif  guess > number_to_guse:
      print("to high!")

    else:
      print('congratulation ! you guessed the number')  
 except ValueError:
    print("please enter a valid number ")
