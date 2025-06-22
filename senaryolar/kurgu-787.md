# CWE-787 - Out-of-bounds Write
<a href="https://cwe.mitre.org/data/definitions/787.html" target="_blank">🔗 CWE-787 - Out-of-bounds Write</a>

## ✏️ Senaryo 1
Bir metin editörü uygulamasında kullanıcılar belge içeriğini düzenler. Sistem metin verilerini bellek alanlarında saklar. Kullanıcı düzenlemeleri sistem tarafından işlenir ve kayıt edilir. Belge içeriği düzenli olarak güncellenir.

## ✏️ Senaryo 2
Bir grafik tasarım uygulamasında kullanıcılar piksel verilerini değiştirir. Görüntü verileri bellek buffer'larında tutulur. Kullanıcı düzenlemeleri sistem tarafından işlenir. Görüntü değişiklikleri ekranda gösterilir.

## ✏️ Senaryo 3
Bir ses düzenleme programında kullanıcılar audio verilerini işler. Ses örnekleri bellek dizilerinde saklanır. Kullanıcı düzenlemeleri sistem tarafından uygulanır. Ses dosyası yeni haliyle kaydedilir.

## ✏️ Senaryo 4
Bir veri işleme uygulamasında kullanıcılar büyük veri setlerini yönetir. Veriler bellek yapılarında organize edilir. Kullanıcı işlemleri sistem tarafından gerçekleştirilir. İşlenmiş veriler kullanıcıya sunulur.

## ✏️ Senaryo 5
Bir oyun uygulamasında kullanıcılar oyun dünyasını değiştirir. Oyun verileri bellek alanlarında tutulur. Kullanıcı eylemleri sistem tarafından uygulanır. Oyun durumu sürekli güncellenir.

## ✏️ Senaryo 6
Bir dosya işleme uygulamasında kullanıcılar dosya içeriklerini düzenler. Dosya verileri bellek buffer'larında saklanır. Kullanıcı değişiklikleri sistem tarafından işlenir. Dosya yeni haliyle kaydedilir.

## ✏️ Senaryo 7
Bir spreadsheet uygulamasında kullanıcılar hücre verilerini girer. Tablo verileri bellek matrislerinde tutulur. Kullanıcı girişleri sistem tarafından kaydedilir. Hesaplamalar otomatik olarak yapılır.

## ✏️ Senaryo 8
Bir çizim uygulamasında kullanıcılar çizgi ve şekiller oluşturur. Çizim verileri bellek alanlarında saklanır. Kullanıcı girişleri sistem tarafından işlenir. Çizim ekranda görüntülenir.

## ✏️ Senaryo 9
Bir video düzenleme uygulamasında kullanıcılar frame verilerini değiştirir. Video verileri bellek buffer'larında tutulur. Kullanıcı düzenlemeleri sistem tarafından uygulanır. Video yeni haliyle oluşturulur.

## ✏️ Senaryo 10
Bir form uygulamasında kullanıcılar form alanlarını doldurur. Form verileri bellek yapılarında saklanır. Kullanıcı girişleri sistem tarafından işlenir. Form verileri doğrulanır ve kaydedilir.

