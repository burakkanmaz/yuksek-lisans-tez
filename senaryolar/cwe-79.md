# CWE-79 - Cross-site Scripting (XSS)
<a href="https://cwe.mitre.org/data/definitions/79.html" target="_blank">🔗 CWE-79 - Cross-site Scripting (XSS)</a>

## ✏️ Senaryo 1
Bir blog platformunda kullanıcılar yazılara yorum bırakabiliyor. Her yorum, metin kutusuna yazıldıktan sonra veritabanına kaydediliyor ve yorum kısmında ziyaretçilere gösteriliyor. Yorum formunda kullanıcı adı ve mesaj alanı bulunuyor. Kullanıcılar herhangi bir kayıt işlemi olmadan da yorum yapabiliyor.

## ✏️ Senaryo 2
Bir müşteri destek sistemi içerisinde kullanıcılar, yaşadıkları sorunu açıklayan formlar dolduruyor. Bu formlar, hem kullanıcıya hem de destek ekibine gösterilen web sayfasında görünüyor. Mesaj alanı çok satırlı metin kutusundan alınıyor ve HTML şablonuna ekleniyor. Sistem, bu mesajı kullanıcının kendi yardım talebi geçmişinde de listeliyor.

## ✏️ Senaryo 3
Bir eğitim portalında öğrenciler, ders videolarının altında geri bildirim paylaşabiliyor. Geri bildirim mesajı, veritabanına eklendikten sonra doğrudan sayfada görüntüleniyor. Sistemde herhangi bir filtreleme veya düzenleme arayüzü olmadan, mesaj ham haliyle kullanıcılara gösteriliyor. Kullanıcılar aynı zamanda diğer öğrencilerin mesajlarını da görebiliyor.

## ✏️ Senaryo 4
Bir forum sitesinde kullanıcılar, başkalarının açtığı konulara cevaplar yazabiliyor. Cevaplar, her kullanıcının profil fotoğrafı ve ismiyle birlikte listeleniyor. Gönderilen içerik doğrudan HTML template'e yerleştirilerek gösteriliyor. Herhangi bir editör veya işaretleme dili kullanılmadan sade metin desteği sağlanıyor.

## ✏️ Senaryo 5
Bir otel rezervasyon sitesinde müşteriler, konakladıkları oteller hakkında görüşlerini paylaşabiliyor. Otel sayfasında tüm yorumlar toplu şekilde listeleniyor. Yorum içeriği, kullanıcıdan alındığı biçimiyle HTML içerisinde yer alıyor. Aynı içerik, yönetici panelinde de görüntülenebiliyor.

## ✏️ Senaryo 6
Bir alışveriş sitesinde kullanıcılar ürünlere puan ve açıklama yazabiliyor. Bu açıklamalar, ürün sayfasında ve ana sayfadaki 'öne çıkan yorumlar' kısmında gösteriliyor. Yorumlar HTML template'e veri olarak doğrudan aktarılıyor. Kullanıcıdan alınan veri üzerinde biçimlendirme kontrolü yapılmıyor.

## ✏️ Senaryo 7
Bir haber uygulamasında okuyucular, haberlere tepki bırakabiliyor ve açıklama yazabiliyor. Açıklamalar yorum başlığı, ad ve mesaj içeriyor. Tüm bilgiler formdan alınıp doğrudan ilgili haberin altına ekleniyor. Editoryal onay süreci olmayan bu sistemde kullanıcılar anında içerik yayınlayabiliyor.

## ✏️ Senaryo 8
Bir etkinlik planlama sitesinde katılımcılar, etkinlik sonrası değerlendirme formu doldurabiliyor. Kullanıcının yazdığı açıklama, etkinlik detay sayfasında görünür hale geliyor. Değerlendirme alanı geniş metin kutusu olarak tasarlanmış ve serbest biçimde doldurulabiliyor. Görselde yorumun tamamı HTML içinde görüntüleniyor.

## ✏️ Senaryo 9
Bir çevrimiçi eğitim sisteminde öğrenciler sınav sonrasında yorum paylaşabiliyor. Yorumlar, hem eğitmenin panelinde hem de sınıf arkadaşlarının ekranında listeleniyor. Yorumun metni olduğu gibi HTML'e gömülüyor. Ekstra işleme veya filtreleme yapılmıyor.

## ✏️ Senaryo 10
Bir restoran değerlendirme platformunda kullanıcılar deneyimlerini paylaşabiliyor. Kullanıcılar, restoran adını ve görüşlerini yazarak gönderiyor. Görüşler, hem mobil uygulamada hem de web arayüzünde HTML formatında gösteriliyor. Mesajlar doğrudan kullanıcıdan gelen metinle oluşturuluyor.

