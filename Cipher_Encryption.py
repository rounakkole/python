
from os import system

Dict = {}

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


flag1 = True
def encrypt (text1, shift1) :
  encryption = ""
  
    
  for texts in text : 
    flag1 = True
    for position in range(26) :
      alphabet1 = alphabet[position]
      if texts in alphabet:

        if alphabet1 == texts :
          #print(texts)
          encryption += alphabet[position + shift1]
          #print(position)
      elif flag1 :
          encryption += texts
          flag1 = False
  print("\n encryption:")
  print(encryption)

def decrypt (text1, shift1) :
    decryption = ""
   
    for texts in text :
      flag1 = True
      for position in range(26) :
        alphabet1 = alphabet[position]
        if texts in alphabet:
          if alphabet1 == texts :
            decryption += alphabet[position - shift1]
            #print(position)
        elif flag1 :
          decryption += texts
          flag1 = False
    print("\n decryption:")
    print(decryption)
i = 0
while i<25 :
  i = i+1

  direction = input("\n \nEnter 'en' to ENCRYPT, type 'de' to DECRYPT:\nen / de ?\n  ")
  system('clear')

  if direction == "en" :
    text = input("\nEnter message:\n  ").lower()
    shift = int(input("\nEnter secret number:\n  "))

    Dict[i] = {'en' :{'message' : text , 'shift' : shift }}
    shift1 = shift % 26
    text1 = text
    encrypt(text1, shift1)
  elif direction == "de" :
    text = input("\nEnter message:\n  ").lower()

    shift = int(input("\nEnter secret number:\n  "))
    Dict[i] = {'de' :{'message' : text, 'shift' : shift }}
    shift1 = shift % 26
    text1 = text
    decrypt(text1, shift1)
  elif direction == "history" :
    print(Dict)
    #print(Dict['direct']['message']['shift'])
  else : print("syntax error    en / de ?")

