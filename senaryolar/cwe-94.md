# CWE-94 - Improper Control of Generation of Code
<a href="https://cwe.mitre.org/data/definitions/94.html" target="_blank">🔗 CWE-94 - Improper Control of Generation of Code</a>

## ✏️ Senaryo 1
Bir çevrim içi programlama eğitim platformu, kullanıcıdan alınan kodu belirli şablonlara yerleştirip çalıştırarak çıktı döndürüyor. Kullanıcının yazdığı kod, arka planda doğrudan sistemde derlenip çalıştırılıyor. Kod içeriği öncesinde detaylı analiz edilmeden işleniyor.

## ✏️ Senaryo 2
Bir web tabanlı hesap makinesi uygulamasında, kullanıcıdan gelen ifadeler dinamik olarak JavaScript koduna dönüştürülerek tarayıcıda çalıştırılıyor. İfade kontrolü yapılmadan doğrudan eval fonksiyonuyla işleme alınıyor. Kullanıcıdan gelen tüm içerik kod olarak yorumlanıyor.

## ✏️ Senaryo 3
Bir yazılım geliştirme yardımcısı, kullanıcıdan aldığı girişe göre Python kodu üreterek çalıştırıyor. Kullanıcının belirttiği fonksiyon adı ve parametreler doğrudan kodun içine gömülüyor. Bu işlem sırasında herhangi bir filtreleme yapılmadan metin kodun bir parçası haline geliyor.

## ✏️ Senaryo 4
Bir eklenti motoru, kullanıcıların yüklediği dosyalardan komut seti oluşturarak sistem üzerinde çalıştırıyor. Dosyadaki içerik doğrudan bir betik motoruna aktarılıyor. İçeriğin güvenliği veya izinleri denetlenmeden bu işlem yapılıyor.

## ✏️ Senaryo 5
Bir özelleştirilebilir form uygulaması, kullanıcı tanımlı formülleri bir şablona yerleştirerek işliyor. Formül yapısında kontrol eksikliği olduğunda girilen metin, uygulama içinde çalışan kodun parçası olabiliyor. Bu kodlar çalıştırıldığında beklenmedik sonuçlar doğabiliyor.

## ✏️ Senaryo 6
Bir grafik raporlama aracı, kullanıcıdan gelen filtre kriterlerini şablonlara yerleştirerek SQL benzeri bir betik üretip yorumluyor. Filtrelerin içeriği kontrol edilmediğinde, sistem beklenmedik ifadeleri çalıştırabiliyor. Bu yapı doğrudan kod üretmeye dayalı çalışıyor.

## ✏️ Senaryo 7
Bir test otomasyon aracı, kullanıcıdan gelen test senaryolarını kod bloklarına dönüştürerek otomatik olarak çalıştırıyor. Girişler doğrudan programatik şablonlara yerleştirilerek dosya olarak kaydediliyor ve sistem tarafından derleniyor. İçerik filtrelenmediğinde zararlı kodlar çalışabiliyor.

## ✏️ Senaryo 8
Bir chatbot geliştirme platformu, kullanıcı girdilerini JavaScript içinde kullanılacak şekilde gömüyor. Girdi içeriği escape edilmeden doğrudan şablon kod içerisine yazılıyor. Kod parçası olarak kullanıldığında bu yapı beklenmeyen komutlar çalıştırabiliyor.

## ✏️ Senaryo 9
Bir e-posta otomasyon sistemi, kullanıcıdan gelen kuralları dinamik olarak C# koduna dönüştürüp derliyor. Her kural, belirli şablonlar üzerinden koda yerleştiriliyor. Girdi üzerinde kontrol yapılmadığında beklenmeyen ifadeler doğrudan sistemde çalışan kod haline gelebiliyor.

## ✏️ Senaryo 10
Bir web uygulamasında kullanıcıdan gelen yapılandırma ayarlarıyla JavaScript fonksiyonları dinamik olarak üretiliyor. Ayar içeriği doğrudan script bloğu olarak HTML sayfasına gömülüyor. İçerik kontrolü yapılmadığı durumda kullanıcıdan gelen veri doğrudan kod haline geliyor.

