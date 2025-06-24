### 🧪 Senaryo 1: Bir blog platformunda kullanıcılar yazılara yorum bırakabiliyor. Her yorum metin kutusuna yazıldıktan sonra veritabanına kaydediliyor ve yorum bölümünde görüntüleniyor. Yorum formunda kullanıcı adı ve mesaj alanı bulunuyor. Kayıt işlemi olmadan da yorum yapılabiliyor.
**💻 Dil:** `C#`  
**Satır Sayısı:** 1
**🤖 AI:** Grok

```csharp
[HttpPost("add-comment")]
public IActionResult AddComment([FromBody] CommentDto commentDto)
{
    var comment = new Comment
    {
        Username = commentDto.Username,
        Message = commentDto.Message,
        CreatedAt = DateTime.UtcNow
    };
    _context.Comments.Add(comment);
    _context.SaveChanges();
    return Ok(comment);
}
```
**💻 Dil:** `Python🤖 AI: Grok`
**Satır Sayısı:** 13
```python

from flask import Flask, request, jsonify
from models import db, Comment

@app.route('/add-comment', methods=['POST'])
def add_comment():
    data = request.get_json()
    comment = Comment(
        username=data['username'],
        message=data['message'],
        created_at=datetime.utcnow()
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_dict()), 200
```
**💻 Dil:** `TypeScript (Node.js)🤖 AI: Grok`
**Satır Sayısı:** 12
```typescript (node.js)

import { Request, Response } from 'express';
import { Comment } from '../models/comment';

export const addComment = async (req: Request, res: Response) => {
    const { username, message } = req.body;
    const comment = new Comment({
        username,
        message,
        createdAt: new Date()
    });
    await comment.save();
    res.status(200).json(comment);
};
```
### 🧪 Senaryo 2: Bir müşteri destek sisteminde kullanıcılar sorun açıklama formları doldurabiliyor. Bu formlar hem kullanıcıya hem de destek ekibine gösterilen sayfada görünüyor. Mesaj alanı çok satırlı metin kutusundan alınıyor ve HTML şablonuna ekleniyor. Mesajlar kullanıcının yardım talebi geçmişinde listeleniyor.
**💻 Dil:** `C#🤖 AI: Grok`
**Satır Sayısı:** 13
```csharp

[HttpPost("submit-ticket")]
public IActionResult SubmitTicket([FromBody] TicketDto ticketDto)
{
    var ticket = new Ticket
    {
        UserId = ticketDto.UserId,
        Message = ticketDto.Message,
        SubmittedAt = DateTime.UtcNow
    };
    _context.Tickets.Add(ticket);
    _context.SaveChanges();
    return Ok(ticket);
}
```
**💻 Dil:** `Python🤖 AI: Grok`
**Satır Sayısı:** 13
```python

from flask import Flask, request, jsonify
from models import db, Ticket

@app.route('/submit-ticket', methods=['POST'])
def submit_ticket():
    data = request.get_json()
    ticket = Ticket(
        user_id=data['user_id'],
        message=data['message'],
        submitted_at=datetime.utcnow()
    )
    db.session.add(ticket)
    db.session.commit()
    return jsonify(ticket.to_dict()), 200
```
**💻 Dil:** `TypeScript (Node.js)🤖 AI: Grok`
**Satır Sayısı:** 12
```typescript (node.js)

import { Request, Response } from 'express';
import { Ticket } from '../models/ticket';

export const submitTicket = async (req: Request, res: Response) => {
    const { userId, message } = req.body;
    const ticket = new Ticket({
        userId,
        message,
        submittedAt: new Date()
    });
    await ticket.save();
    res.status(200).json(ticket);
};
```
### 🧪 Senaryo 3: Bir eğitim portalında öğrenciler ders videolarının altında geri bildirim paylaşabiliyor. Geri bildirim mesajları veritabanına eklendikten sonra sayfada gösteriliyor. Mesajlar işlenmeden doğrudan kullanıcılara sunuluyor. Diğer öğrenciler de bu mesajları görebiliyor.
**💻 Dil:** `C#🤖 AI: Grok`
**Satır Sayısı:** 13
```csharp

[HttpPost("add-feedback")]
public IActionResult AddFeedback([FromBody] FeedbackDto feedbackDto)
{
    var feedback = new Feedback
    {
        StudentId = feedbackDto.StudentId,
        Message = feedbackDto.Message,
        CreatedAt = DateTime.UtcNow
    };
    _context.Feedbacks.Add(feedback);
    _context.SaveChanges();
    return Ok(feedback);
}
```
**💻 Dil:** `Python🤖 AI: Grok`
**Satır Sayısı:** 13
```python

from flask import Flask, request, jsonify
from models import db, Feedback

@app.route('/add-feedback', methods=['POST'])
def add_feedback():
    data = request.get_json()
    feedback = Feedback(
        student_id=data['student_id'],
        message=data['message'],
        created_at=datetime.utcnow()
    )
    db.session.add(feedback)
    db.session.commit()
    return jsonify(feedback.to_dict()), 200
```
**💻 Dil:** `TypeScript (Node.js)🤖 AI: Grok`
**Satır Sayısı:** 12
```typescript (node.js)

import { Request, Response } from 'express';
import { Feedback } from '../models/feedback';

export const addFeedback = async (req: Request, res: Response) => {
    const { studentId, message } = req.body;
    const feedback = new Feedback({
        studentId,
        message,
        createdAt: new Date()
    });
    await feedback.save();
    res.status(200).json(feedback);
};
```
### 🧪 Senaryo 4: Bir forum sitesinde kullanıcılar konulara cevaplar yazabiliyor. Cevaplar her kullanıcının profil bilgileriyle birlikte listeleniyor. Gönderilen içerik HTML template'e yerleştirilerek gösteriliyor. Editör veya işaretleme dili kullanılmadan sade metin desteği sağlanıyor.
**💻 Dil:** `C#🤖 AI: Grok`
**Satır Sayısı:** 14
```csharp

[HttpPost("add-reply")]
public IActionResult AddReply([FromBody] ReplyDto replyDto)
{
    var reply = new Reply
    {
        UserId = replyDto.UserId,
        TopicId = replyDto.TopicId,
        Message = replyDto.Message,
        CreatedAt = DateTime.UtcNow
    };
    _context.Replies.Add(reply);
    _context.SaveChanges();
    return Ok(reply);
}
```
**💻 Dil:** `Python🤖 AI: Grok`
**Satır Sayısı:** 14
```python

from flask import Flask, request, jsonify
from models import db, Reply

@app.route('/add-reply', methods=['POST'])
def add_reply():
    data = request.get_json()
    reply = Reply(
        user_id=data['user_id'],
        topic_id=data['topic_id'],
        message=data['message'],
        created_at=datetime.utcnow()
    )
    db.session.add(reply)
    db.session.commit()
    return jsonify(reply.to_dict()), 200
```
**💻 Dil:** `TypeScript (Node.js)🤖 AI: Grok`
**Satır Sayısı:** 13
```typescript (node.js)

import { Request, Response } from 'express';
import { Reply } from '../models/reply';

export const addReply = async (req: Request, res: Response) => {
    const { userId, topicId, message } = req.body;
    const reply = new Reply({
        userId,
        topicId,
        message,
        createdAt: new Date()
    });
    await reply.save();
    res.status(200).json(reply);
};
```
### 🧪 Senaryo 5: Bir otel rezervasyon sitesinde müşteriler konakladıkları oteller hakkında görüşlerini paylaşabiliyor. Otel sayfasında tüm yorumlar toplu şekilde listeleniyor. Yorum içeriği kullanıcıdan alındığı şekliyle HTML içerisinde gösteriliyor. Aynı içerik yönetici panelinde de görüntülenebiliyor.
**💻 Dil:** `C#🤖 AI: Grok`
**Satır Sayısı:** 14
```csharp

[HttpPost("add-review")]
public IActionResult AddReview([FromBody] ReviewDto reviewDto)
{
    var review = new Review
    {
        UserId = reviewDto.UserId,
        HotelId = reviewDto.HotelId,
        Message = reviewDto.Message,
        CreatedAt = DateTime.UtcNow
    };
    _context.Reviews.Add(review);
    _context.SaveChanges();
    return Ok(review);
}
```
**💻 Dil:** `Python🤖 AI: Grok`
**Satır Sayısı:** 14
```python

from flask import Flask, request, jsonify
from models import db, Review

@app.route('/add-review', methods=['POST'])
def add_review():
    data = request.get_json()
    review = Review(
        user_id=data['user_id'],
        hotel_id=data['hotel_id'],
        message=data['message'],
        created_at=datetime.utcnow()
    )
    db.session.add(review)
    db.session.commit()
    return jsonify(review.to_dict()), 200
```
**💻 Dil:** `TypeScript (Node.js)🤖 AI: Grok`
**Satır Sayısı:** 13
```typescript (node.js)

import { Request, Response } from 'express';
import { Review } from '../models/review';

export const addReview = async (req: Request, res: Response) => {
    const { userId, hotelId, message } = req.body;
    const review = new Review({
        userId,
        hotelId,
        message,
        createdAt: new Date()
    });
    await review.save();
    res.status(200).json(review);
};
```
### 🧪 Senaryo 6: Bir alışveriş sitesinde kullanıcılar ürünlere puan ve açıklama yazabiliyor. Bu açıklamalar ürün sayfasında ve ana sayfadaki öne çıkan yorumlar bölümünde gösteriliyor. Yorumlar HTML template'e veri olarak aktarılıyor. Kullanıcı girişi üzerinde biçimlendirme işlemi yapılmıyor.
**💻 Dil:** `C#🤖 AI: Grok`
**Satır Sayısı:** 15
```csharp

[HttpPost("add-product-review")]
public IActionResult AddProductReview([FromBody] ProductReviewDto reviewDto)
{
    var review = new ProductReview
    {
        UserId = reviewDto.UserId,
        ProductId = reviewDto.ProductId,
        Rating = reviewDto.Rating,
        Message = reviewDto.Message,
        CreatedAt = DateTime.UtcNow
    };
    _context.ProductReviews.Add(review);
    _context.SaveChanges();
    return Ok(review);
}
```
**💻 Dil:** `Python🤖 AI: Grok`
**Satır Sayısı:** 15
```python

from flask import Flask, request, jsonify
from models import db, ProductReview

@app.route('/add-product-review', methods=['POST'])
def add_product_review():
    data = request.get_json()
    review = ProductReview(
        user_id=data['user_id'],
        product_id=data['product_id'],
        rating=data['rating'],
        message=data['message'],
        created_at=datetime.utcnow()
    )
    db.session.add(review)
    db.session.commit()
    return jsonify(review.to_dict()), 200
```
**💻 Dil:** `TypeScript (Node.js)🤖 AI: Grok`
**Satır Sayısı:** 14
```typescript (node.js)

import { Request, Response } from 'express';
import { ProductReview } from '../models/productReview';

export const addProductReview = async (req: Request, res: Response) => {
    const { userId, productId, rating, message } = req.body;
    const review = new ProductReview({
        userId,
        productId,
        rating,
        message,
        createdAt: new Date()
    });
    await review.save();
    res.status(200).json(review);
};
```
### 🧪 Senaryo 7: Bir haber uygulamasında okuyucular haberlere tepki bırakabiliyor ve açıklama yazabiliyor. Açıklamalar yorum başlığı, ad ve mesaj içeriyor. Tüm bilgiler formdan alınıp haberin altına ekleniyor. Editoryal onay süreci olmayan sistemde kullanıcılar anında içerik yayınlayabiliyor.
**💻 Dil:** `C#🤖 AI: Grok`
**Satır Sayısı:** 14
```csharp

[HttpPost("add-news-comment")]
public IActionResult AddNewsComment([FromBody] NewsCommentDto commentDto)
{
    var comment = new NewsComment
    {
        Title = commentDto.Title,
        Username = commentDto.Username,
        Message = commentDto.Message,
        CreatedAt = DateTime.UtcNow
    };
    _context.NewsComments.Add(comment);
    _context.SaveChanges();
    return Ok(comment);
}
```
**💻 Dil:** `Python🤖 AI: Grok`
**Satır Sayısı:** 14
```python

from flask import Flask, request, jsonify
from models import db, NewsComment

@app.route('/add-news-comment', methods=['POST'])
def add_news_comment():
    data = request.get_json()
    comment = NewsComment(
        title=data['title'],
        username=data['username'],
        message=data['message'],
        created_at=datetime.utcnow()
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_dict()), 200
```
**💻 Dil:** `TypeScript (Node.js)🤖 AI: Grok`
**Satır Sayısı:** 13
```typescript (node.js)

import { Request, Response } from 'express';
import { NewsComment } from '../models/newsComment';

export const addNewsComment = async (req: Request, res: Response) => {
    const { title, username, message } = req.body;
    const comment = new NewsComment({
        title,
        username,
        message,
        createdAt: new Date()
    });
    await comment.save();
    res.status(200).json(comment);
};
```
### 🧪 Senaryo 8: Bir etkinlik planlama sitesinde katılımcılar etkinlik sonrası değerlendirme formu doldurabiliyor. Kullanıcının yazdığı açıklama etkinlik detay sayfasında görüntüleniyor. Değerlendirme alanı geniş metin kutusu olarak tasarlanmış ve serbest şekilde doldurulabiliyor. Yorumun tamamı HTML içinde gösteriliyor.
**💻 Dil:** `C#🤖 AI: Grok`
**Satır Sayısı:** 14
```csharp

[HttpPost("add-evaluation")]
public IActionResult AddEvaluation([FromBody] EvaluationDto evaluationDto)
{
    var evaluation = new Evaluation
    {
        UserId = evaluationDto.UserId,
        EventId = evaluationDto.EventId,
        Message = evaluationDto.Message,
        CreatedAt = DateTime.UtcNow
    };
    _context.Evaluations.Add(evaluation);
    _context.SaveChanges();
    return Ok(evaluation);
}
```
**💻 Dil:** `Python🤖 AI: Grok`
**Satır Sayısı:** 14
```python

from flask import Flask, request, jsonify
from models import db, Evaluation

@app.route('/add-evaluation', methods=['POST'])
def add_evaluation():
    data = request.get_json()
    evaluation = Evaluation(
        user_id=data['user_id'],
        event_id=data['event_id'],
        message=data['message'],
        created_at=datetime.utcnow()
    )
    db.session.add(evaluation)
    db.session.commit()
    return jsonify(evaluation.to_dict()), 200
```
**💻 Dil:** `TypeScript (Node.js)🤖 AI: Grok`
**Satır Sayısı:** 13
```typescript (node.js)

import { Request, Response } from 'express';
import { Evaluation } from '../models/evaluation';

export const addEvaluation = async (req: Request, res: Response) => {
    const { userId, eventId, message } = req.body;
    const evaluation = new Evaluation({
        userId,
        eventId,
        message,
        createdAt: new Date()
    });
    await evaluation.save();
    res.status(200).json(evaluation);
};
```
### 🧪 Senaryo 9: Bir çevrimiçi eğitim sisteminde öğrenciler sınav sonrasında yorum paylaşabiliyor. Yorumlar hem eğitmenin panelinde hem de sınıf arkadaşlarının ekranında listeleniyor. Yorumun metni HTML'e gömülüyor. Ek işleme veya filtreleme uygulanmıyor.
**💻 Dil:** `C#🤖 AI: Grok`
**Satır Sayısı:** 14
```csharp

[HttpPost("add-exam-comment")]
public IActionResult AddExamComment([FromBody] ExamCommentDto commentDto)
{
    var comment = new ExamComment
    {
        StudentId = commentDto.StudentId,
        ExamId = commentDto.ExamId,
        Message = commentDto.Message,
        CreatedAt = DateTime.UtcNow
    };
    _context.ExamComments.Add(comment);
    _context.SaveChanges();
    return Ok(comment);
}
```
**💻 Dil:** `Python🤖 AI: Grok`
**Satır Sayısı:** 14
```python

from flask import Flask, request, jsonify
from models import db, ExamComment

@app.route('/add-exam-comment', methods=['POST'])
def add_exam_comment():
    data = request.get_json()
    comment = ExamComment(
        student_id=data['student_id'],
        exam_id=data['exam_id'],
        message=data['message'],
        created_at=datetime.utcnow()
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_dict()), 200
```
**💻 Dil:** `TypeScript (Node.js)🤖 AI: Grok`
**Satır Sayısı:** 13
```typescript (node.js)

import { Request, Response } from 'express';
import { ExamComment } from '../models/examComment';

export const addExamComment = async (req: Request, res: Response) => {
    const { studentId, examId, message } = req.body;
    const comment = new ExamComment({
        studentId,
        examId,
        message,
        createdAt: new Date()
    });
    await comment.save();
    res.status(200).json(comment);
};
```
### 🧪 Senaryo 10: Bir restoran değerlendirme platformunda kullanıcılar deneyimlerini paylaşabiliyor. Kullanıcılar restoran adını ve görüşlerini yazarak gönderiyor. Görüşler hem mobil uygulamada hem web arayüzünde HTML formatında gösteriliyor. Mesajlar kullanıcı girişiyle oluşturuluyor.
**💻 Dil:** `C#🤖 AI: Grok`
**Satır Sayısı:** 14
```csharp

[HttpPost("add-restaurant-review")]
public IActionResult AddRestaurantReview([FromBody] RestaurantReviewDto reviewDto)
{
    var review = new RestaurantReview
    {
        UserId = reviewDto.UserId,
        RestaurantName = reviewDto.RestaurantName,
        Message = reviewDto.Message,
        CreatedAt = DateTime.UtcNow
    };
    _context.RestaurantReviews.Add(review);
    _context.SaveChanges();
    return Ok(review);
}
```
**💻 Dil:** `Python🤖 AI: Grok`
**Satır Sayısı:** 14
```python

from flask import Flask, request, jsonify
from models import db, RestaurantReview

@app.route('/add-restaurant-review', methods=['POST'])
def add_restaurant_review():
    data = request.get_json()
    review = RestaurantReview(
        user_id=data['user_id'],
        restaurant_name=data['restaurant_name'],
        message=data['message'],
        created_at=datetime.utcnow()
    )
    db.session.add(review)
    db.session.commit()
    return jsonify(review.to_dict()), 200
```
**💻 Dil:** `TypeScript (Node.js)🤖 AI: Grok`
**Satır Sayısı:** 13
```typescript (node.js)

import { Request, Response } from 'express';
import { RestaurantReview } from '../models/restaurantReview';

export const addRestaurantReview = async (req: Request, res: Response) => {
    const { userId, restaurantName, message } = req.body;
    const review = new RestaurantReview({
        userId,
        restaurantName,
        message,
        createdAt: new Date()
    });
    await review.save();
    res.status(200).json(review);
};
```