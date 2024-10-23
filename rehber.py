from db_setup import Kisi, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = engine)
session = Session()

def kisi_ekle(Name,Number,Surname=None,Adress=None):
    yeni_kisi = Kisi(Name=Name, Surname=Surname, Number=Number, Adress=Adress)
    session.add(yeni_kisi)
    session.commit()
    print(f"{yeni_kisi.Name} {yeni_kisi.Surname} kişisi eklendi.")

def kisileri_listele():
    kisiler = session.query(Kisi).all()
    for kisi in kisiler:
        print("+++++++++++++++++")
        print(f"id: {kisi.id}")
        print(f"Adı: {kisi.Name}")
        print(f"Soyadı: {kisi.Surname}")
        print(f"Numara: {kisi.Number}")
        print(f"Adres: {kisi.Adress}")
        
def kisi_goruntule (id): 
    kisi = session.query(Kisi).filter_by(id=id).one_or_none()
    if kisi:
        print(f"Adı: {kisi.Name}")
        print(f"Soyadı: {kisi.Surname}")
        print(f"Numara: {kisi.Number}")
        print(f"Adres: {kisi.Adress}")
    else: 
      print(f"id:{id} ile eşleşen kişi bulunamadı.")

def kisi_sil(id):
   kisi = session.query(Kisi).filter_by(id=id).one_or_none()
   if kisi:
        print(f"{kisi.Name} {kisi.Surname} kişisi silindi.")
        session.delete(kisi)
        session.commit()    
   else:
      print(f"id:{id} ile eşleşen kişi bulunamadı.")

def kisi_duzenle(id):
    kisi = session.query(Kisi).filter_by(id=id).one_or_none()
    if kisi:
        print(f"İsim: {kisi.Name}")
        print(f"Soyad: {kisi.Surname}")
        print(f"Numara: {kisi.Number}")
        print(f"Adres: {kisi.Adress}")
        print("\nYeni bilgileri girin (değiştirmek istemediğiniz alanları boş bırakın):")

        new_Name = input("Yeni isim: ")
        new_Surname = input("Yeni soyad: ")
        new_Number = input("Yeni numara: ")
        new_Adress = input("Yeni adres: ")
        if new_Name:
            kisi.Name = new_Name
        if new_Surname:
            kisi.Surname = new_Surname
        if new_Number:
            kisi.Number = new_Number
        if new_Adress:
            kisi.Adress = new_Adress
        session.commit()
        print(f"{kisi.Name} {kisi.Surname} kişisi düzenlendi.")
    else:
        print(f"id:{id} ile eşleşen kişi bulunamadı.")

def kisi_ara(id):
    kisi = session.query(Kisi).filter_by(id = id).one_or_none()
    if kisi:
        print(f"{kisi.Name} {kisi.Surname} aranıyor...")
    else:
        print(f"id:{id} ile eşleşen kişi bulunamadı.")
        
def menu():
    while True:
        print("***********************")
        print("1. Kişi Ekle")
        print("2. Kişileri Listele")
        print("3. Kişi Düzenle")
        print("4. Kişi Sil")
        print("5. Kişi Ara")
        print("6. Kişi Görüntüle")
        print("***********************")
        secim = int(input("Seçiminizi yapın: "))

        if secim == 1:
            Name = input("İsim: ")
            Surname = input("Soyad: ")
            Number = input("Numara: ")
            Adress = input("Adres: ")
            kisi_ekle(Name, Surname, Number, Adress)
        elif secim == 2:
            kisileri_listele()

        elif secim == 3:
            id = int(input("Düzenlenecek Kişi ID'si: "))
            kisi_duzenle(id)
            
        elif secim == 4:
            id = int(input("Silinecek Kişi ID'si: "))
            kisi_sil(id)
        elif secim == 5:
            id = int(input("Aranacak Kişi ID'si: "))
            kisi_ara(id)
        elif secim == 6:
            id = int(input("Görüntülemek istediğiniz kişinin id'si: "))
            kisi_goruntule (id)
        elif secim == 0:
            print("çıkılıyor...")
            return
        else:
            print("Geçersiz işlem.")

            menu()

menu()



            