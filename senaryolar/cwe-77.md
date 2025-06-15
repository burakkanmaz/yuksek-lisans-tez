# CWE-77 - Command Injection
<a href="https://cwe.mitre.org/data/definitions/77.html" target="_blank">🔗 CWE-77 - Command Injection</a>

## ✏️ Senaryo 1
Bir sistem yönetim arayüzünde kullanıcılar, sunucuda çalışan işlemleri sonlandırmak için işlem adını giriyor. Bu ad, sistemde arka planda çalıştırılan bir komutun parametresi olarak kullanılıyor. Kullanıcı girişine dair belirli bir karakter kontrolü yapılmıyor. İşlem sonucu kullanıcıya metin olarak geri döndürülüyor.

## ✏️ Senaryo 2
Bir sistem sağlık kontrol panelinde kullanıcılar, belirli bir log dosyasının içeriğini görüntülemek üzere dosya adını girebiliyor. Girilen dosya adı, arka planda çalışan bir komut dizisine doğrudan ekleniyor. Sistem, sadece dosyanın var olup olmadığını kontrol ediyor. Sonuçlar kullanıcı arayüzüne yansıtılıyor.

## ✏️ Senaryo 3
Bir FTP arayüzünde kullanıcılar, sistemde belirli bir dizini sıkıştırarak indirme işlemi başlatabiliyor. Dizinin adı metin kutusuna yazılarak sunucuya iletiliyor. Sistem, bu girdiyi bir sıkıştırma komutunun argümanı olarak kullanıyor. Dosya daha sonra indirme bağlantısıyla sunuluyor.

## ✏️ Senaryo 4
Bir yedekleme uygulamasında, kullanıcıdan alınan dosya adı bir script çalıştırılarak arşivleniyor. Dosya adı, çalıştırılacak komutun içinde doğrudan yer alıyor. Sistem dosya adının yapısına dair herhangi bir filtreleme uygulamıyor. Yedekleme tamamlandıktan sonra kullanıcıya bildirim gönderiliyor.

## ✏️ Senaryo 5
Bir güvenlik kontrol sisteminde kullanıcılar, bir IP adresi girerek ağa ping atabiliyor. IP adresi doğrudan bir sistem komutunun içine eklenerek ping işlemi başlatılıyor. Adresin biçimine dair yüzeysel bir kontrol dışında denetim yapılmıyor. Sonuçlar metin biçiminde kullanıcıya aktarılıyor.

## ✏️ Senaryo 6
Bir terminal tabanlı kullanıcı arayüzünde, kullanıcılar sistemde çalıştırmak istedikleri program adını yazabiliyor. Yazılan ifade, sunucuda çalıştırılacak komutun parçası olarak kullanılıyor. Sistem bu girişe dair herhangi bir kontrol gerçekleştirmiyor. Program çıktısı doğrudan gösteriliyor.

## ✏️ Senaryo 7
Bir uzaktan kontrol yazılımında kullanıcılar, belirli bir klasördeki dosyaları silmek için dizin adı giriyor. Girilen dizin, komut satırı komutuna dahil ediliyor. Sistem bu dizinin geçerli olup olmadığını kontrol etse de içerik denetimi yapılmıyor. Komut başarılıysa kullanıcı bilgilendiriliyor.

## ✏️ Senaryo 8
Bir sunucu bakım aracı, kullanıcıların logları dışa aktarmasına izin veriyor. Kullanıcı, log tipi ve hedef dosya adını giriyor. Bu bilgiler birleştirilerek komut satırına aktarılıyor. Oluşturulan dosya daha sonra kullanıcıya sunuluyor.

## ✏️ Senaryo 9
Bir dosya dönüştürme sisteminde kullanıcılar kaynak dosya adını girerek işlem başlatabiliyor. Dosya adı bir dış yazılıma argüman olarak iletiliyor. Sistemde dosya adının içeriğine dair filtreleme yapılmıyor. İşlem tamamlandıktan sonra kullanıcı çıktıyı alabiliyor.

## ✏️ Senaryo 10
Bir sistemde, kullanıcılar belirli bir kullanıcıyı devre dışı bırakmak için kullanıcı adını form üzerinden giriyor. Bu ad, sunucuda çalıştırılan bir yönetim komutunun argümanı olarak geçiyor. Kullanıcı adında yalnızca uzunluk sınırı uygulanıyor. Sonuç, arayüzde işlem durumu olarak görünüyor.

