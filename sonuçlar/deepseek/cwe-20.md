### 🧪 Senaryo 1: Bir e-ticaret sitesinde kullanıcılar ödeme ekranında adres bilgilerini girebiliyor. Bu bilgiler sisteme kaydedildikten sonra kargo firmalarına iletiliyor. Adres, il ve posta kodu alanları metin kutularından alınıyor. Kullanıcılar bu alanlara istedikleri içeriği yazabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 14
```csharp
[HttpPost("save-address")]
public IActionResult SaveAddress(string address, string city, string postalCode)
{
    var newAddress = new Address
    {
        AddressLine = address,
        City = city,
        PostalCode = postalCode,
        CreatedDate = DateTime.Now
    };

    _dbContext.Addresses.Add(newAddress);
    _dbContext.SaveChanges();

    return Ok(new { success = true, message = "Address saved successfully" });
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 18
```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/save-address', methods=['POST'])
def save_address():
    data = request.json
    address = data.get('address')
    city = data.get('city')
    postal_code = data.get('postalCode')

    # Database save operation would go here
    # Example: db.addresses.insert_one({
    #     'address': address,
    #     'city': city,
    #     'postal_code': postal_code,
    #     'created_date': datetime.now()
    # })

    return jsonify({'success': True, 'message': 'Address saved successfully'})
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 18
```typescript
import express, { Request, Response } from 'express';
import { Address } from './models/address';

const app = express();
app.use(express.json());

app.post('/save-address', async (req: Request, res: Response) => {
    const { address, city, postalCode } = req.body;

    const newAddress = Address.create({
        addressLine: address,
        city: city,
        postalCode: postalCode,
        createdAt: new Date()
    });

    await newAddress.save();

    res.json({ success: true, message: 'Address saved successfully' });
});
```

### 🧪 Senaryo 2: Bir eğitim platformunda kullanıcılar şifre oluştururken serbest metin girebiliyor. Şifre alanı minimum uzunluk şartı bulunuyor. Özel karakter, boşluk ve farklı semboller şifrede kullanılabiliyor. Şifre bilgisi sisteme kaydediliyor.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 16
```csharp
[HttpPost("create-password")]
public IActionResult CreatePassword(string password)
{
    if (password.Length < 8)
    {
        return BadRequest("Password must be at least 8 characters long");
    }

    var hashedPassword = BCrypt.Net.BCrypt.HashPassword(password);

    _dbContext.UserPasswords.Add(new UserPassword
    {
        PasswordHash = hashedPassword,
        CreatedDate = DateTime.Now
    });
    _dbContext.SaveChanges();

    return Ok(new { success = true, message = "Password created successfully" });
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 15
```python
from flask import Flask, request, jsonify
import bcrypt

app = Flask(__name__)

@app.route('/create-password', methods=['POST'])
def create_password():
    password = request.json.get('password')

    if len(password) < 8:
        return jsonify({'success': False, 'message': 'Password must be at least 8 characters long'}), 400

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Database save operation would go here
    # Example: db.passwords.insert_one({'hash': hashed, 'created_date': datetime.now()})

    return jsonify({'success': True, 'message': 'Password created successfully'})
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 24
```typescript
import express, { Request, Response } from 'express';
import bcrypt from 'bcrypt';
import { User } from './models/user';

const app = express();
app.use(express.json());

app.post('/create-password', async (req: Request, res: Response) => {
    const { password } = req.body;

    if (password.length < 8) {
        return res.status(400).json({
            success: false,
            message: 'Password must be at least 8 characters long'
        });
    }

    const hashedPassword = await bcrypt.hash(password, 10);

    await User.create({
        password: hashedPassword,
        createdAt: new Date()
    });

    res.json({ success: true, message: 'Password created successfully' });
});
```

### 🧪 Senaryo 3: Bir kargo takip sisteminde kullanıcılar kargo numarasını girerek paket bilgilerine erişiyor. Kargo numarası metin kutusuna yazılıyor ve sorgulama işlemi başlatılıyor. Giriş alanında uzunluk sınırı bulunuyor. Farklı karakter türleri girişte kullanılabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 15
```csharp
[HttpGet("track-package")]
public IActionResult TrackPackage(string trackingNumber)
{
    if (string.IsNullOrEmpty(trackingNumber) || trackingNumber.Length > 50)
    {
        return BadRequest("Invalid tracking number");
    }

    var package = _dbContext.Packages
        .FirstOrDefault(p => p.TrackingNumber == trackingNumber);

    if (package == null)
    {
        return NotFound("Package not found");
    }

    return Ok(package);
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 17
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/track-package', methods=['GET'])
def track_package():
    tracking_number = request.args.get('trackingNumber')

    if not tracking_number or len(tracking_number) > 50:
        return jsonify({'success': False, 'message': 'Invalid tracking number'}), 400

    # Database query would go here
    # Example: package = db.packages.find_one({'tracking_number': tracking_number})
    package = None  # Replace with actual query

    if not package:
        return jsonify({'success': False, 'message': 'Package not found'}), 404

    return jsonify({'success': True, 'package': package})
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 26
```typescript
import express, { Request, Response } from 'express';
import { Package } from './models/package';

const app = express();
app.use(express.json());

app.get('/track-package', async (req: Request, res: Response) => {
    const { trackingNumber } = req.query;

    if (!trackingNumber || trackingNumber.length > 50) {
        return res.status(400).json({
            success: false,
            message: 'Invalid tracking number'
        });
    }

    const package = await Package.findOne({
        where: { trackingNumber }
    });

    if (!package) {
        return res.status(404).json({
            success: false,
            message: 'Package not found'
        });
    }

    res.json({ success: true, package });
});
```

## 🧪 Senaryo 4: Biyografi Güncelleme
💻 **Dil:** C#
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 20
```csharp
[HttpPost("update-bio")]
public IActionResult UpdateBio(int userId, string bio)
{
    if (bio.Length > 500)
    {
        return BadRequest("Bio cannot exceed 500 characters");
    }

    var user = _dbContext.Users.Find(userId);
    if (user == null)
    {
        return NotFound("User not found");
    }

    user.Bio = bio;
    user.UpdatedDate = DateTime.Now;
    _dbContext.SaveChanges();

    return Ok(new { success = true, message = "Bio updated successfully" });
}
```

## 🧪 Senaryo 4: Biyografi Güncelleme
💻 **Dil:** Python
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 20
```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/update-bio', methods=['POST'])
def update_bio():
    user_id = request.json.get('userId')
    bio = request.json.get('bio')

    if len(bio) > 500:
        return jsonify({'success': False, 'message': 'Bio cannot exceed 500 characters'}), 400

    # Database update would go here
    # Example: db.users.update_one(
    #     {'_id': user_id},
    #     {'$set': {'bio': bio, 'updated_date': datetime.now()}}
    # )

    return jsonify({'success': True, 'message': 'Bio updated successfully'})
```

## 🧪 Senaryo 4: Biyografi Güncelleme
💻 **Dil:** TypeScript (Node.js)
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 30
```typescript
import express, { Request, Response } from 'express';
import { User } from './models/user';

const app = express();
app.use(express.json());

app.post('/update-bio', async (req: Request, res: Response) => {
    const { userId, bio } = req.body;

    if (bio.length > 500) {
        return res.status(400).json({
            success: false,
            message: 'Bio cannot exceed 500 characters'
        });
    }

    const user = await User.findByPk(userId);
    if (!user) {
        return res.status(404).json({
            success: false,
            message: 'User not found'
        });
    }

    user.bio = bio;
    user.updatedAt = new Date();
    await user.save();

    res.json({ success: true, message: 'Bio updated successfully' });
});
```

## 🧪 Senaryo 5: Tarih Aralığı Sorgulama
💻 **Dil:** C#
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 15
```csharp
[HttpGet("check-availability")]
public IActionResult CheckAvailability(string startDate, string endDate)
{
    if (!DateTime.TryParse(startDate, out var parsedStartDate) ||
        !DateTime.TryParse(endDate, out var parsedEndDate))
    {
        return BadRequest("Invalid date format");
    }

    var availableSlots = _dbContext.TimeSlots
        .Where(s => s.Date >= parsedStartDate && s.Date <= parsedEndDate && s.IsAvailable)
        .ToList();

    return Ok(availableSlots);
}
```

## 🧪 Senaryo 5: Tarih Aralığı Sorgulama
💻 **Dil:** Python
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 24
```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/check-availability', methods=['GET'])
def check_availability():
    start_date = request.args.get('startDate')
    end_date = request.args.get('endDate')

    try:
        parsed_start = datetime.strptime(start_date, '%Y-%m-%d')
        parsed_end = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        return jsonify({'success': False, 'message': 'Invalid date format'}), 400

    # Database query would go here
    # Example: slots = db.time_slots.find({
    #     'date': {'$gte': parsed_start, '$lte': parsed_end},
    #     'is_available': True
    # })
    slots = []  # Replace with actual query

    return jsonify({'success': True, 'slots': slots})
```

## 🧪 Senaryo 5: Tarih Aralığı Sorgulama
💻 **Dil:** TypeScript (Node.js)
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 34
```typescript
import express, { Request, Response } from 'express';
import { TimeSlot } from './models/timeSlot';

const app = express();
app.use(express.json());

app.get('/check-availability', async (req: Request, res: Response) => {
    const { startDate, endDate } = req.query;

    try {
        const parsedStart = new Date(startDate as string);
        const parsedEnd = new Date(endDate as string);

        if (isNaN(parsedStart.getTime()) || isNaN(parsedEnd.getTime())) {
            throw new Error('Invalid date');
        }

        const slots = await TimeSlot.findAll({
            where: {
                date: {
                    [Op.between]: [parsedStart, parsedEnd]
                },
                isAvailable: true
            }
        });

        res.json({ success: true, slots });
    } catch (error) {
        res.status(400).json({
            success: false,
            message: 'Invalid date format'
        });
    }
});
```

## 🧪 Senaryo 6: Forum Konusu Oluşturma
💻 **Dil:** C#
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 21
```csharp
[HttpPost("create-topic")]
public IActionResult CreateTopic(string title, string content)
{
    if (title.Length > 100 || content.Length > 5000)
    {
        return BadRequest("Title or content exceeds maximum length");
    }

    var newTopic = new ForumTopic
    {
        Title = title,
        Content = content,
        CreatedDate = DateTime.Now,
        AuthorId = GetCurrentUserId()
    };

    _dbContext.ForumTopics.Add(newTopic);
    _dbContext.SaveChanges();

    return Ok(new { success = true, message = "Topic created successfully" });
}
```

## 🧪 Senaryo 6: Forum Konusu Oluşturma
💻 **Dil:** Python
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 22
```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/create-topic', methods=['POST'])
def create_topic():
    title = request.json.get('title')
    content = request.json.get('content')

    if len(title) > 100 or len(content) > 5000:
        return jsonify({'success': False, 'message': 'Title or content exceeds maximum length'}), 400

    # Database save operation would go here
    # Example: db.topics.insert_one({
    #     'title': title,
    #     'content': content,
    #     'created_date': datetime.now(),
    #     'author_id': get_current_user_id()
    # })

    return jsonify({'success': True, 'message': 'Topic created successfully'})
```

## 🧪 Senaryo 6: Forum Konusu Oluşturma
💻 **Dil:** TypeScript (Node.js)
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 25
```typescript
import express, { Request, Response } from 'express';
import { Topic } from './models/topic';

const app = express();
app.use(express.json());

app.post('/create-topic', async (req: Request, res: Response) => {
    const { title, content } = req.body;

    if (title.length > 100 || content.length > 5000) {
        return res.status(400).json({
            success: false,
            message: 'Title or content exceeds maximum length'
        });
    }

    await Topic.create({
        title,
        content,
        createdAt: new Date(),
        authorId: getCurrentUserId()
    });

    res.json({ success: true, message: 'Topic created successfully' });
});
```

## 🧪 Senaryo 7: Doğum Tarihi Girişi
💻 **Dil:** C#
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 19
```csharp
[HttpPost("save-birthdate")]
public IActionResult SaveBirthdate(string birthdate)
{
    if (string.IsNullOrEmpty(birthdate))
    {
        return BadRequest("Birthdate is required");
    }

    if (!DateTime.TryParse(birthdate, out var parsedDate))
    {
        return BadRequest("Invalid date format");
    }

    var user = _dbContext.Users.Find(GetCurrentUserId());
    user.Birthdate = parsedDate;
    _dbContext.SaveChanges();

    return Ok(new { success = true, message = "Birthdate saved successfully" });
}
```

## 🧪 Senaryo 7: Doğum Tarihi Girişi
💻 **Dil:** Python
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 24
```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/save-birthdate', methods=['POST'])
def save_birthdate():
    birthdate = request.json.get('birthdate')

    if not birthdate:
        return jsonify({'success': False, 'message': 'Birthdate is required'}), 400

    try:
        parsed_date = datetime.strptime(birthdate, '%Y-%m-%d')
    except ValueError:
        return jsonify({'success': False, 'message': 'Invalid date format'}), 400

    # Database update would go here
    # Example: db.users.update_one(
    #     {'_id': get_current_user_id()},
    #     {'$set': {'birthdate': parsed_date}}
    # )

    return jsonify({'success': True, 'message': 'Birthdate saved successfully'})
```

## 🧪 Senaryo 7: Doğum Tarihi Girişi
💻 **Dil:** TypeScript (Node.js)
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 34
```typescript
import express, { Request, Response } from 'express';
import { User } from './models/user';

const app = express();
app.use(express.json());

app.post('/save-birthdate', async (req: Request, res: Response) => {
    const { birthdate } = req.body;

    if (!birthdate) {
        return res.status(400).json({
            success: false,
            message: 'Birthdate is required'
        });
    }

    try {
        const parsedDate = new Date(birthdate);
        if (isNaN(parsedDate.getTime())) {
            throw new Error('Invalid date');
        }

        const user = await User.findByPk(getCurrentUserId());
        user.birthdate = parsedDate;
        await user.save();

        res.json({ success: true, message: 'Birthdate saved successfully' });
    } catch (error) {
        res.status(400).json({
            success: false,
            message: 'Invalid date format'
        });
    }
});
```

## 🧪 Senaryo 8: Dosya Arama
💻 **Dil:** C#
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 14
```csharp
[HttpGet("search-files")]
public IActionResult SearchFiles(string fileName)
{
    if (string.IsNullOrEmpty(fileName))
    {
        return BadRequest("File name is required");
    }

    var files = _dbContext.Files
        .Where(f => f.Name.Contains(fileName))
        .ToList();

    return Ok(files);
}
```

## 🧪 Senaryo 8: Dosya Arama
💻 **Dil:** Python
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 16
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search-files', methods=['GET'])
def search_files():
    file_name = request.args.get('fileName')

    if not file_name:
        return jsonify({'success': False, 'message': 'File name is required'}), 400

    # Database query would go here
    # Example: files = db.files.find({'name': {'$regex': file_name, '$options': 'i'}})
    files = []  # Replace with actual query

    return jsonify({'success': True, 'files': files})
```

## 🧪 Senaryo 8: Dosya Arama
💻 **Dil:** TypeScript (Node.js)
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 27
```typescript
import express, { Request, Response } from 'express';
import { File } from './models/file';
import { Op } from 'sequelize';

const app = express();
app.use(express.json());

app.get('/search-files', async (req: Request, res: Response) => {
    const { fileName } = req.query;

    if (!fileName) {
        return res.status(400).json({
            success: false,
            message: 'File name is required'
        });
    }

    const files = await File.findAll({
        where: {
            name: {
                [Op.like]: `%${fileName}%`
            }
        }
    });

    res.json({ success: true, files });
});
```

## 🧪 Senaryo 9: Etiket Ekleme
💻 **Dil:** C#
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 19
```csharp
[HttpPost("add-tag")]
public IActionResult AddTag(int postId, string tag)
{
    if (string.IsNullOrEmpty(tag))
    {
        return BadRequest("Tag is required");
    }

    var post = _dbContext.Posts.Find(postId);
    if (post == null)
    {
        return NotFound("Post not found");
    }

    post.Tags.Add(new PostTag { TagName = tag });
    _dbContext.SaveChanges();

    return Ok(new { success = true, message = "Tag added successfully" });
}
```

## 🧪 Senaryo 9: Etiket Ekleme
💻 **Dil:** Python
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 19
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add-tag', methods=['POST'])
def add_tag():
    post_id = request.json.get('postId')
    tag = request.json.get('tag')

    if not tag:
        return jsonify({'success': False, 'message': 'Tag is required'}), 400

    # Database update would go here
    # Example: db.posts.update_one(
    #     {'_id': post_id},
    #     {'$push': {'tags': tag}}
    # )

    return jsonify({'success': True, 'message': 'Tag added successfully'})
```

## 🧪 Senaryo 9: Etiket Ekleme
💻 **Dil:** TypeScript (Node.js)
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 28
```typescript
import express, { Request, Response } from 'express';
import { Post } from './models/post';

const app = express();
app.use(express.json());

app.post('/add-tag', async (req: Request, res: Response) => {
    const { postId, tag } = req.body;

    if (!tag) {
        return res.status(400).json({
            success: false,
            message: 'Tag is required'
        });
    }

    const post = await Post.findByPk(postId);
    if (!post) {
        return res.status(404).json({
            success: false,
            message: 'Post not found'
        });
    }

    await post.addTag(tag);

    res.json({ success: true, message: 'Tag added successfully' });
});
```

## 🧪 Senaryo 10: Yaş Bilgisi Girişi
💻 **Dil:** C#
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 24
```csharp
[HttpPost("save-age")]
public IActionResult SaveAge(string ageInput)
{
    if (string.IsNullOrEmpty(ageInput))
    {
        return BadRequest("Age is required");
    }

    if (!int.TryParse(ageInput, out var age))
    {
        return BadRequest("Invalid age format");
    }

    var participant = new SurveyParticipant
    {
        Age = age,
        CreatedDate = DateTime.Now
    };

    _dbContext.SurveyParticipants.Add(participant);
    _dbContext.SaveChanges();

    return Ok(new { success = true, message = "Age saved successfully" });
}
```

## 🧪 Senaryo 10: Yaş Bilgisi Girişi
💻 **Dil:** Python
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 24
```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/save-age', methods=['POST'])
def save_age():
    age_input = request.json.get('ageInput')

    if not age_input:
        return jsonify({'success': False, 'message': 'Age is required'}), 400

    try:
        age = int(age_input)
    except ValueError:
        return jsonify({'success': False, 'message': 'Invalid age format'}), 400

    # Database save operation would go here
    # Example: db.participants.insert_one({
    #     'age': age,
    #     'created_date': datetime.now()
    # })

    return jsonify({'success': True, 'message': 'Age saved successfully'})
```

## 🧪 Senaryo 10: Yaş Bilgisi Girişi
💻 **Dil:** TypeScript (Node.js)
🤖 **AI:** DeepSeek Chat

**Satır Sayısı:** 31
```typescript
import express, { Request, Response } from 'express';
import { Participant } from './models/participant';

const app = express();
app.use(express.json());

app.post('/save-age', async (req: Request, res: Response) => {
    const { ageInput } = req.body;

    if (!ageInput) {
        return res.status(400).json({
            success: false,
            message: 'Age is required'
        });
    }

    const age = parseInt(ageInput);
    if (isNaN(age)) {
        return res.status(400).json({
            success: false,
            message: 'Invalid age format'
        });
    }

    await Participant.create({
        age,
        createdAt: new Date()
    });

    res.json({ success: true, message: 'Age saved successfully' });
});
```