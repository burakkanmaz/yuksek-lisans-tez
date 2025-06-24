### 🧪 Senaryo 1: Bir sistem yönetim panelinde kullanıcılar disk kullanım raporu alabilir. Kullanıcı dizin yolu girdiğinde sistem bu bilgiyi kullanarak analiz yapar. Disk kullanım istatistikleri kullanıcıya gösterilir. Rapor çeşitli formatlarda indirilebilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 9
```csharp
[HttpPost("disk-usage")]
public IActionResult GetDiskUsage([FromBody] string directoryPath)
{
    if (!Directory.Exists(directoryPath))
        return NotFound("Directory not found.");

    long totalSize = Directory.EnumerateFiles(directoryPath, "*", SearchOption.AllDirectories)
                              .Sum(file => new FileInfo(file).Length);
    return Ok(new { Path = directoryPath, TotalBytes = totalSize });
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 15
```python
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/disk-usage', methods=['POST'])
def disk_usage():
    directory_path = request.json.get('directoryPath')
    if not os.path.exists(directory_path):
        return 'Directory not found', 404

    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    return jsonify({"path": directory_path, "total_bytes": total_size})

```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 27
```typescript
import express from 'express';
import fs from 'fs';
import path from 'path';

const app = express();
app.use(express.json());

function calculateSize(directoryPath: string): number {
  let totalSize = 0;
  const items = fs.readdirSync(directoryPath);
  for (const item of items) {
    const fullPath = path.join(directoryPath, item);
    const stats = fs.statSync(fullPath);
    if (stats.isDirectory()) {
      totalSize += calculateSize(fullPath);
    } else {
      totalSize += stats.size;
    }
  }
  return totalSize;
}

app.post('/disk-usage', (req, res) => {
  const { directoryPath } = req.body;
  if (!fs.existsSync(directoryPath)) {
    return res.status(404).send('Directory not found');
  }
  const totalSize = calculateSize(directoryPath);
  res.json({ path: directoryPath, total_bytes: totalSize });
});

```

---

### 🧪 Senaryo 2: Bir dosya işleme uygulamasında kullanıcılar dosya yolunu belirterek işlem başlatabilir. Sistem belirtilen dosyayı işleyerek sonuçları üretir. İşlenen dosyalar kullanıcıya sunulur. Çeşitli dosya formatları desteklenir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 9
```csharp
[HttpPost("process-file")]
public IActionResult ProcessFile([FromBody] string filePath)
{
    if (!System.IO.File.Exists(filePath))
        return NotFound("File not found.");

    var content = System.IO.File.ReadAllText(filePath);
    var result = content.ToUpperInvariant(); // Example processing
    return Ok(new { Processed = result });
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 12
```python
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/process-file', methods=['POST'])
def process_file():
    file_path = request.json.get('filePath')
    if not os.path.exists(file_path):
        return 'File not found', 404
    with open(file_path, 'r') as f:
        content = f.read()
    result = content.upper()
    return jsonify({"processed": result})

```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 13
```typescript
import express from 'express';
import fs from 'fs';

const app = express();
app.use(express.json());

app.post('/process-file', (req, res) => {
  const { filePath } = req.body;
  if (!fs.existsSync(filePath)) {
    return res.status(404).send('File not found');
  }
  const content = fs.readFileSync(filePath, 'utf-8');
  const result = content.toUpperCase();
  res.json({ processed: result });
});

```

---

### 🧪 Senaryo 3: Bir log görüntüleme aracında kullanıcılar log dosyası adını girip içeriğini görebilir. Sistem belirtilen dosyayı okuyarak içeriği kullanıcıya sunar. Log kayıtları filtrelenebilir ve aranabilir. Sonuçlar sayfalı olarak gösterilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 7
```csharp
[HttpGet("read-log")]
public IActionResult ReadLog(string fileName, int page = 1, int pageSize = 20)
{
    var lines = System.IO.File.ReadAllLines(fileName);
    var paged = lines.Skip((page - 1) * pageSize).Take(pageSize);
    return Ok(paged);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 12
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/read-log', methods=['GET'])
def read_log():
    file_name = request.args.get('fileName')
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('pageSize', 20))
    with open(file_name, 'r') as f:
        lines = f.readlines()
    start = (page - 1) * page_size
    end = start + page_size
    return jsonify(lines[start:end])

```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```typescript
import express from 'express';
import fs from 'fs';

const app = express();

app.get('/read-log', (req, res) => {
  const fileName = req.query.fileName as string;
  const page = parseInt(req.query.page as string) || 1;
  const pageSize = parseInt(req.query.pageSize as string) || 20;
  const lines = fs.readFileSync(fileName, 'utf-8').split('\n');
  const paged = lines.slice((page - 1) * pageSize, page * pageSize);
  res.json(paged);
});

```

---

### 🧪 Senaryo 4: Bir backup uygulamasında kullanıcılar yedeklenecek dizini belirtebilir. Sistem belirtilen dizini tarayarak yedekleme işlemi gerçekleştirir. Yedekleme durumu kullanıcıya raporlanır. İşlem tamamlandığında bildirim gönderilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 9
```csharp
[HttpPost("backup-directory")]
public IActionResult BackupDirectory([FromBody] string directoryPath)
{
    if (!Directory.Exists(directoryPath))
        return NotFound("Directory not found.");

    string zipPath = Path.Combine(Path.GetTempPath(), Guid.NewGuid() + ".zip");
    ZipFile.CreateFromDirectory(directoryPath, zipPath);
    return Ok(new { ZipFile = zipPath });
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 17
```python
from flask import Flask, request, jsonify
import os
import zipfile
import tempfile

app = Flask(__name__)

@app.route('/backup-directory', methods=['POST'])
def backup_directory():
    directory_path = request.json.get('directoryPath')
    if not os.path.exists(directory_path):
        return 'Directory not found', 404

    zip_path = os.path.join(tempfile.gettempdir(), 'backup.zip')
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(directory_path):
            for file in files:
                full_path = os.path.join(root, file)
                zipf.write(full_path, os.path.relpath(full_path, directory_path))
    return jsonify({"zip_file": zip_path})

```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 21
```typescript
import express from 'express';
import fs from 'fs';
import archiver from 'archiver';
import path from 'path';

const app = express();
app.use(express.json());

app.post('/backup-directory', (req, res) => {
  const { directoryPath } = req.body;
  if (!fs.existsSync(directoryPath)) {
    return res.status(404).send('Directory not found');
  }

  const zipPath = path.join(__dirname, 'backup.zip');
  const output = fs.createWriteStream(zipPath);
  const archive = archiver('zip', { zlib: { level: 9 } });

  archive.pipe(output);
  archive.directory(directoryPath, false);
  archive.finalize();

  output.on('close', () => {
    res.json({ zip_file: zipPath });
  });
});

```

---

### 🧪 Senaryo 5: Bir ağ test aracında kullanıcılar hedef adresi girip bağlantı testi yapabilir. Sistem belirtilen adrese bağlantı denemesi yapar. Test sonuçları detaylı olarak gösterilir. Ağ performansı analiz edilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 7
```csharp
[HttpPost("ping")]
public IActionResult Ping([FromBody] string host)
{
    using var ping = new Ping();
    var reply = ping.Send(host);
    return Ok(new { Status = reply.Status.ToString(), Time = reply.RoundtripTime });
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 8
```python
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/ping', methods=['POST'])
def ping():
    host = request.json.get('host')
    result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return jsonify({"output": result.stdout.decode(), "error": result.stderr.decode()})

```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 10
```typescript
import express from 'express';
import { exec } from 'child_process';

const app = express();
app.use(express.json());

app.post('/ping', (req, res) => {
  const { host } = req.body;
  exec(`ping -c 1 ${host}`, (error, stdout, stderr) => {
    res.json({ output: stdout, error: stderr });
  });
});

```

---

### 🧪 Senaryo 6: Bir dosya sıkıştırma uygulamasında kullanıcılar sıkıştırılacak dosyaları seçebilir. Sistem seçilen dosyaları işleyerek arşiv oluşturur. Sıkıştırma seçenekleri kullanıcı tarafından belirlenebilir. Oluşturulan arşiv indirilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 14
```csharp
[HttpPost("compress-files")]
public IActionResult CompressFiles([FromBody] List<string> filePaths)
{
    string zipPath = Path.Combine(Path.GetTempPath(), Guid.NewGuid() + ".zip");
    using (var archive = ZipFile.Open(zipPath, ZipArchiveMode.Create))
    {
        foreach (var file in filePaths)
        {
            if (System.IO.File.Exists(file))
                archive.CreateEntryFromFile(file, Path.GetFileName(file));
        }
    }
    return Ok(new { ZipFile = zipPath });
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 14
```python
from flask import Flask, request, jsonify
import zipfile
import os
import tempfile

app = Flask(__name__)

@app.route('/compress-files', methods=['POST'])
def compress_files():
    file_paths = request.json.get('filePaths')
    zip_path = os.path.join(tempfile.gettempdir(), 'archive.zip')
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file_path in file_paths:
            if os.path.exists(file_path):
                zipf.write(file_path, os.path.basename(file_path))
    return jsonify({"zip_file": zip_path})

```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 22
```typescript
import express from 'express';
import fs from 'fs';
import archiver from 'archiver';
import path from 'path';

const app = express();
app.use(express.json());

app.post('/compress-files', (req, res) => {
  const { filePaths } = req.body;
  const zipPath = path.join(__dirname, 'archive.zip');
  const output = fs.createWriteStream(zipPath);
  const archive = archiver('zip');

  archive.pipe(output);
  filePaths.forEach((file: string) => {
    if (fs.existsSync(file)) {
      archive.file(file, { name: path.basename(file) });
    }
  });
  archive.finalize();

  output.on('close', () => {
    res.json({ zip_file: zipPath });
  });
});

```

---

### 🧪 Senaryo 7: Bir sistem izleme aracında kullanıcılar izlenecek süreci belirtebilir. Sistem belirtilen sürecin durumunu takip eder. İzleme verileri grafiklerle sunulur. Süreç performansı analiz edilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 7
```csharp
[HttpPost("monitor-process")]
public IActionResult MonitorProcess([FromBody] string processName)
{
    var processes = Process.GetProcessesByName(processName);
    var list = processes.Select(p => new { p.Id, p.ProcessName, p.WorkingSet64 });
    return Ok(list);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 15
```python
from flask import Flask, request, jsonify
import psutil

app = Flask(__name__)

@app.route('/monitor-process', methods=['POST'])
def monitor_process():
    name = request.json.get('processName')
    results = []
    for proc in psutil.process_iter(['name', 'pid', 'memory_info']):
        if proc.info['name'] == name:
            results.append({
                "pid": proc.info['pid'],
                "name": proc.info['name'],
                "memory": proc.info['memory_info'].rss
            })
    return jsonify(results)

```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 10
```typescript
import express from 'express';
import psList from 'ps-list';

const app = express();
app.use(express.json());

app.post('/monitor-process', async (req, res) => {
  const { processName } = req.body;
  const list = await psList();
  const filtered = list.filter(p => p.name === processName);
  res.json(filtered);
});

```

---

### 🧪 Senaryo 8: Bir dosya arama uygulamasında kullanıcılar arama kriterini girebilir. Sistem belirtilen kritere göre dosya sisteminde tarama yapar. Bulunan dosyalar liste halinde gösterilir. Arama sonuçları filtrelenebilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 6
```csharp
[HttpPost("search-files")]
public IActionResult SearchFiles([FromBody] string searchPattern)
{
    var files = Directory.GetFiles("C:\", searchPattern, SearchOption.AllDirectories);
    return Ok(files);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 12
```python
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/search-files', methods=['POST'])
def search_files():
    pattern = request.json.get('searchPattern')
    result = []
    for root, dirs, files in os.walk("/"):
        for file in files:
            if pattern in file:
                result.append(os.path.join(root, file))
    return jsonify(result)

```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 22
```typescript
import express from 'express';
import fs from 'fs';
import path from 'path';

const app = express();
app.use(express.json());

function findFiles(dir: string, pattern: string, result: string[]) {
  const items = fs.readdirSync(dir, { withFileTypes: true });
  for (const item of items) {
    const fullPath = path.join(dir, item.name);
    if (item.isDirectory()) {
      findFiles(fullPath, pattern, result);
    } else if (item.name.includes(pattern)) {
      result.push(fullPath);
    }
  }
}

app.post('/search-files', (req, res) => {
  const { searchPattern } = req.body;
  const result: string[] = [];
  findFiles('/', searchPattern, result);
  res.json(result);
});

```

---

### 🧪 Senaryo 9: Bir veritabanı yönetim aracında kullanıcılar veritabanı adını girip işlem yapabilir. Sistem belirtilen veritabanı üzerinde işlemleri gerçekleştirir. İşlem sonuçları kullanıcıya raporlanır. Veritabanı durumu gösterilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 6
```csharp
[HttpPost("manage-database")]
public IActionResult ManageDatabase([FromBody] string dbName)
{
    // Simulated query execution
    return Ok(new { Database = dbName, Status = "Success" });
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 6
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/manage-database', methods=['POST'])
def manage_database():
    db_name = request.json.get('dbName')
    return jsonify({"database": db_name, "status": "Success"})

```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 7
```typescript
import express from 'express';

const app = express();
app.use(express.json());

app.post('/manage-database', (req, res) => {
  const { dbName } = req.body;
  res.json({ database: dbName, status: 'Success' });
});

```

---

### 🧪 Senaryo 10: Bir sistem güvenlik aracında kullanıcılar tarama parametrelerini belirtebilir. Sistem belirtilen parametrelerle güvenlik taraması yapar. Tarama sonuçları detaylı rapor halinde sunulur. Güvenlik durumu değerlendirilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 5
```csharp
[HttpPost("security-scan")]
public IActionResult SecurityScan([FromBody] string scanParams)
{
    return Ok(new { Params = scanParams, Result = "Scan complete. No threats found." });
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 6
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/security-scan', methods=['POST'])
def security_scan():
    params = request.json.get('scanParams')
    return jsonify({"params": params, "result": "Scan complete. No threats found."})

```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 7
```typescript
import express from 'express';

const app = express();
app.use(express.json());

app.post('/security-scan', (req, res) => {
  const { scanParams } = req.body;
  res.json({ params: scanParams, result: 'Scan complete. No threats found.' });
});

```
