"""Contact List """

contacts = dict() # Our contacts will be in dict. 
while True : 
    print("Contact Program . Follow the options\n1-See list of contacts\n2-Add Person\n3-Delete Person\n4-Edit Person\n5-Exit")

    choice = input ("Write between 1-5 : ")  #Takes choice
    
    if choice == "2" :  #Add Person
        while True :    #name loop
            print("Use in name only alphabet ")
            name = input("Name : ")
            if name.isalpha():              #Checked is only alpha
                
                while True:                 #number loop
                    number = input("Number : ")
                    if number.isdigit() and len(number)== 10 :       #checked is only digit
                        while True:             #imported question loop
                            imported_question = input ("is that person imported for you ? Y/N : ") 
                            if imported_question == "Y" or imported_question == "y" :    #checked is imported situation
                                contacts[name] = (number,)
                                print("Added succesfully")
                                break # End imported question's loop
                            elif imported_question == "N" or imported_question == "n" : 
                                contacts[name]= [number]
                                print("Added succesfully")
                                break #End imported question's loop
                            else :
                                print("invalid")
                                continue
                        break             #End number's loop      
                    else:
                        print("Write only numeric or 10 digit")
                        continue
                break # End name's loop
            else :
                print("Name is not only alphabet try again")
                continue
    elif choice == "1" : #Shows contact of list
        for name,number in contacts.items():
            print(name , "->",number)
    elif choice == "4" : #Edit contact of list
        name = input("Enter the name you want to edit : ")
        if name in contacts.keys():
            print(f"name : {name}\nNumber :{contacts[name]}")
            
            while True : 
                changeoption = input ("1-Edit Number\n2-Edit Name\n3-Exit")
                if changeoption == "1" : 
                    while True : 
                        newnumber = input("Number : ")
                        if newnumber.isdigit() and len(newnumber)== 10 :
                            deletechoice = input("the all numbers will deleted are you sure ? : Y/N")
                            if deletechoice == "y" or deletechoice == "Y" : 
                                contacts[name] = [newnumber]
                            elif deletechoice == "n" or deletechoice == "N" :
                                print("it didnt change.")
                                break
                            else : 
                                print("invalid")
                                continue
                        else : 
                            print("invalid number")
                            continue
                        break
                elif changeoption == "2":
                    while True : 
                        newname = input("New Name : ")
                        if newname.isalpha(): 
                            contacts[newname] =contacts[name]
                            del contacts[name]
                            break
                        elif not newname.isalpha() :
                            print("invalid name try again")
                            continue
                        else : 
                            print("invalid action")
                            break
                elif changeoption == "3" : 
                    break
                else : 
                    print("invalid action")
                    continue
    elif choice == "5":
        break          
    elif choice == "3" : 
        
        while True :
            name = input("Enter the name you want to delete : ")
            if name in contacts.keys():
                print(f"name : {name}\nNumber :{contacts[name]}")
                del contacts[name]
                print(f"{name} is deleted")
                break
            else : 
                print("There is no person who has this name ")
                continue

    else : 
        print("Invalid choice . Use 1-5")


         
