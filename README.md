# Telefon Rehberi Uygulaması

Bu proje, Python ve SQLAlchemy kullanarak basit bir telefon rehberi uygulaması geliştirmektedir. Veritabanı olarak MSSQL kullanılmaktadır ve bu uygulama, rehbere kişi ekleme, silme, düzenleme, görüntüleme ve kişi arama işlemlerini gerçekleştirebilir.

## İçindekiler
- [Dosya Organizasyonu](#dosya-organizasyonu)
- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Veritabanı Şeması](#veritabanı-şeması)
- [Kullanım](#kullanım)


## Dosya Organizasyonu

Proje dosyalarının organizasyonu ve aralarındaki ilişkiler aşağıdaki gibidir:
 ``` bash
📁 Proje Klasörü
│
├── README.md              # Proje hakkında genel bilgiler, kullanım ve kurulum talimatları
│
├── db_setup.py            # Veritabanı kurulumunu ve tablo yapılandırmasını yapan Python scripti
│      │
│      └── Veritabanı bağlantısı kurulur ve 'rehber' tablosu oluşturulur.
│
├── rehber.py              # Telefon rehberi işlevlerini yöneten ana Python scripti
       └── db_setup.py içindeki Kisi sınıfını kullanarak CRUD işlemlerini gerçekleştirir.
 ```


## Özellikler

- **Yeni kişi ekle**: İsim, soyisim, telefon numarası ve adres gibi bilgileri ekleyin.
- **Kişileri listele**: Tüm kayıtlı kişilerin bilgilerini listeleyin.
- **Kişiyi ID ile arama**: Belirli bir ID'ye sahip kişiyi arayın.
- **Kişiyi düzenle**: Mevcut bir kişinin bilgilerini güncelleyin.
- **Kişiyi sil**: Rehberden bir kişiyi silin.
- **Kişiyi görütüntüle**: Belirli bir ID'ye sahip kişiyi görüntüleyin.


### Gereksinimler
- Bilgisayarınızda Python 3.x yüklü olmalıdır.
- Microsoft SQL Server ve ODBC sürücüsü (ODBC Driver 17 for SQL Server).
- Python için `SQLAlchemy` ve `pyodbc` paketleri.

## Kurulum

1. Gerekli kütüphaneyi yükleyin:
   ```bash
   pip install sqlalchemy pyodbc
2. db_setup.py dosyasındaki SQL Server bağlantı bilgilerini düzenleyin:
   ```bash
   server_name = "SUNUCU_ADINIZ"
   database_name = "master"
3. Veritabanı tablolarını oluşturmak için db_setup.py kodunu çalıştırın:
   ```bash
   python db_setup.py
4. Uygulamayı başlatın:
    ```bash
   python rehber.py

## Veritabanı Şeması
- Kişi bilgilerinin saklandığı "rehber" tablosu:
- ![image](https://github.com/user-attachments/assets/bd8ae248-c192-42ee-a9e2-00bd0b57dd69)
- Bu tablo eğer mevcut değilse, uygulama çalıştığında otomatik olarak oluşturulur.

## Kullanım
Uygulamayı çalıştırdıktan sonra, bir menü ile karşılaşacaksınız. Bu menü aracılığıyla rehberinizi yönetebilirsiniz:
```bash
0. Çıkış 
1. Kişi Ekle
2. Kişileri Listele
3. Kişi Düzenle
4. Kişi Sil
5. Kişi Ara
6. Kişi Görüntüle
```
 ### örnek
Yeni bir kişi eklemek için:
- Menüden 1 numaralı seçeneği seçin.
- Kişinin bilgilerini (İsim, Soyisim, Telefon Numarası, Adres) girin.
- Uygulama, kişiyi eklediğinizi doğrular.
 



























    
