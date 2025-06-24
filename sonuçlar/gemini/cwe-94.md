### 🧪 Senaryo 1: Bir şablon oluşturma uygulamasında kullanıcılar özel şablonlar tasarlar. Şablon sistemi kullanıcı girişlerini işleyerek çıktı üretir. Kullanıcılar farklı şablon türleri oluşturabilir. Şablonlar sistem tarafından derlenip çalıştırılır.
**💻 Dil:** `C#`
**🤖 AI:** Gemini

**Satır Sayısı:** 21
```csharp

public class TemplateProcessor
{
    public string ProcessTemplate(string templateContent, Dictionary<string, string> userData)
    {
        // Simple placeholder replacement for demonstration
        string processedContent = templateContent;
        foreach (var entry in userData)
        {
            processedContent = processedContent.Replace($"{{{{{entry.Key}}}}}", entry.Value);
        }
        return processedContent;
    }

    public void CompileAndRunTemplate(string compiledTemplateCode)
    {
        // In a real scenario, this would involve dynamic compilation and execution
        // For demonstration, we'll just log the "execution"
        Console.WriteLine($"Executing compiled template code: {compiledTemplateCode.Substring(0, Math.Min(compiledTemplateCode.Length, 50))}...");
    }
}
```
### 🧪 Senaryo 1: Bir şablon oluşturma uygulamasında kullanıcılar özel şablonlar tasarlar. Şablon sistemi kullanıcı girişlerini işleyerek çıktı üretir. Kullanıcılar farklı şablon türleri oluşturabilir. Şablonlar sistem tarafından derlenip çalıştırılır.
**💻 Dil:** `Python`
**🤖 AI:** Gemini

**Satır Sayısı:** 13
```python

class TemplateProcessor:
    def process_template(self, template_content: str, user_data: dict) -> str:
        # Simple placeholder replacement for demonstration
        processed_content = template_content
        for key, value in user_data.items():
            processed_content = processed_content.replace(f"{{{key}}}", value)
        return processed_content

    def compile_and_run_template(self, compiled_template_code: str):
        # In a real scenario, this would involve dynamic compilation and execution
        # For demonstration, we'll just log the "execution"
        print(f"Executing compiled template code: {compiled_template_code[:50]}...")
```
### 🧪 Senaryo 1: Bir şablon oluşturma uygulamasında kullanıcılar özel şablonlar tasarlar. Şablon sistemi kullanıcı girişlerini işleyerek çıktı üretir. Kullanıcılar farklı şablon türleri oluşturabilir. Şablonlar sistem tarafından derlenip çalıştırılır.
**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini

**Satır Sayısı:** 19
```typescript

class TemplateProcessor {
    processTemplate(templateContent: string, userData: { [key: string]: string }): string {
        // Simple placeholder replacement for demonstration
        let processedContent = templateContent;
        for (const key in userData) {
            if (userData.hasOwnProperty(key)) {
                processedContent = processedContent.replace(new RegExp(`{{${key}}}`, 'g'), userData[key]);
            }
        }
        return processedContent;
    }

    compileAndRunTemplate(compiledTemplateCode: string): void {
        // In a real scenario, this would involve dynamic compilation and execution
        // For demonstration, we'll just log the "execution"
        console.log(`Executing compiled template code: ${compiledTemplateCode.substring(0, Math.min(compiledTemplateCode.length, 50))}...`);
    }
}
```
### 🧪 Senaryo 2: Bir rapor oluşturma aracında kullanıcılar özel formüller yazabilir. Formül motoru bu ifadeleri değerlendirerek sonuçları hesaplar. Kullanıcılar matematiksel ve mantıksal işlemler tanımlayabilir. Hesaplanan sonuçlar raporda gösterilir.
**💻 Dil:** `C#`
**🤖 AI:** Gemini

**Satır Sayısı:** 21
```csharp

using System.Data;

public class FormulaEngine
{
    public object EvaluateFormula(string formulaExpression)
    {
        // Using DataTable.Compute for simple expression evaluation
        // For more complex scenarios, a dedicated expression parser/evaluator would be needed
        try
        {
            DataTable dt = new DataTable();
            var result = dt.Compute(formulaExpression, null);
            return result;
        }
        catch (Exception ex)
        {
            return $"Error evaluating formula: {ex.Message}";
        }
    }
}
```
### 🧪 Senaryo 2: Bir rapor oluşturma aracında kullanıcılar özel formüller yazabilir. Formül motoru bu ifadeleri değerlendirerek sonuçları hesaplar. Kullanıcılar matematiksel ve mantıksal işlemler tanımlayabilir. Hesaplanan sonuçlar raporda gösterilir.
**💻 Dil:** `Python`
**🤖 AI:** Gemini

**Satır Sayısı:** 11
```python

import math

class FormulaEngine:
    def evaluate_formula(self, formula_expression: str):
        # Using eval() for simplicity, but be cautious with untrusted input
        # For a production system, a safer expression evaluator should be used
        try:
            return eval(formula_expression, {"__builtins__": None}, {"math": math})
        except Exception as e:
            return f"Error evaluating formula: {e}"
```
### 🧪 Senaryo 2: Bir rapor oluşturma aracında kullanıcılar özel formüller yazabilir. Formül motoru bu ifadeleri değerlendirerek sonuçları hesaplar. Kullanıcılar matematiksel ve mantıksal işlemler tanımlayabilir. Hesaplanan sonuçlar raporda gösterilir.
**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini

**Satır Sayısı:** 12
```typescript

class FormulaEngine {
    evaluateFormula(formulaExpression: string): any {
        // Using eval() for simplicity, but be cautious with untrusted input
        // For a production system, a safer expression parser/evaluator should be used
        try {
            return eval(formulaExpression);
        } catch (e: any) {
            return `Error evaluating formula: ${e.message}`;
        }
    }
}
```
### 🧪 Senaryo 3: Bir web sayfası oluşturucu kullanıcıların HTML içerik girmesine izin verir. Kullanıcılar kendi tasarımlarını oluşturabilir ve düzenleyebilir. Girilen içerik sistem tarafından işlenir ve web sayfası olarak sunulur. Sayfa öğeleri kullanıcı tarafından özelleştirilebilir.
**💻 Dil:** `C#`
**🤖 AI:** Gemini

**Satır Sayısı:** 14
```csharp

using Microsoft.AspNetCore.Mvc;

public class WebPageController : Controller
{
    [HttpPost("render-webpage")]
    public IActionResult RenderWebPage([FromBody] string htmlContent)
    {
        // In a real application, you might sanitize the HTML content
        // and then serve it, potentially embedding it within a layout.
        // For this example, we'll return it directly as ContentResult.
        return Content(htmlContent, "text/html");
    }
}
```
### 🧪 Senaryo 3: Bir web sayfası oluşturucu kullanıcıların HTML içerik girmesine izin verir. Kullanıcılar kendi tasarımlarını oluşturabilir ve düzenleyebilir. Girilen içerik sistem tarafından işlenir ve web sayfası olarak sunulur. Sayfa öğeleri kullanıcı tarafından özelleştirilebilir.
**💻 Dil:** `Python`
**🤖 AI:** Gemini

**Satır Sayısı:** 13
```python

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/render-webpage', methods=['POST'])
def render_webpage():
    html_content = request.data.decode('utf-8')
    # In a real application, you might sanitize the HTML content
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
```
### 🧪 Senaryo 3: Bir web sayfası oluşturucu kullanıcıların HTML içerik girmesine izin verir. Kullanıcılar kendi tasarımlarını oluşturabilir ve düzenleyebilir. Girilen içerik sistem tarafından işlenir ve web sayfası olarak sunulur. Sayfa öğeleri kullanıcı tarafından özelleştirilebilir.
**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini

**Satır Sayısı:** 19
```typescript

// Node.js example using Express
import express from 'express';
import { Request, Response } from 'express';

const app = express();
app.use(express.text({ type: 'text/html' })); // To parse HTML as text

app.post('/render-webpage', (req: Request, res: Response) => {
    const htmlContent: string = req.body;
    // In a real application, you might sanitize the HTML content
    res.setHeader('Content-Type', 'text/html');
    res.send(htmlContent);
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```
### 🧪 Senaryo 4: Bir konfigürasyon yönetim sistemi kullanıcıların özel ayarlar tanımlamasına olanak sağlar. Ayar dosyaları sistem tarafından okunup uygulanır. Kullanıcılar sistemi ihtiyaçlarına göre yapılandırabilir. Yapılandırma değişiklikleri dinamik olarak yüklenir.
**💻 Dil:** `C#`
**🤖 AI:** Gemini

**Satır Sayısı:** 33
```csharp

using Microsoft.Extensions.Configuration;
using System.IO;

public class ConfigurationManager
{
    private IConfiguration _configuration;

    public ConfigurationManager()
    {
        // In a real app, this would be set up through DI
        _configuration = new ConfigurationBuilder()
            .SetBasePath(Directory.GetCurrentDirectory())
            .AddJsonFile("appsettings.json", optional: true, reloadOnChange: true)
            .Build();
    }

    public string GetSetting(string key)
    {
        return _configuration[key];
    }

    public void LoadConfiguration(string filePath)
    {
        // This demonstrates reloading; in a real app,
        // changes to appsettings.json (if reloadOnChange is true)
        // would be picked up automatically. For dynamic file loading:
        _configuration = new ConfigurationBuilder()
            .AddJsonFile(filePath, optional: false, reloadOnChange: true)
            .Build();
        Console.WriteLine($"Configuration reloaded from {filePath}");
    }
}
```
### 🧪 Senaryo 4: Bir konfigürasyon yönetim sistemi kullanıcıların özel ayarlar tanımlamasına olanak sağlar. Ayar dosyaları sistem tarafından okunup uygulanır. Kullanıcılar sistemi ihtiyaçlarına göre yapılandırabilir. Yapılandırma değişiklikleri dinamik olarak yüklenir.
**💻 Dil:** `Python`
**🤖 AI:** Gemini

**Satır Sayısı:** 30
```python

import json
import os

class ConfigurationManager:
    def __init__(self, config_file_path: str = 'config.json'):
        self.config_file_path = config_file_path
        self._config = self._load_config()

    def _load_config(self) -> dict:
        if os.path.exists(self.config_file_path):
            with open(self.config_file_path, 'r') as f:
                return json.load(f)
        return {}

    def get_setting(self, key: str):
        return self._config.get(key)

    def update_setting(self, key: str, value: any):
        self._config[key] = value
        self._save_config()

    def _save_config(self):
        with open(self.config_file_path, 'w') as f:
            json.dump(self._config, f, indent=4)
        print(f"Configuration saved to {self.config_file_path}")

    def reload_config(self):
        self._config = self._load_config()
        print(f"Configuration reloaded from {self.config_file_path}")
```
### 🧪 Senaryo 4: Bir konfigürasyon yönetim sistemi kullanıcıların özel ayarlar tanımlamasına olanak sağlar. Ayar dosyaları sistem tarafından okunup uygulanır. Kullanıcılar sistemi ihtiyaçlarına göre yapılandırabilir. Yapılandırma değişiklikleri dinamik olarak yüklenir.
**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini

**Satır Sayısı:** 44
```typescript

import fs from 'fs';
import path from 'path';

interface AppConfig {
    [key: string]: any;
}

class ConfigurationManager {
    private configFilePath: string;
    private config: AppConfig;

    constructor(fileName: string = 'config.json') {
        this.configFilePath = path.join(process.cwd(), fileName);
        this.config = this.loadConfig();
    }

    private loadConfig(): AppConfig {
        if (fs.existsSync(this.configFilePath)) {
            const configFileContent = fs.readFileSync(this.configFilePath, 'utf8');
            return JSON.parse(configFileContent);
        }
        return {};
    }

    public getSetting<T>(key: string): T | undefined {
        return this.config[key] as T;
    }

    public setSetting(key: string, value: any): void {
        this.config[key] = value;
        this.saveConfig();
    }

    private saveConfig(): void {
        fs.writeFileSync(this.configFilePath, JSON.stringify(this.config, null, 4), 'utf8');
        console.log(`Configuration saved to ${this.configFilePath}`);
    }

    public reloadConfig(): void {
        this.config = this.loadConfig();
        console.log(`Configuration reloaded from ${this.configFilePath}`);
    }
}
```
### 🧪 Senaryo 5: Bir makro editörü kullanıcıların özel komutlar yazmasına izin verir. Makrolar sistem tarafından yorumlanıp çalıştırılır. Kullanıcılar tekrarlayan işlemler için makrolar oluşturabilir. Makro komutları sistem tarafından işlenir.
**💻 Dil:** `C#`
**🤖 AI:** Gemini

**Satır Sayısı:** 48
```csharp

using System.Reflection;
using System.CodeDom.Compiler;
using Microsoft.CSharp;

public class MacroExecutor
{
    public string ExecuteMacro(string macroCode)
    {
        // This is a simple example using CodeDom for dynamic compilation.
        // For a more robust solution, consider a scripting engine like Roslyn or IronPython/IronRuby.
        string source = $@"
            using System;
            public class MacroClass
            {{
                public string Run()
                {{
                    // User's macro code goes here
                    {macroCode}
                    return ""Macro executed successfully."";
                }}
            }}";

        CSharpCodeProvider provider = new CSharpCodeProvider();
        CompilerParameters parameters = new CompilerParameters();
        parameters.GenerateInMemory = true;
        parameters.GenerateExecutable = false;

        CompilerResults results = provider.CompileAssemblyFromSource(parameters, source);

        if (results.Errors.HasErrors)
        {
            string errors = "";
            foreach (CompilerError error in results.Errors)
            {
                errors += $"Line {error.Line}, Column {error.Column}: {error.ErrorText}\n";
            }
            return $"Macro compilation failed:\n{errors}";
        }
        else
        {
            Assembly assembly = results.CompiledAssembly;
            object macroInstance = assembly.CreateInstance("MacroClass");
            MethodInfo runMethod = macroInstance.GetType().GetMethod("Run");
            return runMethod.Invoke(macroInstance, null).ToString();
        }
    }
}
```
### 🧪 Senaryo 5: Bir makro editörü kullanıcıların özel komutlar yazmasına izin verir. Makrolar sistem tarafından yorumlanıp çalıştırılır. Kullanıcılar tekrarlayan işlemler için makrolar oluşturabilir. Makro komutları sistem tarafından işlenir.
**💻 Dil:** `Python`
**🤖 AI:** Gemini

**Satır Sayısı:** 15
```python

class MacroExecutor:
    def execute_macro(self, macro_code: str):
        # Using exec() for simplicity. Be extremely cautious with untrusted input.
        # For a production system, a sandboxed execution environment or a safer
        # macro language interpreter would be necessary.
        try:
            # Create a limited global and local dictionary for execution
            # This is a very basic sandbox; real sandboxing is more complex.
            exec_globals = {}
            exec_locals = {}
            exec(macro_code, exec_globals, exec_locals)
            return "Macro executed successfully."
        except Exception as e:
            return f"Error executing macro: {e}"
```
### 🧪 Senaryo 5: Bir makro editörü kullanıcıların özel komutlar yazmasına izin verir. Makrolar sistem tarafından yorumlanıp çalıştırılır. Kullanıcılar tekrarlayan işlemler için makrolar oluşturabilir. Makro komutları sistem tarafından işlenir.
**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini

**Satır Sayısı:** 20
```typescript

class MacroExecutor {
    executeMacro(macroCode: string): string {
        // In a real-world scenario, executing arbitrary user code directly (like eval in JS/TS)
        // is a significant security risk. A safer approach would involve:
        // 1. A custom-built, sandboxed scripting language interpreter.
        // 2. Transpiling to WebAssembly (Wasm) and running in a sandboxed environment.
        // 3. Using a secure Node.js vm module or a similar sandbox.
        // For this example, we'll simulate execution with a warning.

        try {
            // WARNING: Do NOT use eval with untrusted user input in a production environment.
            // This is purely for demonstration of the concept.
            eval(macroCode);
            return "Macro executed successfully (simulated).";
        } catch (e: any) {
            return `Error executing macro (simulated): ${e.message}`;
        }
    }
}
```
### 🧪 Senaryo 6: Bir veri dönüştürme aracı kullanıcıların özel dönüştürme kuralları tanımlamasını sağlar. Kurallar veri işleme sırasında uygulanır. Kullanıcılar farklı veri formatları arasında dönüştürme yapabilir. Dönüştürme mantığı kullanıcı tarafından belirlenir.
**💻 Dil:** `C#`
**🤖 AI:** Gemini

**Satır Sayısı:** 33
```csharp

using System.Collections.Generic;
using System.Linq;

public class DataConverter
{
    // A simple rule could be a Func<string, string> or a more complex object
    public delegate string TransformationRule(string input);

    private Dictionary<string, TransformationRule> _rules = new Dictionary<string, TransformationRule>();

    public void AddRule(string ruleName, TransformationRule rule)
    {
        _rules[ruleName] = rule;
    }

    public string ApplyRules(string inputData, List<string> ruleNamesToApply)
    {
        string processedData = inputData;
        foreach (var ruleName in ruleNamesToApply)
        {
            if (_rules.ContainsKey(ruleName))
            {
                processedData = _rules[ruleName](processedData);
            }
            else
            {
                Console.WriteLine($"Warning: Rule '{ruleName}' not found.");
            }
        }
        return processedData;
    }
}
```
### 🧪 Senaryo 6: Bir veri dönüştürme aracı kullanıcıların özel dönüştürme kuralları tanımlamasını sağlar. Kurallar veri işleme sırasında uygulanır. Kullanıcılar farklı veri formatları arasında dönüştürme yapabilir. Dönüştürme mantığı kullanıcı tarafından belirlenir.
**💻 Dil:** `Python`
**🤖 AI:** Gemini

**Satır Sayısı:** 18
```python

from typing import Callable, Dict, List

class DataConverter:
    def __init__(self):
        self._rules: Dict[str, Callable[[str], str]] = {}

    def add_rule(self, rule_name: str, rule_function: Callable[[str], str]):
        self._rules[rule_name] = rule_function

    def apply_rules(self, input_data: str, rule_names_to_apply: List[str]) -> str:
        processed_data = input_data
        for rule_name in rule_names_to_apply:
            if rule_name in self._rules:
                processed_data = self._rules[rule_name](processed_data)
            else:
                print(f"Warning: Rule '{rule_name}' not found.")
        return processed_data
```
### 🧪 Senaryo 6: Bir veri dönüştürme aracı kullanıcıların özel dönüştürme kuralları tanımlamasını sağlar. Kurallar veri işleme sırasında uygulanır. Kullanıcılar farklı veri formatları arasında dönüştürme yapabilir. Dönüştürme mantığı kullanıcı tarafından belirlenir.
**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini

**Satır Sayısı:** 22
```typescript

type TransformationRule = (input: string) => string;

class DataConverter {
    private rules: { [key: string]: TransformationRule } = {};

    public addRule(ruleName: string, rule: TransformationRule): void {
        this.rules[ruleName] = rule;
    }

    public applyRules(inputData: string, ruleNamesToApply: string[]): string {
        let processedData = inputData;
        for (const ruleName of ruleNamesToApply) {
            if (this.rules[ruleName]) {
                processedData = this.rules[ruleName](processedData);
            } else {
                console.warn(`Warning: Rule '${ruleName}' not found.`);
            }
        }
        return processedData;
    }
}
```
### 🧪 Senaryo 7: Bir otomatik test aracı kullanıcıların test senaryoları yazmasına olanak tanır. Test senaryoları sistem tarafından çalıştırılarak sonuçlar alınır. Kullanıcılar özel test durumları tanımlayabilir. Test mantığı kullanıcı girişlerine göre şekillenir.
**💻 Dil:** `C#`
**🤖 AI:** Gemini

**Satır Sayısı:** 52
```csharp

using System;
using System.Collections.Generic;

public class TestRunner
{
    public delegate TestResult TestCase(TestContext context);

    public class TestContext
    {
        public List<string> Logs { get; } = new List<string>();
        public void Log(string message) => Logs.Add(message);
        // Add other utilities for test cases (e.g., assertion methods)
    }

    public class TestResult
    {
        public bool IsPassed { get; set; }
        public string Message { get; set; }
        public List<string> Logs { get; set; }
    }

    private Dictionary<string, TestCase> _testCases = new Dictionary<string, TestCase>();

    public void AddTestCase(string testName, TestCase testCase)
    {
        _testCases[testName] = testCase;
    }

    public TestResult RunTest(string testName)
    {
        if (_testCases.ContainsKey(testName))
        {
            TestContext context = new TestContext();
            try
            {
                TestResult result = _testCases[testName](context);
                result.Logs.AddRange(context.Logs);
                return result;
            }
            catch (Exception ex)
            {
                context.Log($"Exception during test: {ex.Message}");
                return new TestResult { IsPassed = false, Message = $"Test failed due to exception: {ex.Message}", Logs = context.Logs };
            }
        }
        else
        {
            return new TestResult { IsPassed = false, Message = $"Test case '{testName}' not found." };
        }
    }
}
```
### 🧪 Senaryo 7: Bir otomatik test aracı kullanıcıların test senaryoları yazmasına olanak tanır. Test senaryoları sistem tarafından çalıştırılarak sonuçlar alınır. Kullanıcılar özel test durumları tanımlayabilir. Test mantığı kullanıcı girişlerine göre şekillenir.
**💻 Dil:** `Python`
**🤖 AI:** Gemini

**Satır Sayısı:** 50
```python

from typing import Callable, Dict, List

class TestContext:
    def __init__(self):
        self.logs: List[str] = []
        self.assertions_passed = 0
        self.assertions_failed = 0

    def log(self, message: str):
        self.logs.append(message)

    def assert_equals(self, actual, expected, message: str = ""):
        if actual == expected:
            self.assertions_passed += 1
            self.log(f"Assertion Passed: {message or ''} (Actual: {actual}, Expected: {expected})")
            return True
        else:
            self.assertions_failed += 1
            self.log(f"Assertion FAILED: {message or ''} (Actual: {actual}, Expected: {expected})")
            return False

class TestResult:
    def __init__(self, is_passed: bool, message: str, logs: List[str], assertions_passed: int, assertions_failed: int):
        self.is_passed = is_passed
        self.message = message
        self.logs = logs
        self.assertions_passed = assertions_passed
        self.assertions_failed = assertions_failed

class TestRunner:
    def __init__(self):
        self._test_cases: Dict[str, Callable[[TestContext], bool]] = {}

    def add_test_case(self, test_name: str, test_function: Callable[[TestContext], bool]):
        self._test_cases[test_name] = test_function

    def run_test(self, test_name: str) -> TestResult:
        if test_name not in self._test_cases:
            return TestResult(False, f"Test case '{test_name}' not found.", [], 0, 0)

        context = TestContext()
        try:
            test_function = self._test_cases[test_name]
            test_passed = test_function(context)
            final_message = "Test Passed" if test_passed and context.assertions_failed == 0 else "Test Failed"
            return TestResult(test_passed and context.assertions_failed == 0, final_message, context.logs, context.assertions_passed, context.assertions_failed)
        except Exception as e:
            context.log(f"Exception during test: {e}")
            return TestResult(False, f"Test failed due to exception: {e}", context.logs, context.assertions_passed, context.assertions_failed)
```
### 🧪 Senaryo 7: Bir otomatik test aracı kullanıcıların test senaryoları yazmasına olanak tanır. Test senaryoları sistem tarafından çalıştırılarak sonuçlar alınır. Kullanıcılar özel test durumları tanımlayabilir. Test mantığı kullanıcı girişlerine göre şekillenir.
**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini

**Satır Sayısı:** 50
```typescript

interface TestResult {
    isPassed: boolean;
    message: string;
    logs: string[];
}

class TestContext {
    public logs: string[] = [];

    public log(message: string): void {
        this.logs.push(message);
    }

    // Add assertion methods here
    public assertEquals(actual: any, expected: any, message: string = ''): boolean {
        if (actual === expected) {
            this.log(`Assertion Passed: ${message} (Actual: ${actual}, Expected: ${expected})`);
            return true;
        } else {
            this.log(`Assertion FAILED: ${message} (Actual: ${actual}, Expected: ${expected})`);
            return false;
        }
    }
}

type TestCaseFunction = (context: TestContext) => boolean;

class TestRunner {
    private testCases: { [key: string]: TestCaseFunction } = {};

    public addTestCase(testName: string, testFunction: TestCaseFunction): void {
        this.testCases[testName] = testFunction;
    }

    public runTest(testName: string): TestResult {
        const context = new TestContext();
        if (!this.testCases[testName]) {
            return { isPassed: false, message: `Test case '${testName}' not found.`, logs: [] };
        }

        try {
            const passed = this.testCases[testName](context);
            return { isPassed: passed, message: passed ? 'Test Passed' : 'Test Failed', logs: context.logs };
        } catch (e: any) {
            context.log(`Exception during test: ${e.message}`);
            return { isPassed: false, message: `Test failed due to exception: ${e.message}`, logs: context.logs };
        }
    }
}
```
### 🧪 Senaryo 8: Bir hesaplama motoru kullanıcıların özel hesaplama formülleri girmesine izin verir. Formüller sistem tarafından değerlendirilerek sonuçlar üretilir. Kullanıcılar karmaşık hesaplamalar tanımlayabilir. Hesaplama sonuçları kullanıcıya döndürülür.
**💻 Dil:** `C#`
**🤖 AI:** Gemini

**Satır Sayısı:** 34
```csharp

using System.Data;

public class CalculationEngine
{
    public object EvaluateFormula(string formulaExpression, Dictionary<string, object> variables = null)
    {
        // Using DataTable.Compute for simple expression evaluation.
        // For more advanced scenarios (e.g., custom functions, complex variable types),
        // a more sophisticated expression parser/evaluator library is recommended (e.g., NCalc).
        try
        {
            // DataTable.Compute doesn't directly support variables like "x + y".
            // You'd need to replace variables with their values in the string.
            string processedExpression = formulaExpression;
            if (variables != null)
            {
                foreach (var kvp in variables)
                {
                    // Basic string replacement; handle type conversions carefully
                    processedExpression = processedExpression.Replace(kvp.Key, kvp.Value.ToString());
                }
            }

            DataTable dt = new DataTable();
            var result = dt.Compute(processedExpression, null);
            return result;
        }
        catch (Exception ex)
        {
            return $"Error evaluating formula: {ex.Message}";
        }
    }
}
```
### 🧪 Senaryo 8: Bir hesaplama motoru kullanıcıların özel hesaplama formülleri girmesine izin verir. Formüller sistem tarafından değerlendirilerek sonuçlar üretilir. Kullanıcılar karmaşık hesaplamalar tanımlayabilir. Hesaplama sonuçları kullanıcıya döndürülür.
**💻 Dil:** `Python`
**🤖 AI:** Gemini

**Satır Sayısı:** 19
```python

import math

class CalculationEngine:
    def evaluate_formula(self, formula_expression: str, variables: dict = None):
        # Using eval() for simplicity, but be cautious with untrusted input.
        # For a production system, a safer expression evaluator should be used.
        # Variables can be passed into the namespace of eval.
        safe_dict = {
            "__builtins__": None,
            "math": math
        }
        if variables:
            safe_dict.update(variables)

        try:
            return eval(formula_expression, safe_dict)
        except Exception as e:
            return f"Error evaluating formula: {e}"
```
### 🧪 Senaryo 8: Bir hesaplama motoru kullanıcıların özel hesaplama formülleri girmesine izin verir. Formüller sistem tarafından değerlendirilerek sonuçlar üretilir. Kullanıcılar karmaşık hesaplamalar tanımlayabilir. Hesaplama sonuçları kullanıcıya döndürülür.
**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini

**Satır Sayısı:** 24
```typescript

class CalculationEngine {
    evaluateFormula(formulaExpression: string, variables?: { [key: string]: number }): any {
        // WARNING: Using eval() with untrusted user input is a security risk.
        // For a production system, consider a safe expression parser library (e.g., math.js)
        // or implement a custom parser.

        let processedExpression = formulaExpression;
        if (variables) {
            for (const key in variables) {
                if (variables.hasOwnProperty(key)) {
                    // Simple replacement; ensure variable names don't conflict with operators etc.
                    processedExpression = processedExpression.replace(new RegExp(`\\b${key}\\b`, 'g'), variables[key].toString());
                }
            }
        }

        try {
            return eval(processedExpression);
        } catch (e: any) {
            return `Error evaluating formula: ${e.message}`;
        }
    }
}
```
### 🧪 Senaryo 9: Bir içerik yönetim sistemi kullanıcıların özel içerik şablonları oluşturmasını sağlar. Şablonlar dinamik içerik üretimi için kullanılır. Kullanıcılar farklı içerik türleri için şablonlar tasarlayabilir. İçerik şablonları sistem tarafından işlenir.
**💻 Dil:** `C#`
**🤖 AI:** Gemini

**Satır Sayısı:** 33
```csharp

using System.Collections.Generic;
using System.Text.RegularExpressions;

public class ContentTemplateProcessor
{
    public string ProcessContentTemplate(string templateContent, Dictionary<string, string> contentData)
    {
        string processedContent = templateContent;

        // Simple regex-based replacement for placeholders like {{FieldName}}
        foreach (var entry in contentData)
        {
            processedContent = Regex.Replace(processedContent, $@"{{{{{entry.Key}}}}}", entry.Value, RegexOptions.IgnoreCase);
        }

        // In a real CMS, you might have more advanced templating features:
        // - Conditional logic (if/else)
        // - Loops (foreach)
        // - Partial templates / includes
        // - Custom functions
        // This would typically involve a dedicated templating engine (e.g., Razor, Handlebars.NET, Liquid).

        return processedContent;
    }

    public void SaveTemplate(string templateName, string templateContent)
    {
        // This would save the template to a database or file system
        // For demonstration, we'll just log it.
        Console.WriteLine($"Template '{templateName}' saved. Content snippet: {templateContent.Substring(0, Math.Min(templateContent.Length, 50))}...");
    }
}
```
### 🧪 Senaryo 9: Bir içerik yönetim sistemi kullanıcıların özel içerik şablonları oluşturmasını sağlar. Şablonlar dinamik içerik üretimi için kullanılır. Kullanıcılar farklı içerik türleri için şablonlar tasarlayabilir. İçerik şablonları sistem tarafından işlenir.
**💻 Dil:** `Python`
**🤖 AI:** Gemini

**Satır Sayısı:** 21
```python

import re
from typing import Dict

class ContentTemplateProcessor:
    def process_content_template(self, template_content: str, content_data: Dict[str, str]) -> str:
        processed_content = template_content

        # Simple regex-based replacement for placeholders like {{FieldName}}
        for key, value in content_data.items():
            processed_content = re.sub(r'{{' + re.escape(key) + r'}}', value, processed_content, flags=re.IGNORECASE)

        # In a real CMS, you might use a dedicated templating engine like Jinja2 or Django Templates
        # for more advanced features (conditionals, loops, includes).

        return processed_content

    def save_template(self, template_name: str, template_content: str):
        # This would save the template to a database or file system
        # For demonstration, we'll just print it.
        print(f"Template '{template_name}' saved. Content snippet: {template_content[:50]}...")
```
### 🧪 Senaryo 9: Bir içerik yönetim sistemi kullanıcıların özel içerik şablonları oluşturmasını sağlar. Şablonlar dinamik içerik üretimi için kullanılır. Kullanıcılar farklı içerik türleri için şablonlar tasarlayabilir. İçerik şablonları sistem tarafından işlenir.
**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini

**Satır Sayısı:** 24
```typescript

class ContentTemplateProcessor {
    public processContentTemplate(templateContent: string, contentData: { [key: string]: string }): string {
        let processedContent = templateContent;

        // Simple regex-based replacement for placeholders like {{FieldName}}
        for (const key in contentData) {
            if (contentData.hasOwnProperty(key)) {
                processedContent = processedContent.replace(new RegExp(`{{${key}}}`, 'gi'), contentData[key]);
            }
        }

        // For more advanced templating (conditionals, loops, etc.), a dedicated library
        // like Handlebars.js, Nunjucks, or a custom parser would be used.

        return processedContent;
    }

    public saveTemplate(templateName: string, templateContent: string): void {
        // This would typically save to a database or a file system in a Node.js environment.
        // For a browser-based app, this would involve API calls to a backend.
        console.log(`Template '${templateName}' saved. Content snippet: ${templateContent.substring(0, Math.min(templateContent.length, 50))}...`);
    }
}
```
### 🧪 Senaryo 10: Bir iş akışı motoru kullanıcıların özel iş akışı kuralları tanımlamasına olanak verir. Kurallar iş süreçleri sırasında uygulanır. Kullanıcılar iş mantığını özelleştirebilir. İş akışı adımları kullanıcı tanımlı kurallara göre çalışır.
**💻 Dil:** `C#`
**🤖 AI:** Gemini

**Satır Sayısı:** 60
```csharp

using System;
using System.Collections.Generic;
using System.Linq;

public class WorkflowEngine
{
    public delegate WorkflowResult WorkflowRule(WorkflowContext context);

    public class WorkflowContext
    {
        public Dictionary<string, object> Data { get; set; } = new Dictionary<string, object>();
        public List<string> AuditTrail { get; } = new List<string>();

        public void AddData(string key, object value) => Data[key] = value;
        public object GetData(string key) => Data.GetValueOrDefault(key);
        public void Log(string message) => AuditTrail.Add(message);
    }

    public class WorkflowResult
    {
        public bool IsSuccessful { get; set; }
        public string Message { get; set; }
        public List<string> AuditTrail { get; set; }
    }

    private Dictionary<string, WorkflowRule> _workflowRules = new Dictionary<string, WorkflowRule>();

    public void AddRule(string ruleName, WorkflowRule rule)
    {
        _workflowRules[ruleName] = rule;
    }

    public WorkflowResult ExecuteWorkflow(List<string> ruleNamesToExecute, WorkflowContext initialContext)
    {
        WorkflowContext context = initialContext ?? new WorkflowContext();
        context.Log($"Starting workflow execution with rules: {string.Join(", ", ruleNamesToExecute)}");

        foreach (var ruleName in ruleNamesToExecute)
        {
            if (_workflowRules.ContainsKey(ruleName))
            {
                context.Log($"Executing rule: {ruleName}");
                WorkflowResult ruleResult = _workflowRules[ruleName](context);
                if (!ruleResult.IsSuccessful)
                {
                    context.Log($"Rule '{ruleName}' failed: {ruleResult.Message}");
                    return new WorkflowResult { IsSuccessful = false, Message = $"Workflow stopped due to rule failure: {ruleResult.Message}", AuditTrail = context.AuditTrail };
                }
            }
            else
            {
                context.Log($"Error: Rule '{ruleName}' not found.");
                return new WorkflowResult { IsSuccessful = false, Message = $"Workflow stopped: Rule '{ruleName}' not found.", AuditTrail = context.AuditTrail };
            }
        }
        context.Log("Workflow completed successfully.");
        return new WorkflowResult { IsSuccessful = true, Message = "Workflow completed.", AuditTrail = context.AuditTrail };
    }
}
```
### 🧪 Senaryo 10: Bir iş akışı motoru kullanıcıların özel iş akışı kuralları tanımlamasına olanak verir. Kurallar iş süreçleri sırasında uygulanır. Kullanıcılar iş mantığını özelleştirebilir. İş akışı adımları kullanıcı tanımlı kurallara göre çalışır.
**💻 Dil:** `Python`
**🤖 AI:** Gemini

**Satır Sayısı:** 51
```python

from typing import Callable, Dict, List, Any

class WorkflowContext:
    def __init__(self):
        self.data: Dict[str, Any] = {}
        self.audit_trail: List[str] = []

    def add_data(self, key: str, value: Any):
        self.data[key] = value

    def get_data(self, key: str) -> Any:
        return self.data.get(key)

    def log(self, message: str):
        self.audit_trail.append(message)

class WorkflowResult:
    def __init__(self, is_successful: bool, message: str, audit_trail: List[str]):
        self.is_successful = is_successful
        self.message = message
        self.audit_trail = audit_trail

# Define a type for a workflow rule function
WorkflowRule = Callable[[WorkflowContext], WorkflowResult]

class WorkflowEngine:
    def __init__(self):
        self._workflow_rules: Dict[str, WorkflowRule] = {}

    def add_rule(self, rule_name: str, rule_function: WorkflowRule):
        self._workflow_rules[rule_name] = rule_function

    def execute_workflow(self, rule_names_to_execute: List[str], initial_context: WorkflowContext = None) -> WorkflowResult:
        context = initial_context if initial_context is not None else WorkflowContext()
        context.log(f"Starting workflow execution with rules: {', '.join(rule_names_to_execute)}")

        for rule_name in rule_names_to_execute:
            if rule_name in self._workflow_rules:
                context.log(f"Executing rule: {rule_name}")
                rule_function = self._workflow_rules[rule_name]
                rule_result = rule_function(context)
                if not rule_result.is_successful:
                    context.log(f"Rule '{rule_name}' failed: {rule_result.message}")
                    return WorkflowResult(False, f"Workflow stopped due to rule failure: {rule_result.message}", context.audit_trail)
            else:
                context.log(f"Error: Rule '{rule_name}' not found.")
                return WorkflowResult(False, f"Workflow stopped: Rule '{rule_name}' not found.", context.audit_trail)

        context.log("Workflow completed successfully.")
        return WorkflowResult(True, "Workflow completed.", context.audit_trail)
```
### 🧪 Senaryo 10: Bir iş akışı motoru kullanıcıların özel iş akışı kuralları tanımlamasına olanak verir. Kurallar iş süreçleri sırasında uygulanır. Kullanıcılar iş mantığını özelleştirebilir. İş akışı adımları kullanıcı tanımlı kurallara göre çalışır.
**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini

**Satır Sayısı:** 53
```typescript

interface WorkflowResult {
    isSuccessful: boolean;
    message: string;
    auditTrail: string[];
}

class WorkflowContext {
    public data: { [key: string]: any } = {};
    public auditTrail: string[] = [];

    public addData(key: string, value: any): void {
        this.data[key] = value;
    }

    public getData(key: string): any {
        return this.data[key];
    }

    public log(message: string): void {
        this.auditTrail.push(message);
    }
}

type WorkflowRuleFunction = (context: WorkflowContext) => WorkflowResult;

class WorkflowEngine {
    private workflowRules: { [key: string]: WorkflowRuleFunction } = {};

    public addRule(ruleName: string, ruleFunction: WorkflowRuleFunction): void {
        this.workflowRules[ruleName] = ruleFunction;
    }

    public executeWorkflow(ruleNamesToExecute: string[], initialContext?: WorkflowContext): WorkflowResult {
        const context = initialContext || new WorkflowContext();
        context.log(`Starting workflow execution with rules: ${ruleNamesToExecute.join(', ')}`);

        for (const ruleName of ruleNamesToExecute) {
            if (this.workflowRules[ruleName]) {
                context.log(`Executing rule: ${ruleName}`);
                const ruleResult = this.workflowRules[ruleName](context);
                if (!ruleResult.isSuccessful) {
                    context.log(`Rule '${ruleName}' failed: ${ruleResult.message}`);
                    return { isSuccessful: false, message: `Workflow stopped due to rule failure: ${ruleResult.message}`, auditTrail: context.auditTrail };
                }
            } else {
                context.log(`Error: Rule '${ruleName}' not found.`);
                return { isSuccessful: false, message: `Workflow stopped: Rule '${ruleName}' not found.`, auditTrail: context.auditTrail };
            }
        }
        context.log("Workflow completed successfully.");
        return { isSuccessful: true, message: "Workflow completed.", auditTrail: context.auditTrail };
    }
```
}