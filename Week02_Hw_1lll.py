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
                return Number
            else:
                print("10 digits Please")
        

n = int(input("Enter how many names you want to enter: "))

for i in range(n):

	key = Name_Fon()
	value = Number_Fon()
	Contact_Information[key] = value

print(Contact_Information)