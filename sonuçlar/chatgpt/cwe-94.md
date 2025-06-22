 ----
### 🧪 Senaryo 1: Bir şablon oluşturma uygulamasında kullanıcılar özel şablonlar tasarlar. Şablon sistemi kullanıcı girişlerini işleyerek çıktı üretir. Kullanıcılar farklı şablon türleri oluşturabilir. Şablonlar sistem tarafından derlenip çalıştırılır.
**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT

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

----
### 🧪 Senaryo 1: Bir şablon oluşturma uygulamasında kullanıcılar özel şablonlar tasarlar. Şablon sistemi kullanıcı girişlerini işleyerek çıktı üretir. Kullanıcılar farklı şablon türleri oluşturabilir. Şablonlar sistem tarafından derlenip çalıştırılır.
**💻 Dil:** `Python`  
**🤖 AI:** ChatGPT

```python
@app.route("/compile-template", methods=["POST"])
def compile_template():
    content = request.json.get("content", "")
    if not content:
        return jsonify(error="Template content is required"), 400

    compiled = content.replace("{{name}}", "Burak").replace("{{date}}", "2025-06-21")
    return jsonify(output=compiled)
```

----
### 🧪 Senaryo 1: Bir şablon oluşturma uygulamasında kullanıcılar özel şablonlar tasarlar. Şablon sistemi kullanıcı girişlerini işleyerek çıktı üretir. Kullanıcılar farklı şablon türleri oluşturabilir. Şablonlar sistem tarafından derlenip çalıştırılır.
**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT

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

----
### 🧪 Senaryo 2: Bir rapor oluşturma aracında kullanıcılar özel formüller yazabilir. Formül motoru bu ifadeleri değerlendirerek sonuçları hesaplar. Kullanıcılar matematiksel ve mantıksal işlemler tanımlayabilir. Hesaplanan sonuçlar raporda gösterilir.
**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT

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

----
### 🧪 Senaryo 2: Bir rapor oluşturma aracında kullanıcılar özel formüller yazabilir. Formül motoru bu ifadeleri değerlendirerek sonuçları hesaplar. Kullanıcılar matematiksel ve mantıksal işlemler tanımlayabilir. Hesaplanan sonuçlar raporda gösterilir.
**💻 Dil:** `Python`  
**🤖 AI:** ChatGPT

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

----
### 🧪 Senaryo 2: Bir rapor oluşturma aracında kullanıcılar özel formüller yazabilir. Formül motoru bu ifadeleri değerlendirerek sonuçları hesaplar. Kullanıcılar matematiksel ve mantıksal işlemler tanımlayabilir. Hesaplanan sonuçlar raporda gösterilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT

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

----
### 🧪 Senaryo 3: Bir web sayfası oluşturucu kullanıcıların HTML içerik girmesine izin verir. Kullanıcılar kendi tasarımlarını oluşturabilir ve düzenleyebilir. Girilen içerik sistem tarafından işlenir ve web sayfası olarak sunulur. Sayfa öğeleri kullanıcı tarafından özelleştirilebilir.
**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT

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

----
### 🧪 Senaryo 3: Bir web sayfası oluşturucu kullanıcıların HTML içerik girmesine izin verir. Kullanıcılar kendi tasarımlarını oluşturabilir ve düzenleyebilir. Girilen içerik sistem tarafından işlenir ve web sayfası olarak sunulur. Sayfa öğeleri kullanıcı tarafından özelleştirilebilir.
**💻 Dil:** `Python`  
**🤖 AI:** ChatGPT

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

----
### 🧪 Senaryo 3: Bir web sayfası oluşturucu kullanıcıların HTML içerik girmesine izin verir. Kullanıcılar kendi tasarımlarını oluşturabilir ve düzenleyebilir. Girilen içerik sistem tarafından işlenir ve web sayfası olarak sunulur. Sayfa öğeleri kullanıcı tarafından özelleştirilebilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT

```typescript
app.post("/render-html", (req, res) => {
    let html = req.body.html;
    if (!html) return res.status(400).json({ error: "HTML content required" });

    html = html.replace(/<script/gi, "&lt;script").replace(/onerror/gi, "");
    require("fs").writeFileSync("public/generated.html", html);
    res.json({ status: "Page created" });
});
```

----
### 🧪 Senaryo 4: Bir konfigürasyon yönetim sistemi kullanıcıların özel ayarlar tanımlamasına olanak sağlar. Ayar dosyaları sistem tarafından okunup uygulanır. Kullanıcılar sistemi ihtiyaçlarına göre yapılandırabilir. Yapılandırma değişiklikleri dinamik olarak yüklenir.
**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT

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

----
### 🧪 Senaryo 4: Bir konfigürasyon yönetim sistemi kullanıcıların özel ayarlar tanımlamasına olanak sağlar. Ayar dosyaları sistem tarafından okunup uygulanır. Kullanıcılar sistemi ihtiyaçlarına göre yapılandırabilir. Yapılandırma değişiklikleri dinamik olarak yüklenir.
**💻 Dil:** `Python`  
**🤖 AI:** ChatGPT

```python
@app.route("/save-config", methods=["POST"])
def save_config():
    config = request.json.get("jsonConfig", "")
    with open("config/custom_config.json", "w") as f:
        f.write(config)
    return jsonify(status="Configuration saved.")
```

----
### 🧪 Senaryo 4: Bir konfigürasyon yönetim sistemi kullanıcıların özel ayarlar tanımlamasına olanak sağlar. Ayar dosyaları sistem tarafından okunup uygulanır. Kullanıcılar sistemi ihtiyaçlarına göre yapılandırabilir. Yapılandırma değişiklikleri dinamik olarak yüklenir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT

```typescript
app.post("/save-config", (req, res) => {
    const config = req.body.jsonConfig;
    require("fs").writeFileSync("config/custom-config.json", config);
    res.json({ status: "Configuration saved." });
});
```

----
### 🧪 Senaryo 5: Bir makro editörü kullanıcıların özel komutlar yazmasına izin verir. Makrolar sistem tarafından yorumlanıp çalıştırılır. Kullanıcılar tekrarlayan işlemler için makrolar oluşturabilir. Makro komutları sistem tarafından işlenir.
**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT

```csharp
[HttpPost("run-macro")]
public IActionResult RunMacro([FromBody] MacroInput input)
{
    string result = ExecuteMacro(input.Commands);
    return Ok(new { result });
}

private string ExecuteMacro(string command)
{
    if (command == "OPEN_FILE") return "File opened.";
    if (command == "CLOSE_FILE") return "File closed.";
    return "Unknown macro.";
}

public class MacroInput
{
    public string Commands { get; set; }
}
```

----
### 🧪 Senaryo 5: Bir makro editörü kullanıcıların özel komutlar yazmasına izin verir. Makrolar sistem tarafından yorumlanıp çalıştırılır. Kullanıcılar tekrarlayan işlemler için makrolar oluşturabilir. Makro komutları sistem tarafından işlenir.
**💻 Dil:** `Python`  
**🤖 AI:** ChatGPT

```python
@app.route("/run-macro", methods=["POST"])
def run_macro():
    cmd = request.json.get("commands", "")
    if cmd == "OPEN_FILE":
        return jsonify(result="File opened.")
    elif cmd == "CLOSE_FILE":
        return jsonify(result="File closed.")
    return jsonify(result="Unknown macro.")
```

----
### 🧪 Senaryo 5: Bir makro editörü kullanıcıların özel komutlar yazmasına izin verir. Makrolar sistem tarafından yorumlanıp çalıştırılır. Kullanıcılar tekrarlayan işlemler için makrolar oluşturabilir. Makro komutları sistem tarafından işlenir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT

```typescript
app.post("/run-macro", (req, res) => {
    const cmd = req.body.commands;
    const result = cmd === "OPEN_FILE" ? "File opened." :
                   cmd === "CLOSE_FILE" ? "File closed." : "Unknown macro.";
    res.json({ result });
});
```

----
### 🧪 Senaryo 6: Bir veri dönüştürme aracı kullanıcıların özel dönüştürme kuralları tanımlamasını sağlar. Kurallar veri işleme sırasında uygulanır. Kullanıcılar farklı veri formatları arasında dönüştürme yapabilir. Dönüştürme mantığı kullanıcı tarafından belirlenir.
**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT

```csharp
[HttpPost("transform-data")]
public IActionResult TransformData([FromBody] TransformInput input)
{
    string transformed = input.Data.Replace(input.Find, input.Replace);
    return Ok(new { transformed });
}

public class TransformInput
{
    public string Data { get; set; }
    public string Find { get; set; }
    public string Replace { get; set; }
}
```

----
### 🧪 Senaryo 6: Bir veri dönüştürme aracı kullanıcıların özel dönüştürme kuralları tanımlamasını sağlar. Kurallar veri işleme sırasında uygulanır. Kullanıcılar farklı veri formatları arasında dönüştürme yapabilir. Dönüştürme mantığı kullanıcı tarafından belirlenir.
**💻 Dil:** `Python`  
**🤖 AI:** ChatGPT

```python
@app.route("/transform-data", methods=["POST"])
def transform_data():
    data = request.json.get("data")
    find = request.json.get("find")
    replace = request.json.get("replace")
    transformed = data.replace(find, replace)
    return jsonify(transformed=transformed)
```

----
### 🧪 Senaryo 6: Bir veri dönüştürme aracı kullanıcıların özel dönüştürme kuralları tanımlamasını sağlar. Kurallar veri işleme sırasında uygulanır. Kullanıcılar farklı veri formatları arasında dönüştürme yapabilir. Dönüştürme mantığı kullanıcı tarafından belirlenir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT

```typescript
app.post("/transform-data", (req, res) => {
    const { data, find, replace } = req.body;
    const transformed = data.replace(new RegExp(find, "g"), replace);
    res.json({ transformed });
});
```

----
### 🧪 Senaryo 7: Bir otomatik test aracı kullanıcıların test senaryoları yazmasına olanak tanır. Test senaryoları sistem tarafından çalıştırılarak sonuçlar alınır. Kullanıcılar özel test durumları tanımlayabilir. Test mantığı kullanıcı girişlerine göre şekillenir.
**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT

```csharp
[HttpPost("run-test")]
public IActionResult RunTest([FromBody] TestInput input)
{
    bool passed = input.Expected == input.Actual;
    return Ok(new { result = passed ? "PASS" : "FAIL" });
}

public class TestInput
{
    public string Expected { get; set; }
    public string Actual { get; set; }
}
```

----
### 🧪 Senaryo 7: Bir otomatik test aracı kullanıcıların test senaryoları yazmasına olanak tanır. Test senaryoları sistem tarafından çalıştırılarak sonuçlar alınır. Kullanıcılar özel test durumları tanımlayabilir. Test mantığı kullanıcı girişlerine göre şekillenir.
**💻 Dil:** `Python`  
**🤖 AI:** ChatGPT

```python
@app.route("/run-test", methods=["POST"])
def run_test():
    expected = request.json.get("expected")
    actual = request.json.get("actual")
    result = "PASS" if expected == actual else "FAIL"
    return jsonify(result=result)
```

----
### 🧪 Senaryo 7: Bir otomatik test aracı kullanıcıların test senaryoları yazmasına olanak tanır. Test senaryoları sistem tarafından çalıştırılarak sonuçlar alınır. Kullanıcılar özel test durumları tanımlayabilir. Test mantığı kullanıcı girişlerine göre şekillenir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT

```typescript
app.post("/run-test", (req, res) => {
    const { expected, actual } = req.body;
    const result = expected === actual ? "PASS" : "FAIL";
    res.json({ result });
});
```

----
### 🧪 Senaryo 8: Bir hesaplama motoru kullanıcıların özel hesaplama formülleri girmesine izin verir. Formüller sistem tarafından değerlendirilerek sonuçlar üretilir. Kullanıcılar karmaşık hesaplamalar tanımlayabilir. Hesaplama sonuçları kullanıcıya döndürülür.
**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT

```csharp
[HttpPost("calculate")]
public IActionResult Calculate([FromBody] CalcInput input)
{
    var result = new DataTable().Compute(input.Formula, null);
    return Ok(new { result });
}

public class CalcInput
{
    public string Formula { get; set; }
}
```

----
### 🧪 Senaryo 8: Bir hesaplama motoru kullanıcıların özel hesaplama formülleri girmesine izin verir. Formüller sistem tarafından değerlendirilerek sonuçlar üretilir. Kullanıcılar karmaşık hesaplamalar tanımlayabilir. Hesaplama sonuçları kullanıcıya döndürülür.
**💻 Dil:** `Python`  
**🤖 AI:** ChatGPT

```python
@app.route("/calculate", methods=["POST"])
def calculate():
    formula = request.json.get("formula", "")
    try:
        result = eval(formula)
        return jsonify(result=result)
    except:
        return jsonify(error="Invalid formula"), 400
```

----
### 🧪 Senaryo 8: Bir hesaplama motoru kullanıcıların özel hesaplama formülleri girmesine izin verir. Formüller sistem tarafından değerlendirilerek sonuçlar üretilir. Kullanıcılar karmaşık hesaplamalar tanımlayabilir. Hesaplama sonuçları kullanıcıya döndürülür.
**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT

```typescript
app.post("/calculate", (req, res) => {
    const formula = req.body.formula;
    try {
        const result = eval(formula); // only safe in trusted environments
        res.json({ result });
    } catch {
        res.status(400).json({ error: "Invalid formula" });
    }
});
```

----
### 🧪 Senaryo 9: Bir içerik yönetim sistemi kullanıcıların özel içerik şablonları oluşturmasını sağlar. Şablonlar dinamik içerik üretimi için kullanılır. Kullanıcılar farklı içerik türleri için şablonlar tasarlayabilir. İçerik şablonları sistem tarafından işlenir.
**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT

```csharp
[HttpPost("generate-content")]
public IActionResult GenerateContent([FromBody] ContentInput input)
{
    string result = input.Template.Replace("{{title}}", input.Title).Replace("{{body}}", input.Body);
    return Ok(new { content = result });
}

public class ContentInput
{
    public string Template { get; set; }
    public string Title { get; set; }
    public string Body { get; set; }
}
```

----
### 🧪 Senaryo 9: Bir içerik yönetim sistemi kullanıcıların özel içerik şablonları oluşturmasını sağlar. Şablonlar dinamik içerik üretimi için kullanılır. Kullanıcılar farklı içerik türleri için şablonlar tasarlayabilir. İçerik şablonları sistem tarafından işlenir.
**💻 Dil:** `Python`  
**🤖 AI:** ChatGPT

```python
@app.route("/generate-content", methods=["POST"])
def generate_content():
    tpl = request.json.get("template", "")
    title = request.json.get("title", "")
    body = request.json.get("body", "")
    content = tpl.replace("{{title}}", title).replace("{{body}}", body)
    return jsonify(content=content)
```

----
### 🧪 Senaryo 9: Bir içerik yönetim sistemi kullanıcıların özel içerik şablonları oluşturmasını sağlar. Şablonlar dinamik içerik üretimi için kullanılır. Kullanıcılar farklı içerik türleri için şablonlar tasarlayabilir. İçerik şablonları sistem tarafından işlenir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT

```typescript
app.post("/generate-content", (req, res) => {
    const { template, title, body } = req.body;
    const content = template.replace(/{{title}}/g, title).replace(/{{body}}/g, body);
    res.json({ content });
});
```

----
### 🧪 Senaryo 10: Bir iş akışı motoru kullanıcıların özel iş akışı kuralları tanımlamasına olanak verir. Kurallar iş süreçleri sırasında uygulanır. Kullanıcılar iş mantığını özelleştirebilir. İş akışı adımları kullanıcı tanımlı kurallara göre çalışır.
**💻 Dil:** `C#`  
**🤖 AI:** ChatGPT

```csharp
[HttpPost("run-workflow")]
public IActionResult RunWorkflow([FromBody] WorkflowInput input)
{
    var steps = input.Steps.Split(',');
    var result = steps.Select(s => $"Step {s} completed").ToList();
    return Ok(new { log = result });
}

public class WorkflowInput
{
    public string Steps { get; set; }
}
```

----
### 🧪 Senaryo 10: Bir iş akışı motoru kullanıcıların özel iş akışı kuralları tanımlamasına olanak verir. Kurallar iş süreçleri sırasında uygulanır. Kullanıcılar iş mantığını özelleştirebilir. İş akışı adımları kullanıcı tanımlı kurallara göre çalışır.
**💻 Dil:** `Python`  
**🤖 AI:** ChatGPT

```python
@app.route("/run-workflow", methods=["POST"])
def run_workflow():
    steps = request.json.get("steps", "").split(",")
    log = [f"Step {s} completed" for s in steps]
    return jsonify(log=log)
```

----
### 🧪 Senaryo 10: Bir iş akışı motoru kullanıcıların özel iş akışı kuralları tanımlamasına olanak verir. Kurallar iş süreçleri sırasında uygulanır. Kullanıcılar iş mantığını özelleştirebilir. İş akışı adımları kullanıcı tanımlı kurallara göre çalışır.
**💻 Dil:** `TypeScript`  
**🤖 AI:** ChatGPT

```typescript
app.post("/run-workflow", (req, res) => {
    const steps = req.body.steps.split(",");
    const log = steps.map((s: string) => `Step ${s} completed`);
    res.json({ log });
});
```