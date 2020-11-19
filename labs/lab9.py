#from random import randint
#from time import sleep

def menu():
    while(True):
        choice=input("menu:\n----------\n1.dogs details\n2.friends list\n.3N azzeret\n")
        if (choice=="1"):
            dogs()
        elif(choice=="2"):
            friends()
        elif(choice=="3"):
            azzeret()

        else:
            print("enter 1-3 only!!")
            continue
        exit=input("do you want to exit? yes/no\n")
        if(exit=="yes"):
            break
        else:
            print("welcome back\n")
    print("bye bye..")


def dogs():
    name=input("enter dogs name: ")
    age=int(input("enter dog's age: "))
    print("\ndog's name: " + name + "\ndog's age: " + str(age*7) + "\n")

def friends():
        list_friends=[]
        for i in range(5):
            list_friends.append(input("enter a friend's name: "))
        name=input("enter new name: ")
        if(name in list_friends):
            print(name + "is inside the list\n")
        else:
             print(name + "isn't inside the list\n")

def azzeret():
            num=int(input("enter a number: "))
            sum=1
            for i in range(1,num+1):
                sum=sum*i
            print(str(num) + " azzeret is: " + str(sum) + "\n")


menu()




