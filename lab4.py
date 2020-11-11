#create a list  with 4 details about you: name,age,mail,phone and print it to the screen
#then create another list with 2 ips, then add 3 more ips, pop the 3rd ip and print how many
# ips do we have and print them.

detail_list=["bar shelly",22,"barshelly731@gmal.com","0504757284"]
print("full name: " + detail_list[0] + "\nmy age: " + str(detail_list[1]) + "\nmy mail: " + detail_list[2] + "\nmy phone: " + detail_list[3])

IP_list=["192.168.1.1","192.168.2.2"]
print(IP_list)

IP_list.append("3.3.3.3")
IP_list.append("2.2.2.2")
IP_list.append("4.4.4.4")
print(IP_list)
IP_list.pop(2)
print(IP_list)
print("IP list length is: " + str(len(IP_list)) + "\nand the IP list: " + str(IP_list))