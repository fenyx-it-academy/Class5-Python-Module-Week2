guide = {}     #Ana listemiz
secguide={}    #Degismeyenleri sakladigimiz yer

while True:
    name = input("Add name:")
    if name in guide:      #Eger isim zaten girilmisse burdan devam edip 2.numarayi ekletecek,kisiyi silecek yada ilk numarayi degistirecek
        edit = input("The name already exists,wanna add 2nd number press 'A',for delete 'D',for renew press any :")
#A,ikinci numarayi ekleme,Renew eski numalari silecek,D ismi tamamen dictionary  den temizleyecek
        if edit == "A":
            num2 = input("Add 2.Number :")
            option=input("Do you want to keep this number , Y/N:")
            if len(num2) != 10 :
                print("Please enter a valid number(10 digits):")
                continue

            elif option=="Y":  #Onemli kisileri her iki listeye yazdiriyoruz.
              guide[name] =[ num, num2]
              secguide[name]=[num,num2]
              print(num2,"Has been added ",name,"succesfully!")
              continue
            elif option=="N":  #Onemsizleri sadece tuple olmayacak listeye yazdiriyoruz.
              guide[name] = [num, num2]
              continue

        elif edit == "D": #Ekli ismi silmek icin
            guide.pop(name)
            secguide.pop(name)
            print(name,"Has been succesfully deleted!")
            continue
    num = input("Add a Number:") #Eger isim onceden ekli degilse buraya direk gelecek

    if len(num) != 10 or name.isalpha() == False: #numara 10 digit,isim ise sadece alfabetik olmasi icin dogrulama
        print("Please enter a valid name(alphabetic char only) or Number(10 digits) :")
        continue

    else :
        a = input("Do you want to keep this number , Y/N :")
        if a == "Y":
            guide.update({name: num})
            secguide.update({name:num})
            esc = input("Press C for continue,else type any button :")
            if esc == "C":
                continue
            else:
                break
        elif a == "N":
            guide.update({name: num})
            esc = input("Press C for continue,else type any button :")
            if esc == "C":
                continue
            else:
                break
secguide = tuple(secguide.items())
print(guide)
print(secguide)