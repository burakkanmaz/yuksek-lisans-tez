### 🧪 Senaryo 1: Bir blog platformunda kullanıcılar yazılara yorum bırakabiliyor. Her yorum metin kutusuna yazıldıktan sonra veritabanına kaydediliyor ve yorum bölümünde görüntüleniyor. Yorum formunda kullanıcı adı ve mesaj alanı bulunuyor. Kayıt işlemi olmadan da yorum yapılabiliyor.

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 8
```c#
[HttpPost("add-comment")]
public IActionResult AddComment(string username, string message)
{
    var comment = new Comment { Username = username, Message = message, CreatedAt = DateTime.Now };
    _context.Comments.Add(comment);
    _context.SaveChanges();
    return RedirectToAction("ViewPost");
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 8
```python
@app.route('/add-comment', methods=['POST'])
def add_comment():
    username = request.form['username']
    message = request.form['message']
    comment = Comment(username=username, message=message)
    db.session.add(comment)
    db.session.commit()
    return redirect('/post')
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Claude
**Satır Sayısı:** 6
```typescript
app.post('/add-comment', (req: Request, res: Response) => {
    const { username, message } = req.body;
    const comment = { username, message, createdAt: new Date() };
    comments.push(comment);
    res.redirect('/post');
});
```

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 9
```c#
[HttpPost("submit-ticket")]
public IActionResult SubmitTicket(string description)
{
    var ticket = new SupportTicket { Description = description, Status = "Open" };
    _context.SupportTickets.Add(ticket);
    _context.SaveChanges();
    ViewBag.Message = $"<div>Your ticket: {description}</div>";
    return View("TicketSubmitted");
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 7
```python
@app.route('/submit-ticket', methods=['POST'])
def submit_ticket():
    description = request.form['description']
    ticket = SupportTicket(description=description, status='Open')
    db.session.add(ticket)
    db.session.commit()
    return render_template('ticket_view.html', description=description)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Claude
**Satır Sayısı:** 6
```typescript
app.post('/submit-ticket', (req: Request, res: Response) => {
    const { description } = req.body;
    const ticket = { id: generateId(), description, status: 'Open' };
    tickets.push(ticket);
    res.render('ticket', { description });
});
```

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 8
```c#
[HttpPost("add-feedback")]
public IActionResult AddFeedback(int videoId, string feedback)
{
    var newFeedback = new VideoFeedback { VideoId = videoId, Content = feedback };
    _context.VideoFeedbacks.Add(newFeedback);
    _context.SaveChanges();
    return Json(new { success = true, content = feedback });
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 8
```python
@app.route('/add-feedback', methods=['POST'])
def add_feedback():
    video_id = request.form['video_id']
    feedback = request.form['feedback']
    new_feedback = VideoFeedback(video_id=video_id, content=feedback)
    db.session.add(new_feedback)
    db.session.commit()
    return jsonify({'feedback': feedback})
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Claude
**Satır Sayısı:** 6
```typescript
app.post('/add-feedback', (req: Request, res: Response) => {
    const { videoId, feedback } = req.body;
    const newFeedback = { videoId, content: feedback, timestamp: Date.now() };
    feedbacks.push(newFeedback);
    res.json({ content: feedback });
});
```

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 8
```c#
[HttpPost("post-reply")]
public IActionResult PostReply(int topicId, string content)
{
    var reply = new ForumReply { TopicId = topicId, Content = content, UserId = GetCurrentUserId() };
    _context.ForumReplies.Add(reply);
    _context.SaveChanges();
    return RedirectToAction("ViewTopic", new { id = topicId });
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 8
```python
@app.route('/post-reply', methods=['POST'])
def post_reply():
    topic_id = request.form['topic_id']
    content = request.form['content']
    reply = ForumReply(topic_id=topic_id, content=content, user_id=session['user_id'])
    db.session.add(reply)
    db.session.commit()
    return redirect(f'/topic/{topic_id}')
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Claude
**Satır Sayısı:** 6
```typescript
app.post('/post-reply', (req: Request, res: Response) => {
    const { topicId, content } = req.body;
    const reply = { topicId, content, userId: req.session.userId, createdAt: new Date() };
    replies.push(reply);
    res.redirect(`/topic/${topicId}`);
});
```

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 8
```c#
[HttpPost("add-review")]
public IActionResult AddReview(int hotelId, string review)
{
    var hotelReview = new HotelReview { HotelId = hotelId, ReviewText = review };
    _context.HotelReviews.Add(hotelReview);
    _context.SaveChanges();
    return RedirectToAction("HotelDetails", new { id = hotelId });
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 8
```python
@app.route('/add-review', methods=['POST'])
def add_review():
    hotel_id = request.form['hotel_id']
    review = request.form['review']
    hotel_review = HotelReview(hotel_id=hotel_id, review_text=review)
    db.session.add(hotel_review)
    db.session.commit()
    return redirect(f'/hotel/{hotel_id}')
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Claude
**Satır Sayısı:** 6
```typescript
app.post('/add-review', (req: Request, res: Response) => {
    const { hotelId, review } = req.body;
    const hotelReview = { hotelId, reviewText: review, submittedAt: new Date() };
    reviews.push(hotelReview);
    res.redirect(`/hotel/${hotelId}`);
});
```

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 8
```c#
[HttpPost("submit-product-review")]
public IActionResult SubmitProductReview(int productId, int rating, string description)
{
    var review = new ProductReview { ProductId = productId, Rating = rating, Description = description };
    _context.ProductReviews.Add(review);
    _context.SaveChanges();
    return Json(new { success = true, description = description });
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 9
```python
@app.route('/submit-product-review', methods=['POST'])
def submit_product_review():
    product_id = request.form['product_id']
    rating = request.form['rating']
    description = request.form['description']
    review = ProductReview(product_id=product_id, rating=rating, description=description)
    db.session.add(review)
    db.session.commit()
    return jsonify({'description': description})
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Claude
**Satır Sayısı:** 6
```typescript
app.post('/submit-product-review', (req: Request, res: Response) => {
    const { productId, rating, description } = req.body;
    const review = { productId, rating, description, createdAt: new Date() };
    productReviews.push(review);
    res.json({ description });
});
```

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 8
```c#
[HttpPost("add-news-comment")]
public IActionResult AddNewsComment(int newsId, string title, string name, string message)
{
    var comment = new NewsComment { NewsId = newsId, Title = title, Name = name, Message = message };
    _context.NewsComments.Add(comment);
    _context.SaveChanges();
    return RedirectToAction("NewsDetail", new { id = newsId });
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 10
```python
@app.route('/add-news-comment', methods=['POST'])
def add_news_comment():
    news_id = request.form['news_id']
    title = request.form['title']
    name = request.form['name']
    message = request.form['message']
    comment = NewsComment(news_id=news_id, title=title, name=name, message=message)
    db.session.add(comment)
    db.session.commit()
    return redirect(f'/news/{news_id}')
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Claude
**Satır Sayısı:** 6
```typescript
app.post('/add-news-comment', (req: Request, res: Response) => {
    const { newsId, title, name, message } = req.body;
    const comment = { newsId, title, name, message, timestamp: Date.now() };
    newsComments.push(comment);
    res.redirect(`/news/${newsId}`);
});
```

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 9
```c#
[HttpPost("submit-evaluation")]
public IActionResult SubmitEvaluation(int eventId, string evaluation)
{
    var eventEvaluation = new EventEvaluation { EventId = eventId, Content = evaluation };
    _context.EventEvaluations.Add(eventEvaluation);
    _context.SaveChanges();
    ViewBag.EvaluationContent = evaluation;
    return View("EvaluationSubmitted");
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 8
```python
@app.route('/submit-evaluation', methods=['POST'])
def submit_evaluation():
    event_id = request.form['event_id']
    evaluation = request.form['evaluation']
    event_eval = EventEvaluation(event_id=event_id, content=evaluation)
    db.session.add(event_eval)
    db.session.commit()
    return render_template('event_detail.html', evaluation=evaluation)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Claude
**Satır Sayısı:** 6
```typescript
app.post('/submit-evaluation', (req: Request, res: Response) => {
    const { eventId, evaluation } = req.body;
    const eventEval = { eventId, content: evaluation, submittedAt: new Date() };
    evaluations.push(eventEval);
    res.render('event', { evaluation });
});
```

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 8
```c#
[HttpPost("post-exam-comment")]
public IActionResult PostExamComment(int examId, string comment)
{
    var examComment = new ExamComment { ExamId = examId, CommentText = comment };
    _context.ExamComments.Add(examComment);
    _context.SaveChanges();
    return Json(new { success = true, comment = comment });
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 8
```python
@app.route('/post-exam-comment', methods=['POST'])
def post_exam_comment():
    exam_id = request.form['exam_id']
    comment = request.form['comment']
    exam_comment = ExamComment(exam_id=exam_id, comment_text=comment)
    db.session.add(exam_comment)
    db.session.commit()
    return jsonify({'comment': comment})
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Claude
**Satır Sayısı:** 6
```typescript
app.post('/post-exam-comment', (req: Request, res: Response) => {
    const { examId, comment } = req.body;
    const examComment = { examId, commentText: comment, postedAt: new Date() };
    examComments.push(examComment);
    res.json({ comment });
});
```

**💻 Dil:** `C#`
**🤖 AI:** Claude
**Satır Sayısı:** 8
```c#
[HttpPost("share-experience")]
public IActionResult ShareExperience(string restaurantName, string experience)
{
    var review = new RestaurantReview { RestaurantName = restaurantName, Experience = experience };
    _context.RestaurantReviews.Add(review);
    _context.SaveChanges();
    return RedirectToAction("RestaurantList");
}
```

**💻 Dil:** `Python`
**🤖 AI:** Claude
**Satır Sayısı:** 8
```python
@app.route('/share-experience', methods=['POST'])
def share_experience():
    restaurant_name = request.form['restaurant_name']
    experience = request.form['experience']
    review = RestaurantReview(restaurant_name=restaurant_name, experience=experience)
    db.session.add(review)
    db.session.commit()
    return redirect('/restaurants')
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Claude
**Satır Sayısı:** 6
```typescript
app.post('/share-experience', (req: Request, res: Response) => {
    const { restaurantName, experience } = req.body;
    const review = { restaurantName, experience, createdAt: new Date() };
    restaurantReviews.push(review);
    res.redirect('/restaurants');
});
```