#cube project
from random import randint
from time import sleep

print("welcome to our cube game\neach turn cost 3 ILS!")
money=int(input("enter how much money do you have:\n "))
turns=(money//3)
print("you have: " + str (turns) + " turns\nyour change is: " + str(money%3) + "ILS\n")
prize=0

for i in range(turns):
    print("round number " + str(i+1) + " :\n-----------------------------\n")
    sleep(3)
    cube1=randint(1,6)
    cube2=randint(1,6)
    print("cube1: " + str(cube1) + "\ncube2: " + str(cube2) + "\n")
    if(cube1==cube2):
        if(cube1==6):
            prize=prize+1000
        else:
            prize=prize+100
    elif(cube1==1):
        prize = prize + 20
    elif(cube2==2):
        prize = prize + 40
        print("calculating your prize...")
        sleep(3)
        print("your prize: " + str(prize) + " ILS")



