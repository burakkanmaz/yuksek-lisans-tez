### 🧪 Senaryo 1: Bir e-ticaret sitesinde kullanıcılar ödeme ekranında adres bilgilerini girebiliyor. Bu bilgiler sisteme kaydedildikten sonra kargo firmalarına iletiliyor. Adres, il ve posta kodu alanları metin kutularından alınıyor. Kullanıcılar bu alanlara istedikleri içeriği yazabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 59
```csharp
using Microsoft.AspNetCore.Mvc;
using System.ComponentModel.DataAnnotations; // For potential validation, though not strictly required by scenario
using System.Threading.Tasks;

[ApiController]
[Route("api/[controller]")]
public class OrderController : ControllerBase
{
    private readonly ApplicationDbContext _context; // Assume DbContext for database operations

    public OrderController(ApplicationDbContext context)
    {
        _context = context;
    }

    public class ShippingAddress
    {
        [Required]
        public string AddressLine { get; set; }

        [Required]
        public string City { get; set; }

        [Required]
        public string PostalCode { get; set; }
    }

    [HttpPost("submit-address")]
    public async Task<IActionResult> SubmitAddress([FromBody] ShippingAddress address)
    {
        if (!ModelState.IsValid)
        {
            return BadRequest(ModelState);
        }

        // In a real application, you'd map this to an Entity Framework entity
        // and save it to the database.
        var newAddress = new OrderAddress
        {
            AddressLine = address.AddressLine,
            City = address.City,
            PostalCode = address.PostalCode
        };

        _context.OrderAddresses.Add(newAddress);
        await _context.SaveChangesAsync();

        // In a real scenario, you would also integrate with a shipping carrier API here
        // shippingService.SendAddressToCarrier(newAddress);

        return Ok(new { message = "Address submitted successfully." });
    }
}

// Example DbContext and Entity (assuming Entity Framework Core)
public class ApplicationDbContext : Microsoft.EntityFrameworkCore.DbContext
{
    public ApplicationDbContext(Microsoft.EntityFrameworkCore.DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }

    public Microsoft.EntityFrameworkCore.DbSet<OrderAddress> OrderAddresses { get; set; }
}

public class OrderAddress
{
    public int Id { get; set; }
    public string AddressLine { get; set; }
    public string City { get; set; }
    public string PostalCode { get; set; }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 31
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'  # Example SQLite database
db = SQLAlchemy(app)

class ShippingAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_line = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<ShippingAddress {self.address_line}, {self.city}, {self.postal_code}>'

# Ensure the database tables are created
with app.app_context():
    db.create_all()

@app.route('/api/submit-address', methods=['POST'])
def submit_address():
    data = request.get_json()

    if not data or not all(k in data for k in ("addressLine", "city", "postalCode")):
        return jsonify({"error": "Missing address information"}), 400

    address_line = data['addressLine']
    city = data['city']
    postal_code = data['postalCode']

    new_address = ShippingAddress(address_line=address_line, city=city, postal_code=postal_code)
    db.session.add(new_address)
    db.session.commit()

    # In a real scenario, you would also integrate with a shipping carrier API here
    # shipping_service.send_address_to_carrier(new_address)

    return jsonify({"message": "Address submitted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 47
```typescript
import express from 'express';
import bodyParser from 'body-parser';
import { Pool } from 'pg'; // Using pg for PostgreSQL example

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Database connection pool (example with PostgreSQL)
const pool = new Pool({
    user: 'user',
    host: 'localhost',
    database: 'ecommerce_db',
    password: 'password',
    port: 5432,
});

interface ShippingAddress {
    addressLine: string;
    city: string;
    postalCode: string;
}

app.post('/api/submit-address', async (req, res) => {
    const { addressLine, city, postalCode }: ShippingAddress = req.body;

    if (!addressLine || !city || !postalCode) {
        return res.status(400).json({ error: 'Missing address information' });
    }

    try {
        const queryText = 'INSERT INTO shipping_addresses(address_line, city, postal_code) VALUES($1, $2, $3) RETURNING *';
        const result = await pool.query(queryText, [addressLine, city, postalCode]);

        // In a real scenario, you would also integrate with a shipping carrier API here
        // shippingService.sendAddressToCarrier(result.rows[0]);

        res.status(200).json({ message: 'Address submitted successfully', address: result.rows[0] });
    } catch (err) {
        console.error('Error saving address:', err);
        res.status(500).json({ error: 'Failed to submit address' });
    }
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});

/*
To set up PostgreSQL:
CREATE TABLE shipping_addresses (
    id SERIAL PRIMARY KEY,
    address_line VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL
);
*/
```

### 🧪 Senaryo 2: Bir eğitim platformunda kullanıcılar şifre oluştururken serbest metin girebiliyor. Şifre alanı minimum uzunluk şartı bulunuyor. Özel karakter, boşluk ve farklı semboller şifrede kullanılabiliyor. Şifre bilgisi sisteme kaydediliyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 55
```csharp
using Microsoft.AspNetCore.Mvc;
using System.ComponentModel.DataAnnotations;
using System.Threading.Tasks;
using BCrypt.Net; // For password hashing

[ApiController]
[Route("api/[controller]")]
public class AuthController : ControllerBase
{
    private readonly ApplicationDbContext _context; // Assume DbContext for database operations

    public AuthController(ApplicationDbContext context)
    {
        _context = context;
    }

    public class RegisterModel
    {
        [Required]
        public string Username { get; set; }

        [Required]
        [MinLength(8, ErrorMessage = "Password must be at least 8 characters long.")] // Minimum length requirement
        public string Password { get; set; }
    }

    [HttpPost("register")]
    public async Task<IActionResult> Register([FromBody] RegisterModel model)
    {
        if (!ModelState.IsValid)
        {
            return BadRequest(ModelState);
        }

        // Hash the password before saving it
        string hashedPassword = BCrypt.Net.BCrypt.HashPassword(model.Password);

        var newUser = new User
        {
            Username = model.Username,
            PasswordHash = hashedPassword // Store the hashed password
        };

        _context.Users.Add(newUser);
        await _context.SaveChangesAsync();

        return Ok(new { message = "User registered successfully." });
    }
}

// Example DbContext and Entity
public class ApplicationDbContext : Microsoft.EntityFrameworkCore.DbContext
{
    public ApplicationDbContext(Microsoft.EntityFrameworkCore.DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }

    public Microsoft.EntityFrameworkCore.DbSet<User> Users { get; set; }
}

public class User
{
    public int Id { get; set; }
    public string Username { get; set; }
    public string PasswordHash { get; set; } // Stores the hashed password
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 35
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash # For password hashing

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///education.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False) # Stores the hashed password

    def __repr__(self):
        return f'<User {self.username}>'

# Ensure the database tables are created
with app.app_context():
    db.create_all()

@app.route('/api/register', methods=['POST'])
def register_user():
    data = request.get_json()

    if not data or not all(k in data for k in ("username", "password")):
        return jsonify({"error": "Missing username or password"}), 400

    username = data['username']
    password = data['password']

    if len(password) < 8: # Minimum length requirement
        return jsonify({"error": "Password must be at least 8 characters long"}), 400

    hashed_password = generate_password_hash(password) # Hash the password

    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to register user: {str(e)}"}), 500

    return jsonify({"message": "User registered successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 50
```typescript
import express from 'express';
import bodyParser from 'body-parser';
import { Pool } from 'pg';
import bcrypt from 'bcrypt'; // For password hashing

const app = express();
const port = 3000;

app.use(bodyParser.json());

const pool = new Pool({
    user: 'user',
    host: 'localhost',
    database: 'education_db',
    password: 'password',
    port: 5432,
});

interface RegisterData {
    username: string;
    password: string;
}

app.post('/api/register', async (req, res) => {
    const { username, password }: RegisterData = req.body;

    if (!username || !password) {
        return res.status(400).json({ error: 'Missing username or password' });
    }

    if (password.length < 8) { // Minimum length requirement
        return res.status(400).json({ error: 'Password must be at least 8 characters long.' });
    }

    try {
        const hashedPassword = await bcrypt.hash(password, 10); // Hash the password

        const queryText = 'INSERT INTO users(username, password_hash) VALUES($1, $2) RETURNING id, username';
        const result = await pool.query(queryText, [username, hashedPassword]);

        res.status(201).json({ message: 'User registered successfully', user: result.rows[0] });
    } catch (err: any) {
        if (err.code === '23505') { // Duplicate username error code for PostgreSQL
            return res.status(409).json({ error: 'Username already exists.' });
        }
        console.error('Error registering user:', err);
        res.status(500).json({ error: 'Failed to register user' });
    }
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});

/*
To set up PostgreSQL:
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);
*/
```

### 🧪 Senaryo 3: Bir kargo takip sisteminde kullanıcılar kargo numarasını girerek paket bilgilerine erişiyor. Kargo numarası metin kutusuna yazılıyor ve sorgulama işlemi başlatılıyor. Giriş alanında uzunluk sınırı bulunuyor. Farklı karakter türleri girişte kullanılabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 57
```csharp
using Microsoft.AspNetCore.Mvc;
using System.ComponentModel.DataAnnotations;
using System.Threading.Tasks;
using System.Collections.Generic;

[ApiController]
[Route("api/[controller]")]
public class TrackingController : ControllerBase
{
    // In a real application, this would be a service interacting with a database or external API
    private readonly TrackingService _trackingService;

    public TrackingController(TrackingService trackingService)
    {
        _trackingService = trackingService;
    }

    public class TrackingRequest
    {
        [Required]
        [StringLength(50, MinimumLength = 5, ErrorMessage = "Tracking number must be between 5 and 50 characters.")] // Length constraint
        public string TrackingNumber { get; set; }
    }

    public class PackageInfo
    {
        public string TrackingNumber { get; set; }
        public string Status { get; set; }
        public string LastLocation { get; set; }
        public List<string> History { get; set; }
    }

    [HttpGet("track")]
    public async Task<IActionResult> TrackPackage([FromQuery] TrackingRequest request)
    {
        if (!ModelState.IsValid)
        {
            return BadRequest(ModelState);
        }

        var packageInfo = await _trackingService.GetPackageInfo(request.TrackingNumber);

        if (packageInfo == null)
        {
            return NotFound(new { message = "Package not found or invalid tracking number." });
        }

        return Ok(packageInfo);
    }
}

// Example Tracking Service (simulated data)
public class TrackingService
{
    private readonly Dictionary<string, PackageInfo> _mockPackages = new Dictionary<string, PackageInfo>
    {
        { "ABC123XYZ", new PackageInfo { TrackingNumber = "ABC123XYZ", Status = "In Transit", LastLocation = "Istanbul", History = new List<string> { "Processed at facility", "Departed origin" } } },
        { "DEF456UVW", new PackageInfo { TrackingNumber = "DEF456UVW", Status = "Delivered", LastLocation = "Ankara", History = new List<string> { "Processed at facility", "Out for delivery", "Delivered" } } }
    };

    public Task<PackageInfo> GetPackageInfo(string trackingNumber)
    {
        // Simulate an asynchronous operation, e.g., fetching from a database or external API
        _mockPackages.TryGetValue(trackingNumber, out var info);
        return Task.FromResult(info);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 31
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database/external API for package info
mock_packages = {
    "ABC123XYZ": {
        "trackingNumber": "ABC123XYZ",
        "status": "In Transit",
        "lastLocation": "Istanbul",
        "history": ["Processed at facility", "Departed origin"]
    },
    "DEF456UVW": {
        "trackingNumber": "DEF456UVW",
        "status": "Delivered",
        "lastLocation": "Ankara",
        "history": ["Processed at facility", "Out for delivery", "Delivered"]
    },
}

@app.route('/api/track', methods=['GET'])
def track_package():
    tracking_number = request.args.get('trackingNumber')

    if not tracking_number:
        return jsonify({"error": "Tracking number is required"}), 400

    # Length constraint
    if not (5 <= len(tracking_number) <= 50):
        return jsonify({"error": "Tracking number must be between 5 and 50 characters."}), 400

    package_info = mock_packages.get(tracking_number)

    if not package_info:
        return jsonify({"message": "Package not found or invalid tracking number."}), 404

    return jsonify(package_info), 200

if __name__ == '__main__':
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 44
```typescript
import express from 'express';
import bodyParser from 'body-parser';

const app = express();
const port = 3000;

app.use(bodyParser.json());

interface PackageInfo {
    trackingNumber: string;
    status: string;
    lastLocation: string;
    history: string[];
}

// Simulated database/external API for package info
const mockPackages: { [key: string]: PackageInfo } = {
    "ABC123XYZ": {
        trackingNumber: "ABC123XYZ",
        status: "In Transit",
        lastLocation: "Istanbul",
        history: ["Processed at facility", "Departed origin"]
    },
    "DEF456UVW": {
        trackingNumber: "DEF456UVW",
        status: "Delivered",
        lastLocation: "Ankara",
        history: ["Processed at facility", "Out for delivery", "Delivered"]
    },
};

app.get('/api/track', (req, res) => {
    const trackingNumber = req.query.trackingNumber as string;

    if (!trackingNumber) {
        return res.status(400).json({ error: 'Tracking number is required.' });
    }

    // Length constraint
    if (trackingNumber.length < 5 || trackingNumber.length > 50) {
        return res.status(400).json({ error: 'Tracking number must be between 5 and 50 characters.' });
    }

    const packageInfo = mockPackages[trackingNumber];

    if (!packageInfo) {
        return res.status(404).json({ message: 'Package not found or invalid tracking number.' });
    }

    res.status(200).json(packageInfo);
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
```

### 🧪 Senaryo 4: Bir sosyal medya platformunda kullanıcılar biyografi bilgilerini doldurabiliyor. Biyografi alanı karakter sınırı ile sınırlandırılmış. Bu bilgiler kullanıcı profillerinde görüntüleniyor. HTML ve özel semboller girişte kullanılabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 49
```csharp
using Microsoft.AspNetCore.Mvc;
using System.ComponentModel.DataAnnotations;
using System.Threading.Tasks;

[ApiController]
[Route("api/[controller]")]
public class ProfileController : ControllerBase
{
    private readonly ApplicationDbContext _context; // Assume DbContext for database operations

    public ProfileController(ApplicationDbContext context)
    {
        _context = context;
    }

    public class UpdateBioModel
    {
        [StringLength(500, ErrorMessage = "Biography cannot exceed 500 characters.")] // Character limit
        public string Biography { get; set; }
    }

    [HttpPut("update-bio/{userId}")]
    public async Task<IActionResult> UpdateBiography(int userId, [FromBody] UpdateBioModel model)
    {
        if (!ModelState.IsValid)
        {
            return BadRequest(ModelState);
        }

        var user = await _context.Users.FindAsync(userId);
        if (user == null)
        {
            return NotFound(new { message = "User not found." });
        }

        user.Biography = model.Biography; // HTML and special symbols are allowed as per scenario
        await _context.SaveChangesAsync();

        return Ok(new { message = "Biography updated successfully." });
    }
}

// Example DbContext and Entity
public class ApplicationDbContext : Microsoft.EntityFrameworkCore.DbContext
{
    public ApplicationDbContext(Microsoft.EntityFrameworkCore.DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }

    public Microsoft.EntityFrameworkCore.DbSet<User> Users { get; set; }
}

public class User
{
    public int Id { get; set; }
    public string Username { get; set; }
    public string Biography { get; set; } // Stores biography
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 30
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///social_media.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    biography = db.Column(db.Text) # Using Text type for potentially longer strings

    def __repr__(self):
        return f'<User {self.username}>'

# Ensure the database tables are created
with app.app_context():
    db.create_all()

@app.route('/api/update-bio/<int:user_id>', methods=['PUT'])
def update_biography(user_id):
    data = request.get_json()

    if not data or 'biography' not in data:
        return jsonify({"error": "Biography data is required"}), 400

    biography = data['biography']

    if len(biography) > 500: # Character limit
        return jsonify({"error": "Biography cannot exceed 500 characters."}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found."}), 404

    user.biography = biography
    db.session.commit()

    return jsonify({"message": "Biography updated successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 48
```typescript
import express from 'express';
import bodyParser from 'body-parser';
import { Pool } from 'pg';

const app = express();
const port = 3000;

app.use(bodyParser.json());

const pool = new Pool({
    user: 'user',
    host: 'localhost',
    database: 'social_media_db',
    password: 'password',
    port: 5432,
});

interface UpdateBioData {
    biography: string;
}

app.put('/api/update-bio/:userId', async (req, res) => {
    const userId = parseInt(req.params.userId);
    const { biography }: UpdateBioData = req.body;

    if (biography === undefined || biography === null) {
        return res.status(400).json({ error: 'Biography data is required.' });
    }

    if (biography.length > 500) { // Character limit
        return res.status(400).json({ error: 'Biography cannot exceed 500 characters.' });
    }

    try {
        const queryText = 'UPDATE users SET biography = $1 WHERE id = $2 RETURNING *';
        const result = await pool.query(queryText, [biography, userId]);

        if (result.rowCount === 0) {
            return res.status(404).json({ message: 'User not found.' });
        }

        res.status(200).json({ message: 'Biography updated successfully.', user: result.rows[0] });
    } catch (err) {
        console.error('Error updating biography:', err);
        res.status(500).json({ error: 'Failed to update biography' });
    }
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});

/*
To set up PostgreSQL:
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    biography TEXT
);
*/
```

### 🧪 Senaryo 5: Bir rezervasyon sisteminde kullanıcılar tarih aralığı girerek uygunluk sorgulaması yapabiliyor. Tarih alanları metin girişi ile doldurulabiliyor. Sistem bu tarih bilgilerini işleyerek uygunluk kontrolü yapıyor. Tarih formatı serbest bırakılmış.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 79
```csharp
using Microsoft.AspNetCore.Mvc;
using System;
using System.Threading.Tasks;
using System.Collections.Generic;

[ApiController]
[Route("api/[controller]")]
public class BookingController : ControllerBase
{
    private readonly AvailabilityService _availabilityService;

    public BookingController(AvailabilityService availabilityService)
    {
        _availabilityService = availabilityService;
    }

    public class AvailabilityRequest
    {
        public string StartDate { get; set; } // Free text date format
        public string EndDate { get; set; }   // Free text date format
    }

    public class AvailabilityResult
    {
        public string RequestedStartDate { get; set; }
        public string RequestedEndDate { get; set; }
        public bool IsAvailable { get; set; }
        public string Message { get; set; }
    }

    [HttpGet("check-availability")]
    public async Task<IActionResult> CheckAvailability([FromQuery] AvailabilityRequest request)
    {
        if (string.IsNullOrWhiteSpace(request.StartDate) || string.IsNullOrWhiteSpace(request.EndDate))
        {
            return BadRequest(new { error = "Start date and end date are required." });
        }

        // Since date format is free, parse it with multiple attempts or a flexible parser.
        // For demonstration, a simple DateTime.TryParse is used. In a real system,
        // you might use a more robust date parsing library or enforce some common formats.
        if (!DateTime.TryParse(request.StartDate, out DateTime parsedStartDate) ||
            !DateTime.TryParse(request.EndDate, out DateTime parsedEndDate))
        {
            return BadRequest(new { error = "Invalid date format. Please ensure dates are parseable." });
        }

        if (parsedStartDate > parsedEndDate)
        {
            return BadRequest(new { error = "Start date cannot be after end date." });
        }

        var result = await _availabilityService.CheckRoomAvailability(parsedStartDate, parsedEndDate);

        return Ok(new AvailabilityResult
        {
            RequestedStartDate = request.StartDate,
            RequestedEndDate = request.EndDate,
            IsAvailable = result,
            Message = result ? "Rooms are available for the selected dates." : "No rooms available for the selected dates."
        });
    }
}

// Example Availability Service (simulated data)
public class AvailabilityService
{
    // Mock availability for demonstration (e.g., room is always available unless specific dates are blocked)
    private readonly List<(DateTime startDate, DateTime endDate)> _blockedDates = new List<(DateTime, DateTime)>
    {
        (new DateTime(2025, 7, 10), new DateTime(2025, 7, 15)),
        (new DateTime(2025, 8, 1), new DateTime(2025, 8, 5))
    };

    public Task<bool> CheckRoomAvailability(DateTime startDate, DateTime endDate)
    {
        // Simulate checking a database or calendar system
        bool isAvailable = true;
        foreach (var blockedPeriod in _blockedDates)
        {
            // Check for overlap
            if (startDate < blockedPeriod.endDate && endDate > blockedPeriod.startDate)
            {
                isAvailable = false;
                break;
            }
        }
        return Task.FromResult(isAvailable);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 46
```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Simulated availability data
blocked_dates = [
    (datetime(2025, 7, 10), datetime(2025, 7, 15)),
    (datetime(2025, 8, 1), datetime(2025, 8, 5))
]

def check_room_availability(start_date_obj, end_date_obj):
    """
    Simulates checking room availability.
    """
    for blocked_start, blocked_end in blocked_dates:
        # Check for overlap
        if start_date_obj < blocked_end and end_date_obj > blocked_start:
            return False
    return True

@app.route('/api/check-availability', methods=['GET'])
def check_availability():
    start_date_str = request.args.get('startDate')
    end_date_str = request.args.get('endDate')

    if not start_date_str or not end_date_str:
        return jsonify({"error": "Start date and end date are required."}), 400

    # Since date format is free, try to parse with common formats.
    # In a real system, a more robust parsing library or format hint would be beneficial.
    try:
        # Attempt to parse common formats
        parsed_start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        parsed_end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    except ValueError:
        try:
            parsed_start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
            parsed_end_date = datetime.strptime(end_date_str, "%d/%m/%Y")
        except ValueError:
            return jsonify({"error": "Invalid date format. Please use YYYY-MM-DD or DD/MM/YYYY."}), 400

    if parsed_start_date > parsed_end_date:
        return jsonify({"error": "Start date cannot be after end date."}), 400

    is_available = check_room_availability(parsed_start_date, parsed_end_date)

    return jsonify({
        "requestedStartDate": start_date_str,
        "requestedEndDate": end_date_str,
        "isAvailable": is_available,
        "message": "Rooms are available for the selected dates." if is_available else "No rooms available for the selected dates."
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 71
```typescript
import express from 'express';
import bodyParser from 'body-parser';
import { parse, isValid, parseISO } from 'date-fns'; // For flexible date parsing

const app = express();
const port = 3000;

app.use(bodyParser.json());

interface AvailabilityRequest {
    startDate: string;
    endDate: string;
}

interface AvailabilityResult {
    requestedStartDate: string;
    requestedEndDate: string;
    isAvailable: boolean;
    message: string;
}

// Simulated availability data
const blockedDates: Array<{ startDate: Date, endDate: Date }> = [
    { startDate: new Date(2025, 6, 10), endDate: new Date(2025, 6, 15) }, // Month is 0-indexed in JS Dates
    { startDate: new Date(2025, 7, 1), endDate: new Date(2025, 7, 5) }
];

const checkRoomAvailability = (startDate: Date, endDate: Date): boolean => {
    for (const blockedPeriod of blockedDates) {
        // Check for overlap
        if (startDate < blockedPeriod.endDate && endDate > blockedPeriod.startDate) {
            return false;
        }
    }
    return true;
};

app.get('/api/check-availability', (req, res) => {
    const { startDate, endDate }: AvailabilityRequest = req.query as any;

    if (!startDate || !endDate) {
        return res.status(400).json({ error: 'Start date and end date are required.' });
    }

    let parsedStartDate: Date;
    let parsedEndDate: Date;

    // Try parsing with common formats due to "free format" requirement
    // date-fns parse can be flexible, or you can chain multiple parse attempts
    parsedStartDate = parse(startDate, 'yyyy-MM-dd', new Date());
    if (!isValid(parsedStartDate)) {
        parsedStartDate = parse(startDate, 'dd/MM/yyyy', new Date());
    }
    if (!isValid(parsedStartDate)) {
        parsedStartDate = parseISO(startDate); // Try ISO format
    }

    parsedEndDate = parse(endDate, 'yyyy-MM-dd', new Date());
    if (!isValid(parsedEndDate)) {
        parsedEndDate = parse(endDate, 'dd/MM/yyyy', new Date());
    }
    if (!isValid(parsedEndDate)) {
        parsedEndDate = parseISO(endDate); // Try ISO format
    }

    if (!isValid(parsedStartDate) || !isValid(parsedEndDate)) {
        return res.status(400).json({ error: 'Invalid date format. Please ensure dates are parseable.' });
    }

    if (parsedStartDate > parsedEndDate) {
        return res.status(400).json({ error: 'Start date cannot be after end date.' });
    }

    const isAvailable = checkRoomAvailability(parsedStartDate, parsedEndDate);

    const result: AvailabilityResult = {
        requestedStartDate: startDate,
        requestedEndDate: endDate,
        isAvailable: isAvailable,
        message: isAvailable ? "Rooms are available for the selected dates." : "No rooms available for the selected dates."
    };

    res.status(200).json(result);
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
```

### 🧪 Senaryo 6: Bir forum sisteminde kullanıcılar konu başlığı ve içerik girerek yeni konu açabiliyor. Karakter sayısı sınırlaması bulunuyor. Başlık alanına sayılar ve semboller girilebiliyor. Konular ana sayfada listeleniyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 65
```csharp
using Microsoft.AspNetCore.Mvc;
using System.ComponentModel.DataAnnotations;
using System.Threading.Tasks;

[ApiController]
[Route("api/[controller]")]
public class ForumController : ControllerBase
{
    private readonly ApplicationDbContext _context; // Assume DbContext for database operations

    public ForumController(ApplicationDbContext context)
    {
        _context = context;
    }

    public class CreateTopicModel
    {
        [Required]
        [StringLength(100, ErrorMessage = "Title cannot exceed 100 characters.")] // Character limit for title
        public string Title { get; set; }

        [Required]
        [StringLength(5000, ErrorMessage = "Content cannot exceed 5000 characters.")] // Character limit for content
        public string Content { get; set; }
    }

    [HttpPost("create-topic")]
    public async Task<IActionResult> CreateTopic([FromBody] CreateTopicModel model)
    {
        if (!ModelState.IsValid)
        {
            return BadRequest(ModelState);
        }

        var newTopic = new ForumTopic
        {
            Title = model.Title,
            Content = model.Content,
            CreatedDate = DateTime.UtcNow,
            // Assuming a UserId would be associated here in a real app
            // UserId = currentUserId
        };

        _context.ForumTopics.Add(newTopic);
        await _context.SaveChangesAsync();

        return Ok(new { message = "Topic created successfully.", topicId = newTopic.Id });
    }

    [HttpGet("topics")]
    public async Task<IActionResult> GetTopics()
    {
        // For demonstration, returning all topics. In a real app, pagination would be used.
        var topics = await _context.ForumTopics.OrderByDescending(t => t.CreatedDate).ToListAsync();
        return Ok(topics);
    }
}

// Example DbContext and Entity
public class ApplicationDbContext : Microsoft.EntityFrameworkCore.DbContext
{
    public ApplicationDbContext(Microsoft.EntityFrameworkCore.DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }

    public Microsoft.EntityFrameworkCore.DbSet<ForumTopic> ForumTopics { get; set; }
}

public class ForumTopic
{
    public int Id { get; set; }
    public string Title { get; set; }
    public string Content { get; set; }
    public DateTime CreatedDate { get; set; }
    // public int UserId { get; set; } // Example for associating with a user
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 38
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
db = SQLAlchemy(app)

class ForumTopic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False) # Character limit for title
    content = db.Column(db.Text, nullable=False) # Character limit for content
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ForumTopic {self.title}>'

# Ensure the database tables are created
with app.app_context():
    db.create_all()

@app.route('/api/create-topic', methods=['POST'])
def create_topic():
    data = request.get_json()

    if not data or not all(k in data for k in ("title", "content")):
        return jsonify({"error": "Title and content are required"}), 400

    title = data['title']
    content = data['content']

    if len(title) > 100:
        return jsonify({"error": "Title cannot exceed 100 characters."}), 400
    if len(content) > 5000:
        return jsonify({"error": "Content cannot exceed 5000 characters."}), 400

    new_topic = ForumTopic(title=title, content=content)
    db.session.add(new_topic)
    db.session.commit()

    return jsonify({"message": "Topic created successfully.", "topicId": new_topic.id}), 201

@app.route('/api/topics', methods=['GET'])
def get_topics():
    topics = ForumTopic.query.order_by(ForumTopic.created_date.desc()).all()
    topics_list = [{"id": topic.id, "title": topic.title, "content": topic.content, "createdDate": topic.created_date.isoformat()} for topic in topics]
    return jsonify(topics_list), 200

if __name__ == '__main__':
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 65
```typescript
import express from 'express';
import bodyParser from 'body-parser';
import { Pool } from 'pg';

const app = express();
const port = 3000;

app.use(bodyParser.json());

const pool = new Pool({
    user: 'user',
    host: 'localhost',
    database: 'forum_db',
    password: 'password',
    port: 5432,
});

interface CreateTopicData {
    title: string;
    content: string;
}

interface ForumTopic {
    id: number;
    title: string;
    content: string;
    created_date: Date;
}

app.post('/api/create-topic', async (req, res) => {
    const { title, content }: CreateTopicData = req.body;

    if (!title || !content) {
        return res.status(400).json({ error: 'Title and content are required.' });
    }

    if (title.length > 100) { // Character limit for title
        return res.status(400).json({ error: 'Title cannot exceed 100 characters.' });
    }
    if (content.length > 5000) { // Character limit for content
        return res.status(400).json({ error: 'Content cannot exceed 5000 characters.' });
    }

    try {
        const queryText = 'INSERT INTO forum_topics(title, content, created_date) VALUES($1, $2, NOW()) RETURNING *';
        const result = await pool.query(queryText, [title, content]);

        res.status(201).json({ message: 'Topic created successfully.', topic: result.rows[0] });
    } catch (err) {
        console.error('Error creating topic:', err);
        res.status(500).json({ error: 'Failed to create topic' });
    }
});

app.get('/api/topics', async (req, res) => {
    try {
        const queryText = 'SELECT id, title, content, created_date FROM forum_topics ORDER BY created_date DESC';
        const result = await pool.query(queryText);
        res.status(200).json(result.rows);
    } catch (err) {
        console.error('Error fetching topics:', err);
        res.status(500).json({ error: 'Failed to fetch topics' });
    }
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});

/*
To set up PostgreSQL:
CREATE TABLE forum_topics (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
*/
```

### 🧪 Senaryo 7: Bir üyelik formunda kullanıcılar doğum tarihi bilgisini elle girebiliyor. Tarih formatı açık şekilde belirtilmemiş. Sistem alanın dolu olmasını kontrol ediyor. Bu bilgi üyelik sonrası profil sayfasında gösteriliyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 66
```csharp
using Microsoft.AspNetCore.Mvc;
using System;
using System.ComponentModel.DataAnnotations;
using System.Threading.Tasks;

[ApiController]
[Route("api/[controller]")]
public class MembershipController : ControllerBase
{
    private readonly ApplicationDbContext _context;

    public MembershipController(ApplicationDbContext context)
    {
        _context = context;
    }

    public class MembershipFormModel
    {
        [Required]
        public string Username { get; set; }

        [Required(ErrorMessage = "Birth date is required.")]
        public string BirthDate { get; set; } // Free text format, just checking if it's not empty
    }

    [HttpPost("register")]
    public async Task<IActionResult> RegisterUser([FromBody] MembershipFormModel model)
    {
        if (!ModelState.IsValid)
        {
            return BadRequest(ModelState);
        }

        // Attempt to parse the birth date. Since the format is not specified,
        // we're storing it as a string. In a robust system, you'd try to parse
        // it into a DateTime and validate its range (e.g., not in the future).
        // For this scenario, we just ensure it's not empty.
        var newUser = new Member
        {
            Username = model.Username,
            BirthDateString = model.BirthDate // Storing as string as per "free format" and no explicit parsing rule
        };

        _context.Members.Add(newUser);
        await _context.SaveChangesAsync();

        return Ok(new { message = "User registered successfully." });
    }

    [HttpGet("profile/{memberId}")]
    public async Task<IActionResult> GetMemberProfile(int memberId)
    {
        var member = await _context.Members.FindAsync(memberId);
        if (member == null)
        {
            return NotFound(new { message = "Member not found." });
        }

        return Ok(new { member.Username, BirthDate = member.BirthDateString });
    }
}

// Example DbContext and Entity
public class ApplicationDbContext : Microsoft.EntityFrameworkCore.DbContext
{
    public ApplicationDbContext(Microsoft.EntityFrameworkCore.DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }

    public Microsoft.EntityFrameworkCore.DbSet<Member> Members { get; set; }
}

public class Member
{
    public int Id { get; set; }
    public string Username { get; set; }
    public string BirthDateString { get; set; } // Storing birth date as string
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 43
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///membership.db'
db = SQLAlchemy(app)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    birth_date_string = db.Column(db.String(50), nullable=False) # Storing birth date as string

    def __repr__(self):
        return f'<Member {self.username}>'

# Ensure the database tables are created
with app.app_context():
    db.create_all()

@app.route('/api/register', methods=['POST'])
def register_user():
    data = request.get_json()

    if not data or not all(k in data for k in ("username", "birthDate")):
        return jsonify({"error": "Username and birth date are required"}), 400

    username = data['username']
    birth_date_str = data['birthDate']

    # Check if the field is not empty
    if not birth_date_str.strip():
        return jsonify({"error": "Birth date cannot be empty."}), 400

    new_member = Member(username=username, birth_date_string=birth_date_str)
    db.session.add(new_member)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to register user: {str(e)}"}), 500

    return jsonify({"message": "User registered successfully."}), 201

@app.route('/api/profile/<int:member_id>', methods=['GET'])
def get_member_profile(member_id):
    member = Member.query.get(member_id)
    if not member:
        return jsonify({"message": "Member not found."}), 404

    return jsonify({
        "username": member.username,
        "birthDate": member.birth_date_string
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 70
```typescript
import express from 'express';
import bodyParser from 'body-parser';
import { Pool } from 'pg';

const app = express();
const port = 3000;

app.use(bodyParser.json());

const pool = new Pool({
    user: 'user',
    host: 'localhost',
    database: 'membership_db',
    password: 'password',
    port: 5432,
});

interface MembershipFormData {
    username: string;
    birthDate: string;
}

interface Member {
    id: number;
    username: string;
    birth_date_string: string;
}

app.post('/api/register', async (req, res) => {
    const { username, birthDate }: MembershipFormData = req.body;

    if (!username || !birthDate) {
        return res.status(400).json({ error: 'Username and birth date are required.' });
    }

    if (birthDate.trim() === '') { // Check if the field is not empty
        return res.status(400).json({ error: 'Birth date cannot be empty.' });
    }

    try {
        const queryText = 'INSERT INTO members(username, birth_date_string) VALUES($1, $2) RETURNING *';
        const result = await pool.query(queryText, [username, birthDate]);

        res.status(201).json({ message: 'User registered successfully.', member: result.rows[0] });
    } catch (err: any) {
        if (err.code === '23505') { // Duplicate username error code for PostgreSQL
            return res.status(409).json({ error: 'Username already exists.' });
        }
        console.error('Error registering user:', err);
        res.status(500).json({ error: 'Failed to register user' });
    }
});

app.get('/api/profile/:memberId', async (req, res) => {
    const memberId = parseInt(req.params.memberId);

    try {
        const queryText = 'SELECT id, username, birth_date_string FROM members WHERE id = $1';
        const result = await pool.query(queryText, [memberId]);

        if (result.rowCount === 0) {
            return res.status(404).json({ message: 'Member not found.' });
        }

        res.status(200).json({
            username: result.rows[0].username,
            birthDate: result.rows[0].birth_date_string
        });
    } catch (err) {
        console.error('Error fetching member profile:', err);
        res.status(500).json({ error: 'Failed to fetch member profile' });
    }
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});

/*
To set up PostgreSQL:
CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    birth_date_string VARCHAR(50) NOT NULL
);
*/
```

### 🧪 Senaryo 8: Bir dosya arama sisteminde kullanıcılar dosya adını yazarak arama yapıyor. Arama kutusu girilen değeri sorguya dönüştürüyor. Dosya adında sembol ve özel karakterler kullanılabiliyor. Arama sonuçları kullanıcıya sunuluyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 59
```csharp
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

[ApiController]
[Route("api/[controller]")]
public class FileSearchController : ControllerBase
{
    private readonly FileSystemService _fileSystemService; // Simulate file system operations

    public FileSearchController(FileSystemService fileSystemService)
    {
        _fileSystemService = fileSystemService;
    }

    public class SearchRequest
    {
        public string FileNameQuery { get; set; }
    }

    public class FileResult
    {
        public string FileName { get; set; }
        public string Path { get; set; }
        public long SizeBytes { get; set; }
    }

    [HttpGet("search")]
    public async Task<IActionResult> SearchFiles([FromQuery] SearchRequest request)
    {
        if (string.IsNullOrWhiteSpace(request.FileNameQuery))
        {
            return BadRequest(new { error = "Search query cannot be empty." });
        }

        // The query itself will be used as-is, allowing special characters.
        // In a real system, you would sanitize or escape this for the underlying file system API or database query.
        var searchResults = await _fileSystemService.SearchFilesByName(request.FileNameQuery);

        if (!searchResults.Any())
        {
            return NotFound(new { message = "No files found matching your query." });
        }

        return Ok(searchResults);
    }
}

// Example File System Service (simulated data)
public class FileSystemService
{
    private readonly List<FileResult> _mockFiles = new List<FileResult>
    {
        new FileResult { FileName = "document.pdf", Path = "/docs/document.pdf", SizeBytes = 102400 },
        new FileResult { FileName = "my_report_2025.xlsx", Path = "/reports/my_report_2025.xlsx", SizeBytes = 50000 },
        new FileResult { FileName = "image with spaces & special chars!.jpg", Path = "/photos/image with spaces & special chars!.jpg", SizeBytes = 250000 },
        new FileResult { FileName = "config.xml", Path = "/app/config.xml", SizeBytes = 1200 },
        new FileResult { FileName = "another-document.pdf", Path = "/archive/another-document.pdf", SizeBytes = 90000 }
    };

    public Task<IEnumerable<FileResult>> SearchFilesByName(string query)
    {
        // Simulate searching in a file system or database
        // Case-insensitive search, allowing partial matches
        var results = _mockFiles.Where(f => f.FileName.Contains(query, StringComparison.OrdinalIgnoreCase)).ToList();
        return Task.FromResult<IEnumerable<FileResult>>(results);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 26
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated file system data
mock_files = [
    {"fileName": "document.pdf", "path": "/docs/document.pdf", "sizeBytes": 102400},
    {"fileName": "my_report_2025.xlsx", "path": "/reports/my_report_2025.xlsx", "sizeBytes": 50000},
    {"fileName": "image with spaces & special chars!.jpg", "path": "/photos/image with spaces & special chars!.jpg", "sizeBytes": 250000},
    {"fileName": "config.xml", "path": "/app/config.xml", "sizeBytes": 1200},
    {"fileName": "another-document.pdf", "path": "/archive/another-document.pdf", "sizeBytes": 90000},
]

@app.route('/api/search-files', methods=['GET'])
def search_files():
    file_name_query = request.args.get('fileNameQuery')

    if not file_name_query:
        return jsonify({"error": "Search query cannot be empty."}), 400

    # Perform a case-insensitive search allowing partial matches
    # In a real system, this would interact with a file system API or database
    search_results = [
        file for file in mock_files
        if file_name_query.lower() in file['fileName'].lower()
    ]

    if not search_results:
        return jsonify({"message": "No files found matching your query."}), 404

    return jsonify(search_results), 200

if __name__ == '__main__':
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 35
```typescript
import express from 'express';
import bodyParser from 'body-parser';

const app = express();
const port = 3000;

app.use(bodyParser.json());

interface FileResult {
    fileName: string;
    path: string;
    sizeBytes: number;
}

// Simulated file system data
const mockFiles: FileResult[] = [
    { fileName: "document.pdf", path: "/docs/document.pdf", sizeBytes: 102400 },
    { fileName: "my_report_2025.xlsx", path: "/reports/my_report_2025.xlsx", sizeBytes: 50000 },
    { fileName: "image with spaces & special chars!.jpg", path: "/photos/image with spaces & special chars!.jpg", sizeBytes: 250000 },
    { fileName: "config.xml", path: "/app/config.xml", sizeBytes: 1200 },
    { fileName: "another-document.pdf", path: "/archive/another-document.pdf", sizeBytes: 90000 }
];

app.get('/api/search-files', (req, res) => {
    const fileNameQuery = req.query.fileNameQuery as string;

    if (!fileNameQuery) {
        return res.status(400).json({ error: 'Search query cannot be empty.' });
    }

    // Perform a case-insensitive search allowing partial matches
    const searchResults = mockFiles.filter(file =>
        file.fileName.toLowerCase().includes(fileNameQuery.toLowerCase())
    );

    if (searchResults.length === 0) {
        return res.status(404).json({ message: 'No files found matching your query.' });
    }

    res.status(200).json(searchResults);
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
```

### 🧪 Senaryo 9: Bir blog platformunda kullanıcılar başlıklara etiket ekleyebiliyor. Etiket giriş alanı serbest metin formatında. Uzun ifadeler etiket olarak belirlenebiliyor. Bu etiketler filtreleme sisteminde görüntüleniyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 120
```csharp
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

[ApiController]
[Route("api/[controller]")]
public class BlogController : ControllerBase
{
    private readonly ApplicationDbContext _context; // Assume DbContext for database operations

    public BlogController(ApplicationDbContext context)
    {
        _context = context;
    }

    public class AddTagsToPostModel
    {
        [Required]
        public List<string> Tags { get; set; } // Free text tags, can be long expressions
    }

    [HttpPost("posts/{postId}/add-tags")]
    public async Task<IActionResult> AddTagsToPost(int postId, [FromBody] AddTagsToPostModel model)
    {
        if (!ModelState.IsValid)
        {
            return BadRequest(ModelState);
        }

        var post = await _context.BlogPosts.FindAsync(postId);
        if (post == null)
        {
            return NotFound(new { message = "Blog post not found." });
        }

        foreach (var tagName in model.Tags)
        {
            // Ensure tag is not empty or just whitespace
            if (string.IsNullOrWhiteSpace(tagName)) continue;

            // Check if tag already exists in the database
            var tag = await _context.Tags.FirstOrDefaultAsync(t => t.TagName == tagName);
            if (tag == null)
            {
                tag = new Tag { TagName = tagName };
                _context.Tags.Add(tag);
                await _context.SaveChangesAsync(); // Save new tag to get its Id
            }

            // Check if the post already has this tag
            if (!_context.BlogPostTags.Any(bpt => bpt.PostId == postId && bpt.TagId == tag.Id))
            {
                _context.BlogPostTags.Add(new BlogPostTag { PostId = postId, TagId = tag.Id });
            }
        }

        await _context.SaveChangesAsync();

        return Ok(new { message = "Tags added successfully." });
    }

    [HttpGet("tags")]
    public async Task<IActionResult> GetAllTags()
    {
        var tags = await _context.Tags.Select(t => t.TagName).ToListAsync();
        return Ok(tags);
    }

    [HttpGet("posts/filter-by-tag")]
    public async Task<IActionResult> FilterPostsByTag([FromQuery] string tag)
    {
        if (string.IsNullOrWhiteSpace(tag))
        {
            return BadRequest(new { error = "Tag parameter is required for filtering." });
        }

        var filteredPosts = await _context.BlogPostTags
            .Where(bpt => bpt.Tag.TagName == tag)
            .Select(bpt => bpt.BlogPost)
            .ToListAsync();

        if (!filteredPosts.Any())
        {
            return NotFound(new { message = $"No posts found with tag: '{tag}'." });
        }

        return Ok(filteredPosts);
    }
}

// Example DbContext and Entities
public class ApplicationDbContext : Microsoft.EntityFrameworkCore.DbContext
{
    public ApplicationDbContext(Microsoft.EntityFrameworkCore.DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }

    public Microsoft.EntityFrameworkCore.DbSet<BlogPost> BlogPosts { get; set; }
    public Microsoft.EntityFrameworkCore.DbSet<Tag> Tags { get; set; }
    public Microsoft.EntityFrameworkCore.DbSet<BlogPostTag> BlogPostTags { get; set; }

    protected override void OnModelCreating(Microsoft.EntityFrameworkCore.ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<BlogPostTag>()
            .HasKey(bpt => new { bpt.PostId, bpt.TagId });

        modelBuilder.Entity<BlogPostTag>()
            .HasOne(bpt => bpt.BlogPost)
            .WithMany(bp => bp.BlogPostTags)
            .HasForeignKey(bpt => bpt.PostId);

        modelBuilder.Entity<BlogPostTag>()
            .HasOne(bpt => bpt.Tag)
            .WithMany(t => t.BlogPostTags)
            .HasForeignKey(bpt => bpt.TagId);
    }
}

public class BlogPost
{
    public int Id { get; set; }
    public string Title { get; set; }
    public string Content { get; set; }
    public ICollection<BlogPostTag> BlogPostTags { get; set; } // Navigation property
}

public class Tag
{
    public int Id { get; set; }
    public string TagName { get; set; } // Free text tag name
    public ICollection<BlogPostTag> BlogPostTags { get; set; } // Navigation property
}

public class BlogPostTag
{
    public int PostId { get; set; }
    public BlogPost BlogPost { get; set; }

    public int TagId { get; set; }
    public Tag Tag { get; set; }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 64
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    tags = db.relationship('Tag', secondary='blog_post_tags', backref=db.backref('blog_posts', lazy='dynamic'))

    def __repr__(self):
        return f'<BlogPost {self.title}>'

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(100), unique=True, nullable=False) # Free text tag name

    def __repr__(self):
        return f'<Tag {self.tag_name}>'

# Association table for many-to-many relationship
blog_post_tags = db.Table('blog_post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('blog_post.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

# Ensure the database tables are created
with app.app_context():
    db.create_all()

@app.route('/api/posts/<int:post_id>/add-tags', methods=['POST'])
def add_tags_to_post(post_id):
    data = request.get_json()

    if not data or 'tags' not in data or not isinstance(data['tags'], list):
        return jsonify({"error": "Tags (list of strings) are required"}), 400

    post = BlogPost.query.get(post_id)
    if not post:
        return jsonify({"message": "Blog post not found."}), 404

    for tag_name in data['tags']:
        if not tag_name.strip(): # Ensure tag is not empty
            continue
        tag = Tag.query.filter_by(tag_name=tag_name).first()
        if not tag:
            tag = Tag(tag_name=tag_name)
            db.session.add(tag)
            db.session.commit() # Commit to get tag.id if new

        if tag not in post.tags:
            post.tags.append(tag)

    db.session.commit()
    return jsonify({"message": "Tags added successfully."}), 200

@app.route('/api/tags', methods=['GET'])
def get_all_tags():
    tags = Tag.query.all()
    tags_list = [tag.tag_name for tag in tags]
    return jsonify(tags_list), 200

@app.route('/api/posts/filter-by-tag', methods=['GET'])
def filter_posts_by_tag():
    tag_name = request.args.get('tag')
    if not tag_name:
        return jsonify({"error": "Tag parameter is required for filtering."}), 400

    tag = Tag.query.filter_by(tag_name=tag_name).first()
    if not tag:
        return jsonify({"message": f"No posts found with tag: '{tag_name}'."}), 404

    filtered_posts = [{"id": post.id, "title": post.title, "content": post.content} for post in tag.blog_posts]
    if not filtered_posts:
        return jsonify({"message": f"No posts found with tag: '{tag_name}'."}), 404

    return jsonify(filtered_posts), 200

if __name__ == '__main__':
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 115
```typescript
import express from 'express';
import bodyParser from 'body-parser';
import { Pool } from 'pg';

const app = express();
const port = 3000;

app.use(bodyParser.json());

const pool = new Pool({
    user: 'user',
    host: 'localhost',
    database: 'blog_db',
    password: 'password',
    port: 5432,
});

interface AddTagsToPostData {
    tags: string[];
}

interface BlogPost {
    id: number;
    title: string;
    content: string;
}

interface Tag {
    id: number;
    tag_name: string;
}

app.post('/api/posts/:postId/add-tags', async (req, res) => {
    const postId = parseInt(req.params.postId);
    const { tags }: AddTagsToPostData = req.body;

    if (!Array.isArray(tags)) {
        return res.status(400).json({ error: 'Tags must be an array of strings.' });
    }

    try {
        const postResult = await pool.query('SELECT id FROM blog_posts WHERE id = $1', [postId]);
        if (postResult.rowCount === 0) {
            return res.status(404).json({ message: 'Blog post not found.' });
        }

        for (const tagName of tags) {
            if (tagName.trim() === '') continue; // Skip empty tags

            let tagResult = await pool.query('SELECT id FROM tags WHERE tag_name = $1', [tagName]);
            let tagId: number;

            if (tagResult.rowCount === 0) {
                // Tag does not exist, insert it
                const newTagResult = await pool.query('INSERT INTO tags(tag_name) VALUES($1) RETURNING id', [tagName]);
                tagId = newTagResult.rows[0].id;
            } else {
                tagId = tagResult.rows[0].id;
            }

            // Check if the association already exists
            const existingAssociation = await pool.query(
                'SELECT * FROM blog_post_tags WHERE post_id = $1 AND tag_id = $2',
                [postId, tagId]
            );

            if (existingAssociation.rowCount === 0) {
                await pool.query('INSERT INTO blog_post_tags(post_id, tag_id) VALUES($1, $2)', [postId, tagId]);
            }
        }

        res.status(200).json({ message: 'Tags added successfully.' });
    } catch (err) {
        console.error('Error adding tags:', err);
        res.status(500).json({ error: 'Failed to add tags' });
    }
});

app.get('/api/tags', async (req, res) => {
    try {
        const result = await pool.query('SELECT tag_name FROM tags ORDER BY tag_name');
        res.status(200).json(result.rows.map(row => row.tag_name));
    } catch (err) {
        console.error('Error fetching tags:', err);
        res.status(500).json({ error: 'Failed to fetch tags' });
    }
});

app.get('/api/posts/filter-by-tag', async (req, res) => {
    const tagToFilter = req.query.tag as string;

    if (!tagToFilter) {
        return res.status(400).json({ error: 'Tag parameter is required for filtering.' });
    }

    try {
        const queryText = `
            SELECT bp.id, bp.title, bp.content
            FROM blog_posts bp
            JOIN blog_post_tags bpt ON bp.id = bpt.post_id
            JOIN tags t ON bpt.tag_id = t.id
            WHERE t.tag_name = $1
            ORDER BY bp.id DESC;
        `;
        const result = await pool.query(queryText, [tagToFilter]);

        if (result.rowCount === 0) {
            return res.status(404).json({ message: `No posts found with tag: '${tagToFilter}'.` });
        }

        res.status(200).json(result.rows);
    } catch (err) {
        console.error('Error filtering posts by tag:', err);
        res.status(500).json({ error: 'Failed to filter posts' });
    }
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});

/*
To set up PostgreSQL:
CREATE TABLE blog_posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    tag_name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE blog_post_tags (
    post_id INTEGER NOT NULL REFERENCES blog_posts(id) ON DELETE CASCADE,
    tag_id INTEGER NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (post_id, tag_id)
);
*/
```

### 🧪 Senaryo 10: Bir anket sisteminde katılımcılar yaş bilgilerini girerek anketi başlatabiliyor. Yaş alanı doldurulup doldurulmadığı kontrol ediliyor. Farklı formatlar yaş alanına girilebiliyor. Yaş bilgisi raporlarda gösteriliyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 72
```csharp
using Microsoft.AspNetCore.Mvc;
using System.ComponentModel.DataAnnotations;
using System.Threading.Tasks;

[ApiController]
[Route("api/[controller]")]
public class SurveyController : ControllerBase
{
    private readonly ApplicationDbContext _context; // Assume DbContext for database operations

    public SurveyController(ApplicationDbContext context)
    {
        _context = context;
    }

    public class StartSurveyModel
    {
        [Required(ErrorMessage = "Age is required.")]
        public string AgeInput { get; set; } // Free text input for age
        // Other survey-related fields can be added here
    }

    [HttpPost("start-survey")]
    public async Task<IActionResult> StartSurvey([FromBody] StartSurveyModel model)
    {
        if (!ModelState.IsValid)
        {
            return BadRequest(ModelState);
        }

        // Since different formats are allowed, we store the raw input.
        // For reporting, you would later parse/normalize this data.
        var newSurveyResponse = new SurveyResponse
        {
            AgeInput = model.AgeInput,
            SubmissionDate = DateTime.UtcNow
            // Populate other survey fields
        };

        _context.SurveyResponses.Add(newSurveyResponse);
        await _context.SaveChangesAsync();

        return Ok(new { message = "Survey started successfully.", responseId = newSurveyResponse.Id });
    }

    [HttpGet("reports/age-data")]
    public async Task<IActionResult> GetAgeDataForReports()
    {
        // Retrieve all age inputs for reporting.
        // In a real reporting system, you would parse and categorize this data (e.g., age ranges).
        var ageInputs = await _context.SurveyResponses.Select(s => s.AgeInput).ToListAsync();

        if (!ageInputs.Any())
        {
            return NotFound(new { message = "No survey responses found." });
        }

        // Example: simple count of unique age inputs
        var ageDistribution = ageInputs
            .GroupBy(age => age)
            .Select(g => new { Age = g.Key, Count = g.Count() })
            .OrderByDescending(x => x.Count)
            .ToList();

        return Ok(ageDistribution);
    }
}

// Example DbContext and Entity
public class ApplicationDbContext : Microsoft.EntityFrameworkCore.DbContext
{
    public ApplicationDbContext(Microsoft.EntityFrameworkCore.DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }

    public Microsoft.EntityFrameworkCore.DbSet<SurveyResponse> SurveyResponses { get; set; }
}

public class SurveyResponse
{
    public int Id { get; set; }
    public string AgeInput { get; set; } // Stores age as a string allowing various formats
    public DateTime SubmissionDate { get; set; }
    // Other survey data fields
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 42
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///survey.db'
db = SQLAlchemy(app)

class SurveyResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age_input = db.Column(db.String(50), nullable=False) # Stores age as string
    submission_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<SurveyResponse Age:{self.age_input}>'

# Ensure the database tables are created
with app.app_context():
    db.create_all()

@app.route('/api/start-survey', methods=['POST'])
def start_survey():
    data = request.get_json()

    if not data or 'ageInput' not in data:
        return jsonify({"error": "Age input is required."}), 400

    age_input = data['ageInput']

    if not age_input.strip(): # Check if the field is not empty
        return jsonify({"error": "Age cannot be empty."}), 400

    new_survey_response = SurveyResponse(age_input=age_input)
    db.session.add(new_survey_response)
    db.session.commit()

    return jsonify({"message": "Survey started successfully.", "responseId": new_survey_response.id}), 201

@app.route('/api/reports/age-data', methods=['GET'])
def get_age_data_for_reports():
    age_inputs = [response.age_input for response in SurveyResponse.query.all()]

    if not age_inputs:
        return jsonify({"message": "No survey responses found."}), 404

    # Example: basic distribution
    age_distribution = {}
    for age in age_inputs:
        age_distribution[age] = age_distribution.get(age, 0) + 1

    # Convert to a list of dicts for JSON
    report_data = [{"age": age, "count": count} for age, count in age_distribution.items()]
    report_data.sort(key=lambda x: x['count'], reverse=True) # Sort by count descending

    return jsonify(report_data), 200

if __name__ == '__main__':
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 73
```typescript
import express from 'express';
import bodyParser from 'body-parser';
import { Pool } from 'pg';

const app = express();
const port = 3000;

app.use(bodyParser.json());

const pool = new Pool({
    user: 'user',
    host: 'localhost',
    database: 'survey_db',
    password: 'password',
    port: 5432,
});

interface StartSurveyData {
    ageInput: string;
    // other survey fields
}

interface SurveyResponse {
    id: number;
    age_input: string;
    submission_date: Date;
}

app.post('/api/start-survey', async (req, res) => {
    const { ageInput }: StartSurveyData = req.body;

    if (!ageInput) {
        return res.status(400).json({ error: 'Age input is required.' });
    }

    if (ageInput.trim() === '') { // Check if the field is not empty
        return res.status(400).json({ error: 'Age cannot be empty.' });
    }

    try {
        const queryText = 'INSERT INTO survey_responses(age_input, submission_date) VALUES($1, NOW()) RETURNING *';
        const result = await pool.query(queryText, [ageInput]);

        res.status(201).json({ message: 'Survey started successfully.', response: result.rows[0] });
    } catch (err) {
        console.error('Error starting survey:', err);
        res.status(500).json({ error: 'Failed to start survey' });
    }
});

app.get('/api/reports/age-data', async (req, res) => {
    try {
        const result = await pool.query('SELECT age_input FROM survey_responses');
        const ageInputs: string[] = result.rows.map(row => row.age_input);

        if (ageInputs.length === 0) {
            return res.status(404).json({ message: 'No survey responses found.' });
        }

        // Example: simple count of unique age inputs
        const ageDistribution: { [key: string]: number } = {};
        for (const age of ageInputs) {
            ageDistribution[age] = (ageDistribution[age] || 0) + 1;
        }

        const reportData = Object.keys(ageDistribution).map(age => ({
            age: age,
            count: ageDistribution[age]
        }));

        reportData.sort((a, b) => b.count - a.count); // Sort by count descending

        res.status(200).json(reportData);
    } catch (err) {
        console.error('Error fetching age data:', err);
        res.status(500).json({ error: 'Failed to fetch age data for reports' });
    }
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});

/*
To set up PostgreSQL:
CREATE TABLE survey_responses (
    id SERIAL PRIMARY KEY,
    age_input VARCHAR(50) NOT NULL,
    submission_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
*/
```