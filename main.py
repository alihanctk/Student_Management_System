print('--- ÖĞRENCİ YÖNETİM SİSTEMİ ---')

ogrenciler = []
next_id = 1

def ogrenci_ekle():
    global next_id
    ad = input("Öğrenci Adı: ")
    notu = input("Öğrenci Notu: ")
    ogrenciler.append({
        "id": next_id,
        "ad": ad,
        "not": notu
    })
    print("Öğrenci başarıyla eklendi.")
    return next_id + 1

def ogrenci_sil():
    silinecek_id = int(input("Silinecek öğrencinin ID'sini girin: "))
    for ogrenci in ogrenciler:
        if ogrenci["id"] == silinecek_id:
            ogrenciler.remove(ogrenci)
            print("Öğrenci silindi.")
            return
    print("Öğrenci bulunamadı.")

def ogrencileri_listele():
    if not ogrenciler:
        print("Kayıtlı öğrenci yok.")
    else:
        print("\nÖğrenciler:")
        for ogrenci in ogrenciler:
            print(f"No: {ogrenci['id']}, Adı: {ogrenci['ad']}, Notu: {ogrenci['not']}")

while True:
    print("\n1. Öğrenci Ekle")
    print("2. Öğrenci Sil")
    print("3. Öğrencileri Listele")
    print("4. Çıkış")

    secim = input("\nBir işlem seçin: ")

    match secim:
        case "1":
            next_id = ogrenci_ekle()
        case "2":
            ogrenci_sil()
        case "3":
            ogrencileri_listele()
        case "4":
            print("Çıkış yapılıyor...")
            break
        case _:
            print("Geçersiz seçim! Lütfen 1-4 arasında bir değer girin!")
