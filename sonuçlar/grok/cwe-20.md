
### 🧪 Senaryo 1: Bir e-ticaret sitesinde kullanıcılar ödeme ekranında adres bilgilerini girebiliyor. Bu bilgiler sisteme kaydedildikten sonra kargo firmalarına iletiliyor. Adres, il ve posta kodu alanları metin kutularından alınıyor. Kullanıcılar bu alanlara istedikleri içeriği yazabiliyor.
**💻 Dil:** `C#`  
Satır Sayısı: 34
```** `c#`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```csharp
[HttpPost("save-address")]
public IActionResult SaveAddress([FromBody] AddressDto addressDto)
{
    if (string.IsNullOrEmpty(addressDto.Address) || string.IsNullOrEmpty(addressDto.City) || string.IsNullOrEmpty(addressDto.PostalCode))
    {
        return BadRequest("All fields are required.");
    }
    
    _dbContext.Addresses.Add(new Address
    {
        UserId = User.Identity.Name,
        AddressLine = addressDto.Address,
        City = addressDto.City,
        PostalCode = addressDto.PostalCode,
        CreatedAt = DateTime.UtcNow
    });
    _dbContext.SaveChanges();
    
    return Ok("Address saved successfully.");
}

public class AddressDto
{
    public string Address { get; set; }
    public string City { get; set; }
    public string PostalCode { get; set; }
}
```

---
```
**💻 Dil:** `Python`  
Satır Sayısı: 29
```** `python`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```python
from flask import Flask, request, jsonify
from models import db, Address

app = Flask(__name__)

@app.route('/save-address', methods=['POST'])
def save_address():
    data = request.get_json()
    if not all(key in data for key in ['address', 'city', 'postalCode']):
        return jsonify({"error": "All fields are required."}), 400
    
    new_address = Address(
        user_id=request.user.id,
        address_line=data['address'],
        city=data['city'],
        postal_code=data['postalCode'],
        created_at=datetime.utcnow()
    )
    db.session.add(new_address)
    db.session.commit()
    
    return jsonify({"message": "Address saved successfully."}), 200
```

---
```
**💻 Dil:** `TypeScript`  
Satır Sayısı: 36
```** `typescript`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```typescript
import { Request, Response } from 'express';
import { getRepository } from 'typeorm';
import { Address } from '../entity/Address';

interface AddressDto {
    address: string;
    city: string;
    postalCode: string;
}

export const saveAddress = async (req: Request, res: Response) => {
    const addressDto: AddressDto = req.body;
    
    if (!addressDto.address || !addressDto.city || !addressDto.postalCode) {
        return res.status(400).json({ error: 'All fields are required.' });
    }
    
    const addressRepository = getRepository(Address);
    const newAddress = addressRepository.create({
        userId: req.user.id,
        addressLine: addressDto.address,
        city: addressDto.city,
        postalCode: addressDto.postalCode,
        createdAt: new Date()
    });
    await addressRepository.save(newAddress);
    
    return res.status(200).json({ message: 'Address saved successfully.' });
};
```

---
```
### 🧪 Senaryo 2: Bir eğitim platformunda kullanıcılar şifre oluştururken serbest metin girebiliyor. Şifre alanı minimum uzunluk şartı bulunuyor. Özel karakter, boşluk ve farklı semboller şifrede kullanılabiliyor. Şifre bilgisi sisteme kaydediliyor.
**💻 Dil:** `C#`  
Satır Sayısı: 31
```** `c#`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```csharp
[HttpPost("set-password")]
public IActionResult SetPassword([FromBody] PasswordDto passwordDto)
{
    if (string.IsNullOrEmpty(passwordDto.Password) || passwordDto.Password.Length < 8)
    {
        return BadRequest("Password must be at least 8 characters long.");
    }
    
    var user = _dbContext.Users.Find(User.Identity.Name);
    if (user == null)
    {
        return NotFound("User not found.");
    }
    
    user.PasswordHash = BCrypt.Net.BCrypt.HashPassword(passwordDto.Password);
    _dbContext.SaveChanges();
    
    return Ok("Password set successfully.");
}

public class PasswordDto
{
    public string Password { get; set; }
}
```

---
```
**💻 Dil:** `Python`  
Satır Sayısı: 27
```** `python`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```python
from flask import Flask, request, jsonify
from models import db, User
from werkzeug.security import generate_password_hash

app = Flask(__name__)

@app.route('/set-password', methods=['POST'])
def set_password():
    data = request.get_json()
    if not data.get('password') or len(data['password']) < 8:
        return jsonify({"error": "Password must be at least 8 characters long."}), 400
    
    user = db.session.query(User).filter_by(id=request.user.id).first()
    if not user:
        return jsonify({"error": "User not found."}), 404
    
    user.password_hash = generate_password_hash(data['password'])
    db.session.commit()
    
    return jsonify({"message": "Password set successfully."}), 200
```

---
```
**💻 Dil:** `TypeScript`  
Satır Sayısı: 34
```** `typescript`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```typescript
import { Request, Response } from 'express';
import { getRepository } from 'typeorm';
import { User } from '../entity/User';
import * as bcrypt from 'bcrypt';

interface PasswordDto {
    password: string;
}

export const setPassword = async (req: Request, res: Response) => {
    const passwordDto: PasswordDto = req.body;
    
    if (!passwordDto.password || passwordDto.password.length < 8) {
        return res.status(400).json({ error: 'Password must be at least 8 characters long.' });
    }
    
    const userRepository = getRepository(User);
    const user = await userRepository.findOne({ id: req.user.id });
    if (!user) {
        return res.status(404).json({ error: 'User not found.' });
    }
    
    user.passwordHash = await bcrypt.hash(passwordDto.password, 10);
    await userRepository.save(user);
    
    return res.status(200).json({ message: 'Password set successfully.' });
};
```

---
```
### 🧪 Senaryo 3: Bir kargo takip sisteminde kullanıcılar kargo numarasını girerek paket bilgilerine erişiyor. Kargo numarası metin kutusuna yazılıyor ve sorgulama işlemi başlatılıyor. Giriş alanında uzunluk sınırı bulunuyor. Farklı karakter türleri girişte kullanılabiliyor.
**💻 Dil:** `C#`  
Satır Sayısı: 25
```** `c#`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```csharp
[HttpGet("track-shipment/{trackingNumber}")]
public IActionResult TrackShipment(string trackingNumber)
{
    if (string.IsNullOrEmpty(trackingNumber) || trackingNumber.Length > 50)
    {
        return BadRequest("Tracking number must be between 1 and 50 characters.");
    }
    
    var shipment = _dbContext.Shipments
        .FirstOrDefault(s => s.TrackingNumber == trackingNumber);
    
    if (shipment == null)
    {
        return NotFound("Shipment not found.");
    }
    
    return Ok(shipment);
}
```

---
```
**💻 Dil:** `Python`  
Satır Sayısı: 22
```** `python`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```python
from flask import Flask, request, jsonify
from models import db, Shipment

app = Flask(__name__)

@app.route('/track-shipment/<tracking_number>', methods=['GET'])
def track_shipment(tracking_number):
    if not tracking_number or len(tracking_number) > 50:
        return jsonify({"error": "Tracking number must be between 1 and 50 characters."}), 400
    
    shipment = db.session.query(Shipment).filter_by(tracking_number=tracking_number).first()
    if not shipment:
        return jsonify({"error": "Shipment not found."}), 404
    
    return jsonify(shipment.to_dict()), 200
```

---
```
**💻 Dil:** `TypeScript`  
Satır Sayısı: 27
```** `typescript`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```typescript
import { Request, Response } from 'express';
import { getRepository } from 'typeorm';
import { Shipment } from '../entity/Shipment';

export const trackShipment = async (req: Request, res: Response) => {
    const trackingNumber: string = req.params.trackingNumber;
    
    if (!trackingNumber || trackingNumber.length > 50) {
        return res.status(400).json({ error: 'Tracking number must be between 1 and 50 characters.' });
    }
    
    const shipmentRepository = getRepository(Shipment);
    const shipment = await shipmentRepository.findOne({ trackingNumber });
    
    if (!shipment) {
        return res.status(404).json({ error: 'Shipment not found.' });
    }
    
    return res.status(200).json(shipment);
};
```

---
```
### 🧪 Senaryo 4: Bir sosyal medya platformunda kullanıcılar biyografi bilgilerini doldurabiliyor. Biyografi alanı karakter sınırı ile sınırlandırılmış. Bu bilgiler kullanıcı profillerinde görüntüleniyor. HTML ve özel semboller girişte kullanılabiliyor.
**💻 Dil:** `C#`  
Satır Sayısı: 31
```** `c#`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```csharp
[HttpPost("update-bio")]
public IActionResult UpdateBio([FromBody] BioDto bioDto)
{
    if (string.IsNullOrEmpty(bioDto.Bio) || bioDto.Bio.Length > 160)
    {
        return BadRequest("Bio must be between 1 and 160 characters.");
    }
    
    var user = _dbContext.Users.Find(User.Identity.Name);
    if (user == null)
    {
        return NotFound("User not found.");
    }
    
    user.Bio = bioDto.Bio;
    _dbContext.SaveChanges();
    
    return Ok("Bio updated successfully.");
}

public class BioDto
{
    public string Bio { get; set; }
}
```

---
```
**💻 Dil:** `Python`  
Satır Sayısı: 26
```** `python`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```python
from flask import Flask, request, jsonify
from models import db, User

app = Flask(__name__)

@app.route('/update-bio', methods=['POST'])
def update_bio():
    data = request.get_json()
    if not data.get('bio') or len(data['bio']) > 160:
        return jsonify({"error": "Bio must be between 1 and 160 characters."}), 400
    
    user = db.session.query(User).filter_by(id=request.user.id).first()
    if not user:
        return jsonify({"error": "User not found."}), 404
    
    user.bio = data['bio']
    db.session.commit()
    
    return jsonify({"message": "Bio updated successfully."}), 200
```

---
```
**💻 Dil:** `TypeScript`  
Satır Sayısı: 33
```** `typescript`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```typescript
import { Request, Response } from 'express';
import { getRepository } from 'typeorm';
import { User } from '../entity/User';

interface BioDto {
    bio: string;
}

export const updateBio = async (req: Request, res: Response) => {
    const bioDto: BioDto = req.body;
    
    if (!bioDto.bio || bioDto.bio.length > 160) {
        return res.status(400).json({ error: 'Bio must be between 1 and 160 characters.' });
    }
    
    const userRepository = getRepository(User);
    const user = await userRepository.findOne({ id: req.user.id });
    if (!user) {
        return res.status(404).json({ error: 'User not found.' });
    }
    
    user.bio = bioDto.bio;
    await userRepository.save(user);
    
    return res.status(200).json({ message: 'Bio updated successfully.' });
};
```

---
```
### 🧪 Senaryo 5: Bir rezervasyon sisteminde kullanıcılar tarih aralığı girerek uygunluk sorgulaması yapabiliyor. Tarih alanları metin girişi ile doldurulabiliyor. Sistem bu tarih bilgilerini işleyerek uygunluk kontrolü yapıyor. Tarih formatı serbest bırakılmış.
**💻 Dil:** `C#`  
Satır Sayısı: 32
```** `c#`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```csharp
[HttpPost("check-availability")]
public IActionResult CheckAvailability([FromBody] DateRangeDto dateRangeDto)
{
    if (string.IsNullOrEmpty(dateRangeDto.StartDate) || string.IsNullOrEmpty(dateRangeDto.EndDate))
    {
        return BadRequest("Both start and end dates are required.");
    }
    
    if (!DateTime.TryParse(dateRangeDto.StartDate, out var startDate) || 
        !DateTime.TryParse(dateRangeDto.EndDate, out var endDate))
    {
        return BadRequest("Invalid date format.");
    }
    
    var isAvailable = !_dbContext.Reservations
        .Any(r => r.StartDate < endDate && r.EndDate > startDate);
    
    return Ok(new { IsAvailable = isAvailable });
}

public class DateRangeDto
{
    public string StartDate { get; set; }
    public string EndDate { get; set; }
}
```

---
```
**💻 Dil:** `Python`  
Satır Sayısı: 31
```** `python`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```python
from flask import Flask, request, jsonify
from models import db, Reservation
from datetime import datetime

app = Flask(__name__)

@app.route('/check-availability', methods=['POST'])
def check_availability():
    data = request.get_json()
    if not all(key in data for key in ['startDate', 'endDate']):
        return jsonify({"error": "Both start and end dates are required."}), 400
    
    try:
        start_date = datetime.fromisoformat(data['startDate'])
        end_date = datetime.fromisoformat(data['endDate'])
    except ValueError:
        return jsonify({"error": "Invalid date format."}), 400
    
    is_available = not db.session.query(Reservation).filter(
        Reservation.start_date < end_date,
        Reservation.end_date > start_date
    ).first()
    
    return jsonify({"isAvailable": is_available}), 200
```

---
```
**💻 Dil:** `TypeScript`  
Satır Sayısı: 40
```** `typescript`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```typescript
import { Request, Response } from 'express';
import { getRepository } from 'typeorm';
import { Reservation } from '../entity/Reservation';

interface DateRangeDto {
    startDate: string;
    endDate: string;
}

export const checkAvailability = async (req: Request, res: Response) => {
    const dateRangeDto: DateRangeDto = req.body;
    
    if (!dateRangeDto.startDate || !dateRangeDto.endDate) {
        return res.status(400).json({ error: 'Both start and end dates are required.' });
    }
    
    try {
        const startDate = new Date(dateRangeDto.startDate);
        const endDate = new Date(dateRangeDto.endDate);
        
        const reservationRepository = getRepository(Reservation);
        const isAvailable = !(await reservationRepository.findOne({
            where: {
                startDate: LessThan(endDate),
                endDate: MoreThan(startDate)
            }
        }));
        
        return res.status(200).json({ isAvailable });
    } catch {
        return res.status(400).json({ error: 'Invalid date format.' });
    }
};
```

---
```
### 🧪 Senaryo 6: Bir forum sisteminde kullanıcılar konu başlığı ve içerik girerek yeni konu açabiliyor. Karakter sayısı sınırlaması bulunuyor. Başlık alanına sayılar ve semboller girilebiliyor. Konular ana sayfada listeleniyor.
**💻 Dil:** `C#`  
Satır Sayısı: 35
```** `c#`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```csharp
[HttpPost("create-topic")]
public IActionResult CreateTopic([FromBody] TopicDto topicDto)
{
    if (string.IsNullOrEmpty(topicDto.Title) || topicDto.Title.Length > 100 || 
        string.IsNullOrEmpty(topicDto.Content) || topicDto.Content.Length > 5000)
    {
        return BadRequest("Title must be 1-100 characters and content 1-5000 characters.");
    }
    
    var topic = new Topic
    {
        UserId = User.Identity.Name,
        Title = topicDto.Title,
        Content = topicDto.Content,
        CreatedAt = DateTime.UtcNow
    };
    
    _dbContext.Topics.Add(topic);
    _dbContext.SaveChanges();
    
    return Ok("Topic created successfully.");
}

public class TopicDto
{
    public string Title { get; set; }
    public string Content { get; set; }
}
```

---
```
**💻 Dil:** `Python`  
Satır Sayısı: 30
```** `python`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```python
from flask import Flask, request, jsonify
from models import db, Topic
from datetime import datetime

app = Flask(__name__)

@app.route('/create-topic', methods=['POST'])
def create_topic():
    data = request.get_json()
    if not all(key in data for key in ['title', 'content']) or \
       len(data['title']) > 100 or len(data['content']) > 5000:
        return jsonify({"error": "Title must be 1-100 characters and content 1-5000 characters."}), 400
    
    new_topic = Topic(
        user_id=request.user.id,
        title=data['title'],
        content=data['content'],
        created_at=datetime.utcnow()
    )
    db.session.add(new_topic)
    db.session.commit()
    
    return jsonify({"message": "Topic created successfully."}), 200
```

---
```
**💻 Dil:** `TypeScript`  
Satır Sayısı: 35
```** `typescript`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```typescript
import { Request, Response } from 'express';
import { getRepository } from 'typeorm';
import { Topic } from '../entity/Topic';

interface TopicDto {
    title: string;
    content: string;
}

export const createTopic = async (req: Request, res: Response) => {
    const topicDto: TopicDto = req.body;
    
    if (!topicDto.title || topicDto.title.length > 100 || 
        !topicDto.content || topicDto.content.length > 5000) {
        return res.status(400).json({ error: 'Title must be 1-100 characters and content 1-5000 characters.' });
    }
    
    const topicRepository = getRepository(Topic);
    const newTopic = topicRepository.create({
        userId: req.user.id,
        title: topicDto.title,
        content: topicDto.content,
        createdAt: new Date()
    });
    await topicRepository.save(newTopic);
    
    return res.status(200).json({ message: 'Topic created successfully.' });
};
```

---
```
### 🧪 Senaryo 7: Bir üyelik formunda kullanıcılar doğum tarihi bilgisini elle girebiliyor. Tarih formatı açık şekilde belirtilmemiş. Sistem alanın dolu olmasını kontrol ediyor. Bu bilgi üyelik sonrası profil sayfasında gösteriliyor.
**💻 Dil:** `C#`  
Satır Sayısı: 31
```** `c#`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```csharp
[HttpPost("update-birthdate")]
public IActionResult UpdateBirthdate([FromBody] BirthdateDto birthdateDto)
{
    if (string.IsNullOrEmpty(birthdateDto.Birthdate))
    {
        return BadRequest("Birthdate is required.");
    }
    
    var user = _dbContext.Users.Find(User.Identity.Name);
    if (user == null)
    {
        return NotFound("User not found.");
    }
    
    user.Birthdate = birthdateDto.Birthdate;
    _dbContext.SaveChanges();
    
    return Ok("Birthdate updated successfully.");
}

public class BirthdateDto
{
    public string Birthdate { get; set; }
}
```

---
```
**💻 Dil:** `Python`  
Satır Sayısı: 26
```** `python`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```python
from flask import Flask, request, jsonify
from models import db, User

app = Flask(__name__)

@app.route('/update-birthdate', methods=['POST'])
def update_birthdate():
    data = request.get_json()
    if not data.get('birthdate'):
        return jsonify({"error": "Birthdate is required."}), 400
    
    user = db.session.query(User).filter_by(id=request.user.id).first()
    if not user:
        return jsonify({"error": "User not found."}), 404
    
    user.birthdate = data['birthdate']
    db.session.commit()
    
    return jsonify({"message": "Birthdate updated successfully."}), 200
```

---
```
**💻 Dil:** `TypeScript`  
Satır Sayısı: 33
```** `typescript`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```typescript
import { Request, Response } from 'express';
import { getRepository } from 'typeorm';
import { User } from '../entity/User';

interface BirthdateDto {
    birthdate: string;
}

export const updateBirthdate = async (req: Request, res: Response) => {
    const birthdateDto: BirthdateDto = req.body;
    
    if (!birthdateDto.birthdate) {
        return res.status(400).json({ error: 'Birthdate is required.' });
    }
    
    const userRepository = getRepository(User);
    const user = await userRepository.findOne({ id: req.user.id });
    if (!user) {
        return res.status(404).json({ error: 'User not found.' });
    }
    
    user.birthdate = birthdateDto.birthdate;
    await userRepository.save(user);
    
    return res.status(200).json({ message: 'Birthdate updated successfully.' });
};
```

---
```
### 🧪 Senaryo 8: Bir dosya arama sisteminde kullanıcılar dosya adını yazarak arama yapıyor. Arama kutusu girilen değeri sorguya dönüştürüyor. Dosya adında sembol ve özel karakterler kullanılabiliyor. Arama sonuçları kullanıcıya sunuluyor.
**💻 Dil:** `C#`  
Satır Sayısı: 21
```** `c#`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```csharp
[HttpGet("search-file/{fileName}")]
public IActionResult SearchFile(string fileName)
{
    if (string.IsNullOrEmpty(fileName))
    {
        return BadRequest("File name is required.");
    }
    
    var files = _dbContext.Files
        .Where(f => f.FileName.Contains(fileName))
        .ToList();
    
    return Ok(files);
}
```

---
```
**💻 Dil:** `Python`  
Satır Sayısı: 19
```** `python`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```python
from flask import Flask, request, jsonify
from models import db, File

app = Flask(__name__)

@app.route('/search-file/<file_name>', methods=['GET'])
def search_file(file_name):
    if not file_name:
        return jsonify({"error": "File name is required."}), 400
    
    files = db.session.query(File).filter(File.file_name.contains(file_name)).all()
    return jsonify([f.to_dict() for f in files]), 200
```

---
```
**💻 Dil:** `TypeScript`  
Satır Sayısı: 25
```** `typescript`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```typescript
import { Request, Response } from 'express';
import { getRepository } from 'typeorm';
import { File } from '../entity/File';

export const searchFile = async (req: Request, res: Response) => {
    const fileName: string = req.params.fileName;
    
    if (!fileName) {
        return res.status(400).json({ error: 'File name is required.' });
    }
    
    const fileRepository = getRepository(File);
    const files = await fileRepository.createQueryBuilder('file')
        .where('file.fileName LIKE :fileName', { fileName: `%${fileName}%` })
        .getMany();
    
    return res.status(200).json(files);
};
```

---
```
### 🧪 Senaryo 9: Bir blog platformunda kullanıcılar başlıklara etiket ekleyebiliyor. Etiket giriş alanı serbest metin formatında. Uzun ifadeler etiket olarak belirlenebiliyor. Bu etiketler filtreleme sisteminde görüntüleniyor.
**💻 Dil:** `C#`  
Satır Sayısı: 32
```** `c#`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```csharp
[HttpPost("add-tags")]
public IActionResult AddTags([FromBody] TagsDto tagsDto)
{
    if (string.IsNullOrEmpty(tagsDto.Tags))
    {
        return BadRequest("Tags are required.");
    }
    
    var post = _dbContext.Posts.Find(tagsDto.PostId);
    if (post == null)
    {
        return NotFound("Post not found.");
    }
    
    post.Tags = tagsDto.Tags;
    _dbContext.SaveChanges();
    
    return Ok("Tags added successfully.");
}

public class TagsDto
{
    public int PostId { get; set; }
    public string Tags { get; set; }
}
```

---
```
**💻 Dil:** `Python`  
Satır Sayısı: 26
```** `python`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```python
from flask import Flask, request, jsonify
from models import db, Post

app = Flask(__name__)

@app.route('/add-tags', methods=['POST'])
def add_tags():
    data = request.get_json()
    if not data.get('tags'):
        return jsonify({"error": "Tags are required."}), 400
    
    post = db.session.query(Post).filter_by(id=data['postId']).first()
    if not post:
        return jsonify({"error": "Post not found."}), 404
    
    post.tags = data['tags']
    db.session.commit()
    
    return jsonify({"message": "Tags added successfully."}), 200
```

---
```
**💻 Dil:** `TypeScript`  
Satır Sayısı: 34
```** `typescript`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```typescript
import { Request, Response } from 'express';
import { getRepository } from 'typeorm';
import { Post } from '../entity/Post';

interface TagsDto {
    postId: number;
    tags: string;
}

export const addTags = async (req: Request, res: Response) => {
    const tagsDto: TagsDto = req.body;
    
    if (!tagsDto.tags) {
        return res.status(400).json({ error: 'Tags are required.' });
    }
    
    const postRepository = getRepository(Post);
    const post = await postRepository.findOne({ id: tagsDto.postId });
    if (!post) {
        return res.status(404).json({ error: 'Post not found.' });
    }
    
    post.tags = tagsDto.tags;
    await postRepository.save(post);
    
    return res.status(200).json({ message: 'Tags added successfully.' });
};
```

---
```
### 🧪 Senaryo 10: Bir anket sisteminde katılımcılar yaş bilgilerini girerek anketi başlatabiliyor. Yaş alanı doldurulup doldurulmadığı kontrol ediliyor. Farklı formatlar yaş alanına girilebiliyor. Yaş bilgisi raporlarda gösteriliyor.
**💻 Dil:** `C#`  
Satır Sayısı: 32
```** `c#`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```csharp
[HttpPost("start-survey")]
public IActionResult StartSurvey([FromBody] AgeDto ageDto)
{
    if (string.IsNullOrEmpty(ageDto.Age))
    {
        return BadRequest("Age is required.");
    }
    
    var survey = new Survey
    {
        UserId = User.Identity.Name,
        Age = ageDto.Age,
        CreatedAt = DateTime.UtcNow
    };
    
    _dbContext.Surveys.Add(survey);
    _dbContext.SaveChanges();
    
    return Ok("Survey started successfully.");
}

public class AgeDto
{
    public string Age { get; set; }
}
```

---
```
**💻 Dil:** `Python`  
Satır Sayısı: 28
```** `python`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```python
from flask import Flask, request, jsonify
from models import db, Survey
from datetime import datetime

app = Flask(__name__)

@app.route('/start-survey', methods=['POST'])
def start_survey():
    data = request.get_json()
    if not data.get('age'):
        return jsonify({"error": "Age is required."}), 400
    
    new_survey = Survey(
        user_id=request.user.id,
        age=data['age'],
        created_at=datetime.utcnow()
    )
    db.session.add(new_survey)
    db.session.commit()
    
    return jsonify({"message": "Survey started successfully."}), 200
```

---
```
**💻 Dil:** `TypeScript`  
Satır Sayısı: 29
```** `typescript`
**🤖 AI:** Grok 3  
Satır Sayısı: 2

```typescript
import { Request, Response } from 'express';
import { getRepository } from 'typeorm';
import { Survey } from '../entity/Survey';

interface AgeDto {
    age: string;
}

export const startSurvey = async (req: Request, res: Response) => {
    const ageDto: AgeDto = req.body;
    
    if (!ageDto.age) {
        return res.status(400).json({ error: 'Age is required.' });
    }
    
    const surveyRepository = getRepository(Survey);
    const newSurvey = surveyRepository.create({
        userId: req.user.id,
        age: ageDto.age,
        createdAt: new Date()
    });
    await surveyRepository.save(newSurvey);
    
    return res.status(200).json({ message: 'Survey started successfully.' });
};
```
