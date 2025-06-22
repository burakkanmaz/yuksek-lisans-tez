### 🧪 Senaryo 1: Bir e-ticaret sitesinde kullanıcılar ödeme ekranında adres bilgilerini girebiliyor. Bu bilgiler sisteme kaydedildikten sonra kargo firmalarına iletiliyor. Adres, il ve posta kodu alanları metin kutularından alınıyor. Kullanıcılar bu alanlara istedikleri içeriği yazabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 18
```csharp
[HttpPost("submit-address")]
public IActionResult SubmitAddress([FromBody] AddressModel model)
{
    if (ModelState.IsValid)
    {
        _dbContext.Addresses.Add(model);
        _dbContext.SaveChanges();
        return Ok();
    }
    return BadRequest(ModelState);
}

public class AddressModel
{
    public string AddressLine { get; set; }
    public string City { get; set; }
    public string PostalCode { get; set; }
}
```

---

### 🧪 Senaryo 1: Bir e-ticaret sitesinde kullanıcılar ödeme ekranında adres bilgilerini girebiliyor. Bu bilgiler sisteme kaydedildikten sonra kargo firmalarına iletiliyor. Adres, il ve posta kodu alanları metin kutularından alınıyor. Kullanıcılar bu alanlara istedikleri içeriği yazabiliyor.

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 16
```python
from flask import Flask, request, jsonify
from models import db, Address

app = Flask(__name__)

@app.route('/submit-address', methods=['POST'])
def submit_address():
    data = request.json
    new_address = Address(
        address_line=data['address_line'],
        city=data['city'],
        postal_code=data['postal_code']
    )
    db.session.add(new_address)
    db.session.commit()
    return jsonify({"message": "Address saved successfully"}), 200
```

---

### 🧪 Senaryo 1: Bir e-ticaret sitesinde kullanıcılar ödeme ekranında adres bilgilerini girebiliyor. Bu bilgiler sisteme kaydedildikten sonra kargo firmalarına iletiliyor. Adres, il ve posta kodu alanları metin kutularından alınıyor. Kullanıcılar bu alanlara istedikleri içeriği yazabiliyor.

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 18
```typescript
import express from 'express';
import { PrismaClient } from '@prisma/client';

const app = express();
app.use(express.json());
const prisma = new PrismaClient();

app.post('/submit-address', async (req, res) => {
    const { addressLine, city, postalCode } = req.body;
    const newAddress = await prisma.address.create({
        data: {
            addressLine,
            city,
            postalCode,
        },
    });
    res.json(newAddress);
});
```

---

### 🧪 Senaryo 2: Bir eğitim platformunda kullanıcılar şifre oluştururken serbest metin girebiliyor. Şifre alanı minimum uzunluk şartı bulunuyor. Özel karakter, boşluk ve farklı semboller şifrede kullanılabiliyor. Şifre bilgisi sisteme kaydediliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 16
```csharp
[HttpPost("create-password")]
public IActionResult CreatePassword([FromBody] PasswordModel model)
{
    if (model.Password.Length >= 8)
    {
        _dbContext.Passwords.Add(model);
        _dbContext.SaveChanges();
        return Ok();
    }
    return BadRequest("Password too short");
}

public class PasswordModel
{
    public string Password { get; set; }
}
```

---

### 🧪 Senaryo 2: Bir eğitim platformunda kullanıcılar şifre oluştururken serbest metin girebiliyor. Şifre alanı minimum uzunluk şartı bulunuyor. Özel karakter, boşluk ve farklı semboller şifrede kullanılabiliyor. Şifre bilgisi sisteme kaydediliyor.

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 9
```python
@app.route('/create-password', methods=['POST'])
def create_password():
    data = request.json
    if len(data['password']) >= 8:
        new_password = Password(password=data['password'])
        db.session.add(new_password)
        db.session.commit()
        return jsonify({"message": "Password saved"})
    return jsonify({"error": "Password too short"}), 400
```

---

### 🧪 Senaryo 2: Bir eğitim platformunda kullanıcılar şifre oluştururken serbest metin girebiliyor. Şifre alanı minimum uzunluk şartı bulunuyor. Özel karakter, boşluk ve farklı semboller şifrede kullanılabiliyor. Şifre bilgisi sisteme kaydediliyor.

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 11
```typescript
app.post('/create-password', async (req, res) => {
    const { password } = req.body;
    if (password.length >= 8) {
        const newPassword = await prisma.password.create({
            data: { password },
        });
        res.json(newPassword);
    } else {
        res.status(400).json({ error: "Password too short" });
    }
});
```

---

### 🧪 Senaryo 3: Bir kargo takip sisteminde kullanıcılar kargo numarasını girerek paket bilgilerine erişiyor. Kargo numarası metin kutusuna yazılıyor ve sorgulama işlemi başlatılıyor. Giriş alanında uzunluk sınırı bulunuyor. Farklı karakter türleri girişte kullanılabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 10
```csharp
[HttpGet("track-package")]
public IActionResult TrackPackage(string trackingNumber)
{
    if (trackingNumber.Length <= 20)
    {
        var result = _dbContext.Packages.FirstOrDefault(p => p.TrackingNumber == trackingNumber);
        return Ok(result);
    }
    return BadRequest("Invalid tracking number");
}
```

---

### 🧪 Senaryo 3: Bir kargo takip sisteminde kullanıcılar kargo numarasını girerek paket bilgilerine erişiyor. Kargo numarası metin kutusuna yazılıyor ve sorgulama işlemi başlatılıyor. Giriş alanında uzunluk sınırı bulunuyor. Farklı karakter türleri girişte kullanılabiliyor.

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 7
```python
@app.route('/track-package', methods=['GET'])
def track_package():
    tracking_number = request.args.get('trackingNumber')
    if len(tracking_number) <= 20:
        result = Package.query.filter_by(tracking_number=tracking_number).first()
        return jsonify(result.serialize() if result else {})
    return jsonify({"error": "Invalid tracking number"}), 400
```

---

### 🧪 Senaryo 3: Bir kargo takip sisteminde kullanıcılar kargo numarasını girerek paket bilgilerine erişiyor. Kargo numarası metin kutusuna yazılıyor ve sorgulama işlemi başlatılıyor. Giriş alanında uzunluk sınırı bulunuyor. Farklı karakter türleri girişte kullanılabiliyor.

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 9
```typescript
app.get('/track-package', async (req, res) => {
    const trackingNumber = req.query.trackingNumber as string;
    if (trackingNumber.length <= 20) {
        const packageInfo = await prisma.package.findFirst({ where: { trackingNumber } });
        res.json(packageInfo);
    } else {
        res.status(400).json({ error: "Invalid tracking number" });
    }
});
```

---

### 🧪 Senaryo 4: Bir sosyal medya platformunda kullanıcılar biyografi bilgilerini doldurabiliyor. Biyografi alanı karakter sınırı ile sınırlandırılmış. Bu bilgiler kullanıcı profillerinde görüntüleniyor. HTML ve özel semboller girişte kullanılabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 16
```csharp
[HttpPost("update-bio")]
public IActionResult UpdateBio([FromBody] BioModel model)
{
    if (model.Biography.Length <= 500)
    {
        _dbContext.Biographies.Add(model);
        _dbContext.SaveChanges();
        return Ok();
    }
    return BadRequest("Biography too long");
}

public class BioModel
{
    public string Biography { get; set; }
}
```

---

### 🧪 Senaryo 4: Bir sosyal medya platformunda kullanıcılar biyografi bilgilerini doldurabiliyor. Biyografi alanı karakter sınırı ile sınırlandırılmış. Bu bilgiler kullanıcı profillerinde görüntüleniyor. HTML ve özel semboller girişte kullanılabiliyor.

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 9
```python
@app.route('/update-bio', methods=['POST'])
def update_bio():
    data = request.json
    if len(data['biography']) <= 500:
        new_bio = Biography(biography=data['biography'])
        db.session.add(new_bio)
        db.session.commit()
        return jsonify({"message": "Biography saved"})
    return jsonify({"error": "Biography too long"}), 400
```

---

### 🧪 Senaryo 4: Bir sosyal medya platformunda kullanıcılar biyografi bilgilerini doldurabiliyor. Biyografi alanı karakter sınırı ile sınırlandırılmış. Bu bilgiler kullanıcı profillerinde görüntüleniyor. HTML ve özel semboller girişte kullanılabiliyor.

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 9
```typescript
app.post('/update-bio', async (req, res) => {
    const { biography } = req.body;
    if (biography.length <= 500) {
        const newBio = await prisma.biography.create({ data: { biography } });
        res.json(newBio);
    } else {
        res.status(400).json({ error: "Biography too long" });
    }
});
```

---

### 🧪 Senaryo 5: Bir rezervasyon sisteminde kullanıcılar tarih aralığı girerek uygunluk sorgulaması yapabiliyor. Tarih alanları metin girişi ile doldurulabiliyor. Sistem bu tarih bilgilerini işleyerek uygunluk kontrolü yapıyor. Tarih formatı serbest bırakılmış.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 17
```csharp
[HttpPost("check-availability")]
public IActionResult CheckAvailability([FromBody] DateRangeModel model)
{
    DateTime start, end;
    if (DateTime.TryParse(model.StartDate, out start) && DateTime.TryParse(model.EndDate, out end))
    {
        var available = _reservationService.IsAvailable(start, end);
        return Ok(new { available });
    }
    return BadRequest("Invalid date format");
}

public class DateRangeModel
{
    public string StartDate { get; set; }
    public string EndDate { get; set; }
}
```

---

### 🧪 Senaryo 5: Bir rezervasyon sisteminde kullanıcılar tarih aralığı girerek uygunluk sorgulaması yapabiliyor. Tarih alanları metin girişi ile doldurulabiliyor. Sistem bu tarih bilgilerini işleyerek uygunluk kontrolü yapıyor. Tarih formatı serbest bırakılmış.

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 10
```python
@app.route('/check-availability', methods=['POST'])
def check_availability():
    data = request.json
    try:
        start = datetime.strptime(data['start_date'], '%Y-%m-%d')
        end = datetime.strptime(data['end_date'], '%Y-%m-%d')
        available = reservation_service.is_available(start, end)
        return jsonify({"available": available})
    except:
        return jsonify({"error": "Invalid date format"}), 400
```

---

### 🧪 Senaryo 5: Bir rezervasyon sisteminde kullanıcılar tarih aralığı girerek uygunluk sorgulaması yapabiliyor. Tarih alanları metin girişi ile doldurulabiliyor. Sistem bu tarih bilgilerini işleyerek uygunluk kontrolü yapıyor. Tarih formatı serbest bırakılmış.

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 10
```typescript
app.post('/check-availability', async (req, res) => {
    const { startDate, endDate } = req.body;
    const start = new Date(startDate);
    const end = new Date(endDate);
    if (isNaN(start.getTime()) || isNaN(end.getTime())) {
        return res.status(400).json({ error: "Invalid date format" });
    }
    const available = await reservationService.isAvailable(start, end);
    res.json({ available });
});
```

---

### 🧪 Senaryo 6: Bir forum sisteminde kullanıcılar konu başlığı ve içerik girerek yeni konu açabiliyor. Karakter sayısı sınırlaması bulunuyor. Başlık alanına sayılar ve semboller girilebiliyor. Konular ana sayfada listeleniyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 17
```csharp
[HttpPost("create-topic")]
public IActionResult CreateTopic([FromBody] TopicModel model)
{
    if (model.Title.Length <= 100 && model.Content.Length <= 1000)
    {
        _dbContext.Topics.Add(model);
        _dbContext.SaveChanges();
        return Ok();
    }
    return BadRequest("Title or content too long");
}

public class TopicModel
{
    public string Title { get; set; }
    public string Content { get; set; }
}
```

---

### 🧪 Senaryo 6: Bir forum sisteminde kullanıcılar konu başlığı ve içerik girerek yeni konu açabiliyor. Karakter sayısı sınırlaması bulunuyor. Başlık alanına sayılar ve semboller girilebiliyor. Konular ana sayfada listeleniyor.

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 9
```python
@app.route('/create-topic', methods=['POST'])
def create_topic():
    data = request.json
    if len(data['title']) <= 100 and len(data['content']) <= 1000:
        topic = Topic(title=data['title'], content=data['content'])
        db.session.add(topic)
        db.session.commit()
        return jsonify({"message": "Topic created"})
    return jsonify({"error": "Input too long"}), 400
```

---

### 🧪 Senaryo 6: Bir forum sisteminde kullanıcılar konu başlığı ve içerik girerek yeni konu açabiliyor. Karakter sayısı sınırlaması bulunuyor. Başlık alanına sayılar ve semboller girilebiliyor. Konular ana sayfada listeleniyor.

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 9
```typescript
app.post('/create-topic', async (req, res) => {
    const { title, content } = req.body;
    if (title.length <= 100 && content.length <= 1000) {
        const newTopic = await prisma.topic.create({ data: { title, content } });
        res.json(newTopic);
    } else {
        res.status(400).json({ error: "Input too long" });
    }
});
```

---

### 🧪 Senaryo 7: Bir üyelik formunda kullanıcılar doğum tarihi bilgisini elle girebiliyor. Tarih formatı açık şekilde belirtilmemiş. Sistem alanın dolu olmasını kontrol ediyor. Bu bilgi üyelik sonrası profil sayfasında gösteriliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 16
```csharp
[HttpPost("set-birthdate")]
public IActionResult SetBirthdate([FromBody] BirthdateModel model)
{
    if (!string.IsNullOrEmpty(model.Birthdate))
    {
        _dbContext.Users.Add(model);
        _dbContext.SaveChanges();
        return Ok();
    }
    return BadRequest("Birthdate is required");
}

public class BirthdateModel
{
    public string Birthdate { get; set; }
}
```

---

### 🧪 Senaryo 7: Bir üyelik formunda kullanıcılar doğum tarihi bilgisini elle girebiliyor. Tarih formatı açık şekilde belirtilmemiş. Sistem alanın dolu olmasını kontrol ediyor. Bu bilgi üyelik sonrası profil sayfasında gösteriliyor.

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 9
```python
@app.route('/set-birthdate', methods=['POST'])
def set_birthdate():
    data = request.json
    if data.get('birthdate'):
        birth = Birthdate(birthdate=data['birthdate'])
        db.session.add(birth)
        db.session.commit()
        return jsonify({"message": "Birthdate saved"})
    return jsonify({"error": "Birthdate required"}), 400
```

---

### 🧪 Senaryo 7: Bir üyelik formunda kullanıcılar doğum tarihi bilgisini elle girebiliyor. Tarih formatı açık şekilde belirtilmemiş. Sistem alanın dolu olmasını kontrol ediyor. Bu bilgi üyelik sonrası profil sayfasında gösteriliyor.

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 9
```typescript
app.post('/set-birthdate', async (req, res) => {
    const { birthdate } = req.body;
    if (birthdate) {
        const newRecord = await prisma.birthdate.create({ data: { birthdate } });
        res.json(newRecord);
    } else {
        res.status(400).json({ error: "Birthdate is required" });
    }
});
```

---

### 🧪 Senaryo 8: Bir dosya arama sisteminde kullanıcılar dosya adını yazarak arama yapıyor. Arama kutusu girilen değeri sorguya dönüştürüyor. Dosya adında sembol ve özel karakterler kullanılabiliyor. Arama sonuçları kullanıcıya sunuluyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```csharp
[HttpGet("search-file")]
public IActionResult SearchFile(string fileName)
{
    var results = _dbContext.Files
        .Where(f => f.Name.Contains(fileName))
        .ToList();
    return Ok(results);
}
```

---

### 🧪 Senaryo 8: Bir dosya arama sisteminde kullanıcılar dosya adını yazarak arama yapıyor. Arama kutusu girilen değeri sorguya dönüştürüyor. Dosya adında sembol ve özel karakterler kullanılabiliyor. Arama sonuçları kullanıcıya sunuluyor.

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 5
```python
@app.route('/search-file', methods=['GET'])
def search_file():
    name = request.args.get('file_name')
    results = File.query.filter(File.name.contains(name)).all()
    return jsonify([r.serialize() for r in results])
```

---

### 🧪 Senaryo 8: Bir dosya arama sisteminde kullanıcılar dosya adını yazarak arama yapıyor. Arama kutusu girilen değeri sorguya dönüştürüyor. Dosya adında sembol ve özel karakterler kullanılabiliyor. Arama sonuçları kullanıcıya sunuluyor.

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 7
```typescript
app.get('/search-file', async (req, res) => {
    const fileName = req.query.fileName as string;
    const files = await prisma.file.findMany({
        where: { name: { contains: fileName } }
    });
    res.json(files);
});
```

---

### 🧪 Senaryo 9: Bir blog platformunda kullanıcılar başlıklara etiket ekleyebiliyor. Etiket giriş alanı serbest metin formatında. Uzun ifadeler etiket olarak belirlenebiliyor. Bu etiketler filtreleme sisteminde görüntüleniyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 12
```csharp
[HttpPost("add-tag")]
public IActionResult AddTag([FromBody] TagModel model)
{
    _dbContext.Tags.Add(model);
    _dbContext.SaveChanges();
    return Ok();
}

public class TagModel
{
    public string TagText { get; set; }
}
```

---

### 🧪 Senaryo 9: Bir blog platformunda kullanıcılar başlıklara etiket ekleyebiliyor. Etiket giriş alanı serbest metin formatında. Uzun ifadeler etiket olarak belirlenebiliyor. Bu etiketler filtreleme sisteminde görüntüleniyor.

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 7
```python
@app.route('/add-tag', methods=['POST'])
def add_tag():
    data = request.json
    tag = Tag(tag_text=data['tag_text'])
    db.session.add(tag)
    db.session.commit()
    return jsonify({"message": "Tag added"})
```

---

### 🧪 Senaryo 9: Bir blog platformunda kullanıcılar başlıklara etiket ekleyebiliyor. Etiket giriş alanı serbest metin formatında. Uzun ifadeler etiket olarak belirlenebiliyor. Bu etiketler filtreleme sisteminde görüntüleniyor.

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 5
```typescript
app.post('/add-tag', async (req, res) => {
    const { tagText } = req.body;
    const tag = await prisma.tag.create({ data: { tagText } });
    res.json(tag);
});
```

---

### 🧪 Senaryo 10: Bir anket sisteminde katılımcılar yaş bilgilerini girerek anketi başlatabiliyor. Yaş alanı doldurulup doldurulmadığı kontrol ediliyor. Farklı formatlar yaş alanına girilebiliyor. Yaş bilgisi raporlarda gösteriliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 16
```csharp
[HttpPost("submit-age")]
public IActionResult SubmitAge([FromBody] AgeModel model)
{
    if (!string.IsNullOrEmpty(model.Age))
    {
        _dbContext.Ages.Add(model);
        _dbContext.SaveChanges();
        return Ok();
    }
    return BadRequest("Age is required");
}

public class AgeModel
{
    public string Age { get; set; }
}
```

---

### 🧪 Senaryo 10: Bir anket sisteminde katılımcılar yaş bilgilerini girerek anketi başlatabiliyor. Yaş alanı doldurulup doldurulmadığı kontrol ediliyor. Farklı formatlar yaş alanına girilebiliyor. Yaş bilgisi raporlarda gösteriliyor.

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 9
```python
@app.route('/submit-age', methods=['POST'])
def submit_age():
    data = request.json
    if data.get('age'):
        age = Age(age=data['age'])
        db.session.add(age)
        db.session.commit()
        return jsonify({"message": "Age saved"})
    return jsonify({"error": "Age is required"}), 400
```

---

### 🧪 Senaryo 10: Bir anket sisteminde katılımcılar yaş bilgilerini girerek anketi başlatabiliyor. Yaş alanı doldurulup doldurulmadığı kontrol ediliyor. Farklı formatlar yaş alanına girilebiliyor. Yaş bilgisi raporlarda gösteriliyor.

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 9
```typescript
app.post('/submit-age', async (req, res) => {
    const { age } = req.body;
    if (age) {
        const ageRecord = await prisma.age.create({ data: { age } });
        res.json(ageRecord);
    } else {
        res.status(400).json({ error: "Age is required" });
    }
});
```
