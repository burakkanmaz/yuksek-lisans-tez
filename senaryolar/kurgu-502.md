# CWE-502 - Deserialization of Untrusted Data
<a href="https://cwe.mitre.org/data/definitions/502.html" target="_blank">🔗 CWE-502 - Deserialization of Untrusted Data</a>

## ✏️ Senaryo 1
Bir web uygulamasında kullanıcı oturum bilgileri cookie formatında saklanır. Oturum verileri seri hale getirilerek tarayıcıya gönderilir. Kullanıcı sitesine tekrar geldiğinde bu veriler okunur ve işlenir. Sistem oturum durumunu bu bilgilerle yeniden oluşturur.

## ✏️ Senaryo 2
Bir dosya paylaşım uygulamasında kullanıcı tercihleri dosya formatında kaydedilir. Tercih dosyaları binary formatta seri hale getirilir. Uygulama başlatıldığında bu dosyalar okunur ve ayarlar yüklenir. Kullanıcı deneyimi önceki tercihlerle devam eder.

## ✏️ Senaryo 3
Bir oyun uygulamasında oyuncu ilerlemesi kayıt dosyalarında tutulur. Oyun verileri kompakt format kullanılarak saklanır. Oyun başlatıldığında kayıt dosyası okunur ve durum geri yüklenir. Oyuncu kaldığı yerden devam edebilir.

## ✏️ Senaryo 4
Bir API uygulamasında istemci verileri JSON formatında alınır. Gelen veriler sistem nesnelerine dönüştürülür. API bu nesneleri kullanarak iş mantığını yürütür. Yanıt verileri yine JSON formatında geri gönderilir.

## ✏️ Senaryo 5
Bir konfigürasyon yönetim sisteminde ayar dosyaları YAML formatında saklanır. Sistem başlangıcında bu dosyalar okunur ve yapı nesnelerine çevrilir. Uygulamanın çalışma parametreleri bu verilerle belirlenir. Ayarlar runtime sırasında kullanılır.

## ✏️ Senaryo 6
Bir mesajlaşma uygulamasında mesaj geçmişi arşiv formatında kaydedilir. Eski mesajlar binary protokol kullanılarak saklanır. Kullanıcı geçmişe baktığında veriler okunur ve görüntülenir. Mesaj objelerri yeniden oluşturulur.

## ✏️ Senaryo 7
Bir cache sistemi veri nesnelerini hızlı erişim için depolar. Nesneler bellek içinde seri formatta tutulur. İstek geldiğinde cache verisi okunur ve nesneye dönüştürülür. Sistem performansı cache kullanımıyla artırılır.

## ✏️ Senaryo 8
Bir rapor uygulamasında şablon dosyaları özel formatta kaydedilir. Şablonlar tasarım verilerini içerir. Rapor oluşturulurken şablon dosyası okunur ve işlenir. Rapor yapısı şablon verilerine göre oluşturulur.

## ✏️ Senaryo 9
Bir workflow sistemi süreç tanımlarını dosyalarda saklar. Süreçler XML formatında seri hale getirilir. Workflow çalıştırıldığında tanım dosyası okunur ve işlenir. Süreç adımları bu verilerle oluşturulur.

## ✏️ Senaryo 10
Bir e-ticaret uygulamasında sepet bilgileri session datasında tutulur. Sepet içeriği serialize edilerek saklanır. Kullanıcı alışverişe devam ettiğinde bu veriler restore edilir. Sepet durumu önceki halini korur.

