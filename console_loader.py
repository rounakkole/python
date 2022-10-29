def print_loader(progress, total):
    #from os import system

    percentageR = total / 100
    temp = progress / percentageR

    if (temp <= 100):
        #system('clear')
        print("|", end="")
        while (temp > 4):
            print("█", end="")
            temp = temp - 5

        remainder = 100 - ((progress / percentageR) - temp)
        while (remainder > 4):
            print("-", end="")
            remainder = remainder - 5

        print("|", end="  ")
        print(int(progress / total * 100), end="\n \n")

  #from console_loader import print_loader
  #print_loader(25, 100)
        
