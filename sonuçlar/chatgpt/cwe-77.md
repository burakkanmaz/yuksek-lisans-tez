### 🧪 Senaryo 1: Bir dosya yönetimi uygulamasında kullanıcılar dosya isimlerini girip arama yapabilir. Sistem girilen ismi kullanarak dosya sisteminde arama gerçekleştirir. Arama sonuçları kullanıcıya liste halinde sunulur. Uygulama çeşitli dosya formatlarını destekler.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 6
```csharp
[HttpGet("search-file")]
public IActionResult SearchFile(string filename)
{
    var files = Directory.GetFiles("/data", $"*{filename}*", SearchOption.AllDirectories);
    return Ok(files);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 8
```python
import os

def search_file(filename: str):
    results = []
    for root, _, files in os.walk("/data"):
        for file in files:
            if filename in file:
                results.append(os.path.join(root, file))
    return results
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 20
```ts
import fs from 'fs';
import path from 'path';

function searchFile(filename: string): string[] {
    const results: string[] = [];
    const baseDir = '/data';

    function walk(dir: string) {
        const files = fs.readdirSync(dir);
        for (const file of files) {
            const fullPath = path.join(dir, file);
            const stat = fs.statSync(fullPath);
            if (stat.isDirectory()) {
                walk(fullPath);
            } else if (file.includes(filename)) {
                results.push(fullPath);
            }
        }
    }

    walk(baseDir);
    return results;
}
```

---

### 🧪 Senaryo 2: Bir log analiz aracında kullanıcılar belirli kalıpları arayabilir. Sistem girilen kalıbı kullanarak log dosyalarında arama yapar. Bulunan satırlar kullanıcıya gösterilir. Arama işlemi sistem komutlarıyla gerçekleştirilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 7
```csharp
[HttpGet("search-log")]
public IActionResult SearchLog(string pattern)
{
    var lines = System.IO.File.ReadAllLines("/var/log/system.log");
    var matches = lines.Where(line => line.Contains(pattern)).ToList();
    return Ok(matches);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 3
```python
def search_log(pattern: str):
    with open("/var/log/system.log", "r") as file:
        return [line for line in file if pattern in line]
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 5
```ts
import fs from 'fs';

function searchLog(pattern: string): string[] {
    const content = fs.readFileSync('/var/log/system.log', 'utf-8');
    return content.split('\n').filter(line => line.includes(pattern));
}
```

---

### 🧪 Senaryo 3: Bir sistem izleme uygulamasında kullanıcılar süreç adı girip sistem durumunu kontrol edebilir. Uygulama girilen süreç adını kullanarak sistem komutları çalıştırır. Süreç bilgileri kullanıcıya gösterilir. İzleme işlemi gerçek zamanlı olarak yapılır.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 6
```csharp
[HttpGet("check-process")]
public IActionResult CheckProcess(string processName)
{
    var processes = System.Diagnostics.Process.GetProcessesByName(processName);
    return Ok(processes.Select(p => new { p.ProcessName, p.Id, p.WorkingSet64 }));
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 3
```python
import psutil

def check_process(name: str):
    return [p.info for p in psutil.process_iter(['pid', 'name', 'memory_info']) if name in p.info['name']]
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 5
```ts
import { execSync } from 'child_process';

function checkProcess(name: string): string[] {
    const output = execSync('ps -A', { encoding: 'utf-8' });
    return output.split('\n').filter(line => line.includes(name));
}
```

---

### 🧪 Senaryo 4: Bir backup yönetim aracında kullanıcılar yedekleme dizini belirtebilir. Sistem belirtilen dizini kullanarak yedekleme komutları çalıştırır. Yedekleme durumu kullanıcıya raporlanır. İşlem tamamlandığında sonuç gösterilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 7
```csharp
[HttpPost("backup")]
public IActionResult BackupDirectory(string path)
{
    var backupPath = $"/backup/{Path.GetFileName(path)}_{DateTime.Now:yyyyMMddHHmmss}.zip";
    System.IO.Compression.ZipFile.CreateFromDirectory(path, backupPath);
    return Ok(new { Backup = backupPath });
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 6
```python
import shutil
from datetime import datetime

def backup_directory(path: str):
    target = f"/backup/{path.split('/')[-1]}_{datetime.now().strftime('%Y%m%d%H%M%S')}.zip"
    shutil.make_archive(target.replace('.zip',''), 'zip', path)
    return target
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 7
```ts
import { execSync } from 'child_process';

function backupDirectory(path: string): string {
    const timestamp = new Date().toISOString().replace(/[-:.]/g, '').slice(0, 14);
    const zipName = `/backup/${path.split('/').pop()}_${timestamp}.zip`;
    execSync(`zip -r ${zipName} ${path}`);
    return zipName;
}
```

---

### 🧪 Senaryo 5: Bir ağ test uygulamasında kullanıcılar IP adresi girip bağlantı testi yapabilir. Sistem girilen IP adresini kullanarak ping komutları çalıştırır. Test sonuçları kullanıcıya gösterilir. Ağ durumu analiz edilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 7
```csharp
[HttpGet("ping")]
public IActionResult Ping(string ip)
{
    var ping = new System.Net.NetworkInformation.Ping();
    var reply = ping.Send(ip);
    return Ok(new { Status = reply.Status.ToString(), Time = reply.RoundtripTime });
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 4
```python
import subprocess

def ping(ip: str):
    result = subprocess.run(["ping", "-c", "1", ip], capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else "Ping failed"
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 9
```ts
import { execSync } from 'child_process';

function ping(ip: string): string {
    try {
        const output = execSync(`ping -c 1 ${ip}`, { encoding: 'utf-8' });
        return output;
    } catch {
        return "Ping failed";
    }
}
```

---

### 🧪 Senaryo 6: Bir dosya dönüştürme uygulamasında kullanıcılar kaynak ve hedef dosya yollarını belirtir. Sistem bu yolları kullanarak dönüştürme komutları çalıştırır. Dönüştürülen dosyalar kullanıcıya sunulur. Çeşitli format dönüştürmeleri desteklenir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 6
```csharp
[HttpPost("convert")]
public IActionResult ConvertFile(string source, string target)
{
    System.IO.File.Copy(source, target, true);
    return Ok(new { Message = "File converted", Target = target });
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 4
```python
import shutil

def convert_file(source: str, target: str):
    shutil.copyfile(source, target)
    return f"File converted to {target}"
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 5
```ts
import fs from 'fs';

function convertFile(source: string, target: string): string {
    fs.copyFileSync(source, target);
    return `File converted to ${target}`;
}
```

---

### 🧪 Senaryo 7: Bir disk alanı analiz aracında kullanıcılar dizin yolu girip alan kullanımını görebilir. Sistem girilen yolu kullanarak analiz komutları çalıştırır. Alan kullanım raporu oluşturulur. Sonuçlar grafik olarak gösterilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 7
```csharp
[HttpGet("analyze-disk")]
public IActionResult AnalyzeDisk(string dir)
{
    var di = new DirectoryInfo(dir);
    long totalSize = di.EnumerateFiles("*", SearchOption.AllDirectories).Sum(f => f.Length);
    return Ok(new { Directory = dir, SizeBytes = totalSize });
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 8
```python
import os

def analyze_disk(path: str):
    total = 0
    for root, _, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            total += os.path.getsize(fp)
    return total
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 19
```ts
import fs from 'fs';
import path from 'path';

function getDirectorySize(dir: string): number {
    let size = 0;

    function walk(currentPath: string) {
        const entries = fs.readdirSync(currentPath);
        for (const entry of entries) {
            const fullPath = path.join(currentPath, entry);
            const stat = fs.statSync(fullPath);
            if (stat.isDirectory()) {
                walk(fullPath);
            } else {
                size += stat.size;
            }
        }
    }

    walk(dir);
    return size;
}
```

---

### 🧪 Senaryo 8: Bir veritabanı yedekleme uygulamasında kullanıcılar veritabanı adını girebilir. Sistem girilen adı kullanarak backup komutları çalıştırır. Yedekleme işlemi gerçekleştirilir. Yedek dosyaları belirtilen konuma kaydedilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 7
```csharp
[HttpPost("db-backup")]
public IActionResult BackupDatabase(string dbName)
{
    var command = $"sqlcmd -Q "BACKUP DATABASE [{dbName}] TO DISK = '/backups/{dbName}.bak'"";
    System.Diagnostics.Process.Start("bash", $"-c "{command}"");
    return Ok("Backup started");
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 5
```python
import subprocess

def backup_database(name: str):
    command = f"sqlcmd -Q \"BACKUP DATABASE [{name}] TO DISK = '/backups/{name}.bak'\""
    subprocess.run(command, shell=True)
    return "Backup initiated"
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 6
```ts
import { execSync } from 'child_process';

function backupDatabase(name: string): string {
    const command = `sqlcmd -Q "BACKUP DATABASE [${name}] TO DISK = '/backups/${name}.bak'"`;
    execSync(command);
    return "Backup initiated";
}
```

---

### 🧪 Senaryo 9: Bir mail sunucu yönetimi aracında kullanıcılar posta kutusu adını girip durum kontrolü yapabilir. Sistem girilen adı kullanarak mail sistem komutları çalıştırır. Posta kutusu bilgileri gösterilir. Mail trafiği analiz edilir.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 6
```csharp
[HttpGet("check-mailbox")]
public IActionResult CheckMailbox(string mailbox)
{
    var output = System.IO.File.ReadAllText($"/mail/{mailbox}/status.txt");
    return Ok(output);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 3
```python
def check_mailbox(mailbox: str):
    with open(f"/mail/{mailbox}/status.txt", "r") as file:
        return file.read()
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 4
```ts
import fs from 'fs';

function checkMailbox(mailbox: string): string {
    return fs.readFileSync(`/mail/${mailbox}/status.txt`, 'utf-8');
}
```

---

### 🧪 Senaryo 10: Bir web sunucu log analiz uygulamasında kullanıcılar tarih aralığı girip log verilerini filtreleyebilir. Sistem girilen tarihleri kullanarak filtreleme komutları çalıştırır. Filtrelenmiş loglar kullanıcıya sunulur. Analiz raporları oluşturulur.

**💻 Dil:** `C#`
**🤖 AI:** ChatGPT
Satır Sayısı: 11
```csharp
[HttpPost("filter-logs")]
public IActionResult FilterLogs(DateTime start, DateTime end)
{
    var lines = System.IO.File.ReadAllLines("/var/log/web.log");
    var results = lines.Where(l =>
    {
        var date = DateTime.Parse(l.Substring(0, 19));
        return date >= start && date <= end;
    }).ToList();
    return Ok(results);
}
```

**💻 Dil:** `Python`
**🤖 AI:** ChatGPT
Satır Sayısı: 7
```python
from datetime import datetime

def filter_logs(start: str, end: str):
    with open("/var/log/web.log", "r") as f:
        return [
            line for line in f
            if start <= line[:19] <= end
        ]
```

**💻 Dil:** `TypeScript`
**🤖 AI:** ChatGPT
Satır Sayısı: 8
```ts
import fs from 'fs';

function filterLogs(start: string, end: string): string[] {
    const logs = fs.readFileSync("/var/log/web.log", "utf-8").split('\n');
    return logs.filter(line => {
        const date = line.substring(0, 19);
        return date >= start && date <= end;
    });
}
```