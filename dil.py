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
__magaza_en = [
    "\nSeller not found!",
    "store",
    "seller sales (Date > Amount):\n",
    "Store Total Sales:",
    "Seller Total Sales:"
]
__main_en = [
    "Enter the required information... (Leave blank for exit)",
    "Store Name:",
    "Seller Name:",
    "Seller Type:",
    "Sales amount:",
    "Enter a valid value!",
    "\nRegistration Successful!",
    "\nEnter the store name you want to get the information of (Leave blank for exit):",
    "Store not found!",
    "Enter the seller name you want to get the sales of (Leave blank for all store):",
    "\nSeller total sales amount:"
]

def main():
    if dil == "tr":
        return __main_tr
    
def magaza():
    if dil == "tr":
        return __magaza_tr