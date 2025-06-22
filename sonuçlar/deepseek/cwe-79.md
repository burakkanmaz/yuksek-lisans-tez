 markdown
### 🧪 Senaryo 1: Blog Platformunda Yorum Bırakma  
**💻 Dil:** `C#`  
**🤖 AI:** DeepSeek Chat  

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
🧪 Senaryo 1: Blog Platformunda Yorum Bırakma
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/add-comment', methods=['POST'])
def add_comment():
    username = request.form.get('username')
    message = request.form.get('message')
    comment = Comment(username=username, message=message, created_at=datetime.now())
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_dict())
🧪 Senaryo 1: Blog Platformunda Yorum Bırakma
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.post('/add-comment', (req, res) => {
    const { username, message } = req.body;
    const comment = new Comment({ username, message, createdAt: new Date() });
    comment.save().then(() => res.json(comment));
});
🧪 Senaryo 2: Müşteri Destek Sistemi Mesajı
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
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
🧪 Senaryo 2: Müşteri Destek Sistemi Mesajı
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/submit-ticket', methods=['POST'])
def submit_ticket():
    description = request.form.get('description')
    ticket = SupportTicket(description=description, created_at=datetime.now(), status="Open")
    db.session.add(ticket)
    db.session.commit()
    return jsonify(ticket.to_dict())
🧪 Senaryo 2: Müşteri Destek Sistemi Mesajı
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.post('/submit-ticket', (req, res) => {
    const { description } = req.body;
    const ticket = new SupportTicket({ description, createdAt: new Date(), status: "Open" });
    ticket.save().then(() => res.json(ticket));
});
🧪 Senaryo 3: Eğitim Portalında Geri Bildirim
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
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
🧪 Senaryo 3: Eğitim Portalında Geri Bildirim
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    message = request.form.get('message')
    feedback = Feedback(message=message, created_at=datetime.now())
    db.session.add(feedback)
    db.session.commit()
    return jsonify(feedback.to_dict())
🧪 Senaryo 3: Eğitim Portalında Geri Bildirim
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.post('/submit-feedback', (req, res) => {
    const { message } = req.body;
    const feedback = new Feedback({ message, createdAt: new Date() });
    feedback.save().then(() => res.json(feedback));
});
🧪 Senaryo 4: Forum Sitesinde Cevap Yazma
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
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
🧪 Senaryo 4: Forum Sitesinde Cevap Yazma
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/post-reply', methods=['POST'])
def post_reply():
    topic_id = request.form.get('topicId')
    message = request.form.get('message')
    reply = Reply(topic_id=topic_id, message=message, created_at=datetime.now())
    db.session.add(reply)
    db.session.commit()
    return jsonify(reply.to_dict())
🧪 Senaryo 4: Forum Sitesinde Cevap Yazma
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.post('/post-reply', (req, res) => {
    const { topicId, message } = req.body;
    const reply = new Reply({ topicId, message, createdAt: new Date() });
    reply.save().then(() => res.json(reply));
});
🧪 Senaryo 5: Otel Rezervasyon Sitesinde Yorum Paylaşma
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
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
🧪 Senaryo 5: Otel Rezervasyon Sitesinde Yorum Paylaşma
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/submit-review', methods=['POST'])
def submit_review():
    hotel_id = request.form.get('hotelId')
    comment = request.form.get('comment')
    review = Review(hotel_id=hotel_id, comment=comment, created_at=datetime.now())
    db.session.add(review)
    db.session.commit()
    return jsonify(review.to_dict())
🧪 Senaryo 5: Otel Rezervasyon Sitesinde Yorum Paylaşma
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.post('/submit-review', (req, res) => {
    const { hotelId, comment } = req.body;
    const review = new Review({ hotelId, comment, createdAt: new Date() });
    review.save().then(() => res.json(review));
});
(Not: Senaryo 6-10 için benzer şablonla devam edilebilir. Kısalık için burada kesiyorum.)

text

Bu şekilde her senaryo için C#, Python ve TypeScript örnekleri oluşturulabilir. İstenirse diğer senaryolar da eklenebilir.
devam et
markdown
### 🧪 Senaryo 6: Alışveriş Sitesinde Ürün Yorumu  
**💻 Dil:** `C#`  
**🤖 AI:** DeepSeek Chat  

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
🧪 Senaryo 6: Alışveriş Sitesinde Ürün Yorumu
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/submit-product-review', methods=['POST'])
def submit_product_review():
    product_id = request.form.get('productId')
    rating = request.form.get('rating')
    comment = request.form.get('comment')
    review = ProductReview(product_id=product_id, rating=rating, comment=comment, created_at=datetime.now())
    db.session.add(review)
    db.session.commit()
    return jsonify(review.to_dict())
🧪 Senaryo 6: Alışveriş Sitesinde Ürün Yorumu
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.post('/submit-product-review', (req, res) => {
    const { productId, rating, comment } = req.body;
    const review = new ProductReview({ productId, rating, comment, createdAt: new Date() });
    review.save().then(() => res.json(review));
});
🧪 Senaryo 7: Haber Uygulamasında Tepki ve Yorum
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpPost("add-news-comment")]
public IActionResult AddNewsComment(int newsId, string title, string name, string message)
{
    var comment = new NewsComment
    {
        NewsId = newsId,
        Title = title,
        Name = name,
        Message = message,
        CreatedAt = DateTime.Now
    };
    _dbContext.NewsComments.Add(comment);
    _dbContext.SaveChanges();
    return Ok(comment);
}
🧪 Senaryo 7: Haber Uygulamasında Tepki ve Yorum
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/add-news-comment', methods=['POST'])
def add_news_comment():
    news_id = request.form.get('newsId')
    title = request.form.get('title')
    name = request.form.get('name')
    message = request.form.get('message')
    comment = NewsComment(news_id=news_id, title=title, name=name, message=message, created_at=datetime.now())
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_dict())
🧪 Senaryo 7: Haber Uygulamasında Tepki ve Yorum
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.post('/add-news-comment', (req, res) => {
    const { newsId, title, name, message } = req.body;
    const comment = new NewsComment({ newsId, title, name, message, createdAt: new Date() });
    comment.save().then(() => res.json(comment));
});
🧪 Senaryo 8: Etkinlik Değerlendirme Formu
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpPost("submit-event-feedback")]
public IActionResult SubmitEventFeedback(int eventId, string feedback)
{
    var eventFeedback = new EventFeedback
    {
        EventId = eventId,
        Feedback = feedback,
        CreatedAt = DateTime.Now
    };
    _dbContext.EventFeedbacks.Add(eventFeedback);
    _dbContext.SaveChanges();
    return Ok(eventFeedback);
}
🧪 Senaryo 8: Etkinlik Değerlendirme Formu
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/submit-event-feedback', methods=['POST'])
def submit_event_feedback():
    event_id = request.form.get('eventId')
    feedback = request.form.get('feedback')
    event_feedback = EventFeedback(event_id=event_id, feedback=feedback, created_at=datetime.now())
    db.session.add(event_feedback)
    db.session.commit()
    return jsonify(event_feedback.to_dict())
🧪 Senaryo 8: Etkinlik Değerlendirme Formu
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.post('/submit-event-feedback', (req, res) => {
    const { eventId, feedback } = req.body;
    const eventFeedback = new EventFeedback({ eventId, feedback, createdAt: new Date() });
    eventFeedback.save().then(() => res.json(eventFeedback));
});
🧪 Senaryo 9: Çevrimiçi Eğitim Sisteminde Sınav Yorumu
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpPost("submit-exam-comment")]
public IActionResult SubmitExamComment(int examId, string comment)
{
    var examComment = new ExamComment
    {
        ExamId = examId,
        Comment = comment,
        CreatedAt = DateTime.Now
    };
    _dbContext.ExamComments.Add(examComment);
    _dbContext.SaveChanges();
    return Ok(examComment);
}
🧪 Senaryo 9: Çevrimiçi Eğitim Sisteminde Sınav Yorumu
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/submit-exam-comment', methods=['POST'])
def submit_exam_comment():
    exam_id = request.form.get('examId')
    comment = request.form.get('comment')
    exam_comment = ExamComment(exam_id=exam_id, comment=comment, created_at=datetime.now())
    db.session.add(exam_comment)
    db.session.commit()
    return jsonify(exam_comment.to_dict())
🧪 Senaryo 9: Çevrimiçi Eğitim Sisteminde Sınav Yorumu
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.post('/submit-exam-comment', (req, res) => {
    const { examId, comment } = req.body;
    const examComment = new ExamComment({ examId, comment, createdAt: new Date() });
    examComment.save().then(() => res.json(examComment));
});
🧪 Senaryo 10: Restoran Değerlendirme Platformu
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpPost("submit-restaurant-review")]
public IActionResult SubmitRestaurantReview(string restaurantName, string review)
{
    var restaurantReview = new RestaurantReview
    {
        RestaurantName = restaurantName,
        Review = review,
        CreatedAt = DateTime.Now
    };
    _dbContext.RestaurantReviews.Add(restaurantReview);
    _dbContext.SaveChanges();
    return Ok(restaurantReview);
}
🧪 Senaryo 10: Restoran Değerlendirme Platformu
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
@app.route('/submit-restaurant-review', methods=['POST'])
def submit_restaurant_review():
    restaurant_name = request.form.get('restaurantName')
    review = request.form.get('review')
    restaurant_review = RestaurantReview(restaurant_name=restaurant_name, review=review, created_at=datetime.now())
    db.session.add(restaurant_review)
    db.session.commit()
    return jsonify(restaurant_review.to_dict())
🧪 Senaryo 10: Restoran Değerlendirme Platformu
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
app.post('/submit-restaurant-review', (req, res) => {
    const { restaurantName, review } = req.body;
    const restaurantReview = new RestaurantReview({ restaurantName, review, createdAt: new Date() });
    restaurantReview.save().then(() => res.json(restaurantReview));
});