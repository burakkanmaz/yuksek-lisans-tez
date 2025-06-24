### 🧪 Senaryo 1: Bir blog platformunda kullanıcılar yazılara yorum bırakabiliyor. Her yorum metin kutusuna yazıldıktan sonra veritabanına kaydediliyor ve yorum bölümünde görüntüleniyor. Yorum formunda kullanıcı adı ve mesaj alanı bulunuyor. Kayıt işlemi olmadan da yorum yapılabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 13
```csharp
[HttpPost("add-comment")]
public IActionResult AddComment(string username, string message)
{
    var comment = new Comment
    {
        Username = username,
        Message = message,
        CreatedAt = DateTime.Now
    };
    _dbContext.Comments.Add(comment);
    _dbContext.SaveChanges();
    return Ok(comment);
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 8
```python
@app.route('/add-comment', methods=['POST'])
def add_comment():
    username = request.form.get('username')
    message = request.form.get('message')
    comment = Comment(username=username, message=message, created_at=datetime.now())
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_dict())
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 6
```typescript
app.post('/add-comment', (req, res) => {
    const { username, message } = req.body;
    const comment = new Comment({ username, message, createdAt: new Date() });
    comment.save().then(() => res.json(comment));
});
```

### 🧪 Senaryo 2: Bir müşteri destek sisteminde kullanıcılar sorun açıklama formları doldurabiliyor. Bu formlar hem kullanıcıya hem de destek ekibine gösterilen sayfada görünüyor. Mesaj alanı çok satırlı metin kutusundan alınıyor ve HTML şablonuna ekleniyor. Mesajlar kullanıcının yardım talebi geçmişinde listeleniyor.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 12
```csharp
[HttpPost("submit-ticket")]
public IActionResult SubmitTicket(string description)
{
    var ticket = new SupportTicket
    {
        Description = description,
        CreatedAt = DateTime.Now,
        Status = "Open"
    };
    _dbContext.SupportTickets.Add(ticket);
    _dbContext.SaveChanges();
    return Ok(ticket);
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 7
```python
@app.route('/submit-ticket', methods=['POST'])
def submit_ticket():
    description = request.form.get('description')
    ticket = SupportTicket(description=description, created_at=datetime.now(), status="Open")
    db.session.add(ticket)
    db.session.commit()
    return jsonify(ticket.to_dict())
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 6
```typescript
app.post('/submit-ticket', (req, res) => {
    const { description } = req.body;
    const ticket = new SupportTicket({ description, createdAt: new Date(), status: "Open" });
    ticket.save().then(() => res.json(ticket));
});
```

### 🧪 Senaryo 3: Bir eğitim portalında öğrenciler ders videolarının altında geri bildirim paylaşabiliyor. Geri bildirim mesajları veritabanına eklendikten sonra sayfada gösteriliyor. Mesajlar işlenmeden doğrudan kullanıcılara sunuluyor. Diğer öğrenciler de bu mesajları görebiliyor.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 11
```csharp
[HttpPost("submit-feedback")]
public IActionResult SubmitFeedback(string message)
{
    var feedback = new Feedback
    {
        Message = message,
        CreatedAt = DateTime.Now
    };
    _dbContext.Feedbacks.Add(feedback);
    _dbContext.SaveChanges();
    return Ok(feedback);
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 6
```python
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    message = request.form.get('message')
    feedback = Feedback(message=message, created_at=datetime.now())
    db.session.add(feedback)
    db.session.commit()
    return jsonify(feedback.to_dict())
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 6
```typescript
app.post('/submit-feedback', (req, res) => {
    const { message } = req.body;
    const feedback = new Feedback({ message, createdAt: new Date() });
    feedback.save().then(() => res.json(feedback));
});
```

### 🧪 Senaryo 4: Bir forum sitesinde kullanıcılar konulara cevaplar yazabiliyor. Cevaplar her kullanıcının profil bilgileriyle birlikte listeleniyor. Gönderilen içerik HTML template'e yerleştirilerek gösteriliyor. Editör veya işaretleme dili kullanılmadan sade metin desteği sağlanıyor.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 12
```csharp
[HttpPost("post-reply")]
public IActionResult PostReply(int topicId, string message)
{
    var reply = new Reply
    {
        TopicId = topicId,
        Message = message,
        CreatedAt = DateTime.Now
    };
    _dbContext.Replies.Add(reply);
    _dbContext.SaveChanges();
    return Ok(reply);
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 7
```python
@app.route('/post-reply', methods=['POST'])
def post_reply():
    topic_id = request.form.get('topicId')
    message = request.form.get('message')
    reply = Reply(topic_id=topic_id, message=message, created_at=datetime.now())
    db.session.add(reply)
    db.session.commit()
    return jsonify(reply.to_dict())
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 6
```typescript
app.post('/post-reply', (req, res) => {
    const { topicId, message } = req.body;
    const reply = new Reply({ topicId, message, createdAt: new Date() });
    reply.save().then(() => res.json(reply));
});
```

### 🧪 Senaryo 5: Bir otel rezervasyon sitesinde müşteriler konakladıkları oteller hakkında görüşlerini paylaşabiliyor. Otel sayfasında tüm yorumlar toplu şekilde listeleniyor. Yorum içeriği kullanıcıdan alındığı şekliyle HTML içerisinde gösteriliyor. Aynı içerik yönetici panelinde de görüntülenebiliyor.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 12
```csharp
[HttpPost("submit-review")]
public IActionResult SubmitReview(int hotelId, string comment)
{
    var review = new Review
    {
        HotelId = hotelId,
        Comment = comment,
        CreatedAt = DateTime.Now
    };
    _dbContext.Reviews.Add(review);
    _dbContext.SaveChanges();
    return Ok(review);
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 7
```python
@app.route('/submit-review', methods=['POST'])
def submit_review():
    hotel_id = request.form.get('hotelId')
    comment = request.form.get('comment')
    review = Review(hotel_id=hotel_id, comment=comment, created_at=datetime.now())
    db.session.add(review)
    db.session.commit()
    return jsonify(review.to_dict())
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 6
```typescript
app.post('/submit-review', (req, res) => {
    const { hotelId, comment } = req.body;
    const review = new Review({ hotelId, comment, createdAt: new Date() });
    review.save().then(() => res.json(review));
});
```

### 🧪 Senaryo 6: Bir alışveriş sitesinde kullanıcılar ürünlere puan ve açıklama yazabiliyor. Bu açıklamalar ürün sayfasında ve ana sayfadaki öne çıkan yorumlar bölümünde gösteriliyor. Yorumlar HTML template'e veri olarak aktarılıyor. Kullanıcı girişi üzerinde biçimlendirme işlemi yapılmıyor.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 14
```csharp
[HttpPost("submit-product-review")]
public IActionResult SubmitProductReview(int productId, int rating, string comment)
{
    var review = new ProductReview
    {
        ProductId = productId,
        Rating = rating,
        Comment = comment,
        CreatedAt = DateTime.Now
    };
    _dbContext.ProductReviews.Add(review);
    _dbContext.SaveChanges();
    return Ok(review);
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 8
```python
@app.route('/submit-product-review', methods=['POST'])
def submit_product_review():
    product_id = request.form.get('productId')
    rating = request.form.get('rating')
    comment = request.form.get('comment')
    review = ProductReview(product_id=product_id, rating=rating, comment=comment, created_at=datetime.now())
    db.session.add(review)
    db.session.commit()
    return jsonify(review.to_dict())
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 7
```typescript
app.post('/submit-product-review', (req, res) => {
    const { productId, rating, comment } = req.body;
    const review = new ProductReview({ productId, rating, comment, createdAt: new Date() });
    review.save().then(() => res.json(review));
});
```

### 🧪 Senaryo 7: Bir haber uygulamasında okuyucular haberlere tepki bırakabiliyor ve açıklama yazabiliyor. Açıklamalar yorum başlığı, ad ve mesaj içeriyor. Tüm bilgiler formdan alınıp haberin altına ekleniyor. Editoryal onay süreci olmayan sistemde kullanıcılar anında içerik yayınlayabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 14
```csharp
[HttpPost("post-reaction")]
public IActionResult PostReaction(int newsId, string name, string message)
{
    var reaction = new NewsReaction
    {
        NewsId = newsId,
        Name = name,
        Message = message,
        CreatedAt = DateTime.Now
    };
    _dbContext.NewsReactions.Add(reaction);
    _dbContext.SaveChanges();
    return Ok(reaction);
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 8
```python
@app.route('/post-reaction', methods=['POST'])
def post_reaction():
    news_id = request.form.get('newsId')
    name = request.form.get('name')
    message = request.form.get('message')
    reaction = NewsReaction(news_id=news_id, name=name, message=message, created_at=datetime.now())
    db.session.add(reaction)
    db.session.commit()
    return jsonify(reaction.to_dict())
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 7
```typescript
app.post('/post-reaction', (req, res) => {
    const { newsId, name, message } = req.body;
    const reaction = new NewsReaction({ newsId, name, message, createdAt: new Date() });
    reaction.save().then(() => res.json(reaction));
});
```

### 🧪 Senaryo 8: Bir etkinlik planlama sitesinde katılımcılar etkinlik sonrası değerlendirme formu doldurabiliyor. Kullanıcının yazdığı açıklama etkinlik detay sayfasında görüntüleniyor. Değerlendirme alanı geniş metin kutusu olarak tasarlanmış ve serbest şekilde doldurulabiliyor. Yorumun tamamı HTML içinde gösteriliyor.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 12
```csharp
[HttpPost("submit-evaluation")]
public IActionResult SubmitEvaluation(int eventId, string evaluationText)
{
    var evaluation = new EventEvaluation
    {
        EventId = eventId,
        EvaluationText = evaluationText,
        CreatedAt = DateTime.Now
    };
    _dbContext.EventEvaluations.Add(evaluation);
    _dbContext.SaveChanges();
    return Ok(evaluation);
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 7
```python
@app.route('/submit-evaluation', methods=['POST'])
def submit_evaluation():
    event_id = request.form.get('eventId')
    evaluation_text = request.form.get('evaluationText')
    evaluation = EventEvaluation(event_id=event_id, evaluation_text=evaluation_text, created_at=datetime.now())
    db.session.add(evaluation)
    db.session.commit()
    return jsonify(evaluation.to_dict())
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 6
```typescript
app.post('/submit-evaluation', (req, res) => {
    const { eventId, evaluationText } = req.body;
    const evaluation = new EventEvaluation({ eventId, evaluationText, createdAt: new Date() });
    evaluation.save().then(() => res.json(evaluation));
});
```

### 🧪 Senaryo 9: Bir çevrimiçi eğitim sisteminde öğrenciler sınav sonrasında yorum paylaşabiliyor. Yorumlar hem eğitmenin panelinde hem de sınıf arkadaşlarının ekranında listeleniyor. Yorumun metni HTML'e gömülüyor. Ek işleme veya filtreleme uygulanmıyor.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 12
```csharp
[HttpPost("post-exam-comment")]
public IActionResult PostExamComment(int examId, string commentText)
{
    var comment = new ExamComment
    {
        ExamId = examId,
        CommentText = commentText,
        CreatedAt = DateTime.Now
    };
    _dbContext.ExamComments.Add(comment);
    _dbContext.SaveChanges();
    return Ok(comment);
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 7
```python
@app.route('/post-exam-comment', methods=['POST'])
def post_exam_comment():
    exam_id = request.form.get('examId')
    comment_text = request.form.get('commentText')
    comment = ExamComment(exam_id=exam_id, comment_text=comment_text, created_at=datetime.now())
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_dict())
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 6
```typescript
app.post('/post-exam-comment', (req, res) => {
    const { examId, commentText } = req.body;
    const comment = new ExamComment({ examId, commentText, createdAt: new Date() });
    comment.save().then(() => res.json(comment));
});
```

### 🧪 Senaryo 10: Bir restoran değerlendirme platformunda kullanıcılar deneyimlerini paylaşabiliyor. Kullanıcılar restoran adını ve görüşlerini yazarak gönderiyor. Görüşler hem mobil uygulamada hem web arayüzünde HTML formatında gösteriliyor. Mesajlar kullanıcı girişiyle oluşturuluyor.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 13
```csharp
[HttpPost("share-experience")]
public IActionResult ShareExperience(string restaurantName, string experienceText)
{
    var experience = new RestaurantExperience
    {
        RestaurantName = restaurantName,
        ExperienceText = experienceText,
        CreatedAt = DateTime.Now
    };
    _dbContext.RestaurantExperiences.Add(experience);
    _dbContext.SaveChanges();
    return Ok(experience);
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 7
```python
@app.route('/share-experience', methods=['POST'])
def share_experience():
    restaurant_name = request.form.get('restaurantName')
    experience_text = request.form.get('experienceText')
    experience = RestaurantExperience(restaurant_name=restaurant_name, experience_text=experience_text, created_at=datetime.now())
    db.session.add(experience)
    db.session.commit()
    return jsonify(experience.to_dict())
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 6
```typescript
app.post('/share-experience', (req, res) => {
    const { restaurantName, experienceText } = req.body;
    const experience = new RestaurantExperience({ restaurantName, experienceText, createdAt: new Date() });
    experience.save().then(() => res.json(experience));
});
```
