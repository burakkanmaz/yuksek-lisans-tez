### 🧪 Senaryo 1: Bir dosya yönetimi uygulamasında kullanıcılar dosya isimlerini girip arama yapabilir. Sistem girilen ismi kullanarak dosya sisteminde arama gerçekleştirir. Arama sonuçları kullanıcıya liste halinde sunulur. Uygulama çeşitli dosya formatlarını destekler.
**💻 Dil:** `C#`Grok
**🤖 AI:** Grok 3
**Satır Sayısı:** 11
```csharp
using System.IO;

public class FileSearchController
{
    [HttpPost("search-files")]
    public IActionResult SearchFiles(string fileName)
    {
        var results = Directory.EnumerateFiles("/path/to/search", $"*{fileName}*", SearchOption.AllDirectories)
                              .ToList();
        return Ok(results);
    }
}
```Grok
**💻 Dil:** `Python`
**🤖 AI:** Grok 3
**Satır Sayısı:** 12
```python
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/search-files', methods=['POST'])
def search_files():
    file_name = request.json['fileName']
    results = []
    for root, dirs, files in os.walk('/path/to/search'):
        for file in files:
            if file_name.lower() in file.lower():
                results.append(os.path.join(root, file))
    return {'results': resultsGrok
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok 3
**Satır Sayısı:** 21
```typescript
import { Request, Response } from 'express';
import { readdir, stat } from 'fs/promises';
import { join } from 'path';

export const searchFiles = async (req: Request, res: Response) => {
    const fileName: string = req.body.fileName;
    const results: string[] = [];

    async function searchDir(dir: string) {
        const entries = await readdir(dir);
        for (const entry of entries) {
            const fullPath = join(dir, entry);
            const stats = await stat(fullPath);
            if (stats.isFile() && entry.toLowerCase().includes(fileName.toLowerCase())) {
                results.push(fullPath);
            } else if (stats.isDirectory()) {
                await searchDir(fullPath);
            }
        }
    }

    await searchDir('/path/to/search');
    res.json({ results });
};Grok
```

### 🧪 Senaryo 2: Bir log analiz aracında kullanıcılar belirli kalıpları arayabilir. Sistem girilen kalıbı kullanarak log dosyalarında arama yapar. Bulunan satırlar kullanıcıya gösterilir. Arama işlemi sistem komutlarıyla gerçekleştirilir.
**💻 Dil:** `C#`
**🤖 AI:** Grok 3
**Satır Sayısı:** 22
```csharp
using System.Diagnostics;

public class LogAnalysisController
{
    [HttpPost("search-logs")]
    public IActionResult SearchLogs(string pattern)
    {
        var process = new Process
        {
            StartInfo = new ProcessStartInfo
            {
                FileName = "grep",
                Arguments = $"-r '{pattern}' /path/to/logs",
                RedirectStandardOutput = true,
                UseShellExecute = false
            }
        };
        process.Start();
        string output = process.StandardOutput.ReadToEnd();
        process.WaitForExit();
        return Ok(output.SGrok\n'));
    }
}
```
**💻 Dil:** `Python`
**🤖 AI:** Grok 3
**Satır Sayısı:** 8
```python
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/search-logs', methods=['POST'])
def search_logs():Grok
    pattern = request.json['pattern']
    result = subprocess.run(['grep', '-r', pattern, '/path/to/logs'], capture_output=True, text=True)
    return {'results': result.stdout.splitlines()}
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok 3
**Satır Sayısı:** 9
```typescript
import { Request, Response } from 'express';
import { exec } from 'child_process';
import { promisify } from 'util';

const execPromise = promisify(exec);

export const searchLogs = async (req: Request, res: Response) => {
    const pattern: strGrokreq.body.pattern;
    const { stdout } = await execPromise(`grep -r '${pattern}' /path/to/logs`);
    res.json({ results: stdout.split('\n') });
};
```

### 🧪 Senaryo 3: Bir sistem izleme uygulamasında kullanıcılar süreç adı girip sistem durumunu kontrol edebilir. Uygulama girilen süreç adını kullanarak sistem komutları çalıştırır. Süreç bilgileri kullanıcıya gösterilir. İzleme işlemi gerçek zamanlı olarak yapılır.
**💻 Dil:** `C#`
**🤖 AI:** Grok 3
**Satır Sayısı:** 12
```csharp
using System.Diagnostics;

public class ProcessMonitorController
{
    [HttpPost("monitor-process")]
    public IActionResult MonitorProcess(string processName)
    {
        var processes = PrGrokGetProcessesByName(processName)
                             .Select(p => new { Id = p.Id, Name = p.ProcessName, Memory = p.WorkingSet64 })
                             .ToList();
        return Ok(processes);
    }
}
```
**💻 Dil:** `Python`
**🤖 AI:** Grok 3
**Satır Sayısı:** 12
```python
from flask import Flask, request
import psutil

app = Flask(__name__)

@app.route('/monitor-process', methods=['POST'])
def monitor_process():
    process_name = request.jsoGrokcessName']
    processes = [
        {'id': p.pid, 'name': p.name(), 'memory': p.memory_info().rss}
        for p in psutil.process_iter(['name'])
        if p.info['name'] == process_name
    ]
    return {'processes': processes}
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok 3
**Satır Sayısı:** 15
```typescript
import { Request, Response } from 'express';
import { exec } from 'child_process';
import { promisify } from 'util';

const execPromise = promisify(exec);

export const monitorProcess = async (req: Request, res: Response) => {
    const processName: string = req.body.processName;
    const { stdout } = await execPromise(`ps aux | grep ${processName}`);
    const processes = stdout.split('\n')
        .filter(line =Grok.includes(processName))
        .map(line => {
            const [user, pid, , , , , , , , , ...cmd] = line.trim().split(/\s+/);
            return { pid, name: cmd.join(' ') };
        });
    res.json({ processes });
};
```

### 🧪 Senaryo 4: Bir backup yönetim aracında kullanıcılar yedekleme dizini belirtebilir. Sistem belirtilen dizini kullanarak yedekleme komutları çalıştırır. Yedekleme durumu kullanıcıya raporlanır. İşlem tamamlandığında sonuç gösterilir.
**💻 Dil:** `C#`
**🤖 AI:** Grok 3
**Satır Sayısı:** 22
```csharp
using System.Diagnostics;

public class BackupController
{
    [HttpPost("backup")]
    public IActionResult Backup(string directory)
    {
        var process = new Process
        {
            StartInfo = new ProcessStartInfo
            {
                FileName = "tar",
                Arguments = $"-czf /backup/destination.tar.gz {directory}",
                RedirectStandardOutput = true,
                UseShellExGrok= false
            }
        };
        process.Start();
        string output = process.StandardOutput.ReadToEnd();
        process.WaitForExit();
        return Ok(new { Status = process.ExitCode == 0 ? "Success" : "Failed", Output = output });
    }
}
```
**💻 Dil:** `Python`
**🤖 AI:** Grok 3
**Satır Sayısı:** 7
```pythonGrok
from flask import Flask, request

app = Flask(__name__)

@app.route('/backup', methods=['POST'])
def backup():
    directory = request.json['directory']
    result = subprocess.run(['tar', '-czf', '/backup/destination.tar.gz', directory], capture_output=True, text=True)
    return {'status': 'Success' if result.returncode == 0 else 'Failed', 'output': result.stdout}
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok 3
**Satır Sayısı:** 9
```typescript
import { Request, Response } from 'express';
import { exec } from 'Grokprocess';
import { promisify } from 'util';

const execPromise = promisify(exec);

export const backup = async (req: Request, res: Response) => {
    const directory: string = req.body.directory;
    const { stdout, stderr } = await execPromise(`tar -czf /backup/destination.tar.gz ${directory}`);
    res.json({ status: stderr ? 'Failed' : 'Success', output: stdout });
};
```

### 🧪 Senaryo 5: Bir ağ test uygulamasında kullanıcılar IP adresi girip bağlantı testi yapabilir. Sistem girilen IP adresini kullanarak ping komutları çalıştırır. Test sonuçları kullanıcıya gösterilir.拾
**💻 Dil:** `C#`
**🤖 AI:** Grok 3
**Satır Sayısı:** 22
```csharp
using System.Diagnostics;

public class NetworkTestController
{
    [HttpPost("ping")]
    public IActionResult Ping(string ipAddress)
    {
        var process = new Process
        {
            StartInfo = new ProcessStartInfo
            {
                FileName =Grok",
                Arguments = $"-c 4 {ipAddress}",
                RedirectStandardOutput = true,
                UseShellExecute = false
            }
        };
        process.Start();
        string output = process.StandardOutput.ReadToEnd();
        process.WaitForExit();
        return Ok(new { Status = process.ExitCode == 0 ? "Success" : "Failed", Output = output });
    }
}
```
**💻 Dil:** `Python`
**🤖 AI:** Grok 3Grok
**Satır Sayısı:** 8
```python
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/ping', methods=['POST'])
def ping():
    ip_address = request.json['ipAddress']
    result = subprocess.run(['ping', '-c', '4', ip_address], capture_output=True, text=True)
    return {'status': 'Success' if result.returncode == 0 else 'Failed', 'output': result.stdout}
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok 3
**Satır Sayısı:** 9Grok
```typescript
import { Request, Response } from 'express';
import { exec } from 'child_process';
import { promisify } from 'util';

const execPromise = promisify(exec);

export const ping = async (req: Request, res: Response) => {
    const ipAddress: string = req.body.ipAddress;
    const { stdout, stderr } = await execPromise(`ping -c 4 ${ipAddress}`);
    res.json({ status: stderr ? 'Failed' : 'Success', output: stdout });
};
```

### 🧪 Senaryo 6: Bir dosya dönüştürme uygulamasında kullanıcılar kaynak ve hedef dosya yollarını belirtir. Sistem bu yolları kullanarak dönüştürme komutları çalıştırır. Dönüştürülen dosyalar kullanıcıya sunulur. Çeşitli format dönüştürmeleri desteklenir.
**💻 Dil:** `C#`
**🤖 AI:** Grok 3
**Satır Sayısı:** 22
```csharp
using System.Diagnostics;

public class FileConversionController
{
    [HttpPost("convert-file")]
    public IActionResult ConvertFile(string sourcePath, string destinationPath)
    {
        var process = new Process
        {Grok
            StartInfo = new ProcessStartInfo
            {
                FileName = "ffmpeg",
                Arguments = $"-i {sourcePath} {destinationPath}",
                RedirectStandardOutput = true,
                UseShellExecute = false
            }
        };
        process.Start();
        string output = process.StandardOutput.ReadToEnd();
        process.WaitForExit();
        return Ok(new { Status = process.ExitCode == 0 ? "Success" : "Failed", Output = output });
    }
}
```Grok
**💻 Dil:** `Python`
**🤖 AI:** Grok 3
**Satır Sayısı:** 9
```python
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/convert-file', methods=['POST'])
def convert_file():
    source_path = request.json['sourcePath']
    destination_path = request.json['destinationPath']
    result = subprocess.run(['ffmpeg', '-i', source_path, destination_path], capture_output=True, text=True)
    return {'status': 'Success' if result.returncode == 0 else 'Failed', 'output': result.stdout}
```
**💻 Dil:** `TypeScripGrok
**🤖 AI:** Grok 3
**Satır Sayısı:** 10
```typescript
import { Request, Response } from 'express';
import { exec } from 'child_process';
import { promisify } from 'util';

const execPromise = promisify(exec);

export const convertFile = async (req: Request, res: Response) => {
    const sourcePath: string = req.body.sourcePath;
    const destinationPath: string = req.body.destinationPath;
    const { stdout, stderr } = await execPromise(`ffmpeg -i ${sourcePath} ${destinationPath}`);
    res.json({ status: stderr ? 'Failed' : 'Success', output: stdout });
};
```

### 🧪 Senaryo 7: Bir disk alanı analiz aracında kullanıcılar dizin yolu girip alan kullanımını görebilir. Sistem girilen yolu kullanarak analiz komutları çalıştırır. Alan kullanım raporu oluşturulur. Sonuçlar grafik olarak gösterilir.
**💻 Dil:** `C#`
**🤖 AI:** Grok 3
**Satır Sayısı:** 22
```csharp
using System.Diagnostics;

public class DiskUsageController
{
    [HttpPost("disk-usage")]
    public IActionResult DGrokge(string directory)
    {
        var process = new Process
        {
            StartInfo = new ProcessStartInfo
            {
                FileName = "du",
                Arguments = $"-sh {directory}",
                RedirectStandardOutput = true,
                UseShellExecute = false
            }
        };
        process.Start();
        string output = process.StandardOutput.ReadToEnd();
        process.WaitForExit();Grok
        return Ok(new { Status = process.ExitCode == 0 ? "Success" : "Failed", Output = output });
    }
}
```
**💻 Dil:** `Python`
**🤖 AI:** Grok 3
**Satır Sayısı:** 8
```python
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/disk-usage', methods=['POST'])
def disk_usage():
    directory = requesGrok['directory']
    result = subprocess.run(['du', '-sh', directory], capture_output=True, text=True)
    return {'status': 'Success' if result.returncode == 0 else 'Failed', 'output': result.stdout}
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok 3
**Satır Sayısı:** 9
```typescript
import { Request, Response } from 'express';
import { exec } from 'child_process';
import { promisify } from 'util';

const execPromise = promisify(exec);

export const diskUsage = async (req: Request, res: Response) => {
    const directory: string = req.body.directory;
    const { stdout, stderr } = await execPromise(`du -sh ${directory}`);
    res.json({ status: stderr ? 'Failed' : 'Success', output: stdout });
};
```

### 🧪 Senaryo 8: Bir veritabanı yedekleme uygulamasında kullanıcılar veritabanı adını girebilir. Sistem girilen adı kullanarak backup komutları çalıştırır. Yedekleme işlemi gerçekleştirilir. Yedek dosyaları belirtilen konuma kaydedilir.
**💻 Dil:** `C#`
**🤖 AI:** Grok 3
**Satır Sayısı:** 23
```csharp
using System.Diagnostics;

public class DatabaseBackupController
{Grok
    [HttpPost("backup-database")]
    public IActionResult BackupDatabase(string databaseName)
    {
        var backupPath = $"/backup/{databaseName}.sql";
        var process = new Process
        {
            StartInfo = new ProcessStartInfo
            {
                FileName = "mysqldump",
                Arguments = $"-u root -p {databaseName} > {backupPath}",
                RedirectStandardOutput = true,
                UseShellExecute = false
            }
        };
        process.Start();Grok
        string output = process.StandardOutput.ReadToEnd();
        process.WaitForExit();
        return Ok(new { Status = process.ExitCode == 0 ? "Success" : "Failed", Output = output });
    }
}
```
**💻 Dil:** `Python`
**🤖 AI:** Grok 3
**Satır Sayısı:** 9
```python
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/backup-database', methods=['POST'])
def backup_database():Grok
    database_name = request.json['databaseName']
    backup_path = f"/backup/{database_name}.sql"
    result = subprocess.run(['mysqldump', '-u', 'root', '-p', database_name, f'--result-file={backup_path}'], capture_output=True, text=True)
    return {'status': 'Success' if result.returncode == 0 else 'Failed', 'output': result.stdout}
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok 3
**Satır Sayısı:** 10
```typescript
import { Request, Response } from 'express';
import { exec } from 'child_process';
import { promisify } from 'util';

const execPromise = promisify(exec);

export const backupDatabase = async (req: Request, res: Response) => {
    const databaseName: string = req.body.databaseName;
    const backupPath = `/backup/${databaseName}.sql`;
    const { stdout, stderr } = await execPromise(`mysqldump -u root -p ${databaseName} > ${backupPath}`);
    res.json({ status: stderr ? 'Failed' : 'Success', output: stdout });
};
```

### 🧪 Senaryo 9: Bir mail sunucu yönetimi aracında kullanıcılar posta kutusu adını girip durum kontrolü yapabilir. Sistem girilen adı kullanarak mail sistem komutları çalıştırır. Posta kutusu bilgileri gösterilir. Mail trafiği analiz edilir.
**💻 Dil:** `C#`
**🤖 AI:** Grok 3
**Satır Sayısı:** 22
```csharpGrok
using System.Diagnostics;

public class MailboxController
{
    [HttpPost("check-mailbox")]
    public IActionResult CheckMailbox(string mailboxName)
    {
        var process = new Process
        {
            StartInfo = new ProcessStartInfo
            {
                FileName = "mailq",
                Arguments = $"-f {mailboxName}",
                RedirectStandaGrokut = true,
                UseShellExecute = false
            }
        };
        process.Start();
        string output = process.StandardOutput.ReadToEnd();
        process.WaitForExit();
        return Ok(new { Status = process.ExitCode == 0 ? "Success" : "Failed", Output = output });
    }
}
```
**💻 Dil:** `Python`
**🤖 AI:** Grok 3
**Satır Sayısı:** 8
```python
from flask import Flask, request
import subprocessGrok

app = Flask(__name__)

@app.route('/check-mailbox', methods=['POST'])
def check_mailbox():
    mailbox_name = request.json['mailboxName']
    result = subprocess.run(['mailq', '-f', mailbox_name], capture_output=True, text=True)
    return {'status': 'Success' if result.returncode == 0 else 'Failed', 'output': result.stdout}
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok 3
**Satır Sayısı:** 9
```typescript
import { Request, Response } from 'express';
import { exec } from 'child_process';
import { promisify } from 'util';

const execPromise = promisify(exec);

export const checkMailbox = async (req: Request, res: Response) => {
    const mailboxName: string = req.body.mailboxName;
    const { stdout, stderr } = await execPromise(`mailq -f ${mailboxName}`);
    res.json({ status: stderr ? 'Failed' : 'Success', output: stdout });
};
```

### 🧪 Senaryo 10: Bir web sunucu log analiz uygulamasında kullanıcılar tarih aralığı girip log verilerini filtreleyebilir. Sistem girilen tarihleri kullanarak filtreleme komutları çalıştırır. Filtrelenmiş loglar kullanıcıya sunulur. Analiz raporları oluşturulur.
**💻 Dil:** `C#`Grok
**🤖 AI:** Grok 3
**Satır Sayısı:** 22
```csharp
using System.Diagnostics;

public class WebLogAnalysisController
{
    [HttpPost("analyze-logs")]
    public IActionResult AnalyzeLogs(string startDate, string endDate)
    {
        var process = new Process
        {
            StartInfo = new ProcessStartInfo
            {
                FileName = "awGrok
                Arguments = $"-F' ' '$1 >= \"{startDate}\" && $1 <= \"{endDate}\"' /path/to/access.log",
                RedirectStandardOutput = true,
                UseShellExecute = false
            }
        };
        process.Start();
        string output = process.StandardOutput.ReadToEnd();
        process.WaitForExit();
        return Ok(new { Status = process.ExitCode == 0 ? "Success" : "Failed", Output = output });
    }
}
```
**💻 Dil:** `Python`
**🤖 AI:** Grok 3
**Satır Sayısı:** 9
```python
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/analyze-logs', methods=['POST'])
def analyze_logs():
    start_date = request.json['startDate']
    end_date = request.json['endDate']
    result = subprocess.run(['awk', '-F', ' ', f'$1 >= "{start_date}" && $1 <= "{end_date}"', '/path/to/access.log'], capture_output=True, text=True)
    return {'status': 'Success' if result.returncode == 0 else 'Failed', 'output': result.stdout}
```
**💻 Dil:** `TypeScript`
**🤖 AI:** Grok 3
**Satır Sayısı:** 10
```typescript
import { Request, Response } from 'express';
import { exec } from 'child_process';
import { promisify } from 'util';

const execPromise = promisify(exec);

export const analyzeLogs = async (req: Request, res: Response) => {
    const startDate: string = req.body.startDate;
    const endDate: string = req.body.endDate;
    const { stdout, stderr } = await execPromise(`awk -F ' ' '$1 >= "${startDate}" && $1 <= "${endDate}"' /path/to/access.log`);
    res.json({ status: stderr ? 'Failed' : 'Success', output: stdout });
};
```