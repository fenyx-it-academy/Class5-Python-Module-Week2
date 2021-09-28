def print_menu():
    print("PHONE BOOK")
    print('1. Phone Numbers')
    print('2. Add Name and Phone Number')
    print('3. Edit a Phone Number')
    print('4. Delete a Phone Number')
    print()
numbers = {}
numbers2=()
l=list(numbers2)
menu_choice = 0
print_menu()
while True:
    menu_choice = int(input("Type in a number (1-4): "))
    if menu_choice == 1:
        print("Phone Numbers:")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x])
        print()
    elif menu_choice == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = int(input("Number: "))
        if len(str(phone))==10 and name.isalpha():
            numbers[name] = phone
        else:
            print("Please enter your phone number in 10 digits and your Name in letters only.")
    elif menu_choice == 3:
        name = input("Enter name you want to edit: ")
        newphone=input("Enter new number:")
        print("Edit Number")
        newname=input("Enter new name:")
        if name in numbers:
            numbers[newname]=newphone
            del(numbers[name])
        else:
            print(name, "was not found")
    elif menu_choice == 4:
        print("Delete Name and Number")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
