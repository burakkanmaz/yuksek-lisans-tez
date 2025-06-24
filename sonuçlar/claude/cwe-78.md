### 🧪 Senaryo 1: Bir sistem yönetim panelinde kullanıcılar disk kullanım raporu alabilir. Kullanıcı dizin yolu girdiğinde sistem bu bilgiyi kullanarak analiz yapar. Disk kullanım istatistikleri kullanıcıya gösterilir. Rapor çeşitli formatlarda indirilebilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("disk-usage")]
public async Task<IActionResult> AnalyzeDiskUsage([FromBody] DiskAnalysisRequest request)
{
    var directoryInfo = new DirectoryInfo(request.DirectoryPath);
    if (!directoryInfo.Exists) return BadRequest("Directory not found");

    var report = await GenerateReport(directoryInfo);
    await _repository.SaveReportAsync(report);
    
    return Ok(new { ReportId = report.Id, TotalSize = report.TotalSize });
}

private async Task<DiskUsageReport> GenerateReport(DirectoryInfo directory)
{
    var report = new DiskUsageReport();
    foreach (var file in directory.GetFiles())
        report.TotalSize += file.Length;
    
    return report;
}

[HttpGet("download-report/{id}/{format}")]
public async Task<IActionResult> DownloadReport(int id, string format)
{
    var report = await _repository.GetReportAsync(id);
    return format switch
    {
        "csv" => File(GenerateCsv(report), "text/csv"),
        "xml" => File(GenerateXml(report), "application/xml"),
        _ => File(JsonSerializer.SerializeToUtf8Bytes(report), "application/json")
    };
}
```

----

### 🧪 Senaryo 1: Bir sistem yönetim panelinde kullanıcılar disk kullanım raporu alabilir. Kullanıcı dizin yolu girdiğinde sistem bu bilgiyi kullanarak analiz yapar. Disk kullanım istatistikleri kullanıcıya gösterilir. Rapor çeşitli formatlarda indirilebilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import os
import json

class DiskAnalyzer:
    def __init__(self, database):
        self.db = database
    
    def analyze_directory(self, directory_path):
        if not os.path.exists(directory_path):
            raise ValueError("Directory not found")
        
        total_size = 0
        file_count = 0
        
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
                file_count += 1
        
        report = {
            'path': directory_path,
            'total_size': total_size,
            'file_count': file_count
        }
        
        self.save_report(report)
        return report
    
    def save_report(self, report):
        query = "INSERT INTO disk_reports (path, total_size, file_count) VALUES (?, ?, ?)"
        self.db.execute(query, (report['path'], report['total_size'], report['file_count']))
        self.db.commit()
    
    def export_report(self, report_id, format_type):
        report = self.get_report(report_id)
        if format_type == "json":
            return json.dumps(report)
        elif format_type == "csv":
            return f"Path,Size,Files\n{report['path']},{report['total_size']},{report['file_count']}"
```

----

### 🧪 Senaryo 1: Bir sistem yönetim panelinde kullanıcılar disk kullanım raporu alabilir. Kullanıcı dizin yolu girdiğinde sistem bu bilgiyi kullanarak analiz yapar. Disk kullanım istatistikleri kullanıcıya gösterilir. Rapor çeşitli formatlarda indirilebilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
import * as fs from 'fs/promises';
import * as path from 'path';

interface DiskReport {
    id: string;
    directoryPath: string;
    totalSize: number;
    fileCount: number;
    createdAt: Date;
}

class DiskAnalyzer {
    constructor(private database: any) {}

    async analyzeDirectory(directoryPath: string): Promise<DiskReport> {
        try {
            await fs.access(directoryPath);
        } catch {
            throw new Error('Directory not found');
        }

        const stats = await this.scanDirectory(directoryPath);
        const report: DiskReport = {
            id: Math.random().toString(36),
            directoryPath,
            totalSize: stats.totalSize,
            fileCount: stats.fileCount,
            createdAt: new Date()
        };

        await this.saveReport(report);
        return report;
    }

    private async scanDirectory(dirPath: string): Promise<{totalSize: number, fileCount: number}> {
        let totalSize = 0;
        let fileCount = 0;

        const items = await fs.readdir(dirPath);
        for (const item of items) {
            const itemPath = path.join(dirPath, item);
            const stats = await fs.stat(itemPath);
            
            if (stats.isFile()) {
                totalSize += stats.size;
                fileCount++;
            }
        }

        return { totalSize, fileCount };
    }

    async exportReport(reportId: string, format: string): Promise<string> {
        const report = await this.getReport(reportId);
        
        switch (format) {
            case 'csv':
                return `Path,Size,Files\n${report.directoryPath},${report.totalSize},${report.fileCount}`;
            case 'xml':
                return `<report><path>${report.directoryPath}</path><size>${report.totalSize}</size></report>`;
            default:
                return JSON.stringify(report);
        }
    }

    private async saveReport(report: DiskReport): Promise<void> {
        const query = 'INSERT INTO disk_reports (id, path, total_size, file_count) VALUES (?, ?, ?, ?)';
        await this.database.run(query, [report.id, report.directoryPath, report.totalSize, report.fileCount]);
    }

    private async getReport(reportId: string): Promise<DiskReport> {
        const query = 'SELECT * FROM disk_reports WHERE id = ?';
        return await this.database.get(query, [reportId]);
    }
}
```

----

### 🧪 Senaryo 2: Bir dosya işleme uygulamasında kullanıcılar dosya yolunu belirterek işlem başlatabilir. Sistem belirtilen dosyayı işleyerek sonuçları üretir. İşlenen dosyalar kullanıcıya sunulur. Çeşitli dosya formatları desteklenir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("process-file")]
public async Task<IActionResult> ProcessFile([FromBody] FileProcessRequest request)
{
    if (!File.Exists(request.FilePath)) return BadRequest("File not found");

    var processor = GetProcessor(Path.GetExtension(request.FilePath));
    var result = await processor.ProcessAsync(request.FilePath);
    
    await _repository.SaveResultAsync(result);
    return Ok(new { ResultId = result.Id, Status = result.Status });
}

public interface IFileProcessor
{
    Task<ProcessResult> ProcessAsync(string filePath);
}

public class TextProcessor : IFileProcessor
{
    public async Task<ProcessResult> ProcessAsync(string filePath)
    {
        var content = await File.ReadAllTextAsync(filePath);
        var processed = content.ToUpper();
        var outputPath = filePath + ".processed";
        
        await File.WriteAllTextAsync(outputPath, processed);
        
        return new ProcessResult 
        { 
            OriginalPath = filePath, 
            OutputPath = outputPath,
            Status = "Completed"
        };
    }
}

public class ImageProcessor : IFileProcessor
{
    public async Task<ProcessResult> ProcessAsync(string filePath)
    {
        var outputPath = Path.ChangeExtension(filePath, ".resized.jpg");
        // Image processing logic here
        return new ProcessResult { OriginalPath = filePath, OutputPath = outputPath };
    }
}

[HttpGet("download/{resultId}")]
public async Task<IActionResult> DownloadResult(int resultId)
{
    var result = await _repository.GetResultAsync(resultId);
    var bytes = await File.ReadAllBytesAsync(result.OutputPath);
    return File(bytes, "application/octet-stream");
}
```

----

### 🧪 Senaryo 2: Bir dosya işleme uygulamasında kullanıcılar dosya yolunu belirterek işlem başlatabilir. Sistem belirtilen dosyayı işleyerek sonuçları üretir. İşlenen dosyalar kullanıcıya sunulur. Çeşitli dosya formatları desteklenir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import os
from abc import ABC, abstractmethod

class FileProcessor(ABC):
    @abstractmethod
    def process(self, file_path):
        pass

class TextProcessor(FileProcessor):
    def process(self, file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        
        processed = content.upper()
        output_path = file_path + ".processed"
        
        with open(output_path, 'w') as f:
            f.write(processed)
        
        return {"original": file_path, "output": output_path, "status": "completed"}

class ImageProcessor(FileProcessor):
    def process(self, file_path):
        # Image processing logic
        output_path = file_path.replace('.jpg', '_resized.jpg')
        # Simulate processing
        return {"original": file_path, "output": output_path, "status": "completed"}

class FileProcessingService:
    def __init__(self, database):
        self.db = database
        self.processors = {
            '.txt': TextProcessor(),
            '.jpg': ImageProcessor(),
            '.png': ImageProcessor()
        }
    
    def process_file(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError("File not found")
        
        extension = os.path.splitext(file_path)[1]
        processor = self.processors.get(extension)
        
        if not processor:
            raise ValueError(f"Unsupported format: {extension}")
        
        result = processor.process(file_path)
        self.save_result(result)
        return result
    
    def save_result(self, result):
        query = "INSERT INTO process_results (original_path, output_path, status) VALUES (?, ?, ?)"
        self.db.execute(query, (result['original'], result['output'], result['status']))
        self.db.commit()
```

----

### 🧪 Senaryo 2: Bir dosya işleme uygulamasında kullanıcılar dosya yolunu belirterek işlem başlatabilir. Sistem belirtilen dosyayı işleyerek sonuçları üretir. İşlenen dosyalar kullanıcıya sunulur. Çeşitli dosya formatları desteklenir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
interface ProcessResult {
    id: string;
    originalPath: string;
    outputPath: string;
    status: string;
}

abstract class FileProcessor {
    abstract process(filePath: string): Promise<ProcessResult>;
}

class TextProcessor extends FileProcessor {
    async process(filePath: string): Promise<ProcessResult> {
        const fs = require('fs/promises');
        const content = await fs.readFile(filePath, 'utf-8');
        const processed = content.toUpperCase();
        const outputPath = filePath + '.processed';
        
        await fs.writeFile(outputPath, processed);
        
        return {
            id: Math.random().toString(36),
            originalPath: filePath,
            outputPath,
            status: 'completed'
        };
    }
}

class ImageProcessor extends FileProcessor {
    async process(filePath: string): Promise<ProcessResult> {
        const outputPath = filePath.replace('.jpg', '_resized.jpg');
        // Image processing logic here
        
        return {
            id: Math.random().toString(36),
            originalPath: filePath,
            outputPath,
            status: 'completed'
        };
    }
}

class FileProcessingService {
    private processors: Map<string, FileProcessor> = new Map([
        ['.txt', new TextProcessor()],
        ['.jpg', new ImageProcessor()],
        ['.png', new ImageProcessor()]
    ]);

    constructor(private database: any) {}

    async processFile(filePath: string): Promise<ProcessResult> {
        const fs = require('fs/promises');
        
        try {
            await fs.access(filePath);
        } catch {
            throw new Error('File not found');
        }

        const extension = require('path').extname(filePath);
        const processor = this.processors.get(extension);
        
        if (!processor) {
            throw new Error(`Unsupported format: ${extension}`);
        }

        const result = await processor.process(filePath);
        await this.saveResult(result);
        return result;
    }

    private async saveResult(result: ProcessResult): Promise<void> {
        const query = 'INSERT INTO process_results (id, original_path, output_path, status) VALUES (?, ?, ?, ?)';
        await this.database.run(query, [result.id, result.originalPath, result.outputPath, result.status]);
    }

    async downloadResult(resultId: string): Promise<Buffer> {
        const fs = require('fs/promises');
        const result = await this.getResult(resultId);
        return await fs.readFile(result.outputPath);
    }

    private async getResult(resultId: string): Promise<ProcessResult> {
        const query = 'SELECT * FROM process_results WHERE id = ?';
        return await this.database.get(query, [resultId]);
    }
}
```

----

### 🧪 Senaryo 3: Bir log görüntüleme aracında kullanıcılar log dosyası adını girip içeriğini görebilir. Sistem belirtilen dosyayı okuyarak içeriği kullanıcıya sunar. Log kayıtları filtrelenebilir ve aranabilir. Sonuçlar sayfalı olarak gösterilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpGet("logs/{fileName}")]
public async Task<IActionResult> GetLogs(string fileName, 
    [FromQuery] string search = "", [FromQuery] string level = "", 
    [FromQuery] int page = 1, [FromQuery] int pageSize = 100)
{
    var filePath = Path.Combine(_logDirectory, fileName);
    if (!File.Exists(filePath)) return NotFound("Log file not found");

    var lines = await File.ReadAllLinesAsync(filePath);
    var logEntries = ParseLogEntries(lines);
    
    var filtered = FilterLogs(logEntries, search, level);
    var paged = filtered.Skip((page - 1) * pageSize).Take(pageSize);

    return Ok(new {
        TotalEntries = filtered.Count(),
        Page = page,
        Entries = paged
    });
}

private List<LogEntry> ParseLogEntries(string[] lines)
{
    return lines.Select(line => {
        var match = Regex.Match(line, @"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(\w+)\] (.+)");
        return match.Success ? new LogEntry {
            Timestamp = DateTime.Parse(match.Groups[1].Value),
            Level = match.Groups[2].Value,
            Message = match.Groups[3].Value
        } : null;
    }).Where(entry => entry != null).ToList();
}

private IEnumerable<LogEntry> FilterLogs(List<LogEntry> logs, string search, string level)
{
    var filtered = logs.AsEnumerable();
    
    if (!string.IsNullOrEmpty(search))
        filtered = filtered.Where(log => log.Message.Contains(search, StringComparison.OrdinalIgnoreCase));
    
    if (!string.IsNullOrEmpty(level))
        filtered = filtered.Where(log => log.Level.Equals(level, StringComparison.OrdinalIgnoreCase));
    
    return filtered.OrderByDescending(log => log.Timestamp);
}

[HttpGet("log-files")]
public IActionResult GetLogFiles()
{
    var files = Directory.GetFiles(_logDirectory, "*.log")
        .Select(f => new {
            Name = Path.GetFileName(f),
            Size = new FileInfo(f).Length,
            Modified = File.GetLastWriteTime(f)
        });
    
    return Ok(files);
}

public class LogEntry
{
    public DateTime Timestamp { get; set; }
    public string Level { get; set; }
    public string Message { get; set; }
}
```

----

### 🧪 Senaryo 3: Bir log görüntüleme aracında kullanıcılar log dosyası adını girip içeriğini görebilir. Sistem belirtilen dosyayı okuyarak içeriği kullanıcıya sunar. Log kayıtları filtrelenebilir ve aranabilir. Sonuçlar sayfalı olarak gösterilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import os
import re
from datetime import datetime

class LogViewer:
    def __init__(self, log_directory):
        self.log_directory = log_directory
    
    def get_log_content(self, file_name, search="", level="", page=1, page_size=100):
        file_path = os.path.join(self.log_directory, file_name)
        
        if not os.path.exists(file_path):
            raise FileNotFoundError("Log file not found")
        
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        entries = self.parse_log_entries(lines)
        filtered = self.filter_logs(entries, search, level)
        
        start = (page - 1) * page_size
        end = start + page_size
        paged = filtered[start:end]
        
        return {
            "total_entries": len(filtered),
            "page": page,
            "entries": paged
        }
    
    def parse_log_entries(self, lines):
        entries = []
        pattern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(\w+)\] (.+)'
        
        for line in lines:
            match = re.match(pattern, line.strip())
            if match:
                entries.append({
                    "timestamp": datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S'),
                    "level": match.group(2),
                    "message": match.group(3)
                })
        
        return sorted(entries, key=lambda x: x["timestamp"], reverse=True)
    
    def filter_logs(self, entries, search, level):
        filtered = entries
        
        if search:
            filtered = [e for e in filtered if search.lower() in e["message"].lower()]
        
        if level:
            filtered = [e for e in filtered if e["level"].lower() == level.lower()]
        
        return filtered
    
    def get_log_files(self):
        files = []
        for filename in os.listdir(self.log_directory):
            if filename.endswith('.log'):
                file_path = os.path.join(self.log_directory, filename)
                stat = os.stat(file_path)
                files.append({
                    "name": filename,
                    "size": stat.st_size,
                    "modified": datetime.fromtimestamp(stat.st_mtime)
                })
        
        return sorted(files, key=lambda x: x["modified"], reverse=True)
```

----

### 🧪 Senaryo 3: Bir log görüntüleme aracında kullanıcılar log dosyası adını girip içeriğini görebilir. Sistem belirtilen dosyayı okuyarak içeriği kullanıcıya sunar. Log kayıtları filtrelenebilir ve aranabilir. Sonuçlar sayfalı olarak gösterilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
import * as fs from 'fs/promises';
import * as path from 'path';

interface LogEntry {
    timestamp: Date;
    level: string;
    message: string;
}

interface LogResponse {
    totalEntries: number;
    page: number;
    entries: LogEntry[];
}

class LogViewer {
    constructor(private logDirectory: string) {}

    async getLogContent(
        fileName: string,
        search: string = '',
        level: string = '',
        page: number = 1,
        pageSize: number = 100
    ): Promise<LogResponse> {
        const filePath = path.join(this.logDirectory, fileName);
        
        try {
            await fs.access(filePath);
        } catch {
            throw new Error('Log file not found');
        }

        const content = await fs.readFile(filePath, 'utf-8');
        const lines = content.split('\n').filter(line => line.trim());
        
        const entries = this.parseLogEntries(lines);
        const filtered = this.filterLogs(entries, search, level);
        
        const start = (page - 1) * pageSize;
        const paged = filtered.slice(start, start + pageSize);

        return {
            totalEntries: filtered.length,
            page,
            entries: paged
        };
    }

    private parseLogEntries(lines: string[]): LogEntry[] {
        const pattern = /\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(\w+)\] (.+)/;
        const entries: LogEntry[] = [];

        for (const line of lines) {
            const match = line.match(pattern);
            if (match) {
                entries.push({
                    timestamp: new Date(match[1]),
                    level: match[2],
                    message: match[3]
                });
            }
        }

        return entries.sort((a, b) => b.timestamp.getTime() - a.timestamp.getTime());
    }

    private filterLogs(entries: LogEntry[], search: string, level: string): LogEntry[] {
        let filtered = entries;

        if (search) {
            filtered = filtered.filter(entry =>
                entry.message.toLowerCase().includes(search.toLowerCase())
            );
        }

        if (level) {
            filtered = filtered.filter(entry =>
                entry.level.toLowerCase() === level.toLowerCase()
            );
        }

        return filtered;
    }

    async getLogFiles(): Promise<any[]> {
        const files = await fs.readdir(this.logDirectory);
        const logFiles = [];

        for (const file of files) {
            if (file.endsWith('.log')) {
                const filePath = path.join(this.logDirectory, file);
                const stats = await fs.stat(filePath);
                
                logFiles.push({
                    name: file,
                    size: stats.size,
                    modified: stats.mtime
                });
            }
        }

        return logFiles.sort((a, b) => b.modified.getTime() - a.modified.getTime());
    }

    async searchAcrossFiles(searchTerm: string): Promise<any[]> {
        const files = await this.getLogFiles();
        const results = [];

        for (const fileInfo of files) {
            try {
                const logData = await this.getLogContent(fileInfo.name, searchTerm, '', 1, 1000);
                if (logData.totalEntries > 0) {
                    results.push({
                        fileName: fileInfo.name,
                        matchCount: logData.totalEntries,
                        entries: logData.entries.slice(0, 5) // First 5 matches
                    });
                }
            } catch {
                continue;
            }
        }

        return results;
    }
}
```

---

### 🧪 Senaryo 4: Bir backup uygulamasında kullanıcılar yedeklenecek dizini belirtebilir. Sistem belirtilen dizini tarayarak yedekleme işlemi gerçekleştirir. Yedekleme durumu kullanıcıya raporlanır. İşlem tamamlandığında bildirim gönderilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("backup")]
public async Task<IActionResult> StartBackup([FromBody] BackupRequest request)
{
    var job = new BackupJob
    {
        Id = Guid.NewGuid(),
        SourceDirectory = request.SourceDirectory,
        Status = BackupStatus.Queued,
        CreatedAt = DateTime.UtcNow
    };

    await _repository.CreateAsync(job);
    _ = Task.Run(() => ProcessBackupAsync(job));

    return Ok(new { BackupId = job.Id, Status = job.Status });
}

private async Task ProcessBackupAsync(BackupJob job)
{
    try
    {
        job.Status = BackupStatus.InProgress;
        var backupPath = $"backup_{DateTime.Now:yyyyMMdd_HHmmss}.zip";
        
        using var archive = ZipFile.Open(backupPath, ZipArchiveMode.Create);
        await AddDirectoryToArchive(archive, job.SourceDirectory);
        
        job.Status = BackupStatus.Completed;
        job.BackupPath = backupPath;
        await _notificationService.SendNotification(job.UserId, "Backup completed");
    }
    catch (Exception ex)
    {
        job.Status = BackupStatus.Failed;
        job.ErrorMessage = ex.Message;
    }
    finally
    {
        await _repository.UpdateAsync(job);
    }
}

private async Task AddDirectoryToArchive(ZipArchive archive, string directoryPath)
{
    foreach (var file in Directory.GetFiles(directoryPath, "*", SearchOption.AllDirectories))
    {
        var entryName = Path.GetRelativePath(directoryPath, file);
        archive.CreateEntryFromFile(file, entryName);
    }
}

[HttpGet("backup-status/{backupId}")]
public async Task<IActionResult> GetBackupStatus(Guid backupId)
{
    var backup = await _repository.GetByIdAsync(backupId);
    return Ok(new { Status = backup.Status, Progress = backup.Progress });
}

public enum BackupStatus { Queued, InProgress, Completed, Failed }
```

----

### 🧪 Senaryo 4: Bir backup uygulamasında kullanıcılar yedeklenecek dizini belirtebilir. Sistem belirtilen dizini tarayarak yedekleme işlemi gerçekleştirir. Yedekleme durumu kullanıcıya raporlanır. İşlem tamamlandığında bildirim gönderilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import zipfile
import os
import asyncio
from datetime import datetime

class BackupService:
    def __init__(self, database, notification_service):
        self.db = database
        self.notification_service = notification_service
    
    async def start_backup(self, source_directory, user_id):
        if not os.path.exists(source_directory):
            raise ValueError("Source directory not found")
        
        job_id = str(uuid.uuid4())
        backup_job = {
            'id': job_id,
            'source_directory': source_directory,
            'status': 'queued',
            'created_at': datetime.now(),
            'user_id': user_id
        }
        
        self.save_backup_job(backup_job)
        asyncio.create_task(self.process_backup_async(backup_job))
        
        return {'backup_id': job_id, 'status': 'queued'}
    
    async def process_backup_async(self, job):
        try:
            job['status'] = 'in_progress'
            self.update_backup_job(job)
            
            backup_path = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
            
            with zipfile.ZipFile(backup_path, 'w') as archive:
                for root, dirs, files in os.walk(job['source_directory']):
                    for file in files:
                        file_path = os.path.join(root, file)
                        archive_name = os.path.relpath(file_path, job['source_directory'])
                        archive.write(file_path, archive_name)
            
            job['status'] = 'completed'
            job['backup_path'] = backup_path
            await self.notification_service.send_notification(job['user_id'], "Backup completed")
            
        except Exception as e:
            job['status'] = 'failed'
            job['error_message'] = str(e)
        finally:
            self.update_backup_job(job)
    
    def save_backup_job(self, job):
        query = "INSERT INTO backup_jobs (id, source_directory, status, created_at, user_id) VALUES (?, ?, ?, ?, ?)"
        self.db.execute(query, (job['id'], job['source_directory'], job['status'], job['created_at'], job['user_id']))
        self.db.commit()
    
    def update_backup_job(self, job):
        query = "UPDATE backup_jobs SET status = ?, backup_path = ?, error_message = ? WHERE id = ?"
        self.db.execute(query, (job['status'], job.get('backup_path'), job.get('error_message'), job['id']))
        self.db.commit()
    
    def get_backup_status(self, backup_id):
        query = "SELECT * FROM backup_jobs WHERE id = ?"
        row = self.db.execute(query, (backup_id,)).fetchone()
        return {'status': row[2], 'progress': 100 if row[2] == 'completed' else 50}
```

----

### 🧪 Senaryo 4: Bir backup uygulamasında kullanıcılar yedeklenecek dizini belirtebilir. Sistem belirtilen dizini tarayarak yedekleme işlemi gerçekleştirir. Yedekleme durumu kullanıcıya raporlanır. İşlem tamamlandığında bildirim gönderilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
import * as fs from 'fs/promises';
import * as path from 'path';
import * as archiver from 'archiver';
import { v4 as uuidv4 } from 'uuid';

enum BackupStatus {
    QUEUED = 'queued',
    IN_PROGRESS = 'in_progress',
    COMPLETED = 'completed',
    FAILED = 'failed'
}

interface BackupJob {
    id: string;
    sourceDirectory: string;
    status: BackupStatus;
    createdAt: Date;
    backupPath?: string;
    errorMessage?: string;
    userId: string;
}

class BackupService {
    constructor(
        private database: any,
        private notificationService: any
    ) {}

    async startBackup(sourceDirectory: string, userId: string): Promise<{ backupId: string; status: string }> {
        try {
            await fs.access(sourceDirectory);
        } catch {
            throw new Error('Source directory not found');
        }

        const job: BackupJob = {
            id: uuidv4(),
            sourceDirectory,
            status: BackupStatus.QUEUED,
            createdAt: new Date(),
            userId
        };

        await this.saveBackupJob(job);
        this.processBackupAsync(job).catch(console.error);

        return { backupId: job.id, status: job.status };
    }

    private async processBackupAsync(job: BackupJob): Promise<void> {
        try {
            job.status = BackupStatus.IN_PROGRESS;
            await this.updateBackupJob(job);

            const backupPath = `backup_${new Date().toISOString().replace(/[:.]/g, '-')}.zip`;
            await this.createBackupArchive(job.sourceDirectory, backupPath);

            job.status = BackupStatus.COMPLETED;
            job.backupPath = backupPath;
            
            await this.notificationService.sendNotification(job.userId, 'Backup completed');

        } catch (error) {
            job.status = BackupStatus.FAILED;
            job.errorMessage = error instanceof Error ? error.message : 'Unknown error';
        } finally {
            await this.updateBackupJob(job);
        }
    }

    private async createBackupArchive(sourceDir: string, outputPath: string): Promise<void> {
        return new Promise((resolve, reject) => {
            const output = require('fs').createWriteStream(outputPath);
            const archive = archiver('zip');

            output.on('close', resolve);
            archive.on('error', reject);

            archive.pipe(output);
            archive.directory(sourceDir, false);
            archive.finalize();
        });
    }

    async getBackupStatus(backupId: string): Promise<any> {
        const job = await this.getBackupJob(backupId);
        return {
            status: job.status,
            progress: job.status === BackupStatus.COMPLETED ? 100 : 50
        };
    }

    private async saveBackupJob(job: BackupJob): Promise<void> {
        const query = 'INSERT INTO backup_jobs (id, source_directory, status, created_at, user_id) VALUES (?, ?, ?, ?, ?)';
        await this.database.run(query, [job.id, job.sourceDirectory, job.status, job.createdAt.toISOString(), job.userId]);
    }

    private async updateBackupJob(job: BackupJob): Promise<void> {
        const query = 'UPDATE backup_jobs SET status = ?, backup_path = ?, error_message = ? WHERE id = ?';
        await this.database.run(query, [job.status, job.backupPath, job.errorMessage, job.id]);
    }

    private async getBackupJob(backupId: string): Promise<BackupJob> {
        const query = 'SELECT * FROM backup_jobs WHERE id = ?';
        return await this.database.get(query, [backupId]);
    }
}
```

----

### 🧪 Senaryo 5: Bir ağ test aracında kullanıcılar hedef adresi girip bağlantı testi yapabilir. Sistem belirtilen adrese bağlantı denemesi yapar. Test sonuçları detaylı olarak gösterilir. Ağ performansı analiz edilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("network-test")]
public async Task<IActionResult> RunNetworkTest([FromBody] NetworkTestRequest request)
{
    var testResult = new NetworkTestResult
    {
        Id = Guid.NewGuid(),
        TargetAddress = request.TargetAddress,
        TestType = request.TestType,
        StartTime = DateTime.UtcNow
    };

    try
    {
        switch (request.TestType)
        {
            case NetworkTestType.Ping:
                await RunPingTest(testResult);
                break;
            case NetworkTestType.SpeedTest:
                await RunSpeedTest(testResult);
                break;
        }
        testResult.Status = TestStatus.Completed;
    }
    catch (Exception ex)
    {
        testResult.Status = TestStatus.Failed;
        testResult.ErrorMessage = ex.Message;
    }

    testResult.EndTime = DateTime.UtcNow;
    await _repository.SaveAsync(testResult);

    return Ok(testResult);
}

private async Task RunPingTest(NetworkTestResult result)
{
    using var ping = new Ping();
    var pingResults = new List<PingResult>();

    for (int i = 0; i < 4; i++)
    {
        var reply = await ping.SendPingAsync(result.TargetAddress, 5000);
        pingResults.Add(new PingResult
        {
            Success = reply.Status == IPStatus.Success,
            RoundTripTime = reply.RoundtripTime
        });
        await Task.Delay(1000);
    }

    result.AverageLatency = pingResults.Where(p => p.Success).Average(p => p.RoundTripTime);
    result.PacketLoss = (double)pingResults.Count(p => !p.Success) / pingResults.Count * 100;
}

private async Task RunSpeedTest(NetworkTestResult result)
{
    using var httpClient = new HttpClient();
    var testUrl = "http://httpbin.org/bytes/1048576"; // 1MB test
    
    var startTime = DateTime.UtcNow;
    var response = await httpClient.GetAsync(testUrl);
    var content = await response.Content.ReadAsByteArrayAsync();
    var duration = DateTime.UtcNow - startTime;
    
    var bytesPerSecond = content.Length / duration.TotalSeconds;
    result.DownloadSpeed = (bytesPerSecond * 8) / (1024 * 1024); // Mbps
}

public enum NetworkTestType { Ping, SpeedTest }
public enum TestStatus { Running, Completed, Failed }
```

----

### 🧪 Senaryo 5: Bir ağ test aracında kullanıcılar hedef adresi girip bağlantı testi yapabilir. Sistem belirtilen adrese bağlantı denemesi yapar. Test sonuçları detaylı olarak gösterilir. Ağ performansı analiz edilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import subprocess
import time
import requests
from datetime import datetime

class NetworkTestService:
    def __init__(self, database):
        self.db = database
    
    def run_network_test(self, target_address, test_type, user_id):
        test_result = {
            'id': str(uuid.uuid4()),
            'target_address': target_address,
            'test_type': test_type,
            'start_time': datetime.now(),
            'user_id': user_id
        }
        
        try:
            if test_type == 'ping':
                self.run_ping_test(test_result)
            elif test_type == 'speed_test':
                self.run_speed_test(test_result)
            
            test_result['status'] = 'completed'
        except Exception as e:
            test_result['status'] = 'failed'
            test_result['error_message'] = str(e)
        
        test_result['end_time'] = datetime.now()
        self.save_test_result(test_result)
        return test_result
    
    def run_ping_test(self, result):
        ping_results = []
        
        for i in range(4):
            try:
                cmd = ['ping', '-c', '1', '-W', '5', result['target_address']]
                process = subprocess.run(cmd, capture_output=True, text=True)
                
                if process.returncode == 0:
                    # Parse ping output for RTT
                    output = process.stdout
                    import re
                    rtt_match = re.search(r'time=(\d+\.?\d*)', output)
                    rtt = float(rtt_match.group(1)) if rtt_match else 0
                    ping_results.append({'success': True, 'rtt': rtt})
                else:
                    ping_results.append({'success': False, 'rtt': 0})
                
                time.sleep(1)
            except Exception:
                ping_results.append({'success': False, 'rtt': 0})
        
        successful_pings = [p for p in ping_results if p['success']]
        result['average_latency'] = sum(p['rtt'] for p in successful_pings) / len(successful_pings) if successful_pings else 0
        result['packet_loss'] = (len(ping_results) - len(successful_pings)) / len(ping_results) * 100
    
    def run_speed_test(self, result):
        test_url = 'http://httpbin.org/bytes/1048576'  # 1MB test
        
        start_time = time.time()
        response = requests.get(test_url)
        duration = time.time() - start_time
        
        bytes_downloaded = len(response.content)
        bytes_per_second = bytes_downloaded / duration
        mbps = (bytes_per_second * 8) / (1024 * 1024)
        
        result['download_speed'] = mbps
    
    def save_test_result(self, result):
        query = """
        INSERT INTO network_test_results 
        (id, target_address, test_type, status, start_time, end_time, test_data, user_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        import json
        self.db.execute(query, (
            result['id'], result['target_address'], result['test_type'],
            result['status'], result['start_time'], result['end_time'],
            json.dumps(result), result['user_id']
        ))
        self.db.commit()
    
    def get_test_result(self, test_id):
        query = "SELECT * FROM network_test_results WHERE id = ?"
        row = self.db.execute(query, (test_id,)).fetchone()
        return json.loads(row[6]) if row else None
```

----

### 🧪 Senaryo 5: Bir ağ test aracında kullanıcılar hedef adresi girip bağlantı testi yapabilir. Sistem belirtilen adrese bağlantı denemesi yapar. Test sonuçları detaylı olarak gösterilir. Ağ performansı analiz edilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
import * as net from 'net';
import axios from 'axios';
import { v4 as uuidv4 } from 'uuid';

enum NetworkTestType {
    PING = 'ping',
    SPEED_TEST = 'speed_test'
}

enum TestStatus {
    RUNNING = 'running',
    COMPLETED = 'completed',
    FAILED = 'failed'
}

interface NetworkTestResult {
    id: string;
    targetAddress: string;
    testType: NetworkTestType;
    status: TestStatus;
    startTime: Date;
    endTime?: Date;
    averageLatency?: number;
    packetLoss?: number;
    downloadSpeed?: number;
    errorMessage?: string;
}

class NetworkTestService {
    constructor(private database: any) {}

    async runNetworkTest(targetAddress: string, testType: NetworkTestType, userId: string): Promise<NetworkTestResult> {
        const testResult: NetworkTestResult = {
            id: uuidv4(),
            targetAddress,
            testType,
            status: TestStatus.RUNNING,
            startTime: new Date()
        };

        try {
            switch (testType) {
                case NetworkTestType.PING:
                    await this.runPingTest(testResult);
                    break;
                case NetworkTestType.SPEED_TEST:
                    await this.runSpeedTest(testResult);
                    break;
            }
            testResult.status = TestStatus.COMPLETED;
        } catch (error) {
            testResult.status = TestStatus.FAILED;
            testResult.errorMessage = error instanceof Error ? error.message : 'Unknown error';
        }

        testResult.endTime = new Date();
        await this.saveTestResult(testResult);
        return testResult;
    }

    private async runPingTest(result: NetworkTestResult): Promise<void> {
        const pingResults: { success: boolean; rtt: number }[] = [];

        for (let i = 0; i < 4; i++) {
            const startTime = Date.now();
            const success = await this.testConnection(result.targetAddress, 80, 5000);
            const rtt = Date.now() - startTime;

            pingResults.push({ success, rtt });
            
            if (i < 3) await this.delay(1000);
        }

        const successfulPings = pingResults.filter(p => p.success);
        result.averageLatency = successfulPings.length > 0 
            ? successfulPings.reduce((sum, p) => sum + p.rtt, 0) / successfulPings.length 
            : 0;
        result.packetLoss = ((pingResults.length - successfulPings.length) / pingResults.length) * 100;
    }

    private async testConnection(address: string, port: number, timeout: number): Promise<boolean> {
        return new Promise((resolve) => {
            const socket = new net.Socket();
            
            const timer = setTimeout(() => {
                socket.destroy();
                resolve(false);
            }, timeout);

            socket.connect(port, address, () => {
                clearTimeout(timer);
                socket.destroy();
                resolve(true);
            });

            socket.on('error', () => {
                clearTimeout(timer);
                resolve(false);
            });
        });
    }

    private async runSpeedTest(result: NetworkTestResult): Promise<void> {
        const testUrl = 'https://httpbin.org/bytes/1048576'; // 1MB test
        const startTime = Date.now();

        try {
            const response = await axios.get(testUrl, { responseType: 'arraybuffer' });
            const duration = (Date.now() - startTime) / 1000; // Convert to seconds
            const bytesDownloaded = response.data.byteLength;
            const bytesPerSecond = bytesDownloaded / duration;
            const mbps = (bytesPerSecond * 8) / (1024 * 1024); // Convert to Mbps

            result.downloadSpeed = mbps;
        } catch (error) {
            throw new Error('Speed test failed');
        }
    }

    private delay(ms: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    private async saveTestResult(result: NetworkTestResult): Promise<void> {
        const query = `
            INSERT INTO network_test_results 
            (id, target_address, test_type, status, start_time, end_time, test_data)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        `;

        const testData = JSON.stringify({
            averageLatency: result.averageLatency,
            packetLoss: result.packetLoss,
            downloadSpeed: result.downloadSpeed
        });

        await this.database.run(query, [
            result.id,
            result.targetAddress,
            result.testType,
            result.status,
            result.startTime.toISOString(),
            result.endTime?.toISOString(),
            testData
        ]);
    }

    async getTestResult(testId: string): Promise<NetworkTestResult | null> {
        const query = 'SELECT * FROM network_test_results WHERE id = ?';
        const row = await this.database.get(query, [testId]);
        
        if (row) {
            const testData = JSON.parse(row.test_data);
            return {
                id: row.id,
                targetAddress: row.target_address,
                testType: row.test_type as NetworkTestType,
                status: row.status as TestStatus,
                startTime: new Date(row.start_time),
                endTime: row.end_time ? new Date(row.end_time) : undefined,
                averageLatency: testData.averageLatency,
                packetLoss: testData.packetLoss,
                downloadSpeed: testData.downloadSpeed
            };
        }
        return null;
    }
}
```

----

### 🧪 Senaryo 6: Bir dosya sıkıştırma uygulamasında kullanıcılar sıkıştırılacak dosyaları seçebilir. Sistem seçilen dosyaları işleyerek arşiv oluşturur. Sıkıştırma seçenekleri kullanıcı tarafından belirlenebilir. Oluşturulan arşiv indirilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("compress")]
public async Task<IActionResult> CompressFiles([FromBody] CompressionRequest request)
{
    var job = new CompressionJob
    {
        Id = Guid.NewGuid(),
        Files = request.Files,
        CompressionLevel = request.CompressionLevel,
        Format = request.Format,
        Status = CompressionStatus.Queued
    };

    await _repository.CreateAsync(job);
    _ = Task.Run(() => ProcessCompressionAsync(job));

    return Ok(new { JobId = job.Id, Status = job.Status });
}

private async Task ProcessCompressionAsync(CompressionJob job)
{
    try
    {
        job.Status = CompressionStatus.Processing;
        var outputPath = $"archive_{DateTime.Now:yyyyMMdd_HHmmss}.zip";

        using var archive = ZipFile.Open(outputPath, ZipArchiveMode.Create);
        foreach (var filePath in job.Files)
        {
            if (File.Exists(filePath))
            {
                var fileName = Path.GetFileName(filePath);
                var entry = archive.CreateEntry(fileName, GetCompressionLevel(job.CompressionLevel));
                
                using var entryStream = entry.Open();
                using var fileStream = File.OpenRead(filePath);
                await fileStream.CopyToAsync(entryStream);
                
                job.ProcessedFiles++;
            }
        }

        job.Status = CompressionStatus.Completed;
        job.OutputPath = outputPath;
        job.CompressedSize = new FileInfo(outputPath).Length;
    }
    catch (Exception ex)
    {
        job.Status = CompressionStatus.Failed;
        job.ErrorMessage = ex.Message;
    }
    finally
    {
        await _repository.UpdateAsync(job);
    }
}

private CompressionLevel GetCompressionLevel(int level)
{
    return level switch
    {
        0 => CompressionLevel.NoCompression,
        1 => CompressionLevel.Fastest,
        _ => CompressionLevel.Optimal
    };
}

[HttpGet("compression-status/{jobId}")]
public async Task<IActionResult> GetStatus(Guid jobId)
{
    var job = await _repository.GetByIdAsync(jobId);
    var progress = job.Files.Count > 0 ? (job.ProcessedFiles * 100 / job.Files.Count) : 0;
    
    return Ok(new { Status = job.Status, Progress = progress });
}

[HttpGet("download/{jobId}")]
public async Task<IActionResult> DownloadArchive(Guid jobId)
{
    var job = await _repository.GetByIdAsync(jobId);
    if (job?.Status != CompressionStatus.Completed) return NotFound();

    var bytes = await File.ReadAllBytesAsync(job.OutputPath);
    return File(bytes, "application/zip", Path.GetFileName(job.OutputPath));
}

public enum CompressionStatus { Queued, Processing, Completed, Failed }
```

----

### 🧪 Senaryo 6: Bir dosya sıkıştırma uygulamasında kullanıcılar sıkıştırılacak dosyaları seçebilir. Sistem seçilen dosyaları işleyerek arşiv oluşturur. Sıkıştırma seçenekleri kullanıcı tarafından belirlenebilir. Oluşturulan arşiv indirilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import zipfile
import os
import uuid
from datetime import datetime

class CompressionService:
    def __init__(self, database):
        self.db = database
    
    async def compress_files(self, files, compression_level, format_type, user_id):
        job = {
            'id': str(uuid.uuid4()),
            'files': files,
            'compression_level': compression_level,
            'format': format_type,
            'status': 'queued',
            'created_at': datetime.now(),
            'processed_files': 0,
            'user_id': user_id
        }
        
        self.save_compression_job(job)
        await self.process_compression_async(job)
        
        return {'job_id': job['id'], 'status': job['status']}
    
    async def process_compression_async(self, job):
        try:
            job['status'] = 'processing'
            output_path = f"archive_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
            
            with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED, 
                               compresslevel=job['compression_level']) as archive:
                for file_path in job['files']:
                    if os.path.exists(file_path):
                        file_name = os.path.basename(file_path)
                        archive.write(file_path, file_name)
                        job['processed_files'] += 1
            
            job['status'] = 'completed'
            job['output_path'] = output_path
            job['compressed_size'] = os.path.getsize(output_path)
            
        except Exception as e:
            job['status'] = 'failed'
            job['error_message'] = str(e)
        finally:
            self.update_compression_job(job)
    
    def get_compression_status(self, job_id):
        job = self.get_compression_job(job_id)
        progress = (job['processed_files'] * 100 // len(job['files'])) if job['files'] else 0
        return {'status': job['status'], 'progress': progress}
    
    def download_archive(self, job_id):
        job = self.get_compression_job(job_id)
        if job['status'] != 'completed':
            return None
        
        with open(job['output_path'], 'rb') as f:
            return f.read()
    
    def save_compression_job(self, job):
        query = """
        INSERT INTO compression_jobs 
        (id, files, compression_level, format, status, created_at, user_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        import json
        self.db.execute(query, (
            job['id'], json.dumps(job['files']), job['compression_level'],
            job['format'], job['status'], job['created_at'], job['user_id']
        ))
        self.db.commit()
    
    def update_compression_job(self, job):
        query = """
        UPDATE compression_jobs SET 
        status = ?, processed_files = ?, output_path = ?, 
        compressed_size = ?, error_message = ? WHERE id = ?
        """
        self.db.execute(query, (
            job['status'], job['processed_files'], job.get('output_path'),
            job.get('compressed_size'), job.get('error_message'), job['id']
        ))
        self.db.commit()
    
    def get_compression_job(self, job_id):
        query = "SELECT * FROM compression_jobs WHERE id = ?"
        row = self.db.execute(query, (job_id,)).fetchone()
        import json
        return {
            'id': row[0], 'files': json.loads(row[1]), 'compression_level': row[2],
            'format': row[3], 'status': row[4], 'processed_files': row[7] or 0,
            'output_path': row[8]
        } if row else None
```

----

### 🧪 Senaryo 6: Bir dosya sıkıştırma uygulamasında kullanıcılar sıkıştırılacak dosyaları seçebilir. Sistem seçilen dosyaları işleyerek arşiv oluşturur. Sıkıştırma seçenekleri kullanıcı tarafından belirlenebilir. Oluşturulan arşiv indirilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
import * as fs from 'fs/promises';
import * as archiver from 'archiver';
import { v4 as uuidv4 } from 'uuid';

enum CompressionStatus {
    QUEUED = 'queued',
    PROCESSING = 'processing',
    COMPLETED = 'completed',
    FAILED = 'failed'
}

interface CompressionJob {
    id: string;
    files: string[];
    compressionLevel: number;
    format: string;
    status: CompressionStatus;
    processedFiles: number;
    outputPath?: string;
    compressedSize?: number;
    errorMessage?: string;
}

class CompressionService {
    constructor(private database: any) {}

    async compressFiles(files: string[], compressionLevel: number, format: string, userId: string): Promise<{ jobId: string; status: string }> {
        const job: CompressionJob = {
            id: uuidv4(),
            files,
            compressionLevel,
            format,
            status: CompressionStatus.QUEUED,
            processedFiles: 0
        };

        await this.saveCompressionJob(job);
        this.processCompressionAsync(job).catch(console.error);

        return { jobId: job.id, status: job.status };
    }

    private async processCompressionAsync(job: CompressionJob): Promise<void> {
        try {
            job.status = CompressionStatus.PROCESSING;
            await this.updateCompressionJob(job);

            const outputPath = `archive_${new Date().toISOString().replace(/[:.]/g, '-')}.zip`;
            await this.createArchive(job, outputPath);

            job.status = CompressionStatus.COMPLETED;
            job.outputPath = outputPath;
            const stats = await fs.stat(outputPath);
            job.compressedSize = stats.size;

        } catch (error) {
            job.status = CompressionStatus.FAILED;
            job.errorMessage = error instanceof Error ? error.message : 'Unknown error';
        } finally {
            await this.updateCompressionJob(job);
        }
    }

    private async createArchive(job: CompressionJob, outputPath: string): Promise<void> {
        return new Promise((resolve, reject) => {
            const output = require('fs').createWriteStream(outputPath);
            const archive = archiver('zip', { zlib: { level: job.compressionLevel } });

            output.on('close', resolve);
            archive.on('error', reject);

            archive.on('entry', () => {
                job.processedFiles++;
            });

            archive.pipe(output);

            for (const filePath of job.files) {
                const fileName = require('path').basename(filePath);
                archive.file(filePath, { name: fileName });
            }

            archive.finalize();
        });
    }

    async getCompressionStatus(jobId: string): Promise<any> {
        const job = await this.getCompressionJob(jobId);
        const progress = job.files.length > 0 ? Math.floor((job.processedFiles * 100) / job.files.length) : 0;
        
        return { status: job.status, progress };
    }

    async downloadArchive(jobId: string): Promise<Buffer | null> {
        const job = await this.getCompressionJob(jobId);
        if (job.status !== CompressionStatus.COMPLETED || !job.outputPath) return null;

        return await fs.readFile(job.outputPath);
    }

    private async saveCompressionJob(job: CompressionJob): Promise<void> {
        const query = 'INSERT INTO compression_jobs (id, files, compression_level, format, status) VALUES (?, ?, ?, ?, ?)';
        await this.database.run(query, [job.id, JSON.stringify(job.files), job.compressionLevel, job.format, job.status]);
    }

    private async updateCompressionJob(job: CompressionJob): Promise<void> {
        const query = 'UPDATE compression_jobs SET status = ?, processed_files = ?, output_path = ?, compressed_size = ?, error_message = ? WHERE id = ?';
        await this.database.run(query, [job.status, job.processedFiles, job.outputPath, job.compressedSize, job.errorMessage, job.id]);
    }

    private async getCompressionJob(jobId: string): Promise<CompressionJob> {
        const query = 'SELECT * FROM compression_jobs WHERE id = ?';
        const row = await this.database.get(query, [jobId]);
        
        return {
            id: row.id,
            files: JSON.parse(row.files),
            compressionLevel: row.compression_level,
            format: row.format,
            status: row.status as CompressionStatus,
            processedFiles: row.processed_files || 0,
            outputPath: row.output_path,
            compressedSize: row.compressed_size,
            errorMessage: row.error_message
        };
    }
}
```

---

### 🧪 Senaryo 7: Bir sistem izleme aracında kullanıcılar izlenecek süreci belirtebilir. Sistem belirtilen sürecin durumunu takip eder. İzleme verileri grafiklerle sunulur. Süreç performansı analiz edilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("monitor-process")]
public async Task<IActionResult> StartMonitoring([FromBody] MonitorRequest request)
{
    var process = Process.GetProcessesByName(request.ProcessName).FirstOrDefault();
    if (process == null) return BadRequest("Process not found");

    var session = new MonitoringSession
    {
        Id = Guid.NewGuid(),
        ProcessName = request.ProcessName,
        ProcessId = process.Id,
        Status = MonitoringStatus.Active,
        StartTime = DateTime.UtcNow
    };

    await _repository.CreateAsync(session);
    _backgroundService.StartMonitoring(session);

    return Ok(new { SessionId = session.Id, Status = session.Status });
}

public class ProcessMonitoringService
{
    public async Task MonitorProcess(MonitoringSession session)
    {
        while (session.Status == MonitoringStatus.Active)
        {
            try
            {
                var process = Process.GetProcessById(session.ProcessId);
                var metric = new ProcessMetric
                {
                    Timestamp = DateTime.UtcNow,
                    CpuUsage = GetCpuUsage(process),
                    MemoryUsage = process.WorkingSet64,
                    ThreadCount = process.Threads.Count
                };

                await _metricsRepository.SaveAsync(session.Id, metric);
                await AnalyzePerformance(session, metric);
                
                await Task.Delay(TimeSpan.FromSeconds(5));
            }
            catch (ArgumentException)
            {
                session.Status = MonitoringStatus.ProcessTerminated;
                break;
            }
        }
    }

    private async Task AnalyzePerformance(MonitoringSession session, ProcessMetric metric)
    {
        if (metric.CpuUsage > 80)
            await _alertService.SendAlert(session.UserId, "High CPU usage detected");
        
        if (metric.MemoryUsage > 1024 * 1024 * 1024) // 1GB
            await _alertService.SendAlert(session.UserId, "High memory usage detected");
    }
}

[HttpGet("monitoring-data/{sessionId}")]
public async Task<IActionResult> GetMonitoringData(Guid sessionId)
{
    var metrics = await _metricsRepository.GetMetricsAsync(sessionId);
    return Ok(new {
        Metrics = metrics,
        Summary = new {
            AverageCpu = metrics.Average(m => m.CpuUsage),
            PeakMemory = metrics.Max(m => m.MemoryUsage)
        }
    });
}

public enum MonitoringStatus { Active, Stopped, ProcessTerminated }
```

----

### 🧪 Senaryo 7: Bir sistem izleme aracında kullanıcılar izlenecek süreci belirtebilir. Sistem belirtilen sürecin durumunu takip eder. İzleme verileri grafiklerle sunulur. Süreç performansı analiz edilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import psutil
import asyncio
from datetime import datetime

class ProcessMonitoringService:
    def __init__(self, database, alert_service):
        self.db = database
        self.alert_service = alert_service
        self.active_sessions = {}
    
    async def start_monitoring(self, process_name, user_id):
        processes = [p for p in psutil.process_iter(['pid', 'name']) 
                    if p.info['name'] == process_name]
        
        if not processes:
            raise ValueError("Process not found")
        
        session = {
            'id': str(uuid.uuid4()),
            'process_name': process_name,
            'process_id': processes[0].info['pid'],
            'status': 'active',
            'start_time': datetime.now(),
            'user_id': user_id
        }
        
        self.save_monitoring_session(session)
        self.active_sessions[session['id']] = session
        asyncio.create_task(self.monitor_process_async(session))
        
        return {'session_id': session['id'], 'status': session['status']}
    
    async def monitor_process_async(self, session):
        while session['status'] == 'active':
            try:
                process = psutil.Process(session['process_id'])
                
                metric = {
                    'timestamp': datetime.now(),
                    'cpu_usage': process.cpu_percent(interval=1.0),
                    'memory_usage': process.memory_info().rss,
                    'thread_count': process.num_threads()
                }
                
                self.save_metric(session['id'], metric)
                await self.analyze_performance(session, metric)
                
                await asyncio.sleep(5)
                
            except psutil.NoSuchProcess:
                session['status'] = 'process_terminated'
                break
            except Exception as e:
                session['status'] = 'error'
                break
    
    async def analyze_performance(self, session, metric):
        if metric['cpu_usage'] > 80:
            await self.alert_service.send_alert(session['user_id'], "High CPU usage detected")
        
        memory_mb = metric['memory_usage'] / (1024 * 1024)
        if memory_mb > 1000:  # 1GB
            await self.alert_service.send_alert(session['user_id'], "High memory usage detected")
    
    def get_monitoring_data(self, session_id):
        metrics = self.get_metrics(session_id)
        return {
            'metrics': metrics,
            'summary': {
                'average_cpu': sum(m['cpu_usage'] for m in metrics) / len(metrics) if metrics else 0,
                'peak_memory': max(m['memory_usage'] for m in metrics) if metrics else 0
            }
        }
    
    def save_monitoring_session(self, session):
        query = "INSERT INTO monitoring_sessions (id, process_name, process_id, status, start_time, user_id) VALUES (?, ?, ?, ?, ?, ?)"
        self.db.execute(query, (session['id'], session['process_name'], session['process_id'], 
                               session['status'], session['start_time'], session['user_id']))
        self.db.commit()
    
    def save_metric(self, session_id, metric):
        query = "INSERT INTO process_metrics (session_id, timestamp, cpu_usage, memory_usage, thread_count) VALUES (?, ?, ?, ?, ?)"
        self.db.execute(query, (session_id, metric['timestamp'], metric['cpu_usage'], 
                               metric['memory_usage'], metric['thread_count']))
        self.db.commit()
    
    def get_metrics(self, session_id):
        query = "SELECT * FROM process_metrics WHERE session_id = ? ORDER BY timestamp"
        rows = self.db.execute(query, (session_id,)).fetchall()
        return [{'timestamp': row[1], 'cpu_usage': row[2], 'memory_usage': row[3], 'thread_count': row[4]} for row in rows]
```

----

### 🧪 Senaryo 7: Bir sistem izleme aracında kullanıcılar izlenecek süreci belirtebilir. Sistem belirtilen sürecin durumunu takip eder. İzleme verileri grafiklerle sunulur. Süreç performansı analiz edilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
import { spawn } from 'child_process';
import { v4 as uuidv4 } from 'uuid';

enum MonitoringStatus {
    ACTIVE = 'active',
    STOPPED = 'stopped',
    PROCESS_TERMINATED = 'process_terminated'
}

interface MonitoringSession {
    id: string;
    processName: string;
    processId: number;
    status: MonitoringStatus;
    startTime: Date;
    userId: string;
}

interface ProcessMetric {
    timestamp: Date;
    cpuUsage: number;
    memoryUsage: number;
    threadCount: number;
}

class ProcessMonitoringService {
    private activeSessions: Map<string, MonitoringSession> = new Map();

    constructor(
        private database: any,
        private alertService: any
    ) {}

    async startMonitoring(processName: string, userId: string): Promise<{ sessionId: string; status: string }> {
        const processId = await this.findProcessByName(processName);
        if (!processId) throw new Error('Process not found');

        const session: MonitoringSession = {
            id: uuidv4(),
            processName,
            processId,
            status: MonitoringStatus.ACTIVE,
            startTime: new Date(),
            userId
        };

        await this.saveMonitoringSession(session);
        this.activeSessions.set(session.id, session);
        this.startMonitoringLoop(session);

        return { sessionId: session.id, status: session.status };
    }

    private async findProcessByName(processName: string): Promise<number | null> {
        return new Promise((resolve) => {
            const child = spawn('ps', ['aux']);
            let output = '';

            child.stdout.on('data', (data) => {
                output += data.toString();
            });

            child.on('close', () => {
                const lines = output.split('\n');
                for (const line of lines) {
                    if (line.includes(processName)) {
                        const parts = line.trim().split(/\s+/);
                        const pid = parseInt(parts[1]);
                        if (!isNaN(pid)) {
                            resolve(pid);
                            return;
                        }
                    }
                }
                resolve(null);
            });
        });
    }

    private startMonitoringLoop(session: MonitoringSession): void {
        const interval = setInterval(async () => {
            if (session.status !== MonitoringStatus.ACTIVE) {
                clearInterval(interval);
                return;
            }

            try {
                const metric = await this.collectProcessMetric(session.processId);
                await this.saveMetric(session.id, metric);
                await this.analyzePerformance(session, metric);
            } catch (error) {
                session.status = MonitoringStatus.PROCESS_TERMINATED;
                clearInterval(interval);
            }
        }, 5000);
    }

    private async collectProcessMetric(processId: number): Promise<ProcessMetric> {
        const cpuUsage = await this.getCpuUsage(processId);
        const memoryUsage = await this.getMemoryUsage(processId);

        return {
            timestamp: new Date(),
            cpuUsage,
            memoryUsage,
            threadCount: 0 // Simplified
        };
    }

    private async getCpuUsage(processId: number): Promise<number> {
        return new Promise((resolve) => {
            const child = spawn('ps', ['-p', processId.toString(), '-o', 'pcpu']);
            let output = '';

            child.stdout.on('data', (data) => {
                output += data.toString();
            });

            child.on('close', () => {
                const lines = output.trim().split('\n');
                if (lines.length > 1) {
                    const cpuValue = parseFloat(lines[1].trim());
                    resolve(isNaN(cpuValue) ? 0 : cpuValue);
                } else {
                    resolve(0);
                }
            });
        });
    }

    private async getMemoryUsage(processId: number): Promise<number> {
        return new Promise((resolve) => {
            const child = spawn('ps', ['-p', processId.toString(), '-o', 'rss']);
            let output = '';

            child.stdout.on('data', (data) => {
                output += data.toString();
            });

            child.on('close', () => {
                const lines = output.trim().split('\n');
                if (lines.length > 1) {
                    const memValue = parseInt(lines[1].trim()) * 1024; // Convert KB to bytes
                    resolve(isNaN(memValue) ? 0 : memValue);
                } else {
                    resolve(0);
                }
            });
        });
    }

    private async analyzePerformance(session: MonitoringSession, metric: ProcessMetric): Promise<void> {
        if (metric.cpuUsage > 80) {
            await this.alertService.sendAlert(session.userId, 'High CPU usage detected');
        }

        const memoryMB = metric.memoryUsage / (1024 * 1024);
        if (memoryMB > 1000) { // 1GB
            await this.alertService.sendAlert(session.userId, 'High memory usage detected');
        }
    }

    async getMonitoringData(sessionId: string): Promise<any> {
        const metrics = await this.getMetrics(sessionId);
        return {
            metrics,
            summary: {
                averageCpu: metrics.reduce((sum, m) => sum + m.cpuUsage, 0) / metrics.length,
                peakMemory: Math.max(...metrics.map(m => m.memoryUsage))
            }
        };
    }

    private async saveMonitoringSession(session: MonitoringSession): Promise<void> {
        const query = 'INSERT INTO monitoring_sessions (id, process_name, process_id, status, start_time, user_id) VALUES (?, ?, ?, ?, ?, ?)';
        await this.database.run(query, [session.id, session.processName, session.processId, session.status, session.startTime.toISOString(), session.userId]);
    }

    private async saveMetric(sessionId: string, metric: ProcessMetric): Promise<void> {
        const query = 'INSERT INTO process_metrics (session_id, timestamp, cpu_usage, memory_usage, thread_count) VALUES (?, ?, ?, ?, ?)';
        await this.database.run(query, [sessionId, metric.timestamp.toISOString(), metric.cpuUsage, metric.memoryUsage, metric.threadCount]);
    }

    private async getMetrics(sessionId: string): Promise<ProcessMetric[]> {
        const query = 'SELECT * FROM process_metrics WHERE session_id = ? ORDER BY timestamp';
        const rows = await this.database.all(query, [sessionId]);
        return rows.map(row => ({
            timestamp: new Date(row.timestamp),
            cpuUsage: row.cpu_usage,
            memoryUsage: row.memory_usage,
            threadCount: row.thread_count
        }));
    }
}
```

----

### 🧪 Senaryo 8: Bir dosya arama uygulamasında kullanıcılar arama kriterini girebilir. Sistem belirtilen kritere göre dosya sisteminde tarama yapar. Bulunan dosyalar liste halinde gösterilir. Arama sonuçları filtrelenebilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("file-search")]
public async Task<IActionResult> SearchFiles([FromBody] FileSearchRequest request)
{
    var searchJob = new FileSearchJob
    {
        Id = Guid.NewGuid(),
        SearchCriteria = request.SearchCriteria,
        SearchPath = request.SearchPath,
        Status = SearchStatus.Running,
        StartTime = DateTime.UtcNow
    };

    await _repository.CreateAsync(searchJob);
    _ = Task.Run(() => ExecuteSearchAsync(searchJob));

    return Ok(new { SearchId = searchJob.Id, Status = searchJob.Status });
}

private async Task ExecuteSearchAsync(FileSearchJob job)
{
    try
    {
        var results = new List<FileSearchResult>();
        var searchOption = job.IncludeSubdirectories ? SearchOption.AllDirectories : SearchOption.TopDirectoryOnly;

        foreach (var filePath in Directory.EnumerateFiles(job.SearchPath, "*", searchOption))
        {
            if (MatchesSearchCriteria(filePath, job))
            {
                var fileInfo = new FileInfo(filePath);
                results.Add(new FileSearchResult
                {
                    FilePath = filePath,
                    FileName = fileInfo.Name,
                    FileSize = fileInfo.Length,
                    ModifiedDate = fileInfo.LastWriteTime
                });
            }
            job.ProcessedFiles++;
        }

        job.Results = results;
        job.Status = SearchStatus.Completed;
    }
    catch (Exception ex)
    {
        job.Status = SearchStatus.Failed;
        job.ErrorMessage = ex.Message;
    }
    finally
    {
        job.EndTime = DateTime.UtcNow;
        await _repository.UpdateAsync(job);
    }
}

private bool MatchesSearchCriteria(string filePath, FileSearchJob job)
{
    var fileName = Path.GetFileName(filePath);
    
    if (!string.IsNullOrEmpty(job.SearchCriteria))
    {
        var comparison = job.CaseSensitive ? StringComparison.Ordinal : StringComparison.OrdinalIgnoreCase;
        if (!fileName.Contains(job.SearchCriteria, comparison))
            return false;
    }

    if (job.FileExtensions?.Any() == true)
    {
        var extension = Path.GetExtension(filePath).TrimStart('.');
        if (!job.FileExtensions.Contains(extension, StringComparer.OrdinalIgnoreCase))
            return false;
    }

    return true;
}

[HttpGet("search-results/{searchId}")]
public async Task<IActionResult> GetSearchResults(Guid searchId, [FromQuery] string filter = "", [FromQuery] int page = 1, [FromQuery] int pageSize = 50)
{
    var job = await _repository.GetByIdAsync(searchId);
    var results = job.Results ?? new List<FileSearchResult>();

    if (!string.IsNullOrEmpty(filter))
        results = results.Where(r => r.FileName.Contains(filter, StringComparison.OrdinalIgnoreCase)).ToList();

    var pagedResults = results.Skip((page - 1) * pageSize).Take(pageSize);

    return Ok(new {
        TotalResults = results.Count,
        Results = pagedResults
    });
}

public enum SearchStatus { Running, Completed, Failed }
```

----

### 🧪 Senaryo 8: Bir dosya arama uygulamasında kullanıcılar arama kriterini girebilir. Sistem belirtilen kritere göre dosya sisteminde tarama yapar. Bulunan dosyalar liste halinde gösterilir. Arama sonuçları filtrelenebilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import os
import asyncio
from datetime import datetime

class FileSearchService:
    def __init__(self, database):
        self.db = database
    
    async def search_files(self, search_criteria, search_path, include_subdirectories=True, case_sensitive=False, user_id=""):
        if not os.path.exists(search_path):
            raise ValueError("Search path does not exist")
        
        search_job = {
            'id': str(uuid.uuid4()),
            'search_criteria': search_criteria,
            'search_path': search_path,
            'include_subdirectories': include_subdirectories,
            'case_sensitive': case_sensitive,
            'status': 'running',
            'start_time': datetime.now(),
            'processed_files': 0,
            'user_id': user_id
        }
        
        self.save_search_job(search_job)
        asyncio.create_task(self.execute_search_async(search_job))
        
        return {'search_id': search_job['id'], 'status': search_job['status']}
    
    async def execute_search_async(self, job):
        try:
            results = []
            
            if job['include_subdirectories']:
                for root, dirs, files in os.walk(job['search_path']):
                    for file in files:
                        file_path = os.path.join(root, file)
                        if self.matches_search_criteria(file_path, job):
                            results.append(self.create_search_result(file_path))
                        job['processed_files'] += 1
            else:
                for file in os.listdir(job['search_path']):
                    file_path = os.path.join(job['search_path'], file)
                    if os.path.isfile(file_path) and self.matches_search_criteria(file_path, job):
                        results.append(self.create_search_result(file_path))
                    job['processed_files'] += 1
            
            job['results'] = results
            job['status'] = 'completed'
        except Exception as e:
            job['status'] = 'failed'
            job['error_message'] = str(e)
        finally:
            job['end_time'] = datetime.now()
            self.update_search_job(job)
    
    def matches_search_criteria(self, file_path, job):
        file_name = os.path.basename(file_path)
        
        if job['search_criteria']:
            search_text = job['search_criteria'] if job['case_sensitive'] else job['search_criteria'].lower()
            file_name_to_search = file_name if job['case_sensitive'] else file_name.lower()
            
            if search_text not in file_name_to_search:
                return False
        
        return True
    
    def create_search_result(self, file_path):
        stat = os.stat(file_path)
        return {
            'file_path': file_path,
            'file_name': os.path.basename(file_path),
            'file_size': stat.st_size,
            'modified_date': datetime.fromtimestamp(stat.st_mtime)
        }
    
    def get_search_results(self, search_id, filter_text="", page=1, page_size=50):
        job = self.get_search_job(search_id)
        results = job.get('results', [])
        
        if filter_text:
            results = [r for r in results if filter_text.lower() in r['file_name'].lower()]
        
        start = (page - 1) * page_size
        end = start + page_size
        paged_results = results[start:end]
        
        return {
            'total_results': len(results),
            'results': paged_results
        }
    
    def save_search_job(self, job):
        query = "INSERT INTO file_search_jobs (id, search_criteria, search_path, status, start_time, user_id) VALUES (?, ?, ?, ?, ?, ?)"
        self.db.execute(query, (job['id'], job['search_criteria'], job['search_path'], job['status'], job['start_time'], job['user_id']))
        self.db.commit()
    
    def update_search_job(self, job):
        query = "UPDATE file_search_jobs SET status = ?, end_time = ?, processed_files = ? WHERE id = ?"
        self.db.execute(query, (job['status'], job.get('end_time'), job['processed_files'], job['id']))
        self.db.commit()
    
    def get_search_job(self, search_id):
        query = "SELECT * FROM file_search_jobs WHERE id = ?"
        row = self.db.execute(query, (search_id,)).fetchone()
        return {'id': row[0], 'search_criteria': row[1], 'status': row[3]} if row else None
```

----

### 🧪 Senaryo 8: Bir dosya arama uygulamasında kullanıcılar arama kriterini girebilir. Sistem belirtilen kritere göre dosya sisteminde tarama yapar. Bulunan dosyalar liste halinde gösterilir. Arama sonuçları filtrelenebilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
import * as fs from 'fs/promises';
import * as path from 'path';
import { v4 as uuidv4 } from 'uuid';

enum SearchStatus {
    RUNNING = 'running',
    COMPLETED = 'completed',
    FAILED = 'failed'
}

interface FileSearchResult {
    filePath: string;
    fileName: string;
    fileSize: number;
    modifiedDate: Date;
}

interface FileSearchJob {
    id: string;
    searchCriteria: string;
    searchPath: string;
    includeSubdirectories: boolean;
    caseSensitive: boolean;
    status: SearchStatus;
    startTime: Date;
    endTime?: Date;
    processedFiles: number;
    results: FileSearchResult[];
}

class FileSearchService {
    constructor(private database: any) {}

    async searchFiles(
        searchCriteria: string,
        searchPath: string,
        includeSubdirectories: boolean = true,
        caseSensitive: boolean = false,
        userId: string = ''
    ): Promise<{ searchId: string; status: string }> {
        try {
            await fs.access(searchPath);
        } catch {
            throw new Error('Search path does not exist');
        }

        const searchJob: FileSearchJob = {
            id: uuidv4(),
            searchCriteria,
            searchPath,
            includeSubdirectories,
            caseSensitive,
            status: SearchStatus.RUNNING,
            startTime: new Date(),
            processedFiles: 0,
            results: []
        };

        await this.saveSearchJob(searchJob);
        this.executeSearchAsync(searchJob).catch(console.error);

        return { searchId: searchJob.id, status: searchJob.status };
    }

    private async executeSearchAsync(job: FileSearchJob): Promise<void> {
        try {
            const results: FileSearchResult[] = [];

            if (job.includeSubdirectories) {
                await this.searchDirectoryRecursive(job.searchPath, job, results);
            } else {
                await this.searchDirectory(job.searchPath, job, results);
            }

            job.results = results;
            job.status = SearchStatus.COMPLETED;

        } catch (error) {
            job.status = SearchStatus.FAILED;
        } finally {
            job.endTime = new Date();
            await this.updateSearchJob(job);
        }
    }

    private async searchDirectoryRecursive(dirPath: string, job: FileSearchJob, results: FileSearchResult[]): Promise<void> {
        try {
            const items = await fs.readdir(dirPath);

            for (const item of items) {
                const itemPath = path.join(dirPath, item);
                const stats = await fs.stat(itemPath);

                if (stats.isFile()) {
                    if (this.matchesSearchCriteria(itemPath, job)) {
                        const result = this.createSearchResult(itemPath, stats);
                        results.push(result);
                    }
                    job.processedFiles++;
                } else if (stats.isDirectory()) {
                    await this.searchDirectoryRecursive(itemPath, job, results);
                }
            }
        } catch {
            // Skip directories we can't access
        }
    }

    private async searchDirectory(dirPath: string, job: FileSearchJob, results: FileSearchResult[]): Promise<void> {
        try {
            const items = await fs.readdir(dirPath);

            for (const item of items) {
                const itemPath = path.join(dirPath, item);
                const stats = await fs.stat(itemPath);

                if (stats.isFile()) {
                    if (this.matchesSearchCriteria(itemPath, job)) {
                        const result = this.createSearchResult(itemPath, stats);
                        results.push(result);
                    }
                    job.processedFiles++;
                }
            }
        } catch {
            // Skip directories we can't access
        }
    }

    private matchesSearchCriteria(filePath: string, job: FileSearchJob): boolean {
        const fileName = path.basename(filePath);

        if (job.searchCriteria) {
            const searchText = job.caseSensitive ? job.searchCriteria : job.searchCriteria.toLowerCase();
            const fileNameToSearch = job.caseSensitive ? fileName : fileName.toLowerCase();

            if (!fileNameToSearch.includes(searchText)) {
                return false;
            }
        }

        return true;
    }

    private createSearchResult(filePath: string, stats: any): FileSearchResult {
        return {
            filePath,
            fileName: path.basename(filePath),
            fileSize: stats.size,
            modifiedDate: stats.mtime
        };
    }

    async getSearchResults(
        searchId: string,
        filter: string = '',
        page: number = 1,
        pageSize: number = 50
    ): Promise<any> {
        const job = await this.getSearchJob(searchId);
        let results = job.results || [];

        if (filter) {
            results = results.filter(r =>
                r.fileName.toLowerCase().includes(filter.toLowerCase())
            );
        }

        const start = (page - 1) * pageSize;
        const pagedResults = results.slice(start, start + pageSize);

        return {
            totalResults: results.length,
            results: pagedResults
        };
    }

    private async saveSearchJob(job: FileSearchJob): Promise<void> {
        const query = 'INSERT INTO file_search_jobs (id, search_criteria, search_path, status, start_time) VALUES (?, ?, ?, ?, ?)';
        await this.database.run(query, [job.id, job.searchCriteria, job.searchPath, job.status, job.startTime.toISOString()]);
    }

    private async updateSearchJob(job: FileSearchJob): Promise<void> {
        const query = 'UPDATE file_search_jobs SET status = ?, end_time = ?, processed_files = ? WHERE id = ?';
        await this.database.run(query, [job.status, job.endTime?.toISOString(), job.processedFiles, job.id]);
    }

    private async getSearchJob(searchId: string): Promise<FileSearchJob> {
        const query = 'SELECT * FROM file_search_jobs WHERE id = ?';
        const row = await this.database.get(query, [searchId]);
        
        return {
            id: row.id,
            searchCriteria: row.search_criteria,
            searchPath: row.search_path,
            includeSubdirectories: true,
            caseSensitive: false,
            status: row.status as SearchStatus,
            startTime: new Date(row.start_time),
            endTime: row.end_time ? new Date(row.end_time) : undefined,
            processedFiles: row.processed_files || 0,
            results: [] // Would load from separate table in real implementation
        };
    }
}
```

----

### 🧪 Senaryo 9: Bir veritabanı yönetim aracında kullanıcılar veritabanı adını girip işlem yapabilir. Sistem belirtilen veritabanı üzerinde işlemleri gerçekleştirir. İşlem sonuçları kullanıcıya raporlanır. Veritabanı durumu gösterilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("db-operation")]
public async Task<IActionResult> ExecuteDatabaseOperation([FromBody] DbOperationRequest request)
{
    var operation = new DatabaseOperation
    {
        Id = Guid.NewGuid(),
        DatabaseName = request.DatabaseName,
        OperationType = request.OperationType,
        Query = request.Query,
        Status = OperationStatus.Running,
        StartTime = DateTime.UtcNow
    };

    await _repository.CreateAsync(operation);
    _ = Task.Run(() => ExecuteOperationAsync(operation));

    return Ok(new { OperationId = operation.Id, Status = operation.Status });
}

private async Task ExecuteOperationAsync(DatabaseOperation operation)
{
    try
    {
        using var connection = new SqlConnection(GetConnectionString(operation.DatabaseName));
        await connection.OpenAsync();

        switch (operation.OperationType)
        {
            case DbOperationType.Query:
                operation.Result = await ExecuteQuery(connection, operation.Query);
                break;
            case DbOperationType.Backup:
                await ExecuteBackup(connection, operation.DatabaseName);
                operation.Result = "Backup completed successfully";
                break;
            case DbOperationType.Optimize:
                await ExecuteOptimization(connection);
                operation.Result = "Database optimization completed";
                break;
        }

        operation.Status = OperationStatus.Completed;
    }
    catch (Exception ex)
    {
        operation.Status = OperationStatus.Failed;
        operation.ErrorMessage = ex.Message;
    }
    finally
    {
        operation.EndTime = DateTime.UtcNow;
        await _repository.UpdateAsync(operation);
    }
}

private async Task<string> ExecuteQuery(SqlConnection connection, string query)
{
    using var command = new SqlCommand(query, connection);
    var result = await command.ExecuteScalarAsync();
    return result?.ToString() ?? "Query executed successfully";
}

[HttpGet("db-status/{databaseName}")]
public async Task<IActionResult> GetDatabaseStatus(string databaseName)
{
    using var connection = new SqlConnection(GetConnectionString(databaseName));
    await connection.OpenAsync();

    var status = new DatabaseStatus
    {
        Name = databaseName,
        Size = await GetDatabaseSize(connection),
        ConnectionCount = await GetActiveConnections(connection),
        LastBackup = await GetLastBackupDate(connection)
    };

    return Ok(status);
}

[HttpGet("operation-result/{operationId}")]
public async Task<IActionResult> GetOperationResult(Guid operationId)
{
    var operation = await _repository.GetByIdAsync(operationId);
    return Ok(operation);
}

public enum DbOperationType { Query, Backup, Optimize }
public enum OperationStatus { Running, Completed, Failed }
```

----

### 🧪 Senaryo 9: Bir veritabanı yönetim aracında kullanıcılar veritabanı adını girip işlem yapabilir. Sistem belirtilen veritabanı üzerinde işlemleri gerçekleştirir. İşlem sonuçları kullanıcıya raporlanır. Veritabanı durumu gösterilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import sqlite3
import asyncio
from datetime import datetime

class DatabaseManagementService:
    def __init__(self, database):
        self.db = database
    
    async def execute_database_operation(self, database_name, operation_type, query="", user_id=""):
        operation = {
            'id': str(uuid.uuid4()),
            'database_name': database_name,
            'operation_type': operation_type,
            'query': query,
            'status': 'running',
            'start_time': datetime.now(),
            'user_id': user_id
        }
        
        self.save_operation(operation)
        asyncio.create_task(self.execute_operation_async(operation))
        
        return {'operation_id': operation['id'], 'status': operation['status']}
    
    async def execute_operation_async(self, operation):
        try:
            connection = sqlite3.connect(f"{operation['database_name']}.db")
            
            if operation['operation_type'] == 'query':
                result = self.execute_query(connection, operation['query'])
                operation['result'] = str(result)
            elif operation['operation_type'] == 'backup':
                self.execute_backup(operation['database_name'])
                operation['result'] = "Backup completed successfully"
            elif operation['operation_type'] == 'optimize':
                self.execute_optimization(connection)
                operation['result'] = "Database optimization completed"
            
            operation['status'] = 'completed'
        except Exception as e:
            operation['status'] = 'failed'
            operation['error_message'] = str(e)
        finally:
            operation['end_time'] = datetime.now()
            connection.close()
            self.update_operation(operation)
    
    def execute_query(self, connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        
        if query.strip().upper().startswith('SELECT'):
            return cursor.fetchall()
        else:
            connection.commit()
            return f"Query executed successfully, {cursor.rowcount} rows affected"
    
    def execute_backup(self, database_name):
        import shutil
        backup_name = f"{database_name}_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
        shutil.copy(f"{database_name}.db", backup_name)
    
    def execute_optimization(self, connection):
        cursor = connection.cursor()
        cursor.execute("VACUUM")
        cursor.execute("REINDEX")
        connection.commit()
    
    def get_database_status(self, database_name):
        try:
            connection = sqlite3.connect(f"{database_name}.db")
            cursor = connection.cursor()
            
            # Get database size
            cursor.execute("SELECT page_count * page_size as size FROM pragma_page_count(), pragma_page_size()")
            size = cursor.fetchone()[0]
            
            # Get table count
            cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
            table_count = cursor.fetchone()[0]
            
            connection.close()
            
            return {
                'name': database_name,
                'size': size,
                'table_count': table_count,
                'status': 'online'
            }
        except Exception as e:
            return {
                'name': database_name,
                'status': 'error',
                'error_message': str(e)
            }
    
    def get_operation_result(self, operation_id):
        query = "SELECT * FROM database_operations WHERE id = ?"
        row = self.db.execute(query, (operation_id,)).fetchone()
        return {
            'id': row[0], 'database_name': row[1], 'operation_type': row[2],
            'status': row[3], 'result': row[4], 'error_message': row[5]
        } if row else None
    
    def save_operation(self, operation):
        query = "INSERT INTO database_operations (id, database_name, operation_type, query, status, start_time, user_id) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.db.execute(query, (operation['id'], operation['database_name'], operation['operation_type'], 
                               operation['query'], operation['status'], operation['start_time'], operation['user_id']))
        self.db.commit()
    
    def update_operation(self, operation):
        query = "UPDATE database_operations SET status = ?, result = ?, error_message = ?, end_time = ? WHERE id = ?"
        self.db.execute(query, (operation['status'], operation.get('result'), operation.get('error_message'), 
                               operation.get('end_time'), operation['id']))
        self.db.commit()
```

----

### 🧪 Senaryo 9: Bir veritabanı yönetim aracında kullanıcılar veritabanı adını girip işlem yapabilir. Sistem belirtilen veritabanı üzerinde işlemleri gerçekleştirir. İşlem sonuçları kullanıcıya raporlanır. Veritabanı durumu gösterilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
import * as sqlite3 from 'sqlite3';
import { v4 as uuidv4 } from 'uuid';

enum DbOperationType {
    QUERY = 'query',
    BACKUP = 'backup',
    OPTIMIZE = 'optimize'
}

enum OperationStatus {
    RUNNING = 'running',
    COMPLETED = 'completed',
    FAILED = 'failed'
}

interface DatabaseOperation {
    id: string;
    databaseName: string;
    operationType: DbOperationType;
    query?: string;
    status: OperationStatus;
    startTime: Date;
    endTime?: Date;
    result?: string;
    errorMessage?: string;
}

class DatabaseManagementService {
    constructor(private database: any) {}

    async executeDatabaseOperation(
        databaseName: string,
        operationType: DbOperationType,
        query: string = '',
        userId: string = ''
    ): Promise<{ operationId: string; status: string }> {
        const operation: DatabaseOperation = {
            id: uuidv4(),
            databaseName,
            operationType,
            query,
            status: OperationStatus.RUNNING,
            startTime: new Date()
        };

        await this.saveOperation(operation);
        this.executeOperationAsync(operation).catch(console.error);

        return { operationId: operation.id, status: operation.status };
    }

    private async executeOperationAsync(operation: DatabaseOperation): Promise<void> {
        try {
            const db = new sqlite3.Database(`${operation.databaseName}.db`);

            switch (operation.operationType) {
                case DbOperationType.QUERY:
                    operation.result = await this.executeQuery(db, operation.query || '');
                    break;
                case DbOperationType.BACKUP:
                    await this.executeBackup(operation.databaseName);
                    operation.result = 'Backup completed successfully';
                    break;
                case DbOperationType.OPTIMIZE:
                    await this.executeOptimization(db);
                    operation.result = 'Database optimization completed';
                    break;
            }

            operation.status = OperationStatus.COMPLETED;
            db.close();

        } catch (error) {
            operation.status = OperationStatus.FAILED;
            operation.errorMessage = error instanceof Error ? error.message : 'Unknown error';
        } finally {
            operation.endTime = new Date();
            await this.updateOperation(operation);
        }
    }

    private async executeQuery(db: sqlite3.Database, query: string): Promise<string> {
        return new Promise((resolve, reject) => {
            if (query.trim().toUpperCase().startsWith('SELECT')) {
                db.all(query, [], (err, rows) => {
                    if (err) reject(err);
                    else resolve(JSON.stringify(rows));
                });
            } else {
                db.run(query, [], function(err) {
                    if (err) reject(err);
                    else resolve(`Query executed successfully, ${this.changes} rows affected`);
                });
            }
        });
    }

    private async executeBackup(databaseName: string): Promise<void> {
        const fs = require('fs/promises');
        const backupName = `${databaseName}_backup_${new Date().toISOString().replace(/[:.]/g, '-')}.db`;
        await fs.copyFile(`${databaseName}.db`, backupName);
    }

    private async executeOptimization(db: sqlite3.Database): Promise<void> {
        return new Promise((resolve, reject) => {
            db.serialize(() => {
                db.run('VACUUM', (err) => {
                    if (err) reject(err);
                });
                db.run('REINDEX', (err) => {
                    if (err) reject(err);
                    else resolve();
                });
            });
        });
    }

    async getDatabaseStatus(databaseName: string): Promise<any> {
        try {
            const db = new sqlite3.Database(`${databaseName}.db`);
            
            const status = await new Promise((resolve, reject) => {
                db.serialize(() => {
                    db.get("SELECT page_count * page_size as size FROM pragma_page_count(), pragma_page_size()", (err, row: any) => {
                        if (err) reject(err);
                        
                        db.get("SELECT COUNT(*) as table_count FROM sqlite_master WHERE type='table'", (err2, row2: any) => {
                            if (err2) reject(err2);
                            else resolve({
                                name: databaseName,
                                size: row?.size || 0,
                                tableCount: row2?.table_count || 0,
                                status: 'online'
                            });
                        });
                    });
                });
            });

            db.close();
            return status;

        } catch (error) {
            return {
                name: databaseName,
                status: 'error',
                errorMessage: error instanceof Error ? error.message : 'Unknown error'
            };
        }
    }

    async getOperationResult(operationId: string): Promise<DatabaseOperation | null> {
        const query = 'SELECT * FROM database_operations WHERE id = ?';
        const row = await this.database.get(query, [operationId]);
        
        if (row) {
            return {
                id: row.id,
                databaseName: row.database_name,
                operationType: row.operation_type as DbOperationType,
                query: row.query,
                status: row.status as OperationStatus,
                startTime: new Date(row.start_time),
                endTime: row.end_time ? new Date(row.end_time) : undefined,
                result: row.result,
                errorMessage: row.error_message
            };
        }
        return null;
    }

    private async saveOperation(operation: DatabaseOperation): Promise<void> {
        const query = 'INSERT INTO database_operations (id, database_name, operation_type, query, status, start_time) VALUES (?, ?, ?, ?, ?, ?)';
        await this.database.run(query, [
            operation.id,
            operation.databaseName,
            operation.operationType,
            operation.query,
            operation.status,
            operation.startTime.toISOString()
        ]);
    }

    private async updateOperation(operation: DatabaseOperation): Promise<void> {
        const query = 'UPDATE database_operations SET status = ?, result = ?, error_message = ?, end_time = ? WHERE id = ?';
        await this.database.run(query, [
            operation.status,
            operation.result,
            operation.errorMessage,
            operation.endTime?.toISOString(),
            operation.id
        ]);
    }
}
```

----

### 🧪 Senaryo 10: Bir sistem güvenlik aracında kullanıcılar tarama parametrelerini belirtebilir. Sistem belirtilen parametrelerle güvenlik taraması yapar. Tarama sonuçları detaylı rapor halinde sunulur. Güvenlik durumu değerlendirilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

```csharp
[HttpPost("security-scan")]
public async Task<IActionResult> StartSecurityScan([FromBody] SecurityScanRequest request)
{
    var scan = new SecurityScan
    {
        Id = Guid.NewGuid(),
        ScanType = request.ScanType,
        TargetPath = request.TargetPath,
        Status = ScanStatus.Running,
        StartTime = DateTime.UtcNow
    };

    await _repository.CreateAsync(scan);
    _ = Task.Run(() => ExecuteScanAsync(scan));

    return Ok(new { ScanId = scan.Id, Status = scan.Status });
}

private async Task ExecuteScanAsync(SecurityScan scan)
{
    try
    {
        var results = new List<SecurityFinding>();

        switch (scan.ScanType)
        {
            case ScanType.VirusScan:
                results.AddRange(await PerformVirusScan(scan.TargetPath));
                break;
            case ScanType.VulnerabilityScan:
                results.AddRange(await PerformVulnerabilityScan(scan.TargetPath));
                break;
            case ScanType.PermissionAudit:
                results.AddRange(await PerformPermissionAudit(scan.TargetPath));
                break;
        }

        scan.Findings = results;
        scan.Status = ScanStatus.Completed;
        scan.RiskLevel = CalculateRiskLevel(results);
    }
    catch (Exception ex)
    {
        scan.Status = ScanStatus.Failed;
        scan.ErrorMessage = ex.Message;
    }
    finally
    {
        scan.EndTime = DateTime.UtcNow;
        await _repository.UpdateAsync(scan);
    }
}

private async Task<List<SecurityFinding>> PerformVirusScan(string targetPath)
{
    var findings = new List<SecurityFinding>();
    
    foreach (var file in Directory.GetFiles(targetPath, "*", SearchOption.AllDirectories))
    {
        if (await IsSuspiciousFile(file))
        {
            findings.Add(new SecurityFinding
            {
                Type = FindingType.SuspiciousFile,
                Severity = Severity.High,
                Description = $"Suspicious file detected: {Path.GetFileName(file)}",
                Location = file
            });
        }
    }
    
    return findings;
}

private async Task<List<SecurityFinding>> PerformVulnerabilityScan(string targetPath)
{
    var findings = new List<SecurityFinding>();
    
    // Check for common vulnerabilities
    if (await HasWeakPermissions(targetPath))
    {
        findings.Add(new SecurityFinding
        {
            Type = FindingType.WeakPermissions,
            Severity = Severity.Medium,
            Description = "Weak file permissions detected",
            Location = targetPath
        });
    }
    
    return findings;
}

private RiskLevel CalculateRiskLevel(List<SecurityFinding> findings)
{
    if (findings.Any(f => f.Severity == Severity.Critical))
        return RiskLevel.Critical;
    if (findings.Any(f => f.Severity == Severity.High))
        return RiskLevel.High;
    if (findings.Any(f => f.Severity == Severity.Medium))
        return RiskLevel.Medium;
    
    return RiskLevel.Low;
}

[HttpGet("scan-report/{scanId}")]
public async Task<IActionResult> GetScanReport(Guid scanId)
{
    var scan = await _repository.GetByIdAsync(scanId);
    
    return Ok(new {
        ScanId = scan.Id,
        Status = scan.Status,
        RiskLevel = scan.RiskLevel,
        FindingsCount = scan.Findings?.Count ?? 0,
        Findings = scan.Findings
    });
}

public enum ScanType { VirusScan, VulnerabilityScan, PermissionAudit }
public enum ScanStatus { Running, Completed, Failed }
public enum RiskLevel { Low, Medium, High, Critical }
public enum Severity { Low, Medium, High, Critical }
```

----

### 🧪 Senaryo 10: Bir sistem güvenlik aracında kullanıcılar tarama parametrelerini belirtebilir. Sistem belirtilen parametrelerle güvenlik taraması yapar. Tarama sonuçları detaylı rapor halinde sunulur. Güvenlik durumu değerlendirilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

```python
import os
import hashlib
import asyncio
from datetime import datetime

class SecurityScanService:
    def __init__(self, database):
        self.db = database
    
    async def start_security_scan(self, scan_type, target_path, user_id):
        if not os.path.exists(target_path):
            raise ValueError("Target path does not exist")
        
        scan = {
            'id': str(uuid.uuid4()),
            'scan_type': scan_type,
            'target_path': target_path,
            'status': 'running',
            'start_time': datetime.now(),
            'user_id': user_id
        }
        
        self.save_scan(scan)
        asyncio.create_task(self.execute_scan_async(scan))
        
        return {'scan_id': scan['id'], 'status': scan['status']}
    
    async def execute_scan_async(self, scan):
        try:
            findings = []
            
            if scan['scan_type'] == 'virus_scan':
                findings.extend(await self.perform_virus_scan(scan['target_path']))
            elif scan['scan_type'] == 'vulnerability_scan':
                findings.extend(await self.perform_vulnerability_scan(scan['target_path']))
            elif scan['scan_type'] == 'permission_audit':
                findings.extend(await self.perform_permission_audit(scan['target_path']))
            
            scan['findings'] = findings
            scan['status'] = 'completed'
            scan['risk_level'] = self.calculate_risk_level(findings)
        except Exception as e:
            scan['status'] = 'failed'
            scan['error_message'] = str(e)
        finally:
            scan['end_time'] = datetime.now()
            self.update_scan(scan)
    
    async def perform_virus_scan(self, target_path):
        findings = []
        suspicious_extensions = ['.exe', '.scr', '.bat', '.com', '.pif']
        
        for root, dirs, files in os.walk(target_path):
            for file in files:
                file_path = os.path.join(root, file)
                
                # Check suspicious extensions
                if any(file.lower().endswith(ext) for ext in suspicious_extensions):
                    findings.append({
                        'type': 'suspicious_file',
                        'severity': 'high',
                        'description': f'Suspicious file detected: {file}',
                        'location': file_path
                    })
                
                # Check file size (very large files might be suspicious)
                try:
                    if os.path.getsize(file_path) > 100 * 1024 * 1024:  # 100MB
                        findings.append({
                            'type': 'large_file',
                            'severity': 'medium',
                            'description': f'Unusually large file: {file}',
                            'location': file_path
                        })
                except OSError:
                    pass
        
        return findings
    
    async def perform_vulnerability_scan(self, target_path):
        findings = []
        
        # Check file permissions
        try:
            stat_info = os.stat(target_path)
            permissions = oct(stat_info.st_mode)[-3:]
            
            if permissions == '777':
                findings.append({
                    'type': 'weak_permissions',
                    'severity': 'high',
                    'description': 'Directory has overly permissive permissions (777)',
                    'location': target_path
                })
        except OSError:
            pass
        
        # Check for common vulnerable files
        vulnerable_files = ['.htaccess', 'config.php', 'database.yml']
        for root, dirs, files in os.walk(target_path):
            for file in files:
                if file in vulnerable_files:
                    findings.append({
                        'type': 'vulnerable_config',
                        'severity': 'medium',
                        'description': f'Potentially vulnerable configuration file: {file}',
                        'location': os.path.join(root, file)
                    })
        
        return findings
    
    async def perform_permission_audit(self, target_path):
        findings = []
        
        for root, dirs, files in os.walk(target_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    stat_info = os.stat(file_path)
                    
                    # Check if file is world-writable
                    if stat_info.st_mode & 0o002:
                        findings.append({
                            'type': 'world_writable',
                            'severity': 'medium',
                            'description': f'File is world-writable: {file}',
                            'location': file_path
                        })
                except OSError:
                    pass
        
        return findings
    
    def calculate_risk_level(self, findings):
        if any(f['severity'] == 'critical' for f in findings):
            return 'critical'
        elif any(f['severity'] == 'high' for f in findings):
            return 'high'
        elif any(f['severity'] == 'medium' for f in findings):
            return 'medium'
        else:
            return 'low'
    
    def get_scan_report(self, scan_id):
        scan = self.get_scan(scan_id)
        if not scan:
            return None
        
        return {
            'scan_id': scan['id'],
            'status': scan['status'],
            'risk_level': scan.get('risk_level', 'unknown'),
            'findings_count': len(scan.get('findings', [])),
            'findings': scan.get('findings', [])
        }
    
    def save_scan(self, scan):
        query = "INSERT INTO security_scans (id, scan_type, target_path, status, start_time, user_id) VALUES (?, ?, ?, ?, ?, ?)"
        self.db.execute(query, (scan['id'], scan['scan_type'], scan['target_path'], 
                               scan['status'], scan['start_time'], scan['user_id']))
        self.db.commit()
    
    def update_scan(self, scan):
        query = "UPDATE security_scans SET status = ?, risk_level = ?, end_time = ?, error_message = ? WHERE id = ?"
        self.db.execute(query, (scan['status'], scan.get('risk_level'), scan.get('end_time'), 
                               scan.get('error_message'), scan['id']))
        self.db.commit()
    
    def get_scan(self, scan_id):
        query = "SELECT * FROM security_scans WHERE id = ?"
        row = self.db.execute(query, (scan_id,)).fetchone()
        return {'id': row[0], 'scan_type': row[1], 'status': row[3], 'risk_level': row[6]} if row else None
```

----

### 🧪 Senaryo 10: Bir sistem güvenlik aracında kullanıcılar tarama parametrelerini belirtebilir. Sistem belirtilen parametrelerle güvenlik taraması yapar. Tarama sonuçları detaylı rapor halinde sunulur. Güvenlik durumu değerlendirilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

```typescript
import * as fs from 'fs/promises';
import * as path from 'path';
import { v4 as uuidv4 } from 'uuid';

enum ScanType {
    VIRUS_SCAN = 'virus_scan',
    VULNERABILITY_SCAN = 'vulnerability_scan',
    PERMISSION_AUDIT = 'permission_audit'
}

enum ScanStatus {
    RUNNING = 'running',
    COMPLETED = 'completed',
    FAILED = 'failed'
}

enum RiskLevel {
    LOW = 'low',
    MEDIUM = 'medium',
    HIGH = 'high',
    CRITICAL = 'critical'
}

enum Severity {
    LOW = 'low',
    MEDIUM = 'medium',
    HIGH = 'high',
    CRITICAL = 'critical'
}

interface SecurityFinding {
    type: string;
    severity: Severity;
    description: string;
    location: string;
}

interface SecurityScan {
    id: string;
    scanType: ScanType;
    targetPath: string;
    status: ScanStatus;
    startTime: Date;
    endTime?: Date;
    findings: SecurityFinding[];
    riskLevel?: RiskLevel;
    errorMessage?: string;
}

class SecurityScanService {
    constructor(private database: any) {}

    async startSecurityScan(
        scanType: ScanType,
        targetPath: string,
        userId: string
    ): Promise<{ scanId: string; status: string }> {
        try {
            await fs.access(targetPath);
        } catch {
            throw new Error('Target path does not exist');
        }

        const scan: SecurityScan = {
            id: uuidv4(),
            scanType,
            targetPath,
            status: ScanStatus.RUNNING,
            startTime: new Date(),
            findings: []
        };

        await this.saveScan(scan);
        this.executeScanAsync(scan).catch(console.error);

        return { scanId: scan.id, status: scan.status };
    }

    private async executeScanAsync(scan: SecurityScan): Promise<void> {
        try {
            const findings: SecurityFinding[] = [];

            switch (scan.scanType) {
                case ScanType.VIRUS_SCAN:
                    findings.push(...await this.performVirusScan(scan.targetPath));
                    break;
                case ScanType.VULNERABILITY_SCAN:
                    findings.push(...await this.performVulnerabilityScan(scan.targetPath));
                    break;
                case ScanType.PERMISSION_AUDIT:
                    findings.push(...await this.performPermissionAudit(scan.targetPath));
                    break;
            }

            scan.findings = findings;
            scan.status = ScanStatus.COMPLETED;
            scan.riskLevel = this.calculateRiskLevel(findings);

        } catch (error) {
            scan.status = ScanStatus.FAILED;
            scan.errorMessage = error instanceof Error ? error.message : 'Unknown error';
        } finally {
            scan.endTime = new Date();
            await this.updateScan(scan);
        }
    }

    private async performVirusScan(targetPath: string): Promise<SecurityFinding[]> {
        const findings: SecurityFinding[] = [];
        const suspiciousExtensions = ['.exe', '.scr', '.bat', '.com', '.pif'];

        await this.scanDirectory(targetPath, async (filePath) => {
            const fileName = path.basename(filePath);
            
            // Check suspicious extensions
            if (suspiciousExtensions.some(ext => fileName.toLowerCase().endsWith(ext))) {
                findings.push({
                    type: 'suspicious_file',
                    severity: Severity.HIGH,
                    description: `Suspicious file detected: ${fileName}`,
                    location: filePath
                });
            }

            // Check file size
            try {
                const stats = await fs.stat(filePath);
                if (stats.size > 100 * 1024 * 1024) { // 100MB
                    findings.push({
                        type: 'large_file',
                        severity: Severity.MEDIUM,
                        description: `Unusually large file: ${fileName}`,
                        location: filePath
                    });
                }
            } catch {
                // Skip files we can't stat
            }
        });

        return findings;
    }

    private async performVulnerabilityScan(targetPath: string): Promise<SecurityFinding[]> {
        const findings: SecurityFinding[] = [];

        // Check directory permissions
        try {
            const stats = await fs.stat(targetPath);
            const mode = (stats.mode & parseInt('777', 8)).toString(8);
            
            if (mode === '777') {
                findings.push({
                    type: 'weak_permissions',
                    severity: Severity.HIGH,
                    description: 'Directory has overly permissive permissions (777)',
                    location: targetPath
                });
            }
        } catch {
            // Skip if we can't check permissions
        }

        // Check for vulnerable files
        const vulnerableFiles = ['.htaccess', 'config.php', 'database.yml'];
        
        await this.scanDirectory(targetPath, async (filePath) => {
            const fileName = path.basename(filePath);
            
            if (vulnerableFiles.includes(fileName)) {
                findings.push({
                    type: 'vulnerable_config',
                    severity: Severity.MEDIUM,
                    description: `Potentially vulnerable configuration file: ${fileName}`,
                    location: filePath
                });
            }
        });

        return findings;
    }

    private async performPermissionAudit(targetPath: string): Promise<SecurityFinding[]> {
        const findings: SecurityFinding[] = [];

        await this.scanDirectory(targetPath, async (filePath) => {
            try {
                const stats = await fs.stat(filePath);
                const fileName = path.basename(filePath);
                
                // Check if file is world-writable (simplified check)
                if (stats.mode & 0o002) {
                    findings.push({
                        type: 'world_writable',
                        severity: Severity.MEDIUM,
                        description: `File is world-writable: ${fileName}`,
                        location: filePath
                    });
                }
            } catch {
                // Skip files we can't check
            }
        });

        return findings;
    }

    private async scanDirectory(dirPath: string, fileHandler: (filePath: string) => Promise<void>): Promise<void> {
        try {
            const items = await fs.readdir(dirPath);

            for (const item of items) {
                const itemPath = path.join(dirPath, item);
                const stats = await fs.stat(itemPath);

                if (stats.isFile()) {
                    await fileHandler(itemPath);
                } else if (stats.isDirectory()) {
                    await this.scanDirectory(itemPath, fileHandler);
                }
            }
        } catch {
            // Skip directories we can't access
        }
    }

    private calculateRiskLevel(findings: SecurityFinding[]): RiskLevel {
        if (findings.some(f => f.severity === Severity.CRITICAL)) {
            return RiskLevel.CRITICAL;
        } else if (findings.some(f => f.severity === Severity.HIGH)) {
            return RiskLevel.HIGH;
        } else if (findings.some(f => f.severity === Severity.MEDIUM)) {
            return RiskLevel.MEDIUM;
        } else {
            return RiskLevel.LOW;
        }
    }

    async getScanReport(scanId: string): Promise<any> {
        const scan = await this.getScan(scanId);
        if (!scan) return null;

        return {
            scanId: scan.id,
            status: scan.status,
            riskLevel: scan.riskLevel,
            findingsCount: scan.findings.length,
            findings: scan.findings
        };
    }

    private async saveScan(scan: SecurityScan): Promise<void> {
        const query = 'INSERT INTO security_scans (id, scan_type, target_path, status, start_time) VALUES (?, ?, ?, ?, ?)';
        await this.database.run(query, [scan.id, scan.scanType, scan.targetPath, scan.status, scan.startTime.toISOString()]);
    }

    private async updateScan(scan: SecurityScan): Promise<void> {
        const query = 'UPDATE security_scans SET status = ?, risk_level = ?, end_time = ?, error_message = ? WHERE id = ?';
        await this.database.run(query, [
            scan.status,
            scan.riskLevel,
            scan.endTime?.toISOString(),
            scan.errorMessage,
            scan.id
        ]);
    }

    private async getScan(scanId: string): Promise<SecurityScan | null> {
        const query = 'SELECT * FROM security_scans WHERE id = ?';
        const row = await this.database.get(query, [scanId]);
        
        if (row) {
            return {
                id: row.id,
                scanType: row.scan_type as ScanType,
                targetPath: row.target_path,
                status: row.status as ScanStatus,
                startTime: new Date(row.start_time),
                endTime: row.end_time ? new Date(row.end_time) : undefined,
                findings: [], // Would load from separate table in real implementation
                riskLevel: row.risk_level as RiskLevel,
                errorMessage: row.error_message
            };
        }
        return null;
    }
}
```