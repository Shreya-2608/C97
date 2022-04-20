import random
number=(random.randint(0,9))

chances=0
while chances <5:
    chances+=1

    guess=int(input("Enter you guess: "))
    if guess==number :
        print("Congratulations you won!")
    elif guess<number :
        print("Your guess was too low")
    else:
        print("Your guess was too high")  
    if not chances < 5:
        print('you lose! the number is', number)