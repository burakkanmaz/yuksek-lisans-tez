# CWE-306 - Missing Authentication for Critical Function
<a href="https://cwe.mitre.org/data/definitions/306.html" target="_blank">🔗 CWE-306 - Missing Authentication for Critical Function</a>

## ✏️ Senaryo 1
Bir web uygulamasında yönetici paneli üzerinden sistem ayarları değiştirilebiliyor. Panel bağlantısı üzerinden ayar sayfalarına erişilebiliyor. URL bilgisi ile bu panele ulaşılabiliyor. Ayar değişiklikleri doğrudan uygulanıyor.

## ✏️ Senaryo 2
Bir bulut depolama hizmetinde kullanıcılar dosya silme işlemi gerçekleştirebiliyor. Silme komutları sistem tarafından işleniyor. Silme isteği gönderildiğinde dosya kaldırılıyor. İşlem API çağrısı ile yapılıyor.

## ✏️ Senaryo 3
Bir IoT cihaz yönetim panelinde cihazları yeniden başlatma işlemleri yapılabiliyor. Panel arayüzü üzerinden bu komutlar çalıştırılıyor. Yeniden başlatma ve sıfırlama gibi işlemler destekleniyor. Komutlar doğrudan cihazlara gönderiliyor.

## ✏️ Senaryo 4
Bir blog platformunda gönderileri yayından kaldırmak için URL çağrısı yapılıyor. Bu çağrı ile gönderiler kaldırılabiliyor. İşlem URL tabanlı API ile gerçekleşiyor. Gönderiler sistem üzerinden kaldırılıyor.

## ✏️ Senaryo 5
Bir dosya paylaşım uygulamasında kullanıcılar dosya bağlantılarını yönetebiliyor. Bağlantıları devre dışı bırakma çağrıları yapılabiliyor. Link yönetimi API servisi üzerinden gerçekleşiyor. Bağlantı durumu bu çağrılarla değiştiriliyor.

## ✏️ Senaryo 6
Bir mobil bankacılık uygulamasında hesap telefon numarası güncellenebiliyor. Numara değiştirme işlemi servis çağrısı ile yapılıyor. Güncelleme talepleri sistem tarafından işleniyor. Telefon numarası değişiklikleri kayıt altına alınıyor.

## ✏️ Senaryo 7
Bir öğrenci bilgi sisteminde not giriş ekranına bağlantı ile erişilebiliyor. Bağlantı üzerinden not değiştirme sayfası açılıyor. Notlar bu ekran üzerinden güncellenebiliyor. Değişiklikler sistem kayıtlarına yansıyor.

## ✏️ Senaryo 8
Bir cihaz yönetim sisteminde uzaktan firmware güncellemesi yapılabiliyor. Güncelleme servisi üzerinden firmware yükleniyor. Sistem bu güncellemeleri cihazlara uygulayabiliyor. İşlem uzak yönetim arayüzünden yapılıyor.

## ✏️ Senaryo 9
Bir raporlama uygulamasında sistem raporları indirilebiliyor. Özel bağlantı üzerinden rapor dosyalarına erişilebiliyor. Bu raporlar sistem genelindeki verileri içeriyor. İndirme işlemi bağlantı tabanlı çalışıyor.

## ✏️ Senaryo 10
Bir müşteri destek uygulamasında müşteri hesapları yönetilebiliyor. Hesap silme endpoint'i üzerinden işlem yapılabiliyor. İstek doğru formatta gönderildiğinde hesap kaldırılıyor. Silme işlemi API ile gerçekleştiriliyor.

