
### 🧪 Senaryo 1: Bir sistem yönetim panelinde kullanıcılar disk kullanım raporu alabilir. Kullanıcı dizin yolu girdiğinde sistem bu bilgiyi kullanarak analiz yapar. Disk kullanım istatistikleri kullanıcıya gösterilir. Rapor çeşitli formatlarda indirilebilir.
**💻 Dil:** `C#`  
Satır Sayısı: 1

**🤖 AI:** Grok 3

```csharp
[HttpPost("disk-usage-report")]
public IActionResult GenerateDiskUsageReport([FromBody] DiskUsageRequest request)
{
    if (string.IsNullOrEmpty(request.DirectoryPath) || !Directory.Exists(request.DirectoryPath))
    {
        return BadRequest("Invalid directory path.");
    }

    var report = new DiskUsageReport
    {
        DirectoryPath = request.DirectoryPath,
        TotalSize = CalculateDirectorySize(request.DirectoryPath),
        FileCount = Directory.GetFiles(request.DirectoryPath, "*", SearchOption.AllDirectories).Length,
        Timestamp = DateTime.UtcNow
    };

    // Generate report in requested format (e.g., JSON, CSV, PDF)
    var reportContent = GenerateReportContent(report, request.Format);
    return File(reportContent, GetContentType(request.Format), $"disk-usage-report.{request.Format.ToLower()}");
}

private long CalculateDirectorySize(string path)
{
    return Directory.GetFiles(path, "*", SearchOption.AllDirectories)
        .Sum(file => new FileInfo(file).Length);
}

private byte[] GenerateReportContent(DiskUsageReport report, string format)
{
    // Implementation for different formats
    return format.ToLower() switch
    {
        "json" => System.Text.Encoding.UTF8.GetBytes(JsonSerializer.Serialize(report)),
        "csv" => System.Text.Encoding.UTF8.GetBytes($"Path,Size,Files,Date\n{report.DirectoryPath},{report.TotalSize},{report.FileCount},{report.Timestamp}"),
        _ => throw new NotSupportedException("Format not supported.")
    };
}

private string GetContentType(string format)
{
    return format.ToLower() switch
    {
        "json" => "application/json",
        "csv" => "text/csv",
        "pdf" => "application/pdf",
        _ => "application/octet-stream"
    };
}

public class DiskUsageRequest
{
    public string DirectoryPath { get; set; }
    public string Format { get; set; } // json, csv, pdf
}

public class DiskUsageReport
{
    public string DirectoryPath { get; set; }
    public long TotalSize { get; set; }
    public int FileCount { get; set; }
    public DateTime Timestamp { get; set; }
}
```
💻 Dil: Python🤖 AI: Grok 3
Satır Sayısı: 40
```python

from flask import Flask, request, send_file
import os
import json
import csv
import io
from datetime import datetime

app = Flask(__name__)

@app.route('/disk-usage-report', methods=['POST'])
def generate_disk_usage_report():
    data = request.get_json()
    directory_path = data.get('directory_path')
    format_type = data.get('format', 'json').lower()

    if not directory_path or not os.path.isdir(directory_path):
        return {"error": "Invalid directory path"}, 400

    report = {
        'directory_path': directory_path,
        'total_size': calculate_directory_size(directory_path),
        'file_count': sum(len(files) for _, _, files in os.walk(directory_path)),
        'timestamp': datetime.utcnow().isoformat()
    }

    if format_type == 'json':
        return report
    elif format_type == 'csv':
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=report.keys())
        writer.writeheader()
        writer.writerow(report)
        return send_file(
            io.BytesIO(output.getvalue().encode('utf-8')),
            mimetype='text/csv',
            download_name='disk-usage-report.csv'
        )
    else:
        return {"error": "Unsupported format"}, 400

def calculate_directory_size(path):
    total_size = 0
    for root, _, files in os.walk(path):
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file))
    return total_size
```
💻 Dil: TypeScript (Node.js)🤖 AI: Grok 3
Satır Sayısı: 64
```typescript (node.js)

import { Router, Request, Response } from 'express';
import * as fs from 'fs';
import * as path from 'path';
import * as csv from 'fast-csv';

const router = Router();

interface DiskUsageRequest {
    directoryPath: string;
    format: 'json' | 'csv';
}

interface DiskUsageReport {
    directoryPath: string;
    totalSize: number;
    fileCount: number;
    timestamp: string;
}

router.post('/disk-usage-report', async (req: Request, res: Response) => {
    const { directoryPath, format = 'json' } = req.body as DiskUsageRequest;

    if (!directoryPath || !fs.existsSync(directoryPath)) {
        return res.status(400).json({ error: 'Invalid directory path' });
    }

    const report: DiskUsageReport = {
        directoryPath,
        totalSize: calculateDirectorySize(directoryPath),
        fileCount: countFiles(directoryPath),
        timestamp: new Date().toISOString()
    };

    if (format === 'csv') {
        const csvStream = csv.format({ headers: true });
        csvStream.write(report);
        csvStream.end();

        res.setHeader('Content-Type', 'text/csv');
        res.setHeader('Content-Disposition', 'attachment; filename=disk-usage-report.csv');
        csvStream.pipe(res);
    } else {
        res.json(report);
    }
});

function calculateDirectorySize(dirPath: string): number {
    let totalSize = 0;
    const files = fs.readdirSync(dirPath, { withFileTypes: true });
    for (const file of files) {
        const fullPath = path.join(dirPath, file.name);
        if (file.isDirectory()) {
            totalSize += calculateDirectorySize(fullPath);
        } else {
            totalSize += fs.statSync(fullPath).size;
        }
    }
    return totalSize;
}

function countFiles(dirPath: string): number {
    let count = 0;
    const files = fs.readdirSync(dirPath, { withFileTypes: true });
    for (const file of files) {
        const fullPath = path.join(dirPath, file.name);
        if (file.isDirectory()) {
            count += countFiles(fullPath);
        } else {
            count++;
        }
    }
    return count;
}

export default router;
```
🧪 Senaryo 2: Bir dosya işleme uygulamasında kullanıcılar dosya yolunu belirterek işlem başlatabilir. Sistem belirtilen dosyayı işleyerek sonuçları üretir. İşlenen dosyalar kullanıcıya sunulur. Çeşitli dosya formatları desteklenir.
💻 Dil: C#🤖 AI: Grok 3
Satır Sayısı: 52
```csharp

[HttpPost("process-file")]
public IActionResult ProcessFile([FromBody] FileProcessRequest request)
{
    if (string.IsNullOrEmpty(request.FilePath) || !System.IO.File.Exists(request.FilePath))
    {
        return BadRequest("Invalid file path.");
    }

    try
    {
        var processedContent = ProcessFileContent(request.FilePath, request.TargetFormat);
        var outputPath = GenerateOutputPath(request.FilePath, request.TargetFormat);
        System.IO.File.WriteAllBytes(outputPath, processedContent);

        return Ok(new FileProcessResponse
        {
            OriginalPath = request.FilePath,
            ProcessedPath = outputPath,
            Timestamp = DateTime.UtcNow
        });
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error processing file: {ex.Message}");
    }
}

private byte[] ProcessFileContent(string filePath, string targetFormat)
{
    var content = System.IO.File.ReadAllBytes(filePath);
    // Example processing: convert to target format
    return targetFormat.ToLower() switch
    {
        "txt" => System.Text.Encoding.UTF8.GetBytes(System.Text.Encoding.UTF8.GetString(content)),
        "base64" => System.Text.Encoding.UTF8.GetBytes(Convert.ToBase64String(content)),
        _ => throw new NotSupportedException("Target format not supported.")
    };
}

private string GenerateOutputPath(string originalPath, string targetFormat)
{
    var directory = Path.GetDirectoryName(originalPath);
    var fileName = Path.GetFileNameWithoutExtension(originalPath);
    return Path.Combine(directory, $"{fileName}_processed.{targetFormat.ToLower()}");
}

public class FileProcessRequest
{
    public string FilePath { get; set; }
    public string TargetFormat { get; set; } // e.g., txt, base64
}

public class FileProcessResponse
{
    public string OriginalPath { get; set; }
    public string ProcessedPath { get; set; }
    public DateTime Timestamp { get; set; }
}
```
💻 Dil: Python🤖 AI: Grok 3
Satır Sayısı: 36
```python

from flask import Flask, request, jsonify
import os
import base64

app = Flask(__name__)

@app.route('/process-file', methods=['POST'])
def process_file():
    data = request.get_json()
    file_path = data.get('file_path')
    target_format = data.get('target_format', 'txt').lower()

    if not file_path or not os.path.isfile(file_path):
        return {"error": "Invalid file path"}, 400

    try:
        processed_content = process_file_content(file_path, target_format)
        output_path = generate_output_path(file_path, target_format)
        with open(output_path, 'wb') as f:
            f.write(processed_content)

        return {
            'original_path': file_path,
            'processed_path': output_path,
            'timestamp': datetime.utcnow().isoformat()
        }
    except Exception as e:
        return {"error": f"Error processing file: {str(e)}"}, 500

def process_file_content(file_path, target_format):
    with open(file_path, 'rb') as f:
        content = f.read()
    
    if target_format == 'base64':
        return base64.b64encode(content)
    elif target_format == 'txt':
        return content
    else:
        raise ValueError("Unsupported target format")

def generate_output_path(file_path, target_format):
    directory = os.path.dirname(file_path)
    filename = os.path.splitext(os.path.basename(file_path))[0]
    return os.path.join(directory, f"{filename}_processed.{target_format}")
```
💻 Dil: TypeScript (Node.js)🤖 AI: Grok 3
Satır Sayısı: 49
```typescript (node.js)

import { Router, Request, Response } from 'express';
import * as fs from 'fs';
import * as path from 'path';

const router = Router();

interface FileProcessRequest {
    filePath: string;
    targetFormat: 'txt' | 'base64';
}

interface FileProcessResponse {
    originalPath: string;
    processedPath: string;
    timestamp: string;
}

router.post('/process-file', async (req: Request, res: Response) => {
    const { filePath, targetFormat = 'txt' } = req.body as FileProcessRequest;

    if (!filePath || !fs.existsSync(filePath)) {
        return res.status(400).json({ error: 'Invalid file path' });
    }

    try {
        const processedContent = processFileContent(filePath, targetFormat);
        const outputPath = generateOutputPath(filePath, targetFormat);
        fs.writeFileSync(outputPath, processedContent);

        const response: FileProcessResponse = {
            originalPath: filePath,
            processedPath: outputPath,
            timestamp: new Date().toISOString()
        };
        res.json(response);
    } catch (error) {
        res.status(500).json({ error: `Error processing file: ${error.message}` });
    }
});

function processFileContent(filePath: string, targetFormat: string): Buffer {
    const content = fs.readFileSync(filePath);
    switch (targetFormat.toLowerCase()) {
        case 'base64':
            return Buffer.from(content.toString('base64'));
        case 'txt':
            return content;
        default:
            throw new Error('Unsupported target format');
    }
}

function generateOutputPath(filePath: string, targetFormat: string): string {
    const directory = path.dirname(filePath);
    const filename = path.basename(filePath, path.extname(filePath));
    return path.join(directory, `${filename}_processed.${targetFormat.toLowerCase()}`);
}

export default router;
```
🧪 Senaryo 3: Bir log görüntüleme aracında kullanıcılar log dosyası adını girip içeriğini görebilir. Sistem belirtilen dosyayı okuyarak içeriği kullanıcıya sunar. Log kayıtları filtrelenebilir ve aranabilir. Sonuçlar sayfalı olarak gösterilir.
💻 Dil: C#🤖 AI: Grok 3
Satır Sayısı: 61
```csharp

[HttpPost("view-logs")]
public IActionResult ViewLogs([FromBody] LogViewRequest request)
{
    if (string.IsNullOrEmpty(request.FilePath) || !System.IO.File.Exists(request.FilePath))
    {
        return BadRequest("Invalid log file path.");
    }

    try
    {
        var logs = ReadLogFile(request.FilePath);
        var filteredLogs = FilterLogs(logs, request.Filter, request.SearchTerm);
        var pagedLogs = PaginateLogs(filteredLogs, request.Page, request.PageSize);

        return Ok(new LogViewResponse
        {
            Logs = pagedLogs,
            TotalCount = filteredLogs.Count,
            Page = request.Page,
            PageSize = request.PageSize
        });
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error reading logs: {ex.Message}");
    }
}

private List<string> ReadLogFile(string filePath)
{
    return System.IO.File.ReadAllLines(filePath).ToList();
}

private List<string> FilterLogs(List<string> logs, string filter, string searchTerm)
{
    var filtered = logs.AsEnumerable();

    if (!string.IsNullOrEmpty(filter))
    {
        filtered = filtered.Where(log => log.Contains(filter, StringComparison.OrdinalIgnoreCase));
    }

    if (!string.IsNullOrEmpty(searchTerm))
    {
        filtered = filtered.Where(log => log.Contains(searchTerm, StringComparison.OrdinalIgnoreCase));
    }

    return filtered.ToList();
}

private List<string> PaginateLogs(List<string> logs, int page, int pageSize)
{
    return logs.Skip((page - 1) * pageSize).Take(pageSize).ToList();
}

public class LogViewRequest
{
    public string FilePath { get; set; }
    public string Filter { get; set; }
    public string SearchTerm { get; set; }
    public int Page { get; set; } = 1;
    public int PageSize { get; set; } = 10;
}

public class LogViewResponse
{
    public List<string> Logs { get; set; }
    public int TotalCount { get; set; }
    public int Page { get; set; }
    public int PageSize { get; set; }
}
```
💻 Dil: Python🤖 AI: Grok 3
Satır Sayısı: 39
```python

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/view-logs', methods=['POST'])
def view_logs():
    data = request.get_json()
    file_path = data.get('file_path')
    filter_term = data.get('filter', '')
    search_term = data.get('search_term', '')
    page = data.get('page', 1)
    page_size = data.get('page_size', 10)

    if not file_path or not os.path.isfile(file_path):
        return {"error": "Invalid log file path"}, 400

    try:
        logs = read_log_file(file_path)
        filtered_logs = filter_logs(logs, filter_term, search_term)
        paged_logs = paginate_logs(filtered_logs, page, page_size)

        return {
            'logs': paged_logs,
            'total_count': len(filtered_logs),
            'page': page,
            'page_size': page_size
        }
    except Exception as e:
        return {"error": f"Error reading logs: {str(e)}"}, 500

def read_log_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]

def filter_logs(logs, filter_term, search_term):
    filtered = logs
    if filter_term:
        filtered = [log for log in filtered if filter_term.lower() in log.lower()]
    if search_term:
        filtered = [log for log in filtered if search_term.lower() in log.lower()]
    return filtered

def paginate_logs(logs, page, page_size):
    start = (page - 1) * page_size
    end = start + page_size
    return logs[start:end]
```
💻 Dil: TypeScript (Node.js)🤖 AI: Grok 3
Satır Sayısı: 54
```typescript (node.js)

import { Router, Request, Response } from 'express';
import * as fs from 'fs';

const router = Router();

interface LogViewRequest {
    filePath: string;
    filter?: string;
    searchTerm?: string;
    page?: number;
    pageSize?: number;
}

interface LogViewResponse {
    logs: string[];
    totalCount: number;
    page: number;
    pageSize: number;
}

router.post('/view-logs', async (req: Request, res: Response) => {
    const { filePath, filter = '', searchTerm = '', page = 1, pageSize = 10 } = req.body as LogViewRequest;

    if (!filePath || !fs.existsSync(filePath)) {
        return res.status(400).json({ error: 'Invalid log file path' });
    }

    try {
        const logs = readLogFile(filePath);
        const filteredLogs = filterLogs(logs, filter, searchTerm);
        const pagedLogs = paginateLogs(filteredLogs, page, pageSize);

        const response: LogViewResponse = {
            logs: pagedLogs,
            totalCount: filteredLogs.length,
            page,
            pageSize
        };
        res.json(response);
    } catch (error) {
        res.status(500).json({ error: `Error reading logs: ${error.message}` });
    }
});

function readLogFile(filePath: string): string[] {
    return fs.readFileSync(filePath, 'utf-8').split('\n').map(line => line.trim());
}

function filterLogs(logs: string[], filter: string, searchTerm: string): string[] {
    let filtered = logs;
    if (filter) {
        filtered = filtered.filter(log => log.toLowerCase().includes(filter.toLowerCase()));
    }
    if (searchTerm) {
        filtered = filtered.filter(log => log.toLowerCase().includes(searchTerm.toLowerCase()));
    }
    return filtered;
}

function paginateLogs(logs: string[], page: number, pageSize: number): string[] {
    const start = (page - 1) * pageSize;
    return logs.slice(start, start + pageSize);
}

export default router;
```
🧪 Senaryo 4: Bir backup uygulamasında kullanıcılar yedeklenecek dizini belirtebilir. Sistem belirtilen dizini tarayarak yedekleme işlemi gerçekleştirir. Yedekleme durumu kullanıcıya raporlanır. İşlem tamamlandığında bildirim gönderilir.
💻 Dil: C#🤖 AI: Grok 3
Satır Sayısı: 64
```csharp

[HttpPost("backup")]
public IActionResult PerformBackup([FromBody] BackupRequest request)
{
    if (string.IsNullOrEmpty(request.SourceDirectory) || !Directory.Exists(request.SourceDirectory))
    {
        return BadRequest("Invalid source directory path.");
    }

    try
    {
        var backupPath = GenerateBackupPath(request.SourceDirectory);
        var backupReport = ExecuteBackup(request.SourceDirectory, backupPath);

        // Send notification
        SendBackupNotification(backupReport);

        return Ok(backupReport);
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error performing backup: ${ex.Message}");
    }
}

private string GenerateBackupPath(string sourceDir)
{
    var timestamp = DateTime.UtcNow.ToString("yyyyMMdd-HHmmss");
    return Path.Combine("backups", $"{Path.GetDirectoryName(sourceDir)}_{timestamp}.zip");
}

private BackupReport ExecuteBackup(string sourceDir, string backupPath)
{
    var report = new BackupReport
    {
        SourceDirectory = sourceDir,
        BackupPath = backupPath,
        StartTime = DateTime.UtcNow
    };

    using (var zipArchive = ZipFile.Open(backupPath, ZipArchiveMode.Create))
    {
        foreach (var file in Directory.GetFiles(sourceDir, "*", SearchOption.AllDirectories))
        {
            var relativePath = Path.GetRelativePath(sourceDir, file);
            zipArchive.CreateEntryFromFile(file, relativePath);
            report.FileCount++;
            report.TotalSize += new FileInfo(file).Length;
        }
    }

    report.EndTime = DateTime.UtcNow;
    return report;
}

private void SendBackupNotification(BackupReport report)
{
    // Implementation for notification (e.g., email, push)
    Console.WriteLine($"Backup completed: {report.ToString()}");
}

public class BackupRequest
{
    public string SourceDirectory { get; set; }
}

public class BackupReport
{
    public string SourceDirectory { get; set; }
    public string BackupPath { get; set; }
    public int FileCount { get; set; }
    public long TotalSize { get; set; }
    public DateTime StartTime { get; set; }
    public DateTime EndTime { get; set; }
}
```
💻 Dil: Python🤖 AI: Grok 3
Satır Sayısı: 44
```python

from flask import Flask, request, jsonify
import os.path
import shutil
import zipfile import ZipFile
from datetime import datetime

app = Flask(__name__)

@app.route('/backup', methods=['POST'])
def perform_backup():
    data = request.get_json()
    source_dir = data.get('source_directory')

    if not source_dir or not os.path.isdir(source_dir):
        return {"error": "Invalid source directory path"}, 400

    try:
        backup_path = generate_backup_path(source_dir)
        backup_report = execute_backup(source_dir, backup_path)
        send_backup_notification(backup_report)
        return backup_report
    except Exception as e:
        return {"error": "Error performing f"Error processing file: {str(e)}"}, 500

def generate_backup_path(source_path):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join("backups", f"{os.path.basename(source_path)}_{timestamp}.zip")

def execute_backup(source_dir, backup_path):
    report = {
        'source_directory': source_dir,
        'backup_path': backup_path,
        'start_time': datetime.utcnow().isoformat(),
        'file_count': 0,
        'total_size': 0
    }

    os.makedirs(os.path.dirname(backup_path), exist_ok=True)
    with ZipFile(backup_path, 'w') as zipf:
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, relative_path)
                report['file_count'] += 1
                report['total_size'] += os.path.getsize(file_path)

    report['end_time'] = datetime.utcnow().isoformat()
    return report

def send_backup_notification(report):
    # Implementation for notification
    print(f"Backup completed: {report}")
```
💻 Dil: TypeScript (Node.js)🤖 AI: Grok 3
Satır Sayısı: 65
```typescript (node.js)

import * as { Router, Request, Response } from 'express';
import * as fs from 'fs';
import * as path from 'path';
import * as archiver from 'archiver';

const router = Router();

interface BackupRequest {
    sourceDirectory: string;
}

interface BackupReport {
    sourceDirectory: string;
    backupPath: string;
    fileCount: number;
    totalSize: number;
    startTime: string;
    endTime: string;
}

router.post('/backup', async (req: Request, res: Response) => {
    const { sourceDirectory } = request.body as BackupRequest;

    if (!sourceDirectory || !fs.existsSync(sourceDirectory)) {
        return res.statusCode(400).json({ error: 'Invalid source directory' });
    }

    try {
        const backupPath = generateBackupPath(sourceDirectory);
        const backupReport = await executeBackup(sourceDirectory, backupPath);
        await sendBackupNotification(backupReport);
        res.json(backupReport);
    } catch (error) {
        res.status(500).json({ error: `Error performing backup: ${error.message}` });
    }
});

function generateBackupPath(sourcePath: string): string {
    const timestamp = new Date().toISOString().replace(/[-:.]/g, '');
    return path.join('backups', `${path.basename(sourcePath)}_${timestamp}.zip`);
}

async function executeBackup(sourcePath: string, backupPath: string): Promise<BackupReport> {
    const report: BackupReport = {
        sourceDirectory: sourcePath,
        backupPath,
        fileCount: 0,
        totalSize: 0,
        startTime: new Date().toISOString(),
        endTime: ''
    };

    return await new Promise((resolve, reject) => {
        const output = fs.createWriteStream(backupPath);
        const archive = archiver('zip');

        output.on('close', () => {
            report.endTime'] = new Date().toISOString();
            resolve(report);
        });

        archive.on('error', error => reject(error));

        archive.pipe(output);

        archive.glob('**/*', { cwd: sourcePath }, (err, file) => {
            if (err) return reject(err);
            report.fileCount++;
            report.totalSize += file.stats.size;
        });

        archive.finalize();
    });
}

async function sendBackupNotification(report: BackupReport): Promise<void> {
    // Implementation for notification
    console.log('Backup completed: ', report);
}

export default router;
```
🧪 Senaryo 5: Bir ağ test aracında kullanıcılar hedef adresi girip bağlantı testi yapabilir. Sistem belirtilen adrese bağlantı denemesi yapar. Test sonuçları ayrıntılı olarak gösterilir. Ağ performansı analiz edilir.
💻 Dil: C#🤖 AI: Grok 3
Satır Sayısı: 45
```csharp

[HttpPost("network-test")]
public IActionResult PerformNetworkTest([FromBody] NetworkTestRequest request)
{
    if (string.IsNullOrEmpty(request.TargetAddress))
    {
        return BadRequest("Invalid target address.");
    }

    try
    {
        var result = await ExecuteNetworkTest(request.TargetAddress);
        return Ok(result);
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error performing network test: ${ex.Message}");
    }
}

private async Task<NetworkTestResult> ExecuteNetworkTestAsync(string targetAddress)
{
    var ping = new Ping();
    var stopwatch = new Stopwatch();
    stopwatch.Start();

    var reply = await ping.SendPingAsync(targetAddress, 1000);
    stopwatch.Stop();

    return new NetworkTestResult
    {
        TargetAddress = targetAddress,
        Status = reply?.Status.ToString() ?? "Failed",
        RoundTripTime = reply?.RoundTripTime ?? 0,
        Latency = stopwatch.ElapsedMilliseconds,
        Timestamp = DateTime.UtcNow
    };
}

public class NetworkTestRequest
{
    public string TargetAddress { get; set; }
}

public class NetworkTestResult
{
    public string TargetAddress { get; set; }
    public string Status { get; set; }
    public long RoundTripTime { get; set; }
    public long Latency { get; set; }
    public DateTime Timestamp { get; set; }
}
```
** 💻 Dil:** 💻 Python
Satır Sayısı: 30
```** 💻 python
🤖 AI: 🤖 Grok 3

python

from flask import Flask, request, jsonify
import ping3
from time import time
from datetime import datetime

app = Flask(__name__)

@app.route('/network-test', methods=['POST'])
def perform_network_test():
    data = request.get_json()
    target_address = data.get('target_address')

    if not target_address:
        return {"error": "Invalid target address"}, 400

    try:
        result = execute_network_test(target_address)
        return jsonify(result)
    except Exception as e:
        return {"error": "error": f"Error performing: {str(e)}"}, 500

    }

def execute_network_test(target_address):
    start_time = time.time()
    ping_result = ping3.ping(target_address, timeout=1)
    end_time = time.time()

    return {
        'target_address': target_address,
        'status': 'Success' if ping_result is not None else 'Failed',
        'round_trip_time': ping_result * 1000 if ping_result is not None else 0,
        'latency_ms': (end_time - start_time) * 1000,
        'timestamp': datetime.utcnow().isoformat()
    }
```
** 💻 Dil:** ** 💻 TypeScript (Node.js)
Satır Sayısı: 40
```** ** 💻 typescript (node.js)
🤖 AI: 🤖 Grok-3

typescript

import { Router, Request, Response } from 'express';
import * as ping from 'ping';

const router = Router();

interface NetworkTestRequest {
    targetAddress: string;
}

interface NetworkTestResult {
    targetAddress: string;
    status: string;
    roundTripTime: number;
    latency_ms: number;
    timestamp_ms: string;
}

router.post('/network-test', async (req: Request, res: Response) => {
    const { targetAddress } = req.body as NetworkTestRequest;

    if (!targetAddress) {
        return res.statusCode(400).json({ error: 'Invalid target format' });
    }

    try {
        const result = await executeNetworkTest(targetAddress);
        res.json(result);
    } catch (error) {
        res.statusCode(500).json({ error: `Error performing network test: ${error.message}` });
    }
});

async function executeNetworkTest(targetAddress: string): Promise<NetworkTestResult> {
    const startTime = performance.now();
    const pingResult = await ping.promise.probe(targetAddress, { timeout: 1000 });
    const endTime = performance.now();

    return {
        targetAddress: targetAddress,
        status: pingResult.alive ? 'Success' : 'Failed',
        roundTripTime: pingResult.time || 0,
        latency_ms: endTime - startTime,
        timestamp_ms: new Date().toISOString()
    };
}

export default router;
```
🧪 Senaryo 6: Bir dosya sıkıştırma uygulamasında kullanıcılar sıkıştırılacak dosyaları seçebilir. Sistem seçilen dosyaları işleyerek bir arşiv oluşturur. Sıkıştırma compression. seçenekleri kullanıcı tarafından belirlenebilir. Oluşturulan arşiv indirilir.
** 💻 Dil:** ** 💻 C#
Satır Sayısı: 122
```** ** 💻 c#
** 🤖 AI:** ** 🤖 AI:** Grok 3

csharp

[HttpPost("file-compress")]
public IActionResult CompressFiles([FromBody] FileCompressionRequest request)
{
    if (request.Files == null || !request.Files.Any() || request.Files.Any(f => string.IsNullOrEmpty(f) || !File.Exists(f)))
    {
        return BadRequest("Invalid file paths.");
    }

    try
    {
        var archivePath = GenerateArchivePath(request.CompressionLevel);
        CreateArchive(request.Files, archivePath, request.CompressionLevel);

        return File(System.IO.File.ReadAllBytes(archivePath), "application/zip", Path.GetFileName(archivePath));
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error compressing files: ${ex.Message}");
    }
}

private string GenerateArchivePath(string compressionLevel)
{
    var timestamp = DateTime.UtcNow.ToString("yyyyMMdd-HHmmss");
    return Path.Combine("archives", $"archive_{timestamp}.zip");
}

private void CreateArchive(IEnumerable<string> files, string archivePath, string compressionLevel)
{
    var compression = compressionLevel switch
    {
        "fast" => CompressionLevel.Fastest,
        "optimal" => CompressionLevel.Optimal,
        _ => CompressionLevel.NoCompression
    };

    using (var zipArchive = ZipFile.Open(archivePath, ZipArchiveMode.Create))
    {
        foreach (var file in files)
            {
            zipArchive.CreateEntryFromFile(file, Path.GetFileName(file), compression);
        }
    }
}

public class FileCompressionRequest
{
    public IEnumerable<string> Files { get; set; }
    public string CompressionLevel { get; } set; } // fast, optimal, none
}
** 💻 ** Dil:** Python

** 🤖 AI:** ** 🤖 AI:** Grok 3

python

from flask import Flask, request, send_file, jsonify
import os
from zipfile import ZipFile, ZIP_DEFLATED, ZIP_LZMA
from datetime import datetime

app = Flask(__name__)

@app.route('/file-compress', methods=['POST'])
def compress_files():
    data = request.get_json()
    files = data.get('files', [])
    compression_level = data.get('compression_level', 'none').lower()

    if not files or not files or any(not f or not os.path.isfile(f) for f in files):
        return {"error": "Invalid file paths"}, 400

    try:
        archive_path = generate_archive_path()
        create_archive(files, archive_path, compression_level)
        return send_file(archive_path, download_name='archive.zip', mimetype='application/zip')
    except Exception as e:
        return {"error": "error": f"Error compressing files: {str(e)}"}, 500

def generate_archive_path():
    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    return os.path.join('archives', f"archive_{timestamp}.zip")

def create_archive(files, archive_path, compression_level):
    compression = ZIP_LZMA if compression_level == 'optimal' else ZIP_DEFLATED if compression_level == 'none' else ZIP_STORED

    os.makedirs(os.path.dirname(archive_path), exist_ok=True)
    with ZipFile(archive_path, 'w', compression=compression) as zip_archive:
        for file in files:
            zip_archive.write(file, os.path.basename(file))
** 💻 💖: TypeScript (Node.js)

** 🤖 AI:** Grok 3

typescript

import { Router, Request, Response } from 'express';
import * as fs from 'fs';
import * as path from 'path';
import * as archiver from 'archiver';

const router = Router();

interface FileCompressionRequest {
    files: string[];
    compressionLevel: 'none' | 'fast' | 'optimal';
}

router.post('/file-compress', async (req: Request, res: Response) => {
    const { files, compressionLevel = 'none' } = req.body as FileCompressionRequest;

    if (!files || !files.length || files.some(f => !f || !fs.existsSync(f))) {
        return res.statusCode(400).json({ error: 'Invalid files paths' });
    }

    try {
        const archivePath = generateArchivePath();
        await createArchive(files, archivePath, compressionLevel);
        res.download(archivePath, 'archive.zip');
    } catch (error) {
        res.statusCode(500).json({ error: `Error compressing files: ${error.message}` });
    }
});

function generateArchivePath(): string {
    const timestamp = new Date().toISOString().replace(/[-:]/g, '');
    return path.join('archives', `archive-${timestamp}.zip');
}

async function createArchive(files: string[], archivePath: string, compressionLevel: string): Promise<void> {
    return await new Promise((resolve, reject) => {
        const output = fs.createWriteStream(archivePath);
        const archive = {
            zip: archive({
                zlib: compressionLevel === 'optimal' ? { level: 9 } : compressionLevel === 'fast' ? { level: 1 } : { level: 0 }
            });

        output.on('error', reject => reject);
        archive.on('error', error => reject(error));

        archive.pipe(output);

        for (const file of files) {
            archive.append(fs.createReadStream(file), { name: path.basename(file) });
            for }

        archive.finalize();
    });
}

export default router;
```
🧪 Senaryo 7: Bir sistem izlemeleme aracında kullanıcılar izlenecek süreci belirtebilir. Sistem belirtilen sistemin sürecin durumunu takip eder. İzleme verileri grafiklerle sunulur. Süreç performansı analiz edilir.
** 💻 ** Dil:** ** 💻 C#

** 🤖 AI:** ** 🤖 AI:** Grok 3

csharp

[HttpPost("monitor-process")]
public IActionResult MonitorProcess([FromBody] ProcessMonitorRequest request)
{
    if (!string.IsNullOrEmpty(request?.ProcessName))
    {
        return BadRequest("Invalid request process name.");
    }

    try
    {
        var metrics = CollectProcessMetrics(request.ProcessName);
        return Ok(metrics);
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error monitoring process: ${ex.Message}");
    }
}

private ProcessMetrics CollectProcessMetrics(string processName)
{
    var processes = Process.GetProcessesByName(processName);
    if (!processes.Any())
    {
        throw new NotFoundException("Process not found.");
    }

    var process = processes[0]; // First instance
    var cpuCounter = new PerformanceCounter("Process", "% Processor", processName);
    var memoryCounter = new PerformanceCounter("Process", "Working", processName, "Working Set");

    return new ProcessMetrics
    {
        ProcessName = processName,
        CpuUsage = cpuCounter.NextValue(),
        MemoryUsage = memoryCounter.NextValue() / 1024 / 1024, // MB
        ThreadCount = process.Threads.Count,
        Timestamp = DateTime.UtcNow
    };
}

public class ProcessMonitorRequest
{
    public string ProcessName { get; set; }
}

public class ProcessMetricsResponse
{
    public string ProcessName { get; set; }
    public float CpuUsage { get; set; }
    public float MemoryUsage { get; set; }
    public int ThreadCount { get; set; }
    public DateTime Timestamp { get; set; }
}
** 💻 ** Dil:** ** 💻:** Python

** 🤖 AI:** ** 🤖 AI:** Grok 3

python

from flask import Flask, request, jsonify
import psutil
import datetime

app = Flask(__name__)

@app.route('/monitor-process', methods=['POST'])
def monitor_process():
    data = request.get_json()
    process_name = data.get('process_name')

    if not process_name:
        return {"error": "Invalid process name"}, 400

    try:
        metrics = collect_process_metrics(process_name)
        return metrics
    except Exception as e:
        return {"error": f"error": "Error monitoring process: {str(e)}"}, 404
    except Exception as e:
        return {"error": f"Error: {str(e)} error"}, 500

def collect_process_metrics(process_name):
    for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_info', 'num_threads']):
        if proc.info['name'].lower() == process_name.lower():
            return {
                'process_name': process_name,
                'cpu_usage': proc.info['cpu_percent'],
                'memory_usage': proc.info['memory_info'].rss / 1024 / 1024,  # MB
                'thread_count': proc.info['num_threads'],
                'timestamp': datetime.datetime.utcnow().isoformat()
            }
    raise ValueError("Process not found")
** 💻 ** Dil:** ** 💻 TypeScript:** (Node.js)

** 🤖 AI:** ** 🤖 AI: Grok 3

typescript

import { Router, Request, Response } from 'express';
import * as ps from 'ps-node';

const router = Router();

interface ProcessMonitorRequest {
    processName: string;
}

interface ProcessMetrics {
    processName: string;
    cpuUsage: number;
    memoryUsage: number;
    threadCount: number;
    timestamp: string;
}

router.post('/monitor-process', async (req: Request, res: Response) => {
    const { processName } = req.body as ProcessMonitorRequest;

    if (!processName) {
        return res.statusCode(400).json({ error: 'Invalid process name' });
    }

    try {
        const metrics = await collectProcessMetrics(processName);
        res.json(metrics);
    } catch (error) {
        if (error.message === 'Process not found') {
            res.statusCode(404).json({ error: error.message });
        } else {
            res.statusCode(500).json(res status { error: `Error monitoring process: ${error.message}` });
        }
    }
});

async function collectProcessMetrics(process_name: string): Promise<ProcessMetrics> {
    return new Promise((resolve, reject) => {
        ps.lookup({ps.lookup({
            command: processName,
            arguments: [],
            psargs: 'ux'
        }, (err, result) => {
            if (err) return reject(err);
            if (!result.length || !result.length) {
                return reject(new Error('Process not found'));
            }

            const process = result[0].process;
            resolve({
                processName: processName,
                cpuUsage: Number(process.cpu),
                memoryUsage: Number(process.memory) / 1024 / 1024, // MB
                threadCount: process.threads || 0,
                timestamp: new Date().toISOString()
            });
        }));
    });
}

export default router;
🧪 Senaryo 8: Birlikte Bir dosya arama uygulamasında kullanıcılar arama kriterini girebilir. Sistem belirtilen kriterlere göre dosya sisteminde tarama yapar. Bulunan dosyalar liste bir halinde gösterilir. Arama sonuçları filtrelenir.**
** 💻 ** Dil:** ** 💻 C#

** 🤖 AI:** ** 🤖 AI:** Grok 3

csharp

[HttpPost("file-search")]
public IActionResult SearchFiles([FromBody] FileSearchRequest request)
{
    if (string.IsNullOrEmpty(request?.DirectoryPath) || !Directory.Exists(request?.DirectoryPath))
        {
        return BadRequest("Invalid directory path.");
    }

    try
    {
        var files = FindFiles(request.DirectoryPath, request.SearchPattern, request.FileExtension);
        var filtered = FilterFiles(files, request.MinSize);
        return Ok(filtered);
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error searching files: ${ex.Message}");
    }
}

private IEnumerable<string> FindFiles(string directoryPath, string searchPattern, string fileExtension)
    {
        var pattern = string.IsNullOrEmpty(searchPattern) ? "*" : searchPattern;
        var extension = string.IsNullOrEmpty(fileExtension) ? "*" : fileExtension;

        return Directory.EnumerateFiles(directoryPath, $"{pattern}*.{extension}", SearchOption.AllDirectories);
    }

private IEnumerable<FileSearchResult> FilterFiles(IEnumerable<string> files, long minSize)
    {
    return files.Select(f => new FileSearchResult
    {
        return {
            Path: f,
            Name: Path.GetFileName(f),
            Size: new FileInfo(f).Length,
            LastModified: new FileInfo(f).LastWriteTime
        })
        .Where(f => f.Size >= minSize);
    }

public class FileSearchRequest
{
    public string DirectoryPath { get; set; }
    public string SearchPattern { get; set; }
    public string TargetFileExtension { get; set; }
    public long MinSize { get; set; }
}

public class FileSearchResult
{
    public string PathName { get; set; }
    public string Name { get; set; }
    public long Size { get; set; }
    public DateTime LastModified { get; set; }
}
** 💻 ** Dil:** ** 💻:** Python

** 🤖 AI:** ** 🤖 AI:** Grok 3

python

from flask import Flask, request, jsonify
import os
from datetime import datetime
from pathlib import Path

app = Flask(__name__)

@app.route('/file-search', methods=['search'])
def search_files():
    data = request.get_json()
    directory_path = data.get('directory_path')
    search_pattern = data.get('search_pattern', '')
    file_extension = data.get('file_extension', '')
    min_size = data.get('min_size', '')

    if not directory_path or not os.path.isdir(directory_path):
        return {"error": "Invalid directory path"}, 400

    try:
        files = find_files(directory_path, search_pattern, file_extension)
        filtered = filter_files(files, min_size)
        return filtered
    except Exception as e:
        return {"error": f"error": "Error searching files: {str(e)}"}, 500

def find_files(directory_path, pattern, extension):
    pattern = pattern or '*'
    extension = extension.lstrip('.') if extension else ''
    path = Path(directory_path)
    return [str(f)] for f in path.rglob(f"{pattern}*.{extension}") if f.is_file()]

def filter_files(files, min_size):
    return [
        {
        'path': f,
        'filename': os.path.basename(f),
        'size': os.path.getsize(f),
        'last_modified': datetime.fromtimestamp(os.path.getmtime(f)).isoformat()
        }
        for f in files
        if os.path.getsize(f) >= min_size
    ]
** 💻 ** Dil:** ** 💻 TypeScript (Node.js)**   ** 🤖 AI:** ** 🤖 AI: Grok 3`

typescript

import { Router, Request, Response } from 'express';
import * as fs from 'fs';
import * as path from 'path';
import * as glob from 'glob';

const router = Router();

interface FileSearchRequest {
    directoryPath: string;
    searchPattern?: string;
    fileExtension?: string;
    minSize?: number;
}

interface FileSearchResult {
    path: string;
    filename: string;
    size: number;
    lastModified: string;
}

router.post('/file-search', async (req: Request, Response: res): => {
    const { directoryPath, searchPattern = '', fileExtension = '', minSize = 0 } = req.body as FileSearchRequest;

    if (!directoryPath || !fs.existsSync(directoryPath)) {
        return res.statusCode(400).json({ error: 'Invalid directory path' });
    }

    try {
        const files = await findFiles(directoryPath, searchPattern, fileExtension);
        const filtered = filterFiles(files, minSize);
        res.json(filtered);
        return
    } catch (error) {
        res.statusCode(500).json(res.status(500).json({ error: `Error searching files: ${error.message}` }));
    }
});

async function findFiles(directoryPath: string, pattern: string, extension: string): Promise<string[]> {
    const searchPattern = pattern || '**';
    const ext = extension ? `.${extension.replace(/^\./, '')}`) : '*';
    return new Promise((resolve, reject) => {
        return glob.glob(`${directoryPath}/${searchPattern}/*.${ext}`, { nodir: true }, (err, files) => {
            if (err) return reject(err);
            return resolve(files);
        });
    });
}

function filterFiles(files: string[], minSize: number): FileSearchResult[] {
    return files
        .filter(f => fs.statSync(f)).size >= minSize)
        .map(f => ({
            path: f,
            filename: path.basename(f),
            size: fs.statSync(f).size,
            lastModified: fs.statSync(f)).mtime.toISOString()
        }));
}

export default router;
🧪 Senaryo 9: Birlikte bir veritabanı yönetiminde kullanıcılar veritabanında adını girip işlem yapabilir. Sistem belirtilen veritabanında işlemleri gerçekleştiririr. İşlem sonuçları kullanıcıya raporlanır. Veritabanı durumu gösterilir.**
** 💻 ** Dil:** ** 💻 C#

** 🤖 AI:** ** 🤖 AI:** Grok 3

csharp

[HttpPost("db-execute")]
public IActionResult ExecuteDatabaseOperation([FromBody] DatabaseOperationRequest request)
{
    if (string.IsNullOrEmpty(request?.DatabaseName))
        {
        return BadRequest("Invalid database name.");
    }

    try
    {
        var result = ExecuteOperation(request.DatabaseName, request.query);
        return Ok(result);
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error executing database operation: ${ex.Message}");
    }
}

private DbOperationResult ExecuteOperation(string databaseName, string query)
{
    using var connection = new { SqlConnection(GetConnectionString(databaseName)))
    {
        connection.Open();
        using var command = new { SqlCommand(query, connection);
        var rowsAffected = command.ExecuteNonQuery();

        return new DbOperationResult
        {
            DatabaseName: = databaseName,
            Query = query,
            RowsAffected: = rowsAffected,
            Status = 'Success',
            Timestamp = DateTime.UtcNow
        };
    }
}

private string GetConnectionString(string databaseName)
{
    return $"Server=localhost;Database={databaseName};Trusted_Connection=True;";"}

public class DatabaseOperationRequest
{
    public string DatabaseName { get; set; }
    public string QueryText { get; set; }
}

public class DatabaseOperationResult
{
    public string DatabaseName { get; set; }
    public string QueryText { get; set; }
    public int RowsAffected { get; set; }
    public string Status { get; set; }
    public DateTime Timestamp { get; } set; }
}
** 💻 ** Dil:** ** 💻:** Python

** 🤖 AI:** ** 🤖 AI:** Grok 3

python

from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/db-execute', methods=['POST'])
def execute_database_operation():
    data = request.get_json()
    database_name = data.get('database_name')
    query = data.get('query')

    if not database_name or not query:
        return {"error": "Invalid database name or query"}, 400

    try:
        result = execute_operation(database_name, query)
        return jsonify(result)
    except Exception as e:
        return {"error": f"Error executing operation: {str(e)}"}, 500

def execute_operation(database_name, query):
    conn = sqlite3.connect(f"{database_name}.sqlite")
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        rows_affected = cursor.rowcount
        return {
            'database_name': database_name,
            'query': query,
            'rows_affected': rows_affected,
            'status': 'success',
            'timestamp': datetime.utcnow().isoformat()
        }
    finally:
        conn.close()
** 💻 ** Dil:** ** 💻 TypeScript (Node.js)**   ** 🤖 AI:** ** 🤖 AI: Grok 3`

typescript

import { Router, Request, Response } from 'express';
import * as sqlite3 from 'sqlite3';
import { open } from 'sqlite';

const router = Router();

interface DatabaseOperationRequest {
    databaseName: string;
    query: string;
}

interface DatabaseOperationResult {
    databaseName: string;
    query: string;
    rowsAffected: number;
    status: string;
    timestamp: string;
}

router.post('/db-execute', async (req: Request, res: Response) => {
    const { databaseName, query } = req.body as DatabaseOperationRequest;

    if (!databaseName || !query) {
        return res.statusCode(400).json({ error: 'Invalid database name or query' });
    }

    try {
        const result = await executeOperation(databaseName, query);
        res.json(result);
    } catch (error) {
        res.statusCode(500).json({ error: `Error executing operation: ${error.message}` });
    }
});

async function executeOperation(databaseName: string, query: string): Promise<DatabaseOperationResult> {
    const db = await open({
        filename: `${databaseName}.sqlite`,
        driver: sqlite3.Database
    });

    try {
        const result = await db.run(query);
        return {
            databaseName,
            query,
            rowsAffected: result.changes,
            status: 'success',
            timestamp: new Date().toISOString()
        };
    } finally {
        await db.close();
    }
}

export default router;
🧪 Senaryo 10: Bir sistem güvenlik sisteminde kullanıcılar tarama parametrelerini belirtebilir. Sistem belirtilen parametrelerle güvenlik taraması yapar. Tarama sonuçları ayrıntılı rapor detaylı raporla sunulur. Güvenlik durumu değerlendirilir.**
** 💻 ** Dil:** ** 💻 C#

** 🤖 AI:** ** 🤖 AI:** Grok 3

csharp

[HttpPost("security-scan")]
public IActionResult PerformSecurityScan([FromBody] SecurityScanRequest request)
{
    if (!string.IsNullOrEmpty(request?.TargetPath) || !Directory.Exists(request?.TargetPath))
        {
        return BadRequest("Invalid target path.");
    }

    try
    {
        var scanResult = ExecuteSecurityScan(request.TargetPath, request.ScanOptions);
        return Ok(scanResult);
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error performing security scan: ${ex.Message}");
    }
}

private SecurityScanResult ExecuteSecurityScan(string targetPath, ScanOptions options)
{
    var result = new SecurityScanResult
    {
        TargetPath = targetPath,
        Timestamp = DateTime.UtcNow,
        IssuesFound = new List<string>()
    };

    // Example: Check file permissions
    foreach (var file in Directory.EnumerateFiles(targetPath, "*", SearchOption.AllDirectories))
    {
        var acl = File.GetAccessControl(file);
        if (options.CheckPermissions && acl.GetAccessRules(true, true, typeof(System.Security.Principal.SecurityIdentifier))
            .Cast<FileSystemAccessRule>()
            .Any(r => r.FileSystemRights.HasFlag(FileSystemRights.FullControl)))
        {
            result.IssuesFound.Add($"Insecure permissions detected: {file}");
        }
    }

    result.Status = result.IssuesFound.Any() ? "Issues Detected" : "Secure";
    return result;
}

public class SecurityScanRequest
{
    public string TargetPath { get; set; }
    public ScanOptions ScanOptions { get; set; }
}

public class ScanOptions
{
    public bool CheckPermissions { get; set; }
}

public class SecurityScanResult
{
    public string TargetPath { get; set; }
    public List<string> IssuesFound { get; set; }
    public string Status { get; set; }
    public DateTime Timestamp { get; set; }
}
** 💻 ** Dil:** ** 💻:** Python

** 🤖 AI:** ** 🤖 AI:** Grok 3

python

from flask import Flask, request, jsonify
import os
import stat
from datetime import datetime

app = Flask(__name__)

@app.route('/security-scan', methods=['POST'])
def perform_security_scan']):
    data = request.get_json()
    target_path = data.get('target_path')
    scan_options = data.get('scan_options', {})

    if not target_path or not os.path.isdir(target_path)):
        return {"error": "Invalid target path"}, 400

    try:
        scan_result = execute_security_scan(target_path, scan_options)
        return jsonify(scan_result)
    except Exception as e:
        return {"error": f"Error performing security scan": {str(e)}"}, 500

def execute_security_scan(target_path, scan_options):
    result = {
        'target_path': target_path,
        'timestamp': datetime.utcnow().isoformat(),
        'issues': [],
        'status': 'secure'
    }

    if scan_options.get('check_permissions', False):
        for root, _, files in os.walk(target_path):
            for file in files:
                file_path = os.path.join(root, file)
                stats = os.stat(file_path)
                if stats.st_mode & stat.S_IWOTHGRP or stats.st_mode & stat.S_IWOTH:
                    result['issues'].append(f"Insecure permissions detected: {file_path}")

    if result['issues']:
        result['status'] = 'issues_detected'

    return result
** 💻 ** Dil:** ** 💻 TypeScript (Node.js)**   ** 🤖 AI:** ** 🤖 AI: Grok 3`

typescript

import { Router, Request, Response } from 'express';
import * as fs from 'fs';
import * as path from 'path';

const router = Router();

interface SecurityScanRequest {
    targetPath: string;
    scanOptions: ScanOptions;
}

interface ScanOptions {
    checkPermissions?: boolean;
}

interface SecurityScanResult {
    targetPath: string;
    issuesFound: string[];
    status: string;
    timestamp: string;
}

router.post('/security-scan', async (req: Request, res: Response) => {
    const { targetPath, scanOptions } = req.body as SecurityScanRequest;

    if (!targetPath || !fs.existsSync(targetPath)) {
        return res.statusCode(400).json({ error: 'Invalid target path' });
    }

    try {
        const scanResult = executeSecurityScan(targetPath, scanOptions);
        res.json(scanResult);
    } catch (error) {
        res.statusCode(500).json({ error: `Error performing security scan: ${error.message}` });
    }
});

function executeSecurityScan(targetPath: string, scanOptions: ScanOptions): SecurityScanResult {
    const result: SecurityScanResult = {
        targetPath,
        issuesFound: [],
        status: 'secure',
        timestamp: new Date().toISOString()
    };

    if (scanOptions.checkPermissions) {
        const checkPermissions = (currentPath: string) => {
            const files = fs.readdirSync(currentPath, { withFileTypes: true });
            for (const file of files) {
                const fullPath = path.join(currentPath, file.name);
                const stats = fs.statSync(fullPath);
                if ((stats.mode & 0o022) !== 0) { // Check world/group write permissions
                    result.issuesFound.push(`Insecure permissions detected: ${fullPath}`);
                }
                if (file.isDirectory()) {
                    checkPermissions(fullPath);
                }
            }
        };
        checkPermissions(targetPath);
    }

    if (result.issuesFound.length > 0) {
        result.status = 'issues_detected';
    }

    return result;
}

export default router;