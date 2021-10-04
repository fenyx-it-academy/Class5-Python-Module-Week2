def menu():
    print('''
    telefon defterine hos geldiniz!
    *     print icin \033[32;1m 0 \033[0m girin
    *       add icin \033[32;1m 1 \033[0m girin
    *      edit icin \033[32;1m 2 \033[0m girin
    *     delet icin \033[32;1m 3 \033[0m girin
    *      exit icin \033[32;1m 4 \033[0m girin
    ''')

contact = {}
contact_vip = {}
options = 0
while (options != '4' ) :
    menu()
    #secim dongusu,1~4  girmesi saglanir
    while True:
        options = input('menu secin:')
        if options.isdigit() and 0 <= int(options) <= 4: break
        else:
            print('yanlis girdiniz \n''0 = print','1 = add','2 = edit','3 = delet','4 = quit',sep=",")
            continue
    # menu 1 girilirse isim ve numara istenir, ve bunlar sartlara uygunsa Contact(dict) kayitlenir
    if options == '1':
        #girilen isimin sadece harflardan ulasmasi saglayan dongu
        while True:
            isim = input('adi girin : ')
            if isim.isalpha():
                break
            else:
                print('isim sadece harflardan ulusmali !')
                continue
        #girilen numaranin sayilardan ulasmasi ve 10 hane olmasi saglayan dongu
        while True:
            numara = input('numarayi girin : ')
            if (numara.isdigit() and len(numara)) == 10:
                contact[isim] = numara
                important = input('bu onemli biri mi?evet =e,hayir =h : ')
                if important == 'e':
                    contact_vip[isim] = numara
                else:
                    break
                # print('{key}={value}'.format(key=isim, value=numara))
                # print(contact)
                break
            else:
                print('numaralar sadece sayilardan ulusmali 10 hane olmali ! ')
                continue
    #menu secimi 2 ise
    elif options == '2':
        #mevcut numarayi edit etmek,once girilen isimi Contact Dict ten ariyor
        while True:
            arama = input('degistireceginiz isimi girin : ')
            if arama.isalpha():
                if arama not in contact:
                    print('bulunmadi,tekrar deneyin !')
                    continue
                else:
                    print('{key}={value}'.format(key=arama, value=contact[arama]))
                    #mevcutsa yeni numara girmesi istenir ve eski numaranin yerine koyar
                    while True:
                        yeni_numara = input('yeni numarayi girin : ')
                        if (yeni_numara .isdigit() and len(yeni_numara )) == 10:
                            contact[arama] = yeni_numara
                            # print('{key}={value}'.format(key=arama, value=yeni_numara))
                            # print(contact)
                            break

                        else:
                            print('numaralar sadece sayilardan ulusmali ve 10 hane olmali !')
                            continue
                break
            else:
                print('isim sadece harflardan ulusmali\naradiginiz isim bulunmadi')
    #menu secim 3 ise
    elif options == '3':
        #once aranip,buluktan sonra silme karari sorulur
        while True:
            sil_isim =input('silmek istediginiz isimi girin : ')
            if sil_isim.isalpha():
                if sil_isim not in contact:
                    print('bu kisi bulunmadi !')
                    continue
                else:
                    print('{key}={value}'.format(key=sil_isim, value=contact[sil_isim]))
                    #silme karari alinip,silinir yada menuye doner
                    while True:
                        print('input d = delet or b =back to menu ')
                        silmekarari = input('d / b?:')
                        if (silmekarari == 'd'):
                            del contact[sil_isim]
                            # print(contact)
                            break
                        elif silmekarari == 'b':
                            break
                        else:
                            continue

                break
            else:
                print('isim sadece harflardan ulusmali !')
    #menu secimi 4 ise dongu bitip sistemden cikar
    elif (options == '4'):
        break
    #defteri yazdirmak icin
    elif (options == '0'):
        print('important list : ',contact_vip)
        print('tum list : ',contact)
        continue