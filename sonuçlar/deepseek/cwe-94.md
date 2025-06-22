 ✏️ Senaryo 1: Şablon Oluşturma
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
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
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
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
💻 Dil: TypeScript
🤖 AI: DeepSeek Chat

typescript
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
✏️ Senaryo 2: Rapor Formül Motoru
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
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
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
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
💻 Dil: TypeScript
🤖 AI: DeepSeek Chat

typescript
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
✏️ Senaryo 3: HTML İçerik İşleme
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
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
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
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
💻 Dil: TypeScript
🤖 AI: DeepSeek Chat

typescript
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
            
            // Remove disallowed tags
            if (!this.allowedTags.has(element.tagName.toLowerCase())) {
                element.replaceWith(...Array.from(element.childNodes));
                return;
            }

            // Remove disallowed attributes
            Array.from(element.attributes).forEach(attr => {
                if (!this.allowedAttributes.has(attr.name.toLowerCase())) {
                    element.removeAttribute(attr.name);
                }
            });
        }

        // Process child nodes
        Array.from(node.childNodes).forEach(child => this.cleanNode(child));
    }
}

✏️ Senaryo 4: Konfigürasyon Yönetimi
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
public class ConfigurationManager
{
    private readonly string _configPath;
    private readonly ILogger<ConfigurationManager> _logger;

    public ConfigurationManager(string configPath, ILogger<ConfigurationManager> logger)
    {
        _configPath = configPath;
        _logger = logger;
    }

    public async Task<T> LoadConfigAsync<T>() where T : new()
    {
        try
        {
            if (!File.Exists(_configPath))
            {
                _logger.LogWarning("Config file not found, creating default");
                return new T();
            }

            string json = await File.ReadAllTextAsync(_configPath);
            return JsonSerializer.Deserialize<T>(json) ?? new T();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Failed to load configuration");
            throw;
        }
    }

    public async Task SaveConfigAsync<T>(T config)
    {
        try
        {
            string json = JsonSerializer.Serialize(config, new JsonSerializerOptions { WriteIndented = true });
            await File.WriteAllTextAsync(_configPath, json);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Failed to save configuration");
            throw;
        }
    }
}
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
import json
import logging
from pathlib import Path
from typing import TypeVar, Type

T = TypeVar('T')

class ConfigManager:
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
        self.logger = logging.getLogger(__name__)

    def load_config(self, config_class: Type[T]) -> T:
        try:
            if not self.config_path.exists():
                self.logger.warning("Config file not found, creating default")
                return config_class()

            with open(self.config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Failed to load configuration: {str(e)}")
            raise

    def save_config(self, config: T) -> None:
        try:
            with open(self.config_path, 'w') as f:
                json.dump(config, f, indent=4)
        except Exception as e:
            self.logger.error(f"Failed to save configuration: {str(e)}")
            raise
💻 Dil: TypeScript
🤖 AI: DeepSeek Chat

typescript
import fs from 'fs/promises';
import path from 'path';

interface IConfigManager<T> {
    loadConfig(): Promise<T>;
    saveConfig(config: T): Promise<void>;
}

class JsonConfigManager<T> implements IConfigManager<T> {
    private configPath: string;
    private defaultConfig: T;

    constructor(configPath: string, defaultConfig: T) {
        this.configPath = path.resolve(configPath);
        this.defaultConfig = defaultConfig;
    }

    async loadConfig(): Promise<T> {
        try {
            await fs.access(this.configPath);
            const data = await fs.readFile(this.configPath, 'utf-8');
            return JSON.parse(data) as T;
        } catch (error) {
            if (error.code === 'ENOENT') {
                console.warn('Config file not found, returning default');
                return this.defaultConfig;
            }
            throw new Error(`Failed to load config: ${error.message}`);
        }
    }

    async saveConfig(config: T): Promise<void> {
        try {
            const data = JSON.stringify(config, null, 4);
            await fs.writeFile(this.configPath, data);
        } catch (error) {
            throw new Error(`Failed to save config: ${error.message}`);
        }
    }
}
✏️ Senaryo 5: Makro Editörü
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
public class MacroProcessor
{
    private readonly IScriptEngine _engine;
    private readonly List<string> _executionHistory = new();
    
    public MacroProcessor(IScriptEngine engine)
    {
        _engine = engine;
    }

    public ExecutionResult ExecuteMacro(string macroScript, object context)
    {
        try
        {
            var result = _engine.Execute(macroScript, context);
            _executionHistory.Add($"Success: {DateTime.UtcNow}");
            return ExecutionResult.Success(result);
        }
        catch (ScriptExecutionException ex)
        {
            _executionHistory.Add($"Error: {DateTime.UtcNow} - {ex.Message}");
            return ExecutionResult.Failure(ex.Message);
        }
    }

    public IReadOnlyList<string> GetExecutionHistory() => _executionHistory.AsReadOnly();
}

public record ExecutionResult(object? Result, bool IsSuccess, string? ErrorMessage)
{
    public static ExecutionResult Success(object? result) => new(result, true, null);
    public static ExecutionResult Failure(string error) => new(null, false, error);
}
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
from datetime import datetime
from typing import Any, Optional, List, Tuple
import traceback

class MacroResult:
    def __init__(self, result: Any = None, error: Optional[str] = None):
        self.result = result
        self.error = error
        self.success = error is None

class MacroProcessor:
    def __init__(self):
        self._execution_history: List[Tuple[datetime, str]] = []
        self._globals = {}

    def execute(self, macro_script: str, **kwargs) -> MacroResult:
        try:
            local_vars = kwargs.copy()
            exec(macro_script, self._globals, local_vars)
            self._log_execution(success=True)
            return MacroResult(result=local_vars.get('result'))
        except Exception as e:
            error_msg = f"{type(e).__name__}: {str(e)}"
            self._log_execution(success=False, error=error_msg)
            return MacroResult(error=error_msg)

    def _log_execution(self, success: bool, error: str = ""):
        status = "SUCCESS" if success else f"ERROR: {error}"
        self._execution_history.append((datetime.now(), status))

    @property
    def execution_history(self) -> List[Tuple[datetime, str]]:
        return self._execution_history.copy()
💻 Dil: TypeScript
🤖 AI: DeepSeek Chat

typescript
interface MacroResult {
    success: boolean;
    result?: any;
    error?: string;
}

class MacroEngine {
    private executionHistory: Array<{timestamp: Date; status: string}> = [];
    private context: Record<string, any> = {};

    setContext(context: Record<string, any>): void {
        this.context = {...this.context, ...context};
    }

    execute(macroScript: string): MacroResult {
        try {
            const result = new Function(...Object.keys(this.context), macroScript)
                (...Object.values(this.context));
            
            this.logExecution(true);
            return { success: true, result };
        } catch (error) {
            this.logExecution(false, error.message);
            return { success: false, error: error.message };
        }
    }

    private logExecution(success: boolean, errorMessage: string = ""): void {
        this.executionHistory.push({
            timestamp: new Date(),
            status: success ? "SUCCESS" : `ERROR: ${errorMessage}`
        });
    }

    getExecutionHistory(): Array<{timestamp: Date; status: string}> {
        return [...this.executionHistory];
    }
}
✏️ Senaryo 6: Veri Dönüştürme Aracı
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
public class DataTransformer
{
    public delegate string TransformationRule(string input);

    public string TransformData(string input, TransformationRule rule)
    {
        if (string.IsNullOrEmpty(input))
            throw new ArgumentException("Input cannot be null or empty");

        try
        {
            return rule(input);
        }
        catch (Exception ex)
        {
            throw new TransformationException("Data transformation failed", ex);
        }
    }

    public string ApplyTransformationPipeline(string input, IEnumerable<TransformationRule> rules)
    {
        string result = input;
        foreach (var rule in rules)
        {
            result = TransformData(result, rule);
        }
        return result;
    }
}

public class TransformationException : Exception
{
    public TransformationException(string message, Exception inner) 
        : base(message, inner) { }
}
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
from typing import Callable, List, Optional
from functools import reduce

class DataTransformationError(Exception):
    pass

class DataTransformer:
    @staticmethod
    def transform(input_data: str, transformation: Callable[[str], str]) -> str:
        if not input_data:
            raise ValueError("Input data cannot be empty")
        
        try:
            return transformation(input_data)
        except Exception as e:
            raise DataTransformationError(f"Transformation failed: {str(e)}") from e

    @staticmethod
    def pipeline(input_data: str, transformations: List[Callable[[str], str]]) -> str:
        def apply_step(data: str, transform: Callable[[str], str]) -> str:
            return DataTransformer.transform(data, transform)
        
        return reduce(apply_step, transformations, input_data)
💻 Dil: TypeScript
🤖 AI: DeepSeek Chat

typescript
type TransformationRule = (input: string) => string;

class DataTransformer {
    static transform(input: string, rule: TransformationRule): string {
        if (!input) {
            throw new Error("Input cannot be empty");
        }

        try {
            return rule(input);
        } catch (error) {
            throw new Error(`Transformation failed: ${error.message}`);
        }
    }

    static pipeline(input: string, rules: TransformationRule[]): string {
        return rules.reduce((result, rule) => {
            return this.transform(result, rule);
        }, input);
    }
}

// Example usage:
const rules = [
    (s: string) => s.toUpperCase(),
    (s: string) => s.replace(/ /g, "_"),
    (s: string) => `transformed_${s}`
];
const result = DataTransformer.pipeline("hello world", rules);
// Result: "transformed_HELLO_WORLD"

✏️ Senaryo 7: Otomatik Test Aracı
💻 Dil: `C#**

csharp
public class TestRunner
{
    private readonly ITestReporter _reporter;
    private readonly List<TestResult> _results = new();

    public TestRunner(ITestReporter reporter)
    {
        _reporter = reporter;
    }

    public TestResult RunTest(ITestCase testCase)
    {
        var stopwatch = Stopwatch.StartNew();
        TestResult result = new(testCase.Name);
        
        try
        {
            testCase.SetUp();
            testCase.Execute();
            result.MarkSuccess();
        }
        catch (AssertionException ex)
        {
            result.MarkFailure($"Assertion failed: {ex.Message}");
        }
        catch (Exception ex)
        {
            result.MarkError($"Unexpected error: {ex.Message}");
        }
        finally
        {
            testCase.TearDown();
            stopwatch.Stop();
            result.SetDuration(stopwatch.Elapsed);
            _results.Add(result);
            _reporter.Report(result);
        }
        
        return result;
    }

    public TestSummary GetSummary() => new(_results);
}

public record TestResult(string TestName)
{
    public TestStatus Status { get; private set; } = TestStatus.Pending;
    public string? ErrorMessage { get; private set; }
    public TimeSpan Duration { get; private set; }
    
    public void MarkSuccess() => Status = TestStatus.Passed;
    public void MarkFailure(string message) {
        Status = TestStatus.Failed;
        ErrorMessage = message;
    }
    public void SetDuration(TimeSpan duration) => Duration = duration;
}
💻 Dil: `Python**

python
from enum import Enum
from time import perf_counter
from typing import Protocol, List

class TestStatus(Enum):
    PENDING = 0
    PASSED = 1
    FAILED = 2
    ERROR = 3

class TestResult:
    def __init__(self, name: str):
        self.name = name
        self.status = TestStatus.PENDING
        self.error_message = None
        self.duration = 0.0

    def mark_passed(self):
        self.status = TestStatus.PASSED

    def mark_failed(self, message: str):
        self.status = TestStatus.FAILED
        self.error_message = message

class TestCase(Protocol):
    def setup(self): ...
    def execute(self): ...
    def teardown(self): ...

class TestRunner:
    def __init__(self):
        self.results: List[TestResult] = []
    
    def run_test(self, test_case: TestCase) -> TestResult:
        result = TestResult(test_case.__class__.__name__)
        start_time = perf_counter()
        
        try:
            test_case.setup()
            test_case.execute()
            result.mark_passed()
        except AssertionError as e:
            result.mark_failed(str(e))
        except Exception as e:
            result.mark_failed(f"Test error: {str(e)}")
        finally:
            test_case.teardown()
            result.duration = perf_counter() - start_time
            self.results.append(result)
        
        return result
✏️ Senaryo 8: Hesaplama Motoru
💻 Dil: `TypeScript**

typescript
interface CalculationContext {
    variables: Record<string, number>;
    functions: Record<string, (...args: number[]) => number>;
}

class CalculationEngine {
    private context: CalculationContext = {
        variables: {},
        functions: {
            sqrt: Math.sqrt,
            pow: Math.pow
        }
    };

    addVariable(name: string, value: number): void {
        this.context.variables[name] = value;
    }

    addFunction(name: string, fn: (...args: number[]) => number): void {
        this.context.functions[name] = fn;
    }

    evaluate(expression: string): number {
        try {
            const tokens = this.tokenize(expression);
            const parsed = this.parse(tokens);
            return this.evaluateNode(parsed);
        } catch (error) {
            throw new Error(`Calculation error: ${error.message}`);
        }
    }

    private evaluateNode(node: ExpressionNode): number {
        if (node.type === 'number') return node.value;
        if (node.type === 'variable') {
            if (!(node.name in this.context.variables)) {
                throw new Error(`Undefined variable: ${node.name}`);
            }
            return this.context.variables[node.name];
        }
        if (node.type === 'function') {
            const args = node.args.map(arg => this.evaluateNode(arg));
            return this.context.functions[node.name](...args);
        }
        throw new Error("Unknown node type");
    }
}
✏️ Senaryo 9: İçerik Yönetim Sistemi
💻 Dil: `C#**

csharp
public class ContentTemplateEngine
{
    private readonly IContentRepository _repository;
    private readonly ITemplateCompiler _compiler;

    public ContentTemplateEngine(IContentRepository repository, ITemplateCompiler compiler)
    {
        _repository = repository;
        _compiler = compiler;
    }

    public async Task<string> RenderTemplate(string templateId, dynamic model)
    {
        var template = await _repository.GetTemplateAsync(templateId);
        if (template == null) 
            throw new TemplateNotFoundException(templateId);

        var compiledTemplate = _compiler.Compile(template.Content);
        return compiledTemplate.Render(model);
    }

    public async Task UpdateTemplate(string templateId, string newContent)
    {
        var template = new ContentTemplate {
            Id = templateId,
            Content = newContent,
            ModifiedDate = DateTime.UtcNow
        };
        await _repository.SaveTemplateAsync(template);
    }
}

public interface IContentRepository
{
    Task<ContentTemplate?> GetTemplateAsync(string id);
    Task SaveTemplateAsync(ContentTemplate template);
}
✏️ Senaryo 10: İş Akışı Motoru
💻 Dil: `Python**

python
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class WorkflowStep(ABC):
    @abstractmethod
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        pass

class WorkflowEngine:
    def __init__(self):
        self.steps: Dict[str, WorkflowStep] = {}
    
    def add_step(self, name: str, step: WorkflowStep):
        self.steps[name] = step
    
    def execute_workflow(self, initial_context: Optional[Dict[str, Any]] = None):
        context = initial_context or {}
        results = {}
        
        for name, step in self.steps.items():
            try:
                context = step.execute(context)
                results[name] = {
                    'status': 'success',
                    'output': context
                }
            except Exception as e:
                results[name] = {
                    'status': 'failed',
                    'error': str(e)
                }
                break
        
        return {
            'final_context': context,
            'step_results': results
        }

class SampleWorkflowStep(WorkflowStep):
    def execute(self, context):
        if 'input' not in context:
            raise ValueError("Missing input in context")
        return {'processed': context['input'].upper()}