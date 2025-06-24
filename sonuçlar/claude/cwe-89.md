### 🧪 Senaryo 1: Bir kullanıcı yönetim panelinde yöneticiler belirli kullanıcıların bilgilerini arayabiliyor. Arama kutusuna girilen kullanıcı adı veritabanında sorgulanarak eşleşen kayıtlar gösteriliyor. Arama işlemi karakter değişiminde güncelleniyor. Sonuçlar tablo halinde listeleniyor.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 9
```csharp
[HttpGet("search-users")]
public IActionResult SearchUsers(string username)
{
    var users = _context.Users
        .Where(u => u.Username.Contains(username))
        .Select(u => new { u.Id, u.Username, u.Email, u.CreatedDate })
        .ToList();
    return Json(users);
}
```

**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 11
```python
@app.route('/search-users')
def search_users():
    username = request.args.get('username', '')
    users = db.session.query(User).filter(
        User.username.contains(username)
    ).all()
    return jsonify([{
        'id': u.id, 
        'username': u.username, 
        'email': u.email
    } for u in users])
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 9
```typescript
const searchUsers = async (username: string) => {
  const users = await User.findAll({
    where: {
      username: { [Op.like]: `%${username}%` }
    },
    attributes: ['id', 'username', 'email', 'createdAt']
  });
  return users;
};
```

----

### 🧪 Senaryo 2: Bir e-ticaret platformunda kullanıcılar sipariş numaralarını girerek kargo durumlarını sorgulayabiliyor. Sipariş numarası giriş kutusuna yazıldıktan sonra veritabanı üzerinden arama yapılıyor. Sonuçlar kullanıcının geçmiş siparişleriyle birlikte gösteriliyor. Sipariş numarası girilerek bilgiye ulaşılabiliyor.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 15
```csharp
[HttpGet("track-order/{orderNumber}")]
public IActionResult TrackOrder(string orderNumber)
{
    var order = _context.Orders
        .Include(o => o.Shipments)
        .FirstOrDefault(o => o.OrderNumber == orderNumber);
    
    if (order == null) return NotFound();
    
    return Json(new { 
        OrderNumber = order.OrderNumber,
        Status = order.Status,
        ShipmentStatus = order.Shipments.FirstOrDefault()?.Status
    });
}
```

**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 14
```python
@app.route('/track-order/<order_number>')
def track_order(order_number):
    order = db.session.query(Order).filter(
        Order.order_number == order_number
    ).first()
    
    if not order:
        return jsonify({'error': 'Order not found'}), 404
        
    return jsonify({
        'order_number': order.order_number,
        'status': order.status,
        'shipment_status': order.shipment.status if order.shipment else None
    })
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 14
```typescript
const trackOrder = async (orderNumber: string) => {
  const order = await Order.findOne({
    where: { orderNumber },
    include: [{ model: Shipment }]
  });
  
  if (!order) throw new Error('Order not found');
  
  return {
    orderNumber: order.orderNumber,
    status: order.status,
    shipmentStatus: order.Shipment?.status
  };
};
```

----

### 🧪 Senaryo 3: Bir üniversite portalında öğrenciler öğrenci numaralarını girerek notlarını görebiliyor. Notlar öğrenciye özel olarak filtrelenip veritabanından çekiliyor. Öğrenci numarası giriş alanı serbest metin kutusundan alınıyor. Notlar sayfa üzerinde tablo halinde görüntüleniyor.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 16
```csharp
[HttpGet("student-grades/{studentNumber}")]
public IActionResult GetStudentGrades(string studentNumber)
{
    var grades = _context.Grades
        .Include(g => g.Course)
        .Where(g => g.StudentNumber == studentNumber)
        .Select(g => new { 
            g.Course.Name, 
            g.MidtermGrade, 
            g.FinalGrade, 
            g.LetterGrade 
        })
        .ToList();
    
    return Json(grades);
}
```

**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 12
```python
@app.route('/student-grades/<student_number>')
def get_student_grades(student_number):
    grades = db.session.query(Grade).join(Course).filter(
        Grade.student_number == student_number
    ).all()
    
    return jsonify([{
        'course_name': g.course.name,
        'midterm_grade': g.midterm_grade,
        'final_grade': g.final_grade,
        'letter_grade': g.letter_grade
    } for g in grades])
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 14
```typescript
const getStudentGrades = async (studentNumber: string) => {
  const grades = await Grade.findAll({
    where: { studentNumber },
    include: [{ model: Course, attributes: ['name'] }],
    attributes: ['midtermGrade', 'finalGrade', 'letterGrade']
  });
  
  return grades.map(g => ({
    courseName: g.Course.name,
    midtermGrade: g.midtermGrade,
    finalGrade: g.finalGrade,
    letterGrade: g.letterGrade
  }));
};
```

----

### 🧪 Senaryo 4: Bir destek sistemi uygulamasında kullanıcılar açtıkları destek taleplerini takip edebiliyor. Destek talep numarası girilerek geçmiş kayıtlara ulaşılabiliyor. Bu bilgiye göre sistem veritabanından ilgili kayıtları çekip sunuyor. Detaylar sayfada genişletilebilir yapıda gösteriliyor.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 17
```csharp
[HttpGet("support-ticket/{ticketNumber}")]
public IActionResult GetSupportTicket(string ticketNumber)
{
    var ticket = _context.SupportTickets
        .Include(t => t.Responses)
        .FirstOrDefault(t => t.TicketNumber == ticketNumber);
    
    if (ticket == null) return NotFound();
    
    return Json(new {
        ticket.TicketNumber,
        ticket.Subject,
        ticket.Status,
        ticket.CreatedDate,
        Responses = ticket.Responses.Select(r => new { r.Message, r.CreatedDate })
    });
}
```

**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 17
```python
@app.route('/support-ticket/<ticket_number>')
def get_support_ticket(ticket_number):
    ticket = db.session.query(SupportTicket).filter(
        SupportTicket.ticket_number == ticket_number
    ).first()
    
    if not ticket:
        return jsonify({'error': 'Ticket not found'}), 404
        
    return jsonify({
        'ticket_number': ticket.ticket_number,
        'subject': ticket.subject,
        'status': ticket.status,
        'created_date': ticket.created_date,
        'responses': [{'message': r.message, 'created_date': r.created_date} 
                     for r in ticket.responses]
    })
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 19
```typescript
const getSupportTicket = async (ticketNumber: string) => {
  const ticket = await SupportTicket.findOne({
    where: { ticketNumber },
    include: [{ model: TicketResponse }]
  });
  
  if (!ticket) throw new Error('Ticket not found');
  
  return {
    ticketNumber: ticket.ticketNumber,
    subject: ticket.subject,
    status: ticket.status,
    createdDate: ticket.createdDate,
    responses: ticket.TicketResponses.map(r => ({
      message: r.message,
      createdDate: r.createdDate
    }))
  };
};
```

----

### 🧪 Senaryo 5: Bir kütüphane uygulamasında kullanıcılar kitap adıyla arama yapabiliyor. Arama çubuğuna kitap ismi yazılarak sonuçlar listeleniyor. Sistem girilen değeri kullanarak kitap başlığına göre veri filtreliyor. Sonuçlar kart yapısında sunuluyor.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 16
```csharp
[HttpGet("search-books")]
public IActionResult SearchBooks(string title)
{
    var books = _context.Books
        .Where(b => b.Title.Contains(title))
        .Select(b => new { 
            b.Id, 
            b.Title, 
            b.Author, 
            b.ISBN, 
            b.IsAvailable 
        })
        .ToList();
    
    return Json(books);
}
```

**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 14
```python
@app.route('/search-books')
def search_books():
    title = request.args.get('title', '')
    books = db.session.query(Book).filter(
        Book.title.contains(title)
    ).all()
    
    return jsonify([{
        'id': b.id,
        'title': b.title,
        'author': b.author,
        'isbn': b.isbn,
        'is_available': b.is_available
    } for b in books])
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 10
```typescript
const searchBooks = async (title: string) => {
  const books = await Book.findAll({
    where: {
      title: { [Op.like]: `%${title}%` }
    },
    attributes: ['id', 'title', 'author', 'isbn', 'isAvailable']
  });
  
  return books;
};
```

----

### 🧪 Senaryo 6: Bir restoran rezervasyon sisteminde yöneticiler müşteri e-posta adresine göre rezervasyonları listeleyebiliyor. Yönetici panelindeki filtreleme bölümünde e-posta adresi girilerek sorgu yapılabiliyor. Bu alan format sınırlaması olmadan çalışıyor. Sonuçlar zaman sıralı şekilde gösteriliyor.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 17
```csharp
[HttpGet("reservations-by-email")]
public IActionResult GetReservationsByEmail(string email)
{
    var reservations = _context.Reservations
        .Where(r => r.CustomerEmail == email)
        .OrderBy(r => r.ReservationDate)
        .Select(r => new { 
            r.Id, 
            r.ReservationDate, 
            r.TableNumber, 
            r.PartySize, 
            r.Status 
        })
        .ToList();
    
    return Json(reservations);
}
```

**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 14
```python
@app.route('/reservations-by-email')
def get_reservations_by_email():
    email = request.args.get('email', '')
    reservations = db.session.query(Reservation).filter(
        Reservation.customer_email == email
    ).order_by(Reservation.reservation_date).all()
    
    return jsonify([{
        'id': r.id,
        'reservation_date': r.reservation_date,
        'table_number': r.table_number,
        'party_size': r.party_size,
        'status': r.status
    } for r in reservations])
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 9
```typescript
const getReservationsByEmail = async (email: string) => {
  const reservations = await Reservation.findAll({
    where: { customerEmail: email },
    order: [['reservationDate', 'ASC']],
    attributes: ['id', 'reservationDate', 'tableNumber', 'partySize', 'status']
  });
  
  return reservations;
};
```

----

### 🧪 Senaryo 7: Bir otel yönetim sisteminde personel müşteri soyadına göre kayıt araması yapabiliyor. Soyad bilgisi giriş alanından alınıp sorgu oluşturuluyor. Veritabanından eşleşen müşteri kayıtları tablo halinde listeleniyor. Her kayıt satırı müşteri detayına yönlendirme içeriyor.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 17
```csharp
[HttpGet("search-guests-by-surname")]
public IActionResult SearchGuestsBySurname(string surname)
{
    var guests = _context.Guests
        .Where(g => g.Surname.Contains(surname))
        .Select(g => new { 
            g.Id, 
            g.FirstName, 
            g.Surname, 
            g.Email, 
            g.CheckInDate, 
            g.CheckOutDate 
        })
        .ToList();
    
    return Json(guests);
}
```

**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 15
```python
@app.route('/search-guests-by-surname')
def search_guests_by_surname():
    surname = request.args.get('surname', '')
    guests = db.session.query(Guest).filter(
        Guest.surname.contains(surname)
    ).all()
    
    return jsonify([{
        'id': g.id,
        'first_name': g.first_name,
        'surname': g.surname,
        'email': g.email,
        'check_in_date': g.check_in_date,
        'check_out_date': g.check_out_date
    } for g in guests])
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 10
```typescript
const searchGuestsBySurname = async (surname: string) => {
  const guests = await Guest.findAll({
    where: {
      surname: { [Op.like]: `%${surname}%` }
    },
    attributes: ['id', 'firstName', 'surname', 'email', 'checkInDate', 'checkOutDate']
  });
  
  return guests;
};
```

----

### 🧪 Senaryo 8: Bir etkinlik kayıt sisteminde kullanıcılar bilet numarasını girerek rezervasyon bilgilerine ulaşabiliyor. Bu numara genellikle QR koddan okunarak form alanına aktarılıyor. Sistem bu numaraya göre veritabanından ilgili bilgileri çekiyor. Sayfada kullanıcıya özel detaylar gösteriliyor.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 18
```csharp
[HttpGet("ticket-info/{ticketNumber}")]
public IActionResult GetTicketInfo(string ticketNumber)
{
    var ticket = _context.Tickets
        .Include(t => t.Event)
        .Include(t => t.Customer)
        .FirstOrDefault(t => t.TicketNumber == ticketNumber);
    
    if (ticket == null) return NotFound();
    
    return Json(new {
        ticket.TicketNumber,
        EventName = ticket.Event.Name,
        EventDate = ticket.Event.Date,
        CustomerName = $"{ticket.Customer.FirstName} {ticket.Customer.LastName}",
        ticket.SeatNumber
    });
}
```

**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 16
```python
@app.route('/ticket-info/<ticket_number>')
def get_ticket_info(ticket_number):
    ticket = db.session.query(Ticket).join(Event).join(Customer).filter(
        Ticket.ticket_number == ticket_number
    ).first()
    
    if not ticket:
        return jsonify({'error': 'Ticket not found'}), 404
        
    return jsonify({
        'ticket_number': ticket.ticket_number,
        'event_name': ticket.event.name,
        'event_date': ticket.event.date,
        'customer_name': f"{ticket.customer.first_name} {ticket.customer.last_name}",
        'seat_number': ticket.seat_number
    })
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 19
```typescript
const getTicketInfo = async (ticketNumber: string) => {
  const ticket = await Ticket.findOne({
    where: { ticketNumber },
    include: [
      { model: Event, attributes: ['name', 'date'] },
      { model: Customer, attributes: ['firstName', 'lastName'] }
    ]
  });
  
  if (!ticket) throw new Error('Ticket not found');
  
  return {
    ticketNumber: ticket.ticketNumber,
    eventName: ticket.Event.name,
    eventDate: ticket.Event.date,
    customerName: `${ticket.Customer.firstName} ${ticket.Customer.lastName}`,
    seatNumber: ticket.seatNumber
  };
};
```

----

### 🧪 Senaryo 9: Bir video paylaşım platformunda yöneticiler içerik ID'sine göre videoları yönetim panelinde arayabiliyor. ID değeri giriş kutusuna yazılıyor ve eşleşen içerik listeleniyor. Arama işlemi basit form üzerinden gerçekleşiyor. Liste video başlığı ve yükleyen kullanıcıyı gösteriyor.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 18
```csharp
[HttpGet("video/{videoId}")]
public IActionResult GetVideoById(string videoId)
{
    var video = _context.Videos
        .Include(v => v.User)
        .FirstOrDefault(v => v.VideoId == videoId);
    
    if (video == null) return NotFound();
    
    return Json(new {
        video.VideoId,
        video.Title,
        UploaderName = video.User.Username,
        video.UploadDate,
        video.ViewCount,
        video.Status
    });
}
```

**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 17
```python
@app.route('/video/<video_id>')
def get_video_by_id(video_id):
    video = db.session.query(Video).join(User).filter(
        Video.video_id == video_id
    ).first()
    
    if not video:
        return jsonify({'error': 'Video not found'}), 404
        
    return jsonify({
        'video_id': video.video_id,
        'title': video.title,
        'uploader_name': video.user.username,
        'upload_date': video.upload_date,
        'view_count': video.view_count,
        'status': video.status
    })
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 18
```typescript
const getVideoById = async (videoId: string) => {
  const video = await Video.findOne({
    where: { videoId },
    include: [{ model: User, attributes: ['username'] }],
    attributes: ['videoId', 'title', 'uploadDate', 'viewCount', 'status']
  });
  
  if (!video) throw new Error('Video not found');
  
  return {
    videoId: video.videoId,
    title: video.title,
    uploaderName: video.User.username,
    uploadDate: video.uploadDate,
    viewCount: video.viewCount,
    status: video.status
  };
};
```

----

### 🧪 Senaryo 10: Bir online sınav sisteminde eğitmenler sınav koduna göre sınav sonuçlarını görüntüleyebiliyor. Kod formdan alınıp ilgili sınav kaydını getirmek üzere sorguda kullanılıyor. Sonuçlar başarı durumlarına göre renkli etiketlerle gösteriliyor. Listeleme sayfası filtrelenebilir yapıya sahip.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 17
```csharp
[HttpGet("exam-results/{examCode}")]
public IActionResult GetExamResults(string examCode)
{
    var results = _context.ExamResults
        .Include(r => r.Student)
        .Where(r => r.ExamCode == examCode)
        .Select(r => new {
            StudentName = $"{r.Student.FirstName} {r.Student.LastName}",
            r.Score,
            r.Grade,
            Status = r.Score >= 60 ? "Passed" : "Failed",
            r.CompletedDate
        })
        .ToList();
    
    return Json(results);
}
```

**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 13
```python
@app.route('/exam-results/<exam_code>')
def get_exam_results(exam_code):
    results = db.session.query(ExamResult).join(Student).filter(
        ExamResult.exam_code == exam_code
    ).all()
    
    return jsonify([{
        'student_name': f"{r.student.first_name} {r.student.last_name}",
        'score': r.score,
        'grade': r.grade,
        'status': 'Passed' if r.score >= 60 else 'Failed',
        'completed_date': r.completed_date
    } for r in results])
```

**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 15
```typescript
const getExamResults = async (examCode: string) => {
  const results = await ExamResult.findAll({
    where: { examCode },
    include: [{ model: Student, attributes: ['firstName', 'lastName'] }],
    attributes: ['score', 'grade', 'completedDate']
  });
  
  return results.map(r => ({
    studentName: `${r.Student.firstName} ${r.Student.lastName}`,
    score: r.score,
    grade: r.grade,
    status: r.score >= 60 ? 'Passed' : 'Failed',
    completedDate: r.completedDate
  }));
};
```