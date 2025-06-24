### 🧪 Senaryo 1: Bir kullanıcı yönetim panelinde yöneticiler belirli kullanıcıların bilgilerini arayabiliyor. Arama kutusuna girilen kullanıcı adı veritabanında sorgulanarak eşleşen kayıtlar gösteriliyor. Arama işlemi karakter değişiminde güncelleniyor. Sonuçlar tablo halinde listeleniyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```csharp
[HttpGet("admin/search-user")]
public IActionResult SearchUser(string name)
{
    var users = _db.Users
        .Where(u => u.UserName.Contains(name))
        .ToList();
    return Ok(users);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 5
```python
@app.route("/admin/search-user")
def search_user():
    name = request.args.get("name")
    users = User.query.filter(User.username.contains(name)).all()
    return jsonify(users)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 7
```ts
app.get("/admin/search-user", async (req, res) => {
    const name = req.query.name as string;
    const users = await prisma.user.findMany({
        where: { username: { contains: name } },
    });
    res.json(users);
});
```

---

### 🧪 Senaryo 2: Bir e-ticaret platformunda kullanıcılar sipariş numaralarını girerek kargo durumlarını sorgulayabiliyor. Sipariş numarası giriş kutusuna yazıldıktan sonra veritabanı üzerinden arama yapılıyor. Sonuçlar kullanıcının geçmiş siparişleriyle birlikte gösteriliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```csharp
[HttpGet("orders/track")]
public IActionResult TrackOrder(string orderNo)
{
    var result = _db.Orders
        .Where(o => o.OrderNumber == orderNo)
        .ToList();
    return Ok(result);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 5
```python
@app.route("/orders/track")
def track_order():
    order_no = request.args.get("orderNo")
    orders = Order.query.filter_by(order_number=order_no).all()
    return jsonify(orders)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 7
```ts
app.get("/orders/track", async (req, res) => {
    const orderNo = req.query.orderNo as string;
    const orders = await prisma.order.findMany({
        where: { orderNumber: orderNo },
    });
    res.json(orders);
});
```

---

### 🧪 Senaryo 3: Bir üniversite portalında öğrenciler öğrenci numaralarını girerek notlarını görebiliyor. Notlar öğrenciye özel olarak filtrelenip veritabanından çekiliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```csharp
[HttpGet("grades")]
public IActionResult GetGrades(string studentNo)
{
    var grades = _db.Grades
        .Where(g => g.StudentNo == studentNo)
        .ToList();
    return Ok(grades);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 5
```python
@app.route("/grades")
def get_grades():
    student_no = request.args.get("studentNo")
    grades = Grade.query.filter_by(student_no=student_no).all()
    return jsonify(grades)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 7
```ts
app.get("/grades", async (req, res) => {
    const studentNo = req.query.studentNo as string;
    const grades = await prisma.grade.findMany({
        where: { studentNo },
    });
    res.json(grades);
});
```

---

### 🧪 Senaryo 4: Bir destek sistemi uygulamasında kullanıcılar açtıkları destek taleplerini takip edebiliyor. Destek talep numarası girilerek geçmiş kayıtlara ulaşılabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 7
```csharp
[HttpGet("support/ticket")]
public IActionResult GetTicket(string ticketId)
{
    var ticket = _db.SupportTickets
        .FirstOrDefault(t => t.TicketId == ticketId);
    return Ok(ticket);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 5
```python
@app.route("/support/ticket")
def get_ticket():
    ticket_id = request.args.get("ticketId")
    ticket = SupportTicket.query.filter_by(ticket_id=ticket_id).first()
    return jsonify(ticket)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 7
```ts
app.get("/support/ticket", async (req, res) => {
    const ticketId = req.query.ticketId as string;
    const ticket = await prisma.supportTicket.findUnique({
        where: { ticketId },
    });
    res.json(ticket);
});
```

---

### 🧪 Senaryo 5: Bir kütüphane uygulamasında kullanıcılar kitap adıyla arama yapabiliyor. Sistem girilen değeri kullanarak kitap başlığına göre veri filtreliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```csharp
[HttpGet("library/search")]
public IActionResult SearchBooks(string title)
{
    var books = _db.Books
        .Where(b => b.Title.Contains(title))
        .ToList();
    return Ok(books);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 5
```python
@app.route("/library/search")
def search_books():
    title = request.args.get("title")
    books = Book.query.filter(Book.title.contains(title)).all()
    return jsonify(books)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 7
```ts
app.get("/library/search", async (req, res) => {
    const title = req.query.title as string;
    const books = await prisma.book.findMany({
        where: { title: { contains: title } },
    });
    res.json(books);
});
```

---

### 🧪 Senaryo 6: Bir ürün kataloğunda kullanıcılar ürün kimliği (ID) ile arama yaparak ürün detaylarını görebiliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 7
```csharp
[HttpGet("products/{id}")]
public IActionResult GetProduct(int id)
{
    var product = _db.Products
        .FirstOrDefault(p => p.ProductId == id);
    return Ok(product);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 4
```python
@app.route("/products/<int:id>")
def get_product(id):
    product = Product.query.get(id)
    return jsonify(product)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 7
```ts
app.get("/products/:id", async (req, res) => {
    const id = parseInt(req.params.id);
    const product = await prisma.product.findUnique({
        where: { id },
    });
    res.json(product);
});
```

---

### 🧪 Senaryo 7: Bir forumda kullanıcılar belirli bir başlık altındaki mesajları görüntüleyebiliyor. Başlık kimliği (ID) kullanılarak ilgili mesajlar veritabanından çekiliyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```csharp
[HttpGet("forum/topics/{topicId}")]
public IActionResult GetMessages(int topicId)
{
    var messages = _db.ForumMessages
        .Where(m => m.TopicId == topicId)
        .ToList();
    return Ok(messages);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 4
```python
@app.route("/forum/topics/<int:topic_id>")
def get_messages(topic_id):
    messages = ForumMessage.query.filter_by(topic_id=topic_id).all()
    return jsonify(messages)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 7
```ts
app.get("/forum/topics/:topicId", async (req, res) => {
    const topicId = parseInt(req.params.topicId);
    const messages = await prisma.forumMessage.findMany({
        where: { topicId },
    });
    res.json(messages);
});
```

---

### 🧪 Senaryo 8: Bir blog platformunda yazarlar kendi yazdıkları yazıları düzenleyebiliyor. Yazar kimliği ve yazı kimliği kullanılarak yetki kontrolü yapılıyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 9
```csharp
[HttpPut("posts/{postId}")]
public IActionResult UpdatePost(int postId, [FromBody] PostUpdateDto data, int authorId)
{
    var post = _db.Posts
        .FirstOrDefault(p => p.PostId == postId && p.AuthorId == authorId);
    if (post == null) return NotFound();
    // Update logic...
    return Ok(post);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```python
@app.route("/posts/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    author_id = request.json.get("author_id")
    post = Post.query.filter_by(id=post_id, author_id=author_id).first()
    if not post:
        return jsonify(error="Not found"), 404
    # Update logic...
    return jsonify(post)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 10
```ts
app.put("/posts/:postId", async (req, res) => {
    const postId = parseInt(req.params.postId);
    const { authorId, ...data } = req.body;
    const post = await prisma.post.findFirst({
        where: { id: postId, authorId: authorId },
    });
    if (!post) return res.status(404).json({ error: "Not found" });
    // Update logic...
    res.json(post);
});
```

---

### 🧪 Senaryo 9: Bir finans uygulamasında kullanıcılar sadece kendi hesap hareketlerini görebiliyor. Kullanıcı kimliği ile hesap kimliği eşleştirilerek sorgulama yapılıyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 9
```csharp
[HttpGet("accounts/{accountId}/transactions")]
public IActionResult GetTransactions(int accountId, int userId)
{
    var account = _db.Accounts
        .FirstOrDefault(a => a.AccountId == accountId && a.UserId == userId);
    if (account == null) return Forbid();
    // Get transactions...
    return Ok(account.Transactions);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 7
```python
@app.route("/accounts/<int:account_id>/transactions")
def get_transactions(account_id):
    user_id = request.args.get("user_id")
    account = Account.query.filter_by(id=account_id, user_id=user_id).first()
    if not account:
        return jsonify(error="Forbidden"), 403
    return jsonify(account.transactions)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 10
```ts
app.get("/accounts/:accountId/transactions", async (req, res) => {
    const accountId = parseInt(req.params.accountId);
    const userId = parseInt(req.query.userId as string);
    const account = await prisma.account.findFirst({
        where: { id: accountId, userId: userId },
    });
    if (!account) return res.status(403).json({ error: "Forbidden" });
    // Get transactions...
    res.json(account.transactions);
});
```

---

### 🧪 Senaryo 10: Bir dosya paylaşım platformunda kullanıcılar sadece kendi yükledikleri dosyaları silebiliyor. Dosya sahibi kimliği ile işlem yapan kullanıcı kimliği karşılaştırılıyor.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 9
```csharp
[HttpDelete("files/{fileId}")]
public IActionResult DeleteFile(int fileId, int userId)
{
    var file = _db.Files
        .FirstOrDefault(f => f.FileId == fileId && f.OwnerId == userId);
    if (file == null) return Forbid();
    // Delete logic...
    return Ok("File deleted");
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```python
@app.route("/files/<int:file_id>", methods=["DELETE"])
def delete_file(file_id):
    user_id = request.json.get("user_id")
    file = File.query.filter_by(id=file_id, owner_id=user_id).first()
    if not file:
        return jsonify(error="Forbidden"), 403
    # Delete logic...
    return jsonify(status="File deleted")
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 10
```ts
app.delete("/files/:fileId", async (req, res) => {
    const fileId = parseInt(req.params.fileId);
    const { userId } = req.body;
    const file = await prisma.file.findFirst({
        where: { id: fileId, ownerId: userId },
    });
    if (!file) return res.status(403).json({ error: "Forbidden" });
    // Delete logic...
    res.json({ status: "File deleted" });
});
```