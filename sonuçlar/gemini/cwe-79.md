### 🧪 Senaryo 1: Bir blog platformunda kullanıcılar yazılara yorum bırakabiliyor. Her yorum metin kutusuna yazıldıktan sonra veritabanına kaydediliyor ve yorum bölümünde görüntüleniyor. Yorum formunda kullanıcı adı ve mesaj alanı bulunuyor. Kayıt işlemi olmadan da yorum yapılabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
Satır Sayısı: 23
```csharp
public class Comment
{
    public int Id { get; set; }
    public string Username { get; set; }
    public string Message { get; set; }
    public DateTime CreatedAt { get; set; }
}

public class BlogService
{
    private readonly ApplicationDbContext _dbContext;

    public BlogService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    [HttpPost("add-comment")]
    public async Task<IActionResult> AddComment([FromBody] Comment comment)
    {
        comment.CreatedAt = DateTime.UtcNow;
        _dbContext.Comments.Add(comment);
        await _dbContext.SaveChangesAsync();
        return Ok(comment);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
Satır Sayısı: 28
```python
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=True)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Comment {self.username}>'

@app.route('/add-comment', methods=['POST'])
def add_comment():
    data = request.get_json()
    username = data.get('username')
    message = data.get('message')

    if not message:
        return jsonify({"error": "Message cannot be empty"}), 400

    new_comment = Comment(username=username, message=message)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"message": "Comment added successfully", "comment": {"id": new_comment.id, "username": new_comment.username, "message": new_comment.message, "created_at": new_comment.created_at.isoformat()}}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
Satır Sayısı: 85
```typescript
// Node.js (Express with Mongoose for MongoDB)
import express from 'express';
import mongoose from 'mongoose';

const app = express();
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/blogdb');

interface IComment extends mongoose.Document {
  username?: string;
  message: string;
  createdAt: Date;
}

const CommentSchema = new mongoose.Schema<IComment>({
  username: { type: String, required: false },
  message: { type: String, required: true },
  createdAt: { type: Date, default: Date.now },
});

const Comment = mongoose.model<IComment>('Comment', CommentSchema);

app.post('/add-comment', async (req, res) => {
  try {
    const { username, message } = req.body;
    if (!message) {
      return res.status(400).json({ error: 'Message cannot be empty' });
    }
    const newComment = new Comment({ username, message });
    await newComment.save();
    res.status(201).json({ message: 'Comment added successfully', comment: newComment });
  } catch (error) {
    res.status(500).json({ error: 'Failed to add comment' });
  }
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});

// ReactJS (Frontend component for adding a comment)
import React, { useState } from 'react';

const CommentForm: React.FC = () => {
  const [username, setUsername] = useState<string>('');
  const [message, setMessage] = useState<string>('');

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      const response = await fetch('/add-comment', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, message }),
      });
      if (response.ok) {
        alert('Comment added successfully!');
        setUsername('');
        setMessage('');
      } else {
        alert('Failed to add comment.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="username">Username (Optional):</label>
        <input
          type="text"
          id="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="message">Message:</label>
        <textarea
          id="message"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          required
        ></textarea>
      </div>
      <button type="submit">Add Comment</button>
    </form>
  );
};

export default CommentForm;
```

### 🧪 Senaryo 2: Bir müşteri destek sisteminde kullanıcılar sorun açıklama formları doldurabiliyor. Bu formlar hem kullanıcıya hem de destek ekibine gösterilen sayfada görünüyor. Mesaj alanı çok satırlı metin kutusundan alınıyor ve HTML şablonuna ekleniyor. Mesajlar kullanıcının yardım talebi geçmişinde listeleniyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
Satır Sayısı: 34
```csharp
public class SupportTicket
{
    public int Id { get; set; }
    public int UserId { get; set; }
    public string Subject { get; set; }
    public string Description { get; set; } // This will contain the multi-line text
    public DateTime CreatedAt { get; set; }
    public string Status { get; set; } = "Open"; // e.g., Open, Closed, In Progress
}

public class SupportService
{
    private readonly ApplicationDbContext _dbContext;

    public SupportService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    [HttpPost("submit-ticket")]
    public async Task<IActionResult> SubmitTicket([FromBody] SupportTicket ticket)
    {
        ticket.CreatedAt = DateTime.UtcNow;
        _dbContext.SupportTickets.Add(ticket);
        await _dbContext.SaveChangesAsync();
        return Ok(ticket);
    }

    [HttpGet("user-tickets/{userId}")]
    public async Task<IActionResult> GetUserTickets(int userId)
    {
        var tickets = await _dbContext.SupportTickets
            .Where(t => t.UserId == userId)
            .OrderByDescending(t => t.CreatedAt)
            .ToListAsync();
        return Ok(tickets);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
Satır Sayısı: 45
```python
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///support.db'
db = SQLAlchemy(app)

class SupportTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False) # Multi-line text
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default="Open")

    def __repr__(self):
        return f'<SupportTicket {self.subject}>'

@app.route('/submit-ticket', methods=['POST'])
def submit_ticket():
    data = request.get_json()
    user_id = data.get('user_id')
    subject = data.get('subject')
    description = data.get('description')

    if not all([user_id, subject, description]):
        return jsonify({"error": "Missing required fields"}), 400

    new_ticket = SupportTicket(user_id=user_id, subject=subject, description=description)
    db.session.add(new_ticket)
    db.session.commit()
    return jsonify({"message": "Support ticket submitted successfully", "ticket": {"id": new_ticket.id, "user_id": new_ticket.user_id, "subject": new_ticket.subject, "description": new_ticket.description, "created_at": new_ticket.created_at.isoformat(), "status": new_ticket.status}}), 201

@app.route('/user-tickets/<int:user_id>', methods=['GET'])
def get_user_tickets(user_id):
    tickets = SupportTicket.query.filter_by(user_id=user_id).order_by(SupportTicket.created_at.desc()).all()
    output = []
    for ticket in tickets:
        output.append({
            "id": ticket.id,
            "user_id": ticket.user_id,
            "subject": ticket.subject,
            "description": ticket.description,
            "created_at": ticket.created_at.isoformat(),
            "status": ticket.status
        })
    return jsonify(output), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
Satır Sayısı: 103
```typescript
// Node.js (Express with Mongoose for MongoDB)
import express from 'express';
import mongoose from 'mongoose';

const app = express();
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/supportdb');

interface ISupportTicket extends mongoose.Document {
  userId: number;
  subject: string;
  description: string; // Multi-line text
  createdAt: Date;
  status: string;
}

const SupportTicketSchema = new mongoose.Schema<ISupportTicket>({
  userId: { type: Number, required: true },
  subject: { type: String, required: true },
  description: { type: String, required: true },
  createdAt: { type: Date, default: Date.now },
  status: { type: String, default: 'Open' },
});

const SupportTicket = mongoose.model<ISupportTicket>('SupportTicket', SupportTicketSchema);

app.post('/submit-ticket', async (req, res) => {
  try {
    const { userId, subject, description } = req.body;
    if (!userId || !subject || !description) {
      return res.status(400).json({ error: 'Missing required fields' });
    }
    const newTicket = new SupportTicket({ userId, subject, description });
    await newTicket.save();
    res.status(201).json({ message: 'Support ticket submitted successfully', ticket: newTicket });
  } catch (error) {
    res.status(500).json({ error: 'Failed to submit ticket' });
  }
});

app.get('/user-tickets/:userId', async (req, res) => {
  try {
    const userId = parseInt(req.params.userId);
    const tickets = await SupportTicket.find({ userId }).sort({ createdAt: -1 });
    res.status(200).json(tickets);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve tickets' });
  }
});

app.listen(3001, () => {
  console.log('Server is running on port 3001');
});

// ReactJS (Frontend component for submitting a support ticket)
import React, { useState } from 'react';

interface SupportTicketFormProps {
  userId: number;
}

const SupportTicketForm: React.FC<SupportTicketFormProps> = ({ userId }) => {
  const [subject, setSubject] = useState<string>('');
  const [description, setDescription] = useState<string>('');

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      const response = await fetch('/submit-ticket', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ userId, subject, description }),
      });
      if (response.ok) {
        alert('Support ticket submitted successfully!');
        setSubject('');
        setDescription('');
      } else {
        alert('Failed to submit support ticket.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="subject">Subject:</label>
        <input
          type="text"
          id="subject"
          value={subject}
          onChange={(e) => setSubject(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="description">Description:</label>
        <textarea
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          rows={5} // Multi-line text area
          required
        ></textarea>
      </div>
      <button type="submit">Submit Ticket</button>
    </form>
  );
};

export default SupportTicketForm;
```

### 🧪 Senaryo 3: Bir eğitim portalında öğrenciler ders videolarının altında geri bildirim paylaşabiliyor. Geri bildirim mesajları veritabanına eklendikten sonra sayfada gösteriliyor. Mesajlar işlenmeden doğrudan kullanıcılara sunuluyor. Diğer öğrenciler de bu mesajları görebiliyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
Satır Sayısı: 33
```csharp
public class Feedback
{
    public int Id { get; set; }
    public int VideoId { get; set; }
    public int StudentId { get; set; }
    public string Message { get; set; }
    public DateTime CreatedAt { get; set; }
}

public class EducationService
{
    private readonly ApplicationDbContext _dbContext;

    public EducationService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    [HttpPost("add-feedback")]
    public async Task<IActionResult> AddFeedback([FromBody] Feedback feedback)
    {
        feedback.CreatedAt = DateTime.UtcNow;
        _dbContext.Feedbacks.Add(feedback);
        await _dbContext.SaveChangesAsync();
        return Ok(feedback);
    }

    [HttpGet("video-feedback/{videoId}")]
    public async Task<IActionResult> GetVideoFeedback(int videoId)
    {
        var feedbackMessages = await _dbContext.Feedbacks
            .Where(f => f.VideoId == videoId)
            .OrderBy(f => f.CreatedAt)
            .ToListAsync();
        return Ok(feedbackMessages);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
Satır Sayısı: 43
```python
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///education.db'
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Feedback {self.id}>'

@app.route('/add-feedback', methods=['POST'])
def add_feedback():
    data = request.get_json()
    video_id = data.get('video_id')
    student_id = data.get('student_id')
    message = data.get('message')

    if not all([video_id, student_id, message]):
        return jsonify({"error": "Missing required fields"}), 400

    new_feedback = Feedback(video_id=video_id, student_id=student_id, message=message)
    db.session.add(new_feedback)
    db.session.commit()
    return jsonify({"message": "Feedback added successfully", "feedback": {"id": new_feedback.id, "video_id": new_feedback.video_id, "student_id": new_feedback.student_id, "message": new_feedback.message, "created_at": new_feedback.created_at.isoformat()}}), 201

@app.route('/video-feedback/<int:video_id>', methods=['GET'])
def get_video_feedback(video_id):
    feedback_messages = Feedback.query.filter_by(video_id=video_id).order_by(Feedback.created_at.asc()).all()
    output = []
    for feedback in feedback_messages:
        output.append({
            "id": feedback.id,
            "video_id": feedback.video_id,
            "student_id": feedback.student_id,
            "message": feedback.message,
            "created_at": feedback.created_at.isoformat()
        })
    return jsonify(output), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
Satır Sayısı: 128
```typescript
// Node.js (Express with Mongoose for MongoDB)
import express from 'express';
import mongoose from 'mongoose';

const app = express();
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/educationdb');

interface IFeedback extends mongoose.Document {
  videoId: number;
  studentId: number;
  message: string;
  createdAt: Date;
}

const FeedbackSchema = new mongoose.Schema<IFeedback>({
  videoId: { type: Number, required: true },
  studentId: { type: Number, required: true },
  message: { type: String, required: true },
  createdAt: { type: Date, default: Date.now },
});

const Feedback = mongoose.model<IFeedback>('Feedback', FeedbackSchema);

app.post('/add-feedback', async (req, res) => {
  try {
    const { videoId, studentId, message } = req.body;
    if (!videoId || !studentId || !message) {
      return res.status(400).json({ error: 'Missing required fields' });
    }
    const newFeedback = new Feedback({ videoId, studentId, message });
    await newFeedback.save();
    res.status(201).json({ message: 'Feedback added successfully', feedback: newFeedback });
  } catch (error) {
    res.status(500).json({ error: 'Failed to add feedback' });
  }
});

app.get('/video-feedback/:videoId', async (req, res) => {
  try {
    const videoId = parseInt(req.params.videoId);
    const feedbackMessages = await Feedback.find({ videoId }).sort({ createdAt: 1 });
    res.status(200).json(feedbackMessages);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve feedback' });
  }
});

app.listen(3002, () => {
  console.log('Server is running on port 3002');
});

// ReactJS (Frontend component for adding and displaying feedback)
import React, { useState, useEffect } from 'react';

interface FeedbackItem {
  id: string;
  videoId: number;
  studentId: number;
  message: string;
  createdAt: string;
}

interface VideoFeedbackProps {
  videoId: number;
  studentId: number; // Assuming current student ID is available
}

const VideoFeedback: React.FC<VideoFeedbackProps> = ({ videoId, studentId }) => {
  const [message, setMessage] = useState<string>('');
  const [feedbackList, setFeedbackList] = useState<FeedbackItem[]>([]);

  const fetchFeedback = async () => {
    try {
      const response = await fetch(`/video-feedback/${videoId}`);
      if (response.ok) {
        const data: FeedbackItem[] = await response.json();
        setFeedbackList(data);
      } else {
        console.error('Failed to fetch feedback.');
      }
    } catch (error) {
      console.error('Error fetching feedback:', error);
    }
  };

  useEffect(() => {
    fetchFeedback();
  }, [videoId]);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      const response = await fetch('/add-feedback', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ videoId, studentId, message }),
      });
      if (response.ok) {
        setMessage('');
        fetchFeedback(); // Refresh the list
      } else {
        alert('Failed to add feedback.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred.');
    }
  };

  return (
    <div>
      <h3>Leave Feedback</h3>
      <form onSubmit={handleSubmit}>
        <textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          rows={3}
          placeholder="Share your feedback..."
          required
        ></textarea>
        <button type="submit">Submit Feedback</button>
      </form>

      <h3>Student Feedback</h3>
      {feedbackList.length > 0 ? (
        <ul>
          {feedbackList.map((feedback) => (
            <li key={feedback.id}>
              <strong>Student {feedback.studentId}:</strong> {feedback.message}
              <br />
              <small>{new Date(feedback.createdAt).toLocaleString()}</small>
            </li>
          ))}
        </ul>
      ) : (
        <p>No feedback yet for this video.</p>
      )}
    </div>
  );
};

export default VideoFeedback;
```

### 🧪 Senaryo 4: Bir forum sitesinde kullanıcılar konulara cevaplar yazabiliyor. Cevaplar her kullanıcının profil bilgileriyle birlikte listeleniyor. Gönderilen içerik HTML template'e yerleştirilerek gösteriliyor. Editör veya işaretleme dili kullanılmadan sade metin desteği sağlanıyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
Satır Sayısı: 52
```csharp
public class ForumPost
{
    public int Id { get; set; }
    public int TopicId { get; set; }
    public int UserId { get; set; }
    public string Content { get; set; } // Plain text
    public DateTime CreatedAt { get; set; }

    // Navigation property for user profile information (assuming a User model exists)
    public User User { get; set; }
}

public class User
{
    public int Id { get; set; }
    public string Username { get; set; }
    public string ProfilePictureUrl { get; set; }
    // Other user profile details
}

public class ForumService
{
    private readonly ApplicationDbContext _dbContext;

    public ForumService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    [HttpPost("add-forum-post")]
    public async Task<IActionResult> AddForumPost([FromBody] ForumPost post)
    {
        post.CreatedAt = DateTime.UtcNow;
        _dbContext.ForumPosts.Add(post);
        await _dbContext.SaveChangesAsync();
        return Ok(post);
    }

    [HttpGet("topic-posts/{topicId}")]
    public async Task<IActionResult> GetTopicPosts(int topicId)
    {
        var posts = await _dbContext.ForumPosts
            .Where(p => p.TopicId == topicId)
            .Include(p => p.User) // Include user profile information
            .OrderBy(p => p.CreatedAt)
            .Select(p => new
            {
                p.Id,
                p.TopicId,
                p.UserId,
                p.Content,
                p.CreatedAt,
                User = new { p.User.Id, p.User.Username, p.User.ProfilePictureUrl } // Select specific user details
            })
            .ToListAsync();
        return Ok(posts);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayísı:** 53

**Satır Sayısı:** 72
```python
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    profile_picture_url = db.Column(db.String(255), nullable=True)

    posts = db.relationship('ForumPost', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class ForumPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False) # Plain text
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ForumPost {self.id}>'

@app.route('/add-forum-post', methods=['POST'])
def add_forum_post():
    data = request.get_json()
    topic_id = data.get('topic_id')
    user_id = data.get('user_id')
    content = data.get('content')

    if not all([topic_id, user_id, content]):
        return jsonify({"error": "Missing required fields"}), 400

    new_post = ForumPost(topic_id=topic_id, user_id=user_id, content=content)
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Forum post added successfully", "post": {"id": new_post.id, "topic_id": new_post.topic_id, "user_id": new_post.user_id, "content": new_post.content, "created_at": new_post.created_at.isoformat()}}), 201

@app.route('/topic-posts/<int:topic_id>', methods=['GET'])
def get_topic_posts(topic_id):
    posts = ForumPost.query.filter_by(topic_id=topic_id).order_by(ForumPost.created_at.asc()).all()
    output = []
    for post in posts:
        user = User.query.get(post.user_id)
        output.append({
            "id": post.id,
            "topic_id": post.topic_id,
            "user_id": post.user_id,
            "content": post.content,
            "created_at": post.created_at.isoformat(),
            "user": {
                "id": user.id,
                "username": user.username,
                "profile_picture_url": user.profile_picture_url
            } if user else None
        })
    return jsonify(output), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Add a dummy user for testing
        if not User.query.first():
            dummy_user = User(username='testuser', profile_picture_url='[https://example.com/profile.jpg](https://example.com/profile.jpg)')
            db.session.add(dummy_user)
            db.session.commit()
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
Satır Sayısı: 154
```typescript
// Node.js (Express with Mongoose for MongoDB)
import express from 'express';
import mongoose from 'mongoose';

const app = express();
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/forumdb');

interface IUser extends mongoose.Document {
  username: string;
  profilePictureUrl?: string;
}

const UserSchema = new mongoose.Schema<IUser>({
  username: { type: String, required: true, unique: true },
  profilePictureUrl: { type: String },
});

const User = mongoose.model<IUser>('User', UserSchema);

interface IForumPost extends mongoose.Document {
  topicId: number;
  userId: mongoose.Schema.Types.ObjectId; // Reference to User model
  content: string;
  createdAt: Date;
}

const ForumPostSchema = new mongoose.Schema<IForumPost>({
  topicId: { type: Number, required: true },
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  content: { type: String, required: true },
  createdAt: { type: Date, default: Date.now },
});

const ForumPost = mongoose.model<IForumPost>('ForumPost', ForumPostSchema);

app.post('/add-forum-post', async (req, res) => {
  try {
    const { topicId, userId, content } = req.body;
    if (!topicId || !userId || !content) {
      return res.status(400).json({ error: 'Missing required fields' });
    }
    const newPost = new ForumPost({ topicId, userId, content });
    await newPost.save();
    res.status(201).json({ message: 'Forum post added successfully', post: newPost });
  } catch (error) {
    res.status(500).json({ error: 'Failed to add forum post' });
  }
});

app.get('/topic-posts/:topicId', async (req, res) => {
  try {
    const topicId = parseInt(req.params.topicId);
    const posts = await ForumPost.find({ topicId })
      .populate('userId', 'username profilePictureUrl') // Populate user details
      .sort({ createdAt: 1 });
    res.status(200).json(posts);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve forum posts' });
  }
});

app.listen(3003, () => {
  console.log('Server is running on port 3003');
});

// ReactJS (Frontend component for displaying forum posts)
import React, { useState, useEffect } from 'react';

interface UserInfo {
  _id: string;
  username: string;
  profilePictureUrl?: string;
}

interface ForumPostItem {
  _id: string;
  topicId: number;
  userId: UserInfo; // Populated user object
  content: string;
  createdAt: string;
}

interface TopicPostsProps {
  topicId: number;
}

const TopicPosts: React.FC<TopicPostsProps> = ({ topicId }) => {
  const [posts, setPosts] = useState<ForumPostItem[]>([]);
  const [newPostContent, setNewPostContent] = useState<string>('');
  const currentUserId = '60c72b2f9c1e7a001c8e4d2e'; // Example static user ID for demonstration

  const fetchPosts = async () => {
    try {
      const response = await fetch(`/topic-posts/${topicId}`);
      if (response.ok) {
        const data: ForumPostItem[] = await response.json();
        setPosts(data);
      } else {
        console.error('Failed to fetch posts.');
      }
    } catch (error) {
      console.error('Error fetching posts:', error);
    }
  };

  useEffect(() => {
    fetchPosts();
  }, [topicId]);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    if (!newPostContent.trim()) return;

    try {
      const response = await fetch('/add-forum-post', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ topicId, userId: currentUserId, content: newPostContent }),
      });
      if (response.ok) {
        setNewPostContent('');
        fetchPosts(); // Refresh the list
      } else {
        alert('Failed to add post.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred.');
    }
  };

  return (
    <div>
      <h2>Forum Topic Discussions</h2>
      <div>
        <h3>Add a new post</h3>
        <form onSubmit={handleSubmit}>
          <textarea
            value={newPostContent}
            onChange={(e) => setNewPostContent(e.target.value)}
            rows={4}
            placeholder="Write your reply here..."
            required
          ></textarea>
          <button type="submit">Post Reply</button>
        </form>
      </div>

      <h3>Posts:</h3>
      {posts.length > 0 ? (
        <ul>
          {posts.map((post) => (
            <li key={post._id} style={{ border: '1px solid #ccc', margin: '10px 0', padding: '10px' }}>
              <div>
                <strong>{post.userId ? post.userId.username : 'Unknown User'}</strong>
                {post.userId?.profilePictureUrl && (
                  <img src={post.userId.profilePictureUrl} alt="Profile" style={{ width: '30px', height: '30px', borderRadius: '50%', marginLeft: '10px' }} />
                )}
                <br />
                <small>{new Date(post.createdAt).toLocaleString()}</small>
              </div>
              <p>{post.content}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>No posts yet for this topic.</p>
      )}
    </div>
  );
};

export default TopicPosts;
```

### 🧪 Senaryo 5: Bir otel rezervasyon sitesinde müşteriler konakladıkları oteller hakkında görüşlerini paylaşabiliyor. Otel sayfasında tüm yorumlar toplu şekilde listeleniyor. Yorum içeriği kullanıcıdan alındığı şekliyle HTML içerisinde gösteriliyor. Aynı içerik yönetici panelinde de görüntülenebiliyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
Satır Sayısı: 34
```csharp
public class HotelReview
{
    public int Id { get; set; }
    public int HotelId { get; set; }
    public int UserId { get; set; }
    public string ReviewContent { get; set; } // HTML content
    public int Rating { get; set; } // e.g., 1-5 stars
    public DateTime CreatedAt { get; set; }
}

public class HotelReservationService
{
    private readonly ApplicationDbContext _dbContext;

    public HotelReservationService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    [HttpPost("submit-hotel-review")]
    public async Task<IActionResult> SubmitHotelReview([FromBody] HotelReview review)
    {
        review.CreatedAt = DateTime.UtcNow;
        _dbContext.HotelReviews.Add(review);
        await _dbContext.SaveChangesAsync();
        return Ok(review);
    }

    [HttpGet("hotel-reviews/{hotelId}")]
    public async Task<IActionResult> GetHotelReviews(int hotelId)
    {
        var reviews = await _dbContext.HotelReviews
            .Where(r => r.HotelId == hotelId)
            .OrderByDescending(r => r.CreatedAt)
            .ToListAsync();
        return Ok(reviews);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
Satır Sayısı: 48
```python
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel_reviews.db'
db = SQLAlchemy(app)

class HotelReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    review_content = db.Column(db.Text, nullable=False) # HTML content
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<HotelReview {self.id}>'

@app.route('/submit-hotel-review', methods=['POST'])
def submit_hotel_review():
    data = request.get_json()
    hotel_id = data.get('hotel_id')
    user_id = data.get('user_id')
    review_content = data.get('review_content')
    rating = data.get('rating')

    if not all([hotel_id, user_id, review_content, rating is not None]):
        return jsonify({"error": "Missing required fields"}), 400
    if not (1 <= rating <= 5):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    new_review = HotelReview(hotel_id=hotel_id, user_id=user_id, review_content=review_content, rating=rating)
    db.session.add(new_review)
    db.session.commit()
    return jsonify({"message": "Hotel review submitted successfully", "review": {"id": new_review.id, "hotel_id": new_review.hotel_id, "user_id": new_review.user_id, "review_content": new_review.review_content, "rating": new_review.rating, "created_at": new_review.created_at.isoformat()}}), 201

@app.route('/hotel-reviews/<int:hotel_id>', methods=['GET'])
def get_hotel_reviews(hotel_id):
    reviews = HotelReview.query.filter_by(hotel_id=hotel_id).order_by(HotelReview.created_at.desc()).all()
    output = []
    for review in reviews:
        output.append({
            "id": review.id,
            "hotel_id": review.hotel_id,
            "user_id": review.user_id,
            "review_content": review.review_content,
            "rating": review.rating,
            "created_at": review.created_at.isoformat()
        })
    return jsonify(output), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
Satır Sayısı: 151
```typescript
// Node.js (Express with Mongoose for MongoDB)
import express from 'express';
import mongoose from 'mongoose';

const app = express();
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/hotelreservationdb');

interface IHotelReview extends mongoose.Document {
  hotelId: number;
  userId: number;
  reviewContent: string; // HTML content
  rating: number;
  createdAt: Date;
}

const HotelReviewSchema = new mongoose.Schema<IHotelReview>({
  hotelId: { type: Number, required: true },
  userId: { type: Number, required: true },
  reviewContent: { type: String, required: true },
  rating: { type: Number, required: true, min: 1, max: 5 },
  createdAt: { type: Date, default: Date.now },
});

const HotelReview = mongoose.model<IHotelReview>('HotelReview', HotelReviewSchema);

app.post('/submit-hotel-review', async (req, res) => {
  try {
    const { hotelId, userId, reviewContent, rating } = req.body;
    if (!hotelId || !userId || !reviewContent || rating === undefined) {
      return res.status(400).json({ error: 'Missing required fields' });
    }
    if (rating < 1 || rating > 5) {
      return res.status(400).json({ error: 'Rating must be between 1 and 5' });
    }
    const newReview = new HotelReview({ hotelId, userId, reviewContent, rating });
    await newReview.save();
    res.status(201).json({ message: 'Hotel review submitted successfully', review: newReview });
  } catch (error) {
    res.status(500).json({ error: 'Failed to submit hotel review' });
  }
});

app.get('/hotel-reviews/:hotelId', async (req, res) => {
  try {
    const hotelId = parseInt(req.params.hotelId);
    const reviews = await HotelReview.find({ hotelId }).sort({ createdAt: -1 });
    res.status(200).json(reviews);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve hotel reviews' });
  }
});

app.listen(3004, () => {
  console.log('Server is running on port 3004');
});

// ReactJS (Frontend component for submitting and displaying hotel reviews)
import React, { useState, useEffect } from 'react';

interface ReviewItem {
  _id: string;
  hotelId: number;
  userId: number;
  reviewContent: string;
  rating: number;
  createdAt: string;
}

interface HotelReviewProps {
  hotelId: number;
  currentUserId: number; // Assuming current user ID is available
}

const HotelReviews: React.FC<HotelReviewProps> = ({ hotelId, currentUserId }) => {
  const [reviewContent, setReviewContent] = useState<string>('');
  const [rating, setRating] = useState<number>(5);
  const [reviews, setReviews] = useState<ReviewItem[]>([]);

  const fetchReviews = async () => {
    try {
      const response = await fetch(`/hotel-reviews/${hotelId}`);
      if (response.ok) {
        const data: ReviewItem[] = await response.json();
        setReviews(data);
      } else {
        console.error('Failed to fetch reviews.');
      }
    } catch (error) {
      console.error('Error fetching reviews:', error);
    }
  };

  useEffect(() => {
    fetchReviews();
  }, [hotelId]);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      const response = await fetch('/submit-hotel-review', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ hotelId, userId: currentUserId, reviewContent, rating }),
      });
      if (response.ok) {
        setReviewContent('');
        setRating(5);
        fetchReviews(); // Refresh the list
      } else {
        alert('Failed to submit review.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred.');
    }
  };

  return (
    <div>
      <h3>Share Your Review</h3>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="rating">Rating:</label>
          <select id="rating" value={rating} onChange={(e) => setRating(parseInt(e.target.value))} required>
            <option value={1}>1 Star</option>
            <option value={2}>2 Stars</option>
            <option value={3}>3 Stars</option>
            <option value={4}>4 Stars</option>
            <option value={5}>5 Stars</option>
          </select>
        </div>
        <div>
          <label htmlFor="reviewContent">Your Review (HTML allowed):</label>
          <textarea
            id="reviewContent"
            value={reviewContent}
            onChange={(e) => setReviewContent(e.target.value)}
            rows={5}
            placeholder="Write your review here. Basic HTML tags like <b>, <i>, <p> are allowed."
            required
          ></textarea>
        </div>
        <button type="submit">Submit Review</button>
      </form>

      <h3>Customer Reviews</h3>
      {reviews.length > 0 ? (
        <ul>
          {reviews.map((review) => (
            <li key={review._id} style={{ border: '1px solid #eee', margin: '10px 0', padding: '10px' }}>
              <strong>User {review.userId} - Rating: {review.rating} Stars</strong>
              <br />
              <div dangerouslySetInnerHTML={{ __html: review.reviewContent }} />
              <small>{new Date(review.createdAt).toLocaleString()}</small>
            </li>
          ))}
        </ul>
      ) : (
        <p>No reviews yet for this hotel.</p>
      )}
    </div>
  );
};

export default HotelReviews;
```

### 🧪 Senaryo 6: Bir alışveriş sitesinde kullanıcılar ürünlere puan ve açıklama yazabiliyor. Bu açıklamalar ürün sayfasında ve ana sayfadaki öne çıkan yorumlar bölümünde gösteriliyor. Yorumlar HTML template'e veri olarak aktarılıyor. Kullanıcı girişi üzerinde biçimlendirme işlemi yapılmıyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
Satır Sayısı: 44
```csharp
public class ProductReview
{
    public int Id { get; set; }
    public int ProductId { get; set; }
    public int UserId { get; set; }
    public int Rating { get; set; }
    public string Comment { get; set; } // Plain text comment
    public DateTime CreatedAt { get; set; }
}

public class ShoppingService
{
    private readonly ApplicationDbContext _dbContext;

    public ShoppingService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    [HttpPost("add-product-review")]
    public async Task<IActionResult> AddProductReview([FromBody] ProductReview review)
    {
        review.CreatedAt = DateTime.UtcNow;
        _dbContext.ProductReviews.Add(review);
        await _dbContext.SaveChangesAsync();
        return Ok(review);
    }

    [HttpGet("product-reviews/{productId}")]
    public async Task<IActionResult> GetProductReviews(int productId)
    {
        var reviews = await _dbContext.ProductReviews
            .Where(r => r.ProductId == productId)
            .OrderByDescending(r => r.CreatedAt)
            .ToListAsync();
        return Ok(reviews);
    }

    [HttpGet("featured-reviews")]
    public async Task<IActionResult> GetFeaturedReviews()
    {
        // Example: Get top 5 recent reviews or reviews with high ratings
        var featuredReviews = await _dbContext.ProductReviews
            .OrderByDescending(r => r.CreatedAt)
            .Take(5)
            .ToListAsync();
        return Ok(featuredReviews);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
Satır Sayısı: 63
```python
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping.db'
db = SQLAlchemy(app)

class ProductReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False) # Plain text comment
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ProductReview {self.id}>'

@app.route('/add-product-review', methods=['POST'])
def add_product_review():
    data = request.get_json()
    product_id = data.get('product_id')
    user_id = data.get('user_id')
    rating = data.get('rating')
    comment = data.get('comment')

    if not all([product_id, user_id, rating is not None, comment]):
        return jsonify({"error": "Missing required fields"}), 400
    if not (1 <= rating <= 5):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    new_review = ProductReview(product_id=product_id, user_id=user_id, rating=rating, comment=comment)
    db.session.add(new_review)
    db.session.commit()
    return jsonify({"message": "Product review added successfully", "review": {"id": new_review.id, "product_id": new_review.product_id, "user_id": new_review.user_id, "rating": new_review.rating, "comment": new_review.comment, "created_at": new_review.created_at.isoformat()}}), 201

@app.route('/product-reviews/<int:product_id>', methods=['GET'])
def get_product_reviews(product_id):
    reviews = ProductReview.query.filter_by(product_id=product_id).order_by(ProductReview.created_at.desc()).all()
    output = []
    for review in reviews:
        output.append({
            "id": review.id,
            "product_id": review.product_id,
            "user_id": review.user_id,
            "rating": review.rating,
            "comment": review.comment,
            "created_at": review.created_at.isoformat()
        })
    return jsonify(output), 200

@app.route('/featured-reviews', methods=['GET'])
def get_featured_reviews():
    # Example: Get top 5 recent reviews
    featured_reviews = ProductReview.query.order_by(ProductReview.created_at.desc()).limit(5).all()
    output = []
    for review in featured_reviews:
        output.append({
            "id": review.id,
            "product_id": review.product_id,
            "user_id": review.user_id,
            "rating": review.rating,
            "comment": review.comment,
            "created_at": review.created_at.isoformat()
        })
    return jsonify(output), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
Satır Sayısı: 158
```typescript
// Node.js (Express with Mongoose for MongoDB)
import express from 'express';
import mongoose from 'mongoose';

const app = express();
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/shoppingdb');

interface IProductReview extends mongoose.Document {
  productId: number;
  userId: number;
  rating: number;
  comment: string; // Plain text comment
  createdAt: Date;
}

const ProductReviewSchema = new mongoose.Schema<IProductReview>({
  productId: { type: Number, required: true },
  userId: { type: Number, required: true },
  rating: { type: Number, required: true, min: 1, max: 5 },
  comment: { type: String, required: true },
  createdAt: { type: Date, default: Date.now },
});

const ProductReview = mongoose.model<IProductReview>('ProductReview', ProductReviewSchema);

app.post('/add-product-review', async (req, res) => {
  try {
    const { productId, userId, rating, comment } = req.body;
    if (!productId || !userId || rating === undefined || !comment) {
      return res.status(400).json({ error: 'Missing required fields' });
    }
    if (rating < 1 || rating > 5) {
      return res.status(400).json({ error: 'Rating must be between 1 and 5' });
    }
    const newReview = new ProductReview({ productId, userId, rating, comment });
    await newReview.save();
    res.status(201).json({ message: 'Product review added successfully', review: newReview });
  } catch (error) {
    res.status(500).json({ error: 'Failed to add product review' });
  }
});

app.get('/product-reviews/:productId', async (req, res) => {
  try {
    const productId = parseInt(req.params.productId);
    const reviews = await ProductReview.find({ productId }).sort({ createdAt: -1 });
    res.status(200).json(reviews);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve product reviews' });
  }
});

app.get('/featured-reviews', async (req, res) => {
  try {
    const featuredReviews = await ProductReview.find().sort({ createdAt: -1 }).limit(5); // Example: get 5 most recent reviews
    res.status(200).json(featuredReviews);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve featured reviews' });
  }
});

app.listen(3005, () => {
  console.log('Server is running on port 3005');
});

// ReactJS (Frontend component for adding and displaying product reviews)
import React, { useState, useEffect } from 'react';

interface ProductReviewItem {
  _id: string;
  productId: number;
  userId: number;
  rating: number;
  comment: string;
  createdAt: string;
}

interface ProductReviewsProps {
  productId: number;
  currentUserId: number; // Assuming current user ID is available
}

const ProductReviews: React.FC<ProductReviewsProps> = ({ productId, currentUserId }) => {
  const [rating, setRating] = useState<number>(5);
  const [comment, setComment] = useState<string>('');
  const [reviews, setReviews] = useState<ProductReviewItem[]>([]);

  const fetchReviews = async () => {
    try {
      const response = await fetch(`/product-reviews/${productId}`);
      if (response.ok) {
        const data: ProductReviewItem[] = await response.json();
        setReviews(data);
      } else {
        console.error('Failed to fetch product reviews.');
      }
    } catch (error) {
      console.error('Error fetching product reviews:', error);
    }
  };

  useEffect(() => {
    fetchReviews();
  }, [productId]);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      const response = await fetch('/add-product-review', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ productId, userId: currentUserId, rating, comment }),
      });
      if (response.ok) {
        setComment('');
        setRating(5);
        fetchReviews(); // Refresh the list
      } else {
        alert('Failed to submit review.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred.');
    }
  };

  return (
    <div>
      <h3>Write a Review</h3>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="rating">Rating:</label>
          <select id="rating" value={rating} onChange={(e) => setRating(parseInt(e.target.value))} required>
            <option value={1}>1 Star</option>
            <option value={2}>2 Stars</option>
            <option value={3}>3 Stars</option>
            <option value={4}>4 Stars</option>
            <option value={5}>5 Stars</option>
          </select>
        </div>
        <div>
          <label htmlFor="comment">Your Comment:</label>
          <textarea
            id="comment"
            value={comment}
            onChange={(e) => setComment(e.target.value)}
            rows={4}
            placeholder="Write your comment here (plain text)."
            required
          ></textarea>
        </div>
        <button type="submit">Submit Review</button>
      </form>

      <h3>Product Reviews</h3>
      {reviews.length > 0 ? (
        <ul>
          {reviews.map((review) => (
            <li key={review._id} style={{ border: '1px solid #eee', margin: '10px 0', padding: '10px' }}>
              <strong>User {review.userId} - Rating: {review.rating} Stars</strong>
              <p>{review.comment}</p> {/* Render as plain text */}
              <small>{new Date(review.createdAt).toLocaleString()}</small>
            </li>
          ))}
        </ul>
      ) : (
        <p>No reviews yet for this product.</p>
      )}
    </div>
  );
};

export default ProductReviews;
```

### 🧪 Senaryo 7: Bir haber uygulamasında okuyucular haberlere tepki bırakabiliyor ve açıklama yazabiliyor. Açıklamalar yorum başlığı, ad ve mesaj içeriyor. Tüm bilgiler formdan alınıp haberin altına ekleniyor. Editoryal onay süreci olmayan sistemde kullanıcılar anında içerik yayınlayabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
Satır Sayısı: 34
```csharp
public class NewsComment
{
    public int Id { get; set; }
    public int NewsArticleId { get; set; }
    public string CommentTitle { get; set; }
    public string UserName { get; set; } // Name provided by user, not necessarily a registered user
    public string Message { get; set; }
    public DateTime CreatedAt { get; set; }
}

public class NewsService
{
    private readonly ApplicationDbContext _dbContext;

    public NewsService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    [HttpPost("add-news-comment")]
    public async Task<IActionResult> AddNewsComment([FromBody] NewsComment comment)
    {
        comment.CreatedAt = DateTime.UtcNow;
        _dbContext.NewsComments.Add(comment);
        await _dbContext.SaveChangesAsync();
        return Ok(comment);
    }

    [HttpGet("news-comments/{newsArticleId}")]
    public async Task<IActionResult> GetNewsComments(int newsArticleId)
    {
        var comments = await _dbContext.NewsComments
            .Where(c => c.NewsArticleId == newsArticleId)
            .OrderBy(c => c.CreatedAt)
            .ToListAsync();
        return Ok(comments);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
Satır Sayısı: 46
```python
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
db = SQLAlchemy(app)

class NewsComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    news_article_id = db.Column(db.Integer, nullable=False)
    comment_title = db.Column(db.String(255), nullable=True)
    user_name = db.Column(db.String(80), nullable=True) # Name provided by user
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<NewsComment {self.id}>'

@app.route('/add-news-comment', methods=['POST'])
def add_news_comment():
    data = request.get_json()
    news_article_id = data.get('news_article_id')
    comment_title = data.get('comment_title')
    user_name = data.get('user_name')
    message = data.get('message')

    if not all([news_article_id, message]):
        return jsonify({"error": "News article ID and message are required"}), 400

    new_comment = NewsComment(news_article_id=news_article_id, comment_title=comment_title, user_name=user_name, message=message)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"message": "News comment added successfully", "comment": {"id": new_comment.id, "news_article_id": new_comment.news_article_id, "comment_title": new_comment.comment_title, "user_name": new_comment.user_name, "message": new_comment.message, "created_at": new_comment.created_at.isoformat()}}), 201

@app.route('/news-comments/<int:news_article_id>', methods=['GET'])
def get_news_comments(news_article_id):
    comments = NewsComment.query.filter_by(news_article_id=news_article_id).order_by(NewsComment.created_at.asc()).all()
    output = []
    for comment in comments:
        output.append({
            "id": comment.id,
            "news_article_id": comment.news_article_id,
            "comment_title": comment.comment_title,
            "user_name": comment.user_name,
            "message": comment.message,
            "created_at": comment.created_at.isoformat()
        })
    return jsonify(output), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
Satır Sayısı: 156
```typescript
// Node.js (Express with Mongoose for MongoDB)
import express from 'express';
import mongoose from 'mongoose';

const app = express();
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/newsappdb');

interface INewsComment extends mongoose.Document {
  newsArticleId: number;
  commentTitle?: string;
  userName?: string;
  message: string;
  createdAt: Date;
}

const NewsCommentSchema = new mongoose.Schema<INewsComment>({
  newsArticleId: { type: Number, required: true },
  commentTitle: { type: String },
  userName: { type: String },
  message: { type: String, required: true },
  createdAt: { type: Date, default: Date.now },
});

const NewsComment = mongoose.model<INewsComment>('NewsComment', NewsCommentSchema);

app.post('/add-news-comment', async (req, res) => {
  try {
    const { newsArticleId, commentTitle, userName, message } = req.body;
    if (!newsArticleId || !message) {
      return res.status(400).json({ error: 'News article ID and message are required' });
    }
    const newComment = new NewsComment({ newsArticleId, commentTitle, userName, message });
    await newComment.save();
    res.status(201).json({ message: 'News comment added successfully', comment: newComment });
  } catch (error) {
    res.status(500).json({ error: 'Failed to add news comment' });
  }
});

app.get('/news-comments/:newsArticleId', async (req, res) => {
  try {
    const newsArticleId = parseInt(req.params.newsArticleId);
    const comments = await NewsComment.find({ newsArticleId }).sort({ createdAt: 1 });
    res.status(200).json(comments);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve news comments' });
  }
});

app.listen(3006, () => {
  console.log('Server is running on port 3006');
});

// ReactJS (Frontend component for adding and displaying news comments)
import React, { useState, useEffect } from 'react';

interface NewsCommentItem {
  _id: string;
  newsArticleId: number;
  commentTitle?: string;
  userName?: string;
  message: string;
  createdAt: string;
}

interface NewsCommentsProps {
  newsArticleId: number;
}

const NewsComments: React.FC<NewsCommentsProps> = ({ newsArticleId }) => {
  const [commentTitle, setCommentTitle] = useState<string>('');
  const [userName, setUserName] = useState<string>('');
  const [message, setMessage] = useState<string>('');
  const [comments, setComments] = useState<NewsCommentItem[]>([]);

  const fetchComments = async () => {
    try {
      const response = await fetch(`/news-comments/${newsArticleId}`);
      if (response.ok) {
        const data: NewsCommentItem[] = await response.json();
        setComments(data);
      } else {
        console.error('Failed to fetch comments.');
      }
    } catch (error) {
      console.error('Error fetching comments:', error);
    }
  };

  useEffect(() => {
    fetchComments();
  }, [newsArticleId]);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      const response = await fetch('/add-news-comment', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ newsArticleId, commentTitle, userName, message }),
      });
      if (response.ok) {
        setCommentTitle('');
        setUserName('');
        setMessage('');
        fetchComments(); // Refresh the list
      } else {
        alert('Failed to add comment.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred.');
    }
  };

  return (
    <div>
      <h3>Leave a Comment</h3>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="commentTitle">Title (Optional):</label>
          <input
            type="text"
            id="commentTitle"
            value={commentTitle}
            onChange={(e) => setCommentTitle(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="userName">Your Name (Optional):</label>
          <input
            type="text"
            id="userName"
            value={userName}
            onChange={(e) => setUserName(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="message">Message:</label>
          <textarea
            id="message"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            rows={4}
            required
          ></textarea>
        </div>
        <button type="submit">Post Comment</button>
      </form>

      <h3>Comments</h3>
      {comments.length > 0 ? (
        <ul>
          {comments.map((comment) => (
            <li key={comment._id} style={{ border: '1px solid #eee', margin: '10px 0', padding: '10px' }}>
              {comment.commentTitle && <strong>{comment.commentTitle}</strong>}
              {comment.userName && <p>By: {comment.userName}</p>}
              <p>{comment.message}</p>
              <small>{new Date(comment.createdAt).toLocaleString()}</small>
            </li>
          ))}
        </ul>
      ) : (
        <p>No comments yet for this article.</p>
      )}
    </div>
  );
};

export default NewsComments;
```

### 🧪 Senaryo 8: Bir etkinlik planlama sitesinde katılımcılar etkinlik sonrası değerlendirme formu doldurabiliyor. Kullanıcının yazdığı açıklama etkinlik detay sayfasında görüntüleniyor. Değerlendirme alanı geniş metin kutusu olarak tasarlanmış ve serbest şekilde doldurulabiliyor. Yorumun tamamı HTML içinde gösteriliyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
Satır Sayısı: 33
```csharp
public class EventEvaluation
{
    public int Id { get; set; }
    public int EventId { get; set; }
    public int UserId { get; set; }
    public string EvaluationContent { get; set; } // HTML content from a large text area
    public DateTime CreatedAt { get; set; }
}

public class EventPlanningService
{
    private readonly ApplicationDbContext _dbContext;

    public EventPlanningService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    [HttpPost("submit-event-evaluation")]
    public async Task<IActionResult> SubmitEventEvaluation([FromBody] EventEvaluation evaluation)
    {
        evaluation.CreatedAt = DateTime.UtcNow;
        _dbContext.EventEvaluations.Add(evaluation);
        await _dbContext.SaveChangesAsync();
        return Ok(evaluation);
    }

    [HttpGet("event-evaluations/{eventId}")]
    public async Task<IActionResult> GetEventEvaluations(int eventId)
    {
        var evaluations = await _dbContext.EventEvaluations
            .Where(e => e.EventId == eventId)
            .OrderByDescending(e => e.CreatedAt)
            .ToListAsync();
        return Ok(evaluations);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
Satır Sayısı: 43
```python
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_planning.db'
db = SQLAlchemy(app)

class EventEvaluation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    evaluation_content = db.Column(db.Text, nullable=False) # HTML content from large text area
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<EventEvaluation {self.id}>'

@app.route('/submit-event-evaluation', methods=['POST'])
def submit_event_evaluation():
    data = request.get_json()
    event_id = data.get('event_id')
    user_id = data.get('user_id')
    evaluation_content = data.get('evaluation_content')

    if not all([event_id, user_id, evaluation_content]):
        return jsonify({"error": "Missing required fields"}), 400

    new_evaluation = EventEvaluation(event_id=event_id, user_id=user_id, evaluation_content=evaluation_content)
    db.session.add(new_evaluation)
    db.session.commit()
    return jsonify({"message": "Event evaluation submitted successfully", "evaluation": {"id": new_evaluation.id, "event_id": new_evaluation.event_id, "user_id": new_evaluation.user_id, "evaluation_content": new_evaluation.evaluation_content, "created_at": new_evaluation.created_at.isoformat()}}), 201

@app.route('/event-evaluations/<int:event_id>', methods=['GET'])
def get_event_evaluations(event_id):
    evaluations = EventEvaluation.query.filter_by(event_id=event_id).order_by(EventEvaluation.created_at.desc()).all()
    output = []
    for evaluation in evaluations:
        output.append({
            "id": evaluation.id,
            "event_id": evaluation.event_id,
            "user_id": evaluation.user_id,
            "evaluation_content": evaluation.evaluation_content,
            "created_at": evaluation.created_at.isoformat()
        })
    return jsonify(output), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
Satır Sayısı: 133
```typescript
// Node.js (Express with Mongoose for MongoDB)
import express from 'express';
import mongoose from 'mongoose';

const app = express();
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/eventplanningdb');

interface IEventEvaluation extends mongoose.Document {
  eventId: number;
  userId: number;
  evaluationContent: string; // HTML content
  createdAt: Date;
}

const EventEvaluationSchema = new mongoose.Schema<IEventEvaluation>({
  eventId: { type: Number, required: true },
  userId: { type: Number, required: true },
  evaluationContent: { type: String, required: true },
  createdAt: { type: Date, default: Date.now },
});

const EventEvaluation = mongoose.model<IEventEvaluation>('EventEvaluation', EventEvaluationSchema);

app.post('/submit-event-evaluation', async (req, res) => {
  try {
    const { eventId, userId, evaluationContent } = req.body;
    if (!eventId || !userId || !evaluationContent) {
      return res.status(400).json({ error: 'Missing required fields' });
    }
    const newEvaluation = new EventEvaluation({ eventId, userId, evaluationContent });
    await newEvaluation.save();
    res.status(201).json({ message: 'Event evaluation submitted successfully', evaluation: newEvaluation });
  } catch (error) {
    res.status(500).json({ error: 'Failed to submit event evaluation' });
  }
});

app.get('/event-evaluations/:eventId', async (req, res) => {
  try {
    const eventId = parseInt(req.params.eventId);
    const evaluations = await EventEvaluation.find({ eventId }).sort({ createdAt: -1 });
    res.status(200).json(evaluations);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve event evaluations' });
  }
});

app.listen(3007, () => {
  console.log('Server is running on port 3007');
});

// ReactJS (Frontend component for submitting and displaying event evaluations)
import React, { useState, useEffect } from 'react';

interface EventEvaluationItem {
  _id: string;
  eventId: number;
  userId: number;
  evaluationContent: string;
  createdAt: string;
}

interface EventEvaluationProps {
  eventId: number;
  currentUserId: number; // Assuming current user ID is available
}

const EventEvaluations: React.FC<EventEvaluationProps> = ({ eventId, currentUserId }) => {
  const [evaluationContent, setEvaluationContent] = useState<string>('');
  const [evaluations, setEvaluations] = useState<EventEvaluationItem[]>([]);

  const fetchEvaluations = async () => {
    try {
      const response = await fetch(`/event-evaluations/${eventId}`);
      if (response.ok) {
        const data: EventEvaluationItem[] = await response.json();
        setEvaluations(data);
      } else {
        console.error('Failed to fetch evaluations.');
      }
    } catch (error) {
      console.error('Error fetching evaluations:', error);
    }
  };

  useEffect(() => {
    fetchEvaluations();
  }, [eventId]);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      const response = await fetch('/submit-event-evaluation', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ eventId, userId: currentUserId, evaluationContent }),
      });
      if (response.ok) {
        setEvaluationContent('');
        fetchEvaluations(); // Refresh the list
      } else {
        alert('Failed to submit evaluation.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred.');
    }
  };

  return (
    <div>
      <h3>Submit Event Evaluation</h3>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="evaluationContent">Your Evaluation (HTML allowed):</label>
          <textarea
            id="evaluationContent"
            value={evaluationContent}
            onChange={(e) => setEvaluationContent(e.target.value)}
            rows={8} // Large text area
            placeholder="Share your detailed evaluation here. Basic HTML tags like <b>, <i>, <p>, <ul>, <li> are allowed."
            required
          ></textarea>
        </div>
        <button type="submit">Submit Evaluation</button>
      </form>

      <h3>Event Evaluations</h3>
      {evaluations.length > 0 ? (
        <ul>
          {evaluations.map((evaluation) => (
            <li key={evaluation._id} style={{ border: '1px solid #eee', margin: '10px 0', padding: '10px' }}>
              <strong>User {evaluation.userId}</strong>
              <br />
              <div dangerouslySetInnerHTML={{ __html: evaluation.evaluationContent }} />
              <small>{new Date(evaluation.createdAt).toLocaleString()}</small>
            </li>
          ))}
        </ul>
      ) : (
        <p>No evaluations yet for this event.</p>
      )}
    </div>
  );
};

export default EventEvaluations;
```

### 🧪 Senaryo 9: Bir çevrimiçi eğitim sisteminde öğrenciler sınav sonrasında yorum paylaşabiliyor. Yorumlar hem eğitmenin panelinde hem de sınıf arkadaşlarının ekranında listeleniyor. Yorumun metni HTML'e gömülüyor. Ek işleme veya filtreleme uygulanmıyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
Satır Sayısı: 33
```csharp
public class ExamComment
{
    public int Id { get; set; }
    public int ExamId { get; set; }
    public int StudentId { get; set; }
    public string CommentText { get; set; } // Raw comment text, embedded directly into HTML
    public DateTime CreatedAt { get; set; }
}

public class OnlineEducationService
{
    private readonly ApplicationDbContext _dbContext;

    public OnlineEducationService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    [HttpPost("add-exam-comment")]
    public async Task<IActionResult> AddExamComment([FromBody] ExamComment comment)
    {
        comment.CreatedAt = DateTime.UtcNow;
        _dbContext.ExamComments.Add(comment);
        await _dbContext.SaveChangesAsync();
        return Ok(comment);
    }

    [HttpGet("exam-comments/{examId}")]
    public async Task<IActionResult> GetExamComments(int examId)
    {
        var comments = await _dbContext.ExamComments
            .Where(c => c.ExamId == examId)
            .OrderBy(c => c.CreatedAt)
            .ToListAsync();
        return Ok(comments);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
Satır Sayısı: 43
```python
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///online_edu.db'
db = SQLAlchemy(app)

class ExamComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, nullable=False)
    comment_text = db.Column(db.Text, nullable=False) # Raw comment text
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ExamComment {self.id}>'

@app.route('/add-exam-comment', methods=['POST'])
def add_exam_comment():
    data = request.get_json()
    exam_id = data.get('exam_id')
    student_id = data.get('student_id')
    comment_text = data.get('comment_text')

    if not all([exam_id, student_id, comment_text]):
        return jsonify({"error": "Missing required fields"}), 400

    new_comment = ExamComment(exam_id=exam_id, student_id=student_id, comment_text=comment_text)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"message": "Exam comment added successfully", "comment": {"id": new_comment.id, "exam_id": new_comment.exam_id, "student_id": new_comment.student_id, "comment_text": new_comment.comment_text, "created_at": new_comment.created_at.isoformat()}}), 201

@app.route('/exam-comments/<int:exam_id>', methods=['GET'])
def get_exam_comments(exam_id):
    comments = ExamComment.query.filter_by(exam_id=exam_id).order_by(ExamComment.created_at.asc()).all()
    output = []
    for comment in comments:
        output.append({
            "id": comment.id,
            "exam_id": comment.exam_id,
            "student_id": comment.student_id,
            "comment_text": comment.comment_text,
            "created_at": comment.created_at.isoformat()
        })
    return jsonify(output), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
Satır Sayısı: 128
```typescript
// Node.js (Express with Mongoose for MongoDB)
import express from 'express';
import mongoose from 'mongoose';

const app = express();
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/onlineedudb');

interface IExamComment extends mongoose.Document {
  examId: number;
  studentId: number;
  commentText: string; // Raw comment text
  createdAt: Date;
}

const ExamCommentSchema = new mongoose.Schema<IExamComment>({
  examId: { type: Number, required: true },
  studentId: { type: Number, required: true },
  commentText: { type: String, required: true },
  createdAt: { type: Date, default: Date.now },
});

const ExamComment = mongoose.model<IExamComment>('ExamComment', ExamCommentSchema);

app.post('/add-exam-comment', async (req, res) => {
  try {
    const { examId, studentId, commentText } = req.body;
    if (!examId || !studentId || !commentText) {
      return res.status(400).json({ error: 'Missing required fields' });
    }
    const newComment = new ExamComment({ examId, studentId, commentText });
    await newComment.save();
    res.status(201).json({ message: 'Exam comment added successfully', comment: newComment });
  } catch (error) {
    res.status(500).json({ error: 'Failed to add exam comment' });
  }
});

app.get('/exam-comments/:examId', async (req, res) => {
  try {
    const examId = parseInt(req.params.examId);
    const comments = await ExamComment.find({ examId }).sort({ createdAt: 1 });
    res.status(200).json(comments);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve exam comments' });
  }
});

app.listen(3008, () => {
  console.log('Server is running on port 3008');
});

// ReactJS (Frontend component for adding and displaying exam comments)
import React, { useState, useEffect } from 'react';

interface ExamCommentItem {
  _id: string;
  examId: number;
  studentId: number;
  commentText: string;
  createdAt: string;
}

interface ExamCommentsProps {
  examId: number;
  currentStudentId: number; // Assuming current student ID is available
}

const ExamComments: React.FC<ExamCommentsProps> = ({ examId, currentStudentId }) => {
  const [commentText, setCommentText] = useState<string>('');
  const [comments, setComments] = useState<ExamCommentItem[]>([]);

  const fetchComments = async () => {
    try {
      const response = await fetch(`/exam-comments/${examId}`);
      if (response.ok) {
        const data: ExamCommentItem[] = await response.json();
        setComments(data);
      } else {
        console.error('Failed to fetch comments.');
      }
    } catch (error) {
      console.error('Error fetching comments:', error);
    }
  };

  useEffect(() => {
    fetchComments();
  }, [examId]);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      const response = await fetch('/add-exam-comment', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ examId, studentId: currentStudentId, commentText }),
      });
      if (response.ok) {
        setCommentText('');
        fetchComments(); // Refresh the list
      } else {
        alert('Failed to add comment.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred.');
    }
  };

  return (
    <div>
      <h3>Add Exam Comment</h3>
      <form onSubmit={handleSubmit}>
        <textarea
          value={commentText}
          onChange={(e) => setCommentText(e.target.value)}
          rows={5}
          placeholder="Enter your comment about the exam (no formatting)."
          required
        ></textarea>
        <button type="submit">Submit Comment</button>
      </form>

      <h3>Classmate Comments</h3>
      {comments.length > 0 ? (
        <ul>
          {comments.map((comment) => (
            <li key={comment._id} style={{ border: '1px solid #eee', margin: '10px 0', padding: '10px' }}>
              <strong>Student {comment.studentId}:</strong>
              <p>{comment.commentText}</p> {/* Display raw text */}
              <small>{new Date(comment.createdAt).toLocaleString()}</small>
            </li>
          ))}
        </ul>
      ) : (
        <p>No comments yet for this exam.</p>
      )}
    </div>
  );
};

export default ExamComments;
```

### 🧪 Senaryo 10: Bir restoran değerlendirme platformunda kullanıcılar deneyimlerini paylaşabiliyor. Kullanıcılar restoran adını ve görüşlerini yazarak gönderiyor. Görüşler hem mobil uygulamada hem web arayüzünde HTML formatında gösteriliyor. Mesajlar kullanıcı girişiyle oluşturuluyor.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
Satır Sayısı: 43
```csharp
public class RestaurantReview
{
    public int Id { get; set; }
    public int RestaurantId { get; set; }
    public int UserId { get; set; } // Assuming user is logged in
    public string RestaurantName { get; set; }
    public string ReviewContent { get; set; } // HTML content
    public DateTime CreatedAt { get; set; }
}

public class RestaurantReviewService
{
    private readonly ApplicationDbContext _dbContext;

    public RestaurantReviewService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    [HttpPost("submit-restaurant-review")]
    public async Task<IActionResult> SubmitRestaurantReview([FromBody] RestaurantReview review)
    {
        review.CreatedAt = DateTime.UtcNow;
        _dbContext.RestaurantReviews.Add(review);
        await _dbContext.SaveChangesAsync();
        return Ok(review);
    }

    [HttpGet("restaurant-reviews/{restaurantId}")]
    public async Task<IActionResult> GetRestaurantReviews(int restaurantId)
    {
        var reviews = await _dbContext.RestaurantReviews
            .Where(r => r.RestaurantId == restaurantId)
            .OrderByDescending(r => r.CreatedAt)
            .ToListAsync();
        return Ok(reviews);
    }

    [HttpGet("user-reviews/{userId}")]
    public async Task<IActionResult> GetUserReviews(int userId)
    {
        var reviews = await _dbContext.RestaurantReviews
            .Where(r => r.UserId == userId)
            .OrderByDescending(r => r.CreatedAt)
            .ToListAsync();
        return Ok(reviews);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
Satır Sayısı: 60
```python
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant_reviews.db'
db = SQLAlchemy(app)

class RestaurantReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False) # Assuming user is logged in
    restaurant_name = db.Column(db.String(255), nullable=False)
    review_content = db.Column(db.Text, nullable=False) # HTML content
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<RestaurantReview {self.id}>'

@app.route('/submit-restaurant-review', methods=['POST'])
def submit_restaurant_review():
    data = request.get_json()
    restaurant_id = data.get('restaurant_id')
    user_id = data.get('user_id')
    restaurant_name = data.get('restaurant_name')
    review_content = data.get('review_content')

    if not all([restaurant_id, user_id, restaurant_name, review_content]):
        return jsonify({"error": "Missing required fields"}), 400

    new_review = RestaurantReview(restaurant_id=restaurant_id, user_id=user_id, restaurant_name=restaurant_name, review_content=review_content)
    db.session.add(new_review)
    db.session.commit()
    return jsonify({"message": "Restaurant review submitted successfully", "review": {"id": new_review.id, "restaurant_id": new_review.restaurant_id, "user_id": new_review.user_id, "restaurant_name": new_review.restaurant_name, "review_content": new_review.review_content, "created_at": new_review.created_at.isoformat()}}), 201

@app.route('/restaurant-reviews/<int:restaurant_id>', methods=['GET'])
def get_restaurant_reviews(restaurant_id):
    reviews = RestaurantReview.query.filter_by(restaurant_id=restaurant_id).order_by(RestaurantReview.created_at.desc()).all()
    output = []
    for review in reviews:
        output.append({
            "id": review.id,
            "restaurant_id": review.restaurant_id,
            "user_id": review.user_id,
            "restaurant_name": review.restaurant_name,
            "review_content": review.review_content,
            "created_at": review.created_at.isoformat()
        })
    return jsonify(output), 200

@app.route('/user-reviews/<int:user_id>', methods=['GET'])
def get_user_reviews(user_id):
    reviews = RestaurantReview.query.filter_by(user_id=user_id).order_by(RestaurantReview.created_at.desc()).all()
    output = []
    for review in reviews:
        output.append({
            "id": review.id,
            "restaurant_id": review.restaurant_id,
            "user_id": review.user_id,
            "restaurant_name": review.restaurant_name,
            "review_content": review.review_content,
            "created_at": review.created_at.isoformat()
        })
    return jsonify(output), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
Satır Sayısı: 157
```typescript
// Node.js (Express with Mongoose for MongoDB)
import express from 'express';
import mongoose from 'mongoose';

const app = express();
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/restaurantreviewdb');

interface IRestaurantReview extends mongoose.Document {
  restaurantId: number;
  userId: number;
  restaurantName: string;
  reviewContent: string; // HTML content
  createdAt: Date;
}

const RestaurantReviewSchema = new mongoose.Schema<IRestaurantReview>({
  restaurantId: { type: Number, required: true },
  userId: { type: Number, required: true },
  restaurantName: { type: String, required: true },
  reviewContent: { type: String, required: true },
  createdAt: { type: Date, default: Date.now },
});

const RestaurantReview = mongoose.model<IRestaurantReview>('RestaurantReview', RestaurantReviewSchema);

app.post('/submit-restaurant-review', async (req, res) => {
  try {
    const { restaurantId, userId, restaurantName, reviewContent } = req.body;
    if (!restaurantId || !userId || !restaurantName || !reviewContent) {
      return res.status(400).json({ error: 'Missing required fields' });
    }
    const newReview = new RestaurantReview({ restaurantId, userId, restaurantName, reviewContent });
    await newReview.save();
    res.status(201).json({ message: 'Restaurant review submitted successfully', review: newReview });
  } catch (error) {
    res.status(500).json({ error: 'Failed to submit restaurant review' });
  }
});

app.get('/restaurant-reviews/:restaurantId', async (req, res) => {
  try {
    const restaurantId = parseInt(req.params.restaurantId);
    const reviews = await RestaurantReview.find({ restaurantId }).sort({ createdAt: -1 });
    res.status(200).json(reviews);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve restaurant reviews' });
  }
});

app.get('/user-reviews/:userId', async (req, res) => {
  try {
    const userId = parseInt(req.params.userId);
    const reviews = await RestaurantReview.find({ userId }).sort({ createdAt: -1 });
    res.status(200).json(reviews);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve user reviews' });
  }
});

app.listen(3009, () => {
  console.log('Server is running on port 3009');
});

// ReactJS (Frontend component for submitting and displaying restaurant reviews)
import React, { useState, useEffect } from 'react';

interface RestaurantReviewItem {
  _id: string;
  restaurantId: number;
  userId: number;
  restaurantName: string;
  reviewContent: string;
  createdAt: string;
}

interface RestaurantReviewsProps {
  restaurantId: number;
  currentUserId: number; // Assuming current user ID is available
}

const RestaurantReviews: React.FC<RestaurantReviewsProps> = ({ restaurantId, currentUserId }) => {
  const [restaurantName, setRestaurantName] = useState<string>('');
  const [reviewContent, setReviewContent] = useState<string>('');
  const [reviews, setReviews] = useState<RestaurantReviewItem[]>([]);

  const fetchReviews = async () => {
    try {
      const response = await fetch(`/restaurant-reviews/${restaurantId}`);
      if (response.ok) {
        const data: RestaurantReviewItem[] = await response.json();
        setReviews(data);
      } else {
        console.error('Failed to fetch reviews.');
      }
    } catch (error) {
      console.error('Error fetching reviews:', error);
    }
  };

  useEffect(() => {
    fetchReviews();
  }, [restaurantId]);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      const response = await fetch('/submit-restaurant-review', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ restaurantId, userId: currentUserId, restaurantName, reviewContent }),
      });
      if (response.ok) {
        setRestaurantName('');
        setReviewContent('');
        fetchReviews(); // Refresh the list
      } else {
        alert('Failed to submit review.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred.');
    }
  };

  return (
    <div>
      <h3>Share Your Restaurant Experience</h3>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="restaurantName">Restaurant Name:</label>
          <input
            type="text"
            id="restaurantName"
            value={restaurantName}
            onChange={(e) => setRestaurantName(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="reviewContent">Your Review (HTML allowed):</label>
          <textarea
            id="reviewContent"
            value={reviewContent}
            onChange={(e) => setReviewContent(e.target.value)}
            rows={6}
            placeholder="Describe your experience here. Basic HTML tags like <b>, <i>, <p> are allowed."
            required
          ></textarea>
        </div>
        <button type="submit">Submit Review</button>
      </form>

      <h3>Restaurant Reviews</h3>
      {reviews.length > 0 ? (
        <ul>
          {reviews.map((review) => (
            <li key={review._id} style={{ border: '1px solid #eee', margin: '10px 0', padding: '10px' }}>
              <strong>{review.restaurantName}</strong> (Reviewed by User {review.userId})
              <br />
              <div dangerouslySetInnerHTML={{ __html: review.reviewContent }} />
              <small>{new Date(review.createdAt).toLocaleString()}</small>
            </li>
          ))}
        </ul>
      ) : (
        <p>No reviews yet for this restaurant.</p>
      )}
    </div>
  );
};

export default RestaurantReviews;