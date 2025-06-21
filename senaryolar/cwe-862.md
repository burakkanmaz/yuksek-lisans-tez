# CWE-862 - Missing Authorization
<a href="https://cwe.mitre.org/data/definitions/862.html" target="_blank">🔗 CWE-862 - Missing Authorization</a>

## ✏️ Senaryo 1
Bir içerik yönetim sisteminde kullanıcılar farklı rollerle oturum açıyor. Editörler yazı düzenleyip silme işlemlerini gerçekleştirebiliyor. Arayüzde her kullanıcı için silme butonu görüntüleniyor. Kullanıcılar bu butona tıklayarak işlem yapabiliyor.

## ✏️ Senaryo 2
Bir dosya paylaşım platformunda kullanıcılar dosya yönetimi yapabiliyor. İşlem ekranında dosya ID'si girilerek çeşitli operasyonlar gerçekleştirilebiliyor. Platform üzerindeki tüm kullanıcılar bu ekrana erişebiliyor. Dosya ID değerleri URL üzerinden değiştirilebiliyor.

## ✏️ Senaryo 3
Bir kurumsal iletişim uygulamasında mesaj okuma işlemleri yapılıyor. Kullanıcılar mesaj ID'si ile içerik talep edebiliyor. Sistem bu taleplere yanıt vererek mesaj içeriğini döndürüyor. Mesaj detay sayfasına doğrudan erişim mümkün.

## ✏️ Senaryo 4
Bir okul yönetim sisteminde öğrenci bilgi sayfaları bulunuyor. Öğrenci numarası ile detay sayfası açılabiliyor. Bu sayfalara hem arama hem de doğrudan URL ile ulaşılabiliyor. Öğrenci bilgileri sayfa üzerinde görüntüleniyor.

## ✏️ Senaryo 5
Bir sağlık uygulamasında tahlil sonuçları görüntüleniyor. Mobil ve web sürümlerinde test ID'si ile sonuç sorgulaması yapılabiliyor. Test sonuçları ID bilgisiyle getiriliyor. Her iki platform da bu sorguları destekliyor.

## ✏️ Senaryo 6
Bir etkinlik yönetim sisteminde etkinlik güncelleme formları bulunuyor. Katılımcılar bu formlara erişip değişiklik yapabiliyor. Form verisi sunucuya gönderildiğinde etkinlik bilgileri güncelleniyor. Değişiklikler anında sisteme yansıyor.

## ✏️ Senaryo 7
Bir teknik destek sisteminde kayıt görüntüleme sayfaları var. Destek kaydı ID numarası ile detay sayfalarına erişilebiliyor. Bu sayfalar sistem genelinde kullanılabiliyor. Kayıt detayları sayfa üzerinde gösteriliyor.

## ✏️ Senaryo 8
Bir rezervasyon platformunda rezervasyon yönetimi API'si bulunuyor. Rezervasyon silme işlemi ID gönderilerek gerçekleştiriliyor. API bu silme taleplerini işleyerek rezervasyonu kaldırıyor. İşlem sonucu API yanıtı olarak döndürülüyor.

## ✏️ Senaryo 9
Bir anket uygulamasında anket düzenleme sayfaları bulunuyor. Anket ID'si ile düzenleme sayfasına erişim sağlanıyor. Düzenleme işlemleri bu sayfalar üzerinden yapılabiliyor. Değişiklikler kaydedildiğinde anket güncelleniyor.

## ✏️ Senaryo 10
Bir belge yönetim sisteminde belge onay formları sunuluyor. Belge ID'si ile onay formu gönderilebiliyor. Form gönderildiğinde belge durumu değiştiriliyor. Onay işlemi tamamlandığında sistem güncelleniyor.

