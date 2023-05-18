from datetime import datetime as dt #Satış işlemlerini tutarken satışın yapıldı tarihi de tutmak için
import dil

class magaza():

    #Sınıf objelerini belirle
    def __init__(self, mag_ad, sat_ad, sat_cin) -> None: self.__mag_ad, self.__sat_ad, self.__sat_cin, self.__satis = mag_ad, sat_ad, sat_cin, dict()
    
    #Mağaza adını değiştir
    def MagAdYap(self, mag_ad) -> None: self.__mag_ad = mag_ad
    
    #Mağaza adını getir
    def MagAdAl(self) -> str: return self.__mag_ad
    
    #Satıcı adını değiştir
    def SatAdYap(self, sat_ad) -> None: self.__sat_ad = sat_ad
    
    #Satıcı adını getir
    def SatAdAl(self) -> str: return self.__sat_ad
    
    #Satıcı cinsini değiştir
    def SatCinYap(self, sat_cin) -> None: self.__sat_cin = sat_cin
    
    #Satıcı cinsini getir
    def SatCinAl(self) -> str: return self.__sat_cin
    
    #Satıs tutarını satış tarihi ile birlikte __satis sözlüğünde satıcı adının altında liste olarak tut
    def SatisYap(self, satis) -> None: 
        if self.__sat_ad not in self.__satis: self.__satis[self.__sat_ad] = list()
        self.__satis[self.__sat_ad].append(
            {f'{dt.now().year}-{dt.now().month}-{dt.now().day}-{dt.now().hour}-{dt.now().minute}-{dt.now().second}' : satis})

    #Satıcı adına göre satıcının bütün satışlarını ve toplam satışını yazdır, satıcı yoksa bulunamadı yazdır
    def SatisAl(self, satici) -> None:
        if satici not in self.__satis:
            print(dil.magaza()[0])
            return -1.0
        toplam = 0.0
        print(f'{self.__mag_ad} {dil.magaza()[1]} {satici} {dil.magaza()[2]}')
        for satis in self.__satis[satici]: 
            tarih,ucret = list(satis.items())[0]
            print(f'{tarih} > {ucret}')
            toplam += ucret
        return toplam
        
    #Mağazanın toplam satış tutarını ve her satıcının teker teker toplam satışlarını bir string'e dönüştür ve geriye döndür
    def __str__(self) -> str: return (f'{dil.magaza()[3]} {sum([list(satis.values())[0] for satici in self.__satis.values() for satis in satici])}\n' +
                                       '\n'.join([f'{k} {dil.magaza()[4]} {v}' for k, v in {saticiad: sum([list(satis.values())[0] for satis in satici]) for saticiad, satici in self.__satis.items()}.items()]))
