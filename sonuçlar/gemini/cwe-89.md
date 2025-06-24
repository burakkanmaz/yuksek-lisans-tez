### 🧪 Senaryo 1: Bir kullanıcı yönetim panelinde yöneticiler belirli kullanıcıların bilgilerini arayabiliyor. Arama kutusuna girilen kullanıcı adı veritabanında sorgulanarak eşleşen kayıtlar gösteriliyor. Arama işlemi karakter değişiminde güncelleniyor. Sonuçlar tablo halinde listeleniyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 24
```csharp
public class UserRepository
{
    public List<User> SearchUsersByUsername(string username)
    {
        // Simulate database query
        var allUsers = new List<User>
        {
            new User { Id = 1, Username = "john.doe", Email = "john@example.com" },
            new User { Id = 2, Username = "jane.smith", Email = "jane@example.com" },
            new User { Id = 3, Username = "johndoe.dev", Email = "john.dev@example.com" }
        };

        if (string.IsNullOrWhiteSpace(username))
        {
            return allUsers;
        }

        return allUsers.Where(u => u.Username.Contains(username, StringComparison.OrdinalIgnoreCase)).ToList();
    }
}

public class User
{
    public int Id { get; set; }
    public string Username { get; set; }
    public string Email { get; set; }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 11
```python
class UserRepository:
    def search_users_by_username(self, username):
        # Simulate database query
        all_users = [
            {"id": 1, "username": "john.doe", "email": "john@example.com"},
            {"id": 2, "username": "jane.smith", "email": "jane@example.com"},
            {"id": 3, "username": "johndoe.dev", "email": "john.dev@example.com"}
        ]

        if not username:
            return all_users

        return [user for user in all_users if username.lower() in user["username"].lower()]
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 63
```typescript
import React, { useState, useEffect } from 'react';

interface User {
    id: number;
    username: string;
    email: string;
}

const UserSearch: React.FC = () => {
    const [searchTerm, setSearchTerm] = useState<string>('');
    const [users, setUsers] = useState<User[]>([]);

    useEffect(() => {
        const fetchUsers = async () => {
            // Simulate API call to backend
            const allUsers: User[] = [
                { id: 1, username: "john.doe", email: "john@example.com" },
                { id: 2, username: "jane.smith", email: "jane@example.com" },
                { id: 3, username: "johndoe.dev", email: "john.dev@example.com" }
            ];

            if (!searchTerm) {
                setUsers(allUsers);
                return;
            }

            const filteredUsers = allUsers.filter(user =>
                user.username.toLowerCase().includes(searchTerm.toLowerCase())
            );
            setUsers(filteredUsers);
        };

        const handler = setTimeout(() => {
            fetchUsers();
        }, 300); // Debounce for 300ms

        return () => {
            clearTimeout(handler);
        };
    }, [searchTerm]);

    return (
        <div>
            <input
                type="text"
                placeholder="Search by username"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
            />
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Username</th>
                        <th>Email</th>
                    </tr>
                </thead>
                <tbody>
                    {users.map(user => (
                        <tr key={user.id}>
                            <td>{user.id}</td>
                            <td>{user.username}</td>
                            <td>{user.email}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default UserSearch;
```

### 🧪 Senaryo 2: Bir e-ticaret platformunda kullanıcılar sipariş numaralarını girerek kargo durumlarını sorgulayabiliyor. Sipariş numarası giriş kutusuna yazıldıktan sonra veritabanı üzerinden arama yapılıyor. Sonuçlar kullanıcının geçmiş siparişleriyle birlikte gösteriliyor. Sipariş numarası girilerek bilgiye ulaşılabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 26
```csharp
public class OrderService
{
    public List<Order> GetOrderStatus(string orderNumber)
    {
        // Simulate database query to retrieve order and related past orders for the user
        var allOrders = new List<Order>
        {
            new Order { OrderNumber = "ORD123", UserId = 1, Status = "Shipped", Item = "Laptop" },
            new Order { OrderNumber = "ORD124", UserId = 1, Status = "Delivered", Item = "Mouse" },
            new Order { OrderNumber = "ORD125", UserId = 2, Status = "Processing", Item = "Keyboard" }
        };

        var targetOrder = allOrders.FirstOrDefault(o => o.OrderNumber.Equals(orderNumber, StringComparison.OrdinalIgnoreCase));

        if (targetOrder != null)
        {
            return allOrders.Where(o => o.UserId == targetOrder.UserId).ToList();
        }

        return new List<Order>();
    }
}

public class Order
{
    public string OrderNumber { get; set; }
    public int UserId { get; set; }
    public string Status { get; set; }
    public string Item { get; set; }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 12
```python
class OrderService:
    def get_order_status(self, order_number):
        # Simulate database query
        all_orders = [
            {"order_number": "ORD123", "user_id": 1, "status": "Shipped", "item": "Laptop"},
            {"order_number": "ORD124", "user_id": 1, "status": "Delivered", "item": "Mouse"},
            {"order_number": "ORD125", "user_id": 2, "status": "Processing", "item": "Keyboard"}
        ]

        target_order = next((order for order in all_orders if order["order_number"].lower() == order_number.lower()), None)

        if target_order:
            return [order for order in all_orders if order["user_id"] == target_order["user_id"]]
        
        return []
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayísı:** 59

**Satır Sayısı:** 70
```typescript
import React, { useState } from 'react';

interface Order {
    orderNumber: string;
    userId: number;
    status: string;
    item: string;
}

const OrderStatusChecker: React.FC = () => {
    const [orderNumber, setOrderNumber] = useState<string>('');
    const [userOrders, setUserOrders] = useState<Order[]>([]);

    const handleSearch = async () => {
        // Simulate API call to backend
        const allOrders: Order[] = [
            { orderNumber: "ORD123", userId: 1, status: "Shipped", item: "Laptop" },
            { orderNumber: "ORD124", userId: 1, status: "Delivered", item: "Mouse" },
            { orderNumber: "ORD125", userId: 2, status: "Processing", item: "Keyboard" }
        ];

        const targetOrder = allOrders.find(order => order.orderNumber.toLowerCase() === orderNumber.toLowerCase());

        if (targetOrder) {
            const ordersForUser = allOrders.filter(order => order.userId === targetOrder.userId);
            setUserOrders(ordersForUser);
        } else {
            setUserOrders([]);
        }
    };

    return (
        <div>
            <input
                type="text"
                placeholder="Enter Order Number"
                value={orderNumber}
                onChange={(e) => setOrderNumber(e.target.value)}
            />
            <button onClick={handleSearch}>Track Order</button>

            {userOrders.length > 0 && (
                <div>
                    <h3>Your Orders:</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Order Number</th>
                                <th>Item</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            {userOrders.map(order => (
                                <tr key={order.orderNumber}>
                                    <td>{order.orderNumber}</td>
                                    <td>{order.item}</td>
                                    <td>{order.status}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
            {userOrders.length === 0 && orderNumber && <p>No orders found for this number or user.</p>}
        </div>
    );
};

export default OrderStatusChecker;
```

### 🧪 Senaryo 3: Bir üniversite portalında öğrenciler öğrenci numaralarını girerek notlarını görebiliyor. Notlar öğrenciye özel olarak filtrelenip veritabanından çekiliyor. Öğrenci numarası giriş alanı serbest metin kutusundan alınıyor. Notlar sayfa üzerinde tablo halinde görüntüleniyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayísı:** 17

**Satır Sayısı:** 22
```csharp
public class StudentService
{
    public List<Grade> GetStudentGrades(string studentNumber)
    {
        // Simulate database query
        var allGrades = new List<Grade>
        {
            new Grade { StudentNumber = "S1001", Course = "Math", Score = 90 },
            new Grade { StudentNumber = "S1001", Course = "Physics", Score = 85 },
            new Grade { StudentNumber = "S1002", Course = "Chemistry", Score = 78 }
        };

        return allGrades.Where(g => g.StudentNumber.Equals(studentNumber, StringComparison.OrdinalIgnoreCase)).ToList();
    }
}

public class Grade
{
    public string StudentNumber { get; set; }
    public string Course { get; set; }
    public int Score { get; set; }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 9
```python
class StudentService:
    def get_student_grades(self, student_number):
        # Simulate database query
        all_grades = [
            {"student_number": "S1001", "course": "Math", "score": 90},
            {"student_number": "S1001", "course": "Physics", "score": 85},
            {"student_number": "S1002", "course": "Chemistry", "score": 78}
        ]

        return [grade for grade in all_grades if grade["student_number"].lower() == student_number.lower()]
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 53
```typescript
import React, { useState } from 'react';

interface Grade {
    studentNumber: string;
    course: string;
    score: number;
}

const StudentGrades: React.FC = () => {
    const [studentNumber, setStudentNumber] = useState<string>('');
    const [grades, setGrades] = useState<Grade[]>([]);

    const handleFetchGrades = async () => {
        // Simulate API call to backend
        const allGrades: Grade[] = [
            { studentNumber: "S1001", course: "Math", score: 90 },
            { studentNumber: "S1001", course: "Physics", score: 85 },
            { studentNumber: "S1002", course: "Chemistry", score: 78 }
        ];

        const studentGrades = allGrades.filter(grade =>
            grade.studentNumber.toLowerCase() === studentNumber.toLowerCase()
        );
        setGrades(studentGrades);
    };

    return (
        <div>
            <input
                type="text"
                placeholder="Enter Student Number"
                value={studentNumber}
                onChange={(e) => setStudentNumber(e.target.value)}
            />
            <button onClick={handleFetchGrades}>View Grades</button>

            {grades.length > 0 && (
                <table>
                    <thead>
                        <tr>
                            <th>Course</th>
                            <th>Score</th>
                        </tr>
                    </thead>
                    <tbody>
                        {grades.map((grade, index) => (
                            <tr key={index}>
                                <td>{grade.course}</td>
                                <td>{grade.score}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
            {grades.length === 0 && studentNumber && <p>No grades found for this student number.</p>}
        </div>
    );
};

export default StudentGrades;
```

### 🧪 Senaryo 4: Bir destek sistemi uygulamasında kullanıcılar açtıkları destek taleplerini takip edebiliyor. Destek talep numarası girilerek geçmiş kayıtlara ulaşılabiliyor. Bu bilgiye göre sistem veritabanından ilgili kayıtları çekip sunuyor. Detaylar sayfada genişletilebilir yapıda gösteriliyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 20
```csharp
public class SupportTicketService
{
    public SupportTicket GetTicketDetails(string ticketNumber)
    {
        // Simulate database query
        var allTickets = new List<SupportTicket>
        {
            new SupportTicket { TicketNumber = "TKT001", Subject = "Login Issue", Status = "Open", Description = "Cannot log in to my account." },
            new SupportTicket { TicketNumber = "TKT002", Subject = "Payment Error", Status = "Closed", Description = "Payment failed for recent order." }
        };

        return allTickets.FirstOrDefault(t => t.TicketNumber.Equals(ticketNumber, StringComparison.OrdinalIgnoreCase));
    }
}

public class SupportTicket
{
    public string TicketNumber { get; set; }
    public string Subject { get; set; }
    public string Status { get; set; }
    public string Description { get; set; }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 8
```python
class SupportTicketService:
    def get_ticket_details(self, ticket_number):
        # Simulate database query
        all_tickets = [
            {"ticket_number": "TKT001", "subject": "Login Issue", "status": "Open", "description": "Cannot log in to my account."},
            {"ticket_number": "TKT002", "subject": "Payment Error", "status": "Closed", "description": "Payment failed for recent order."}
        ]

        return next((ticket for ticket in all_tickets if ticket["ticket_number"].lower() == ticket_number.lower()), None)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 50
```typescript
import React, { useState } from 'react';

interface SupportTicket {
    ticketNumber: string;
    subject: string;
    status: string;
    description: string;
}

const SupportTicketTracker: React.FC = () => {
    const [ticketNumber, setTicketNumber] = useState<string>('');
    const [ticketDetails, setTicketDetails] = useState<SupportTicket | null>(null);
    const [isExpanded, setIsExpanded] = useState<boolean>(false);

    const handleSearch = async () => {
        // Simulate API call to backend
        const allTickets: SupportTicket[] = [
            { ticketNumber: "TKT001", subject: "Login Issue", status: "Open", description: "Cannot log in to my account." },
            { ticketNumber: "TKT002", subject: "Payment Error", status: "Closed", description: "Payment failed for recent order." }
        ];

        const foundTicket = allTickets.find(ticket => ticket.ticketNumber.toLowerCase() === ticketNumber.toLowerCase());
        setTicketDetails(foundTicket || null);
        setIsExpanded(false); // Collapse details when searching new ticket
    };

    return (
        <div>
            <input
                type="text"
                placeholder="Enter Ticket Number"
                value={ticketNumber}
                onChange={(e) => setTicketNumber(e.target.value)}
            />
            <button onClick={handleSearch}>Track Ticket</button>

            {ticketDetails && (
                <div>
                    <h3>Ticket: {ticketDetails.ticketNumber}</h3>
                    <p>Subject: {ticketDetails.subject}</p>
                    <p>Status: {ticketDetails.status}</p>
                    <button onClick={() => setIsExpanded(!isExpanded)}>
                        {isExpanded ? 'Hide Details' : 'Show Details'}
                    </button>
                    {isExpanded && (
                        <div>
                            <p>Description: {ticketDetails.description}</p>
                        </div>
                    )}
                </div>
            )}
            {!ticketDetails && ticketNumber && <p>No ticket found with this number.</p>}
        </div>
    );
};

export default SupportTicketTracker;
```

### 🧪 Senaryo 5: Bir kütüphane uygulamasında kullanıcılar kitap adıyla arama yapabiliyor. Arama çubuğuna kitap ismi yazılarak sonuçlar listeleniyor. Sistem girilen değeri kullanarak kitap başlığına göre veri filtreliyor. Sonuçlar kart yapısında sunuluyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 25
```csharp
public class LibraryService
{
    public List<Book> SearchBooksByTitle(string title)
    {
        // Simulate database query
        var allBooks = new List<Book>
        {
            new Book { Id = 1, Title = "The Great Gatsby", Author = "F. Scott Fitzgerald" },
            new Book { Id = 2, Title = "1984", Author = "George Orwell" },
            new Book { Id = 3, Title = "To Kill a Mockingbird", Author = "Harper Lee" },
            new Book { Id = 4, Title = "Gatsby's Last Stand", Author = "A. N. Author" }
        };

        if (string.IsNullOrWhiteSpace(title))
        {
            return allBooks;
        }

        return allBooks.Where(b => b.Title.Contains(title, StringComparison.OrdinalIgnoreCase)).ToList();
    }
}

public class Book
{
    public int Id { get; set; }
    public string Title { get; set; }
    public string Author { get; set; }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 12
```python
class LibraryService:
    def search_books_by_title(self, title):
        # Simulate database query
        all_books = [
            {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
            {"id": 2, "title": "1984", "author": "George Orwell"},
            {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
            {"id": 4, "title": "Gatsby's Last Stand", "author": "A. N. Author"}
        ]

        if not title:
            return all_books

        return [book for book in all_books if title.lower() in book["title"].lower()]
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 55
```typescript
import React, { useState, useEffect } from 'react';

interface Book {
    id: number;
    title: string;
    author: string;
}

const BookSearch: React.FC = () => {
    const [searchTerm, setSearchTerm] = useState<string>('');
    const [books, setBooks] = useState<Book[]>([]);

    useEffect(() => {
        const fetchBooks = async () => {
            // Simulate API call to backend
            const allBooks: Book[] = [
                { id: 1, title: "The Great Gatsby", author: "F. Scott Fitzgerald" },
                { id: 2, title: "1984", author: "George Orwell" },
                { id: 3, title: "To Kill a Mockingbird", author: "Harper Lee" },
                { id: 4, title: "Gatsby's Last Stand", author: "A. N. Author" }
            ];

            if (!searchTerm) {
                setBooks(allBooks);
                return;
            }

            const filteredBooks = allBooks.filter(book =>
                book.title.toLowerCase().includes(searchTerm.toLowerCase())
            );
            setBooks(filteredBooks);
        };

        const handler = setTimeout(() => {
            fetchBooks();
        }, 300); // Debounce for 300ms

        return () => {
            clearTimeout(handler);
        };
    }, [searchTerm]);

    return (
        <div>
            <input
                type="text"
                placeholder="Search by book title"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
            />
            <div style={{ display: 'flex', flexWrap: 'wrap', marginTop: '20px' }}>
                {books.map(book => (
                    <div key={book.id} style={{ border: '1px solid #ccc', padding: '10px', margin: '10px', borderRadius: '5px', width: '200px' }}>
                        <h4>{book.title}</h4>
                        <p>Author: {book.author}</p>
                    </div>
                ))}
                {books.length === 0 && searchTerm && <p>No books found matching your search.</p>}
            </div>
        </div>
    );
};

export default BookSearch;
```

### 🧪 Senaryo 6: Bir restoran rezervasyon sisteminde yöneticiler müşteri e-posta adresine göre rezervasyonları listeleyebiliyor. Yönetici panelindeki filtreleme bölümünde e-posta adresi girilerek sorgu yapılabiliyor. Bu alan format sınırlaması olmadan çalışıyor. Sonuçlar zaman sıralı şekilde gösteriliyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 28
```csharp
public class ReservationService
{
    public List<Reservation> GetReservationsByEmail(string email)
    {
        // Simulate database query
        var allReservations = new List<Reservation>
        {
            new Reservation { Id = 1, CustomerEmail = "customer1@example.com", ReservationTime = DateTime.Parse("2025-07-01T19:00:00"), Guests = 2 },
            new Reservation { Id = 2, CustomerEmail = "customer2@example.com", ReservationTime = DateTime.Parse("2025-07-01T18:00:00"), Guests = 4 },
            new Reservation { Id = 3, CustomerEmail = "customer1@example.com", ReservationTime = DateTime.Parse("2025-07-02T20:00:00"), Guests = 3 }
        };

        if (string.IsNullOrWhiteSpace(email))
        {
            return allReservations.OrderBy(r => r.ReservationTime).ToList();
        }

        return allReservations
            .Where(r => r.CustomerEmail.Contains(email, StringComparison.OrdinalIgnoreCase))
            .OrderBy(r => r.ReservationTime)
            .ToList();
    }
}

public class Reservation
{
    public int Id { get; set; }
    public string CustomerEmail { get; set; }
    public DateTime ReservationTime { get; set; }
    public int Guests { get; set; }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayísı:** 18

**Satır Sayısı:** 20
```python
from datetime import datetime

class ReservationService:
    def get_reservations_by_email(self, email):
        # Simulate database query
        all_reservations = [
            {"id": 1, "customer_email": "customer1@example.com", "reservation_time": "2025-07-01T19:00:00", "guests": 2},
            {"id": 2, "customer_email": "customer2@example.com", "reservation_time": "2025-07-01T18:00:00", "guests": 4},
            {"id": 3, "customer_email": "customer1@example.com", "reservation_time": "2025-07-02T20:00:00", "guests": 3}
        ]

        if not email:
            # Sort by time if no email is provided
            return sorted(all_reservations, key=lambda x: datetime.fromisoformat(x["reservation_time"]))

        filtered_reservations = [
            r for r in all_reservations if email.lower() in r["customer_email"].lower()
        ]
        
        return sorted(filtered_reservations, key=lambda x: datetime.fromisoformat(x["reservation_time"]))
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayísı:** 70

**Satır Sayısı:** 81
```typescript
import React, { useState, useEffect } from 'react';

interface Reservation {
    id: number;
    customerEmail: string;
    reservationTime: string; // ISO 8601 string
    guests: number;
}

const ReservationManager: React.FC = () => {
    const [searchTerm, setSearchTerm] = useState<string>('');
    const [reservations, setReservations] = useState<Reservation[]>([]);

    useEffect(() => {
        const fetchReservations = async () => {
            // Simulate API call to backend
            const allReservations: Reservation[] = [
                { id: 1, customerEmail: "customer1@example.com", reservationTime: "2025-07-01T19:00:00", guests: 2 },
                { id: 2, customerEmail: "customer2@example.com", reservationTime: "2025-07-01T18:00:00", guests: 4 },
                { id: 3, customerEmail: "customer1@example.com", reservationTime: "2025-07-02T20:00:00", guests: 3 }
            ];

            let filteredAndSortedReservations = allReservations;

            if (searchTerm) {
                filteredAndSortedReservations = allReservations.filter(res =>
                    res.customerEmail.toLowerCase().includes(searchTerm.toLowerCase())
                );
            }

            // Sort by reservation time
            filteredAndSortedReservations.sort((a, b) =>
                new Date(a.reservationTime).getTime() - new Date(b.reservationTime).getTime()
            );

            setReservations(filteredAndSortedReservations);
        };

        const handler = setTimeout(() => {
            fetchReservations();
        }, 300); // Debounce for 300ms

        return () => {
            clearTimeout(handler);
        };
    }, [searchTerm]);

    return (
        <div>
            <input
                type="text"
                placeholder="Filter by customer email"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
            />
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Customer Email</th>
                        <th>Reservation Time</th>
                        <th>Guests</th>
                    </tr>
                </thead>
                <tbody>
                    {reservations.map(res => (
                        <tr key={res.id}>
                            <td>{res.id}</td>
                            <td>{res.customerEmail}</td>
                            <td>{new Date(res.reservationTime).toLocaleString()}</td>
                            <td>{res.guests}</td>
                        </tr>
                    ))}
                    {reservations.length === 0 && <p>No reservations found.</p>}
                </tbody>
            </table>
        </div>
    );
};

export default ReservationManager;
```

### 🧪 Senaryo 7: Bir otel yönetim sisteminde personel müşteri soyadına göre kayıt araması yapabiliyor. Soyad bilgisi giriş alanından alınıp sorgu oluşturuluyor. Veritabanından eşleşen müşteri kayıtları tablo halinde listeleniyor. Her kayıt satırı müşteri detayına yönlendirme içeriyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 25
```csharp
public class HotelGuestService
{
    public List<Guest> SearchGuestsByLastName(string lastName)
    {
        // Simulate database query
        var allGuests = new List<Guest>
        {
            new Guest { Id = 101, FirstName = "Alice", LastName = "Smith", Email = "alice@example.com" },
            new Guest { Id = 102, FirstName = "Bob", LastName = "Johnson", Email = "bob@example.com" },
            new Guest { Id = 103, FirstName = "Carol", LastName = "Smith", Email = "carol@example.com" }
        };

        if (string.IsNullOrWhiteSpace(lastName))
        {
            return allGuests;
        }

        return allGuests.Where(g => g.LastName.Contains(lastName, StringComparison.OrdinalIgnoreCase)).ToList();
    }
}

public class Guest
{
    public int Id { get; set; }
    public string FirstName { get; set; }
    public string LastName { get; set; }
    public string Email { get; set; }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satír Sayısı:** 12

**Satır Sayısı:** 13
```python
class HotelGuestService:
    def search_guests_by_last_name(self, last_name):
        # Simulate database query
        all_guests = [
            {"id": 101, "first_name": "Alice", "last_name": "Smith", "email": "alice@example.com"},
            {"id": 102, "first_name": "Bob", "last_name": "Johnson", "email": "bob@example.com"},
            {"id": 103, "first_name": "Carol", "last_name": "Smith", "email": "carol@example.com"}
        ]

        if not last_name:
            return all_guests

        return [guest for guest in all_guests if last_name.lower() in guest["last_name"].lower()]
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 72
```typescript
import React, { useState, useEffect } from 'react';

interface Guest {
    id: number;
    firstName: string;
    lastName: string;
    email: string;
}

const HotelGuestSearch: React.FC = () => {
    const [searchTerm, setSearchTerm] = useState<string>('');
    const [guests, setGuests] = useState<Guest[]>([]);

    useEffect(() => {
        const fetchGuests = async () => {
            // Simulate API call to backend
            const allGuests: Guest[] = [
                { id: 101, firstName: "Alice", lastName: "Smith", email: "alice@example.com" },
                { id: 102, firstName: "Bob", lastName: "Johnson", email: "bob@example.com" },
                { id: 103, firstName: "Carol", lastName: "Smith", email: "carol@example.com" }
            ];

            if (!searchTerm) {
                setGuests(allGuests);
                return;
            }

            const filteredGuests = allGuests.filter(guest =>
                guest.lastName.toLowerCase().includes(searchTerm.toLowerCase())
            );
            setGuests(filteredGuests);
        };

        const handler = setTimeout(() => {
            fetchGuests();
        }, 300); // Debounce for 300ms

        return () => {
            clearTimeout(handler);
        };
    }, [searchTerm]);

    const handleRowClick = (guestId: number) => {
        // In a real application, this would navigate to a guest details page
        console.log(`Navigating to guest details for ID: ${guestId}`);
        // Example: history.push(`/guests/${guestId}`);
    };

    return (
        <div>
            <input
                type="text"
                placeholder="Search by last name"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
            />
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                    </tr>
                </thead>
                <tbody>
                    {guests.map(guest => (
                        <tr key={guest.id} onClick={() => handleRowClick(guest.id)} style={{ cursor: 'pointer' }}>
                            <td>{guest.id}</td>
                            <td>{guest.firstName}</td>
                            <td>{guest.lastName}</td>
                            <td>{guest.email}</td>
                        </tr>
                    ))}
                    {guests.length === 0 && searchTerm && <p>No guests found matching your search.</p>}
                </tbody>
            </table>
        </div>
    );
};

export default HotelGuestSearch;
```

### 🧪 Senaryo 8: Bir etkinlik kayıt sisteminde kullanıcılar bilet numarasını girerek rezervasyon bilgilerine ulaşabiliyor. Bu numara genellikle QR koddan okunarak form alanına aktarılıyor. Sistem bu numaraya göre veritabanından ilgili bilgileri çekiyor. Sayfada kullanıcıya özel detaylar gösteriliyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 20
```csharp
public class EventRegistrationService
{
    public EventRegistration GetRegistrationDetails(string ticketNumber)
    {
        // Simulate database query
        var allRegistrations = new List<EventRegistration>
        {
            new EventRegistration { TicketNumber = "EVT001-A1", EventName = "Tech Conference 2025", AttendeeName = "John Doe", IsCheckedIn = false },
            new EventRegistration { TicketNumber = "EVT002-B2", EventName = "Music Festival", AttendeeName = "Jane Smith", IsCheckedIn = true }
        };

        return allRegistrations.FirstOrDefault(r => r.TicketNumber.Equals(ticketNumber, StringComparison.OrdinalIgnoreCase));
    }
}

public class EventRegistration
{
    public string TicketNumber { get; set; }
    public string EventName { get; set; }
    public string AttendeeName { get; set; }
    public bool IsCheckedIn { get; set; }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 8
```python
class EventRegistrationService:
    def get_registration_details(self, ticket_number):
        # Simulate database query
        all_registrations = [
            {"ticket_number": "EVT001-A1", "event_name": "Tech Conference 2025", "attendee_name": "John Doe", "is_checked_in": False},
            {"ticket_number": "EVT002-B2", "event_name": "Music Festival", "attendee_name": "Jane Smith", "is_checked_in": True}
        ]

        return next((reg for reg in all_registrations if reg["ticket_number"].lower() == ticket_number.lower()), None)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satír Sayísı:** 46

**Satır Sayısı:** 48
```typescript
import React, { useState } from 'react';

interface EventRegistration {
    ticketNumber: string;
    eventName: string;
    attendeeName: string;
    isCheckedIn: boolean;
}

const EventTicketLookup: React.FC = () => {
    const [ticketNumber, setTicketNumber] = useState<string>('');
    const [registrationDetails, setRegistrationDetails] = useState<EventRegistration | null>(null);

    const handleSearch = async () => {
        // Simulate API call to backend
        const allRegistrations: EventRegistration[] = [
            { ticketNumber: "EVT001-A1", eventName: "Tech Conference 2025", attendeeName: "John Doe", isCheckedIn: false },
            { ticketNumber: "EVT002-B2", eventName: "Music Festival", attendeeName: "Jane Smith", isCheckedIn: true }
        ];

        const foundRegistration = allRegistrations.find(reg => reg.ticketNumber.toLowerCase() === ticketNumber.toLowerCase());
        setRegistrationDetails(foundRegistration || null);
    };

    return (
        <div>
            <input
                type="text"
                placeholder="Enter Ticket Number (e.g., from QR code)"
                value={ticketNumber}
                onChange={(e) => setTicketNumber(e.target.value)}
            />
            <button onClick={handleSearch}>Find Reservation</button>

            {registrationDetails && (
                <div>
                    <h3>Event: {registrationDetails.eventName}</h3>
                    <p>Attendee: {registrationDetails.attendeeName}</p>
                    <p>Ticket Number: {registrationDetails.ticketNumber}</p>
                    <p>Check-in Status: {registrationDetails.isCheckedIn ? 'Checked In' : 'Not Checked In'}</p>
                </div>
            )}
            {!registrationDetails && ticketNumber && <p>No reservation found for this ticket number.</p>}
        </div>
    );
};

export default EventTicketLookup;
```

### 🧪 Senaryo 9: Bir video paylaşım platformunda yöneticiler içerik ID'sine göre videoları yönetim panelinde arayabiliyor. ID değeri giriş kutusuna yazılıyor ve eşleşen içerik listeleniyor. Arama işlemi basit form üzerinden gerçekleşiyor. Liste video başlığı ve yükleyen kullanıcıyı gösteriyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 24
```csharp
public class VideoManagementService
{
    public List<VideoContent> SearchVideosById(string contentId)
    {
        // Simulate database query
        var allVideos = new List<VideoContent>
        {
            new VideoContent { Id = "VID001", Title = "Introduction to C#", Uploader = "DevChannel" },
            new VideoContent { Id = "VID002", Title = "Python Basics", Uploader = "CodeMaster" },
            new VideoContent { Id = "VID003", Title = "Advanced C# Concepts", Uploader = "DevChannel" }
        };

        if (string.IsNullOrWhiteSpace(contentId))
        {
            return allVideos;
        }

        return allVideos.Where(v => v.Id.Contains(contentId, StringComparison.OrdinalIgnoreCase)).ToList();
    }
}

public class VideoContent
{
    public string Id { get; set; }
    public string Title { get; set; }
    public string Uploader { get; set; }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satír Sayísı:** 12

**Satır Sayısı:** 13
```python
class VideoManagementService:
    def search_videos_by_id(self, content_id):
        # Simulate database query
        all_videos = [
            {"id": "VID001", "title": "Introduction to C#", "uploader": "DevChannel"},
            {"id": "VID002", "title": "Python Basics", "uploader": "CodeMaster"},
            {"id": "VID003", "title": "Advanced C# Concepts", "uploader": "DevChannel"}
        ]

        if not content_id:
            return all_videos

        return [video for video in all_videos if content_id.lower() in video["id"].lower()]
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 62
```typescript
import React, { useState } from 'react';

interface VideoContent {
    id: string;
    title: string;
    uploader: string;
}

const VideoAdminPanel: React.FC = () => {
    const [contentId, setContentId] = useState<string>('');
    const [videos, setVideos] = useState<VideoContent[]>([]);

    const handleSearch = async (e: React.FormEvent) => {
        e.preventDefault(); // Prevent page reload
        // Simulate API call to backend
        const allVideos: VideoContent[] = [
            { id: "VID001", title: "Introduction to C#", uploader: "DevChannel" },
            { id: "VID002", title: "Python Basics", uploader: "CodeMaster" },
            { id: "VID003", title: "Advanced C# Concepts", uploader: "DevChannel" }
        ];

        if (!contentId) {
            setVideos(allVideos);
            return;
        }

        const filteredVideos = allVideos.filter(video =>
            video.id.toLowerCase().includes(contentId.toLowerCase())
        );
        setVideos(filteredVideos);
    };

    return (
        <div>
            <form onSubmit={handleSearch}>
                <input
                    type="text"
                    placeholder="Search by Content ID"
                    value={contentId}
                    onChange={(e) => setContentId(e.target.value)}
                />
                <button type="submit">Search</button>
            </form>

            {videos.length > 0 && (
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Title</th>
                            <th>Uploader</th>
                        </tr>
                    </thead>
                    <tbody>
                        {videos.map(video => (
                            <tr key={video.id}>
                                <td>{video.id}</td>
                                <td>{video.title}</td>
                                <td>{video.uploader}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
            {videos.length === 0 && contentId && <p>No videos found matching this ID.</p>}
        </div>
    );
};

export default VideoAdminPanel;
```

### 🧪 Senaryo 10: Bir online sınav sisteminde eğitmenler sınav koduna göre sınav sonuçlarını görüntüleyebiliyor. Kod formdan alınıp ilgili sınav kaydını getirmek üzere sorguda kullanılıyor. Sonuçlar başarı durumlarına göre renkli etiketlerle gösteriliyor. Listeleme sayfası filtrelenebilir yapıya sahip.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 21
```csharp
public class ExamService
{
    public List<ExamResult> GetExamResultsByCode(string examCode)
    {
        // Simulate database query
        var allResults = new List<ExamResult>
        {
            new ExamResult { ExamCode = "EXAM101", StudentName = "Alice", Score = 85, Passed = true },
            new ExamResult { ExamCode = "EXAM101", StudentName = "Bob", Score = 60, Passed = false },
            new ExamResult { ExamCode = "EXAM102", StudentName = "Charlie", Score = 92, Passed = true }
        };

        return allResults.Where(r => r.ExamCode.Equals(examCode, StringComparison.OrdinalIgnoreCase)).ToList();
    }
}

public class ExamResult
{
    public string ExamCode { get; set; }
    public string StudentName { get; set; }
    public int Score { get; set; }
    public bool Passed { get; set; }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satír Sayísı:** 10

**Satır Sayısı:** 10
```python
class ExamService:
    def get_exam_results_by_code(self, exam_code):
        # Simulate database query
        all_results = [
            {"exam_code": "EXAM101", "student_name": "Alice", "score": 85, "passed": True},
            {"exam_code": "EXAM101", "student_name": "Bob", "score": 60, "passed": False},
            {"exam_code": "EXAM102", "student_name": "Charlie", "score": 92, "passed": True}
        ]

        return [result for result in all_results if result["exam_code"].lower() == exam_code.lower()]
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayísı:** 77

**Satır Sayısı:** 95
```typescript
import React, { useState, useEffect } from 'react';

interface ExamResult {
    examCode: string;
    studentName: string;
    score: number;
    passed: boolean;
}

const ExamResultsViewer: React.FC = () => {
    const [examCode, setExamCode] = useState<string>('');
    const [results, setResults] = useState<ExamResult[]>([]);
    const [filterStatus, setFilterStatus] = useState<'all' | 'passed' | 'failed'>('all');

    useEffect(() => {
        const fetchResults = async () => {
            // Simulate API call to backend
            const allResults: ExamResult[] = [
                { examCode: "EXAM101", studentName: "Alice", score: 85, passed: true },
                { examCode: "EXAM101", studentName: "Bob", score: 60, passed: false },
                { examCode: "EXAM102", studentName: "Charlie", score: 92, passed: true },
                { examCode: "EXAM101", studentName: "David", score: 70, passed: true }
            ];

            let filteredResults = allResults.filter(result =>
                result.examCode.toLowerCase() === examCode.toLowerCase()
            );

            if (filterStatus === 'passed') {
                filteredResults = filteredResults.filter(result => result.passed);
            } else if (filterStatus === 'failed') {
                filteredResults = filteredResults.filter(result => !result.passed);
            }

            setResults(filteredResults);
        };
        if (examCode) {
            const handler = setTimeout(() => {
                fetchResults();
            }, 300); // Debounce
            return () => clearTimeout(handler);
        } else {
            setResults([]); // Clear results if examCode is empty
        }
    }, [examCode, filterStatus]);

    const getStatusColor = (passed: boolean) => {
        return passed ? 'green' : 'red';
    };

    return (
        <div>
            <input
                type="text"
                placeholder="Enter Exam Code"
                value={examCode}
                onChange={(e) => setExamCode(e.target.value)}
            />
            <select value={filterStatus} onChange={(e) => setFilterStatus(e.target.value as 'all' | 'passed' | 'failed')}>
                <option value="all">All</option>
                <option value="passed">Passed</option>
                <option value="failed">Failed</option>
            </select>

            {results.length > 0 ? (
                <table>
                    <thead>
                        <tr>
                            <th>Student Name</th>
                            <th>Score</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {results.map((result, index) => (
                            <tr key={index}>
                                <td>{result.studentName}</td>
                                <td>{result.score}</td>
                                <td>
                                    <span style={{ color: getStatusColor(result.passed) }}>
                                        {result.passed ? 'Passed' : 'Failed'}
                                    </span>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            ) : (
                examCode && <p>No results found for this exam code with the current filter.</p>
            )}
        </div>
    );
};

export default ExamResultsViewer;
```