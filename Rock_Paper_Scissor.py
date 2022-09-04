import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choise = [rock, paper, scissors]
your_choise = int(input("whats your choise? rock, paper or scissors. 1/2/3 \n"))
computer_choise = random.randint(0, 2)
print(f"you\n{choise [your_choise - 1]}\n")
print(f"computer \n {choise [computer_choise]}")
print(computer_choise)

if your_choise == computer_choise+1 :
  print("draw")
elif your_choise == "3" and computer_choise == "0" :
  print("you lose")
elif your_choise == computer_choise :
  print("you lose")
else : print("you win")