# CWE-352 - Cross-Site Request Forgery (CSRF)
<a href="https://cwe.mitre.org/data/definitions/352.html" target="_blank">🔗 CWE-352 - Cross-Site Request Forgery (CSRF)</a>

## ✏️ Senaryo 1
Bir sosyal medya uygulamasında kullanıcılar gönderileri şikayet edebiliyor. Şikayet işlemi buton tıklaması ile gerçekleşiyor ve arka planda işlem sunucuya gönderiliyor. Kullanıcı oturumu aktif olduğunda işlem yapılabiliyor. Şikayet edilen içerikler kullanıcı panelinde gösteriliyor.

## ✏️ Senaryo 2
Bir blog yönetim sisteminde yazarlar eski yazılarını silmek için silme bağlantısını kullanabiliyor. Bu bağlantı HTML sayfasında yer alıyor ve silme işlemini başlatıyor. Yazar başka bir sayfaya geçmeden bu işlemi gerçekleştirebiliyor. İşlem sonrası aynı oturum devam ediyor.

## ✏️ Senaryo 3
Bir dosya paylaşım platformunda kullanıcılar paylaşımlarını kaldırmak için kaldır butonuna tıklıyor. Buton arka planda dosya silme işlemini gerçekleştiriyor. Dosyalar kullanıcının yönetim panelinde güncelleniyor. İşlem doğrudan gerçekleşiyor.

## ✏️ Senaryo 4
Bir çevrimiçi ödeme sisteminde kullanıcılar kayıtlı kartlarını silebiliyor. Kart silme işlemi kartın yanındaki ikon ile yapılıyor. İşlem sonucunda kart listesi yenileniyor. Kullanıcı oturumu açık olduğunda işlem gerçekleşebiliyor.

## ✏️ Senaryo 5
Bir içerik yönetim sisteminde yöneticiler sayfa yayın durumunu değiştirebiliyor. Yayından kaldırma işlemi bağlantı tıklaması ile yapılıyor. Sistem bu işlemi gerçekleştirip sayfa durumunu güncelliyor. Yöneticiler işlem sonrası aynı panelde kalıyor.

## ✏️ Senaryo 6
Bir haber uygulamasında editörler kullanıcı yorumlarını gizleyebiliyor. Yorumun yanındaki gizle bağlantısı ile yorum pasif hale getiriliyor. Editör bu işlemi gerçekleştirerek yorum durumunu değiştiriyor. İşlem sonucu yorum listesi güncelleniyor.

## ✏️ Senaryo 7
Bir müzik paylaşım platformunda sanatçılar şarkılarını kaldırmak için sil butonunu kullanıyor. Silme işlemi hızla gerçekleşiyor ve yeni ekran açılmadan tamamlanıyor. Oturum açık olduğunda işlem yapılabiliyor. Geri alma özelliği sunulmuyor.

## ✏️ Senaryo 8
Bir forum uygulamasında yöneticiler kullanıcı profillerini askıya alabiliyor. Askıya alma işlemi profildeki butonla tetikleniyor. İşlem arka planda çalışıp yönetici panelini güncelliyor. Onay kutusu gösterilmiyor.

## ✏️ Senaryo 9
Bir görev yönetim aracında ekip lideri görevleri iptal edebiliyor. İptal işlemi görev detay ekranında tek tıklamayla yapılıyor. Görevler listesinden görev kaldırılıyor. Ek doğrulama istenmeden işlem gerçekleşiyor.

## ✏️ Senaryo 10
Bir eğitim yönetim sisteminde öğretmenler duyuruları silebiliyor. Silme işlemi duyuru başlığının yanındaki bağlantı ile yapılıyor. Bu bağlantı sunucuya istek göndererek duyuruyu kaldırıyor. Öğretmen işlem sonrası aynı sayfada kalıyor.

