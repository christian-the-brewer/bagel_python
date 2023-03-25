#bagel game

import random

DIGITS = 3 #constant for digits in number
GUESSES = 10 #max guesses

game = True

print('''
Bagels, a deductive logic game.
 
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Pico           One digit is correct but in the wrong position.
  Fermi          One digit is correct and in the right position.
  Bagels         No digit is correct.
  
For example, if the secret number was 248 and your guess was 843, the
  clues would be Fermi Pico.'''.format(DIGITS))


def get_secret_number():
  #pick random numbers from list, then remove them after.
  nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',]
  i = 0
  secret_number_list = []
  while i < DIGITS:
    number = random.choice(nums)
    secret_number_list.append(number)
    nums.remove(number)
    i += 1
    print(number) #TEST
  print(secret_number_list) #TEST
  return ''.join([num for num in secret_number_list])

def guess_correct(guess):
  #check user guess to see if guess is 'in' secret_number and return bool
  if guess in secret_number:
    return True
  else:
    return False
  
  
while game: #game loop
  secret_number = get_secret_number() #secret number
  guesses = GUESSES #keep track of user guesses
  
  while guesses > 0:
    user_guess = input(f"Enter a {DIGITS} digit guess!: ")
    print(secret_number) #TEST
    if guess_correct(user_guess):
      tries = GUESSES - guesses
      print(f"You got it right in {tries} tries!")
      break
    else:
      
  playing = input("Play again? y/n: ")
  if playing.lower() == 'n' or playing.lower() == 'no':
    game = False

  