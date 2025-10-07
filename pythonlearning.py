import random
def result():
    goalnumbers = [4,5,6,8,9,10]
    craps = [2,3,12]
    goalnumber = 0
    while True:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        s = dice1 + dice2
        if s not in goalnumbers and goalnumber == 0:
            if s == 7 or s == 11:
                print(f"The sum of dice is {dice1} + {dice2} = {s}")
                print("You won")
                break
            if s in craps:
                print(f"The sum of dice is {dice1} + {dice2} = {s}")
                print("You lost!")
                break
        elif s == goalnumber:
             print(f"The sum of dice is {dice1} + {dice2} = {s}")
             print("You won")
             break
        elif s in goalnumbers:
            if goalnumber != 0:
                print(f"The sum of dice is {dice1} + {dice2} = {s}")
                continue
            else:
                goalnumber = s
                print(f"The sum of dice is {dice1} + {dice2} = {s}")
                print(f"Now your goal number is {s}")
        elif s == 7 and goalnumber != 0:
            print(f"The sum of dice is {dice1} + {dice2} = {s}")
            print("You lost!")
            break
        else:
            print(f"The sum of dice is {dice1} + {dice2} = {s}")
result()