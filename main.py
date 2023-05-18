from magaza import magaza #Mağaza kütüphanesi/dosyası
import dil

def main():
    while True:
        magazalar = dict() #Oluşturulan bütün mağazaların tutulacağı sözlük

        print(dil.main()[0])
        magazaadi, saticiadi, saticicinsi = input(dil.main()[1]), input(dil.main()[2]),input(dil.main()[3])#Bütün mağaza ve satıcı bilgilerini al

        if not (magazaadi or saticiadi or saticicinsi): break #Çıkış yapma durumu

        if magazaadi not in magazalar: magazalar[magazaadi] = magaza(magazaadi, saticiadi, saticicinsi) #Şu anki mağaza mağazalar sözlüğü içerisinde yoksa oluştur
        else: #Mağaza hali hazırda varsa satıcı adını ve cinsini değiştir
            magazalar[magazaadi].SatAdYap(saticiadi)
            magazalar[magazaadi].SatCinYap(saticicinsi)

        while True:
            try: #Kullanıcıdan geçerli bir satış tutarı almayı dene
                tutar = float(input(dil.main()[4]))
                if tutar < 0: raise(Exception) #Satış 0'dan küçük olamaz
                magazalar[magazaadi].SatisYap(tutar)
                break
            except: print(dil.main()[5])
        print(dil.main()[6])

    while True:
        #Arama için mağaza adını al
        mgz = input(dil.main()[7])
        #Çıkış
        if not mgz: break
        #Bu adla kayıtlı bir mağaza var mı?
        if mgz not in magazalar:
            print(dil.main()[8])
            continue
        #Bir satıcının satışları için satıcı adı al ya da bütün mağaza için
        stc = input(dil.main()[9])
        #Bütün mağaza için
        if not stc: print(f'\n{magazalar[mgz]}')
        #Satıcı için
        else: 
            sts = magazalar[mgz].SatisAl(stc)
            if sts != -1.0: print(f'{dil.main()[10]} {sts}') 



if __name__ == "__main__": main()