import random

jackpot=random.randint(1,100)
#print(jackpot)

guess=int(input("Let's guess a Number"))
counter=1

while guess!=jackpot:
    counter+=1
    if guess>jackpot:
        print("Guess Lower")
        guess=int(input("Let's guess a Number"))

    else:
        print("Guess Higher")
        guess=int(input("Let's guess a Number"))


print("Congrats",counter)
