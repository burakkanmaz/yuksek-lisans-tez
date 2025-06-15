# CWE-78 - OS Command Injection
<a href="https://cwe.mitre.org/data/definitions/78.html" target="_blank">🔗 CWE-78 - OS Command Injection</a>

## ✏️ Senaryo 1
Bir sistem yönetim panelinde kullanıcılar, sunucudaki belirli klasörlerin içeriklerini listeleyebiliyor. Gerekli klasör yolu bir metin kutusundan giriliyor ve sistem bu yola göre işlem yapıyor. Listeleme sonucu kullanıcıya görsel olarak sunuluyor. Kullanıcılar kendi sunucularını tanımlayabildiği için klasör yolu esnek bırakılmış.

## ✏️ Senaryo 2
Bir yedekleme aracı, kullanıcıdan alınan klasör yoluna göre sistemde belirli bir bölgeyi arşivliyor. Arşivleme işlemi komut satırı üzerinden çalıştırılan bir işlemle tetikleniyor. Kullanıcı arayüzünden yalnızca hedef klasörü girerek bu işlemi başlatabiliyor. Yedekleme işlemi arka planda zip dosyası oluşturularak tamamlanıyor.

## ✏️ Senaryo 3
Bir medya yönetim sisteminde kullanıcılar, yükledikleri videoları işleyip formatlarını dönüştürebiliyor. Format dönüşümü, dış bir komutla başlatılıyor ve kaynak dosya adı kullanıcıdan alınıyor. Dönüştürme işlemi tamamlandığında yeni dosya kullanıcıya gösteriliyor. Bu işlem arayüzde sade bir giriş alanı ile tetikleniyor.

## ✏️ Senaryo 4
Bir IoT kontrol panelinde, bağlı cihazların log dosyalarını kullanıcılar indirebiliyor. Hangi log dosyasının indirileceği kullanıcıdan alınıyor ve sistem bu dosyayı sıkıştırarak hazır hale getiriyor. İndirme işlemi, arka planda belirli sistem komutlarıyla başlatılıyor. Dosya daha sonra kullanıcıya sunuluyor.

## ✏️ Senaryo 5
Bir e-posta sunucusu yönetim uygulamasında kullanıcılar, belirli kullanıcıların posta kutularını boşaltabiliyor. Hangi posta kutusunun temizleneceği form alanından giriliyor. Bu alan, sistemde komutla eşleştirilerek arka planda işlem başlatıyor. İşlem tamamlandığında kullanıcıya sonuç bildiriliyor.

## ✏️ Senaryo 6
Bir dosya arama aracı, kullanıcının belirttiği dizin içerisinde anahtar kelimeyle eşleşen dosyaları arıyor. Arama işlemi, sistem komutları kullanılarak çalıştırılıyor. Dizin ve arama terimi kullanıcıdan alınıyor. Sonuçlar liste halinde kullanıcıya sunuluyor.

## ✏️ Senaryo 7
Bir sistem araçları panelinde kullanıcılar, ağ arabirimleri ile ilgili işlemleri başlatabiliyor. Kullanıcı, çalıştırılacak komutu ya da komutun parametresini arayüzde seçerek işlemi tetikliyor. Sistem bu girdiyi bir kabuk komutu ile birleştirerek çalıştırıyor. Sonuçlar arayüzde gösteriliyor.

## ✏️ Senaryo 8
Bir yazılım güncelleme sisteminde kullanıcılar, belirli bir klasördeki scriptleri çalıştırarak uygulamayı güncelleyebiliyor. Çalıştırılacak script dosyasının adı kullanıcı tarafından belirtiliyor. Sistem bu dosyayı tanıyıp çalıştırmak üzere komut oluşturuyor. Güncelleme sonrası çıktı kullanıcıya gösteriliyor.

## ✏️ Senaryo 9
Bir sistem teşhis aracı, kullanıcının girdiği hostname bilgisine göre sunuculara ping atabiliyor. Hostname metin kutusuna girildikten sonra ping komutu çalıştırılıyor. Sonuçlar kullanıcıya süre bilgisiyle birlikte gösteriliyor. Ping işlemi farklı parametrelerle tekrar edilebiliyor.

## ✏️ Senaryo 10
Bir görüntü işleme uygulaması, kullanıcıdan aldığı dosya adı ve parametreye göre sistemde dönüşüm komutu başlatıyor. Kullanıcı arayüzünden format ve hedef adı giriliyor. Bu bilgilerle arka planda bir işlem çalıştırılıyor. Dönüştürülmüş dosya daha sonra indirilebilir olarak sunuluyor.

