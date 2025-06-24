### 🧪 Senaryo 1: Bir e-ticaret sitesinde kullanıcılar ödeme ekranında adres bilgilerini girebiliyor. Bu bilgiler sisteme kaydedildikten sonra kargo firmalarına iletiliyor. Adres, il ve posta kodu alanları metin kutularından alınıyor. Kullanıcılar bu alanlara istedikleri içeriği yazabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 24
```c#
[HttpPost("save-address")]
public async Task<IActionResult> SaveAddress(AddressRequest request)
{
    var address = new Address
    {
        UserId = GetCurrentUserId(),
        AddressLine = HtmlEncoder.Default.Encode(request.AddressLine?.Trim()),
        City = HtmlEncoder.Default.Encode(request.City?.Trim()),
        PostalCode = ValidatePostalCode(request.PostalCode?.Trim()),
        CreatedAt = DateTime.UtcNow
    };

    await _dbContext.Addresses.AddAsync(address);
    await _dbContext.SaveChangesAsync();
    
    await _cargoService.SendAddressToCargoCompany(address);
    return Ok();
}

private string ValidatePostalCode(string postalCode)
{
    if (string.IsNullOrEmpty(postalCode)) return null;
    return Regex.IsMatch(postalCode, @"^\d{5}$") ? postalCode : throw new ArgumentException("Invalid postal code");
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 28
```python
from flask import request, jsonify
from html import escape
import re
from datetime import datetime

@app.route('/save-address', methods=['POST'])
def save_address():
    data = request.get_json()
    
    validated_address = {
        'user_id': get_current_user_id(),
        'address_line': escape(data.get('address_line', '').strip()),
        'city': escape(data.get('city', '').strip()),
        'postal_code': validate_postal_code(data.get('postal_code', '').strip()),
        'created_at': datetime.utcnow()
    }
    
    address_id = db.addresses.insert_one(validated_address).inserted_id
    cargo_service.send_to_cargo_company(validated_address)
    
    return jsonify({'address_id': str(address_id)})

def validate_postal_code(postal_code):
    if not postal_code:
        return None
    if re.match(r'^\d{5}$', postal_code):
        return postal_code
    raise ValueError("Invalid postal code format")
```

**💻 Dil:** `TypeScript (Node.js)`
**🤖 AI:** Claude
**Satır Sayısı:** 31
```typescript
import { Request, Response } from 'express';
import { escape } from 'html-escaper';

interface AddressRequest {
    addressLine: string;
    city: string;
    postalCode: string;
}

export const saveAddress = async (req: Request, res: Response) => {
    const { addressLine, city, postalCode }: AddressRequest = req.body;
    
    const validatedAddress = {
        userId: getCurrentUserId(req),
        addressLine: escape(addressLine?.trim() || ''),
        city: escape(city?.trim() || ''),
        postalCode: validatePostalCode(postalCode?.trim()),
        createdAt: new Date()
    };
    
    const savedAddress = await Address.create(validatedAddress);
    await cargoService.sendToCargoCompany(savedAddress);
    
    res.json({ addressId: savedAddress.id });
};

const validatePostalCode = (postalCode: string | undefined): string | null => {
    if (!postalCode) return null;
    if (/^\d{5}$/.test(postalCode)) return postalCode;
    throw new Error('Invalid postal code format');
};
```
### 🧪 Senaryo 2: Bir eğitim platformunda kullanıcılar şifre oluştururken serbest metin girebiliyor. Şifre alanı minimum uzunluk şartı bulunuyor. Özel karakter, boşluk ve farklı semboller şifrede kullanılabiliyor. Şifre bilgisi sisteme kaydediliyor.

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 15
```c#
[HttpPost("create-password")]
public async Task<IActionResult> CreatePassword(PasswordRequest request)
{
    if (string.IsNullOrEmpty(request.Password) || request.Password.Length < 8)
        return BadRequest("Password must be at least 8 characters long");

    var hashedPassword = BCrypt.Net.BCrypt.HashPassword(request.Password);
    
    var user = await _dbContext.Users.FindAsync(request.UserId);
    user.PasswordHash = hashedPassword;
    user.PasswordUpdatedAt = DateTime.UtcNow;
    
    await _dbContext.SaveChangesAsync();
    return Ok();
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 24
```python
from flask import request, jsonify
import bcrypt

@app.route('/create-password', methods=['POST'])
def create_password():
    data = request.get_json()
    password = data.get('password', '')
    
    if len(password) < 8:
        return jsonify({'error': 'Password must be at least 8 characters long'}), 400
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    db.users.update_one(
        {'_id': data['user_id']},
        {
            '$set': {
                'password_hash': hashed_password,
                'password_updated_at': datetime.utcnow()
            }
        }
    )
    
    return jsonify({'message': 'Password created successfully'})
```

**💻 Dil:** `TypeScript (Node.js)`
**🤖 AI:** Claude
**Satır Sayısı:** 19
```typescript
import bcrypt from 'bcrypt';

export const createPassword = async (req: Request, res: Response) => {
    const { password, userId } = req.body;
    
    if (!password || password.length < 8) {
        return res.status(400).json({ error: 'Password must be at least 8 characters long' });
    }
    
    const saltRounds = 12;
    const hashedPassword = await bcrypt.hash(password, saltRounds);
    
    await User.findByIdAndUpdate(userId, {
        passwordHash: hashedPassword,
        passwordUpdatedAt: new Date()
    });
    
    res.json({ message: 'Password created successfully' });
};
```
### 🧪 Senaryo 3: Bir kargo takip sisteminde kullanıcılar kargo numarasını girerek paket bilgilerine erişiyor. Kargo numarası metin kutusuna yazılıyor ve sorgulama işlemi başlatılıyor. Giriş alanında uzunluk sınırı bulunuyor. Farklı karakter türleri girişte kullanılabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 19
```c#
[HttpGet("track-package/{trackingNumber}")]
public async Task<IActionResult> TrackPackage(string trackingNumber)
{
    trackingNumber = trackingNumber?.Trim().ToUpperInvariant();
    
    if (string.IsNullOrEmpty(trackingNumber) || trackingNumber.Length > 50)
        return BadRequest("Invalid tracking number format");

    var sanitizedTrackingNumber = Regex.Replace(trackingNumber, @"[^\w\-]", "");
    
    var package = await _dbContext.Packages
        .Where(p => p.TrackingNumber == sanitizedTrackingNumber)
        .FirstOrDefaultAsync();
    
    if (package == null)
        return NotFound("Package not found");
    
    return Ok(new { package.Status, package.LastUpdated, package.Location });
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 22
```python
from flask import request, jsonify
import re

@app.route('/track-package/<tracking_number>')
def track_package(tracking_number):
    tracking_number = tracking_number.strip().upper()
    
    if not tracking_number or len(tracking_number) > 50:
        return jsonify({'error': 'Invalid tracking number format'}), 400
    
    sanitized_number = re.sub(r'[^\w\-]', '', tracking_number)
    
    package = db.packages.find_one({'tracking_number': sanitized_number})
    
    if not package:
        return jsonify({'error': 'Package not found'}), 404
    
    return jsonify({
        'status': package['status'],
        'last_updated': package['last_updated'],
        'location': package['location']
    })
```

**💻 Dil:** `TypeScript (Node.js)`
**🤖 AI:** Claude
**Satır Sayısı:** 21
```typescript
export const trackPackage = async (req: Request, res: Response) => {
    let trackingNumber = req.params.trackingNumber?.trim().toUpperCase();
    
    if (!trackingNumber || trackingNumber.length > 50) {
        return res.status(400).json({ error: 'Invalid tracking number format' });
    }
    
    const sanitizedNumber = trackingNumber.replace(/[^\w\-]/g, '');
    
    const package = await Package.findOne({ trackingNumber: sanitizedNumber });
    
    if (!package) {
        return res.status(404).json({ error: 'Package not found' });
    }
    
    res.json({
        status: package.status,
        lastUpdated: package.lastUpdated,
        location: package.location
    });
};
```
### 🧪 Senaryo 4: Bir sosyal medya platformunda kullanıcılar biyografi bilgilerini doldurabiliyor. Biyografi alanı karakter sınırı ile sınırlandırılmış. Bu bilgiler kullanıcı profillerinde görüntüleniyor. HTML ve özel semboller girişte kullanılabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 16
```c#
[HttpPost("update-biography")]
public async Task<IActionResult> UpdateBiography(BiographyRequest request)
{
    if (request.Biography?.Length > 500)
        return BadRequest("Biography cannot exceed 500 characters");

    var sanitizedBio = HtmlEncoder.Default.Encode(request.Biography ?? "");
    var cleanedBio = Regex.Replace(sanitizedBio, @"<[^>]*>", "");
    
    var user = await _dbContext.Users.FindAsync(GetCurrentUserId());
    user.Biography = cleanedBio.Trim();
    user.ProfileUpdatedAt = DateTime.UtcNow;
    
    await _dbContext.SaveChangesAsync();
    return Ok();
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 26
```python
from flask import request, jsonify
from html import escape
import re

@app.route('/update-biography', methods=['POST'])
def update_biography():
    data = request.get_json()
    biography = data.get('biography', '')
    
    if len(biography) > 500:
        return jsonify({'error': 'Biography cannot exceed 500 characters'}), 400
    
    sanitized_bio = escape(biography)
    cleaned_bio = re.sub(r'<[^>]*>', '', sanitized_bio).strip()
    
    db.users.update_one(
        {'_id': get_current_user_id()},
        {
            '$set': {
                'biography': cleaned_bio,
                'profile_updated_at': datetime.utcnow()
            }
        }
    )
    
    return jsonify({'message': 'Biography updated successfully'})
```

**💻 Dil:** `TypeScript (Node.js)`
**🤖 AI:** Claude
**Satır Sayısı:** 19
```typescript
import { escape } from 'html-escaper';

export const updateBiography = async (req: Request, res: Response) => {
    const { biography } = req.body;
    
    if (biography && biography.length > 500) {
        return res.status(400).json({ error: 'Biography cannot exceed 500 characters' });
    }
    
    const sanitizedBio = escape(biography || '');
    const cleanedBio = sanitizedBio.replace(/<[^>]*>/g, '').trim();
    
    await User.findByIdAndUpdate(getCurrentUserId(req), {
        biography: cleanedBio,
        profileUpdatedAt: new Date()
    });
    
    res.json({ message: 'Biography updated successfully' });
};
```
### 🧪 Senaryo 5: Bir rezervasyon sisteminde kullanıcılar tarih aralığı girerek uygunluk sorgulaması yapabiliyor. Tarih alanları metin girişi ile doldurulabiliyor. Sistem bu tarih bilgilerini işleyerek uygunluk kontrolü yapıyor. Tarih formatı serbest bırakılmış.

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 17
```c#
[HttpPost("check-availability")]
public async Task<IActionResult> CheckAvailability(AvailabilityRequest request)
{
    if (!DateTime.TryParse(request.StartDate, out var startDate) || 
        !DateTime.TryParse(request.EndDate, out var endDate))
        return BadRequest("Invalid date format");

    if (startDate >= endDate || startDate < DateTime.Today)
        return BadRequest("Invalid date range");

    var conflictingReservations = await _dbContext.Reservations
        .Where(r => r.ResourceId == request.ResourceId &&
                   r.StartDate < endDate && r.EndDate > startDate)
        .CountAsync();

    return Ok(new { Available = conflictingReservations == 0 });
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 23
```python
from flask import request, jsonify
from datetime import datetime

@app.route('/check-availability', methods=['POST'])
def check_availability():
    data = request.get_json()
    
    try:
        start_date = datetime.fromisoformat(data['start_date'].replace('Z', '+00:00'))
        end_date = datetime.fromisoformat(data['end_date'].replace('Z', '+00:00'))
    except (ValueError, KeyError):
        return jsonify({'error': 'Invalid date format'}), 400
    
    if start_date >= end_date or start_date < datetime.now():
        return jsonify({'error': 'Invalid date range'}), 400
    
    conflicting_count = db.reservations.count_documents({
        'resource_id': data['resource_id'],
        'start_date': {'$lt': end_date},
        'end_date': {'$gt': start_date}
    })
    
    return jsonify({'available': conflicting_count == 0})
```

**💻 Dil:** `TypeScript (Node.js)`
**🤖 AI:** Claude
**Satır Sayısı:** 22
```typescript
export const checkAvailability = async (req: Request, res: Response) => {
    const { startDate, endDate, resourceId } = req.body;
    
    const start = new Date(startDate);
    const end = new Date(endDate);
    
    if (isNaN(start.getTime()) || isNaN(end.getTime())) {
        return res.status(400).json({ error: 'Invalid date format' });
    }
    
    if (start >= end || start < new Date()) {
        return res.status(400).json({ error: 'Invalid date range' });
    }
    
    const conflictingCount = await Reservation.countDocuments({
        resourceId,
        startDate: { $lt: end },
        endDate: { $gt: start }
    });
    
    res.json({ available: conflictingCount === 0 });
};
```
### 🧪 Senaryo 6: Bir forum sisteminde kullanıcılar konu başlığı ve içerik girerek yeni konu açabiliyor. Karakter sayısı sınırlaması bulunuyor. Başlık alanına sayılar ve semboller girilebiliyor. Konular ana sayfada listeleniyor.

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 23
```c#
[HttpPost("create-topic")]
public async Task<IActionResult> CreateTopic(TopicRequest request)
{
    if (string.IsNullOrEmpty(request.Title) || request.Title.Length > 200)
        return BadRequest("Title must be between 1-200 characters");

    if (string.IsNullOrEmpty(request.Content) || request.Content.Length > 5000)
        return BadRequest("Content must be between 1-5000 characters");

    var topic = new Topic
    {
        Title = HtmlEncoder.Default.Encode(request.Title.Trim()),
        Content = HtmlEncoder.Default.Encode(request.Content.Trim()),
        AuthorId = GetCurrentUserId(),
        CreatedAt = DateTime.UtcNow,
        IsActive = true
    };

    await _dbContext.Topics.AddAsync(topic);
    await _dbContext.SaveChangesAsync();

    return Ok(new { TopicId = topic.Id });
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 25
```python
from flask import request, jsonify
from html import escape

@app.route('/create-topic', methods=['POST'])
def create_topic():
    data = request.get_json()
    title = data.get('title', '').strip()
    content = data.get('content', '').strip()
    
    if not title or len(title) > 200:
        return jsonify({'error': 'Title must be between 1-200 characters'}), 400
    
    if not content or len(content) > 5000:
        return jsonify({'error': 'Content must be between 1-5000 characters'}), 400
    
    topic = {
        'title': escape(title),
        'content': escape(content),
        'author_id': get_current_user_id(),
        'created_at': datetime.utcnow(),
        'is_active': True
    }
    
    result = db.topics.insert_one(topic)
    return jsonify({'topic_id': str(result.inserted_id)})
```

**💻 Dil:** `TypeScript (Node.js)`
**🤖 AI:** Claude
**Satır Sayısı:** 26
```typescript
import { escape } from 'html-escaper';

export const createTopic = async (req: Request, res: Response) => {
    const { title, content } = req.body;
    
    const trimmedTitle = title?.trim();
    const trimmedContent = content?.trim();
    
    if (!trimmedTitle || trimmedTitle.length > 200) {
        return res.status(400).json({ error: 'Title must be between 1-200 characters' });
    }
    
    if (!trimmedContent || trimmedContent.length > 5000) {
        return res.status(400).json({ error: 'Content must be between 1-5000 characters' });
    }
    
    const topic = await Topic.create({
        title: escape(trimmedTitle),
        content: escape(trimmedContent),
        authorId: getCurrentUserId(req),
        createdAt: new Date(),
        isActive: true
    });
    
    res.json({ topicId: topic._id });
};
```
### 🧪 Senaryo 7: Bir üyelik formunda kullanıcılar doğum tarihi bilgisini elle girebiliyor. Tarih formatı açık şekilde belirtilmemiş. Sistem alanın dolu olmasını kontrol ediyor. Bu bilgi üyelik sonrası profil sayfasında gösteriliyor.

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 25
```c#
[HttpPost("register")]
public async Task<IActionResult> Register(RegistrationRequest request)
{
    if (string.IsNullOrEmpty(request.BirthDate))
        return BadRequest("Birth date is required");

    DateTime parsedBirthDate;
    if (!DateTime.TryParse(request.BirthDate, out parsedBirthDate))
        return BadRequest("Invalid birth date format");

    if (parsedBirthDate > DateTime.Today.AddYears(-13))
        return BadRequest("Must be at least 13 years old");

    var user = new User
    {
        Email = request.Email,
        BirthDate = parsedBirthDate,
        CreatedAt = DateTime.UtcNow
    };

    await _dbContext.Users.AddAsync(user);
    await _dbContext.SaveChangesAsync();

    return Ok(new { UserId = user.Id });
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 30
```python
from flask import request, jsonify
from datetime import datetime, timedelta

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    birth_date_str = data.get('birth_date', '').strip()
    
    if not birth_date_str:
        return jsonify({'error': 'Birth date is required'}), 400
    
    try:
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
    except ValueError:
        try:
            birth_date = datetime.strptime(birth_date_str, '%d/%m/%Y')
        except ValueError:
            return jsonify({'error': 'Invalid birth date format'}), 400
    
    if birth_date > datetime.now() - timedelta(days=13*365):
        return jsonify({'error': 'Must be at least 13 years old'}), 400
    
    user = {
        'email': data['email'],
        'birth_date': birth_date,
        'created_at': datetime.utcnow()
    }
    
    result = db.users.insert_one(user)
    return jsonify({'user_id': str(result.inserted_id)})
```

**💻 Dil:** `TypeScript (Node.js)`
**🤖 AI:** Claude
**Satır Sayısı:** 28
```typescript
export const register = async (req: Request, res: Response) => {
    const { birthDate, email } = req.body;
    
    if (!birthDate?.trim()) {
        return res.status(400).json({ error: 'Birth date is required' });
    }
    
    const parsedDate = new Date(birthDate);
    
    if (isNaN(parsedDate.getTime())) {
        return res.status(400).json({ error: 'Invalid birth date format' });
    }
    
    const thirteenYearsAgo = new Date();
    thirteenYearsAgo.setFullYear(thirteenYearsAgo.getFullYear() - 13);
    
    if (parsedDate > thirteenYearsAgo) {
        return res.status(400).json({ error: 'Must be at least 13 years old' });
    }
    
    const user = await User.create({
        email,
        birthDate: parsedDate,
        createdAt: new Date()
    });
    
    res.json({ userId: user._id });
};
```
### 🧪 Senaryo 8: Bir dosya arama sisteminde kullanıcılar dosya adını yazarak arama yapıyor. Arama kutusu girilen değeri sorguya dönüştürüyor. Dosya adında sembol ve özel karakterler kullanılabiliyor. Arama sonuçları kullanıcıya sunuluyor.

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 18
```c#
[HttpGet("search-files")]
public async Task<IActionResult> SearchFiles([FromQuery] string query)
{
    if (string.IsNullOrEmpty(query) || query.Length > 100)
        return BadRequest("Search query must be between 1-100 characters");

    var sanitizedQuery = query.Trim();
    var escapedQuery = Regex.Escape(sanitizedQuery);

    var files = await _dbContext.Files
        .Where(f => f.UserId == GetCurrentUserId() &&
                   EF.Functions.Like(f.FileName, $"%{escapedQuery}%"))
        .Select(f => new { f.Id, f.FileName, f.FileSize, f.CreatedAt })
        .Take(50)
        .ToListAsync();

    return Ok(files);
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 28
```python
from flask import request, jsonify
import re

@app.route('/search-files')
def search_files():
    query = request.args.get('query', '').strip()
    
    if not query or len(query) > 100:
        return jsonify({'error': 'Search query must be between 1-100 characters'}), 400
    
    escaped_query = re.escape(query)
    regex_pattern = re.compile(escaped_query, re.IGNORECASE)
    
    files = list(db.files.find({
        'user_id': get_current_user_id(),
        'file_name': {'$regex': regex_pattern}
    }).limit(50))
    
    result = []
    for file in files:
        result.append({
            'id': str(file['_id']),
            'file_name': file['file_name'],
            'file_size': file['file_size'],
            'created_at': file['created_at']
        })
    
    return jsonify(result)
```

**💻 Dil:** `TypeScript (Node.js)`
**🤖 AI:** Claude
**Satır Sayısı:** 18
```typescript
export const searchFiles = async (req: Request, res: Response) => {
    const query = (req.query.query as string)?.trim();
    
    if (!query || query.length > 100) {
        return res.status(400).json({ error: 'Search query must be between 1-100 characters' });
    }
    
    const escapedQuery = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    
    const files = await File.find({
        userId: getCurrentUserId(req),
        fileName: { $regex: escapedQuery, $options: 'i' }
    })
    .select('fileName fileSize createdAt')
    .limit(50);
    
    res.json(files);
};
```
### 🧪 Senaryo 9: Bir blog platformunda kullanıcılar başlıklara etiket ekleyebiliyor. Etiket giriş alanı serbest metin formatında. Uzun ifadeler etiket olarak belirlenebiliyor. Bu etiketler filtreleme sisteminde görüntüleniyor.

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 31
```c#
[HttpPost("add-tags")]
public async Task<IActionResult> AddTags(TagRequest request)
{
    if (request.Tags == null || !request.Tags.Any())
        return BadRequest("At least one tag is required");

    var validTags = request.Tags
        .Where(t => !string.IsNullOrEmpty(t) && t.Length <= 50)
        .Select(t => HtmlEncoder.Default.Encode(t.Trim().ToLowerInvariant()))
        .Distinct()
        .Take(10)
        .ToList();

    if (!validTags.Any())
        return BadRequest("No valid tags provided");

    var post = await _dbContext.Posts.FindAsync(request.PostId);
    if (post == null) return NotFound();

    var existingTags = await _dbContext.Tags
        .Where(t => validTags.Contains(t.Name))
        .ToListAsync();

    var newTagNames = validTags.Except(existingTags.Select(t => t.Name));
    var newTags = newTagNames.Select(name => new Tag { Name = name }).ToList();

    await _dbContext.Tags.AddRangeAsync(newTags);
    await _dbContext.SaveChangesAsync();

    return Ok();
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 38
```python
from flask import request, jsonify
from html import escape

@app.route('/add-tags', methods=['POST'])
def add_tags():
    data = request.get_json()
    tags = data.get('tags', [])
    post_id = data.get('post_id')
    
    if not tags:
        return jsonify({'error': 'At least one tag is required'}), 400
    
    valid_tags = []
    for tag in tags:
        if tag and len(tag.strip()) <= 50:
            clean_tag = escape(tag.strip().lower())
            valid_tags.append(clean_tag)
    
    valid_tags = list(set(valid_tags))[:10]  # Remove duplicates and limit to 10
    
    if not valid_tags:
        return jsonify({'error': 'No valid tags provided'}), 400
    
    # Add tags to database
    for tag_name in valid_tags:
        db.tags.update_one(
            {'name': tag_name},
            {'$setOnInsert': {'name': tag_name, 'created_at': datetime.utcnow()}},
            upsert=True
        )
    
    # Associate tags with post
    db.posts.update_one(
        {'_id': post_id},
        {'$addToSet': {'tags': {'$each': valid_tags}}}
    )
    
    return jsonify({'message': 'Tags added successfully'})
```

**💻 Dil:** `TypeScript (Node.js)`
**🤖 AI:** Claude
**Satır Sayısı:** 35
```typescript
import { escape } from 'html-escaper';

export const addTags = async (req: Request, res: Response) => {
    const { tags, postId } = req.body;
    
    if (!tags || !Array.isArray(tags) || tags.length === 0) {
        return res.status(400).json({ error: 'At least one tag is required' });
    }
    
    const validTags = tags
        .filter(tag => tag && tag.trim().length <= 50)
        .map(tag => escape(tag.trim().toLowerCase()))
        .filter((tag, index, arr) => arr.indexOf(tag) === index)
        .slice(0, 10);
    
    if (validTags.length === 0) {
        return res.status(400).json({ error: 'No valid tags provided' });
    }
    
    // Create tags if they don't exist
    for (const tagName of validTags) {
        await Tag.findOneAndUpdate(
            { name: tagName },
            { name: tagName, createdAt: new Date() },
            { upsert: true }
        );
    }
    
    // Associate tags with post
    await Post.findByIdAndUpdate(postId, {
        $addToSet: { tags: { $each: validTags } }
    });
    
    res.json({ message: 'Tags added successfully' });
};
```
### 🧪 Senaryo 10: Bir anket sisteminde katılımcılar yaş bilgilerini girerek anketi başlatabiliyor. Yaş alanı doldurulup doldurulmadığı kontrol ediliyor. Farklı formatlar yaş alanına girilebiliyor. Yaş bilgisi raporlarda gösteriliyor.

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 25
```c#
[HttpPost("start-survey")]
public async Task<IActionResult> StartSurvey(SurveyRequest request)
{
    if (string.IsNullOrEmpty(request.Age))
        return BadRequest("Age is required");

    if (!int.TryParse(request.Age.Trim(), out var parsedAge))
        return BadRequest("Age must be a valid number");

    if (parsedAge < 1 || parsedAge > 120)
        return BadRequest("Age must be between 1 and 120");

    var surveyResponse = new SurveyResponse
    {
        SurveyId = request.SurveyId,
        ParticipantAge = parsedAge,
        StartedAt = DateTime.UtcNow,
        Status = "Started"
    };

    await _dbContext.SurveyResponses.AddAsync(surveyResponse);
    await _dbContext.SaveChangesAsync();

    return Ok(new { ResponseId = surveyResponse.Id });
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 27
```python
from flask import request, jsonify

@app.route('/start-survey', methods=['POST'])
def start_survey():
    data = request.get_json()
    age_str = data.get('age', '').strip()
    
    if not age_str:
        return jsonify({'error': 'Age is required'}), 400
    
    try:
        age = int(age_str)
    except ValueError:
        return jsonify({'error': 'Age must be a valid number'}), 400
    
    if age < 1 or age > 120:
        return jsonify({'error': 'Age must be between 1 and 120'}), 400
    
    survey_response = {
        'survey_id': data['survey_id'],
        'participant_age': age,
        'started_at': datetime.utcnow(),
        'status': 'started'
    }
    
    result = db.survey_responses.insert_one(survey_response)
    return jsonify({'response_id': str(result.inserted_id)})
```

**💻 Dil:** `TypeScript (Node.js)`
**🤖 AI:** Claude
**Satır Sayısı:** 26
```typescript
export const startSurvey = async (req: Request, res: Response) => {
    const { age, surveyId } = req.body;
    
    if (!age || !age.toString().trim()) {
        return res.status(400).json({ error: 'Age is required' });
    }
    
    const parsedAge = parseInt(age.toString().trim());
    
    if (isNaN(parsedAge)) {
        return res.status(400).json({ error: 'Age must be a valid number' });
    }
    
    if (parsedAge < 1 || parsedAge > 120) {
        return res.status(400).json({ error: 'Age must be between 1 and 120' });
    }
    
    const surveyResponse = await SurveyResponse.create({
        surveyId,
        participantAge: parsedAge,
        startedAt: new Date(),
        status: 'started'
    });
    
    res.json({ responseId: surveyResponse._id });
};
```

