 🧪 Senaryo 1: Kullanıcı Yönetim Paneli Arama
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpGet("search-users")]
public IActionResult SearchUsers(string username)
{
    var users = _dbContext.Users
        .Where(u => u.Username.Contains(username))
        .ToList();
    return Ok(users);
}
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/search-users', methods=['GET'])
def search_users():
    username = request.args.get('username')
    users = User.query.filter(User.username.contains(username)).all()
    return jsonify([user.serialize() for user in users])
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.get('/search-users', (req, res) => {
    const username = req.query.username as string;
    const users = usersDB.filter(user => user.username.includes(username));
    res.json(users);
});
🧪 Senaryo 2: E-Ticaret Sipariş Sorgulama
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpGet("track-order")]
public IActionResult TrackOrder(string orderNumber)
{
    var order = _dbContext.Orders
        .FirstOrDefault(o => o.OrderNumber == orderNumber);
    return Ok(order);
}
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/track-order', methods=['GET'])
def track_order():
    order_number = request.args.get('orderNumber')
    order = Order.query.filter_by(order_number=order_number).first()
    return jsonify(order.serialize())
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.get('/track-order', (req, res) => {
    const orderNumber = req.query.orderNumber as string;
    const order = ordersDB.find(o => o.orderNumber === orderNumber);
    res.json(order);
});
🧪 Senaryo 3: Öğrenci Not Sorgulama
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpGet("get-grades")]
public IActionResult GetGrades(string studentId)
{
    var grades = _dbContext.Grades
        .Where(g => g.StudentId == studentId)
        .ToList();
    return Ok(grades);
}
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/get-grades', methods=['GET'])
def get_grades():
    student_id = request.args.get('studentId')
    grades = Grade.query.filter_by(student_id=student_id).all()
    return jsonify([grade.serialize() for grade in grades])
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.get('/get-grades', (req, res) => {
    const studentId = req.query.studentId as string;
    const grades = gradesDB.filter(g => g.studentId === studentId);
    res.json(grades);
});
🧪 Senaryo 4: Destek Talebi Takibi
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpGet("get-ticket")]
public IActionResult GetTicket(string ticketNumber)
{
    var ticket = _dbContext.Tickets
        .FirstOrDefault(t => t.TicketNumber == ticketNumber);
    return Ok(ticket);
}
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/get-ticket', methods=['GET'])
def get_ticket():
    ticket_number = request.args.get('ticketNumber')
    ticket = Ticket.query.filter_by(ticket_number=ticket_number).first()
    return jsonify(ticket.serialize())
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.get('/get-ticket', (req, res) => {
    const ticketNumber = req.query.ticketNumber as string;
    const ticket = ticketsDB.find(t => t.ticketNumber === ticketNumber);
    res.json(ticket);
});
🧪 Senaryo 5: Kitap Arama
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpGet("search-books")]
public IActionResult SearchBooks(string title)
{
    var books = _dbContext.Books
        .Where(b => b.Title.Contains(title))
        .ToList();
    return Ok(books);
}
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/search-books', methods=['GET'])
def search_books():
    title = request.args.get('title')
    books = Book.query.filter(Book.title.contains(title)).all()
    return jsonify([book.serialize() for book in books])
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.get('/search-books', (req, res) => {
    const title = req.query.title as string;
    const books = booksDB.filter(b => b.title.includes(title));
    res.json(books);
});
🧪 Senaryo 6: Rezervasyon Filtreleme
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpGet("filter-reservations")]
public IActionResult FilterReservations(string email)
{
    var reservations = _dbContext.Reservations
        .Where(r => r.Email == email)
        .OrderBy(r => r.Date)
        .ToList();
    return Ok(reservations);
}
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/filter-reservations', methods=['GET'])
def filter_reservations():
    email = request.args.get('email')
    reservations = Reservation.query.filter_by(email=email).order_by(Reservation.date).all()
    return jsonify([r.serialize() for r in reservations])
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.get('/filter-reservations', (req, res) => {
    const email = req.query.email as string;
    const reservations = reservationsDB
        .filter(r => r.email === email)
        .sort((a, b) => new Date(a.date).getTime() - new Date(b.date).getTime());
    res.json(reservations);
});
🧪 Senaryo 7: Müşteri Arama (Soyad)
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpGet("search-customers")]
public IActionResult SearchCustomers(string lastName)
{
    var customers = _dbContext.Customers
        .Where(c => c.LastName.Contains(lastName))
        .ToList();
    return Ok(customers);
}
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/search-customers', methods=['GET'])
def search_customers():
    last_name = request.args.get('lastName')
    customers = Customer.query.filter(Customer.last_name.contains(last_name)).all()
    return jsonify([c.serialize() for c in customers])
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.get('/search-customers', (req, res) => {
    const lastName = req.query.lastName as string;
    const customers = customersDB.filter(c => c.lastName.includes(lastName));
    res.json(customers);
});
🧪 Senaryo 8: Bilet Bilgisi Sorgulama
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpGet("get-booking")]
public IActionResult GetBooking(string ticketNumber)
{
    var booking = _dbContext.Bookings
        .FirstOrDefault(b => b.TicketNumber == ticketNumber);
    return Ok(booking);
}
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/get-booking', methods=['GET'])
def get_booking():
    ticket_number = request.args.get('ticketNumber')
    booking = Booking.query.filter_by(ticket_number=ticket_number).first()
    return jsonify(booking.serialize())
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.get('/get-booking', (req, res) => {
    const ticketNumber = req.query.ticketNumber as string;
    const booking = bookingsDB.find(b => b.ticketNumber === ticketNumber);
    res.json(booking);
});
🧪 Senaryo 9: İçerik Arama (ID)
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpGet("search-content")]
public IActionResult SearchContent(string contentId)
{
    var content = _dbContext.Contents
        .FirstOrDefault(c => c.ContentId == contentId);
    return Ok(content);
}
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/search-content', methods=['GET'])
def search_content():
    content_id = request.args.get('contentId')
    content = Content.query.filter_by(content_id=content_id).first()
    return jsonify(content.serialize())
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.get('/search-content', (req, res) => {
    const contentId = req.query.contentId as string;
    const content = contentsDB.find(c => c.contentId === contentId);
    res.json(content);
});
🧪 Senaryo 10: Sınav Sonuçları Sorgulama
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpGet("get-exam-results")]
public IActionResult GetExamResults(string examCode)
{
    var results = _dbContext.ExamResults
        .Where(e => e.ExamCode == examCode)
        .ToList();
    return Ok(results);
}
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/get-exam-results', methods=['GET'])
def get_exam_results():
    exam_code = request.args.get('examCode')
    results = ExamResult.query.filter_by(exam_code=exam_code).all()
    return jsonify([r.serialize() for r in results])
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.get('/get-exam-results', (req, res) => {
    const examCode = req.query.examCode as string;
    const results = examResultsDB.filter(e => e.examCode === examCode);
    res.json(results);
});