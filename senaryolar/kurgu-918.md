# CWE-918 - Server-Side Request Forgery (SSRF)
<a href="https://cwe.mitre.org/data/definitions/918.html" target="_blank">🔗 CWE-918 - Server-Side Request Forgery (SSRF)</a>

## ✏️ Senaryo 1
Bir web uygulaması kullanıcıların belirttiği URL'lerden veri çeker. Kullanıcılar RSS feed adresleri veya API endpoint'leri girebilir. Sistem bu adreslere istek göndererek içeriği alır. İçerik işlendikten sonra kullanıcıya sunulur.

## ✏️ Senaryo 2
Bir içerik toplama servisi farklı kaynaklardan bilgi alır. Kullanıcılar veri kaynağı URL'lerini sisteme kaydedebilir. Servis bu URL'lere düzenli olarak erişim sağlar. Toplanan veriler analiz edilerek raporlanır.

## ✏️ Senaryo 3
Bir web sayfası önizleme aracı URL'leri ziyaret ederek ekran görüntüsü alır. Kullanıcılar önizlemek istedikleri web sayfası adresini girebilir. Sistem belirtilen sayfaya erişerek görüntüsünü oluşturur. Oluşturulan önizleme kullanıcıya gösterilir.

## ✏️ Senaryo 4
Bir API proxy servisi istemci isteklerini hedef sunuculara yönlendirir. İstemciler hangi API'ye erişmek istediklerini belirtir. Proxy servisi bu istekleri hedef sunucuya iletir. Yanıt alındığında istemciye geri döndürülür.

## ✏️ Senaryo 5
Bir dosya indirme uygulaması uzak sunuculardan dosyaları çeker. Kullanıcılar indirmek istedikleri dosyanın URL'sini girebilir. Sistem belirtilen adresten dosyayı indirir. İndirilen dosya kullanıcı depolamasına kaydedilir.

## ✏️ Senaryo 6
Bir webhook yönetim sistemi harici servislerden bildirimleri alır. Kullanıcılar webhook URL'lerini sisteme kaydeder. Sistem bu URL'lere test istekleri gönderebilir. Webhook bağlantıları düzenli olarak kontrol edilir.

## ✏️ Senaryo 7
Bir link doğrulama servisi URL'lerin erişilebilirliğini kontrol eder. Kullanıcılar kontrol edilmesini istedikleri linkleri girebilir. Sistem bu linklere erişim deneyerek durumlarını raporlar. Sonuçlar kullanıcıya detaylı olarak sunulur.

## ✏️ Senaryo 8
Bir veri senkronizasyon aracı farklı sistemler arasında bilgi alışverişi yapar. Kullanıcılar senkronize edilecek veri kaynaklarını belirtir. Araç bu kaynaklara erişerek verileri çeker. Çekilen veriler hedef sistemlere aktarılır.

## ✏️ Senaryo 9
Bir medya içerik yönetimi servisi harici kaynaklardan medya dosyalarını alır. Kullanıcılar medya URL'lerini sisteme ekleyebilir. Servis bu URL'lerdeki içerikleri indirir ve işler. İşlenen medya dosyaları kullanıcı galerisinde gösterilir.

## ✏️ Senaryo 10
Bir API test aracı farklı endpoint'leri test etmek için istekler gönderir. Kullanıcılar test edilecek API URL'lerini belirtir. Araç bu endpoint'lere test istekleri göndererek yanıtları analiz eder. Test sonuçları rapor halinde sunulur.

