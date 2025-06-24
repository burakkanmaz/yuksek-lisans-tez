### 🧪 Senaryo 1: Bir dosya yönetimi uygulamasında kullanıcılar dosya isimlerini girip arama yapabilir. Sistem girilen ismi kullanarak dosya sisteminde arama gerçekleştirir. Arama sonuçları kullanıcıya liste halinde sunulur. Uygulama çeşitli dosya formatlarını destekler.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 12
```csharp
[HttpGet("search-files")]  
public IActionResult SearchFiles(string fileName)  
{  
    try  
    {  
        var files = Directory.GetFiles("/var/files", $"{fileName}*");  
        return Ok(new { success = true, files });  
    }  
    catch (Exception ex)  
    {  
        return StatusCode(500, new { success = false, error = ex.Message });  
    }  
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 7
```python
import glob  

def search_files(file_name: str) -> dict:  
    try:  
        files = glob.glob(f"/var/files/{file_name}*")  
        return {"success": True, "files": files}  
    except Exception as e:  
        return {"success": False, "error": str(e)}
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 11
```typescript
import fs from 'fs/promises';  

async function searchFiles(fileName: string): Promise<object> {  
    try {  
        const files = await fs.readdir('/var/files');  
        const matchedFiles = files.filter(file => file.startsWith(fileName));  
        return { success: true, files: matchedFiles };  
    } catch (error) {  
        return { success: false, error: error.message };  
    }  
}
```

### 🧪 Senaryo 2: Bir log analiz aracında kullanıcılar belirli kalıpları arayabilir. Sistem girilen kalıbı kullanarak log dosyalarında arama yapar. Bulunan satırlar kullanıcıya gösterilir. Arama işlemi sistem komutlarıyla gerçekleştirilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 12
```csharp
[HttpGet("search-logs")]  
public async Task<IActionResult> SearchLogs(string pattern)  
{  
    try  
    {  
        var logLines = await File.ReadAllLinesAsync("/var/logs/app.log");  
        var matches = logLines.Where(line => line.Contains(pattern)).ToList();  
        return Ok(new { success = true, matches });  
    }  
    catch (Exception ex)  
    {  
        return StatusCode(500, new { success = false, error = ex.Message });  
    }  
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 7
```python
def search_logs(pattern: str) -> dict:  
    try:  
        with open('/var/logs/app.log', 'r') as f:  
            matches = [line for line in f if pattern in line]  
        return {"success": True, "matches": matches}  
    except Exception as e:  
        return {"success": False, "error": str(e)}
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 11
```typescript
import fs from 'fs/promises';  

async function searchLogs(pattern: string): Promise<object> {  
    try {  
        const logContent = await fs.readFile('/var/logs/app.log', 'utf-8');  
        const matches = logContent.split('\n').filter(line => line.includes(pattern));  
        return { success: true, matches };  
    } catch (error) {  
        return { success: false, error: error.message };  
    }  
}
```

### 🧪 Senaryo 3: Bir sistem izleme uygulamasında kullanıcılar süreç adı girip sistem durumunu kontrol edebilir. Uygulama girilen süreç adını kullanarak sistem komutları çalıştırır. Süreç bilgileri kullanıcıya gösterilir. İzleme işlemi gerçek zamanlı olarak yapılır.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 14
```csharp
[HttpGet("check-process")]  
public IActionResult CheckProcess(string processName)  
{  
    try  
    {  
        var processes = System.Diagnostics.Process.GetProcessesByName(processName);  
        return Ok(new {  
            success = true,  
            isRunning = processes.Length > 0,  
            count = processes.Length  
        });  
    }  
    catch (Exception ex)  
    {  
        return StatusCode(500, new { success = false, error = ex.Message });  
    }  
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 12
```python
import psutil  

def check_process(process_name: str) -> dict:  
    try:  
        processes = [p for p in psutil.process_iter(['name']) if p.info['name'] == process_name]  
        return {  
            "success": True,  
            "isRunning": len(processes) > 0,  
            "count": len(processes)  
        }  
    except Exception as e:  
        return {"success": False, "error": str(e)}
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 17
```typescript
import { exec } from 'child_process';  
import { promisify } from 'util';  

const execAsync = promisify(exec);  

async function checkProcess(processName: string): Promise<object> {  
    try {  
        const { stdout } = await execAsync(`pgrep -f ${processName} | wc -l`);  
        const count = parseInt(stdout.trim());  
        return {  
            success: true,  
            isRunning: count > 0,  
            count  
        };  
    } catch (error) {  
        return { success: false, error: error.message };  
    }  
}
```

### 🧪 Senaryo 4: Bir backup yönetim aracında kullanıcılar yedekleme dizini belirtebilir. Sistem belirtilen dizini kullanarak yedekleme komutları çalıştırır. Yedekleme durumu kullanıcıya raporlanır. İşlem tamamlandığında sonuç gösterilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 18
```csharp
[HttpPost("create-backup")]  
public IActionResult CreateBackup(string sourcePath)  
{  
    try  
    {  
        string backupDir = $"/backups/{DateTime.Now:yyyyMMddHHmmss}";  
        Directory.CreateDirectory(backupDir);  

        foreach (var file in Directory.GetFiles(sourcePath))  
        {  
            File.Copy(file, Path.Combine(backupDir, Path.GetFileName(file)));  
        }  

        return Ok(new { success = true, backupPath = backupDir });  
    }  
    catch (Exception ex)  
    {  
        return StatusCode(500, new { success = false, error = ex.Message });  
    }  
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 18
```python
import shutil  
import os  
from datetime import datetime  

def create_backup(source_path: str) -> dict:  
    try:  
        backup_dir = f"/backups/{datetime.now().strftime('%Y%m%d%H%M%S')}"  
        os.makedirs(backup_dir)  

        for item in os.listdir(source_path):  
            s = os.path.join(source_path, item)  
            d = os.path.join(backup_dir, item)  
            if os.path.isdir(s):  
                shutil.copytree(s, d)  
            else:  
                shutil.copy2(s, d)  

        return {"success": True, "backupPath": backup_dir}  
    except Exception as e:  
        return {"success": False, "error": str(e)}
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 18
```typescript
import fs from 'fs/promises';  
import path from 'path';  

async function createBackup(sourcePath: string): Promise<object> {  
    try {  
        const backupDir = `/backups/${new Date().toISOString().replace(/[:.]/g, '-')}`;  
        await fs.mkdir(backupDir);  

        const files = await fs.readdir(sourcePath);  
        await Promise.all(files.map(async file => {  
            const src = path.join(sourcePath, file);  
            const dest = path.join(backupDir, file);  
            await fs.copyFile(src, dest);  
        }));  

        return { success: true, backupPath: backupDir };  
    } catch (error) {  
        return { success: false, error: error.message };  
    }  
}
```

### 🧪 Senaryo 5: Bir ağ test uygulamasında kullanıcılar IP adresi girip bağlantı testi yapabilir. Sistem girilen IP adresini kullanarak ping komutları çalıştırır. Test sonuçları kullanıcıya gösterilir. Ağ durumu analiz edilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 20
```csharp
[HttpGet("ping")]  
public async Task<IActionResult> PingHost(string host)  
{  
    try  
    {  
        using var ping = new System.Net.NetworkInformation.Ping();  
        var reply = await ping.SendPingAsync(host);  

        if (reply.Status == System.Net.NetworkInformation.IPStatus.Success)  
        {  
            return Ok(new { success = true, status = "Success", roundtripTime = reply.RoundtripTime });  
        }  
        else  
        {  
            return Ok(new { success = false, status = reply.Status.ToString() });  
        }  
    }  
    catch (Exception ex)  
    {  
        return StatusCode(500, new { success = false, error = ex.Message });  
    }  
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 9
```python
import subprocess  

def ping_host(host: str) -> dict:  
    try:  
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)  
        return {"success": True, "output": result.stdout}  
    except subprocess.CalledProcessError as e:  
        return {"success": False, "error": e.stderr}  
    except Exception as e:  
        return {"success": False, "error": str(e)}
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 14
```typescript
import { exec } from 'child_process';  
import { promisify } from 'util';  

const execAsync = promisify(exec);  

async function pingHost(host: string): Promise<object> {  
    try {  
        const { stdout, stderr } = await execAsync(`ping -c 4 ${host}`);  
        if (stderr) {  
            return { success: false, error: stderr };  
        }  
        return { success: true, output: stdout };  
    } catch (error) {  
        return { success: false, error: error.message };  
    }  
}
```

### 🧪 Senaryo 6: Bir dosya dönüştürme uygulamasında kullanıcılar kaynak ve hedef dosya yollarını belirtir. Sistem bu yolları kullanarak dönüştürme komutları çalıştırır. Dönüştürülen dosyalar kullanıcıya sunulur. Çeşitli format dönüştürmeleri desteklenir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 15
```csharp
[HttpPost("convert-file")]  
public async Task<IActionResult> ConvertFile(string sourceFile, string destFile)  
{  
    try  
    {  
        var processInfo = new System.Diagnostics.ProcessStartInfo("ffmpeg", $"-i {sourceFile} {destFile}");  
        processInfo.RedirectStandardOutput = true;  
        processInfo.UseShellExecute = false;  
        var process = System.Diagnostics.Process.Start(processInfo);  
        await process.WaitForExitAsync();  
        return Ok(new { success = true, message = "Conversion completed." });  
    }  
    catch (Exception ex)  
    {  
        return StatusCode(500, new { success = false, error = ex.Message });  
    }  
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 9
```python
import subprocess  

def convert_file(source_file: str, dest_file: str) -> dict:  
    try:  
        subprocess.run(['ffmpeg', '-i', source_file, dest_file], check=True)  
        return {"success": True, "message": "Conversion completed."}  
    except subprocess.CalledProcessError as e:  
        return {"success": False, "error": str(e)}  
    except Exception as e:  
        return {"success": False, "error": str(e)}
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 12
```typescript
import { exec } from 'child_process';  
import { promisify } from 'util';  

const execAsync = promisify(exec);  

async function convertFile(sourceFile: string, destFile: string): Promise<object> {  
    try {  
        await execAsync(`ffmpeg -i ${sourceFile} ${destFile}`);  
        return { success: true, message: "Conversion completed." };  
    } catch (error) {  
        return { success: false, error: error.message };  
    }  
}
```

### 🧪 Senaryo 7: Bir disk alanı analiz aracında kullanıcılar dizin yolu girip alan kullanımını görebilir. Sistem girilen yolu kullanarak analiz komutları çalıştırır. Alan kullanım raporu oluşturulur. Sonuçlar grafik olarak gösterilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 11
```csharp
[HttpGet("disk-usage")]  
public IActionResult GetDiskUsage(string path)  
{  
    try  
    {  
        var driveInfo = new DriveInfo(path);  
        return Ok(new { success = true, total = driveInfo.TotalSize, free = driveInfo.AvailableFreeSpace });  
    }  
    catch (Exception ex)  
    {  
        return StatusCode(500, new { success = false, error = ex.Message });  
    }  
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 7
```python
import shutil  

def get_disk_usage(path: str) -> dict:  
    try:  
        total, used, free = shutil.disk_usage(path)  
        return {"success": True, "total": total, "used": used, "free": free}  
    except Exception as e:  
        return {"success": False, "error": str(e)}
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 12
```typescript
import { exec } from 'child_process';  
import { promisify } from 'util';  

const execAsync = promisify(exec);  

async function getDiskUsage(path: string): Promise<object> {  
    try {  
        const { stdout } = await execAsync(`df -k ${path}`);  
        return { success: true, usage: stdout };  
    } catch (error) {  
        return { success: false, error: error.message };  
    }  
}
```

### 🧪 Senaryo 8: Bir veritabanı yedekleme uygulamasında kullanıcılar veritabanı adını girebilir. Sistem girilen adı kullanarak backup komutları çalıştırır. Yedekleme işlemi gerçekleştirilir. Yedek dosyaları belirtilen konuma kaydedilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 15
```csharp
[HttpPost("backup-db")]  
public async Task<IActionResult> BackupDatabase(string dbName)  
{  
    try  
    {  
        string backupFile = $"/backups/db_{dbName}_{DateTime.Now:yyyyMMdd}.sql";  
        var processInfo = new System.Diagnostics.ProcessStartInfo("pg_dump", $"-U user -d {dbName} -f {backupFile}");  
        processInfo.RedirectStandardOutput = true;  
        processInfo.UseShellExecute = false;  
        var process = System.Diagnostics.Process.Start(processInfo);  
        await process.WaitForExitAsync();  
        return Ok(new { success = true, message = "Database backup completed.", backupFile });  
    }  
    catch (Exception ex)  
    {  
        return StatusCode(500, new { success = false, error = ex.Message });  
    }  
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 10
```python
import subprocess  
from datetime import datetime  

def backup_database(db_name: str) -> dict:  
    try:  
        backup_file = f"/backups/db_{db_name}_{datetime.now().strftime('%Y%m%d')}.sql"  
        subprocess.run(['pg_dump', '-U', 'user', '-d', db_name, '-f', backup_file], check=True)  
        return {"success": True, "message": "Database backup completed.", "backupFile": backup_file}  
    except Exception as e:  
        return {"success": False, "error": str(e)}
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 13
```typescript
import { exec } from 'child_process';  
import { promisify } from 'util';  

const execAsync = promisify(exec);  

async function backupDatabase(dbName: string): Promise<object> {  
    try {  
        const backupFile = `/backups/db_${dbName}_${new Date().toISOString().slice(0, 10)}.sql`;  
        await execAsync(`pg_dump -U user -d ${dbName} -f ${backupFile}`);  
        return { success: true, message: "Database backup completed.", backupFile };  
    } catch (error) {  
        return { success: false, error: error.message };  
    }  
}
```

### 🧪 Senaryo 9: Bir mail sunucu yönetimi aracında kullanıcılar posta kutusu adını girip durum kontrolü yapabilir. Sistem girilen adı kullanarak mail sistem komutları çalıştırır. Posta kutusu bilgileri gösterilir. Mail trafiği analiz edilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 15
```csharp
[HttpGet("check-mailbox")]  
public async Task<IActionResult> CheckMailbox(string mailboxName)  
{  
    try  
    {  
        var processInfo = new System.Diagnostics.ProcessStartInfo("mailq", $"-A | grep {mailboxName}");  
        processInfo.RedirectStandardOutput = true;  
        processInfo.UseShellExecute = false;  
        var process = System.Diagnostics.Process.Start(processInfo);  
        var output = await process.StandardOutput.ReadToEndAsync();  
        await process.WaitForExitAsync();  
        return Ok(new { success = true, output });  
    }  
    catch (Exception ex)  
    {  
        return StatusCode(500, new { success = false, error = ex.Message });  
    }  
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 9
```python
import subprocess  

def check_mailbox(mailbox_name: str) -> dict:  
    try:  
        result = subprocess.run(['mailq', '-A'], capture_output=True, text=True, check=True)  
        output = [line for line in result.stdout.split('\n') if mailbox_name in line]  
        return {"success": True, "output": output}  
    except Exception as e:  
        return {"success": False, "error": str(e)}
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 13
```typescript
import { exec } from 'child_process';  
import { promisify } from 'util';  

const execAsync = promisify(exec);  

async function checkMailbox(mailboxName: string): Promise<object> {  
    try {  
        const { stdout } = await execAsync('mailq -A');  
        const output = stdout.split('\n').filter(line => line.includes(mailboxName));  
        return { success: true, output };  
    } catch (error) {  
        return { success: false, error: error.message };  
    }  
}
```

### 🧪 Senaryo 10: Bir web sunucu log analiz uygulamasında kullanıcılar tarih aralığı girip log verilerini filtreleyebilir. Sistem girilen tarihleri kullanarak filtreleme komutları çalıştırır. Filtrelenmiş loglar kullanıcıya sunulur. Analiz raporları oluşturulur.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 13
```csharp
[HttpGet("filter-logs")]  
public async Task<IActionResult> FilterLogsByDate(string startDate, string endDate)  
{  
    try  
    {  
        // Bu örnek basittir ve idealde log formatına göre daha sağlam bir ayrıştırma gerektirir.  
        var logLines = await File.ReadAllLinesAsync("/var/logs/access.log");  
        var filtered = logLines.Where(line => {  
            // Örnek: "2023-10-27 ...", varsayımsal bir log formatı  
            return line.StartsWith(startDate) || line.StartsWith(endDate);  
        }).ToList();  
        return Ok(new { success = true, logs = filtered });  
    }  
    catch (Exception ex)  
    {  
        return StatusCode(500, new { success = false, error = ex.Message });  
    }  
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 9
```python
def filter_logs_by_date(start_date: str, end_date: str) -> dict:  
    try:  
        with open('/var/logs/access.log', 'r') as f:  
            filtered_logs = [line for line in f if line.startswith(start_date) or line.startswith(end_date)]  
        return {"success": True, "logs": filtered_logs}  
    except Exception as e:  
        return {"success": False, "error": str(e)}
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 12
```typescript
import fs from 'fs/promises';  

async function filterLogsByDate(startDate: string, endDate: string): Promise<object> {  
    try {  
        const logContent = await fs.readFile('/var/logs/access.log', 'utf-8');  
        const filteredLogs = logContent.split('\n').filter(line => line.startsWith(startDate) || line.startsWith(endDate));  
        return { success: true, logs: filteredLogs };  
    } catch (error) {  
        return { success: false, error: error.message };  
    }  
}
```