contacts = {}
important_contacts = {}

while True:
    menu=input("important_contacts: 1\ncontacts: 2\nadd: 3\nedit: 4\ndelete: 5\nquit: 6:")
    print(menu)
    if menu == "1":
        for x,z in important_contacts.items():
            print(x,':',z)
    elif menu == "2":
        for x,z in contacts.items():
            print(x,':',z)
    elif menu == "3":
        while True:
            name = input("enter a name:")
            print(name)
            if name.isalpha() == False:
                print("only with letters")
                continue
            else:
                break
        while True:
            if name in contacts.keys():
                print("There is already someone with this name.")
                ask = input("would you like to add a number ('y' / 'n')")
                if ask == 'y':
                    break
            number = input("enter a number")
            print(number)
            if len(number) != 10:
                print("only 10 digits")
                continue
            else:
                if name in contacts.keys():
                    contacts[name].append(number)
                    important = input("Is this an important contact? (y, n)")
                    print(important)
                    if important == "y":
                        important_contacts[name] = [number]
                        break
                    else:
                        break
                else:
                    contacts[name] = [number]
                    important = input("Is this an important contact? (y/ n)")
                    print(important)
                    if important == "y":
                        important_contacts[name] = [number]
                        break
                    else:
                        break
    elif menu == "4":
        while True:
            edit = input("enter the contact you would like to edit.:")
            print(edit)
            if edit not in contacts.keys():
                print("Contact is not found.")
            elif edit in contacts.keys():
                edit_contact = input("edit name or number:")
                print(edit_contact)
                if edit_contact == "number":
                    for i in contacts[edit]:
                        print(i)
                    edit_number = input("Which line would you like to change? 1,2,3")
                    print(edit_number)
                    if (int(edit_number)>len(contacts[edit])) or (int(edit_number)<1) or (edit_number.isdigit()!=True):
                        print("It is invalid.")
                        break
                    else:
                        while True:
                            new_number = input("enter a new number:")
                            print(new_number)
                            if len(edit_number) != 10:
                                print("only with digits")
                                continue
                            else:
                                contacts[edit][int(edit_number) - 1] = new_number
                                break
                elif edit_contact == "name":
                    new_name = input("enter a new name")
                    print(new_name)
                    if new_name.isalpha()==False:
                        print("only with letters")
                        break
                    elif new_name in contacts.keys():
                        print("The name is already in the contacts.")
                        break
                    else:
                        contacts[new_name] = contacts[edit]
                        del contacts[edit]
                        break
    elif menu == "5":
        delete_name = input("Which contact to delete?")
        print(delete_name)
        del(delete_name)
        del contacts[delete_name]
        print("Contact is deleted.")                
    elif menu == "6":
        break