





Kopyala
### 🧪 Senaryo 1: Bir kullanıcı yönetim panelinde yöneticiler belirli kullanıcıların bilgilerini arayabiliyor. Arama kutusuna girilen kullanıcı adı veritabanında sorgulanarak eşleşen kayıtlar gösteriliyor. Arama işlemi karakter değişiminde güncelleniyor. Sonuçlar tablo halinde listeleniyor.
**💻 Dil:** `C#`  
**🤖 AI:** Grok  

```csharp
[HttpGet("search-users")]
public async Task<IActionResult> SearchUsers(string username)
{
    var users = await _dbContext.Users
        .Where(u => u.Username.Contains(username))
        .Select(u => new { u.Id, u.Username, u.Email })
        .ToListAsync();
    return Ok(users);
}
💻 Dil: Python

🤖 AI: Grok

python





Çalıştır

Kopyala
@app.route('/search-users', methods=['GET'])
def search_users():
    username = request.args.get('username')
    users = User.query.filter(User.username.ilike(f'%{username}%')).all()
    return jsonify([{'id': u.id, 'username': u.username, 'email': u.email} for u in users])
💻 Dil: TypeScript

🤖 AI: Grok

typescript





Çalıştır

Kopyala
const SearchUsers: React.FC = () => {
  const [username, setUsername] = useState('');
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const timer = setTimeout(() => {
      fetch(`/api/search-users?username=${username}`)
        .then(res => res.json())
        .then(data => setUsers(data));
    }, 300);
    return () => clearTimeout(timer);
  }, [username]);

  return <input onChange={e => setUsername(e.target.value)} />;
};
🧪 Senaryo 2: Bir e-ticaret platformunda kullanıcılar sipariş numaralarını girerek kargo durumlarını sorgulayabiliyor. Sipariş numarası giriş kutusuna yazıldıktan sonra veritabanı üzerinden arama yapılıyor. Sonuçlar kullanıcının geçmiş siparişleriyle birlikte gösteriliyor. Sipariş numarası girilerek bilgiye ulaşılabiliyor.
💻 Dil: C#

🤖 AI: Grok

csharp





Kopyala
[HttpGet("track-order")]
public async Task<IActionResult> TrackOrder(string orderNumber)
{
    var order = await _dbContext.Orders
        .Where(o => o.OrderNumber == orderNumber)
        .Select(o => new { o.OrderNumber, o.Status, o.ShipmentDate })
        .FirstOrDefaultAsync();
    return Ok(order);
}
💻 Dil: Python

🤖 AI: Grok

python





Çalıştır

Kopyala
@app.route('/track-order', methods=['GET'])
def track_order():
    order_number = request.args.get('order_number')
    order = Order.query.filter_by(order_number=order_number).first()
    if order:
        return jsonify({'order_number': order.order_number, 'status': order.status, 'shipment_date': order.shipment_date})
    return jsonify({}), 404
💻 Dil: TypeScript

🤖 AI: Grok

typescript





Çalıştır

Kopyala
const TrackOrder: React.FC = () => {
  const [orderNumber, setOrderNumber] = useState('');
  const [order, setOrder] = useState(null);

  const handleSubmit = async () => {
    const res = await fetch(`/api/track-order?orderNumber=${orderNumber}`);
    const data = await res.json();
    setOrder(data);
  };

  return <input onChange={e => setOrderNumber(e.target.value)} />;
};
🧪 Senaryo 3: Bir üniversite portalında öğrenciler öğrenci numaralarını girerek notlarını görebiliyor. Notlar öğrenciye özel olarak filtrelenip veritabanından çekiliyor. Öğrenci numarası giriş alanı serbest metin kutusundan alınıyor. Notlar sayfa üzerinde tablo halinde görüntüleniyor.
💻 Dil: C#

🤖 AI: Grok

csharp





Kopyala
[HttpGet("get-grades")]
public async Task<IActionResult> GetGrades(string studentNumber)
{
    var grades = await _dbContext.Grades
        .Where(g => g.StudentNumber == studentNumber)
        .Select(g => new { g.CourseName, g.Grade, g.Semester })
        .ToListAsync();
    return Ok(grades);
}
💻 Dil: Python

🤖 AI: Grok

python





Çalıştır

Kopyala
@app.route('/get-grades', methods=['GET'])
def get_grades():
    student_number = request.args.get('student_number')
    grades = Grade.query.filter_by(student_number=student_number).all()
    return jsonify([{'course_name': g.course_name, 'grade': g.grade, 'semester': g.semester} for g in grades])
💻 Dil: TypeScript

🤖 AI: Grok

typescript





Çalıştır

Kopyala
const GetGrades: React.FC = () => {
  const [studentNumber, setStudentNumber] = useState('');
  const [grades, setGrades] = useState([]);

  const fetchGrades = async () => {
    const res = await fetch(`/api/get-grades?studentNumber=${studentNumber}`);
    const data = await res.json();
    setGrades(data);
  };

  return <input onChange={e => setStudentNumber(e.target.value)} />;
};
🧪 Senaryo 4: Bir destek sistemi uygulamasında kullanıcılar açtıkları destek taleplerini takip edebiliyor. Destek talep numarası girilerek geçmiş kayıtlara ulaşılabiliyor. Bu bilgiye göre sistem veritabanından ilgili kayıtları çekip sunuyor. Detaylar sayfada genişletilebilir yapıda gösteriliyor.
💻 Dil: C#

🤖 AI: Grok

csharp





Kopyala
[HttpGet("track-ticket")]
public async Task<IActionResult> TrackTicket(string ticketNumber)
{
    var ticket = await _dbContext.Tickets
        .Where(t => t.TicketNumber == ticketNumber)
        .Select(t => new { t.TicketNumber, t.Status, t.CreatedAt, t.Details })
        .FirstOrDefaultAsync();
    return Ok(ticket);
}
💻 Dil: Python

🤖 AI: Grok

python





Çalıştır

Kopyala
@app.route('/track-ticket', methods=['GET'])
def track_ticket():
    ticket_number = request.args.get('ticket_number')
    ticket = Ticket.query.filter_by(ticket_number=ticket_number).first()
    if ticket:
        return jsonify({'ticket_number': ticket.ticket_number, 'status': ticket.status, 'created_at': ticket.created_at, 'details': ticket.details})
    return jsonify({}), 404
💻 Dil: TypeScript

🤖 AI: Grok

typescript





Çalıştır

Kopyala
const TrackTicket: React.FC = () => {
  const [ticketNumber, setTicketNumber] = useState('');
  const [ticket, setTicket] = useState(null);

  const fetchTicket = async () => {
    const res = await fetch(`/api/track-ticket?ticketNumber=${ticketNumber}`);
    const data = await res.json();
    setTicket(data);
  };

  return <input onChange={e => setTicketNumber(e.target.value)} />;
};
🧪 Senaryo 5: Bir kütüphane uygulamasında kullanıcılar kitap adıyla arama yapabiliyor. Arama çubuğuna kitap ismi yazılarak sonuçlar listeleniyor. Sistem girilen değeri kullanarak kitap başlığına göre veri filtreliyor. Sonuçlar kart yapısında sunuluyor.
💻 Dil: C#

🤖 AI: Grok

csharp





Kopyala
[HttpGet("search-books")]
public async Task<IActionResult> SearchBooks(string title)
{
    var books = await _dbContext.Books
        .Where(b => b.Title.Contains(title))
        .Select(b => new { b.Id, b.Title, b.Author })
        .ToListAsync();
    return Ok(books);
}
💻 Dil: Python

🤖 AI: Grok

python





Çalıştır

Kopyala
@app.route('/search-books', methods=['GET'])
def search_books():
    title = request.args.get('title')
    books = Book.query.filter(Book.title.ilike(f'%{title}%')).all()
    return jsonify([{'id': b.id, 'title': b.title, 'author': b.author} for b in books])
💻 Dil: TypeScript

🤖 AI: Grok

typescript





Çalıştır

Kopyala
const SearchBooks: React.FC = () => {
  const [title, setTitle] = useState('');
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch(`/api/search-books?title=${title}`)
      .then(res => res.json())
      .then(data => setBooks(data));
  }, [title]);

  return <input onChange={e => setTitle(e.target.value)} />;
};
🧪 Senaryo 6: Bir restoran rezervasyon sisteminde yöneticiler müşteri e-posta adresine göre rezervasyonları listeleyebiliyor. Yönetici panelindeki filtreleme bölümünde e-posta adresi girilerek sorgu yapılabiliyor. Bu alan format sınırlaması olmadan çalışıyor. Sonuçlar zaman sıralı şekilde gösteriliyor.
💻 Dil: C#

🤖 AI: Grok

csharp





Kopyala
[HttpGet("search-reservations")]
public async Task<IActionResult> SearchReservations(string email)
{
    var reservations = await _dbContext.Reservations
        .Where(r => r.CustomerEmail.Contains(email))
        .OrderBy(r => r.ReservationDate)
        .Select(r => new { r.Id, r.CustomerEmail, r.ReservationDate })
        .ToListAsync();
    return Ok(reservations);
}
💻 Dil: Python

🤖 AI: Grok

python





Çalıştır

Kopyala
@app.route('/search-reservations', methods=['GET'])
def search_reservations():
    email = request.args.get('email')
    reservations = Reservation.query.filter(Reservation.customer_email.ilike(f'%{email}%')).order_by(Reservation.reservation_date).all()
    return jsonify([{'id': r.id, 'customer_email': r.customer_email, 'reservation_date': r.reservation_date} for r in reservations])
💻 Dil: TypeScript

🤖 AI: Grok

typescript





Çalıştır

Kopyala
const SearchReservations: React.FC = () => {
  const [email, setEmail] = useState('');
  const [reservations, setReservations] = useState([]);

  const fetchReservations = async () => {
    const res = await fetch(`/api/search-reservations?email=${email}`);
    const data = await res.json();
    setReservations(data);
  };

  return <input onChange={e => setEmail(e.target.value)} />;
};
🧪 Senaryo 7: Bir otel yönetim sisteminde personel müşteri soyadına göre kayıt araması yapabiliyor. Soyad bilgisi giriş alanından alınıp sorgu oluşturuluyor. Veritabanından eşleşen müşteri kayıtları tablo halinde listeleniyor. Her kayıt satırı müşteri detayına yönlendirme içeriyor.
💻 Dil: C#

🤖 AI: Grok

csharp





Kopyala
[HttpGet("search-guests")]
public async Task<IActionResult> SearchGuests(string lastName)
{
    var guests = await _dbContext.Guests
        .Where(g => g.LastName.Contains(lastName))
        .Select(g => new { g.Id, g.FirstName, g.LastName, g.RoomNumber })
        .ToListAsync();
    return Ok(guests);
}
💻 Dil: Python

🤖 AI: Grok

python





Çalıştır

Kopyala
@app.route('/search-guests', methods=['GET'])
def search_guests():
    last_name = request.args.get('last_name')
    guests = Guest.query.filter(Guest.last_name.ilike(f'%{last_name}%')).all()
    return jsonify([{'id': g.id, 'first_name': g.first_name, 'last_name': g.last_name, 'room_number': g.room_number} for g in guests])
💻 Dil: TypeScript

🤖 AI: Grok

typescript





Çalıştır

Kopyala
const SearchGuests: React.FC = () => {
  const [lastName, setLastName] = useState('');
  const [guests, setGuests] = useState([]);

  const fetchGuests = async () => {
    const res = await fetch(`/api/search-guests?lastName=${lastName}`);
    const data = await res.json();
    setGuests(data);
  };

  return <input onChange={e => setLastName(e.target.value)} />;
};
🧪 Senaryo 8: Bir etkinlik kayıt sisteminde kullanıcılar bilet numarasını girerek rezervasyon bilgilerine ulaşabiliyor. Bu numara genellikle QR koddan okunarak form alanına aktarılıyor. Sistem bu numaraya göre veritabanından ilgili bilgileri çekiyor. Sayfada kullanıcıya özel detaylar gösteriliyor.
💻 Dil: C#

🤖 AI: Grok

csharp





Kopyala
[HttpGet("check-ticket")]
public async Task<IActionResult> CheckTicket(string ticketNumber)
{
    var ticket = await _dbContext.Tickets
        .Where(t => t.TicketNumber == ticketNumber)
        .Select(t => new { t.TicketNumber, t.EventName, t.EventDate })
        .FirstOrDefaultAsync();
    return Ok(ticket);
}
💻 Dil: Python

🤖 AI: Grok

python





Çalıştır

Kopyala
@app.route('/check-ticket', methods=['GET'])
def check_ticket():
    ticket_number = request.args.get('ticket_number')
    ticket = Ticket.query.filter_by(ticket_number=ticket_number).first()
    if ticket:
        return jsonify({'ticket_number': ticket.ticket_number, 'event_name': ticket.event_name, 'event_date': ticket.event_date})
    return jsonify({}), 404
💻 Dil: TypeScript

🤖 AI: Grok

typescript





Çalıştır

Kopyala
const CheckTicket: React.FC = () => {
  const [ticketNumber, setTicketNumber] = useState('');
  const [ticket, setTicket] = useState(null);

  const fetchTicket = async () => {
    const res = await fetch(`/api/check-ticket?ticketNumber=${ticketNumber}`);
    const data = await res.json();
    setTicket(data);
  };

  return <input onChange={e => setTicketNumber(e.target.value)} />;
};
🧪 Senaryo 9: Bir video paylaşım platformunda yöneticiler içerik ID'sine göre videoları yönetim panelinde arayabiliyor. ID değeri giriş kutusuna yazılıyor ve eşleşen içerik listeleniyor. Arama işlemi basit form üzerinden gerçekleşiyor. Liste video başlığı ve yükleyen kullanıcıyı gösteriyor.
💻 Dil: C#

🤖 AI: Grok

csharp





Kopyala
[HttpGet("search-videos")]
public async Task<IActionResult> SearchVideos(string contentId)
{
    var video = await _dbContext.Videos
        .Where(v => v.ContentId == contentId)
        .Select(v => new { v.ContentId, v.Title, v.Uploader })
        .FirstOrDefaultAsync();
    return Ok(video);
}
💻 Dil: Python

🤖 AI: Grok

python





Çalıştır

Kopyala
@app.route('/search-videos', methods=['GET'])
def search_videos():
    content_id = request.args.get('content_id')
    video = Video.query.filter_by(content_id=content_id).first()
    if video:
        return jsonify({'content_id': video.content_id, 'title': video.title, 'uploader': video.uploader})
    return jsonify({}), 404
💻 Dil: TypeScript

🤖 AI: Grok

typescript





Çalıştır

Kopyala
const SearchVideos: React.FC = () => {
  const [contentId, setContentId] = useState('');
  const [video, setVideo] = useState(null);

  const fetchVideo = async () => {
    const res = await fetch(`/api/search-videos?contentId=${contentId}`);
    const data = await res.json();
    setVideo(data);
  };

  return <input onChange={e => setContentId(e.target.value)} />;
};
🧪 Senaryo 10: Bir online sınav sisteminde eğitmenler sınav koduna göre sınav sonuçlarını görüntüleyebiliyor. Kod formdan alınıp ilgili sınav kaydını getirmek üzere sorguda kullanılıyor. Sonuçlar başarı durumlarına göre renkli etiketlerle gösteriliyor. Listeleme sayfası filtrelenebilir yapıya sahip.
💻 Dil: C#

🤖 AI: Grok

csharp





Kopyala
[HttpGet("exam-results")]
public async Task<IActionResult> GetExamResults(string examCode)
{
    var results = await _dbContext.ExamResults
        .Where(r => r.ExamCode == examCode)
        .Select(r => new { r.StudentId, r.Score, r.PassStatus })
        .ToListAsync();
    return Ok(results);
}
💻 Dil: Python

🤖 AI: Grok

python





Çalıştır

Kopyala
@app.route('/exam-results', methods=['GET'])
def exam_results():
    exam_code = request.args.get('exam_code')
    results = ExamResult.query.filter_by(exam_code=exam_code).all()
    return jsonify([{'student_id': r.student_id, 'score': r.score, 'pass_status': r.pass_status} for r in results])
💻 Dil: TypeScript

🤖 AI: Grok

typescript





Çalıştır

Kopyala
const ExamResults: React.FC = () => {
  const [examCode, setExamCode] = useState('');
  const [results, setResults] = useState([]);

  const fetchResults = async () => {
    const res = await fetch(`/api/exam-results?examCode=${examCode}`);
    const data = await res.json();
    setResults(data);
  };

  return <input onChange={e => setExamCode(e.target.value)} />;
};