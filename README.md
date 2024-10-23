# Telefon Rehberi Uygulaması

Bu proje, Python ve SQLAlchemy kullanarak basit bir telefon rehberi uygulaması geliştirmektedir. Veritabanı olarak MSSQL kullanılmaktadır ve bu uygulama, rehbere kişi ekleme, silme, düzenleme, görüntüleme ve kişi arama işlemlerini gerçekleştirebilir.

## İçindekiler
- [Dosyaların Listesi](#dosyaların-listesi)
- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Veritabanı Şeması](#veritabanı-şeması)
- [Bağımlılıklar](#bağımlılıklar)
- [Yapılandırma](#yapılandırma)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## Dosyaların Listesi
1. db_setup.py --> Projenin veritabanı yapılandırma ve bağlantı ayarlarını yapan bir dosyadır. Bu dosyanın amacı, MSSQL veritabanı ile bağlantı kurarak tablo yapısını oluşturmak ve gerekli veritabanı işlemlerini başlatmaktır.
2. rehber.py --> Bir telefon rehberi uygulamasını yönetmek için kullanılan işlevleri içeren bir dosyadır. Bu dosya, kullanıcıların veritabanına yeni kişiler eklemesine, kişileri listelemesine, kişileri düzenlemesine, silmesine ve aramasına olanak tanır.

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
## Kullanım
Uygulamayı çalıştırdıktan sonra, bir menü ile karşılaşacaksınız. Bu menü aracılığıyla rehberinizi yönetebilirsiniz:
0. Çıkış
1. Kişi Ekle
2. Kişileri Listele
3. Kişi Düzenle
4. Kişi Sil
5. Kişi Ara
6. Kişi Görüntüle

 ### örnek
Yeni bir kişi eklemek için:
- Menüden 1 numaralı seçeneği seçin.
- Kişinin bilgilerini (İsim, Soyisim, Telefon Numarası, Adres) girin.
- Uygulama, kişiyi eklediğinizi doğrular.
 



























    
