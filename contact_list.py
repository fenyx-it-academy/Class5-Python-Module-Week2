### Merhaba,
### Ödevi biraz eksik teslim ediyorum bunun için çok özür dilerim.
### Edit bölümünü bir türlü çalıştıramadım. Ve ödevde anlamadığım yerleri biraz yardımla yapabildim.
### Sadece bilgivermek ve hatalı/eksik olan yeri bildirmek için bir not gibi yazdım bu bilgileri.
### Kolay gelsin, İyi günler hocam.


cont_list = {}
imp_cont_list = {}

while (True) :
    menu = input ("Contact List: 1\nAdd: 2\nEdit: 3\nDelete: 4\nImportant Contact List: 5\nPlease code a number!: ")         # Menü
    print (menu)

    if menu == '1' :                                       # Contact List
        for i, x in cont_list.items() :
            print (i," ",x)


    elif menu == '2' :                                     # Add
        while (True) : 
            add_name = input ("Name : ")
            
            if add_name == '1':
                break
            elif add_name.isalpha() == False :
                print("Just Letter Please...")
                continue
            else : break
        while (True) : 
            if add_name in cont_list.keys() :
                print("You have the same name...")
                ask = input ("Do you want to add a number to the this name ? Yes (Y) or No (N): ")
                print(ask)
                if ask != 'Y' :
                    break
            add_number = input ("Number : ")
            print(add_name, "-->",add_number)
            if add_number == '1' :
                break
            elif (len(add_number)!=10) or (add_number.isdigit()==False):
                print ("You should use digit and numbers must have 10 digits!")
                continue
            else:
                if add_name in cont_list.keys() :
                    cont_list[add_name].append (add_number)
                    ask_imp = input ( "Is this user important user? Yes (Y) or No (N): ")
                    print(ask_imp)
                    if ask_imp != 'Y':
                        break
                    else:
                        imp_cont_list [add_name] = [add_number]
                        break
                else:
                    ask_imp=input("Is this user important user? Yes (Y) or No (N): ")
                    print(ask_imp)
                    cont_list[add_name]=[add_number]
                    if ask_imp!='Y':
                        break
                    else:
                        imp_cont_list [add_name]=[add_number]
                        break
    
    elif menu == '3' :                                            # Edit
        while (True) :
            edit_name = input ("Which contact do you want to edit? :")
            if edit_name not in cont_list.keys():
                print("You haven't the contact")
            elif edit_name in cont_list.keys():
                name_or_number = input("Do you want to edit name or number?: ")
                if edit_name == 'name':
                    new_name = input ("Please new name!: ")
                    print(new_name)
                    if new_name.isalpha() == False:
                        print("Just Letters! ")
                    else:
                         cont_list [new_name] == cont_list[edit_name]
                         del cont_list [edit_name]

    
    elif menu == '4':                                            # Delete
        while (True) :
            del_name = input ("Which contact do ypu want to delete?: ")
            print(del_name)
            del cont_list[del_name]
            print("You deleted this contact! ")
            break

    elif menu=='5':                                                   # Important Contact List
        for i,x in imp_cont_list.items():
            print(i," ",x)