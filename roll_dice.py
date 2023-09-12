import random
roll = random.randint(1,6)

guess = (int('Guess the dice roll:\n)'))
if guess == roll:
  print("Correct! They rolled a " + str(roll))
