 ### 🧪 Senaryo 1: Bir şablon oluşturma uygulamasında kullanıcılar özel şablonlar tasarlar. Şablon sistemi kullanıcı girişlerini işleyerek çıktı üretir. Kullanıcılar farklı şablon türleri oluşturabilir. Şablonlar sistem tarafından derlenip çalıştırılır.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("create-template")]
public IActionResult CreateTemplate([FromBody] TemplateRequest request)
{
    try
    {
        var template = new Template
        {
            Name = request.Name,
            Content = request.Content,
            Type = request.Type,
            CreatedBy = request.UserId,
            CreatedDate = DateTime.UtcNow
        };

        var compiledTemplate = _templateEngine.Compile(template.Content);
        template.CompiledContent = compiledTemplate;
        template.IsValid = true;

        _context.Templates.Add(template);
        _context.SaveChanges();

        return Ok(new { TemplateId = template.Id, Status = "Created" });
    }
    catch (TemplateCompilationException ex)
    {
        return BadRequest(new { Error = "Template compilation failed", Details = ex.Message });
    }
}

[HttpPost("execute-template")]
public IActionResult ExecuteTemplate([FromBody] ExecuteTemplateRequest request)
{
    var template = _context.Templates.Find(request.TemplateId);
    if (template == null) return NotFound();

    var output = _templateEngine.Execute(template.CompiledContent, request.Parameters);
    
    _context.TemplateExecutions.Add(new TemplateExecution
    {
        TemplateId = request.TemplateId,
        Parameters = JsonSerializer.Serialize(request.Parameters),
        Output = output,
        ExecutedAt = DateTime.UtcNow
    });
    _context.SaveChanges();

    return Ok(new { Output = output });
}
```

----

### 🧪 Senaryo 1: Bir şablon oluşturma uygulamasında kullanıcılar özel şablonlar tasarlar. Şablon sistemi kullanıcı girişlerini işleyerek çıktı üretir. Kullanıcılar farklı şablon türleri oluşturabilir. Şablonlar sistem tarafından derlenip çalıştırılır.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
from flask import Flask, request, jsonify
from datetime import datetime
import json
import re

class TemplateEngine:
    def __init__(self):
        self.templates = {}
    
    def compile_template(self, content):
        # Simple template compilation with variable replacement
        variables = re.findall(r'\{\{(\w+)\}\}', content)
        return {
            'content': content,
            'variables': variables,
            'compiled_at': datetime.utcnow()
        }
    
    def execute_template(self, compiled_template, parameters):
        content = compiled_template['content']
        for var in compiled_template['variables']:
            if var in parameters:
                content = content.replace(f'{{{{{var}}}}}', str(parameters[var]))
        return content

@app.route('/create-template', methods=['POST'])
def create_template():
    data = request.json
    template_engine = TemplateEngine()
    
    try:
        compiled = template_engine.compile_template(data['content'])
        template = {
            'id': len(template_engine.templates) + 1,
            'name': data['name'],
            'type': data['type'],
            'content': data['content'],
            'compiled': compiled,
            'created_by': data['user_id'],
            'created_date': datetime.utcnow().isoformat()
        }
        
        template_engine.templates[template['id']] = template
        return jsonify({'template_id': template['id'], 'status': 'created'})
    
    except Exception as e:
        return jsonify({'error': 'Template compilation failed', 'details': str(e)}), 400

@app.route('/execute-template', methods=['POST'])
def execute_template():
    data = request.json
    template_engine = TemplateEngine()
    
    template = template_engine.templates.get(data['template_id'])
    if not template:
        return jsonify({'error': 'Template not found'}), 404
    
    output = template_engine.execute_template(template['compiled'], data['parameters'])
    return jsonify({'output': output})
```

----

### 🧪 Senaryo 1: Bir şablon oluşturma uygulamasında kullanıcılar özel şablonlar tasarlar. Şablon sistemi kullanıcı girişlerini işleyerek çıktı üretir. Kullanıcılar farklı şablon türleri oluşturabilir. Şablonlar sistem tarafından derlenip çalıştırılır.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
interface Template {
  id: string;
  name: string;
  content: string;
  type: string;
  compiledContent: CompiledTemplate;
  createdBy: string;
  createdDate: Date;
}

interface CompiledTemplate {
  content: string;
  variables: string[];
  compiledAt: Date;
}

class TemplateEngine {
  private templates: Map<string, Template> = new Map();

  compileTemplate(content: string): CompiledTemplate {
    const variables = content.match(/\{\{(\w+)\}\}/g)?.map(v => v.slice(2, -2)) || [];
    return {
      content,
      variables,
      compiledAt: new Date()
    };
  }

  executeTemplate(compiled: CompiledTemplate, parameters: Record<string, any>): string {
    let output = compiled.content;
    compiled.variables.forEach(variable => {
      if (parameters[variable] !== undefined) {
        output = output.replace(new RegExp(`\\{\\{${variable}\\}\\}`, 'g'), String(parameters[variable]));
      }
    });
    return output;
  }

  createTemplate(name: string, content: string, type: string, userId: string): string {
    const templateId = Date.now().toString();
    const compiled = this.compileTemplate(content);
    
    const template: Template = {
      id: templateId,
      name,
      content,
      type,
      compiledContent: compiled,
      createdBy: userId,
      createdDate: new Date()
    };

    this.templates.set(templateId, template);
    return templateId;
  }

  executeById(templateId: string, parameters: Record<string, any>): string | null {
    const template = this.templates.get(templateId);
    return template ? this.executeTemplate(template.compiledContent, parameters) : null;
  }
}
```

----

### 🧪 Senaryo 2: Bir rapor oluşturma aracında kullanıcılar özel formüller yazabilir. Formül motoru bu ifadeleri değerlendirerek sonuçları hesaplar. Kullanıcılar matematiksel ve mantıksal işlemler tanımlayabilir. Hesaplanan sonuçlar raporda gösterilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("create-formula")]
public IActionResult CreateFormula([FromBody] FormulaRequest request)
{
    try
    {
        var formula = new Formula
        {
            Name = request.Name,
            Expression = request.Expression,
            Description = request.Description,
            CreatedBy = request.UserId
        };

        var validator = new FormulaValidator();
        if (!validator.IsValid(formula.Expression))
            return BadRequest(new { Error = "Invalid formula syntax" });

        _context.Formulas.Add(formula);
        _context.SaveChanges();

        return Ok(new { FormulaId = formula.Id });
    }
    catch (Exception ex)
    {
        return BadRequest(new { Error = ex.Message });
    }
}

[HttpPost("calculate")]
public IActionResult Calculate([FromBody] CalculateRequest request)
{
    var formula = _context.Formulas.Find(request.FormulaId);
    if (formula == null) return NotFound();

    var evaluator = new FormulaEvaluator();
    var result = evaluator.Evaluate(formula.Expression, request.Variables);

    _context.Calculations.Add(new Calculation
    {
        FormulaId = request.FormulaId,
        Variables = JsonSerializer.Serialize(request.Variables),
        Result = result,
        CalculatedAt = DateTime.UtcNow
    });
    _context.SaveChanges();

    return Ok(new { Result = result, Formula = formula.Expression });
}

public class FormulaEvaluator
{
    public double Evaluate(string expression, Dictionary<string, double> variables)
    {
        foreach (var variable in variables)
        {
            expression = expression.Replace(variable.Key, variable.Value.ToString());
        }
        
        var dataTable = new System.Data.DataTable();
        return Convert.ToDouble(dataTable.Compute(expression, null));
    }
}
```

----

### 🧪 Senaryo 2: Bir rapor oluşturma aracında kullanıcılar özel formüller yazabilir. Formül motoru bu ifadeleri değerlendirerek sonuçları hesaplar. Kullanıcılar matematiksel ve mantıksal işlemler tanımlayabilir. Hesaplanan sonuçlar raporda gösterilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import re
import math
from datetime import datetime

class FormulaEngine:
    def __init__(self):
        self.formulas = {}
        self.safe_functions = {
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'sqrt': math.sqrt, 'log': math.log, 'abs': abs,
            'min': min, 'max': max, 'sum': sum
        }
    
    def validate_formula(self, expression):
        # Basic validation for safe expressions
        allowed_chars = r'[a-zA-Z0-9+\-*/().,<>=! ]'
        return bool(re.match(f'^{allowed_chars}+$', expression))
    
    def evaluate_formula(self, expression, variables):
        if not self.validate_formula(expression):
            raise ValueError("Invalid formula syntax")
        
        # Replace variables in expression
        for var, value in variables.items():
            expression = expression.replace(var, str(value))
        
        # Create safe evaluation environment
        safe_dict = {"__builtins__": {}}
        safe_dict.update(self.safe_functions)
        
        try:
            result = eval(expression, safe_dict)
            return float(result)
        except Exception as e:
            raise ValueError(f"Formula evaluation error: {str(e)}")

@app.route('/create-formula', methods=['POST'])
def create_formula():
    data = request.json
    formula_engine = FormulaEngine()
    
    try:
        if not formula_engine.validate_formula(data['expression']):
            return jsonify({'error': 'Invalid formula syntax'}), 400
        
        formula_id = len(formula_engine.formulas) + 1
        formula_engine.formulas[formula_id] = {
            'id': formula_id,
            'name': data['name'],
            'expression': data['expression'],
            'description': data.get('description', ''),
            'created_by': data['user_id'],
            'created_date': datetime.utcnow().isoformat()
        }
        
        return jsonify({'formula_id': formula_id})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

----

### 🧪 Senaryo 8: Bir hesaplama motoru kullanıcıların özel hesaplama formülleri girmesine izin verir. Formüller sistem tarafından değerlendirilerek sonuçlar üretilir. Kullanıcılar karmaşık hesaplamalar tanımlayabilir. Hesaplama sonuçları kullanıcıya döndürülür.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
interface Calculation {
  id: string;
  name: string;
  formula: string;
  description: string;
  variables: Record<string, number>;
  createdBy: string;
  createdDate: Date;
}

interface CalculationResult {
  result: number;
  formula: string;
  inputValues: Record<string, number>;
  executedAt: Date;
}

type MathFunction = (args: number[]) => number;

class CalculationEngine {
  private calculations: Map<string, Calculation> = new Map();
  private calculationResults: CalculationResult[] = [];
  
  private functions: Record<string, MathFunction> = {
    SUM: (args) => args.reduce((sum, val) => sum + val, 0),
    AVG: (args) => args.length > 0 ? args.reduce((sum, val) => sum + val, 0) / args.length : 0,
    MAX: (args) => args.length > 0 ? Math.max(...args) : 0,
    MIN: (args) => args.length > 0 ? Math.min(...args) : 0,
    SQRT: (args) => args.length > 0 ? Math.sqrt(args[0]) : 0,
    POW: (args) => args.length >= 2 ? Math.pow(args[0], args[1]) : 0,
    SIN: (args) => args.length > 0 ? Math.sin(args[0]) : 0,
    COS: (args) => args.length > 0 ? Math.cos(args[0]) : 0,
    TAN: (args) => args.length > 0 ? Math.tan(args[0]) : 0,
    LOG: (args) => args.length > 0 && args[0] > 0 ? Math.log(args[0]) : 0,
    ABS: (args) => args.length > 0 ? Math.abs(args[0]) : 0
  };

  private constants: Record<string, number> = {
    PI: Math.PI,
    E: Math.E
  };

  validateFormula(formula: string): { isValid: boolean; error?: string } {
    const allowedPattern = /^[a-zA-Z0-9+\-*/().,<>=!\s]+$/;
    if (!allowedPattern.test(formula)) {
      return { isValid: false, error: 'Invalid characters in formula' };
    }

    const openParens = (formula.match(/\(/g) || []).length;
    const closeParens = (formula.match(/\)/g) || []).length;
    if (openParens !== closeParens) {
      return { isValid: false, error: 'Unbalanced parentheses' };
    }

    return { isValid: true };
  }

  createCalculation(
    name: string,
    formula: string,
    description: string,
    variables: Record<string, number>,
    userId: string
  ): string {
    const validation = this.validateFormula(formula);
    if (!validation.isValid) {
      throw new Error(validation.error);
    }

    const calculationId = Date.now().toString();
    
    const calculation: Calculation = {
      id: calculationId,
      name,
      formula,
      description,
      variables,
      createdBy: userId,
      createdDate: new Date()
    };

    this.calculations.set(calculationId, calculation);
    return calculationId;
  }

  executeCalculation(calculationId: string, inputValues: Record<string, number>): CalculationResult {
    const calculation = this.calculations.get(calculationId);
    if (!calculation) {
      throw new Error('Calculation not found');
    }

    try {
      const result = this.calculate(calculation.formula, inputValues);
      
      const calculationResult: CalculationResult = {
        result,
        formula: calculation.formula,
        inputValues,
        executedAt: new Date()
      };

      this.calculationResults.push(calculationResult);
      return calculationResult;
    } catch (error) {
      throw new Error(`Calculation error: ${error.message}`);
    }
  }

  private calculate(formula: string, variables: Record<string, number>): number {
    const processedFormula = this.processFormula(formula, variables);
    
    try {
      // Use Function constructor for safer evaluation than eval
      const result = new Function('Math', `return ${processedFormula}`)(Math);
      return Number(result);
    } catch (error) {
      throw new Error(`Formula evaluation error: ${error.message}`);
    }
  }

  private processFormula(formula: string, variables: Record<string, number>): string {
    let processed = formula;

    // Replace variables with their values
    Object.entries(variables).forEach(([varName, varValue]) => {
      const regex = new RegExp(varName, 'g');
      processed = processed.replace(regex, varValue.toString());
    });

    // Replace constants
    Object.entries(this.constants).forEach(([constName, constValue]) => {
      const regex = new RegExp(constName, 'g');
      processed = processed.replace(regex, constValue.toString());
    });

    // Replace functions
    Object.entries(this.functions).forEach(([funcName, funcImpl]) => {
      processed = this.replaceFunctions(processed, funcName, funcImpl);
    });

    return processed;
  }

  private replaceFunctions(formula: string, funcName: string, funcImpl: MathFunction): string {
    const pattern = new RegExp(`${funcName}\\(([^)]+)\\)`, 'g');
    
    return formula.replace(pattern, (match, argsStr) => {
      const args = argsStr.split(',').map((arg: string) => parseFloat(arg.trim()));
      return funcImpl(args).toString();
    });
  }

  getCalculation(calculationId: string): Calculation | undefined {
    return this.calculations.get(calculationId);
  }

  getCalculationResults(): CalculationResult[] {
    return [...this.calculationResults];
  }
}
```

----

### 🧪 Senaryo 9: Bir içerik yönetim sistemi kullanıcıların özel içerik şablonları oluşturmasını sağlar. Şablonlar dinamik içerik üretimi için kullanılır. Kullanıcılar farklı içerik türleri için şablonlar tasarlayabilir. İçerik şablonları sistem tarafından işlenir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("create-content-template")]
public IActionResult CreateContentTemplate([FromBody] ContentTemplateRequest request)
{
    try
    {
        var template = new ContentTemplate
        {
            Name = request.Name,
            ContentType = request.ContentType,
            TemplateBody = request.TemplateBody,
            Fields = JsonSerializer.Serialize(request.Fields),
            CreatedBy = request.UserId,
            CreatedDate = DateTime.UtcNow
        };

        _context.ContentTemplates.Add(template);
        _context.SaveChanges();

        return Ok(new { TemplateId = template.Id });
    }
    catch (Exception ex)
    {
        return BadRequest(new { Error = ex.Message });
    }
}

[HttpPost("generate-content")]
public IActionResult GenerateContent([FromBody] ContentGenerationRequest request)
{
    var template = _context.ContentTemplates.Find(request.TemplateId);
    if (template == null) return NotFound();

    try
    {
        var generator = new ContentGenerator();
        var content = generator.GenerateContent(template, request.Data);

        _context.GeneratedContents.Add(new GeneratedContent
        {
            TemplateId = request.TemplateId,
            Content = content,
            Data = JsonSerializer.Serialize(request.Data),
            GeneratedAt = DateTime.UtcNow
        });
        _context.SaveChanges();

        return Ok(new { Content = content });
    }
    catch (Exception ex)
    {
        return BadRequest(new { Error = ex.Message });
    }
}

public class ContentGenerator
{
    public string GenerateContent(ContentTemplate template, Dictionary<string, object> data)
    {
        var content = template.TemplateBody;
        var fields = JsonSerializer.Deserialize<List<TemplateField>>(template.Fields);

        foreach (var field in fields)
        {
            var placeholder = $"{{{{{field.Name}}}}}";
            var value = GetFieldValue(field, data);
            content = content.Replace(placeholder, value);
        }

        return ProcessConditionals(content, data);
    }

    private string GetFieldValue(TemplateField field, Dictionary<string, object> data)
    {
        if (!data.ContainsKey(field.Name))
            return field.DefaultValue ?? "";

        var value = data[field.Name];

        switch (field.Type.ToLower())
        {
            case "date":
                return FormatDate(value, field.Format);
            case "number":
                return FormatNumber(value, field.Format);
            case "text":
                return value.ToString();
            default:
                return value.ToString();
        }
    }

    private string FormatDate(object value, string format)
    {
        if (DateTime.TryParse(value.ToString(), out var date))
            return date.ToString(format ?? "yyyy-MM-dd");
        return value.ToString();
    }

    private string FormatNumber(object value, string format)
    {
        if (double.TryParse(value.ToString(), out var number))
            return number.ToString(format ?? "F2");
        return value.ToString();
    }

    private string ProcessConditionals(string content, Dictionary<string, object> data)
    {
        var conditionalPattern = @"\{\{if\s+(\w+)\}\}(.*?)\{\{endif\}\}";
        return Regex.Replace(content, conditionalPattern, match =>
        {
            var condition = match.Groups[1].Value;
            var conditionalContent = match.Groups[2].Value;
            
            if (data.ContainsKey(condition) && Convert.ToBoolean(data[condition]))
                return conditionalContent;
            
            return "";
        }, RegexOptions.Singleline);
    }
}
```

----

### 🧪 Senaryo 9: Bir içerik yönetim sistemi kullanıcıların özel içerik şablonları oluşturmasını sağlar. Şablonlar dinamik içerik üretimi için kullanılır. Kullanıcılar farklı içerik türleri için şablonlar tasarlayabilir. İçerik şablonları sistem tarafından işlenir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import re
import json
from datetime import datetime

class ContentGenerator:
    def __init__(self):
        self.content_templates = {}
        self.generated_contents = []
        self.field_processors = {
            'text': self.process_text_field,
            'date': self.process_date_field,
            'number': self.process_number_field,
            'html': self.process_html_field,
            'list': self.process_list_field
        }
    
    def create_content_template(self, name, content_type, template_body, fields, user_id):
        template_id = len(self.content_templates) + 1
        template = {
            'id': template_id,
            'name': name,
            'content_type': content_type,
            'template_body': template_body,
            'fields': fields,
            'created_by': user_id,
            'created_date': datetime.utcnow().isoformat()
        }
        
        self.content_templates[template_id] = template
        return template_id
    
    def generate_content(self, template_id, data):
        template = self.content_templates.get(template_id)
        if not template:
            raise ValueError("Content template not found")
        
        try:
            content = self.process_template(template, data)
            
            generated = {
                'template_id': template_id,
                'content': content,
                'data': data,
                'generated_at': datetime.utcnow().isoformat()
            }
            
            self.generated_contents.append(generated)
            return content
        except Exception as e:
            raise ValueError(f"Content generation error: {str(e)}")
    
    def process_template(self, template, data):
        content = template['template_body']
        
        # Replace field placeholders
        for field in template['fields']:
            placeholder = f"{{{{{field['name']}}}}}"
            value = self.get_field_value(field, data)
            content = content.replace(placeholder, str(value))
        
        # Process conditionals
        content = self.process_conditionals(content, data)
        
        # Process loops
        content = self.process_loops(content, data)
        
        return content
    
    def get_field_value(self, field, data):
        field_name = field['name']
        field_type = field.get('type', 'text')
        default_value = field.get('default_value', '')
        
        value = data.get(field_name, default_value)
        
        if field_type in self.field_processors:
            return self.field_processors[field_type](value, field)
        
        return str(value)
    
    def process_text_field(self, value, field):
        max_length = field.get('max_length')
        if max_length and len(str(value)) > max_length:
            return str(value)[:max_length] + '...'
        return str(value)
    
    def process_date_field(self, value, field):
        date_format = field.get('format', '%Y-%m-%d')
        try:
            if isinstance(value, str):
                date_obj = datetime.fromisoformat(value.replace('Z', '+00:00'))
            else:
                date_obj = datetime.fromisoformat(str(value))
            return date_obj.strftime(date_format)
        except:
            return str(value)
    
    def process_number_field(self, value, field):
        number_format = field.get('format', '.2f')
        try:
            return format(float(value), number_format)
        except:
            return str(value)
    
    def process_html_field(self, value, field):
        # Basic HTML sanitization
        allowed_tags = field.get('allowed_tags', ['p', 'br', 'strong', 'em'])
        # Simple implementation - in production, use proper HTML sanitizer
        return str(value)
    
    def process_list_field(self, value, field):
        separator = field.get('separator', ', ')
        if isinstance(value, list):
            return separator.join(str(item) for item in value)
        return str(value)
    
    def process_conditionals(self, content, data):
        pattern = r'\{\{if\s+(\w+)\}\}(.*?)\{\{endif\}\}'
        
        def replace_conditional(match):
            condition = match.group(1)
            conditional_content = match.group(2)
            
            if condition in data and data[condition]:
                return conditional_content
            return ''
        
        return re.sub(pattern, replace_conditional, content, flags=re.DOTALL)
    
    def process_loops(self, content, data):
        pattern = r'\{\{for\s+(\w+)\s+in\s+(\w+)\}\}(.*?)\{\{endfor\}\}'
        
        def replace_loop(match):
            item_var = match.group(1)
            list_var = match.group(2)
            loop_content = match.group(3)
            
            if list_var in data and isinstance(data[list_var], list):
                result = ''
                for item in data[list_var]:
                    item_content = loop_content.replace(f'{{{{{item_var}}}}}', str(item))
                    result += item_content
                return result
            return ''
        
        return re.sub(pattern, replace_loop, content, flags=re.DOTALL)

@app.route('/create-content-template', methods=['POST'])
def create_content_template():
    data = request.json
    generator = ContentGenerator()
    
    try:
        template_id = generator.create_content_template(
            data['name'],
            data['content_type'],
            data['template_body'],
            data['fields'],
            data['user_id']
        )
        return jsonify({'template_id': template_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/generate-content', methods=['POST'])
def generate_content():
    data = request.json
    generator = ContentGenerator()
    
    try:
        content = generator.generate_content(data['template_id'], data['data'])
        return jsonify({'content': content})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
```

----

### 🧪 Senaryo 9: Bir içerik yönetim sistemi kullanıcıların özel içerik şablonları oluşturmasını sağlar. Şablonlar dinamik içerik üretimi için kullanılır. Kullanıcılar farklı içerik türleri için şablonlar tasarlayabilir. İçerik şablonları sistem tarafından işlenir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
interface ContentTemplate {
  id: string;
  name: string;
  contentType: string;
  templateBody: string;
  fields: TemplateField[];
  createdBy: string;
  createdDate: Date;
}

interface TemplateField {
  name: string;
  type: 'text' | 'date' | 'number' | 'html' | 'list';
  defaultValue?: any;
  format?: string;
  maxLength?: number;
  allowedTags?: string[];
  separator?: string;
}

interface GeneratedContent {
  templateId: string;
  content: string;
  data: Record<string, any>;
  generatedAt: Date;
}

class ContentGenerator {
  private contentTemplates: Map<string, ContentTemplate> = new Map();
  private generatedContents: GeneratedContent[] = [];

  createContentTemplate(
    name: string,
    contentType: string,
    templateBody: string,
    fields: TemplateField[],
    userId: string
  ): string {
    const templateId = Date.now().toString();
    
    const template: ContentTemplate = {
      id: templateId,
      name,
      contentType,
      templateBody,
      fields,
      createdBy: userId,
      createdDate: new Date()
    };

    this.contentTemplates.set(templateId, template);
    return templateId;
  }

  generateContent(templateId: string, data: Record<string, any>): string {
    const template = this.contentTemplates.get(templateId);
    if (!template) {
      throw new Error('Content template not found');
    }

    try {
      const content = this.processTemplate(template, data);
      
      const generated: GeneratedContent = {
        templateId,
        content,
        data,
        generatedAt: new Date()
      };

      this.generatedContents.push(generated);
      return content;
    } catch (error) {
      throw new Error(`Content generation error: ${error.message}`);
    }
  }

  private processTemplate(template: ContentTemplate, data: Record<string, any>): string {
    let content = template.templateBody;

    // Replace field placeholders
    template.fields.forEach(field => {
      const placeholder = `{{${field.name}}}`;
      const value = this.getFieldValue(field, data);
      content = content.replace(new RegExp(placeholder, 'g'), String(value));
    });

    // Process conditionals
    content = this.processConditionals(content, data);

    // Process loops
    content = this.processLoops(content, data);

    return content;
  }

  private getFieldValue(field: TemplateField, data: Record<string, any>): any {
    const value = data[field.name] ?? field.defaultValue ?? '';

    switch (field.type) {
      case 'text':
        return this.processTextField(value, field);
      case 'date':
        return this.processDateField(value, field);
      case 'number':
        return this.processNumberField(value, field);
      case 'html':
        return this.processHtmlField(value, field);
      case 'list':
        return this.processListField(value, field);
      default:
        return String(value);
    }
  }

  private processTextField(value: any, field: TemplateField): string {
    const stringValue = String(value);
    if (field.maxLength && stringValue.length > field.maxLength) {
      return stringValue.substring(0, field.maxLength) + '...';
    }
    return stringValue;
  }

  private processDateField(value: any, field: TemplateField): string {
    try {
      const date = new Date(value);
      if (isNaN(date.getTime())) {
        return String(value);
      }
      
      const format = field.format || 'YYYY-MM-DD';
      return this.formatDate(date, format);
    } catch {
      return String(value);
    }
  }

  private processNumberField(value: any, field: TemplateField): string {
    try {
      const number = Number(value);
      if (isNaN(number)) {
        return String(value);
      }
      
      const format = field.format || '.2f';
      return number.toFixed(2);
    } catch {
      return String(value);
    }
  }

  private processHtmlField(value: any, field: TemplateField): string {
    // Basic HTML processing - in production, use proper HTML sanitizer
    return String(value);
  }

  private processListField(value: any, field: TemplateField): string {
    const separator = field.separator || ', ';
    if (Array.isArray(value)) {
      return value.map(item => String(item)).join(separator);
    }
    return String(value);
  }

  private processConditionals(content: string, data: Record<string, any>): string {
    const conditionalPattern = /\{\{if\s+(\w+)\}\}(.*?)\{\{endif\}\}/gs;
    
    return content.replace(conditionalPattern, (match, condition, conditionalContent) => {
      if (data[condition]) {
        return conditionalContent;
      }
      return '';
    });
  }

  private processLoops(content: string, data: Record<string, any>): string {
    const loopPattern = /\{\{for\s+(\w+)\s+in\s+(\w+)\}\}(.*?)\{\{endfor\}\}/gs;
    
    return content.replace(loopPattern, (match, itemVar, listVar, loopContent) => {
      if (Array.isArray(data[listVar])) {
        return data[listVar].map((item: any) => {
          return loopContent.replace(new RegExp(`\\{\\{${itemVar}\\}\\}`, 'g'), String(item));
        }).join('');
      }
      return '';
    });
  }

  private formatDate(date: Date, format: string): string {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    
    return format
      .replace('YYYY', String(year))
      .replace('MM', month)
      .replace('DD', day);
  }

  getContentTemplate(templateId: string): ContentTemplate | undefined {
    return this.contentTemplates.get(templateId);
  }

  getGeneratedContents(): GeneratedContent[] {
    return [...this.generatedContents];
  }
}
```

----

### 🧪 Senaryo 10: Bir iş akışı motoru kullanıcıların özel iş akışı kuralları tanımlamasına olanak verir. Kurallar iş süreçleri sırasında uygulanır. Kullanıcılar iş mantığını özelleştirebilir. İş akışı adımları kullanıcı tanımlı kurallara göre çalışır.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("create-workflow")]
public IActionResult CreateWorkflow([FromBody] WorkflowRequest request)
{
    try
    {
        var workflow = new Workflow
        {
            Name = request.Name,
            Description = request.Description,
            Steps = JsonSerializer.Serialize(request.Steps),
            Rules = JsonSerializer.Serialize(request.Rules),
            CreatedBy = request.UserId,
            CreatedDate = DateTime.UtcNow
        };

        _context.Workflows.Add(workflow);
        _context.SaveChanges();

        return Ok(new { WorkflowId = workflow.Id });
    }
    catch (Exception ex)
    {
        return BadRequest(new { Error = ex.Message });
    }
}

[HttpPost("execute-workflow/{workflowId}")]
public IActionResult ExecuteWorkflow(int workflowId, [FromBody] WorkflowExecutionRequest request)
{
    var workflow = _context.Workflows.Find(workflowId);
    if (workflow == null) return NotFound();

    try
    {
        var engine = new WorkflowEngine();
        var result = engine.ExecuteWorkflow(workflow, request.InputData);

        _context.WorkflowExecutions.Add(new WorkflowExecution
        {
            WorkflowId = workflowId,
            InputData = JsonSerializer.Serialize(request.InputData),
            Result = JsonSerializer.Serialize(result),
            Status = result.Status,
            ExecutedAt = DateTime.UtcNow
        });
        _context.SaveChanges();

        return Ok(result);
    }
    catch (Exception ex)
    {
        return BadRequest(new { Error = ex.Message });
    }
}

public class WorkflowEngine
{
    public WorkflowResult ExecuteWorkflow(Workflow workflow, Dictionary<string, object> inputData)
    {
        var steps = JsonSerializer.Deserialize<List<WorkflowStep>>(workflow.Steps);
        var rules = JsonSerializer.Deserialize<List<WorkflowRule>>(workflow.Rules);
        
        var result = new WorkflowResult
        {
            WorkflowName = workflow.Name,
            StartTime = DateTime.UtcNow,
            StepResults = new List<StepExecutionResult>(),
            Data = new Dictionary<string, object>(inputData)
        };

        foreach (var step in steps)
        {
            var stepResult = ExecuteStep(step, result.Data, rules);
            result.StepResults.Add(stepResult);
            
            if (!stepResult.Success)
            {
                result.Status = "Failed";
                result.ErrorMessage = stepResult.ErrorMessage;
                break;
            }
            
            // Update workflow data with step output
            if (stepResult.OutputData != null)
            {
                foreach (var output in stepResult.OutputData)
                {
                    result.Data[output.Key] = output.Value;
                }
            }
        }

        result.EndTime = DateTime.UtcNow;
        if (result.Status != "Failed") result.Status = "Completed";
        
        return result;
    }

    private StepExecutionResult ExecuteStep(WorkflowStep step, Dictionary<string, object> workflowData, List<WorkflowRule> rules)
    {
        var stepResult = new StepExecutionResult
        {
            StepName = step.Name,
            StepType = step.Type,
            StartTime = DateTime.UtcNow
        };

        try
        {
            // Apply rules before step execution
            var applicableRules = rules.Where(r => r.StepName == step.Name).ToList();
            foreach (var rule in applicableRules)
            {
                if (!EvaluateRule(rule, workflowData))
                {
                    stepResult.Success = false;
                    stepResult.ErrorMessage = $"Rule validation failed: {rule.Description}";
                    return stepResult;
                }
            }

            // Execute step based on type
            switch (step.Type.ToLower())
            {
                case "approval":
                    stepResult = ExecuteApprovalStep(step, workflowData);
                    break;
                case "notification":
                    stepResult = ExecuteNotificationStep(step, workflowData);
                    break;
                case "calculation":
                    stepResult = ExecuteCalculationStep(step, workflowData);
                    break;
                default:
                    stepResult.Success = true;
                    stepResult.Message = $"Executed {step.Type} step: {step.Name}";
                    break;
            }
        }
        catch (Exception ex)
        {
            stepResult.Success = false;
            stepResult.ErrorMessage = ex.Message;
        }

        stepResult.EndTime = DateTime.UtcNow;
        return stepResult;
    }

    private bool EvaluateRule(WorkflowRule rule, Dictionary<string, object> data)
    {
        // Simple rule evaluation
        switch (rule.Type.ToLower())
        {
            case "condition":
                return EvaluateCondition(rule.Expression, data);
            case "validation":
                return ValidateData(rule.Expression, data);
            default:
                return true;
        }
    }

    private bool EvaluateCondition(string expression, Dictionary<string, object> data)
    {
        // Simple expression evaluation
        foreach (var kvp in data)
        {
            expression = expression.Replace($"{{{kvp.Key}}}", kvp.Value.ToString());
        }
        
        var dataTable = new System.Data.DataTable();
        var result = dataTable.Compute(expression, null);
        return Convert.ToBoolean(result);
    }
}
```

----

### 🧪 Senaryo 10: Bir iş akışı motoru kullanıcıların özel iş akışı kuralları tanımlamasına olanak verir. Kurallar iş süreçleri sırasında uygulanır. Kullanıcılar iş mantığını özelleştirebilir. İş akışı adımları kullanıcı tanımlı kurallara göre çalışır.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import json
from datetime import datetime
from enum import Enum

class StepType(Enum):
    APPROVAL = "approval"
    NOTIFICATION = "notification"
    CALCULATION = "calculation"
    CONDITION = "condition"
    DATA_TRANSFORM = "data_transform"

class WorkflowEngine:
    def __init__(self):
        self.workflows = {}
        self.workflow_executions = []
        self.step_handlers = {
            'approval': self.execute_approval_step,
            'notification': self.execute_notification_step,
            'calculation': self.execute_calculation_step,
            'condition': self.execute_condition_step,
            'data_transform': self.execute_data_transform_step
        }
    
    def create_workflow(self, name, description, steps, rules, user_id):
        workflow_id = len(self.workflows) + 1
        workflow = {
            'id': workflow_id,
            'name': name,
            'description': description,
            'steps': steps,
            'rules': rules,
            'created_by': user_id,
            'created_date': datetime.utcnow().isoformat()
        }
        
        self.workflows[workflow_id] = workflow
        return workflow_id
    
    def execute_workflow(self, workflow_id, input_data):
        workflow = self.workflows.get(workflow_id)
        if not workflow:
            raise ValueError("Workflow not found")
        
        execution_result = {
            'workflow_id': workflow_id,
            'workflow_name': workflow['name'],
            'start_time': datetime.utcnow().isoformat(),
            'status': 'Running',
            'step_results': [],
            'data': dict(input_data),
            'current_step': 0
        }
        
        try:
            for i, step in enumerate(workflow['steps']):
                execution_result['current_step'] = i + 1
                step_result = self.execute_step(step, execution_result['data'], workflow['rules'])
                execution_result['step_results'].append(step_result)
                
                if not step_result['success']:
                    execution_result['status'] = 'Failed'
                    execution_result['error_message'] = step_result.get('error_message', 'Step execution failed')
                    break
                
                # Update workflow data with step output
                if 'output_data' in step_result and step_result['output_data']:
                    execution_result['data'].update(step_result['output_data'])
            
            if execution_result['status'] == 'Running':
                execution_result['status'] = 'Completed'
                
        except Exception as e:
            execution_result['status'] = 'Error'
            execution_result['error_message'] = str(e)
        
        execution_result['end_time'] = datetime.utcnow().isoformat()
        self.workflow_executions.append(execution_result)
        
        return execution_result
    
    def execute_step(self, step, workflow_data, rules):
        step_result = {
            'step_name': step['name'],
            'step_type': step['type'],
            'start_time': datetime.utcnow().isoformat(),
            'success': False,
            'message': '',
            'output_data': {}
        }
        
        try:
            # Apply rules before step execution
            applicable_rules = [r for r in rules if r.get('step_name') == step['name']]
            for rule in applicable_rules:
                if not self.evaluate_rule(rule, workflow_data):
                    step_result['success'] = False
                    step_result['error_message'] = f"Rule validation failed: {rule.get('description', 'Unknown rule')}"
                    return step_result
            
            # Execute step based on type
            step_type = step['type'].lower()
            if step_type in self.step_handlers:
                result = self.step_handlers[step_type](step, workflow_data)
                step_result.update(result)
            else:
                step_result['success'] = True
                step_result['message'] = f"Executed custom step: {step['name']}"
                
        except Exception as e:
            step_result['success'] = False
            step_result['error_message'] = str(e)
        
        step_result['end_time'] = datetime.utcnow().isoformat()
        return step_result
    
    def execute_approval_step(self, step, workflow_data):
        # Simulate approval step
        approver = step.get('approver', 'system')
        approval_required = step.get('approval_required', True)
        
        return {
            'success': True,
            'message': f"Approval step executed by {approver}",
            'output_data': {'approval_status': 'pending'}
        }
    
    def execute_notification_step(self, step, workflow_data):
        # Simulate notification step
        recipients = step.get('recipients', [])
        message = step.get('message', '').format(**workflow_data)
        
        return {
            'success': True,
            'message': f"Notification sent to {len(recipients)} recipients",
            'output_data': {'notification_sent': True}
        }
    
    def execute_calculation_step(self, step, workflow_data):
        # Execute calculation
        formula = step.get('formula', '')
        result_field = step.get('result_field', 'calculation_result')
        
        try:
            # Simple calculation evaluation
            processed_formula = formula
            for key, value in workflow_data.items():
                processed_formula = processed_formula.replace(f'{{{key}}}', str(value))
            
            result = eval(processed_formula)
            
            return {
                'success': True,
                'message': f"Calculation completed: {formula} = {result}",
                'output_data': {result_field: result}
            }
        except Exception as e:
            return {
                'success': False,
                'error_message': f"Calculation error: {str(e)}"
            }
    
    def execute_condition_step(self, step, workflow_data):
        # Execute conditional logic
        condition = step.get('condition', '')
        
        try:
            result = self.evaluate_condition(condition, workflow_data)
            return {
                'success': True,
                'message': f"Condition evaluation: {condition} = {result}",
                'output_data': {'condition_result': result}
            }
        except Exception as e:
            return {
                'success': False,
                'error_message': f"Condition evaluation error: {str(e)}"
            }
    
    def execute_data_transform_step(self, step, workflow_data):
        # Transform data
        transformations = step.get('transformations', [])
        output_data = {}
        
        for transform in transformations:
            source_field = transform['source_field']
            target_field = transform['target_field']
            operation = transform.get('operation', 'copy')
            
            if source_field in workflow_data:
                if operation == 'copy':
                    output_data[target_field] = workflow_data[source_field]
                elif operation == 'uppercase':
                    output_data[target_field] = str(workflow_data[source_field]).upper()
                elif operation == 'lowercase':
                    output_data[target_field] = str(workflow_data[source_field]).lower()
        
        return {
            'success': True,
            'message': f"Data transformation completed for {len(transformations)} fields",
            'output_data': output_data
        }
    
    def evaluate_rule(self, rule, data):
        rule_type = rule.get('type', 'condition')
        expression = rule.get('expression', '')
        
        if rule_type == 'condition':
            return self.evaluate_condition(expression, data)
        elif rule_type == 'validation':
            return self.validate_data(expression, data)
        
        return True
    
    def evaluate_condition(self, condition, data):
        # Simple condition evaluation
        processed_condition = condition
        for key, value in data.items():
            processed_condition = processed_condition.replace(f'{{{key}}}', str(value))
        
        try:
            return bool(eval(processed_condition))
        except:
            return False
    
    def validate_data(self, validation_rule, data):
        # Simple data validation
        return True  # Placeholder for validation logic

@app.route('/create-workflow', methods=['POST'])
def create_workflow():
    data = request.json
    engine = WorkflowEngine()
    
    try:
        workflow_id = engine.create_workflow(
            data['name'],
            data['description'],
            data['steps'],
            data['rules'],
            data['user_id']
        )
        return jsonify({'workflow_id': workflow_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/execute-workflow/<int:workflow_id>', methods=['POST'])
def execute_workflow(workflow_id):
    data = request.json
    engine = WorkflowEngine()
    
    try:
        result = engine.execute_workflow(workflow_id, data['input_data'])
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
```

----

### 🧪 Senaryo 10: Bir iş akışı motoru kullanıcıların özel iş akışı kuralları tanımlamasına olanak verir. Kurallar iş süreçleri sırasında uygulanır. Kullanıcılar iş mantığını özelleştirebilir. İş akışı adımları kullanıcı tanımlı kurallara göre çalışır.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
interface Workflow {
  id: string;
  name: string;
  description: string;
  steps: WorkflowStep[];
  rules: WorkflowRule[];
  createdBy: string;
  createdDate: Date;
}

interface WorkflowStep {
  id: string;
  name: string;
  type: 'approval' | 'notification' | 'calculation' | 'condition' | 'data_transform';
  config: Record<string, any>;
  nextStepId?: string;
}

interface WorkflowRule {
  id: string;
  stepName: string;
  type: 'condition' | 'validation';
  expression: string;
  description: string;
}

interface WorkflowExecution {
  workflowId: string;
  workflowName: string;
  status: 'Running' | 'Completed' | 'Failed' | 'Error';
  startTime: Date;
  endTime?: Date;
  stepResults: StepExecutionResult[];
  data: Record<string, any>;
  currentStep: number;
  errorMessage?: string;
}

interface StepExecutionResult {
  stepName: string;
  stepType: string;
  success: boolean;
  startTime: Date;
  endTime?: Date;
  message: string;
  outputData?: Record<string, any>;
  errorMessage?: string;
}

class WorkflowEngine {
  private workflows: Map<string, Workflow> = new Map();
  private workflowExecutions: WorkflowExecution[] = [];

  createWorkflow(
    name: string,
    description: string,
    steps: WorkflowStep[],
    rules: WorkflowRule[],
    userId: string
  ): string {
    const workflowId = Date.now().toString();
    
    const workflow: Workflow = {
      id: workflowId,
      name,
      description,
      steps,
      rules,
      createdBy: userId,
      createdDate: new Date()
    };

    this.workflows.set(workflowId, workflow);
    return workflowId;
  }

  async executeWorkflow(workflowId: string, inputData: Record<string, any>): Promise<WorkflowExecution> {
    const workflow = this.workflows.get(workflowId);
    if (!workflow) {
      throw new Error('Workflow not found');
    }

    const execution: WorkflowExecution = {
      workflowId,
      workflowName: workflow.name,
      status: 'Running',
      startTime: new Date(),
      stepResults: [],
      data: { ...inputData },
      currentStep: 0
    };

    try {
      for (let i = 0; i < workflow.steps.length; i++) {
        const step = workflow.steps[i];
        execution.currentStep = i + 1;
        
        const stepResult = await this.executeStep(step, execution.data, workflow.rules);
        execution.stepResults.push(stepResult);

        if (!stepResult.success) {
          execution.status = 'Failed';
          execution.errorMessage = stepResult.errorMessage || 'Step execution failed';
          break;
        }

        // Update workflow data with step output
        if (stepResult.outputData) {
          Object.assign(execution.data, stepResult.outputData);
        }
      }

      if (execution.status === 'Running') {
        execution.status = 'Completed';
      }
    } catch (error) {
      execution.status = 'Error';
      execution.errorMessage = error.message;
    }

    execution.endTime = new Date();
    this.workflowExecutions.push(execution);
    
    return execution;
  }

  private async executeStep(
    step: WorkflowStep,
    workflowData: Record<string, any>,
    rules: WorkflowRule[]
  ): Promise<StepExecutionResult> {
    const stepResult: StepExecutionResult = {
      stepName: step.name,
      stepType: step.type,
      success: false,
      startTime: new Date(),
      message: '',
      outputData: {}
    };

    try {
      // Apply rules before step execution
      const applicableRules = rules.filter(rule => rule.stepName === step.name);
      for (const rule of applicableRules) {
        if (!this.evaluateRule(rule, workflowData)) {
          stepResult.success = false;
          stepResult.errorMessage = `Rule validation failed: ${rule.description}`;
          return stepResult;
        }
      }

      // Execute step based on type
      switch (step.type) {
        case 'approval':
          Object.assign(stepResult, await this.executeApprovalStep(step, workflowData));
          break;
        case 'notification':
          Object.assign(stepResult, await this.executeNotificationStep(step, workflowData));
          break;
        case 'calculation':
          Object.assign(stepResult, await this.executeCalculationStep(step, workflowData));
          break;
        case 'condition':
          Object.assign(stepResult, await this.executeConditionStep(step, workflowData));
          break;
        case 'data_transform':
          Object.assign(stepResult, await this.executeDataTransformStep(step, workflowData));
          break;
        default:
          stepResult.success = true;
          stepResult.message = `Executed custom step: ${step.name}`;
      }
    } catch (error) {
      stepResult.success = false;
      stepResult.errorMessage = error.message;
    }

    stepResult.endTime = new Date();
    return stepResult;
  }

  private async executeApprovalStep(step: WorkflowStep, workflowData: Record<string, any>) {
    const approver = step.config.approver || 'system';
    
    return {
      success: true,
      message: `Approval step executed by ${approver}`,
      outputData: { approval_status: 'pending' }
    };
  }

  private async executeNotificationStep(step: WorkflowStep, workflowData: Record<string, any>) {
    const recipients = step.config.recipients || [];
    const message = this.processTemplate(step.config.message || '', workflowData);
    
    return {
      success: true,
      message: `Notification sent to ${recipients.length} recipients`,
      outputData: { notification_sent: true }
    };
  }

  private async executeCalculationStep(step: WorkflowStep, workflowData: Record<string, any>) {
    const formula = step.config.formula || '';
    const resultField = step.config.resultField || 'calculation_result';
    
    try {
      const result = this.evaluateFormula(formula, workflowData);
      
      return {
        success: true,
        message: `Calculation completed: ${formula} = ${result}`,
        outputData: { [resultField]: result }
      };
    } catch (error) {
      return {
        success: false,
        errorMessage: `Calculation error: ${error.message}`
      };
    }
  }

  private async executeConditionStep(step: WorkflowStep, workflowData: Record<string, any>) {
    const condition = step.config.condition || '';
    
    try {
      const result = this.evaluateCondition(condition, workflowData);
      
      return {
        success: true,
        message: `Condition evaluation: ${condition} = ${result}`,
        outputData: { condition_result: result }
      };
    } catch (error) {
      return {
        success: false,
        errorMessage: `Condition evaluation error: ${error.message}`
      };
    }
  }

  private async executeDataTransformStep(step: WorkflowStep, workflowData: Record<string, any>) {
    const transformations = step.config.transformations || [];
    const outputData: Record<string, any> = {};
    
    transformations.forEach((transform: any) => {
      const { sourceField, targetField, operation = 'copy' } = transform;
      
      if (workflowData[sourceField] !== undefined) {
        switch (operation) {
          case 'copy':
            outputData[targetField] = workflowData[sourceField];
            break;
          case 'uppercase':
            outputData[targetField] = String(workflowData[sourceField]).toUpperCase();
            break;
          case 'lowercase':
            outputData[targetField] = String(workflowData[sourceField]).toLowerCase();
            break;
        }
      }
    });
    
    return {
      success: true,
      message: `Data transformation completed for ${transformations.length} fields`,
      outputData
    };
  }

  private evaluateRule(rule: WorkflowRule, data: Record<string, any>): boolean {
    switch (rule.type) {
      case 'condition':
        return this.evaluateCondition(rule.expression, data);
      case 'validation':
        return this.validateData(rule.expression, data);
      default:
        return true;
    }
  }

  private evaluateCondition(condition: string, data: Record<string, any>): boolean {
    let processedCondition = condition;
    
    Object.entries(data).forEach(([key, value]) => {
      processedCondition = processedCondition.replace(
        new RegExp(`\\{${key}\\}`, 'g'),
        String(value)
      );
    });

    try {
      return Boolean(Function(`"use strict"; return (${processedCondition})`)());
    } catch {
      return false;
    }
  }

  private evaluateFormula(formula: string, data: Record<string, any>): number {
    let processedFormula = formula;
    
    Object.entries(data).forEach(([key, value]) => {
      processedFormula = processedFormula.replace(
        new RegExp(`\\{${key}\\}`, 'g'),
        String(value)
      );
    });

    try {
      const result = Function(`"use strict"; return (${processedFormula})`)();
      return Number(result);
    } catch (error) {
      throw new Error(`Formula evaluation failed: ${error.message}`);
    }
  }

  private validateData(validationRule: string, data: Record<string, any>): boolean {
    // Placeholder for validation logic
    return true;
  }

  private processTemplate(template: string, data: Record<string, any>): string {
    let processed = template;
    
    Object.entries(data).forEach(([key, value]) => {
      processed = processed.replace(
        new RegExp(`\\{${key}\\}`, 'g'),
        String(value)
      );
    });

    return processed;
  }

  getWorkflow(workflowId: string): Workflow | undefined {
    return this.workflows.get(workflowId);
  }

  getWorkflowExecutions(): WorkflowExecution[] {
    return [...this.workflowExecutions];
  }
}
```

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    formula_engine = FormulaEngine()
    
    formula = formula_engine.formulas.get(data['formula_id'])
    if not formula:
        return jsonify({'error': 'Formula not found'}), 404
    
    try:
        result = formula_engine.evaluate_formula(formula['expression'], data['variables'])
        return jsonify({'result': result, 'formula': formula['expression']})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
```

----

### 🧪 Senaryo 2: Bir rapor oluşturma aracında kullanıcılar özel formüller yazabilir. Formül motoru bu ifadeleri değerlendirerek sonuçları hesaplar. Kullanıcılar matematiksel ve mantıksal işlemler tanımlayabilir. Hesaplanan sonuçlar raporda gösterilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
interface Formula {
  id: string;
  name: string;
  expression: string;
  description: string;
  createdBy: string;
  createdDate: Date;
}

interface CalculationResult {
  result: number;
  formula: string;
  variables: Record<string, number>;
  calculatedAt: Date;
}

class FormulaEngine {
  private formulas: Map<string, Formula> = new Map();
  private calculations: CalculationResult[] = [];

  private safeFunctions = {
    sin: Math.sin,
    cos: Math.cos,
    tan: Math.tan,
    sqrt: Math.sqrt,
    log: Math.log,
    abs: Math.abs,
    min: Math.min,
    max: Math.max,
    pow: Math.pow
  };

  validateFormula(expression: string): boolean {
    const allowedPattern = /^[a-zA-Z0-9+\-*/().,<>=!\s]+$/;
    return allowedPattern.test(expression);
  }

  evaluateFormula(expression: string, variables: Record<string, number>): number {
    if (!this.validateFormula(expression)) {
      throw new Error('Invalid formula syntax');
    }

    let processedExpression = expression;
    
    // Replace variables with their values
    Object.entries(variables).forEach(([variable, value]) => {
      const regex = new RegExp(variable, 'g');
      processedExpression = processedExpression.replace(regex, value.toString());
    });

    try {
      // Simple evaluation using Function constructor (safer than eval)
      const result = new Function('Math', `return ${processedExpression}`)(Math);
      return Number(result);
    } catch (error) {
      throw new Error(`Formula evaluation error: ${error.message}`);
    }
  }

  createFormula(name: string, expression: string, description: string, userId: string): string {
    const formulaId = Date.now().toString();
    
    if (!this.validateFormula(expression)) {
      throw new Error('Invalid formula syntax');
    }

    const formula: Formula = {
      id: formulaId,
      name,
      expression,
      description,
      createdBy: userId,
      createdDate: new Date()
    };

    this.formulas.set(formulaId, formula);
    return formulaId;
  }

  calculate(formulaId: string, variables: Record<string, number>): CalculationResult {
    const formula = this.formulas.get(formulaId);
    if (!formula) {
      throw new Error('Formula not found');
    }

    const result = this.evaluateFormula(formula.expression, variables);
    
    const calculation: CalculationResult = {
      result,
      formula: formula.expression,
      variables,
      calculatedAt: new Date()
    };

    this.calculations.push(calculation);
    return calculation;
  }
}
```

----

### 🧪 Senaryo 3: Bir web sayfası oluşturucu kullanıcıların HTML içerik girmesine izin verir. Kullanıcılar kendi tasarımlarını oluşturabilir ve düzenleyebilir. Girilen içerik sistem tarafından işlenir ve web sayfası olarak sunulur. Sayfa öğeleri kullanıcı tarafından özelleştirilebilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("create-page")]
public IActionResult CreatePage([FromBody] PageRequest request)
{
    try
    {
        var sanitizer = new HtmlSanitizer();
        var sanitizedContent = sanitizer.Sanitize(request.HtmlContent);

        var page = new WebPage
        {
            Title = request.Title,
            HtmlContent = sanitizedContent,
            CssStyles = request.CssStyles,
            CreatedBy = request.UserId,
            IsPublished = false,
            CreatedDate = DateTime.UtcNow
        };

        _context.WebPages.Add(page);
        _context.SaveChanges();

        return Ok(new { PageId = page.Id, Status = "Created" });
    }
    catch (Exception ex)
    {
        return BadRequest(new { Error = ex.Message });
    }
}

[HttpGet("render/{pageId}")]
public IActionResult RenderPage(int pageId)
{
    var page = _context.WebPages.Find(pageId);
    if (page == null) return NotFound();

    var htmlBuilder = new StringBuilder();
    htmlBuilder.AppendLine("<!DOCTYPE html>");
    htmlBuilder.AppendLine("<html>");
    htmlBuilder.AppendLine("<head>");
    htmlBuilder.AppendLine($"<title>{page.Title}</title>");
    htmlBuilder.AppendLine($"<style>{page.CssStyles}</style>");
    htmlBuilder.AppendLine("</head>");
    htmlBuilder.AppendLine("<body>");
    htmlBuilder.AppendLine(page.HtmlContent);
    htmlBuilder.AppendLine("</body>");
    htmlBuilder.AppendLine("</html>");

    return Content(htmlBuilder.ToString(), "text/html");
}

[HttpPut("update-page/{pageId}")]
public IActionResult UpdatePage(int pageId, [FromBody] PageUpdateRequest request)
{
    var page = _context.WebPages.Find(pageId);
    if (page == null) return NotFound();

    var sanitizer = new HtmlSanitizer();
    page.HtmlContent = sanitizer.Sanitize(request.HtmlContent);
    page.CssStyles = request.CssStyles;
    page.UpdatedDate = DateTime.UtcNow;

    _context.SaveChanges();
    return Ok(new { Status = "Updated" });
}
```

----

### 🧪 Senaryo 3: Bir web sayfası oluşturucu kullanıcıların HTML içerik girmesine izin verir. Kullanıcılar kendi tasarımlarını oluşturabilir ve düzenleyebilir. Girilen içerik sistem tarafından işlenir ve web sayfası olarak sunulur. Sayfa öğeleri kullanıcı tarafından özelleştirilebilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
from flask import Flask, request, jsonify, render_template_string
import bleach
from datetime import datetime

class HTMLSanitizer:
    def __init__(self):
        self.allowed_tags = ['div', 'p', 'h1', 'h2', 'h3', 'span', 'img', 'a', 'ul', 'li', 'br']
        self.allowed_attributes = {
            'img': ['src', 'alt', 'width', 'height'],
            'a': ['href', 'title'],
            '*': ['class', 'id', 'style']
        }
    
    def sanitize(self, html_content):
        return bleach.clean(html_content, tags=self.allowed_tags, attributes=self.allowed_attributes)

class PageBuilder:
    def __init__(self):
        self.pages = {}
        self.sanitizer = HTMLSanitizer()
    
    def create_page(self, title, html_content, css_styles, user_id):
        page_id = len(self.pages) + 1
        sanitized_content = self.sanitizer.sanitize(html_content)
        
        page = {
            'id': page_id,
            'title': title,
            'html_content': sanitized_content,
            'css_styles': css_styles,
            'created_by': user_id,
            'is_published': False,
            'created_date': datetime.utcnow().isoformat()
        }
        
        self.pages[page_id] = page
        return page_id
    
    def render_page(self, page_id):
        page = self.pages.get(page_id)
        if not page:
            return None
        
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{page['title']}</title>
            <style>{page['css_styles']}</style>
        </head>
        <body>
            {page['html_content']}
        </body>
        </html>
        """
        return html_template

@app.route('/create-page', methods=['POST'])
def create_page():
    data = request.json
    page_builder = PageBuilder()
    
    try:
        page_id = page_builder.create_page(
            data['title'],
            data['html_content'],
            data.get('css_styles', ''),
            data['user_id']
        )
        return jsonify({'page_id': page_id, 'status': 'created'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/render/<int:page_id>')
def render_page(page_id):
    page_builder = PageBuilder()
    html_content = page_builder.render_page(page_id)
    
    if not html_content:
        return jsonify({'error': 'Page not found'}), 404
    
    return html_content
```

----

### 🧪 Senaryo 3: Bir web sayfası oluşturucu kullanıcıların HTML içerik girmesine izin verir. Kullanıcılar kendi tasarımlarını oluşturabilir ve düzenleyebilir. Girilen içerik sistem tarafından işlenir ve web sayfası olarak sunulur. Sayfa öğeleri kullanıcı tarafından özelleştirilebilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
interface WebPage {
  id: string;
  title: string;
  htmlContent: string;
  cssStyles: string;
  createdBy: string;
  isPublished: boolean;
  createdDate: Date;
}

class HTMLSanitizer {
  private allowedTags = ['div', 'p', 'h1', 'h2', 'h3', 'span', 'img', 'a', 'ul', 'li', 'br'];
  private allowedAttributes = ['class', 'id', 'src', 'href', 'alt', 'title'];

  sanitize(htmlContent: string): string {
    // Simple sanitization - remove script tags and dangerous attributes
    let sanitized = htmlContent.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
    sanitized = sanitized.replace(/on\w+="[^"]*"/gi, '');
    sanitized = sanitized.replace(/javascript:/gi, '');
    return sanitized;
  }
}

class PageBuilder {
  private pages: Map<string, WebPage> = new Map();
  private sanitizer = new HTMLSanitizer();

  createPage(title: string, htmlContent: string, cssStyles: string, userId: string): string {
    const pageId = Date.now().toString();
    const sanitizedContent = this.sanitizer.sanitize(htmlContent);

    const page: WebPage = {
      id: pageId,
      title,
      htmlContent: sanitizedContent,
      cssStyles,
      createdBy: userId,
      isPublished: false,
      createdDate: new Date()
    };

    this.pages.set(pageId, page);
    return pageId;
  }

  updatePage(pageId: string, htmlContent: string, cssStyles: string): boolean {
    const page = this.pages.get(pageId);
    if (!page) return false;

    page.htmlContent = this.sanitizer.sanitize(htmlContent);
    page.cssStyles = cssStyles;
    return true;
  }

  renderPage(pageId: string): string | null {
    const page = this.pages.get(pageId);
    if (!page) return null;

    return `
      <!DOCTYPE html>
      <html>
      <head>
        <title>${page.title}</title>
        <style>${page.cssStyles}</style>
      </head>
      <body>
        ${page.htmlContent}
      </body>
      </html>
    `;
  }

  publishPage(pageId: string): boolean {
    const page = this.pages.get(pageId);
    if (!page) return false;

    page.isPublished = true;
    return true;
  }

  getPage(pageId: string): WebPage | undefined {
    return this.pages.get(pageId);
  }
}
```

----

### 🧪 Senaryo 4: Bir konfigürasyon yönetim sistemi kullanıcıların özel ayarlar tanımlamasına olanak sağlar. Ayar dosyaları sistem tarafından okunup uygulanır. Kullanıcılar sistemi ihtiyaçlarına göre yapılandırabilir. Yapılandırma değişiklikleri dinamik olarak yüklenir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("save-config")]
public IActionResult SaveConfiguration([FromBody] ConfigRequest request)
{
    try
    {
        var validator = new ConfigValidator();
        if (!validator.ValidateConfig(request.Settings))
            return BadRequest(new { Error = "Invalid configuration format" });

        var config = new Configuration
        {
            Name = request.Name,
            Settings = JsonSerializer.Serialize(request.Settings),
            Environment = request.Environment,
            CreatedBy = request.UserId,
            IsActive = false,
            CreatedDate = DateTime.UtcNow
        };

        _context.Configurations.Add(config);
        _context.SaveChanges();

        return Ok(new { ConfigId = config.Id });
    }
    catch (Exception ex)
    {
        return BadRequest(new { Error = ex.Message });
    }
}

[HttpPost("apply-config/{configId}")]
public IActionResult ApplyConfiguration(int configId)
{
    var config = _context.Configurations.Find(configId);
    if (config == null) return NotFound();

    try
    {
        var settings = JsonSerializer.Deserialize<Dictionary<string, object>>(config.Settings);
        _configManager.ApplySettings(settings);

        config.IsActive = true;
        config.AppliedDate = DateTime.UtcNow;
        _context.SaveChanges();

        return Ok(new { Status = "Configuration applied successfully" });
    }
    catch (Exception ex)
    {
        return BadRequest(new { Error = $"Failed to apply configuration: {ex.Message}" });
    }
}

public class ConfigManager
{
    private Dictionary<string, object> _currentSettings = new();

    public void ApplySettings(Dictionary<string, object> settings)
    {
        foreach (var setting in settings)
        {
            _currentSettings[setting.Key] = setting.Value;
            ApplySettingToSystem(setting.Key, setting.Value);
        }
    }

    private void ApplySettingToSystem(string key, object value)
    {
        // Apply configuration changes to system components
        switch (key.ToLower())
        {
            case "database_timeout":
                ConfigureDatabase("ConnectionTimeout", value);
                break;
            case "cache_size":
                ConfigureCache("MaxSize", value);
                break;
        }
    }
}
```

----

### 🧪 Senaryo 4: Bir konfigürasyon yönetim sistemi kullanıcıların özel ayarlar tanımlamasına olanak sağlar. Ayar dosyaları sistem tarafından okunup uygulanır. Kullanıcılar sistemi ihtiyaçlarına göre yapılandırabilir. Yapılandırma değişiklikleri dinamik olarak yüklenir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import json
import os
from datetime import datetime

class ConfigManager:
    def __init__(self):
        self.configurations = {}
        self.active_config = {}
        self.config_validators = {
            'database_timeout': lambda x: isinstance(x, int) and x > 0,
            'cache_size': lambda x: isinstance(x, int) and x > 0,
            'debug_mode': lambda x: isinstance(x, bool),
            'max_connections': lambda x: isinstance(x, int) and 1 <= x <= 1000
        }
    
    def validate_config(self, settings):
        for key, value in settings.items():
            if key in self.config_validators:
                if not self.config_validators[key](value):
                    return False, f"Invalid value for {key}: {value}"
        return True, "Valid"
    
    def save_configuration(self, name, settings, environment, user_id):
        is_valid, message = self.validate_config(settings)
        if not is_valid:
            raise ValueError(message)
        
        config_id = len(self.configurations) + 1
        config = {
            'id': config_id,
            'name': name,
            'settings': settings,
            'environment': environment,
            'created_by': user_id,
            'is_active': False,
            'created_date': datetime.utcnow().isoformat()
        }
        
        self.configurations[config_id] = config
        return config_id
    
    def apply_configuration(self, config_id):
        config = self.configurations.get(config_id)
        if not config:
            raise ValueError("Configuration not found")
        
        # Apply settings to system
        for key, value in config['settings'].items():
            self.active_config[key] = value
            self.apply_setting_to_system(key, value)
        
        config['is_active'] = True
        config['applied_date'] = datetime.utcnow().isoformat()
        return True
    
    def apply_setting_to_system(self, key, value):
        # Simulate applying settings to different system components
        if key == 'database_timeout':
            print(f"Applied database timeout: {value} seconds")
        elif key == 'cache_size':
            print(f"Applied cache size: {value} MB")
        elif key == 'debug_mode':
            print(f"Debug mode: {'enabled' if value else 'disabled'}")

@app.route('/save-config', methods=['POST'])
def save_configuration():
    data = request.json
    config_manager = ConfigManager()
    
    try:
        config_id = config_manager.save_configuration(
            data['name'],
            data['settings'],
            data['environment'],
            data['user_id']
        )
        return jsonify({'config_id': config_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/apply-config/<int:config_id>', methods=['POST'])
def apply_configuration(config_id):
    config_manager = ConfigManager()
    
    try:
        config_manager.apply_configuration(config_id)
        return jsonify({'status': 'Configuration applied successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
```

----

### 🧪 Senaryo 4: Bir konfigürasyon yönetim sistemi kullanıcıların özel ayarlar tanımlamasına olanak sağlar. Ayar dosyaları sistem tarafından okunup uygulanır. Kullanıcılar sistemi ihtiyaçlarına göre yapılandırabilir. Yapılandırma değişiklikleri dinamik olarak yüklenir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
interface Configuration {
  id: string;
  name: string;
  settings: Record<string, any>;
  environment: string;
  createdBy: string;
  isActive: boolean;
  createdDate: Date;
  appliedDate?: Date;
}

type ConfigValidator = (value: any) => boolean;

class ConfigManager {
  private configurations: Map<string, Configuration> = new Map();
  private activeConfig: Record<string, any> = {};
  
  private validators: Record<string, ConfigValidator> = {
    'database_timeout': (value) => typeof value === 'number' && value > 0,
    'cache_size': (value) => typeof value === 'number' && value > 0,
    'debug_mode': (value) => typeof value === 'boolean',
    'max_connections': (value) => typeof value === 'number' && value >= 1 && value <= 1000,
    'api_rate_limit': (value) => typeof value === 'number' && value > 0
  };

  validateSettings(settings: Record<string, any>): { isValid: boolean; error?: string } {
    for (const [key, value] of Object.entries(settings)) {
      if (this.validators[key] && !this.validators[key](value)) {
        return { isValid: false, error: `Invalid value for ${key}: ${value}` };
      }
    }
    return { isValid: true };
  }

  saveConfiguration(name: string, settings: Record<string, any>, environment: string, userId: string): string {
    const validation = this.validateSettings(settings);
    if (!validation.isValid) {
      throw new Error(validation.error);
    }

    const configId = Date.now().toString();
    const config: Configuration = {
      id: configId,
      name,
      settings,
      environment,
      createdBy: userId,
      isActive: false,
      createdDate: new Date()
    };

    this.configurations.set(configId, config);
    return configId;
  }

  applyConfiguration(configId: string): boolean {
    const config = this.configurations.get(configId);
    if (!config) {
      throw new Error('Configuration not found');
    }

    // Apply settings to system
    Object.entries(config.settings).forEach(([key, value]) => {
      this.activeConfig[key] = value;
      this.applySettingToSystem(key, value);
    });

    config.isActive = true;
    config.appliedDate = new Date();
    return true;
  }

  private applySettingToSystem(key: string, value: any): void {
    switch (key) {
      case 'database_timeout':
        console.log(`Applied database timeout: ${value} seconds`);
        break;
      case 'cache_size':
        console.log(`Applied cache size: ${value} MB`);
        break;
      case 'debug_mode':
        console.log(`Debug mode: ${value ? 'enabled' : 'disabled'}`);
        break;
      case 'max_connections':
        console.log(`Max connections: ${value}`);
        break;
    }
  }

  getActiveConfig(): Record<string, any> {
    return { ...this.activeConfig };
  }

  getConfiguration(configId: string): Configuration | undefined {
    return this.configurations.get(configId);
  }
}
```

----

### 🧪 Senaryo 5: Bir makro editörü kullanıcıların özel komutlar yazmasına izin verir. Makrolar sistem tarafından yorumlanıp çalıştırılır. Kullanıcılar tekrarlayan işlemler için makrolar oluşturabilir. Makro komutları sistem tarafından işlenir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("create-macro")]
public IActionResult CreateMacro([FromBody] MacroRequest request)
{
    try
    {
        var parser = new MacroParser();
        var commands = parser.ParseCommands(request.Script);

        var macro = new Macro
        {
            Name = request.Name,
            Description = request.Description,
            Script = request.Script,
            Commands = JsonSerializer.Serialize(commands),
            CreatedBy = request.UserId,
            CreatedDate = DateTime.UtcNow
        };

        _context.Macros.Add(macro);
        _context.SaveChanges();

        return Ok(new { MacroId = macro.Id });
    }
    catch (Exception ex)
    {
        return BadRequest(new { Error = ex.Message });
    }
}

[HttpPost("execute-macro/{macroId}")]
public IActionResult ExecuteMacro(int macroId, [FromBody] ExecutionContext context)
{
    var macro = _context.Macros.Find(macroId);
    if (macro == null) return NotFound();

    try
    {
        var executor = new MacroExecutor();
        var result = executor.Execute(macro.Script, context.Variables);

        _context.MacroExecutions.Add(new MacroExecution
        {
            MacroId = macroId,
            ExecutedBy = context.UserId,
            Result = JsonSerializer.Serialize(result),
            ExecutedAt = DateTime.UtcNow
        });
        _context.SaveChanges();

        return Ok(new { Result = result });
    }
    catch (Exception ex)
    {
        return BadRequest(new { Error = ex.Message });
    }
}

public class MacroExecutor
{
    public object Execute(string script, Dictionary<string, object> variables)
    {
        var lines = script.Split('\n');
        var result = new List<string>();

        foreach (var line in lines)
        {
            var trimmedLine = line.Trim();
            if (string.IsNullOrEmpty(trimmedLine) || trimmedLine.StartsWith("//"))
                continue;

            var commandResult = ExecuteCommand(trimmedLine, variables);
            result.Add(commandResult);
        }

        return result;
    }

    private string ExecuteCommand(string command, Dictionary<string, object> variables)
    {
        if (command.StartsWith("PRINT"))
        {
            var message = command.Substring(5).Trim().Trim('"');
            return ReplaceVariables(message, variables);
        }
        else if (command.StartsWith("SET"))
        {
            var parts = command.Substring(3).Split('=');
            var varName = parts[0].Trim();
            var varValue = parts[1].Trim().Trim('"');
            variables[varName] = varValue;
            return $"Variable {varName} set to {varValue}";
        }

        return $"Unknown command: {command}";
    }

    private string ReplaceVariables(string text, Dictionary<string, object> variables)
    {
        foreach (var variable in variables)
        {
            text = text.Replace($"{{{variable.Key}}}", variable.Value.ToString());
        }
        return text;
    }
}
```

----

### 🧪 Senaryo 5: Bir makro editörü kullanıcıların özel komutlar yazmasına izin verir. Makrolar sistem tarafından yorumlanıp çalıştırılır. Kullanıcılar tekrarlayan işlemler için makrolar oluşturabilir. Makro komutları sistem tarafından işlenir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import re
from datetime import datetime

class MacroExecutor:
    def __init__(self):
        self.macros = {}
        self.commands = {
            'PRINT': self.print_command,
            'SET': self.set_command,
            'IF': self.if_command,
            'LOOP': self.loop_command,
            'WAIT': self.wait_command
        }
    
    def parse_macro(self, script):
        lines = [line.strip() for line in script.split('\n') if line.strip() and not line.strip().startswith('//')]
        return lines
    
    def execute_macro(self, script, variables=None):
        if variables is None:
            variables = {}
        
        commands = self.parse_macro(script)
        results = []
        
        for command in commands:
            try:
                result = self.execute_command(command, variables)
                results.append(result)
            except Exception as e:
                results.append(f"Error executing {command}: {str(e)}")
        
        return results
    
    def execute_command(self, command, variables):
        parts = command.split(' ', 1)
        cmd_type = parts[0].upper()
        
        if cmd_type in self.commands:
            return self.commands[cmd_type](parts[1] if len(parts) > 1 else '', variables)
        else:
            return f"Unknown command: {cmd_type}"
    
    def print_command(self, args, variables):
        message = args.strip('"\'')
        message = self.replace_variables(message, variables)
        return f"OUTPUT: {message}"
    
    def set_command(self, args, variables):
        parts = args.split('=', 1)
        var_name = parts[0].strip()
        var_value = parts[1].strip().strip('"\'')
        variables[var_name] = var_value
        return f"Variable {var_name} set to {var_value}"
    
    def if_command(self, args, variables):
        # Simple IF condition parsing
        condition = args.strip()
        condition = self.replace_variables(condition, variables)
        return f"IF condition: {condition}"
    
    def loop_command(self, args, variables):
        parts = args.split(' ')
        count = int(parts[0]) if parts[0].isdigit() else 1
        return f"LOOP executed {count} times"
    
    def wait_command(self, args, variables):
        seconds = int(args) if args.isdigit() else 1
        return f"WAIT {seconds} seconds"
    
    def replace_variables(self, text, variables):
        for var_name, var_value in variables.items():
            text = text.replace(f'{{{var_name}}}', str(var_value))
        return text

@app.route('/create-macro', methods=['POST'])
def create_macro():
    data = request.json
    macro_executor = MacroExecutor()
    
    try:
        macro_id = len(macro_executor.macros) + 1
        macro_executor.macros[macro_id] = {
            'id': macro_id,
            'name': data['name'],
            'description': data['description'],
            'script': data['script'],
            'created_by': data['user_id'],
            'created_date': datetime.utcnow().isoformat()
        }
        
        return jsonify({'macro_id': macro_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/execute-macro/<int:macro_id>', methods=['POST'])
def execute_macro(macro_id):
    data = request.json
    macro_executor = MacroExecutor()
    
    macro = macro_executor.macros.get(macro_id)
    if not macro:
        return jsonify({'error': 'Macro not found'}), 404
    
    try:
        variables = data.get('variables', {})
        result = macro_executor.execute_macro(macro['script'], variables)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
```

----

### 🧪 Senaryo 5: Bir makro editörü kullanıcıların özel komutlar yazmasına izin verir. Makrolar sistem tarafından yorumlanıp çalıştırılır. Kullanıcılar tekrarlayan işlemler için makrolar oluşturabilir. Makro komutları sistem tarafından işlenir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
interface Macro {
  id: string;
  name: string;
  description: string;
  script: string;
  createdBy: string;
  createdDate: Date;
}

interface MacroCommand {
  type: string;
  args: string;
  lineNumber: number;
}

interface ExecutionResult {
  success: boolean;
  output: string[];
  variables: Record<string, any>;
  errors: string[];
}

class MacroExecutor {
  private macros: Map<string, Macro> = new Map();
  
  private commandHandlers = {
    'PRINT': this.printCommand.bind(this),
    'SET': this.setCommand.bind(this),
    'IF': this.ifCommand.bind(this),
    'LOOP': this.loopCommand.bind(this),
    'WAIT': this.waitCommand.bind(this)
  };

  parseMacro(script: string): MacroCommand[] {
    const lines = script.split('\n');
    const commands: MacroCommand[] = [];
    
    lines.forEach((line, index) => {
      const trimmed = line.trim();
      if (trimmed && !trimmed.startsWith('//')) {
        const parts = trimmed.split(' ');
        commands.push({
          type: parts[0].toUpperCase(),
          args: parts.slice(1).join(' '),
          lineNumber: index + 1
        });
      }
    });
    
    return commands;
  }

  async executeMacro(script: string, variables: Record<string, any> = {}): Promise<ExecutionResult> {
    const commands = this.parseMacro(script);
    const result: ExecutionResult = {
      success: true,
      output: [],
      variables: { ...variables },
      errors: []
    };

    for (const command of commands) {
      try {
        const handler = this.commandHandlers[command.type];
        if (handler) {
          const output = await handler(command.args, result.variables);
          result.output.push(output);
        } else {
          throw new Error(`Unknown command: ${command.type}`);
        }
      } catch (error) {
        result.errors.push(`Line ${command.lineNumber}: ${error.message}`);
        result.success = false;
      }
    }

    return result;
  }

  private printCommand(args: string, variables: Record<string, any>): string {
    const message = args.replace(/^["']|["']$/g, '');
    const processedMessage = this.replaceVariables(message, variables);
    return `OUTPUT: ${processedMessage}`;
  }

  private setCommand(args: string, variables: Record<string, any>): string {
    const [varName, ...valueParts] = args.split('=');
    const varValue = valueParts.join('=').trim().replace(/^["']|["']$/g, '');
    variables[varName.trim()] = varValue;
    return `Variable ${varName.trim()} set to ${varValue}`;
  }

  private ifCommand(args: string, variables: Record<string, any>): string {
    const condition = this.replaceVariables(args, variables);
    return `IF condition: ${condition}`;
  }

  private loopCommand(args: string, variables: Record<string, any>): string {
    const count = parseInt(args) || 1;
    return `LOOP executed ${count} times`;
  }

  private async waitCommand(args: string, variables: Record<string, any>): Promise<string> {
    const seconds = parseInt(args) || 1;
    await new Promise(resolve => setTimeout(resolve, seconds * 1000));
    return `WAIT ${seconds} seconds completed`;
  }

  private replaceVariables(text: string, variables: Record<string, any>): string {
    return text.replace(/\{(\w+)\}/g, (match, varName) => {
      return variables[varName] !== undefined ? String(variables[varName]) : match;
    });
  }

  createMacro(name: string, description: string, script: string, userId: string): string {
    const macroId = Date.now().toString();
    
    const macro: Macro = {
      id: macroId,
      name,
      description,
      script,
      createdBy: userId,
      createdDate: new Date()
    };

    this.macros.set(macroId, macro);
    return macroId;
  }

  getMacro(macroId: string): Macro | undefined {
    return this.macros.get(macroId);
  }
}
```

----

### 🧪 Senaryo 6: Bir veri dönüştürme aracı kullanıcıların özel dönüştürme kuralları tanımlamasını sağlar. Kurallar veri işleme sırasında uygulanır. Kullanıcılar farklı veri formatları arasında dönüştürme yapabilir. Dönüştürme mantığı kullanıcı tarafından belirlenir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("create-transform-rule")]
public IActionResult CreateTransformRule([FromBody] TransformRuleRequest request)
{
    try
    {
        var rule = new TransformRule
        {
            Name = request.Name,
            SourceFormat = request.SourceFormat,
            TargetFormat = request.TargetFormat,
            Rules = JsonSerializer.Serialize(request.Rules),
            CreatedBy = request.UserId,
            CreatedDate = DateTime.UtcNow
        };

        _context.TransformRules.Add(rule);
        _context.SaveChanges();

        return Ok(new { RuleId = rule.Id });
    }
    catch (Exception ex)
    {
        return BadRequest(new { Error = ex.Message });
    }
}

[HttpPost("transform-data")]
public IActionResult TransformData([FromBody] TransformRequest request)
{
    var rule = _context.TransformRules.Find(request.RuleId);
    if (rule == null) return NotFound();

    try
    {
        var transformer = new DataTransformer();
        var transformRules = JsonSerializer.Deserialize<List<TransformRule>>(rule.Rules);
        var result = transformer.Transform(request.SourceData, transformRules);

        return Ok(new { TransformedData = result });
    }
    catch (Exception ex)
    {
        return BadRequest(new { Error = ex.Message });
    }
}

public class DataTransformer
{
    public object Transform(object sourceData, List<TransformRule> rules)
    {
        var data = JObject.FromObject(sourceData);
        
        foreach (var rule in rules)
        {
            ApplyRule(data, rule);
        }
        
        return data.ToObject<object>();
    }

    private void ApplyRule(JObject data, TransformRule rule)
    {
        switch (rule.Operation)
        {
            case "rename":
                RenameField(data, rule.SourceField, rule.TargetField);
                break;
            case "format":
                FormatField(data, rule.SourceField, rule.Format);
                break;
            case "calculate":
                CalculateField(data, rule.TargetField, rule.Expression);
                break;
            case "filter":
                FilterData(data, rule.Condition);
                break;
        }
    }

    private void RenameField(JObject data, string sourceField, string targetField)
    {
        if (data[sourceField] != null)
        {
            data[targetField] = data[sourceField];
            data.Remove(sourceField);
        }
    }

    private void FormatField(JObject data, string field, string format)
    {
        if (data[field] != null)
        {
            var value = data[field].ToString();
            data[field] = string.Format(format, value);
        }
    }
}
```

----

### 🧪 Senaryo 6: Bir veri dönüştürme aracı kullanıcıların özel dönüştürme kuralları tanımlamasını sağlar. Kurallar veri işleme sırasında uygulanır. Kullanıcılar farklı veri formatları arasında dönüştürme yapabilir. Dönüştürme mantığı kullanıcı tarafından belirlenir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import json
import re
from datetime import datetime

class DataTransformer:
    def __init__(self):
        self.transform_rules = {}
        self.operations = {
            'rename': self.rename_field,
            'format': self.format_field,
            'calculate': self.calculate_field,
            'filter': self.filter_field,
            'convert': self.convert_field
        }
    
    def create_transform_rule(self, name, source_format, target_format, rules, user_id):
        rule_id = len(self.transform_rules) + 1
        self.transform_rules[rule_id] = {
            'id': rule_id,
            'name': name,
            'source_format': source_format,
            'target_format': target_format,
            'rules': rules,
            'created_by': user_id,
            'created_date': datetime.utcnow().isoformat()
        }
        return rule_id
    
    def transform_data(self, source_data, rule_id):
        rule = self.transform_rules.get(rule_id)
        if not rule:
            raise ValueError("Transform rule not found")
        
        # Make a copy of source data
        if isinstance(source_data, str):
            data = json.loads(source_data)
        else:
            data = json.loads(json.dumps(source_data))
        
        # Apply transformation rules
        for transform_rule in rule['rules']:
            self.apply_rule(data, transform_rule)
        
        return data
    
    def apply_rule(self, data, rule):
        operation = rule.get('operation')
        if operation in self.operations:
            self.operations[operation](data, rule)
    
    def rename_field(self, data, rule):
        source_field = rule['source_field']
        target_field = rule['target_field']
        
        if isinstance(data, dict) and source_field in data:
            data[target_field] = data.pop(source_field)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and source_field in item:
                    item[target_field] = item.pop(source_field)
    
    def format_field(self, data, rule):
        field = rule['field']
        format_pattern = rule['format']
        
        if isinstance(data, dict) and field in data:
            data[field] = format_pattern.format(data[field])
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and field in item:
                    item[field] = format_pattern.format(item[field])
    
    def calculate_field(self, data, rule):
        target_field = rule['target_field']
        expression = rule['expression']
        
        if isinstance(data, dict):
            data[target_field] = self.evaluate_expression(expression, data)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    item[target_field] = self.evaluate_expression(expression, item)
    
    def filter_field(self, data, rule):
        condition = rule['condition']
        if isinstance(data, list):
            return [item for item in data if self.evaluate_condition(condition, item)]
        return data
    
    def convert_field(self, data, rule):
        field = rule['field']
        target_type = rule['target_type']
        
        if isinstance(data, dict) and field in data:
            data[field] = self.convert_value(data[field], target_type)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and field in item:
                    item[field] = self.convert_value(item[field], target_type)
    
    def evaluate_expression(self, expression, context):
        # Simple expression evaluation (for demo purposes)
        for key, value in context.items():
            expression = expression.replace(f'{{{key}}}', str(value))
        try:
            return eval(expression)
        except:
            return None
    
    def evaluate_condition(self, condition, context):
        # Simple condition evaluation
        for key, value in context.items():
            condition = condition.replace(f'{{{key}}}', str(value))
        try:
            return eval(condition)
        except:
            return False
    
    def convert_value(self, value, target_type):
        try:
            if target_type == 'int':
                return int(value)
            elif target_type == 'float':
                return float(value)
            elif target_type == 'str':
                return str(value)
            elif target_type == 'bool':
                return bool(value)
        except:
            return value
        return value

@app.route('/create-transform-rule', methods=['POST'])
def create_transform_rule():
    data = request.json
    transformer = DataTransformer()
    
    try:
        rule_id = transformer.create_transform_rule(
            data['name'],
            data['source_format'],
            data['target_format'],
            data['rules'],
            data['user_id']
        )
        return jsonify({'rule_id': rule_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/transform-data', methods=['POST'])
def transform_data():
    data = request.json
    transformer = DataTransformer()
    
    try:
        result = transformer.transform_data(data['source_data'], data['rule_id'])
        return jsonify({'transformed_data': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
```

----

### 🧪 Senaryo 6: Bir veri dönüştürme aracı kullanıcıların özel dönüştürme kuralları tanımlamasını sağlar. Kurallar veri işleme sırasında uygulanır. Kullanıcılar farklı veri formatları arasında dönüştürme yapabilir. Dönüştürme mantığı kullanıcı tarafından belirlenir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
interface TransformRule {
  id: string;
  name: string;
  sourceFormat: string;
  targetFormat: string;
  rules: TransformOperation[];
  createdBy: string;
  createdDate: Date;
}

interface TransformOperation {
  operation: 'rename' | 'format' | 'calculate' | 'filter' | 'convert';
  sourceField?: string;
  targetField?: string;
  format?: string;
  expression?: string;
  condition?: string;
  targetType?: string;
}

class DataTransformer {
  private transformRules: Map<string, TransformRule> = new Map();

  createTransformRule(
    name: string,
    sourceFormat: string,
    targetFormat: string,
    rules: TransformOperation[],
    userId: string
  ): string {
    const ruleId = Date.now().toString();
    
    const transformRule: TransformRule = {
      id: ruleId,
      name,
      sourceFormat,
      targetFormat,
      rules,
      createdBy: userId,
      createdDate: new Date()
    };

    this.transformRules.set(ruleId, transformRule);
    return ruleId;
  }

  transformData(sourceData: any, ruleId: string): any {
    const rule = this.transformRules.get(ruleId);
    if (!rule) {
      throw new Error('Transform rule not found');
    }

    // Deep clone the source data
    let data = JSON.parse(JSON.stringify(sourceData));

    // Apply transformation rules
    rule.rules.forEach(transformRule => {
      data = this.applyOperation(data, transformRule);
    });

    return data;
  }

  private applyOperation(data: any, operation: TransformOperation): any {
    switch (operation.operation) {
      case 'rename':
        return this.renameField(data, operation);
      case 'format':
        return this.formatField(data, operation);
      case 'calculate':
        return this.calculateField(data, operation);
      case 'filter':
        return this.filterData(data, operation);
      case 'convert':
        return this.convertField(data, operation);
      default:
        return data;
    }
  }

  private renameField(data: any, operation: TransformOperation): any {
    if (Array.isArray(data)) {
      return data.map(item => this.renameField(item, operation));
    } else if (typeof data === 'object' && data !== null) {
      const { sourceField, targetField } = operation;
      if (sourceField && targetField && data.hasOwnProperty(sourceField)) {
        data[targetField] = data[sourceField];
        delete data[sourceField];
      }
    }
    return data;
  }

  private formatField(data: any, operation: TransformOperation): any {
    const { sourceField, format } = operation;
    
    if (Array.isArray(data)) {
      return data.map(item => this.formatField(item, operation));
    } else if (typeof data === 'object' && data !== null && sourceField) {
      if (data.hasOwnProperty(sourceField) && format) {
        data[sourceField] = format.replace('{value}', data[sourceField]);
      }
    }
    return data;
  }

  private calculateField(data: any, operation: TransformOperation): any {
    const { targetField, expression } = operation;
    
    if (Array.isArray(data)) {
      return data.map(item => this.calculateField(item, operation));
    } else if (typeof data === 'object' && data !== null && targetField && expression) {
      try {
        const result = this.evaluateExpression(expression, data);
        data[targetField] = result;
      } catch (error) {
        console.warn(`Failed to calculate field ${targetField}:`, error);
      }
    }
    return data;
  }

  private filterData(data: any, operation: TransformOperation): any {
    if (Array.isArray(data) && operation.condition) {
      return data.filter(item => this.evaluateCondition(operation.condition!, item));
    }
    return data;
  }

  private convertField(data: any, operation: TransformOperation): any {
    const { sourceField, targetType } = operation;
    
    if (Array.isArray(data)) {
      return data.map(item => this.convertField(item, operation));
    } else if (typeof data === 'object' && data !== null && sourceField && targetType) {
      if (data.hasOwnProperty(sourceField)) {
        data[sourceField] = this.convertValue(data[sourceField], targetType);
      }
    }
    return data;
  }

  private evaluateExpression(expression: string, context: any): any {
    let processedExpression = expression;
    
    Object.keys(context).forEach(key => {
      processedExpression = processedExpression.replace(
        new RegExp(`\\{${key}\\}`, 'g'),
        context[key]
      );
    });

    try {
      return Function('"use strict"; return (' + processedExpression + ')')();
    } catch (error) {
      return null;
    }
  }

  private evaluateCondition(condition: string, context: any): boolean {
    const result = this.evaluateExpression(condition, context);
    return Boolean(result);
  }

  private convertValue(value: any, targetType: string): any {
    try {
      switch (targetType) {
        case 'string':
          return String(value);
        case 'number':
          return Number(value);
        case 'boolean':
          return Boolean(value);
        case 'date':
          return new Date(value);
        default:
          return value;
      }
    } catch (error) {
      return value;
    }
  }
}
```

----

### 🧪 Senaryo 7: Bir otomatik test aracı kullanıcıların test senaryoları yazmasına olanak tanır. Test senaryoları sistem tarafından çalıştırılarak sonuçlar alınır. Kullanıcılar özel test durumları tanımlayabilir. Test mantığı kullanıcı girişlerine göre şekillenir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("create-test-scenario")]
public IActionResult CreateTestScenario([FromBody] TestScenarioRequest request)
{
    try
    {
        var scenario = new TestScenario
        {
            Name = request.Name,
            Description = request.Description,
            TestSteps = JsonSerializer.Serialize(request.TestSteps),
            ExpectedResults = JsonSerializer.Serialize(request.ExpectedResults),
            CreatedBy = request.UserId,
            CreatedDate = DateTime.UtcNow
        };

        _context.TestScenarios.Add(scenario);
        _context.SaveChanges();

        return Ok(new { ScenarioId = scenario.Id });
    }
    catch (Exception ex)
    {
        return BadRequest(new { Error = ex.Message });
    }
}

[HttpPost("execute-test/{scenarioId}")]
public IActionResult ExecuteTest(int scenarioId)
{
    var scenario = _context.TestScenarios.Find(scenarioId);
    if (scenario == null) return NotFound();

    try
    {
        var executor = new TestExecutor();
        var result = executor.ExecuteScenario(scenario);

        _context.TestExecutions.Add(new TestExecution
        {
            ScenarioId = scenarioId,
            Status = result.Status,
            Results = JsonSerializer.Serialize(result),
            ExecutedAt = DateTime.UtcNow
        });
        _context.SaveChanges();

        return Ok(result);
    }
    catch (Exception ex)
    {
        return BadRequest(new { Error = ex.Message });
    }
}

public class TestExecutor
{
    public TestResult ExecuteScenario(TestScenario scenario)
    {
        var testSteps = JsonSerializer.Deserialize<List<TestStep>>(scenario.TestSteps);
        var expectedResults = JsonSerializer.Deserialize<List<string>>(scenario.ExpectedResults);
        
        var result = new TestResult
        {
            ScenarioName = scenario.Name,
            StartTime = DateTime.UtcNow,
            Steps = new List<StepResult>()
        };

        foreach (var step in testSteps)
        {
            var stepResult = ExecuteStep(step);
            result.Steps.Add(stepResult);
            
            if (!stepResult.Passed)
            {
                result.Status = "Failed";
                break;
            }
        }

        result.EndTime = DateTime.UtcNow;
        result.Duration = result.EndTime - result.StartTime;
        
        if (result.Status != "Failed")
            result.Status = "Passed";

        return result;
    }

    private StepResult ExecuteStep(TestStep step)
    {
        try
        {
            switch (step.Action.ToLower())
            {
                case "verify":
                    return VerifyCondition(step.Target, step.Expected);
                case "click":
                    return SimulateClick(step.Target);
                case "input":
                    return SimulateInput(step.Target, step.Value);
                default:
                    return new StepResult { Passed = false, Message = $"Unknown action: {step.Action}" };
            }
        }
        catch (Exception ex)
        {
            return new StepResult { Passed = false, Message = ex.Message };
        }
    }

    private StepResult VerifyCondition(string target, string expected)
    {
        // Simulate verification logic
        return new StepResult { Passed = true, Message = $"Verified {target} equals {expected}" };
    }

    private StepResult SimulateClick(string target)
    {
        return new StepResult { Passed = true, Message = $"Clicked on {target}" };
    }

    private StepResult SimulateInput(string target, string value)
    {
        return new StepResult { Passed = true, Message = $"Input '{value}' into {target}" };
    }
}
```

----

### 🧪 Senaryo 7: Bir otomatik test aracı kullanıcıların test senaryoları yazmasına olanak tanır. Test senaryoları sistem tarafından çalıştırılarak sonuçlar alınır. Kullanıcılar özel test durumları tanımlayabilir. Test mantığı kullanıcı girişlerine göre şekillenir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import json
import time
from datetime import datetime

class TestExecutor:
    def __init__(self):
        self.test_scenarios = {}
        self.test_executions = []
        self.actions = {
            'verify': self.verify_action,
            'click': self.click_action,
            'input': self.input_action,
            'wait': self.wait_action,
            'navigate': self.navigate_action
        }
    
    def create_test_scenario(self, name, description, test_steps, expected_results, user_id):
        scenario_id = len(self.test_scenarios) + 1
        scenario = {
            'id': scenario_id,
            'name': name,
            'description': description,
            'test_steps': test_steps,
            'expected_results': expected_results,
            'created_by': user_id,
            'created_date': datetime.utcnow().isoformat()
        }
        
        self.test_scenarios[scenario_id] = scenario
        return scenario_id
    
    def execute_test_scenario(self, scenario_id):
        scenario = self.test_scenarios.get(scenario_id)
        if not scenario:
            raise ValueError("Test scenario not found")
        
        execution_result = {
            'scenario_id': scenario_id,
            'scenario_name': scenario['name'],
            'start_time': datetime.utcnow().isoformat(),
            'steps': [],
            'status': 'Running'
        }
        
        try:
            for i, step in enumerate(scenario['test_steps']):
                step_result = self.execute_step(step, i + 1)
                execution_result['steps'].append(step_result)
                
                if not step_result['passed']:
                    execution_result['status'] = 'Failed'
                    break
            
            if execution_result['status'] == 'Running':
                execution_result['status'] = 'Passed'
                
        except Exception as e:
            execution_result['status'] = 'Error'
            execution_result['error'] = str(e)
        
        execution_result['end_time'] = datetime.utcnow().isoformat()
        self.test_executions.append(execution_result)
        
        return execution_result
    
    def execute_step(self, step, step_number):
        action = step.get('action', '').lower()
        target = step.get('target', '')
        value = step.get('value', '')
        expected = step.get('expected', '')
        
        step_result = {
            'step_number': step_number,
            'action': action,
            'target': target,
            'passed': False,
            'message': '',
            'timestamp': datetime.utcnow().isoformat()
        }
        
        try:
            if action in self.actions:
                result = self.actions[action](target, value, expected)
                step_result.update(result)
            else:
                step_result['message'] = f"Unknown action: {action}"
                
        except Exception as e:
            step_result['message'] = f"Error executing step: {str(e)}"
        
        return step_result
    
    def verify_action(self, target, value, expected):
        # Simulate verification
        actual_value = self.get_element_value(target)
        passed = actual_value == expected
        
        return {
            'passed': passed,
            'message': f"Verified {target}: expected '{expected}', got '{actual_value}'"
        }
    
    def click_action(self, target, value, expected):
        # Simulate click
        success = self.simulate_click(target)
        return {
            'passed': success,
            'message': f"Clicked on element: {target}"
        }
    
    def input_action(self, target, value, expected):
        # Simulate input
        success = self.simulate_input(target, value)
        return {
            'passed': success,
            'message': f"Input '{value}' into {target}"
        }
    
    def wait_action(self, target, value, expected):
        # Simulate wait
        wait_time = float(value) if value else 1.0
        time.sleep(wait_time)
        return {
            'passed': True,
            'message': f"Waited {wait_time} seconds"
        }
    
    def navigate_action(self, target, value, expected):
        # Simulate navigation
        return {
            'passed': True,
            'message': f"Navigated to: {target}"
        }
    
    def get_element_value(self, target):
        # Simulate getting element value
        return f"value_of_{target}"
    
    def simulate_click(self, target):
        # Simulate successful click
        return True
    
    def simulate_input(self, target, value):
        # Simulate successful input
        return True

@app.route('/create-test-scenario', methods=['POST'])
def create_test_scenario():
    data = request.json
    executor = TestExecutor()
    
    try:
        scenario_id = executor.create_test_scenario(
            data['name'],
            data['description'],
            data['test_steps'],
            data['expected_results'],
            data['user_id']
        )
        return jsonify({'scenario_id': scenario_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/execute-test/<int:scenario_id>', methods=['POST'])
def execute_test(scenario_id):
    executor = TestExecutor()
    
    try:
        result = executor.execute_test_scenario(scenario_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
```

----

### 🧪 Senaryo 7: Bir otomatik test aracı kullanıcıların test senaryoları yazmasına olanak tanır. Test senaryoları sistem tarafından çalıştırılarak sonuçlar alınır. Kullanıcılar özel test durumları tanımlayabilir. Test mantığı kullanıcı girişlerine göre şekillenir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
interface TestScenario {
  id: string;
  name: string;
  description: string;
  testSteps: TestStep[];
  expectedResults: string[];
  createdBy: string;
  createdDate: Date;
}

interface TestStep {
  action: 'verify' | 'click' | 'input' | 'wait' | 'navigate';
  target: string;
  value?: string;
  expected?: string;
  timeout?: number;
}

interface TestResult {
  scenarioId: string;
  scenarioName: string;
  status: 'Passed' | 'Failed' | 'Error';
  startTime: Date;
  endTime?: Date;
  duration?: number;
  steps: StepResult[];
  errorMessage?: string;
}

interface StepResult {
  stepNumber: number;
  action: string;
  target: string;
  passed: boolean;
  message: string;
  timestamp: Date;
  duration: number;
}

class TestExecutor {
  private testScenarios: Map<string, TestScenario> = new Map();
  private testExecutions: TestResult[] = [];

  createTestScenario(
    name: string,
    description: string,
    testSteps: TestStep[],
    expectedResults: string[],
    userId: string
  ): string {
    const scenarioId = Date.now().toString();
    
    const scenario: TestScenario = {
      id: scenarioId,
      name,
      description,
      testSteps,
      expectedResults,
      createdBy: userId,
      createdDate: new Date()
    };

    this.testScenarios.set(scenarioId, scenario);
    return scenarioId;
  }

  async executeTestScenario(scenarioId: string): Promise<TestResult> {
    const scenario = this.testScenarios.get(scenarioId);
    if (!scenario) {
      throw new Error('Test scenario not found');
    }

    const testResult: TestResult = {
      scenarioId,
      scenarioName: scenario.name,
      status: 'Passed',
      startTime: new Date(),
      steps: []
    };

    try {
      for (let i = 0; i < scenario.testSteps.length; i++) {
        const step = scenario.testSteps[i];
        const stepResult = await this.executeStep(step, i + 1);
        testResult.steps.push(stepResult);

        if (!stepResult.passed) {
          testResult.status = 'Failed';
          break;
        }
      }
    } catch (error) {
      testResult.status = 'Error';
      testResult.errorMessage = error.message;
    }

    testResult.endTime = new Date();
    testResult.duration = testResult.endTime.getTime() - testResult.startTime.getTime();
    
    this.testExecutions.push(testResult);
    return testResult;
  }

  private async executeStep(step: TestStep, stepNumber: number): Promise<StepResult> {
    const startTime = new Date();
    
    const stepResult: StepResult = {
      stepNumber,
      action: step.action,
      target: step.target,
      passed: false,
      message: '',
      timestamp: startTime,
      duration: 0
    };

    try {
      switch (step.action) {
        case 'verify':
          stepResult.passed = await this.verifyElement(step.target, step.expected);
          stepResult.message = `Verified ${step.target} equals ${step.expected}`;
          break;
        
        case 'click':
          stepResult.passed = await this.clickElement(step.target);
          stepResult.message = `Clicked on ${step.target}`;
          break;
        
        case 'input':
          stepResult.passed = await this.inputValue(step.target, step.value || '');
          stepResult.message = `Input '${step.value}' into ${step.target}`;
          break;
        
        case 'wait':
          const waitTime = parseInt(step.value || '1000');
          await this.wait(waitTime);
          stepResult.passed = true;
          stepResult.message = `Waited ${waitTime}ms`;
          break;
        
        case 'navigate':
          stepResult.passed = await this.navigate(step.target);
          stepResult.message = `Navigated to ${step.target}`;
          break;
        
        default:
          stepResult.message = `Unknown action: ${step.action}`;
      }
    } catch (error) {
      stepResult.message = `Error: ${error.message}`;
    }

    const endTime = new Date();
    stepResult.duration = endTime.getTime() - startTime.getTime();
    
    return stepResult;
  }

  private async verifyElement(target: string, expected?: string): Promise<boolean> {
    // Simulate element verification
    const actualValue = await this.getElementValue(target);
    return actualValue === expected;
  }

  private async clickElement(target: string): Promise<boolean> {
    // Simulate clicking an element
    await this.wait(100); // Simulate action delay
    return true;
  }

  private async inputValue(target: string, value: string): Promise<boolean> {
    // Simulate inputting a value
    await this.wait(200); // Simulate typing delay
    return true;
  }

  private async navigate(url: string): Promise<boolean> {
    // Simulate navigation
    await this.wait(500); // Simulate page load
    return true;
  }

  private async getElementValue(target: string): Promise<string> {
    // Simulate getting element value
    return `value_of_${target}`;
  }

  private async wait(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  getTestScenario(scenarioId: string): TestScenario | undefined {
    return this.testScenarios.get(scenarioId);
  }

  getTestExecutions(): TestResult[] {
    return [...this.testExecutions];
  }
}
```

----

### 🧪 Senaryo 8: Bir hesaplama motoru kullanıcıların özel hesaplama formülleri girmesine izin verir. Formüller sistem tarafından değerlendirilerek sonuçlar üretilir. Kullanıcılar karmaşık hesaplamalar tanımlayabilir. Hesaplama sonuçları kullanıcıya döndürülür.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("create-calculation")]
public IActionResult CreateCalculation([FromBody] CalculationRequest request)
{
    try
    {
        var validator = new FormulaValidator();
        if (!validator.IsValidFormula(request.Formula))
            return BadRequest(new { Error = "Invalid formula syntax" });

        var calculation = new Calculation
        {
            Name = request.Name,
            Formula = request.Formula,
            Description = request.Description,
            Variables = JsonSerializer.Serialize(request.Variables),
            CreatedBy = request.UserId,
            CreatedDate = DateTime.UtcNow
        };

        _context.Calculations.Add(calculation);
        _context.SaveChanges();

        return Ok(new { CalculationId = calculation.Id });
    }
    catch (Exception ex)
    {
        return BadRequest(new { Error = ex.Message });
    }
}

[HttpPost("execute-calculation/{calculationId}")]
public IActionResult ExecuteCalculation(int calculationId, [FromBody] ExecutionRequest request)
{
    var calculation = _context.Calculations.Find(calculationId);
    if (calculation == null) return NotFound();

    try
    {
        var engine = new CalculationEngine();
        var result = engine.Calculate(calculation.Formula, request.InputValues);

        _context.CalculationResults.Add(new CalculationResult
        {
            CalculationId = calculationId,
            InputValues = JsonSerializer.Serialize(request.InputValues),
            Result = result,
            ExecutedAt = DateTime.UtcNow
        });
        _context.SaveChanges();

        return Ok(new { Result = result, Formula = calculation.Formula });
    }
    catch (Exception ex)
    {
        return BadRequest(new { Error = ex.Message });
    }
}

public class CalculationEngine
{
    private readonly Dictionary<string, Func<double[], double>> _functions;

    public CalculationEngine()
    {
        _functions = new Dictionary<string, Func<double[], double>>
        {
            { "SUM", args => args.Sum() },
            { "AVG", args => args.Average() },
            { "MAX", args => args.Max() },
            { "MIN", args => args.Min() },
            { "SQRT", args => Math.Sqrt(args[0]) },
            { "POW", args => Math.Pow(args[0], args[1]) },
            { "SIN", args => Math.Sin(args[0]) },
            { "COS", args => Math.Cos(args[0]) }
        };
    }

    public double Calculate(string formula, Dictionary<string, double> variables)
    {
        var processedFormula = ProcessFormula(formula, variables);
        var dataTable = new System.Data.DataTable();
        var result = dataTable.Compute(processedFormula, null);
        return Convert.ToDouble(result);
    }

    private string ProcessFormula(string formula, Dictionary<string, double> variables)
    {
        var processed = formula;

        // Replace variables
        foreach (var variable in variables)
        {
            processed = processed.Replace(variable.Key, variable.Value.ToString());
        }

        // Replace functions
        foreach (var function in _functions)
        {
            processed = ReplaceFunctions(processed, function.Key, function.Value);
        }

        return processed;
    }

    private string ReplaceFunctions(string formula, string functionName, Func<double[], double> function)
    {
        var pattern = $@"{functionName}\(([^)]+)\)";
        return Regex.Replace(formula, pattern, match =>
        {
            var args = match.Groups[1].Value.Split(',').Select(double.Parse).ToArray();
            return function(args).ToString();
        });
    }
}
```

----

### 🧪 Senaryo 8: Bir hesaplama motoru kullanıcıların özel hesaplama formülleri girmesine izin verir. Formüller sistem tarafından değerlendirilerek sonuçlar üretilir. Kullanıcılar karmaşık hesaplamalar tanımlayabilir. Hesaplama sonuçları kullanıcıya döndürülür.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import math
import re
from datetime import datetime

class CalculationEngine:
    def __init__(self):
        self.calculations = {}
        self.functions = {
            'SUM': lambda args: sum(args),
            'AVG': lambda args: sum(args) / len(args) if args else 0,
            'MAX': lambda args: max(args) if args else 0,
            'MIN': lambda args: min(args) if args else 0,
            'SQRT': lambda args: math.sqrt(args[0]) if args else 0,
            'POW': lambda args: math.pow(args[0], args[1]) if len(args) >= 2 else 0,
            'SIN': lambda args: math.sin(args[0]) if args else 0,
            'COS': lambda args: math.cos(args[0]) if args else 0,
            'TAN': lambda args: math.tan(args[0]) if args else 0,
            'LOG': lambda args: math.log(args[0]) if args and args[0] > 0 else 0,
            'ABS': lambda args: abs(args[0]) if args else 0
        }
        
        self.constants = {
            'PI': math.pi,
            'E': math.e
        }
    
    def validate_formula(self, formula):
        # Basic validation for safe formula
        allowed_chars = r'[a-zA-Z0-9+\-*/().,<>=! ]'
        if not re.match(f'^{allowed_chars}+$', formula):
            return False, "Invalid characters in formula"
        
        # Check for balanced parentheses
        if formula.count('(') != formula.count(')'):
            return False, "Unbalanced parentheses"
        
        return True, "Valid"
    
    def create_calculation(self, name, formula, description, variables, user_id):
        is_valid, message = self.validate_formula(formula)
        if not is_valid:
            raise ValueError(message)
        
        calc_id = len(self.calculations) + 1
        calculation = {
            'id': calc_id,
            'name': name,
            'formula': formula,
            'description': description,
            'variables': variables,
            'created_by': user_id,
            'created_date': datetime.utcnow().isoformat()
        }
        
        self.calculations[calc_id] = calculation
        return calc_id
    
    def execute_calculation(self, calc_id, input_values):
        calculation = self.calculations.get(calc_id)
        if not calculation:
            raise ValueError("Calculation not found")
        
        try:
            result = self.calculate(calculation['formula'], input_values)
            return {
                'result': result,
                'formula': calculation['formula'],
                'input_values': input_values
            }
        except Exception as e:
            raise ValueError(f"Calculation error: {str(e)}")
    
    def calculate(self, formula, variables):
        processed_formula = self.process_formula(formula, variables)
        
        # Create safe evaluation environment
        safe_dict = {
            "__builtins__": {},
            "abs": abs, "round": round, "min": min, "max": max,
            "sum": sum, "pow": pow
        }
        safe_dict.update(self.constants)
        
        try:
            result = eval(processed_formula, safe_dict)
            return float(result)
        except Exception as e:
            raise ValueError(f"Formula evaluation error: {str(e)}")
    
    def process_formula(self, formula, variables):
        processed = formula
        
        # Replace variables with their values
        for var_name, var_value in variables.items():
            processed = processed.replace(var_name, str(var_value))
        
        # Replace constants
        for const_name, const_value in self.constants.items():
            processed = processed.replace(const_name, str(const_value))
        
        # Replace functions
        for func_name, func_impl in self.functions.items():
            processed = self.replace_functions(processed, func_name, func_impl)
        
        return processed
    
    def replace_functions(self, formula, func_name, func_impl):
        pattern = f"{func_name}\\(([^)]+)\\)"
        
        def replace_match(match):
            args_str = match.group(1)
            args = [float(arg.strip()) for arg in args_str.split(',')]
            return str(func_impl(args))
        
        return re.sub(pattern, replace_match, formula)

@app.route('/create-calculation', methods=['POST'])
def create_calculation():
    data = request.json
    engine = CalculationEngine()
    
    try:
        calc_id = engine.create_calculation(
            data['name'],
            data['formula'],
            data['description'],
            data['variables'],
            data['user_id']
        )
        return jsonify({'calculation_id': calc_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/execute-calculation/<int:calc_id>', methods=['POST'])
def execute_calculation(calc_id):
    data = request.json
    engine = CalculationEngine()
    
    try:
        result = engine.execute_calculation(calc_id, data['input_values'])
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400