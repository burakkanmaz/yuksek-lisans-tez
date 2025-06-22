# CWE-20 - Improper Input Validation
<a href="https://cwe.mitre.org/data/definitions/20.html" target="_blank">🔗 CWE-20 - Improper Input Validation</a>

## ✏️ Senaryo 1
Bir e-ticaret sitesinde kullanıcılar ödeme ekranında adres bilgilerini girebiliyor. Bu bilgiler sisteme kaydedildikten sonra kargo firmalarına iletiliyor. Adres, il ve posta kodu alanları metin kutularından alınıyor. Kullanıcılar bu alanlara istedikleri içeriği yazabiliyor.

## ✏️ Senaryo 2
Bir eğitim platformunda kullanıcılar şifre oluştururken serbest metin girebiliyor. Şifre alanı minimum uzunluk şartı bulunuyor. Özel karakter, boşluk ve farklı semboller şifrede kullanılabiliyor. Şifre bilgisi sisteme kaydediliyor.

## ✏️ Senaryo 3
Bir kargo takip sisteminde kullanıcılar kargo numarasını girerek paket bilgilerine erişiyor. Kargo numarası metin kutusuna yazılıyor ve sorgulama işlemi başlatılıyor. Giriş alanında uzunluk sınırı bulunuyor. Farklı karakter türleri girişte kullanılabiliyor.

## ✏️ Senaryo 4
Bir sosyal medya platformunda kullanıcılar biyografi bilgilerini doldurabiliyor. Biyografi alanı karakter sınırı ile sınırlandırılmış. Bu bilgiler kullanıcı profillerinde görüntüleniyor. HTML ve özel semboller girişte kullanılabiliyor.

## ✏️ Senaryo 5
Bir rezervasyon sisteminde kullanıcılar tarih aralığı girerek uygunluk sorgulaması yapabiliyor. Tarih alanları metin girişi ile doldurulabiliyor. Sistem bu tarih bilgilerini işleyerek uygunluk kontrolü yapıyor. Tarih formatı serbest bırakılmış.

## ✏️ Senaryo 6
Bir forum sisteminde kullanıcılar konu başlığı ve içerik girerek yeni konu açabiliyor. Karakter sayısı sınırlaması bulunuyor. Başlık alanına sayılar ve semboller girilebiliyor. Konular ana sayfada listeleniyor.

## ✏️ Senaryo 7
Bir üyelik formunda kullanıcılar doğum tarihi bilgisini elle girebiliyor. Tarih formatı açık şekilde belirtilmemiş. Sistem alanın dolu olmasını kontrol ediyor. Bu bilgi üyelik sonrası profil sayfasında gösteriliyor.

## ✏️ Senaryo 8
Bir dosya arama sisteminde kullanıcılar dosya adını yazarak arama yapıyor. Arama kutusu girilen değeri sorguya dönüştürüyor. Dosya adında sembol ve özel karakterler kullanılabiliyor. Arama sonuçları kullanıcıya sunuluyor.

## ✏️ Senaryo 9
Bir blog platformunda kullanıcılar başlıklara etiket ekleyebiliyor. Etiket giriş alanı serbest metin formatında. Uzun ifadeler etiket olarak belirlenebiliyor. Bu etiketler filtreleme sisteminde görüntüleniyor.

## ✏️ Senaryo 10
Bir anket sisteminde katılımcılar yaş bilgilerini girerek anketi başlatabiliyor. Yaş alanı doldurulup doldurulmadığı kontrol ediliyor. Farklı formatlar yaş alanına girilebiliyor. Yaş bilgisi raporlarda gösteriliyor.

