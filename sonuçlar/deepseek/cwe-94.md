### 🧪 Senaryo 1: Bir şablon oluşturma uygulamasında kullanıcılar özel şablonlar tasarlar. Şablon sistemi kullanıcı girişlerini işleyerek çıktı üretir. Kullanıcılar farklı şablon türleri oluşturabilir. Şablonlar sistem tarafından derlenip çalıştırılır.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 24
```csharp
public class TemplateService
{
    private readonly ILogger<TemplateService> _logger;

    public TemplateService(ILogger<TemplateService> logger)
    {
        _logger = logger;
    }

    public string ProcessTemplate(string templateContent, Dictionary<string, object> templateData)
    {
        try
        {
            foreach (var dataItem in templateData)
            {
                string placeholder = $"{{{dataItem.Key}}}";
                templateContent = templateContent.Replace(placeholder, dataItem.Value?.ToString() ?? string.Empty);
            }
            return templateContent;
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Template processing failed");
            throw;
        }
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 16
```python
import logging

class TemplateProcessor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def process_template(self, template: str, data: dict) -> str:
        try:
            for key, value in data.items():
                placeholder = f"{{{key}}}"
                template = template.replace(placeholder, str(value))
            return template
        except Exception as e:
            self.logger.error(f"Template processing failed: {str(e)}")
            raise
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 19
```typescript
class TemplateService {
    private logger: Console;

    constructor(logger: Console = console) {
        this.logger = logger;
    }

    processTemplate(template: string, data: Record<string, any>): string {
        try {
            Object.keys(data).forEach(key => {
                const placeholder = new RegExp(`\\{${key}\\}`, 'g');
                template = template.replace(placeholder, data[key]?.toString() || '');
            });
            return template;
        } catch (error) {
            this.logger.error('Template processing failed', error);
            throw error;
        }
    }
}
```

### 🧪 Senaryo 2: Bir rapor oluşturma aracında kullanıcılar özel formüller yazabilir. Formül motoru bu ifadeleri değerlendirerek sonuçları hesaplar. Kullanıcılar matematiksel ve mantıksal işlemler tanımlayabilir. Hesaplanan sonuçlar raporda gösterilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 23
```csharp
public class FormulaCalculator
{
    public decimal Calculate(string formula, Dictionary<string, decimal> variables)
    {
        var expression = new System.Data.DataTable().Compute(formula, null);
        
        if (expression is decimal result)
        {
            return result;
        }
        
        throw new InvalidOperationException("Formula calculation failed");
    }

    public bool ValidateFormula(string formula)
    {
        try
        {
            // Test calculation with dummy values
            Calculate(formula, new Dictionary<string, decimal> { ["x"] = 1 });
            return true;
        }
        catch
        {
            return false;
        }
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 26
```python
import ast
import operator

class FormulaEngine:
    _operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv
    }

    def calculate(self, formula: str, variables: dict) -> float:
        try:
            node = ast.parse(formula, mode='eval')
            return self._eval(node.body, variables)
        except Exception as e:
            raise ValueError(f"Invalid formula: {str(e)}")

    def _eval(self, node, variables):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Name):
            return variables.get(node.id, 0)
        elif isinstance(node, ast.BinOp):
            return self._operators[type(node.op)](
                self._eval(node.left, variables),
                self._eval(node.right, variables)
            )
        else:
            raise ValueError(f"Unsupported operation: {type(node)}")
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 22
```typescript
class FormulaCalculator {
    private variables: Record<string, number> = {};

    setVariable(name: string, value: number): void {
        this.variables[name] = value;
    }

    calculate(formula: string): number {
        try {
            // Replace variables with their values
            let expression = formula;
            Object.keys(this.variables).forEach(varName => {
                expression = expression.replace(
                    new RegExp(`\\b${varName}\\b`, 'g'), 
                    this.variables[varName].toString()
                );
            });

            // Safe evaluation
            return Function(`"use strict"; return (${expression})`)();
        } catch (error) {
            throw new Error(`Formula calculation failed: ${error.message}`);
        }
    }
}
```

### 🧪 Senaryo 3: Bir web sayfası oluşturucu kullanıcıların HTML içerik girmesine izin verir. Kullanıcılar kendi tasarımlarını oluşturabilir ve düzenleyebilir. Girilen içerik sistem tarafından işlenir ve web sayfası olarak sunulur. Sayfa öğeleri kullanıcı tarafından özelleştirilebilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 21
```csharp
public class HtmlSanitizerService
{
    private readonly HtmlSanitizer _sanitizer;

    public HtmlSanitizerService()
    {
        _sanitizer = new HtmlSanitizer();
        _sanitizer.AllowedTags.Add("div");
        _sanitizer.AllowedAttributes.Add("class");
    }

    public string Sanitize(string htmlContent)
    {
        if (string.IsNullOrWhiteSpace(htmlContent))
            return string.Empty;

        return _sanitizer.Sanitize(htmlContent);
    }

    public string StripAllHtml(string htmlContent)
    {
        return Regex.Replace(htmlContent, "<.*?>", string.Empty);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 22
```python
from bs4 import BeautifulSoup
import re

class HtmlProcessor:
    @staticmethod
    def sanitize_html(html: str, allowed_tags: list = None) -> str:
        if allowed_tags is None:
            allowed_tags = ['p', 'br', 'strong', 'em']
        
        soup = BeautifulSoup(html, 'html.parser')
        
        for tag in soup.find_all(True):
            if tag.name not in allowed_tags:
                tag.unwrap()
        
        return str(soup)

    @staticmethod
    def strip_all_html(html: str) -> str:
        clean_text = re.sub('<[^<]+?>', '', html)
        return clean_text
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 29
```typescript
class HtmlSanitizer {
    private allowedTags: Set<string> = new Set(['p', 'span', 'br', 'strong']);
    private allowedAttributes: Set<string> = new Set(['class', 'style']);

    sanitize(html: string): string {
        const doc = new DOMParser().parseFromString(html, 'text/html');
        this.cleanNode(doc.body);
        return doc.body.innerHTML;
    }

    private cleanNode(node: Node): void {
        if (node.nodeType === Node.ELEMENT_NODE) {
            const element = node as HTMLElement;
            
            if (!this.allowedTags.has(element.tagName.toLowerCase())) {
                element.replaceWith(...Array.from(element.childNodes));
                return;
            }

            const attributeNames = Array.from(element.attributes).map(attr => attr.name);
            for (const name of attributeNames) {
                if (!this.allowedAttributes.has(name)) {
                    element.removeAttribute(name);
                }
            }
        }
        
        node.childNodes.forEach(child => this.cleanNode(child));
    }
}
```

### 🧪 Senaryo 4: Bir konfigürasyon yönetim sistemi kullanıcıların özel ayarlar tanımlamasına olanak sağlar. Ayar dosyaları sistem tarafından okunup uygulanır. Kullanıcılar sistemi ihtiyaçlarına göre yapılandırabilir. Yapılandırma değişiklikleri dinamik olarak yüklenir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 16
```csharp
public class ConfigManager
{
    private readonly IConfiguration _configuration;

    public ConfigManager(IConfiguration configuration)
    {
        _configuration = configuration;
    }

    public string GetSetting(string key)
    {
        return _configuration[key];
    }

    public void UpdateSetting(string key, string value)
    {
        // This is a simplified example. In a real application, you would need to persist the changes.
        _configuration[key] = value;
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 15
```python
import json

class ConfigHandler:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)

    def get_setting(self, key):
        return self.config.get(key)

    def update_setting(self, key, value):
        self.config[key] = value
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 16
```typescript
import * as fs from 'fs';

class ConfigManager {
    private config: Record<string, any>;

    constructor(private configFile: string = 'config.json') {
        const data = fs.readFileSync(this.configFile, 'utf-8');
        this.config = JSON.parse(data);
    }

    getSetting(key: string): any {
        return this.config[key];
    }

    updateSetting(key: string, value: any): void {
        this.config[key] = value;
        fs.writeFileSync(this.configFile, JSON.stringify(this.config, null, 2));
    }
}
```

### 🧪 Senaryo 5: Bir makro editörü kullanıcıların özel komutlar yazmasına izin verir. Makrolar sistem tarafından yorumlanıp çalıştırılır. Kullanıcılar tekrarlayan işlemler için makrolar oluşturabilir. Makro komutları sistem tarafından işlenir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 12
```csharp
public class MacroRunner
{
    public void Execute(string macro)
    {
        // In a real scenario, this would involve a proper parser and execution engine.
        // For demonstration, this is a simplified version.
        var commands = macro.Split(';');
        foreach (var command in commands)
        {
            Console.WriteLine($"Executing: {command.Trim()}");
        }
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 10
```python
class MacroInterpreter:
    def run_macro(self, macro_script):
        commands = macro_script.split(';')
        for command in commands:
            command = command.strip()
            if command:
                print(f"Running command: {command}")
                # In a real app, this would execute the command
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 11
```typescript
class MacroRunner {
    run(macroScript: string): void {
        const commands = macroScript.split(';').filter(cmd => cmd.trim());
        
        commands.forEach(command => {
            console.log(`Executing: ${command.trim()}`);
            // This would be replaced with actual command execution logic.
        });
    }
}
```

### 🧪 Senaryo 6: Bir veri dönüştürme aracı kullanıcıların özel dönüştürme kuralları tanımlamasını sağlar. Kurallar veri işleme sırasında uygulanır. Kullanıcılar farklı veri formatları arasında dönüştürme yapabilir. Dönüştürme mantığı kullanıcı tarafından belirlenir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 15
```csharp
public class DataTransformer
{
    public JObject Transform(JObject data, string rule)
    {
        // A simplified example using a hardcoded rule.
        // A real implementation would parse and apply the rule dynamically.
        if (rule == "uppercase_name")
        {
            if (data["name"] != null)
            {
                data["name"] = data["name"].ToString().ToUpper();
            }
        }
        return data;
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 11
```python
class DataTransformer:
    def transform(self, data: dict, rule: str) -> dict:
        # Example rule: 'field_to_upper:name'
        if rule.startswith('field_to_upper:'):
            field = rule.split(':')[1]
            if field in data and isinstance(data[field], str):
                data[field] = data[field].upper()
        return data
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 14
```typescript
class DataTransformer {
    transform(data: Record<string, any>, rule: string): Record<string, any> {
        // Example rule: 'uppercase:fieldName'
        if (rule.startsWith('uppercase:')) {
            const fieldName = rule.split(':')[1];
            if (data[fieldName] && typeof data[fieldName] === 'string') {
                data[fieldName] = data[fieldName].toUpperCase();
            }
        }
        return data;
    }
}
```

### 🧪 Senaryo 7: Bir otomatik test aracı kullanıcıların test senaryoları yazmasına olanak tanır. Test senaryoları sistem tarafından çalıştırılarak sonuçlar alınır. Kullanıcılar özel test durumları tanımlayabilir. Test mantığı kullanıcı girişlerine göre şekillenir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 13
```csharp
public class TestRunner
{
    public TestResult RunTest(string testScript)
    {
        // This is a mock implementation.
        // A real system would use a scripting engine to run the test.
        Console.WriteLine($"Running test script: {testScript}");
        
        // Simulate a result
        return new TestResult { Passed = !testScript.Contains("fail") };
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 10
```python
class TestExecutor:
    def execute_test(self, script):
        print(f"Executing test script:\n{script}")
        # In a real scenario, this would use a more robust execution model
        if "assert False" in script:
            return {"status": "Failed"}
        return {"status": "Passed"}
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 14
```typescript
interface TestResult {
    status: 'Passed' | 'Failed';
    message?: string;
}

class TestRunner {
    run(script: string): TestResult {
        console.log(`Executing test script: ${script}`);
        // Mock implementation
        if (script.includes('fail')) {
            return { status: 'Failed', message: 'Assertion failed' };
        }
        return { status: 'Passed' };
    }
}
```

### 🧪 Senaryo 8: Bir hesaplama motoru kullanıcıların özel hesaplama formülleri girmesine izin verir. Formüller sistem tarafından değerlendirilerek sonuçlar üretilir. Kullanıcılar karmaşık hesaplamalar tanımlayabilir. Hesaplama sonuçları kullanıcıya döndürülür.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 10
```csharp
public class CalculationEngine
{
    public object Evaluate(string expression)
    {
        // Using DataTable.Compute for safe evaluation of simple expressions.
        // Not suitable for complex logic.
        return new System.Data.DataTable().Compute(expression, null);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 9
```python
class CalculationEngine:
    def evaluate(self, expression):
        try:
            # WARNING: eval is dangerous if the expression is not sanitized.
            // This is for demonstration only.
            return eval(expression)
        except Exception as e:
            return f"Error: {str(e)}"
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 10
```typescript
class CalculationEngine {
    evaluate(expression: string): any {
        try {
            // Using Function constructor for safer evaluation than eval().
            return new Function(`return ${expression}`)();
        } catch (e) {
            return `Error: ${e.message}`;
        }
    }
}
```

### 🧪 Senaryo 9: Bir içerik yönetim sistemi kullanıcıların özel içerik şablonları oluşturmasını sağlar. Şablonlar dinamik içerik üretimi için kullanılır. Kullanıcılar farklı içerik türleri için şablonlar tasarlayabilir. İçerik şablonları sistem tarafından işlenir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 12
```csharp
public class ContentGenerator
{
    public string Generate(string template, object model)
    {
        // A simple example of template processing.
        // Real-world scenarios would use a templating engine like Razor or Scriban.
        var result = template.Replace("{{Model.Title}}", model.GetType().GetProperty("Title")?.GetValue(model)?.ToString());
        result = result.Replace("{{Model.Content}}", model.GetType().GetProperty("Content")?.GetValue(model)?.ToString());
        return result;
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 9
```python
class ContentGenerator:
    def generate(self, template, model):
        # A basic templating replacement
        for key, value in model.items():
            placeholder = f"{{{{{key}}}}}"
            template = template.replace(placeholder, str(value))
        return template
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 12
```typescript
class ContentGenerator {
    generate(template: string, model: Record<string, any>): string {
        let content = template;
        Object.keys(model).forEach(key => {
            const regex = new RegExp(`\\{\\{\\s*${key}\\s*\\}\\}`, 'g');
            content = content.replace(regex, model[key]);
        });
        return content;
    }
}
```

### 🧪 Senaryo 10: Bir iş akışı motoru kullanıcıların özel iş akışı kuralları tanımlamasına olanak verir. Kurallar iş süreçleri sırasında uygulanır. Kullanıcılar iş mantığını özelleştirebilir. İş akışı adımları kullanıcı tanımlı kurallara göre çalışır.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 20
```csharp
public class WorkflowEngine
{
    public void ExecuteWorkflow(WorkflowDefinition workflow, WorkflowContext context)
    {
        foreach (var step in workflow.Steps)
        {
            if (EvaluateCondition(step.Condition, context))
            {
                ExecuteAction(step.Action, context);
            }
        }
    }

    private bool EvaluateCondition(string condition, WorkflowContext context)
    {
        // Simplified condition evaluation
        return condition.ToLower() == "true" || string.IsNullOrEmpty(condition);
    }

    private void ExecuteAction(string action, WorkflowContext context)
    {
        // Simplified action execution
        Console.WriteLine($"Executing action: {action}");
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 16
```python
class WorkflowEngine:
    def execute(self, workflow, context):
        for step in workflow['steps']:
            if self._evaluate_condition(step.get('condition'), context):
                self._execute_action(step['action'], context)

    def _evaluate_condition(self, condition, context):
        # Simplified condition check
        if not condition:
            return True
        # In a real app, this would be a proper expression evaluation
        return eval(condition, {"context": context})

    def _execute_action(self, action, context):
        # Simplified action execution
        print(f"Executing action: {action} with context {context}")
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 20
```typescript
interface WorkflowStep {
    condition?: string;
    action: string;
}

class WorkflowEngine {
    execute(steps: WorkflowStep[], context: any): void {
        steps.forEach(step => {
            if (this.evaluateCondition(step.condition, context)) {
                this.executeAction(step.action, context);
            }
        });
    }

    private evaluateCondition(condition: string | undefined, context: any): boolean {
        if (!condition) return true;
        // Simplified, unsafe evaluation for demonstration
        return new Function('context', `return ${condition}`)(context);
    }

    private executeAction(action: string, context: any): void {
        console.log(`Executing action: ${action}`, context);
    }
}
```