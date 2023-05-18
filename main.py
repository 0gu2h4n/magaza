from magaza import magaza #Mağaza kütüphanesi/dosyası

def main():
    while True:
        magazalar = dict() #Oluşturulan bütün mağazaların tutulacağı sözlük

        print('\nGerekli bilgileri girin... (Çıkış için bilgileri boş bırakın)')
        magazaadi, saticiadi, saticicinsi = input('Mağaza Adı:'), input('Satıcı Adı:'),input('Satıcı Cinsi:')#Bütün mağaza ve satıcı bilgilerini al

        if not (magazaadi or saticiadi or saticicinsi): break #Çıkış yapma durumu

        if magazaadi not in magazalar: magazalar[magazaadi] = magaza(magazaadi, saticiadi, saticicinsi) #Şu anki mağaza mağazalar sözlüğü içerisinde yoksa oluştur
        else: #Mağaza hali hazırda varsa satıcı adını ve cinsini değiştir
            magazalar[magazaadi].SatAdYap(saticiadi)
            magazalar[magazaadi].SatCinYap(saticicinsi)

        while True:
            try: #Kullanıcıdan geçerli bir satış tutarı almayı dene
                tutar = float(input('Satış tutarı: '))
                if tutar < 0: raise(Exception) #Satış 0'dan küçük olamaz
                magazalar[magazaadi].SatisYap(tutar)
                break
            except: print('Geçerli bir değer girin!')
        print('\nKayıt Başarılı!')


if __name__ == "__main__": main()