# dogru isim ve telefon numaralarini alip ekrana ayzdiran dictionary
dic = { }#bos bir dictionary ve liste olusturdum.
liste=[]

while True :
    
    while True: # while True dongusu ile isimler alip eger isimler sadece hadrflerden olusuyorsa kabul eden aksi halde yeni isim isteyen dongu
        name = input( "Enter name of friend :-")
        if (name.isalpha())==False: #burda sadece harflerden olusup olusmadigini kontrol ettim
            print("Please enter the correct name of friend")
        else:
            break
    while True: #burda yine bir dongu ile uygun telefon numaralarini istedim.
        phone =( input("Enter phone number of friend :-" ))
        if len(phone)!=10: # burda istenen numaranin 10 haneden olusup olusmadigini kontrol ettim
            print("Please enter the correct phone number")
        else:
            break
    a=input("Is this person important for you: Y/N") #kisinin onmeli olup olmadigini sordum
    if a=="Y": # eger onemli ise bunu bos listenin icine numara ve isim ile eklemesini istedim.
        liste.append([name,phone])
    
    tup=tuple(liste) # bu isimleri ise tuple icinde guvenli bolge olusturdum. boylece silinmeyecek ve degismeyecek

    dic [name] = phone #burda dictionary i olusturdum.
    choise = input("Enter Q to quit otherwise N :-") #burda tekrar isim eklemek istemedigini sordum. Add bolumu
    if choise == "Q" or choise == "q" : # hayir ise donguden cikacak
        break
print(dic)# ekrana dictionary i yazdirdim
print(tup)#ekrana tuple i yazdirdim

name=input("Please enter the name of friend you want to delete : ")# delete menusu istedigi ismi silecek.
del dic[name]
print(dic)

name=input("Please enter the name of friend you want to edit or change number: ") #edit or change bolumu
phone=int(input("Enter the phone number of friend: "))
del dic[name]
dic[name]=phone
print(dic)