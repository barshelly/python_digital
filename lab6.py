#conditions
#menu
choice=input("menu: \n------\n.1 insert number and ** it by 3\n2.insert 4IPs to a list and print it\n3. insert 4 entries to dns dictionary and print it\n.4 if a string polindrom")
if(choice=="1"):
    print ("the new number is:" + str((int(input("enter a number: ")))**3))
elif(choice=="2"):
    list_ip=[]
    list_ip.append(input("enter new ip: "))
    list_ip.append(input("enter new ip: "))
    list_ip.append(input("enter new ip: "))
    list_ip.append(input("enter new ip: "))
    print("\nthe new list:\n-----------\n" + str(list_ip))
elif(choice=="3"):
    dns_dict={}
    dns_dict.update({input("enter a url: " ): input("enter ip: ")})
    dns_dict.update({input("enter a url: " ): input("enter ip: ")})
    dns_dict.update({input("enter a url: " ): input("enter ip: ")})
    dns_dict.update({input("enter a url: " ): input("enter ip: ")})
    print("\nthe new list:\n-----------\n" + str(dns_dict))
elif(choice=="4"):
    word=input("enter a word: ")
    if(word == word[::-1]):
        print("this is plindrom")
    else:
        print("this is not polindrom")

else:
    print("enter 1-4 only!!")






