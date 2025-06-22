# CWE-287 - Improper Authentication
<a href="https://cwe.mitre.org/data/definitions/287.html" target="_blank">🔗 CWE-287 - Improper Authentication</a>

## ✏️ Senaryo 1
Bir mobil bankacılık uygulamasında kullanıcılar PIN kodunu girerek giriş yapabiliyor. Uygulama PIN uzunluğunu değerlendirip sisteme erişim sağlıyor. Giriş yapıldıktan sonra kullanıcıya tüm bankacılık işlemleri sunuluyor. PIN girişi uygulamanın ana giriş yöntemi.

## ✏️ Senaryo 2
Bir yönetim panelinde kullanıcılar e-posta adresiyle sisteme giriş yapabiliyor. E-posta adresi girildikten sonra sistem giriş işlemini onaylıyor. Kullanıcı adı giriş alanında herhangi bir e-posta formatı kullanılabiliyor. Giriş sonrası yönetim paneli açılıyor.

## ✏️ Senaryo 3
Bir kurumsal portalda kullanıcılar kullanıcı adlarını girerek oturum açıyor. Giriş ekranında sadece kullanıcı adı alanı bulunuyor. Kullanıcı adı girildikten sonra sistem oturumu başlatıyor. Giriş sonrası kullanıcıya portal içerikleri gösteriliyor.

## ✏️ Senaryo 4
Bir IoT cihaz yönetim uygulamasında cihazlara bağlanmak için kullanıcı adı giriliyor. Uygulama bu bilgiyi kullanarak sunucuya bağlantı kuruyor. Cihaza bağlandıktan sonra tüm yönetim komutlarına erişim açılıyor. Bağlantı işlemi tek adımda gerçekleşiyor.

## ✏️ Senaryo 5
Bir video konferans platformunda kullanıcılar toplantı bağlantısıyla katılım sağlayabiliyor. Bağlantıdaki toplantı ID'si değerlendirilerek erişim veriliyor. Katılımcılar bu bağlantı üzerinden toplantıya dahil oluyor. Toplantı erişimi bağlantı tabanlı.

## ✏️ Senaryo 6
Bir bulut dosya saklama hizmetinde dosyalara kısa bağlantılarla erişilebiliyor. Bağlantıya gelen kullanıcılara dosya içeriği gösteriliyor. Sistem bu kısa bağlantıları otomatik olarak oluşturuyor. Dosya paylaşımı bağlantı tabanlı çalışıyor.

## ✏️ Senaryo 7
Bir e-öğrenme platformunda öğretmenler sınavları yönetebiliyor. Sistem tarayıcı bilgilerini kullanarak kullanıcıyı tanıyor. Sınav yönetim ekranına doğrudan erişim mümkün. Kullanıcı tanıma işlemi tarayıcı verileriyle yapılıyor.

## ✏️ Senaryo 8
Bir rezervasyon uygulamasında işletme sahipleri rezervasyon listesine erişebiliyor. Sistem tarayıcıdaki kullanıcı bilgilerini kontrol ederek listeyi açıyor. Rezervasyon sayfası doğrudan URL ile erişilebilir durumda. Liste görüntüleme tarayıcı verilerine dayanıyor.

## ✏️ Senaryo 9
Bir müşteri destek uygulamasında kullanıcılar destek taleplerini takip edebiliyor. Giriş ekranında isim ve e-posta adresi bilgileri isteniyor. Girilen bilgilerle kullanıcı taleplerine erişim sağlanıyor. Takip işlemi bu iki veri ile gerçekleştiriliyor.

## ✏️ Senaryo 10
Bir web sitesinde yönetici paneline doğrudan URL erişimi bulunuyor. Panel URL'si üzerinden yönetici arayüzüne ulaşılabiliyor. Yönetim işlevleri panel içerisinde görüntüleniyor. Panel erişimi URL tabanlı çalışıyor.

