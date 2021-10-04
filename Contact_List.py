
contact = {}
importantcontact = {}
selection = input("select : add ,edit, delete")
while True:
    if selection == "add":
            while True:
                name = input("name:")
                if name.isalpha() == False:
                    print("invalid entry! please try again")
                else:
                    break
            while True:
                number = input("number:")
                if number.isnumeric()==False or len(number) != 10:
                    print("invalid entry! please try again")
                else:
                    break
            important=input("do you want to add important list:y/n")
            if important == "y":
                importantcontact.update({name :number}) 
                contact.update({name :number}) 
            elif important=="n":
                contact.update({name :number}) 
    print("Registration Successful")
    if selection == "edit":
        name=input("write the name of person to edit:")
        while True:
                number2 = input("write the second number of person to edit")
                if number2.isnumeric()==False or len(number2) != 10:
                    print("invalid entry! please try again")
                else:
                    break
        important=input("do you want to add important list:y/n")
        if important == "y":
            importantcontact[name]=[number, number2]
            contact[name]=[number, number2]
        elif important=="n":
            contact[name]=[number, number2]
        print(number2,"added ",name,"succesfully!")
    elif selection == "delete":
        delname=input("delete name:")
        contact.pop(delname)
        importantcontact.pop(delname)
        print(delname,"Has been succesfully deleted!")

    impartantcontact = tuple(importantcontact.items())
    print (contact)
    print (impartantcontact)
