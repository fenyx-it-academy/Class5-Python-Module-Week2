def print_menu():
    print("______PHONE BOOK_________")                                                     
    print('1. Show Phone Numbers')
    print('2. Add a Phone Number')                                                                           
    print('3. Edit a Phone Number')
    print('4. Delete a Phone Number')
    print('5. Show Important numbers ')
    print()

numbers = {}
numbers2=()
l=list(numbers2)
menu_choice = 0
print_menu()
while True:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        print("Telephone Numbers:")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x])
        print()
    elif menu_choice == 2:
        print("Add Name and Number")     
        name = input("Name: ")
        phone = int(input("Number: "))                                                             #Sadece sayı girişi kabul edecek
        if len(str(phone))==10 and name.isalpha():                                                 #Telefon numarasını sadece 10 karakter girebilir ve ismi sadece küçük veya büyük harflerden oluşabilir.
            numbers[name] = phone
            answer=input("Girdiğiniz veriler önemli ise 'Y' harfine tıklayın?")                    #Girilen bilgiler önemli ise ve bilgilerin değişmemesini istiyorsa sözlük sonradan değiştirilebileceği için veriler ayrı bir tuple da daha saklanır.
            if answer=='Y':
                l.append(numbers)
            else:
                continue
        else:
            print("lütfen telefon numarasını 10 haneli ve Adınızı sadece harflerden oluşacak şekilde giriniz")
            
    elif menu_choice == 3:
        name = input("Düzenlemek istediğiniz ismi giriniz: ")
        newphone=input("Yeni numarayı giriniz:")
        print("Edit Number")
        newname=input("Yeni ismi giriniz:")
        if name in numbers:
            numbers[newname]=newphone
            del(numbers[name])

        else:
            print(name, "was not found")
    
    elif menu_choice == 4:
        print("Remove Name and Number")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
    
    elif menu_choice == 5:
        print("Important Numbers")
        print(l)