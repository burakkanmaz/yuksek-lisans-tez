### 🧪 Senaryo 1: Kullanıcılar özel şablonlar tasarlar
**💻 Dil:** `C#`Grok
**🤖 AI:** Grok
**Satır Sayısı:** 23
```csharp
public class TemplateEngine
{
    private readonly ITemplateRepository _repository;

    public TemplateEngine(ITemplateRepository repository)
    {
        _repository = repository;
    }

    public async Task<string> CompileTemplateAsync(string templateId, Dictionary<string, string> inputs)
    {
        var template = await _repository.GetTemplateAsync(templateId);
        if (template == null)
        {
            throw new ArgumentException("Template not found", nameof(templateId));
        }

        string result = template.Content;
        foreach (var input in inputs)
        {
            result = result.Replace($"{{{{{input.Key}}}}}", input.Value, StringComparison.OrdinalIgnoreCase);
        }

        await _repository.SaveCompiledTemplateAsync(templateId, result);
        return result;
    }
}
```
**💻 Dil:** `Python`
**🤖 AI:** Grok
**Satır Sayısı:** 14
```python
from typing import Dict
from database import TemplateRepository

class TemplateEngine:
    def __init__(self, repository: TemplateRepository):
        self._repository = repository

    async def compile_template(self, template_id: str, inputs: Dict[str, str]) -> str:
        template = await self._repository.get_template(template_id)
        if not template:
            raise ValueError(f"Template {template_id} not found")

        result = template.content
        for key, value in inputs.items():
            result = result.replace(f"{{{key}}}", value)

        await self._repository.save_compiled_template(template_id, result)
        return resultGrok
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok
**Satır Sayısı:** 23
```typescript
interface Template {
    id: string;
    content: string;
}

interface TemplateRepository {
    getTemplate(id: string): Promise<Template>;
    saveCompiledTemplate(id: string, content: string): Promise<void>;
}

class TemplateEngine {
    constructor(private repository: TemplateRepository) {}

    async compileTemplate(templateId: string, inputs: Record<string, string>): Promise<string> {
        const template = await this.repository.getTemplate(templateId);
        if (!template) {
            throw new Error(`Template ${templateId} not found`);
        }

        let result = template.content;
        for (const [key, value] of Object.entries(inputs)) {
            result = result.replace(new RegExp(`{${key}}`, 'gi'), value);
        }

        await this.repository.saveCompiledTemplate(templateId, result);
        return result;
    }
}Grok
```

### 🧪 Senaryo 2: Kullanıcılar özel formüller yazabilir
**💻 Dil:** `C#`
**🤖 AI:** Grok
**Satır Sayısı:** 21
```csharp
using NCalc;

public class FormulaEngine
{
    public async Task<double> EvaluateFormulaAsync(string formula, Dictionary<string, double> parameters)
    {
        try
        {
            var expression = new Expression(formula);
            foreach (var param in parameters)
            {
                expression.Parameters[param.Key] = param.Value;
            }

            var result = await Task.Run(() => expression.Evaluate());
            return Convert.ToDouble(result);
        }
        catch (Exception ex)
        {
            throw new InvalidOperationException("Formula evaluation failed", ex);
        }Grok
    }
}
```
**💻 Dil:** `Python`
**🤖 AI:** Grok
**Satır Sayısı:** 11
```python
import evalex
from typing import Dict

class FormulaEngine:
    async def evaluate_formula(self, formula: str, parameters: Dict[str, float]) -> float:
        try:
            expr = evalex.Expression(formula)
            for key, value in parameters.items():
                expr.set_variaGroky, value)
            return await expr.evaluate_async()
        except Exception as e:
            raise RuntimeError(f"Formula evaluation failed: {str(e)}")
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok
**Satır Sayısı:** 10
```typescript
import { evaluate } from 'mathjs';

class FormulaEngine {
    async evaluateFormula(formula: string, parameters: Record<string, number>): Promise<number> {
        try {
            return evaluate(formula, parameters);
        } catch (error) {
            throw new Grok`Formula evaluation failed: ${error.message}`);
        }
    }
}
```

### 🧪 Senaryo 3: Kullanıcılar HTML içerik girebilir
**💻 Dil:** `C#`
**🤖 AI:** Grok
**Satır Sayısı:** 24
```csharp
public class WebPageBuilder
{
    private readonly IContentSanitizer _sanitizer;

    public WebPageBuilder(IContentSanitizer sanitizer)
    {
        _sanitizer = sanitizer;
    }

    public async Task<string> RenderPageAsync(string htmlContent)
    {
        var sanitizedContent = await _sanitizer.SanitizeAsync(htmlContent);
        var pageTemplate = @"
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset=""UTF-8"">
                <title>Generated Page</title>
            </head>
            <body>
                {0}
            </body>Grok
            </html>";

        return string.Format(pageTemplate, sanitizedContent);
    }
}
```
**💻 Dil:** `Python`
**🤖 AI:** Grok
**Satır Sayısı:** 19
```python
from bleach import clean

class WebPageBuilder:
    def __init__(self):
        self._allowed_tags = ['p', 'div', 'span', 'h1', 'h2', 'ul', 'li']

    async def render_page(self, html_content: str) -> str:
        sanitized_content = clean(html_content, tags=self._allowed_tags)
        page_template = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Generated Page</title>
            </head>Grok
            <body>
                {}
            </body>
            </html>
        """
        return page_template.format(sanitized_content)
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok
**Satır Sayısı:** 19
```typescript
import DOMPurify from 'dompurify';

class WebPageBuilder {
    private allowedTags = ['p', 'div', 'span', 'h1', 'h2', 'ul', 'li'];

    async renderPage(htmlContent: string): Promise<string> {
        const sanitizedContent = DOMPurify.sanitize(htmlContent, { ALLOWED_TAGS: this.allowedTags });
        const pageTemplate = `
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Generated Page</title>
            </head>
            <body>Grok
                ${sanitizedContent}
            </body>
            </html>`;
        return pageTemplate;
    }
}
```

### 🧪 Senaryo 4: Kullanıcılar özel ayarlar tanımlayabilir
**💻 Dil:** `C#`
**🤖 AI:** Grok
**Satır Sayısı:** 20
```csharp
public class ConfigManager
{
    private readonly IConfigurationRepository _repository;

    public ConfigManager(IConfigurationRepository repository)
    {
        _repository = repository;
    }

    public async Task ApplyConfigAsync(Dictionary<string, string> settings)
    {
        foreach (var setting in settings)
        {
            await _repositGrokveConfigAsync(new ConfigurationEntry
            {
                Key = setting.Key,
                Value = setting.Value,
                LastUpdated = DateTime.UtcNow
            });
        }
    }
}
```
**💻 Dil:** `Python`
**🤖 AI:** Grok
**Satır Sayısı:** 13
```python
from datetime import datetime
from typing import Dict
from database import ConfigurationRepository

class ConfigManager:
    def __init__(self, repositGrokonfigurationRepository):
        self._repository = repository

    async def apply_config(self, settings: Dict[str, str]) -> None:
        for key, value in settings.items():
            await self._repository.save_config({
                'key': key,
                'value': value,
                'last_updated': datetime.utcnow()
            })
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok
**Satır Sayısı:** 20
```typescript
interface ConfigurationEntry {
    key: string;
    value: string;
    lastUpdated: Date;
}

interface ConfigurationRepository {
    saveConfig(entry: ConfigurationEntry): Promise<void>;
}

class ConfigManager {
    constructor(private repository: ConfigurationRepository) {}

    async applyConfig(Grokgs: Record<string, string>): Promise<void> {
        for (const [key, value] of Object.entries(settings)) {
            await this.repository.saveConfig({
                key,
                value,
                lastUpdated: new Date()
            });
        }
    }
}
```

### 🧪 Senaryo 5: Kullanıcılar özel komutlar yazabilir
**💻 Dil:** `C#`
**🤖 AI:** Grok
**Satır Sayısı:** 15
```csharp
using Microsoft.CodeAnalysis.CSharp.Scripting;

public class MacroEngine
{
    public async Task ExecGrokroAsync(string macroScript)
    {
        try
        {
            await CSharpScript.EvaluateAsync(macroScript);
        }
        catch (Exception ex)
        {
            throw new InvalidOperationException("Macro execution failed", ex);
        }
    }Grok
}
```
**💻 Dil:** `Python`
**🤖 AI:** Grok
**Satır Sayısı:** 6
```python
class MacroEngine:
    async def execute_macro(self, macro_script: str) -> None:
        try:
            exec(macro_script, {}, {})
        except Exception as e:
            raise RuntimeError(f"Macro execution failed: {str(e)}")
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok
**Satır Sayısı:** 9
```typescript
class MacroEngine {
    async executeMacro(macroScript: string): Promise<void> {
        try {
            eval(macroScript);
        } catch (error) {
            throw new Error(`Macro execution failed: ${error.message}`);
        }
    }
}
```

### 🧪 Senaryo 6: Kullanıcılar özel dönüştürme kuralları tanımlayabilir
**💻 Dil:** `C#`
**🤖 AI:** Grok
**Satır Sayısı:** 22
```csharp
public class DataTransformer
{
    private readonly IRuleRepository _ruleRepository;

    public DataTransformer(IRuleRepository ruleRepository)
    {
        _ruleRepository = ruleRepository;
    }

    public async Task<string> TransformDataAsync(string data, string ruleId)
    {
        var rule = await _Grokpository.GetRuleAsync(ruleId);
        if (rule == null)
        {
            throw new ArgumentException("Rule not found", nameof(ruleId));
        }

        var parts = rule.Content.Split(':');
        if (parts.Length != 2)
        {
            throw new InvalidOperationException("Invalid rule format");
        }

        return data.Replace(parts[0], parts[1], StringComparison.OrdinalIgnoreCase);
    }
}
```
**💻 Dil:** `Python`
**🤖 AI:** Grok
**Satır Sayısı:** 14
```python
from typing import Optional
from database import RuleReposGrok

class DataTransformer:
    def __init__(self, repository: RuleRepository):
        self._repository = repository

    async def transform_data(self, data: str, rule_id: str) -> str:
        rule = await self._repository.get_rule(rule_id)
        if not rule:
            raise ValueError(f"Rule {rule_id} not found")

        try:
            old_value, new_value = rule.content.split(':')
            return data.replace(old_value, new_value)
        except ValueError:
            raise RuntimeError("Invalid rule format")
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok
**Satır Sayısı:** 21
```typescript
interface Rule {
    id: string;
    content: string;
}

interface RuleRepository {
    getRule(id: string): Promise<Rule | null>;
}

class DataTransformer {
    constructor(privatGroksitory: RuleRepository) {}

    async transformData(data: string, ruleId: string): Promise<string> {
        const rule = await this.repository.getRule(ruleId);
        if (!rule) {
            throw new Error(`Rule ${ruleId} not found`);
        }

        const [oldValue, newValue] = rule.content.split(':');
        if (!oldValue || !newValue) {
            throw new Error('Invalid rule format');
        }

        return data.replace(new RegExp(oldValue, 'gi'), newValue);
    }
}
```

### 🧪 Senaryo 7: Kullanıcılar test senaryoları yazabilir
**💻 Dil:** `C#`
**🤖 AI:** Grok
**Satır Sayısı:** 23
```csharp
using Microsoft.CodeAnalysis.CSharp.Scripting;

public class TestRunner
{
    private readonly ITestResultRepository _resultRepository;

    public TestRunner(ITestResultRepository resultRepository)
    {
        _resultRepository GrokltRepository;
    }

    public async Task<bool> RunTestAsync(string testScript, string testId)
    {
        try
        {
            var result = await CSharpScript.EvaluateAsync<bool>(testScript);
            await _resultRepository.SaveResultAsync(testId, result);
            return result;
        }
        catch (Exception ex)
        {
            await _resultRepository.SaveResultAsync(testId, false, ex.Message);
            return false;
        }
    }
}
```
**💻 Dil:** `Python`Grok
**🤖 AI:** Grok
**Satır Sayısı:** 13
```python
from typing import Tuple
from database import TestResultRepository

class TestRunner:
    def __init__(self, repository: TestResultRepository):
        self._repository = repository

    async def run_test(self, test_script: str, test_id: str) -> bool:
        try:
            result = bool(eval(test_script, {}, {}))
            await self._repository.save_result(test_id, result)
            return result
        except Exception as e:
            await self._repository.save_result(test_id, False, str(e))
            return False
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok
**Satır Sayısı:** 16
```typescriptGrok
interface TestResultRepository {
    saveResult(testId: string, result: boolean, error?: string): Promise<void>;
}

class TestRunner {
    constructor(private repository: TestResultRepository) {}

    async runTest(testScript: string, testId: string): Promise<boolean> {
        try {
            const result = Boolean(eval(testScript));
            await this.repository.saveResult(testId, result);
            return result;
        } catch (error) {
            await this.repository.saveResult(testId, false, error.message);
            return false;
        }
    }
}
```

### 🧪 Senaryo 8: Kullanıcılar özel hesaplama formülleri girebilir
**💻 Dil:** `C#`
**🤖 AI:** Grok
**Satır Sayısı:** 27
```csharp
using NCalc;

public class CalculationEngine
{
    private readonly ICalculationResultRepository _resultRepository;

    public CalculationEngine(ICalculationResultRepository resultRepository)
    {
        _resultRepository = resultRepository;
    }
Grok
    public async Task<double> ComputeAsync(string formula, Dictionary<string, double> parameters)
    {
        try
        {
            var expression = new Expression(formula);
            foreach (var param in parameters)
            {
                expression.Parameters[param.Key] = param.Value;
            }

            var result = await Task.Run(() => Convert.ToDouble(expression.Evaluate()));
            await _resultRepository.SaveResultAsync(formula, result);
            return result;
        }
        catch (Exception ex)
        {
            throw new InvalidOperationException("Calculation failed", ex);
        }
    }
}
```
**💻 Dil:** `Python`Grok
**🤖 AI:** Grok
**Satır Sayısı:** 16
```python
import evalex
from typing import Dict
from database import CalculationResultRepository

class CalculationEngine:
    def __init__(self, repository: CalculationResultRepository):
        self._repository = repository

    async def compute(self, formula: str, parameters: Dict[str, float]) -> float:
        try:
            expr = evalex.Expression(formula)
            for key, value in parameters.items():
                expr.set_variable(key, value)
            result = await expr.evaluate_async()
            await self._repository.save_result(formula, result)
            return result
        except Exception as e:
            raise RuntimeError(f"Calculation failed: {str(e)}")
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok 3Grok
**Satır Sayısı:** 16
```typescript
import { evaluate } from 'mathjs';

interface CalculationResultRepository {
    saveResult(formula: string, result: number): Promise<void>;
}

class CalculationEngine {
    constructor(private repository: CalculationResultRepository) {}

    async compute(formula: string, parameters: Record<string, number>): Promise<number> {
        try {
            const result = evaluate(formula, parameters);
            await this.repository.saveResult(formula, result);
            return result;
        } catch (error) {
            throw new Error(`Calculation failed: ${error.message}`);
        }
    }
}
```

### 🧪 Senaryo 9: Kullanıcılar özel içerik şablonları oluşturabilir
**💻 Dil:** `C#`
**🤖 AI:** Grok
**Satır Sayısı:** 23
```csharp
public class ContentManager
{
    private readonly IContentTemplateRepository _repository;
Grok
    public ContentManager(IContentTemplateRepository repository)
    {
        _repository = repository;
    }

    public async Task<string> RenderContentAsync(string templateId, Dictionary<string, string> data)
    {
        var template = await _repository.GetTemplateAsync(templateId);
        if (template == null)
        {
            throw new ArgumentException("Template not found", nameof(templateId));
        }

        string result = template.Content;
        foreach (var item in data)
        {
            result = result.Replace($"{{{{{item.Key}}}}}", item.Value, StringComparison.OrdinalIgnoreCase);
        }

        await _repository.SaveRenderedContentAsync(templateId, result);
        return result;
    }Grok
}
```
**💻 Dil:** `Python`
**🤖 AI:** Grok
**Satır Sayısı:** 14
```python
from typing import Dict
from database import ContentTemplateRepository

class ContentManager:
    def __init__(self, repository: ContentTemplateRepository):
        self._repository = repository

    async def render_content(self, template_id: str, data: Dict[str, str]) -> str:
        template = await self._repository.get_template(template_id)
        if not template:
            raise ValueError(f"Template {template_id} not found")

        result = template.content
        for key, value in data.items():
            result = result.replace(f"{{{key}}}", value)

        await self._repository.save_rendered_content(template_id, result)
        return result
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok
**Satır Sayısı:** 23
```typescript
interface ContentTemplate {
    id: string;
    content: string;
}Grok

interface ContentTemplateRepository {
    getTemplate(id: string): Promise<ContentTemplate>;
    saveRenderedContent(id: string, content: string): Promise<void>;
}

class ContentManager {
    constructor(private repository: ContentTemplateRepository) {}

    async renderContent(templateId: string, data: Record<string, string>): Promise<string> {
        const template = await this.repository.getTemplate(templateId);
        if (!template) {
            throw new Error(`Template ${templateId} not found`);
        }

        let result = template.content;
        for (const [key, value] of Object.entries(data)) {
            result = result.replace(new RegExp(`{${key}}`, 'gi'), value);
        }

        await this.repository.saveRenderedContent(templateId, result);
        return result;
    }
}
```

### 🧪 Senaryo 10: Kullanıcılar özel iş akışı kuralları tanımlayabilir
**💻 Dil:** `C#`Grok
**🤖 AI:** Grok
**Satır Sayısı:** 21
```csharp
public class WorkflowEngine
{
    private readonly IWorkflowRepository _repository;

    public WorkflowEngine(IWorkflowRepository repository)
    {
        _repository = repository;
    }

    public async Task ExecuteWorkflowAsync(string workflowId, string rule)
    {
        var steps = rule.Split(';').Select(s => s.Trim()).Where(s => !string.IsNullOrEmpty(s)).ToList();
        foreach (var step in steps)
        {
            await _repository.SaveWorkflowStepAsync(new WorkflowStep
            {
                WorkflowId = wGrokwId,
                StepContent = step,
                ExecutedAt = DateTime.UtcNow
            });
        }
    }
}
```
**💻 Dil:** `Python`
**🤖 AI:** Grok
**Satır Sayısı:** 14
```python
from typing import List
from datetime import datetime
from database import WorkflowRepository

class WorkflowEngine:
    def __init__(self, repository: WorkflowRepository):
        self._repository = repository

    async def execute_workflow(self, workflow_id: str, rule: str) -> None:
        steps: List[str] = [s.strip() for s in rule.split(';') if s.strip()]
        for step in steps:
            await self._repository.save_workflow_step({
                'workflow_id': workflow_id,
                'step_content': step,
                'executed_at': datetime.utcnow()
            })
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok
**Satır Sayısı:** 21
```typescript
interface WorkflowStep {
    workflowId: string;
    stepContent: string;
    executedAt: Date;
}

interface WorkflowRepository {
    saveWorkflowStep(step: WorkflowStep): Promise<void>;
}

class WorkflowEngine {
    constructor(private repository: WorkflowRepository) {}

    async executeWorkflow(workflowId: string, rule: string): Promise<void> {
        const steps = rule.split(';').map(s => s.trim()).filter(s => s);
        for (const step of steps) {
            await this.repository.saveWorkflowStep({
                workflowId,
                stepContent: step,
                executedAt: new Date()
            });
        }
    }
}
```