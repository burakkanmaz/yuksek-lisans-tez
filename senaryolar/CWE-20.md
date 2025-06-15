# CWE-20 - Improper Input Validation
<a href="https://cwe.mitre.org/data/definitions/20.html" target="_blank">🔗 CWE-20 - Improper Input Validation</a>

## ✏️ Senaryo 1
Bir e-ticaret sitesinde kullanıcılar ödeme ekranında adres bilgilerini manuel olarak girebiliyor. Sistem, bu bilgileri aldıktan sonra kargo firmalarına iletiyor. Kullanıcının girdiği alanlar, sunucuya doğrudan aktarılıyor ve herhangi bir biçim kontrolü uygulanmıyor. Adres, il ve posta kodu gibi alanlara her türlü içerik yazılabiliyor.

## ✏️ Senaryo 2
Bir eğitim platformunda kullanıcılar yeni şifre oluştururken istedikleri herhangi bir metni yazabiliyor. Şifre giriş alanı minimum uzunluk şartı dışında başka kontrol içermiyor. Kullanıcılar şifrede özel karakter, boşluk veya sistem komutu gibi içerikler kullanabiliyor. Şifre doğrudan veritabanına kaydediliyor.

## ✏️ Senaryo 3
Bir kargo takip sisteminde kullanıcılar kargo numarasını girerek paket bilgilerine erişiyor. Kargo numarası metin kutusuna yazılıyor ve sistem bu değeri arka planda sorgulama için kullanıyor. Giriş alanında sadece uzunluk kontrolü yapılıyor. Harf, sembol veya komut karakterleri kontrol edilmiyor.

## ✏️ Senaryo 4
Bir sosyal medya platformunda kullanıcılar biyografi bilgilerini istedikleri gibi doldurabiliyor. Biyografi alanı karakter sınırı dışında herhangi bir denetim uygulanmadan veritabanına kaydediliyor. Kullanıcı adları ve profiller bu bilgiyle birlikte görüntüleniyor. Girişte HTML veya özel semboller sınırlandırılmamış.

## ✏️ Senaryo 5
Bir rezervasyon sisteminde kullanıcılar tarih aralığı girerek uygunluk sorgulaması yapabiliyor. Tarih alanları, metin olarak dolduruluyor ve sistem bunu doğrudan işliyor. Geçersiz format, boşluklar veya gelecekteki tarihlerle ilgili kontrol yapılmıyor. Giriş formatı serbest bırakılmış.

## ✏️ Senaryo 6
Bir forum sisteminde kullanıcılar konu başlığı ve içerik girerek yeni konu açabiliyor. Sistem yalnızca karakter sayısını denetliyor. Başlık kısmına sayılar, semboller ya da boşluk dizileri girilebiliyor. Konular daha sonra ana sayfada listeleniyor.

## ✏️ Senaryo 7
Bir üyelik formunda kullanıcılar doğum tarihi bilgisini elle giriyor. Tarih formatı belirgin şekilde belirtilmemiş ve sistem sadece alanın dolu olmasını yeterli sayıyor. Kullanıcılar metin, sayı ya da alakasız ifadeler yazabiliyor. Bu bilgi üyelik sonrası profil sayfasında gösteriliyor.

## ✏️ Senaryo 8
Bir dosya arama sisteminde kullanıcılar dosya adını yazarak arama yapıyor. Sistem arama kutusuna yazılan değeri doğrudan sorguya dönüştürüyor. Dosya adı kısmında sembol, uzantı ya da özel karakterlere karşı bir kısıtlama yok. Arama sonuçları kullanıcıya filtrelenmeden sunuluyor.

## ✏️ Senaryo 9
Bir blog platformunda kullanıcılar başlıklara etiket ekleyebiliyor. Etiket giriş alanı serbest metin olarak tasarlanmış. Kullanıcılar sistemle ilgisiz veya çok uzun ifadeleri etiket olarak belirleyebiliyor. Bu etiketler filtreleme sisteminde görünür hale geliyor.

## ✏️ Senaryo 10
Bir anket sisteminde katılımcılar yaş bilgilerini girerek anketi başlatabiliyor. Yaş alanı yalnızca boş olup olmadığına bakılarak doğrulanıyor. Sayı, harf veya kelime gibi farklı formatlar girilebiliyor. Yaş bilgisi raporlarda doğrudan gösteriliyor.

