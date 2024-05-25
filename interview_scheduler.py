print("Welcome, Dear User")
print("Please enter your Interview date as 21/22/23:")
z= int(input())
print("Please enter your time slot as MOR/NOON/EVE:")
y= input()
print("Please enter your Gender as M/F/T: ")
x= input()

if z== 21:
    if y== "MOR" :
        if x== "M" or x=="m":
            print("Your Gender is Male")
            print("You are alloted Room No.1 for Interview")
        elif x=="F" or x=="f":
            print("Your Gender is Female")
            print("You are alloted Room No.2 for Interview")
        elif x=="T" or x=="t":
            print("Your Gender is Transgender")
            print("You are alloted Room No.3 for Interview")
        else:
            print("Please enter a Valid Input")
           
    elif y== "NOON" : 
        if x== "M" or x=="m":
            print("Your Gender is Male")
            print("You are alloted Room No.2 for Interview")
        elif x=="F" or x=="f":
            print("Your Gender is Female")
            print("You are alloted Room No.3 for Interview")
        elif x=="T" or x=="t":
            print("Your Gender is Transgender")
            print("You are alloted Room No.1 for Interview")
        else:
            print("Please enter a Valid Input")

    elif y== "EVE":
        if x== "M" or x=="m":
            print("Your Gender is Male")
            print("You are alloted Room No.3 for Interview")
        elif x=="F" or x=="f":
            print("Your Gender is Female")
            print("You are alloted Room No.1 for Interview")
        elif x=="T" or x=="t":
            print("Your Gender is Transgender")
            print("You are alloted Room No.2 for Interview")
        else:
            print("Please enter a Valid Input")

elif z== 22: 
    if y== "MOR":
        if x== "M" or x=="m":
            print("Your Gender is Male")
            print("You are alloted Room No.2 for Interview")
        elif x=="F" or x=="f":
            print("Your Gender is Female")
            print("You are alloted Room No.3 for Interview")
        elif x=="T" or x=="t":
            print("Your Gender is Transgender")
            print("You are alloted Room No.1 for Interview")
        else:
            print("Please enter a Valid Input")
           
    elif y== "NOON" : 
        if x== "M" or x=="m":
            print("Your Gender is Male")
            print("You are alloted Room No.3 for Interview")
        elif x=="F" or x=="f":
            print("Your Gender is Female")
            print("You are alloted Room No.1 for Interview")
        elif x=="T" or x=="t":
            print("Your Gender is Transgender")
            print("You are alloted Room No.2 for Interview")
        else:
            print("Please enter a Valid Input")
        
    elif y== "EVE":
        if x== "M" or x=="m":
            print("Your Gender is Male")
            print("You are alloted Room No.1 for Interview")
        elif x=="F" or x=="f":
            print("Your Gender is Female")
            print("You are alloted Room No.2 for Interview")
        elif x=="T" or x=="t":
            print("Your Gender is Transgender")
            print("You are alloted Room No.3 for Interview")
        else:
            print("Please enter a Valid Input")

elif z == 23:
    if y== "MOR":
        if x== "M" or x=="m":
            print("Your Gender is Male")
            print("You are alloted Room No.3 for Interview")
        elif x=="F" or x=="f":
            print("Your Gender is Female")
            print("You are alloted Room No.1 for Interview")
        elif x=="T" or x=="t":
            print("Your Gender is Transgender")
            print("You are alloted Room No.2 for Interview")
        else:
            print("Please enter a Valid Input")
           
    elif y== "NOON" : 
        if x== "M" or x=="m":
            print("Your Gender is Male")
            print("You are alloted Room No.1 for Interview")
        elif x=="F" or x=="f":
            print("Your Gender is Female")
            print("You are alloted Room No.2 for Interview")
        elif x=="T" or x=="t":
            print("Your Gender is Transgender")
            print("You are alloted Room No.3 for Interview")
        else:
            print("Please enter a Valid Input")
        
    elif y== "EVE":
        if x== "M" or x=="m":
            print("Your Gender is Male")
            print("You are alloted Room No.2 for Interview")
        elif x=="F" or x=="f":
            print("Your Gender is Female")
            print("You are alloted Room No.3 for Interview")
        elif x=="T" or x=="t":
            print("Your Gender is Transgender")
            print("You are alloted Room No.1 for Interview")
        else:
            print("Please enter a Valid Input")

else:
    print("Please enter Valid Input")