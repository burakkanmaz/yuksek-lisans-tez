### 🧪 Senaryo 1: Bir blog platformunda kullanıcılar yazılara yorum bırakabiliyor. Her yorum metin kutusuna yazıldıktan sonra veritabanına kaydediliyor ve yorum bölümünde görüntüleniyor. Yorum formunda kullanıcı adı ve mesaj alanı bulunuyor. Kayıt işlemi olmadan da yorum yapılabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 13
```csharp
[HttpPost("submit-comment")]
public IActionResult SubmitComment(string userName, string message)
{
    var comment = new Comment
    {
        UserName = userName,
        Message = message,
        CreatedAt = DateTime.UtcNow
    };

    _dbContext.Comments.Add(comment);
    _dbContext.SaveChanges();

    return Ok();
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```python
@app.route("/submit-comment", methods=["POST"])
def submit_comment():
    data = request.get_json()
    comment = Comment(
        user_name=data["userName"],
        message=data["message"],
        created_at=datetime.utcnow()
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify({"status": "ok"})
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```ts
app.post("/submit-comment", async (req, res) => {
    const { userName, message } = req.body;

    await db.comment.create({
        data: {
            userName,
            message,
            createdAt: new Date(),
        },
    });

    res.json({ status: "ok" });
});
```

---

### 🧪 Senaryo 2: Bir müşteri destek sisteminde kullanıcılar sorun açıklama formları doldurabiliyor. Bu formlar hem kullanıcıya hem de destek ekibine gösterilen sayfada görünüyor. Mesaj alanı çok satırlı metin kutusundan alınıyor ve HTML şablonuna ekleniyor. Mesajlar kullanıcının yardım talebi geçmişinde listeleniyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 13
```csharp
[HttpPost("submit-comment")]
public IActionResult SubmitComment(string userName, string message)
{
    var comment = new Comment
    {
        UserName = userName,
        Message = message,
        CreatedAt = DateTime.UtcNow
    };

    _dbContext.Comments.Add(comment);
    _dbContext.SaveChanges();

    return Ok();
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```python
@app.route("/submit-comment", methods=["POST"])
def submit_comment():
    data = request.get_json()
    comment = Comment(
        user_name=data["userName"],
        message=data["message"],
        created_at=datetime.utcnow()
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify({"status": "ok"})
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```ts
app.post("/submit-comment", async (req, res) => {
    const { userName, message } = req.body;

    await db.comment.create({
        data: {
            userName,
            message,
            createdAt: new Date(),
        },
    });

    res.json({ status: "ok" });
});
```

---

### 🧪 Senaryo 3: Bir eğitim portalında öğrenciler ders videolarının altında geri bildirim paylaşabiliyor. Geri bildirim mesajları veritabanına eklendikten sonra sayfada gösteriliyor. Mesajlar işlenmeden doğrudan kullanıcılara sunuluyor. Diğer öğrenciler de bu mesajları görebiliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 13
```csharp
[HttpPost("submit-comment")]
public IActionResult SubmitComment(string userName, string message)
{
    var comment = new Comment
    {
        UserName = userName,
        Message = message,
        CreatedAt = DateTime.UtcNow
    };

    _dbContext.Comments.Add(comment);
    _dbContext.SaveChanges();

    return Ok();
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```python
@app.route("/submit-comment", methods=["POST"])
def submit_comment():
    data = request.get_json()
    comment = Comment(
        user_name=data["userName"],
        message=data["message"],
        created_at=datetime.utcnow()
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify({"status": "ok"})
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```ts
app.post("/submit-comment", async (req, res) => {
    const { userName, message } = req.body;

    await db.comment.create({
        data: {
            userName,
            message,
            createdAt: new Date(),
        },
    });

    res.json({ status: "ok" });
});
```

---

### 🧪 Senaryo 4: Bir forum sitesinde kullanıcılar konulara cevaplar yazabiliyor. Cevaplar her kullanıcının profil bilgileriyle birlikte listeleniyor. Gönderilen içerik HTML template'e yerleştirilerek gösteriliyor. Editör veya işaretleme dili kullanılmadan sade metin desteği sağlanıyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 13
```csharp
[HttpPost("submit-comment")]
public IActionResult SubmitComment(string userName, string message)
{
    var comment = new Comment
    {
        UserName = userName,
        Message = message,
        CreatedAt = DateTime.UtcNow
    };

    _dbContext.Comments.Add(comment);
    _dbContext.SaveChanges();

    return Ok();
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```python
@app.route("/submit-comment", methods=["POST"])
def submit_comment():
    data = request.get_json()
    comment = Comment(
        user_name=data["userName"],
        message=data["message"],
        created_at=datetime.utcnow()
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify({"status": "ok"})
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```ts
app.post("/submit-comment", async (req, res) => {
    const { userName, message } = req.body;

    await db.comment.create({
        data: {
            userName,
            message,
            createdAt: new Date(),
        },
    });

    res.json({ status: "ok" });
});
```

---

### 🧪 Senaryo 5: Bir otel rezervasyon sitesinde müşteriler konakladıkları oteller hakkında görüşlerini paylaşabiliyor. Otel sayfasında tüm yorumlar toplu şekilde listeleniyor. Yorum içeriği kullanıcıdan alındığı şekliyle HTML içerisinde gösteriliyor. Aynı içerik yönetici panelinde de görüntülenebiliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 13
```csharp
[HttpPost("submit-comment")]
public IActionResult SubmitComment(string userName, string message)
{
    var comment = new Comment
    {
        UserName = userName,
        Message = message,
        CreatedAt = DateTime.UtcNow
    };

    _dbContext.Comments.Add(comment);
    _dbContext.SaveChanges();

    return Ok();
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```python
@app.route("/submit-comment", methods=["POST"])
def submit_comment():
    data = request.get_json()
    comment = Comment(
        user_name=data["userName"],
        message=data["message"],
        created_at=datetime.utcnow()
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify({"status": "ok"})
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```ts
app.post("/submit-comment", async (req, res) => {
    const { userName, message } = req.body;

    await db.comment.create({
        data: {
            userName,
            message,
            createdAt: new Date(),
        },
    });

    res.json({ status: "ok" });
});
```

---

### 🧪 Senaryo 6: Bir alışveriş sitesinde kullanıcılar ürünlere puan ve açıklama yazabiliyor. Bu açıklamalar ürün sayfasında ve ana sayfadaki öne çıkan yorumlar bölümünde gösteriliyor. Yorumlar HTML template'e veri olarak aktarılıyor. Kullanıcı girişi üzerinde biçimlendirme işlemi yapılmıyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 13
```csharp
[HttpPost("submit-comment")]
public IActionResult SubmitComment(string userName, string message)
{
    var comment = new Comment
    {
        UserName = userName,
        Message = message,
        CreatedAt = DateTime.UtcNow
    };

    _dbContext.Comments.Add(comment);
    _dbContext.SaveChanges();

    return Ok();
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```python
@app.route("/submit-comment", methods=["POST"])
def submit_comment():
    data = request.get_json()
    comment = Comment(
        user_name=data["userName"],
        message=data["message"],
        created_at=datetime.utcnow()
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify({"status": "ok"})
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```ts
app.post("/submit-comment", async (req, res) => {
    const { userName, message } = req.body;

    await db.comment.create({
        data: {
            userName,
            message,
            createdAt: new Date(),
        },
    });

    res.json({ status: "ok" });
});
```

---

### 🧪 Senaryo 7: Bir haber uygulamasında okuyucular haberlere tepki bırakabiliyor ve açıklama yazabiliyor. Açıklamalar yorum başlığı, ad ve mesaj içeriyor. Tüm bilgiler formdan alınıp haberin altına ekleniyor. Editoryal onay süreci olmayan sistemde kullanıcılar anında içerik yayınlayabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 13
```csharp
[HttpPost("submit-comment")]
public IActionResult SubmitComment(string userName, string message)
{
    var comment = new Comment
    {
        UserName = userName,
        Message = message,
        CreatedAt = DateTime.UtcNow
    };

    _dbContext.Comments.Add(comment);
    _dbContext.SaveChanges();

    return Ok();
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```python
@app.route("/submit-comment", methods=["POST"])
def submit_comment():
    data = request.get_json()
    comment = Comment(
        user_name=data["userName"],
        message=data["message"],
        created_at=datetime.utcnow()
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify({"status": "ok"})
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```ts
app.post("/submit-comment", async (req, res) => {
    const { userName, message } = req.body;

    await db.comment.create({
        data: {
            userName,
            message,
            createdAt: new Date(),
        },
    });

    res.json({ status: "ok" });
});
```

---

### 🧪 Senaryo 8: Bir etkinlik planlama sitesinde katılımcılar etkinlik sonrası değerlendirme formu doldurabiliyor. Kullanıcının yazdığı açıklama etkinlik detay sayfasında görüntüleniyor. Değerlendirme alanı geniş metin kutusu olarak tasarlanmış ve serbest şekilde doldurulabiliyor. Yorumun tamamı HTML içinde gösteriliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 13
```csharp
[HttpPost("submit-comment")]
public IActionResult SubmitComment(string userName, string message)
{
    var comment = new Comment
    {
        UserName = userName,
        Message = message,
        CreatedAt = DateTime.UtcNow
    };

    _dbContext.Comments.Add(comment);
    _dbContext.SaveChanges();

    return Ok();
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```python
@app.route("/submit-comment", methods=["POST"])
def submit_comment():
    data = request.get_json()
    comment = Comment(
        user_name=data["userName"],
        message=data["message"],
        created_at=datetime.utcnow()
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify({"status": "ok"})
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```ts
app.post("/submit-comment", async (req, res) => {
    const { userName, message } = req.body;

    await db.comment.create({
        data: {
            userName,
            message,
            createdAt: new Date(),
        },
    });

    res.json({ status: "ok" });
});
```

---

### 🧪 Senaryo 9: Bir çevrimiçi eğitim sisteminde öğrenciler sınav sonrasında yorum paylaşabiliyor. Yorumlar hem eğitmenin panelinde hem de sınıf arkadaşlarının ekranında listeleniyor. Yorumun metni HTML'e gömülüyor. Ek işleme veya filtreleme uygulanmıyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 13
```csharp
[HttpPost("submit-comment")]
public IActionResult SubmitComment(string userName, string message)
{
    var comment = new Comment
    {
        UserName = userName,
        Message = message,
        CreatedAt = DateTime.UtcNow
    };

    _dbContext.Comments.Add(comment);
    _dbContext.SaveChanges();

    return Ok();
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```python
@app.route("/submit-comment", methods=["POST"])
def submit_comment():
    data = request.get_json()
    comment = Comment(
        user_name=data["userName"],
        message=data["message"],
        created_at=datetime.utcnow()
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify({"status": "ok"})
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```ts
app.post("/submit-comment", async (req, res) => {
    const { userName, message } = req.body;

    await db.comment.create({
        data: {
            userName,
            message,
            createdAt: new Date(),
        },
    });

    res.json({ status: "ok" });
});
```

---

### 🧪 Senaryo 10: Bir restoran değerlendirme platformunda kullanıcılar deneyimlerini paylaşabiliyor. Kullanıcılar restoran adını ve görüşlerini yazarak gönderiyor. Görüşler hem mobil uygulamada hem web arayüzünde HTML formatında gösteriliyor. Mesajlar kullanıcı girişiyle oluşturuluyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 13
```csharp
[HttpPost("submit-comment")]
public IActionResult SubmitComment(string userName, string message)
{
    var comment = new Comment
    {
        UserName = userName,
        Message = message,
        CreatedAt = DateTime.UtcNow
    };

    _dbContext.Comments.Add(comment);
    _dbContext.SaveChanges();

    return Ok();
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```python
@app.route("/submit-comment", methods=["POST"])
def submit_comment():
    data = request.get_json()
    comment = Comment(
        user_name=data["userName"],
        message=data["message"],
        created_at=datetime.utcnow()
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify({"status": "ok"})
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```ts
app.post("/submit-comment", async (req, res) => {
    const { userName, message } = req.body;

    await db.comment.create({
        data: {
            userName,
            message,
            createdAt: new Date(),
        },
    });

    res.json({ status: "ok" });
});
```
