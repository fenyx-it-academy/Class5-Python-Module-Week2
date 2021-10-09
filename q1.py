# # Contact List
# Write a program that stores the names and phone numbers.
# The program should have a menu which includes following options for the contacts.
# - add
# - edit
# - delete
# * Start with an empty dictionary in order to store names and phone numbers as pairs.
# * Program should take the names and phone numbers with the input() function.
# * Be sure that names have only letters(Uppercase or lowercase). No numbers.. No characters or any other thing.. Just letters.. Program should ask for a new input if the input is not valid.
# * Phone numbers must have 10 digits. Otherwise the program should not accept the input and should ask the user to enter the number again.
# * There must not be a name twice in the list. If a person has two or more phone numbers, then the program should store them for the same name. (So you must use lists somewhere.)
# * While taking input, ask user whether the contact is important or not. If the input is important, store them both in the dictionary and another place where we can be sure of the security of the input. So we do not lose these important contacts forever.

contacts_list={}
important_contact_list={}
while True:
    menu=input("Contract List: 1\nImportant Contract List: 2\nAdd: 3\nEdit: 4\nDelete: 5\nQuit: 6")
    print(menu)
    if menu=='1':
        for i,x in contacts_list.items():
            print(i,"->",x)
    elif menu=='2':
        for i,x in important_contact_list.items():
            print(i,"->",x)
    elif menu=="3": #Add
        while True:
            name=input("Name *(Just letters) (quit 1): ")
            print(name)
            if name=='1':
                break
            elif name.isalpha()==False:
                print("Just letters...")
                continue
            else: break
        while True:
            if name in contacts_list.keys():
                print("This name added already...")
                ask=input("Do you want to add number to this name ? y(yes) or n(no)")
                print(ask)
                if ask!='y':
                    break
            number=input("Number *(Just digits) (quit 1): ")
            print(number)
            if number=='1':
                break
            elif (len(number)!=10) or (number.isdigit()==False):
                print("Numbers must have 10 digits or Just Digit...")
                continue
            else:
                if name in contacts_list.keys():
                    contacts_list[name].append(number)
                    ask_imp=input("If the user is important please click 1 or click any other key: ")
                    print(ask_imp)
                    if ask_imp!='1':
                        break
                    else:
                        important_contact_list[name]=[number]
                        break
                else:
                    ask_imp=input("If the user is important please click 1 or click any other key: ")
                    print(ask_imp)
                    contacts_list[name]=[number]
                    if ask_imp!='1':
                        break
                    else:
                        important_contact_list[name]=[number]
                        break
        
    elif menu=='4': #Edit
        while True:
            edit_name=input("Which your contact would you like to edit ?")
            print(edit_name)
            if edit_name not in contacts_list.keys():
                print("There is no any contact for this contact name ?")
            elif edit_name in contacts_list.keys():
                number_or_name=input("What do you want to edit ? Please type name for name or number for number...")
                print(number_or_name)
                if number_or_name=='number':
                    for i in contacts_list[edit_name]:
                        print(i)
                    ask_number=input('Which row do you want to edit ? (1,2,3,...) ')
                    print(ask_number)
                    if (int(ask_number)>len(contacts_list[edit_name])) or (int(ask_number)<1) or (ask_number.isdigit()!=True):
                        print("You made a mistake...")
                        break
                    else:
                        while True:
                            new_number=input("New number *(Just digits) (quit 1): ")
                            print(new_number)
                            if number=='1':
                                break
                            elif (len(number)!=10) or (number.isdigit()==False):
                                print("Numbers must have 10 digits or Just Digit...")
                                continue
                            else:
                                contacts_list[edit_name][int(ask_number)-1]=new_number
                                break
                        break

                elif number_or_name=='name':
                    new_name=input("New name: ")
                    print(new_name)
                    if new_name.isalpha()==False:
                        print("Just letters...")
                        break
                    elif new_name in contacts_list.keys():
                        print("This name added already...")
                        break
                    else:
                        contacts_list[new_name]=contacts_list[edit_name]
                        del contacts_list[edit_name]
                        break
    elif menu=='5':
        delete_name=input("Which contact do you want to delete ?")
        print(delete_name)
        del contacts_list[delete_name]
        print(delete_name, ' Being deleted...')
    elif menu=='6':
        break