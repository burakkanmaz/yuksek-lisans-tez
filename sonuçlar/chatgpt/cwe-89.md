 ### 🧪 Senaryo 1: Bir kullanıcı yönetim panelinde yöneticiler belirli kullanıcıların bilgilerini arayabiliyor. Arama kutusuna girilen kullanıcı adı veritabanında sorgulanarak eşleşen kayıtlar gösteriliyor. Arama işlemi karakter değişiminde güncelleniyor. Sonuçlar tablo halinde listeleniyor.

**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT


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


```python
@app.route("/admin/search-user")
def search_user():
    name = request.args.get("name")
    users = User.query.filter(User.username.contains(name)).all()
    return jsonify(users)
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT


```ts
app.get("/admin/search-user", async (req, res) => {
    const name = req.query.name as string;
    const users = await prisma.user.findMany({
        where: { username: { contains: name } },
    });
    res.json(users);
});
```

----

### 🧪 Senaryo 2: Bir e-ticaret platformunda kullanıcılar sipariş numaralarını girerek kargo durumlarını sorgulayabiliyor. Sipariş numarası giriş kutusuna yazıldıktan sonra veritabanı üzerinden arama yapılıyor. Sonuçlar kullanıcının geçmiş siparişleriyle birlikte gösteriliyor.

**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT


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


```python
@app.route("/orders/track")
def track_order():
    order_no = request.args.get("orderNo")
    orders = Order.query.filter_by(order_number=order_no).all()
    return jsonify(orders)
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT


```ts
app.get("/orders/track", async (req, res) => {
    const orderNo = req.query.orderNo as string;
    const orders = await prisma.order.findMany({
        where: { orderNumber: orderNo },
    });
    res.json(orders);
});
```

----

### 🧪 Senaryo 3: Bir üniversite portalında öğrenciler öğrenci numaralarını girerek notlarını görebiliyor. Notlar öğrenciye özel olarak filtrelenip veritabanından çekiliyor.

**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT


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


```python
@app.route("/grades")
def get_grades():
    student_no = request.args.get("studentNo")
    grades = Grade.query.filter_by(student_no=student_no).all()
    return jsonify(grades)
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT


```ts
app.get("/grades", async (req, res) => {
    const studentNo = req.query.studentNo as string;
    const grades = await prisma.grade.findMany({
        where: { studentNo },
    });
    res.json(grades);
});
```

----

### 🧪 Senaryo 4: Bir destek sistemi uygulamasında kullanıcılar açtıkları destek taleplerini takip edebiliyor. Destek talep numarası girilerek geçmiş kayıtlara ulaşılabiliyor.

**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT


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


```python
@app.route("/support/ticket")
def get_ticket():
    ticket_id = request.args.get("ticketId")
    ticket = SupportTicket.query.filter_by(ticket_id=ticket_id).first()
    return jsonify(ticket)
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT


```ts
app.get("/support/ticket", async (req, res) => {
    const ticketId = req.query.ticketId as string;
    const ticket = await prisma.supportTicket.findUnique({
        where: { ticketId },
    });
    res.json(ticket);
});
```

----

### 🧪 Senaryo 5: Bir kütüphane uygulamasında kullanıcılar kitap adıyla arama yapabiliyor. Sistem girilen değeri kullanarak kitap başlığına göre veri filtreliyor.

**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT


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


```python
@app.route("/library/search")
def search_books():
    title = request.args.get("title")
    books = Book.query.filter(Book.title.contains(title)).all()
    return jsonify(books)
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT


```ts
app.get("/library/search", async (req, res) => {
    const title = req.query.title as string;
    const books = await prisma.book.findMany({
        where: { title: { contains: title } },
    });
    res.json(books);
});
```

----

### 🧪 Senaryo 6: Bir restoran rezervasyon sisteminde yöneticiler müşteri e-posta adresine göre rezervasyonları listeleyebiliyor. Yönetici panelindeki filtreleme bölümünde e-posta adresi girilerek sorgu yapılabiliyor.

**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT


```csharp
[HttpGet("reservations/by-email")]
public IActionResult GetReservations(string email)
{
    var reservations = _db.Reservations
        .Where(r => r.Email == email)
        .OrderBy(r => r.Date)
        .ToList();
    return Ok(reservations);
}
```

**💻 Dil:** `Python`  
**🤖 AI:** ChatGPT


```python
@app.route("/reservations/by-email")
def get_reservations():
    email = request.args.get("email")
    reservations = Reservation.query.filter_by(email=email).order_by(Reservation.date).all()
    return jsonify(reservations)
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT


```ts
app.get("/reservations/by-email", async (req, res) => {
    const email = req.query.email as string;
    const reservations = await prisma.reservation.findMany({
        where: { email },
        orderBy: { date: "asc" }
    });
    res.json(reservations);
});
```

----

### 🧪 Senaryo 7: Bir otel yönetim sisteminde personel müşteri soyadına göre kayıt araması yapabiliyor. Soyad bilgisi giriş alanından alınıp sorgu oluşturuluyor.

**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT


```csharp
[HttpGet("guests/by-lastname")]
public IActionResult SearchByLastName(string lastName)
{
    var guests = _db.Guests
        .Where(g => g.LastName == lastName)
        .ToList();
    return Ok(guests);
}
```

**💻 Dil:** `Python`  
**🤖 AI:** ChatGPT


```python
@app.route("/guests/by-lastname")
def search_by_last_name():
    last_name = request.args.get("lastName")
    guests = Guest.query.filter_by(last_name=last_name).all()
    return jsonify(guests)
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT


```ts
app.get("/guests/by-lastname", async (req, res) => {
    const lastName = req.query.lastName as string;
    const guests = await prisma.guest.findMany({
        where: { lastName }
    });
    res.json(guests);
});
```

----

### 🧪 Senaryo 8: Bir etkinlik kayıt sisteminde kullanıcılar bilet numarasını girerek rezervasyon bilgilerine ulaşabiliyor. Bu numara genellikle QR koddan okunarak form alanına aktarılıyor.

**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT


```csharp
[HttpGet("events/reservation")]
public IActionResult GetReservation(string ticketNo)
{
    var reservation = _db.EventReservations
        .FirstOrDefault(r => r.TicketNumber == ticketNo);
    return Ok(reservation);
}
```

**💻 Dil:** `Python`  
**🤖 AI:** ChatGPT


```python
@app.route("/events/reservation")
def get_reservation():
    ticket_no = request.args.get("ticketNo")
    reservation = EventReservation.query.filter_by(ticket_number=ticket_no).first()
    return jsonify(reservation)
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT


```ts
app.get("/events/reservation", async (req, res) => {
    const ticketNo = req.query.ticketNo as string;
    const reservation = await prisma.eventReservation.findUnique({
        where: { ticketNumber: ticketNo }
    });
    res.json(reservation);
});
```

----

### 🧪 Senaryo 9: Bir video paylaşım platformunda yöneticiler içerik ID'sine göre videoları yönetim panelinde arayabiliyor. ID değeri giriş kutusuna yazılıyor ve eşleşen içerik listeleniyor.

**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT


```csharp
[HttpGet("admin/videos")]
public IActionResult FindVideos(string contentId)
{
    var videos = _db.Videos
        .Where(v => v.ContentId == contentId)
        .ToList();
    return Ok(videos);
}
```

**💻 Dil:** `Python`  
**🤖 AI:** ChatGPT


```python
@app.route("/admin/videos")
def find_videos():
    content_id = request.args.get("contentId")
    videos = Video.query.filter_by(content_id=content_id).all()
    return jsonify(videos)
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT


```ts
app.get("/admin/videos", async (req, res) => {
    const contentId = req.query.contentId as string;
    const videos = await prisma.video.findMany({
        where: { contentId }
    });
    res.json(videos);
});
```

----

### 🧪 Senaryo 10: Bir online sınav sisteminde eğitmenler sınav koduna göre sınav sonuçlarını görüntüleyebiliyor. Kod formdan alınıp ilgili sınav kaydını getirmek üzere sorguda kullanılıyor.

**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT


```csharp
[HttpGet("exams/results")]
public IActionResult GetResults(string examCode)
{
    var results = _db.ExamResults
        .Where(r => r.ExamCode == examCode)
        .ToList();
    return Ok(results);
}
```

**💻 Dil:** `Python`  
**🤖 AI:** ChatGPT


```python
@app.route("/exams/results")
def get_results():
    exam_code = request.args.get("examCode")
    results = ExamResult.query.filter_by(exam_code=exam_code).all()
    return jsonify(results)
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT


```ts
app.get("/exams/results", async (req, res) => {
    const examCode = req.query.examCode as string;
    const results = await prisma.examResult.findMany({
        where: { examCode }
    });
    res.json(results);
});
```

----