import random
from os import system
import sys
import time
#replit.com/@rounakkole

def printf(text, delay=0.05):
    for t in text:
        sys.stdout.write(t)
        sys.stdout.flush()
        time.sleep(delay)
    print()

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
"error"]

title = """
 _    _                                         
| |  | |            welcome to                  
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       
"""



word_list = ["tiger", "baboon", "camel", "apple", "lime", "purple", "water", "mouth", "secret", "freedom", "code", "knight", "shiny", "gleam", "chewed","growl", "winner", "guess", "hanged", "happy", "angry", "lying", "bird", "king", "queen", "teacher","grateful", "picky", "hoping", "guessing", "words", "lists", "variable", "mango", "framed", "default", "python", "language", "robot", "sleeping", "songs", "magic", "grass", "bawling", "minute"]

play = True
while play is True :

  system('clear')
  word = word_list[random.randint(0,44)]
  #print(word) 
  word_len = len(word)
  dash = ""
  for n in range(word_len) :
    dash += "_ "

  print(title)
  printf(dash)
  guesses = ""
  guesses1 = ""
  win = False
  result = "lose"
  lives = 5
  live = 0
  counter = 0



  while lives > 0 and win is False :
    word_ip = input("guess a character \n").lower()
    lenght = len(word_ip)

    #one word at a time
    number = ord(word_ip)


    guesses1 = ""
    guesses1 += word_ip
    system('clear')





    double = False
    for guess1 in guesses1 :
      for guess2 in guesses :
        if guess1 == guess2 :
          double = True
          printf("you've already guessed that")
  
    if double == False :
      guesses += word_ip


    counter5 = 0
    correct = ""
    for ip in word:
      check = False
      for op in guesses:
        if ip == op and check is False :
          correct += ip + " "
          check = True
          counter5 += 1
      if check is False :
        correct += "_ "



  


    counter = 0
    for op in guesses :
      count = False
      for ip in word :
        if ip == op :
          count = True
      if count is True :
        counter += 1
      


    if word_len == counter or word_len == counter5:
      win = True



    live += 1
    lives = 5 + counter - live
    printf(f"Guesses: {guesses}")
    printf(f"Remaining guesses: {lives}")





    loop = False
    for ip in word :
      if word_ip == ip and loop is False :
        printf("Right guess\n")
        loop = True
    if loop is False :
      printf("Wrong guess\n")





    printf(correct)
    if lives < 6 :
      print(stages[lives])
    else :
      print(stages[5])




  system('clear')
  if win == True :
    result = "Win"
  else :
    printf(stages[0])
  printf(f"Answer: {word}")
  printf(f"You {result}")

  next=input("continue playing? y / n \n").lower()
  if next == "n" :
    play = False
    time.sleep(1)
    printf("\ngame end")