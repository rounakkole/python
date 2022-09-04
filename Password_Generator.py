#Password Generator Project
import random
from os import system
import sys
import time

def printf(text, delay=0.05):
    for t in text:
        sys.stdout.write(t)
        sys.stdout.flush()
        time.sleep(delay)
    print()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


printf('''

▒█▀▀█ █▀▀█ █▀▀ █▀▀ █░░░█ █▀▀█ █▀▀█ █▀▀▄ 
▒█▄▄█ █▄▄█ ▀▀█ ▀▀█ █▄█▄█ █░░█ █▄▄▀ █░░█ 
▒█░░░ ▀░░▀ ▀▀▀ ▀▀▀ ░▀░▀░ ▀▀▀▀ ▀░▀▀ ▀▀▀░''')

print("Password Generator!\n")
nr_letters= int(input("include CHARACTERS: ")) 
nr_symbols = int(input(f"include SYMBOLS: "))
nr_numbers = int(input(f"include NUMBERS: "))


pass_len = nr_letters + nr_numbers + nr_symbols
counter = 0
counter1 = 0
counter2 = 0
counter3 = 0
password = ""
while counter < pass_len :
  pass_nr = random.randint(0, 2)
  counter += 1
  
  if pass_nr == 0 and counter1 < nr_letters:
    letters_nr = random.randint(0, 50)
    counter1 += 1
    password += letters[letters_nr] 
  elif pass_nr == 1 and counter2 < nr_symbols:
    symbols_nr = random.randint(0, 8)
    counter2 += 1
    password += symbols[symbols_nr]
  elif pass_nr == 2 and counter3 < nr_numbers:
    numbers_nr = random.randint(0, 8)
    counter3 += 1
    password += numbers[numbers_nr]
  else : counter -= 1



printf(f"\npassword length {nr_letters, nr_numbers, nr_symbols} = {pass_len}")
time.sleep(1)
print(password)






