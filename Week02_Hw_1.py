
##from ast import NameConstant

Contact_Information={}
Name_List=[]
Number_List=[]

def Name_Fon():
    while True:
        Name = input("What is your name? ")
        if Name.isalpha():

            Name_List.append(Name)   
            return Name
        
        else:
            print("Please use only letters, try again")

def Number_Fon():
    
    while True:
        Number=input("What is your Number? ")
        if Number.isnumeric():

            if len(str(Number))==10: 
                Number_List.append(Number)

                x=input("does your friend another numbers Y/N : ")
                x=x.lower()

                if x=='y':
                    Number=Number_Fon()
                    for i in Number_List:

                        return Number_List.append(Number)
                        
                else:
                    return Number

            else:
                print("10 digits Please")

        else:
            print("Please use only number, try again")
        



n = int(input("Enter how many names you want to enter: "))

for i in range(n):
    
    Name=Name_Fon()
    
    Number=Number_Fon()
    #Number_List.append(Number)
    Contact_Information[Name]=Number_List
    
    '''x=input("does your friend another numbers Y/N : ")
    x=x.lower()

    if x=='y':

        Number_List.append(Number)
        Number=Number_Fon()
    
        Number_List.append(Number)
        Contact_Information[Name]=Number_List
    else:
        continue'''
    

print(Contact_Information)
