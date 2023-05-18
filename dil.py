dil = "tr"

__magaza_tr = [
    "\nSatıcı Bulunamadı!",
    "mağazası",
    "satıcısı satışları (Tarih > Tutar):\n",
    "Mağaza Toplam Satış:",
    "Satıcısı Toplam Satış:"
]
__main_tr = [
    "Gerekli bilgileri girin... (Çıkış için bilgileri boş bırakın)",
    "Mağaza Adı:",
    "Satıcı Adı:",
    "Satıcı Cinsi:",
    "Satış tutarı:",
    "Geçerli bir değer girin!",
    "\nKayıt Başarılı!",
    "\nBilgilerini getirmek istediğiniz mağaza adını girin (Çıkış için boş bırakın):",
    "Mağaza Bulunamadı!",
    "Satışlarını getirmek istediğiniz satıcı adını girin (Bütün mağaza için boş bırakın):",
    "\nSatıcı toplam satış tutarı:"
]

def main():
    if dil == "tr":
        return __main_tr
    
def magaza():
    if dil == "tr":
        return __magaza_tr