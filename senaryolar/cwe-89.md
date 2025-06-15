# CWE-89 - SQL Injection
<a href="https://cwe.mitre.org/data/definitions/89.html" target="_blank">🔗 CWE-89 - SQL Injection</a>

## ✏️ Senaryo 1
Bir kullanıcı yönetim panelinde, yöneticiler belirli bir kullanıcıya ait bilgileri arayabiliyor. Arama kutusuna girilen kullanıcı adı, veritabanında sorgulanarak eşleşen kayıtlar gösteriliyor. Arama işlemi her karakter değişiminde güncelleniyor. Sonuçlar bir tablo halinde listeleniyor.

## ✏️ Senaryo 2
Bir e-ticaret platformunda kullanıcılar sipariş numaralarını girerek kargo durumlarını sorgulayabiliyor. Sipariş numarası, giriş kutusuna yazıldıktan sonra arka planda veritabanı üzerinden arama yapılmakta. Sonuçlar, kullanıcının geçmiş siparişleriyle birlikte gösteriliyor. Kullanıcı sadece sipariş numarasını girerek bilgiye ulaşabiliyor.

## ✏️ Senaryo 3
Bir üniversite portalında öğrenciler, öğrenci numaralarını girerek notlarını görebiliyor. Notlar, öğrenciye özel olarak filtrelenip veritabanından çekiliyor. Öğrenci numarası giriş alanı serbest metin kutusu olarak sunulmuş. Notlar tablo halinde sayfada görüntüleniyor.

## ✏️ Senaryo 4
Bir destek sistemi uygulamasında, kullanıcılar açtıkları destek taleplerini takip edebiliyor. Destek talep numarasını girerek geçmiş kayıtlarına ulaşmaları sağlanıyor. Bu bilgiye göre sistem, veritabanından ilgili kayıtları çekip kullanıcıya sunuyor. Detaylar sayfada genişletilebilir yapıda gösteriliyor.

## ✏️ Senaryo 5
Bir kütüphane uygulamasında kullanıcılar kitap adıyla arama yapabiliyor. Kullanıcı, arama çubuğuna kitap ismini yazarak sonuçları listeleyebiliyor. Sistem, girilen değeri doğrudan kullanarak kitap başlığına göre veri filtreliyor. Sonuçlar kart yapısında sunuluyor.

## ✏️ Senaryo 6
Bir restoran rezervasyon sisteminde yöneticiler, müşteri e-posta adresine göre rezervasyonları listeleyebiliyor. Yönetici panelinde yer alan filtreleme bölümünde e-posta adresi girilerek sorgu yapılabiliyor. Bu alan herhangi bir format kısıtlaması olmadan çalışıyor. Sonuçlar zaman sıralı şekilde gösteriliyor.

## ✏️ Senaryo 7
Bir otel yönetim sisteminde personel, müşteri soyadına göre kayıt araması yapabiliyor. Soyad bilgisi giriş alanı aracılığıyla alınıp sorgu oluşturuluyor. Veritabanından eşleşen müşteri kayıtları tablo halinde listeleniyor. Her kayıt satırı, müşteri detayına yönlendirme içeriyor.

## ✏️ Senaryo 8
Bir etkinlik kayıt sisteminde kullanıcılar, bilet numarasını girerek rezervasyon bilgilerine ulaşabiliyor. Bu numara genellikle QR koddan okunarak form alanına aktarılıyor. Sistem bu numaraya göre arka planda veritabanından ilgili bilgileri çekiyor. Sayfada kullanıcıya özel detaylar gösteriliyor.

## ✏️ Senaryo 9
Bir video paylaşım platformunda, yöneticiler içerik ID'sine göre videoları yönetim panelinde arayabiliyor. ID değeri giriş kutusuna yazılıyor ve eşleşen içerik listeleniyor. Arama işlemi basit bir form üzerinden gerçekleşiyor. Liste, video başlığı ve yükleyen kullanıcıyı gösteriyor.

## ✏️ Senaryo 10
Bir online sınav sisteminde eğitmenler, sınav koduna göre sınav sonuçlarını görüntüleyebiliyor. Kod, formdan alınıp ilgili sınav kaydını getirmek üzere sorguda kullanılıyor. Sonuçlar başarı durumlarına göre renkli etiketlerle gösteriliyor. Listeleme sayfası filtrelenebilir yapıya sahip.

