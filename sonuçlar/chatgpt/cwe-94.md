### 🧪 Senaryo 1: Bir şablon oluşturma uygulamasında kullanıcılar özel şablonlar tasarlar. Şablon sistemi kullanıcı girişlerini işleyerek çıktı üretir. Kullanıcılar farklı şablon türleri oluşturabilir. Şablonlar sistem tarafından derlenip çalıştırılır.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 29
```csharp
[HttpPost("compile-template")]
public IActionResult CompileTemplate([FromBody] TemplateInput input)
{
    if (string.IsNullOrWhiteSpace(input.Content))
        return BadRequest("Template content is required.");

    try
    {
        string output = CompileTemplateContent(input.Content);
        return Ok(new { output });
    }
    catch (Exception ex)
    {
        return StatusCode(500, new { error = ex.Message });
    }
}

private string CompileTemplateContent(string content)
{
    // Replace placeholders like {{name}} with sample values
    var compiled = content.Replace("{{name}}", "Burak");
    compiled = compiled.Replace("{{date}}", DateTime.Now.ToShortDateString());
    return compiled;
}

public class TemplateInput
{
    public string Content { get; set; }
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```python
@app.route("/compile-template", methods=["POST"])
def compile_template():
    content = request.json.get("content", "")
    if not content:
        return jsonify(error="Template content is required"), 400

    compiled = content.replace("{{name}}", "Burak").replace("{{date}}", "2025-06-21")
    return jsonify(output=compiled)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 11
```typescript
app.post("/compile-template", (req, res) => {
    const content = req.body.content;
    if (!content) {
        return res.status(400).json({ error: "Template content is required" });
    }

    let compiled = content.replace(/{{name}}/g, "Burak");
    compiled = compiled.replace(/{{date}}/g, new Date().toLocaleDateString());

    res.json({ output: compiled });
});
```

---

### 🧪 Senaryo 2: Bir rapor oluşturma aracında kullanıcılar özel formüller yazabilir. Formül motoru bu ifadeleri değerlendirerek sonuçları hesaplar. Kullanıcılar matematiksel ve mantıksal işlemler tanımlayabilir. Hesaplanan sonuçlar raporda gösterilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 18
```csharp
[HttpPost("evaluate-formula")]
public IActionResult EvaluateFormula([FromBody] FormulaInput input)
{
    try
    {
        var result = FormulaEngine.Evaluate(input.Expression);
        return Ok(new { result });
    }
    catch
    {
        return BadRequest("Invalid formula expression.");
    }
}

public class FormulaInput
{
    public string Expression { get; set; }
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```python
@app.route("/evaluate-formula", methods=["POST"])
def evaluate_formula():
    expr = request.json.get("expression")
    try:
        result = eval_formula(expr)
        return jsonify(result=result)
    except:
        return jsonify(error="Invalid expression"), 400
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```typescript
app.post("/evaluate-formula", (req, res) => {
    try {
        const result = evaluateExpression(req.body.expression);
        res.json({ result });
    } catch {
        res.status(400).json({ error: "Invalid expression" });
    }
});
```

---

### 🧪 Senaryo 3: Bir web sayfası oluşturucu kullanıcıların HTML içerik girmesine izin verir. Kullanıcılar kendi tasarımlarını oluşturabilir ve düzenleyebilir. Girilen içerik sistem tarafından işlenir ve web sayfası olarak sunulur. Sayfa öğeleri kullanıcı tarafından özelleştirilebilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 21
```csharp
[HttpPost("render-html")]
public IActionResult RenderHtml([FromBody] HtmlContentInput input)
{
    if (string.IsNullOrWhiteSpace(input.Html))
        return BadRequest("HTML content is required.");

    string safeHtml = SanitizeHtml(input.Html);
    System.IO.File.WriteAllText("wwwroot/generated.html", safeHtml);
    return Ok(new { status = "Page created" });
}

private string SanitizeHtml(string html)
{
    // Basic example, in reality use HTML sanitizer libraries
    return html.Replace("<script", "&lt;script").Replace("onerror", "");
}

public class HtmlContentInput
{
    public string Html { get; set; }
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 10
```python
@app.route("/render-html", methods=["POST"])
def render_html():
    html = request.json.get("html", "")
    if not html:
        return jsonify(error="HTML content required"), 400

    safe_html = html.replace("<script", "&lt;script").replace("onerror", "")
    with open("static/generated.html", "w") as f:
        f.write(safe_html)
    return jsonify(status="Page created")
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```typescript
app.post("/render-html", (req, res) => {
    let html = req.body.html;
    if (!html) return res.status(400).json({ error: "HTML content required" });

    html = html.replace(/<script/gi, "&lt;script").replace(/onerror/gi, "");
    require("fs").writeFileSync("public/generated.html", html);
    res.json({ status: "Page created" });
});
```

---

### 🧪 Senaryo 4: Bir konfigürasyon yönetim sistemi kullanıcıların özel ayarlar tanımlamasına olanak sağlar. Ayar dosyaları sistem tarafından okunup uygulanır. Kullanıcılar sistemi ihtiyaçlarına göre yapılandırabilir. Yapılandırma değişiklikleri dinamik olarak yüklenir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 12
```csharp
[HttpPost("save-config")]
public IActionResult SaveConfiguration([FromBody] ConfigInput input)
{
    System.IO.File.WriteAllText("appsettings.custom.json", input.JsonConfig);
    ConfigurationManager.RefreshSection("appSettings");
    return Ok("Configuration saved.");
}

public class ConfigInput
{
    public string JsonConfig { get; set; }
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 6
```python
@app.route("/save-config", methods=["POST"])
def save_config():
    config = request.json.get("jsonConfig", "")
    with open("config/custom_config.json", "w") as f:
        f.write(config)
    return jsonify(status="Config saved")
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```typescript
app.post("/save-config", (req, res) => {
    const config = req.body.jsonConfig;
    if (config === undefined) {
        return res.status(400).json({ error: "Config content is required" });
    }
    require("fs").writeFileSync("config/custom_config.json", config);
    res.json({ status: "Configuration saved." });
});
```

---

### 🧪 Senaryo 5: Bir betik motoru kullanıcıların yazdığı kodları çalıştırır. Kodlar sistem içinde yorumlanarak yürütülür. Kullanıcılar çeşitli komutlar ve fonksiyonlar kullanabilir. Betik dili sistemin yeteneklerini genişletir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 13
```csharp
[HttpPost("run-script")]
public IActionResult RunScript([FromBody] ScriptInput input)
{
    try
    {
        var result = ScriptEngine.Execute(input.Script);
        return Ok(new { result });
    }
    catch
    {
        return BadRequest("Invalid script.");
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```python
@app.route("/run-script", methods=["POST"])
def run_script():
    script = request.json.get("script")
    try:
        result = exec(script)
        return jsonify(result=result)
    except Exception as e:
        return jsonify(error=str(e)), 400
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```typescript
app.post("/run-script", (req, res) => {
    try {
        const result = new Function(req.body.script)();
        res.json({ result: result ?? null });
    } catch (e) {
        res.status(400).json({ error: "Script execution failed" });
    }
});
```

---

### 🧪 Senaryo 6: Bir serileştirme kütüphanesi nesneleri metin formatına dönüştürür. Kullanıcılar özel veri türleri tanımlayabilir. Sistem bu türleri serileştirerek depolar veya ağ üzerinden gönderir. Nesneler daha sonra geri yüklenebilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 14
```csharp
[HttpPost("deserialize")]
public IActionResult Deserialize([FromBody] DataInput input)
{
    try
    {
        var obj = JsonConvert.DeserializeObject(input.Data);
        // Process the deserialized object...
        return Ok(new { status = "Object deserialized" });
    }
    catch
    {
        return BadRequest("Deserialization failed.");
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```python
@app.route("/deserialize", methods=["POST"])
def deserialize():
    data = request.json.get("data")
    try:
        obj = pickle.loads(data.encode())
        return jsonify(status="Object deserialized")
    except:
        return jsonify(error="Deserialization failed"), 400
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 9
```typescript
app.post("/deserialize", (req, res) => {
    try {
        const obj = JSON.parse(req.body.data);
        const deserialized = deserializeCustom(obj); // Fictional deserializer
        res.json({ status: "Object deserialized" });
    } catch {
        res.status(400).json({ error: "Deserialization failed" });
    }
});
```

---

### 🧪 Senaryo 7: Bir dinamik sınıf oluşturma aracı çalışma zamanında yeni sınıflar üretir. Kullanıcılar sınıf üyelerini ve metotlarını belirleyebilir. Sistem bu tanımlara göre yeni türler oluşturur. Bu sınıflar daha sonra uygulamada kullanılır.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 14
```csharp
[HttpPost("create-class")]
public IActionResult CreateClass([FromBody] ClassDefinition def)
{
    try
    {
        Type newClass = DynamicTypeBuilder.CreateType(def.ClassName, def.Properties);
        object instance = Activator.CreateInstance(newClass);
        return Ok("Class created");
    }
    catch
    {
        return BadRequest("Class creation failed.");
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 5
```python
@app.route("/create-class", methods=["POST"])
def create_class():
    def_data = request.json
    DynamicClass = type(def_data["name"], (object,), def_data["props"])
    return jsonify(status="Class created")
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 9
```typescript
app.post("/create-class", (req, res) => {
    try {
        const dynamicClass = createDynamicClass(req.body.definition);
        const instance = new dynamicClass();
        res.json({ result: instance.greet() });
    } catch {
        res.status(400).json({ error: "Class creation failed" });
    }
});
```

---

### 🧪 Senaryo 8: Bir uzak kod yürütme servisi istemciden gelen kodları sunucuda çalıştırır. Servis farklı dillerde kodları destekler. Kullanıcılar test veya otomasyon için kod gönderebilir. Sonuçlar istemciye geri gönderilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 14
```csharp
[HttpPost("remote-exec")]
public IActionResult RemoteExecute([FromBody] CodeExecutionRequest req)
{
    // This is extremely dangerous and should never be done in production
    try
    {
        var result = CodeDom.Compiler.CompileAndRun(req.Code);
        return Ok(new { result });
    }
    catch (Exception ex)
    {
        return BadRequest(ex.Message);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 5
```python
@app.route("/remote-exec", methods=["POST"])
def remote_exec():
    code = request.json.get("code")
    result = eval(code) # Extremely dangerous
    return jsonify(result=result)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 9
```typescript
app.post("/remote-exec", (req, res) => {
    try {
        // In a real scenario, this would be a sandboxed execution
        const result = eval(req.body.code);
        res.json({ result });
    } catch {
        res.status(400).json({ error: "Remote execution failed" });
    }
});
```

---

### 🧪 Senaryo 9: Bir dinamik sorgu oluşturucu kullanıcı girişlerine göre veritabanı sorguları üretir. Kullanıcılar filtreleme ve sıralama seçenekleri belirtebilir. Sistem bu seçenekleri SQL sorgusuna dönüştürür. Sorgular veritabanında çalıştırılır.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```csharp
[HttpGet("products")]
public IActionResult GetProducts(string category)
{
    // DANGER: SQL Injection vulnerability
    string query = "SELECT * FROM Products WHERE Category = '" + category + "'";
    var results = _dbContext.Products.FromSqlRaw(query).ToList();
    return Ok(results);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 6
```python
@app.route("/products")
def get_products():
    category = request.args.get("category")
    # DANGER: SQL Injection
    cursor.execute(f"SELECT * FROM products WHERE category = '{category}'")
    return jsonify(cursor.fetchall())
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 7
```typescript
app.get("/products", (req, res) => {
    const query = `SELECT * FROM products WHERE category = '${req.body.category}'`;
    db.query(query, (err, results) => {
        if (err) return res.status(500).json({ error: "Query failed" });
        res.json(results);
    });
});
```

---

### 🧪 Senaryo 10: Bir işletim sistemi kabuğu kullanıcı komutlarını yorumlar ve çalıştırır. Kullanıcılar sistem yönetimi ve dosya işlemleri yapabilir. Komutlar alt süreçler olarak yürütülür. Kabuk komutların çıktısını kullanıcıya gösterir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```csharp
[HttpPost("run-command")]
public IActionResult RunCommand(string command)
{
    // DANGER: Command Injection
    var process = Process.Start("cmd.exe", "/c " + command);
    process.WaitForExit();
    return Ok("Command executed");
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 6
```python
@app.route("/run-command", methods=["POST"])
def run_command():
    command = request.json.get("command")
    # DANGER: Command Injection
    os.system(command)
    return jsonify(status="Command executed")
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
**Satır Sayısı:** 8
```typescript
app.post("/run-command", (req, res) => {
    const { command } = req.body;
    // DANGER: Command Injection
    const child = require("child_process").exec(command, (err, stdout, stderr) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json({ stdout, stderr });
    });
});
```
