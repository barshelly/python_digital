from random import randint
counter=0
while(True):
    choice=input("menu: \n----------------\n1.printing 100 numbers\n2.check fibo\n.3 randint numbers until we get 12 or we count 10 times\n")
    if(choice=="1"):
        for i in range(1,101):
            print(i)

###########################################
    elif(choice=="2"):
       # fibo = [1, 2, 3, 5, 8, 13, 21]

         fibo=[]
         for i in range(7):
              fibo.append(int(input("enter a number: ")))
         boolean = "True"
         for i in range(2, len(fibo)):
            print(fibo[i])
            print(fibo[i - 1])
            print(fibo[i - 2])
            print("\n")
            if fibo[i] != (fibo[i - 1] + fibo[i - 2]):
                boolean = "false"
                break
         if boolean == "true":
            print("it is fibo series")
         else:
           print("it isnt fibo seires")
 #################################################################

    elif(choice=="3"):
      counter = 1
      num=randint(1,12)
      while(num!=12 and counter<11):
          print("counter:" + str(counter) + " number:" + str(num) + "\n")
          counter=counter+1
          num = randint(1, 12)
      else:
          print("enter 1-3 only!!")
          continue
    exit=input("do you want to exit? yes/no\n")
    if(exit=="yes"):
        print("thank you and bye bye..\n")
        break























fibo=[1,2,3,5,8,13,21]

boolean="True"
for i in range (2,len(fibo)):
    print(fibo[i])
    print(fibo[i-1])
    print(fibo[i-2])
    print("\n")
    if fibo[i]!=(fibo[i-1]+fibo[i-2]):
        boolean = "false"
        break
if boolean=="true":
    print("it is fibo series")
else:
    print("it isnt fibo seires")
