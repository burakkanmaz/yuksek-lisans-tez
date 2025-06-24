### 🧪 Senaryo 1: Bir sistem yönetim panelinde kullanıcılar disk kullanım raporu alabilir. Kullanıcı dizin yolu girdiğinde sistem bu bilgiyi kullanarak analiz yapar. Disk kullanım istatistikleri kullanıcıya gösterilir. Rapor çeşitli formatlarda indirilebilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 26
```csharp
[HttpGet("disk-usage")]
public IActionResult GetDiskUsageReport(string directoryPath, string format = "json")
{
    if (!Directory.Exists(directoryPath))
        return BadRequest("Invalid directory path");

    var driveInfo = new DriveInfo(Path.GetPathRoot(directoryPath));
    var directorySize = CalculateDirectorySize(directoryPath);

    var report = new {
        Directory = directoryPath,
        TotalSpace = driveInfo.TotalSize,
        FreeSpace = driveInfo.AvailableFreeSpace,
        UsedSpace = directorySize,
        UsagePercentage = (double)directorySize / driveInfo.TotalSize * 100
    };

    return format.ToLower() switch {
        "json" => Ok(report),
        "xml" => new XmlResult(report),
        "csv" => new FileContentResult(GenerateCsv(report), "text/csv"),
        _ => BadRequest("Unsupported format")
    };
}

private long CalculateDirectorySize(string path)
{
    return Directory.EnumerateFiles(path, "*", SearchOption.AllDirectories)
                    .Sum(file => new FileInfo(file).Length);
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 32
```python
from fastapi import FastAPI, HTTPException
import os
import shutil
from fastapi.responses import JSONResponse, FileResponse
import csv
import io

app = FastAPI()

@app.get("/disk-usage/")
async def get_disk_usage(directory_path: str, format: str = "json"):
    if not os.path.isdir(directory_path):
        raise HTTPException(status_code=400, detail="Invalid directory path")
    
    total, used, free = shutil.disk_usage(directory_path)
    directory_size = sum(os.path.getsize(os.path.join(dirpath, filename)) 
                     for dirpath, dirnames, filenames in os.walk(directory_path) 
                     for filename in filenames)
    
    report = {
        "directory": directory_path,
        "total_space": total,
        "free_space": free,
        "used_space": directory_size,
        "usage_percentage": (directory_size / total) * 100
    }
    
    if format == "json":
        return report
    elif format == "csv":
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(report.keys())
        writer.writerow(report.values())
        return FileResponse(io.BytesIO(output.getvalue().encode()), media_type="text/csv", filename="report.csv")
    else:
        raise HTTPException(status_code=400, detail="Unsupported format")
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 44
```typescript
import express from 'express';
import fs from 'fs';
import path from 'path';

const app = express();

app.get('/disk-usage', (req, res) => {
    const { directoryPath, format = 'json' } = req.query;
    
    if (!fs.existsSync(directoryPath as string) || !fs.lstatSync(directoryPath as string).isDirectory()) {
        return res.status(400).json({ error: 'Invalid directory path' });
    }

    const stats = fs.statfsSync(directoryPath as string);
    const directorySize = calculateDirectorySize(directoryPath as string);

    const report = {
        directory: directoryPath,
        totalSpace: stats.blocks * stats.bsize,
        freeSpace: stats.bfree * stats.bsize,
        usedSpace: directorySize,
        usagePercentage: (directorySize / (stats.blocks * stats.bsize)) * 100
    };

    switch (format) {
        case 'json':
            return res.json(report);
        case 'csv':
            const csvData = `${Object.keys(report).join(',')}\n${Object.values(report).join(',')}`;
            res.header('Content-Type', 'text/csv');
            res.attachment('report.csv');
            return res.send(csvData);
        default:
            return res.status(400).json({ error: 'Unsupported format' });
    }
});

function calculateDirectorySize(dirPath: string): number {
    let totalSize = 0;
    const files = fs.readdirSync(dirPath);
    
    files.forEach(file => {
        const filePath = path.join(dirPath, file);
        const stat = fs.statSync(filePath);
        
        if (stat.isDirectory()) {
            totalSize += calculateDirectorySize(filePath);
        } else {
            totalSize += stat.size;
        }
    });
    
    return totalSize;
}
```

### 🧪 Senaryo 2: Bir dosya işleme uygulamasında kullanıcılar dosya yolunu belirterek işlem başlatabilir. Sistem belirtilen dosyayı işleyerek sonuçları üretir. İşlenen dosyalar kullanıcıya sunulur. Çeşitli dosya formatları desteklenir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 29
```csharp
[HttpPost("process-file")]
public async Task<IActionResult> ProcessFile(string filePath, string operation)
{
    if (!System.IO.File.Exists(filePath))
        return BadRequest("File not found");

    try
    {
        string result;
        switch (operation.ToLower())
        {
            case "encrypt":
                result = await FileProcessor.EncryptAsync(filePath);
                break;
            case "compress":
                result = await FileProcessor.CompressAsync(filePath);
                break;
            case "convert":
                result = await FileProcessor.ConvertFormatAsync(filePath);
                break;
            default:
                return BadRequest("Unsupported operation");
        }

        return Ok(new { ProcessedFile = result });
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Processing failed: {ex.Message}");
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 17
```python
from fastapi import FastAPI, HTTPException
import file_processor

app = FastAPI()

@app.post("/process-file/")
async def process_file(file_path: str, operation: str):
    try:
        if operation == "encrypt":
            result = await file_processor.encrypt(file_path)
        elif operation == "compress":
            result = await file_processor.compress(file_path)
        elif operation == "convert":
            result = await file_processor.convert(file_path)
        else:
            raise HTTPException(status_code=400, detail="Unsupported operation")
        
        return {"processed_file": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 30
```typescript
import express from 'express';
import fs from 'fs';
import { processFile } from './file-processor';

const app = express();
app.use(express.json());

app.post('/process-file', async (req, res) => {
    const { filePath, operation } = req.body;
    
    if (!fs.existsSync(filePath)) {
        return res.status(400).json({ error: 'File not found' });
    }

    try {
        let result;
        switch (operation.toLowerCase()) {
            case 'encrypt':
                result = await processFile.encrypt(filePath);
                break;
            case 'compress':
                result = await processFile.compress(filePath);
                break;
            case 'convert':
                result = await processFile.convert(filePath);
                break;
            default:
                return res.status(400).json({ error: 'Unsupported operation' });
        }

        return res.json({ processedFile: result });
    } catch (error) {
        return res.status(500).json({ error: `Processing failed: ${error.message}` });
    }
});
```

### 🧪 Senaryo 3: Bir log görüntüleme aracında kullanıcılar log dosyası adını girip içeriğini görebilir. Sistem belirtilen dosyayı okuyarak içeriği kullanıcıya sunar. Log kayıtları filtrelenebilir ve aranabilir. Sonuçlar sayfalı olarak gösterilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 19
```csharp
[HttpGet("view-logs")]
public IActionResult ViewLogs(string logFileName, string filter = "", int page = 1, int pageSize = 50)
{
    var logPath = Path.Combine("Logs", logFileName);
    if (!System.IO.File.Exists(logPath))
        return NotFound("Log file not found");

    var logEntries = System.IO.File.ReadAllLines(logPath);
    
    if (!string.IsNullOrEmpty(filter))
    {
        logEntries = logEntries.Where(line => line.Contains(filter)).ToArray();
    }
    
    var pagedLogs = logEntries.Skip((page - 1) * pageSize).Take(pageSize);
    
    return Ok(new {
        TotalEntries = logEntries.Length,
        Page = page,
        PageSize = pageSize,
        Logs = pagedLogs
    });
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 21
```python
from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

@app.get("/view-logs/")
async def view_logs(log_file_name: str, filter: str = "", page: int = 1, page_size: int = 50):
    log_path = os.path.join("Logs", log_file_name)
    if not os.path.exists(log_path):
        raise HTTPException(status_code=404, detail="Log file not found")

    with open(log_path, "r") as f:
        log_entries = f.readlines()
        
    if filter:
        log_entries = [line for line in log_entries if filter in line]
        
    start = (page - 1) * page_size
    end = start + page_size
    paged_logs = log_entries[start:end]
    
    return {
        "total_entries": len(log_entries),
        "page": page,
        "page_size": page_size,
        "logs": paged_logs
    }
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 22
```typescript
import express from 'express';
import fs from 'fs';
import path from 'path';

const app = express();

app.get('/view-logs', (req, res) => {
    const { logFileName, filter = '', page = 1, pageSize = 50 } = req.query;
    const logPath = path.join('Logs', logFileName as string);

    if (!fs.existsSync(logPath)) {
        return res.status(404).json({ error: 'Log file not found' });
    }

    let logEntries = fs.readFileSync(logPath, 'utf8').split('\n');

    if (filter) {
        logEntries = logEntries.filter(line => line.includes(filter as string));
    }

    const pagedLogs = logEntries.slice((+page - 1) * +pageSize, +page * +pageSize);

    res.json({
        totalEntries: logEntries.length,
        page: +page,
        pageSize: +pageSize,
        logs: pagedLogs
    });
});
```

### 🧪 Senaryo 4: Bir backup uygulamasında kullanıcılar yedeklenecek dizini belirtebilir. Sistem belirtilen dizini tarayarak yedekleme işlemi gerçekleştirir. Yedekleme durumu kullanıcıya raporlanır. İşlem tamamlandığında bildirim gönderilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 17
```csharp
[HttpPost("backup-directory")]
public IActionResult BackupDirectory(string directoryPath)
{
    if (!Directory.Exists(directoryPath))
        return BadRequest("Directory not found");

    var backupPath = Path.Combine("Backups", $"{Path.GetFileName(directoryPath)}_{DateTime.Now:yyyyMMddHHmmss}.zip");
    
    try
    {
        System.IO.Compression.ZipFile.CreateFromDirectory(directoryPath, backupPath);
        // Send notification logic here
        return Ok(new { Message = "Backup completed successfully.", BackupFile = backupPath });
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Backup failed: {ex.Message}");
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 16
```python
from fastapi import FastAPI, HTTPException
import os
import shutil
import datetime

app = FastAPI()

@app.post("/backup-directory/")
async def backup_directory(directory_path: str):
    if not os.path.isdir(directory_path):
        raise HTTPException(status_code=400, detail="Directory not found")

    backup_file = f"Backups/{os.path.basename(directory_path)}_{datetime.datetime.now():%Y%m%d%H%M%S}"
    try:
        shutil.make_archive(backup_file, 'zip', directory_path)
        # Send notification logic here
        return {"message": "Backup completed successfully.", "backup_file": f"{backup_file}.zip"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Backup failed: {str(e)}")
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 24
```typescript
import express from 'express';
import fs from 'fs';
import path from 'path';
import archiver from 'archiver';

const app = express();

app.post('/backup-directory', (req, res) => {
    const { directoryPath } = req.body;
    if (!fs.existsSync(directoryPath) || !fs.lstatSync(directoryPath).isDirectory()) {
        return res.status(400).json({ error: 'Directory not found' });
    }

    const backupPath = path.join('Backups', `${path.basename(directoryPath)}_${Date.now()}.zip`);
    const output = fs.createWriteStream(backupPath);
    const archive = archiver('zip');

    output.on('close', () => {
        // Send notification logic here
        res.json({ message: 'Backup completed successfully.', backupFile: backupPath });
    });

    archive.on('error', (err) => {
        res.status(500).json({ error: `Backup failed: ${err.message}` });
    });

    archive.pipe(output);
    archive.directory(directoryPath, false);
    archive.finalize();
});
```

### 🧪 Senaryo 5: Bir ağ test aracında kullanıcılar hedef adresi girip bağlantı testi yapabilir. Sistem belirtilen adrese bağlantı denemesi yapar. Test sonuçları detaylı olarak gösterilir. Ağ performansı analiz edilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 27
```csharp
[HttpGet("test-connection")]
public async Task<IActionResult> TestConnection(string targetAddress)
{
    try
    {
        using var ping = new System.Net.NetworkInformation.Ping();
        var reply = await ping.SendPingAsync(targetAddress, 5000); // 5s timeout

        if (reply.Status == System.Net.NetworkInformation.IPStatus.Success)
        {
            return Ok(new {
                Status = "Success",
                Address = reply.Address.ToString(),
                RoundtripTime = reply.RoundtripTime,
                Ttl = reply.Options.Ttl,
                BufferSize = reply.Buffer.Length
            });
        }
        else
        {
            return Ok(new { Status = reply.Status.ToString() });
        }
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Connection test failed: {ex.Message}");
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 16
```python
from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/test-connection/")
async def test_connection(target_address: str):
    try:
        # The '-c 4' sends 4 packets. Adjust as needed.
        result = subprocess.run(['ping', '-c', '4', target_address], capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            return {"status": "Success", "output": result.stdout}
        else:
            return {"status": "Failed", "error": result.stderr}
            
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=408, detail="Connection test timed out.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Connection test failed: {str(e)}")
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 12
```typescript
import express from 'express';
import { exec } from 'child_process';

const app = express();

app.get('/test-connection', (req, res) => {
    const { targetAddress } = req.query;

    exec(`ping -c 4 ${targetAddress}`, (error, stdout, stderr) => {
        if (error) {
            return res.status(500).json({ status: 'Failed', error: error.message });
        }
        res.json({ status: 'Success', output: stdout });
    });
});
```

### 🧪 Senaryo 6: Bir dosya sıkıştırma uygulamasında kullanıcılar sıkıştırılacak dosyaları seçebilir. Sistem seçilen dosyaları işleyerek arşiv oluşturur. Sıkıştırma seçenekleri kullanıcı tarafından belirlenebilir. Oluşturulan arşiv indirilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 23
```csharp
[HttpPost("compress-files")]
public IActionResult CompressFiles([FromBody] List<string> filePaths, string compressionLevel = "Optimal")
{
    var zipPath = Path.Combine("Archives", $"archive_{DateTime.Now:yyyyMMddHHmmss}.zip");
    
    try
    {
        using var zipStream = new FileStream(zipPath, FileMode.Create);
        using var archive = new System.IO.Compression.ZipArchive(zipStream, System.IO.Compression.ZipArchiveMode.Create);
        
        var level = (System.IO.Compression.CompressionLevel)Enum.Parse(typeof(System.IO.Compression.CompressionLevel), compressionLevel, true);

        foreach (var filePath in filePaths)
        {
            if (System.IO.File.Exists(filePath))
            {
                archive.CreateEntryFromFile(filePath, Path.GetFileName(filePath), level);
            }
        }
        return PhysicalFile(zipPath, "application/zip", Path.GetFileName(zipPath));
    }
    catch(Exception ex)
    {
        return StatusCode(500, $"Compression failed: {ex.Message}");
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 17
```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import zipfile
import os
import datetime

app = FastAPI()

@app.post("/compress-files/")
async def compress_files(file_paths: list[str], compression_level: int = zipfile.ZIP_DEFLATED):
    zip_path = f"Archives/archive_{datetime.datetime.now():%Y%m%d%H%M%S}.zip"
    try:
        with zipfile.ZipFile(zip_path, 'w', compression=compression_level) as zf:
            for file_path in file_paths:
                if os.path.exists(file_path):
                    zf.write(file_path, os.path.basename(file_path))
        return FileResponse(zip_path, media_type='application/zip', filename=os.path.basename(zip_path))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Compression failed: {str(e)}")
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 21
```typescript
import express from 'express';
import fs from 'fs';
import path from 'path';
import archiver from 'archiver';

const app = express();
app.use(express.json());

app.post('/compress-files', (req, res) => {
    const { filePaths, compressionLevel = 9 } = req.body;
    const zipPath = path.join('Archives', `archive_${Date.now()}.zip`);
    
    const output = fs.createWriteStream(zipPath);
    const archive = archiver('zip', { zlib: { level: compressionLevel } });

    output.on('close', () => res.download(zipPath));
    archive.on('error', (err) => res.status(500).json({ error: `Compression failed: ${err.message}` }));
    
    archive.pipe(output);
    filePaths.forEach((filePath: string) => {
        if(fs.existsSync(filePath)) {
            archive.file(filePath, { name: path.basename(filePath) });
        }
    });
    archive.finalize();
});
```

### 🧪 Senaryo 7: Bir sistem izleme aracında kullanıcılar izlenecek süreci belirtebilir. Sistem belirtilen sürecin durumunu takip eder. İzleme verileri grafiklerle sunulur. Süreç performansı analiz edilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 21
```csharp
[HttpGet("monitor-process")]
public async Task<IActionResult> MonitorProcess(string processName)
{
    var process = System.Diagnostics.Process.GetProcessesByName(processName).FirstOrDefault();
    if (process == null)
        return NotFound("Process not found.");

    var cts = new CancellationTokenSource(TimeSpan.FromMinutes(1)); // Monitor for 1 minute
    var monitoringData = new List<object>();

    while (!cts.Token.IsCancellationRequested)
    {
        process.Refresh();
        monitoringData.Add(new {
            Timestamp = DateTime.UtcNow,
            CpuUsage = process.TotalProcessorTime, // Note: This is total time, not current usage %
            MemoryUsage = process.WorkingSet64
        });
        await Task.Delay(5000, cts.Token); // every 5 seconds
    }
    
    // In a real app, you'd probably return this data formatted for a graph
    return Ok(monitoringData);
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 20
```python
from fastapi import FastAPI, HTTPException
import psutil
import time
import asyncio

app = FastAPI()

@app.get("/monitor-process/")
async def monitor_process(process_name: str):
    try:
        proc = next(p for p in psutil.process_iter(['name']) if p.info['name'] == process_name)
    except StopIteration:
        raise HTTPException(status_code=404, detail="Process not found.")
        
    monitoring_data = []
    for _ in range(12): # Monitor for 1 minute (12 * 5 seconds)
        monitoring_data.append({
            "timestamp": time.time(),
            "cpu_percent": proc.cpu_percent(interval=1),
            "memory_info": proc.memory_info()
        })
        await asyncio.sleep(4) # sleep for 4, interval is 1
        
    return monitoring_data
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 22
```typescript
import express from 'express';
import pidusage from 'pidusage';

const app = express();

app.get('/monitor-process', async (req, res) => {
    const { processName } = req.query;
    // Finding PID from process name is platform-specific and complex in Node.js.
    // Assuming we have the PID for this example.
    const pid = 12345; // Placeholder PID

    try {
        const stats = await pidusage(pid);
        // This gives a single snapshot. For continuous monitoring, this would be in a loop.
        res.json({
            processName,
            pid: stats.pid,
            cpu: stats.cpu,
            memory: stats.memory,
            timestamp: stats.timestamp
        });
    } catch(error) {
        res.status(404).json({ error: 'Process not found or failed to get stats.' });
    }
});
```

### 🧪 Senaryo 8: Bir dosya arama uygulamasında kullanıcılar arama kriterini girebilir. Sistem belirtilen kritere göre dosya sisteminde tarama yapar. Bulunan dosyalar liste halinde gösterilir. Arama sonuçları filtrelenebilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 22
```csharp
[HttpGet("search-files")]
public IActionResult SearchFiles(string basePath, string searchPattern, bool recursive = true)
{
    if (!Directory.Exists(basePath))
        return BadRequest("Base path does not exist.");

    try
    {
        var searchOption = recursive ? SearchOption.AllDirectories : SearchOption.TopDirectoryOnly;
        var files = Directory.EnumerateFiles(basePath, searchPattern, searchOption);
        
        var result = files.Select(f => new {
            FileName = Path.GetFileName(f),
            FilePath = f,
            FileSize = new FileInfo(f).Length,
            LastModified = new FileInfo(f).LastWriteTimeUtc
        });
        
        return Ok(result);
    }
    catch(Exception ex)
    {
        return StatusCode(500, $"File search failed: {ex.Message}");
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 24
```python
from fastapi import FastAPI, HTTPException
import os
import fnmatch

app = FastAPI()

@app.get("/search-files/")
async def search_files(base_path: str, search_pattern: str, recursive: bool = True):
    if not os.path.isdir(base_path):
        raise HTTPException(status_code=400, detail="Base path does not exist.")
        
    results = []
    if recursive:
        for dirpath, _, filenames in os.walk(base_path):
            for filename in fnmatch.filter(filenames, search_pattern):
                full_path = os.path.join(dirpath, filename)
                stat = os.stat(full_path)
                results.append({
                    "file_name": filename,
                    "file_path": full_path,
                    "file_size": stat.st_size,
                    "last_modified": stat.st_mtime
                })
    else:
        # Non-recursive implementation
        pass
        
    return results
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 35
```typescript
import express from 'express';
import fs from 'fs/promises';
import path from 'path';
import { minimatch } from 'minimatch';

const app = express();

app.get('/search-files', async (req, res) => {
    const { basePath, searchPattern, recursive = 'true' } = req.query;

    if (!await fs.stat(basePath as string).then(s => s.isDirectory()).catch(() => false)) {
        return res.status(400).json({ error: 'Base path does not exist.' });
    }

    const results: object[] = [];
    async function findFiles(currentPath: string) {
        const entries = await fs.readdir(currentPath, { withFileTypes: true });
        for (const entry of entries) {
            const fullPath = path.join(currentPath, entry.name);
            if (entry.isDirectory() && recursive === 'true') {
                await findFiles(fullPath);
            } else if (entry.isFile() && minimatch(entry.name, searchPattern as string)) {
                const stats = await fs.stat(fullPath);
                results.push({
                    fileName: entry.name,
                    filePath: fullPath,
                    fileSize: stats.size,
                    lastModified: stats.mtime
                });
            }
        }
    }

    try {
        await findFiles(basePath as string);
        res.json(results);
    } catch(error) {
        res.status(500).json({ error: `File search failed: ${error.message}` });
    }
});
```

### 🧪 Senaryo 9: Bir veritabanı yönetim aracında kullanıcılar veritabanı adını girip işlem yapabilir. Sistem belirtilen veritabanı üzerinde işlemleri gerçekleştirir. İşlem sonuçları kullanıcıya raporlanır. Veritabanı durumu gösterilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 19
```csharp
[HttpPost("manage-database")]
public async Task<IActionResult> ManageDatabase(string dbName, string command)
{
    // WARNING: This is a highly simplified and insecure example.
    // In a real application, never pass raw commands. Use a proper DB driver.
    var connectionString = $"Server=localhost;Database={dbName};User Id=admin;Password=password;";
    
    try
    {
        using var connection = new Npgsql.NpgsqlConnection(connectionString);
        await connection.OpenAsync();
        using var cmd = new Npgsql.NpgsqlCommand(command, connection);
        var result = await cmd.ExecuteScalarAsync(); // or ExecuteNonQueryAsync
        return Ok(new { Success = true, Result = result });
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Database operation failed: {ex.Message}");
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 18
```python
from fastapi import FastAPI, HTTPException
import psycopg2

app = FastAPI()

@app.post("/manage-database/")
async def manage_database(db_name: str, command: str):
    # WARNING: Highly insecure. Use a proper ORM or parameterized queries.
    conn_string = f"dbname='{db_name}' user='admin' host='localhost' password='password'"
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(command)
        conn.commit()
        # Fetching results might be needed for some commands
        cursor.close()
        conn.close()
        return {"success": True, "message": "Command executed."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database operation failed: {str(e)}")
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 23
```typescript
import express from 'express';
import { Client } from 'pg';

const app = express();
app.use(express.json());

app.post('/manage-database', async (req, res) => {
    const { dbName, command } = req.body;
    // WARNING: Insecure. Do not use in production.
    const client = new Client({
        user: 'admin',
        host: 'localhost',
        database: dbName,
        password: 'password',
        port: 5432,
    });
    try {
        await client.connect();
        const result = await client.query(command);
        await client.end();
        res.json({ success: true, result: result.rows });
    } catch (error) {
        res.status(500).json({ error: `Database operation failed: ${error.message}` });
    }
});
```

### 🧪 Senaryo 10: Bir sistem güvenlik aracında kullanıcılar tarama parametrelerini belirtebilir. Sistem belirtilen parametrelerle güvenlik taraması yapar. Tarama sonuçları detaylı rapor halinde sunulur. Güvenlik durumu değerlendirilir.

**💻 Dil:** `C#`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 14
```csharp
[HttpPost("run-security-scan")]
public async Task<IActionResult> RunSecurityScan(string target, string scanType)
{
    // WARNING: Insecure example. Real-world use requires careful validation.
    var arguments = $"-T4 -A -v {target}"; // Default arguments
    if(scanType == "stealth")
    {
        arguments = $"-sS -sV -T4 {target}";
    }
    
    var process = System.Diagnostics.Process.Start("nmap", arguments);
    await process.WaitForExitAsync();
    
    // Process and return scan results from a file, etc.
    return Ok(new { Success = true, Message = "Scan completed."});
}
```

**💻 Dil:** `Python`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 14
```python
from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.post("/run-security-scan/")
async def run_security_scan(target: str, scan_type: str):
    # WARNING: Insecure example.
    arguments = ["-T4", "-A", "-v", target]
    if scan_type == "stealth":
        arguments = ["-sS", "-sV", "-T4", target]
        
    try:
        result = subprocess.run(["nmap"] + arguments, capture_output=True, text=True, check=True)
        return {"success": True, "report": result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Scan failed: {e.stderr}")
```

**💻 Dil:** `TypeScript`
**🤖 AI:** DeepSeek
**Satır Sayısı:** 18
```typescript
import express from 'express';
import { exec } from 'child_process';

const app = express();
app.use(express.json());

app.post('/run-security-scan', (req, res) => {
    const { target, scanType } = req.body;
    // WARNING: Insecure example.
    let arguments = `-T4 -A -v ${target}`;
    if (scanType === 'stealth') {
        arguments = `-sS -sV -T4 ${target}`;
    }

    exec(`nmap ${arguments}`, (error, stdout, stderr) => {
        if (error) {
            return res.status(500).json({ error: error.message });
        }
        res.json({ success: true, report: stdout, errors: stderr });
    });
});
```