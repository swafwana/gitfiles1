num=int(input("Enter the limit of list"))
list=[]
for i in range(1,num+1):
    elements=int(input("Enter element of list"))
    list.append(elements)
print(list)
print("1 for finding greatest and lowest number in list \n2 for sorting list in ascending order \n3 for creating a new list of even numbers \n ")
while 1 :
    choice=int(input("Enter choice"))
    if (choice==1):
        lowest=min(list)
        print("Lowest number is",lowest)
        greatest=max(list)
        print("Greatest number is",greatest)                           
   
    elif(choice==2):
        list1=sorted(list)
        print(list1)
    elif(choice==3):
        Even_Numbers=[]
        for i in list:
            if i%2==0:
                Even_Numbers.append(i)
        print("List of even numbers",Even_Numbers)
    elif(choice==4):
        print("You have exited the program")
        break
    else:
        print("You have entered wrong choice")

   
    
    
    




