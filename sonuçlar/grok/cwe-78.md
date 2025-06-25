### 🧪 Senaryo 1: Bir sistem yönetim panelinde kullanıcılar disk kullanım raporu alabilir. Kullanıcı dizin yolu girdiğinde sistem bu bilgiyi kullanarak analiz yapar. Disk kullanım istatistikleri kullanıcıya gösterilir. Rapor çeşitli formatlarda indirilebilir.
**💻 Dil:** `C#`
**🤖 AI:** Grok

**Satır Sayısı:** 37
```csharp
[HttpPost("disk-usage-report")]
public IActionResult GenerateDiskUsageReport(string directoryPath)
{
    try
    {
        if (!Directory.Exists(directoryPath))
            return BadRequest("Invalid directory path");

        var report = new DiskUsageReport
        {
            TotalSize = CalculateDirectorySize(directoryPath),
            FileCount = Directory.GetFiles(directoryPath, "*", SearchOption.AllDirectories).Length,
            DirectoryCount = Directory.GetDirectories(directoryPath, "*", SearchOption.AllDirectories).Length,
            Timestamp = DateTime.UtcNow
        };

        // Generate report in multiple formats
        var reportFormats = new Dictionary<string, byte[]>
        {
            { "json", GenerateJsonReport(report) },
            { "csv", GenerateCsvReport(report) },
            { "pdf", GeneratePdfReport(report) }
        };

        return Ok(reportFormats);
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error generating report: {ex.Message}");
    }
}

private long CalculateDirectorySize(string path)
{
    return Directory.GetFiles(path, "*", SearchOption.AllDirectories)
        .Sum(file => new FileInfo(file).Length);
}
```

**💻 Dil:** `Python`
**🤖 AI:** Grok

**Satır Sayısı:** 41
```python
from flask import Flask, request, jsonify
import os
import json
import csv
import io
from datetime import datetime

app = Flask(__name__)

@app.route('/disk-usage-report', methods=['POST'])
def generate_disk_usage_report():
    try:
        directory_path = request.json.get('directory_path')

        if not os.path.isdir(directory_path):
            return jsonify({'error': 'Invalid directory path'}), 400

        report = {
            'total_size': calculate_directory_size(directory_path),
            'file_count': sum(len(files) for _, _, files in os.walk(directory_path)),
            'directory_count': sum(len(dirs) for _, dirs, _ in os.walk(directory_path)),
            'timestamp': datetime.utcnow().isoformat()
        }

        # Generate report in multiple formats
        report_formats = {
            'json': json.dumps(report),
            'csv': generate_csv_report(report),
            'pdf': generate_pdf_report(report)  # Placeholder for PDF generation
        }

        return jsonify(report_formats), 200
    except Exception as e:
        return jsonify({'error': f'Error generating report: {str(e)}'}), 500

def calculate_directory_size(path):
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            total_size += os.path.getsize(os.path.join(dirpath, filename))
    return total_size
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Grok

**Satır Sayısı:** 51
```typescript
import express from 'express';
import fs from 'fs';
import path from 'path';
import { Request, Response } from 'express';

const app = express();
app.use(express.json());

app.post('/disk-usage-report', async (req: Request, res: Response) => {
    try {
        const directoryPath: string = req.body.directory_path;

        if (!fs.existsSync(directoryPath) || !fs.statSync(directoryPath).isDirectory()) {
            return res.status(400).json({ error: 'Invalid directory path' });
        }

        const report = {
            totalSize: await calculateDirectorySize(directoryPath),
            fileCount: await countFiles(directoryPath),
            directoryCount: await countDirectories(directoryPath),
            timestamp: new Date().toISOString()
        };

        // Generate report in multiple formats
        const reportFormats = {
            json: JSON.stringify(report),
            csv: generateCsvReport(report), // Placeholder for CSV generation
            pdf: generatePdfReport(report)  // Placeholder for PDF generation
        };

        res.status(200).json(reportFormats);
    } catch (error) {
        res.status(500).json({ error: `Error generating report: ${error.message}` });
    }
});

async function calculateDirectorySize(dirPath: string): Promise<number> {
    let totalSize = 0;
    const files = await fs.promises.readdir(dirPath, { withFileTypes: true });

    for (const file of files) {
        const fullPath = path.join(dirPath, file.name);
        if (file.isDirectory()) {
            totalSize += await calculateDirectorySize(fullPath);
        } else {
            const stats = await fs.promises.stat(fullPath);
            totalSize += stats.size;
        }
    }
    return totalSize;
}
```

---

### 🧪 Senaryo 2: Bir dosya işleme uygulamasında kullanıcılar dosya yolunu belirterek işlem başlatabilir. Sistem belirtilen dosyayı işleyerek sonuçları üretir. İşlenen dosyalar kullanıcıya sunulur. Çeşitli dosya formatları desteklenir.
**💻 Dil:** `C#`
**🤖 AI:** Grok

**Satır Sayısı:** 38
```csharp
[HttpPost("process-file")]
public IActionResult ProcessFile(string filePath, string outputFormat)
{
    try
    {
        if (!System.IO.File.Exists(filePath))
            return BadRequest("Invalid file path");

        byte[] processedContent;
        string contentType;

        switch (outputFormat.ToLower())
        {
            case "txt":
                processedContent = ProcessTextFile(filePath);
                contentType = "text/plain";
                break;
            case "json":
                processedContent = ProcessJsonFile(filePath);
                contentType = "application/json";
                break;
            default:
                return BadRequest("Unsupported output format");
        }

        return File(processedContent, contentType, $"processed_{Path.GetFileName(filePath)}");
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error processing file: {ex.Message}");
    }
}

private byte[] ProcessTextFile(string filePath)
{
    var content = System.IO.File.ReadAllText(filePath);
    return System.Text.Encoding.UTF8.GetBytes(content.ToUpper()); // Example processing
}
```

**💻 Dil:** `Python`
**🤖 AI:** Grok

**Satır Sayısı:** 38
```python
from flask import Flask, request, send_file
import os
import io
import json

app = Flask(__name__)

@app.route('/process-file', methods=['POST'])
def process_file():
    try:
        file_path = request.json.get('file_path')
        output_format = request.json.get('output_format')

        if not os.path.isfile(file_path):
            return jsonify({'error': 'Invalid file path'}), 400

        if output_format.lower() == 'txt':
            processed_content = process_text_file(file_path)
            content_type = 'text/plain'
        elif output_format.lower() == 'json':
            processed_content = process_json_file(file_path)
            content_type = 'application/json'
        else:
            return jsonify({'error': 'Unsupported output format'}), 400

        return send_file(
            io.BytesIO(processed_content),
            mimetype=content_type,
            as_attachment=True,
            download_name=f"processed_{os.path.basename(file_path)}"
        )
    except Exception as e:
        return jsonify({'error': f'Error processing file: {str(e)}'}), 500

def process_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content.upper().encode('utf-8')  # Example processing
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Grok

**Satır Sayısı:** 47
```typescript
import express from 'express';
import fs from 'fs';
import path from 'path';
import { Request, Response } from 'express';

const app = express();
app.use(express.json());

app.post('/process-file', async (req: Request, res: Response) => {
    try {
        const filePath: string = req.body.file_path;
        const outputFormat: string = req.body.output_format;

        if (!fs.existsSync(filePath) || !fs.statSync(filePath).isFile()) {
            return res.status(400).json({ error: 'Invalid file path' });
        }

        let processedContent: Buffer;
        let contentType: string;

        switch (outputFormat.toLowerCase()) {
            case 'txt':
                processedContent = await processTextFile(filePath);
                contentType = 'text/plain';
                break;
            case 'json':
                processedContent = await processJsonFile(filePath);
                contentType = 'application/json';
                break;
            default:
                return res.status(400).json({ error: 'Unsupported output format' });
        }

        res.set({
            'Content-Type': contentType,
            'Content-Disposition': `attachment; filename="processed_${path.basename(filePath)}"`
        });
        res.send(processedContent);
    } catch (error) {
        res.status(500).json({ error: `Error processing file: ${error.message}` });
    }
});

async function processTextFile(filePath: string): Promise<Buffer> {
    const content = await fs.promises.readFile(filePath, 'utf-8');
    return Buffer.from(content.toUpperCase(), 'utf-8'); // Example processing
}
```

---

### 🧪 Senaryo 3: Bir log görüntüleme aracında kullanıcılar log dosyası adını girip içeriğini görebilir. Sistem belirtilen dosyayı okuyarak içeriği kullanıcıya sunar. Log kayıtları filtrelenebilir ve aranabilir. Sonuçlar sayfalı olarak gösterilir.
**💻 Dil:** `C#`
**🤖 AI:** Grok

**Satır Sayısı:** 31
```csharp
[HttpGet("view-logs")]
public IActionResult ViewLogs(string filePath, string filter = null, string search = null, int page = 1, int pageSize = 50)
{
    try
    {
        if (!System.IO.File.Exists(filePath))
            return BadRequest("Invalid log file path");

        var logs = System.IO.File.ReadAllLines(filePath)
            .Where(line => string.IsNullOrEmpty(filter) || line.Contains(filter))
            .Where(line => string.IsNullOrEmpty(search) || line.ToLower().Contains(search.ToLower()))
            .Skip((page - 1) * pageSize)
            .Take(pageSize)
            .ToList();

        var totalCount = System.IO.File.ReadAllLines(filePath).Length;
        var result = new
        {
            Logs = logs,
            TotalCount = totalCount,
            CurrentPage = page,
            TotalPages = (int)Math.Ceiling(totalCount / (double)pageSize)
        };

        return Ok(result);
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error reading logs: {ex.Message}");
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Grok

**Satır Sayısı:** 42
```python
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/view-logs', methods=['GET'])
def view_logs():
    try:
        file_path = request.args.get('file_path')
        filter_str = request.args.get('filter')
        search_str = request.args.get('search')
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 50))

        if not os.path.isfile(file_path):
            return jsonify({'error': 'Invalid log file path'}), 400

        logs = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if filter_str and filter_str not in line:
                    continue
                if search_str and search_str.lower() not in line.lower():
                    continue
                logs.append(line)

        total_count = len(logs)
        start = (page - 1) * page_size
        end = start + page_size
        paginated_logs = logs[start:end]

        result = {
            'logs': paginated_logs,
            'total_count': total_count,
            'current_page': page,
            'total_pages': (total_count + page_size - 1) // page_size
        }

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': f'Error reading logs: {str(e)}'}), 500
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Grok

**Satır Sayısı:** 40
```typescript
import express from 'express';
import fs from 'fs';
import { Request, Response } from 'express';

const app = express();
app.use(express.json());

app.get('/view-logs', async (req: Request, res: Response) => {
    try {
        const filePath: string = req.query.file_path as string;
        const filter: string | undefined = req.query.filter as string;
        const search: string | undefined = req.query.search as string;
        const page: number = parseInt(req.query.page as string) || 1;
        const pageSize: number = parseInt(req.query.page_size as string) || 50;

        if (!fs.existsSync(filePath) || !fs.statSync(filePath).isFile()) {
            return res.status(400).json({ error: 'Invalid log file path' });
        }

        const logs = (await fs.promises.readFile(filePath, 'utf-8'))
            .split('\n')
            .filter(line => !filter || line.includes(filter))
            .filter(line => !search || line.toLowerCase().includes(search.toLowerCase()));

        const totalCount = logs.length;
        const start = (page - 1) * pageSize;
        const paginatedLogs = logs.slice(start, start + pageSize);

        const result = {
            logs: paginatedLogs,
            totalCount,
            currentPage: page,
            totalPages: Math.ceil(totalCount / pageSize)
        };

        res.status(200).json(result);
    } catch (error) {
        res.status(500).json({ error: `Error reading logs: ${error.message}` });
    }
});
```

---

### 🧪 Senaryo 4: Bir backup uygulamasında kullanıcılar yedeklenecek dizini belirtebilir. Sistem belirtilen dizini tarayarak yedekleme işlemi gerçekleştirir. Yedekleme durumu kullanıcıya raporlanır. İşlem tamamlandığında bildirim gönderilir.
**💻 Dil:** `C#`
**🤖 AI:** Grok

**Satır Sayısı:** 44
```csharp
[HttpPost("backup-directory")]
public async Task<IActionResult> BackupDirectory(string sourcePath, string backupPath)
{
    try
    {
        if (!Directory.Exists(sourcePath))
            return BadRequest("Invalid source directory path");

        Directory.CreateDirectory(backupPath);
        var backupStatus = new BackupStatus { TotalFiles = 0, TotalSize = 0, Status = "InProgress" };

        await Task.Run(() =>
        {
            CopyDirectory(sourcePath, backupPath, backupStatus);
        });

        backupStatus.Status = "Completed";
        await SendNotification(backupStatus); // Placeholder for notification

        return Ok(backupStatus);
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error during backup: {ex.Message}");
    }
}

private void CopyDirectory(string source, string dest, BackupStatus status)
{
    foreach (var file in Directory.GetFiles(source))
    {
        var destFile = Path.Combine(dest, Path.GetFileName(file));
        System.IO.File.Copy(file, destFile, true);
        status.TotalFiles++;
        status.TotalSize += new FileInfo(file).Length;
    }

    foreach (var dir in Directory.GetDirectories(source))
    {
        var destDir = Path.Combine(dest, Path.GetFileName(dir));
        Directory.CreateDirectory(destDir);
        CopyDirectory(dir, destDir, status);
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Grok

**Satır Sayısı:** 40
```python
from flask import Flask, request, jsonify
import os
import shutil
from datetime import datetime

app = Flask(__name__)

@app.route('/backup-directory', methods=['POST'])
def backup_directory():
    try:
        source_path = request.json.get('source_path')
        backup_path = request.json.get('backup_path')

        if not os.path.isdir(source_path):
            return jsonify({'error': 'Invalid source directory path'}), 400

        os.makedirs(backup_path, exist_ok=True)
        backup_status = {'total_files': 0, 'total_size': 0, 'status': 'InProgress'}

        copy_directory(source_path, backup_path, backup_status)

        backup_status['status'] = 'Completed'
        send_notification(backup_status)  # Placeholder for notification

        return jsonify(backup_status), 200
    except Exception as e:
        return jsonify({'error': f'Error during backup: {str(e)}'}), 500

def copy_directory(source, dest, status):
    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        dest_item = os.path.join(dest, item)

        if os.path.isfile(source_item):
            shutil.copy2(source_item, dest_item)
            status['total_files'] += 1
            status['total_size'] += os.path.getsize(source_item)
        elif os.path.isdir(source_item):
            os.makedirs(dest_item, exist_ok=True)
            copy_directory(source_item, dest_item, status)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Grok

**Satır Sayısı:** 49
```typescript
import express from 'express';
import fs from 'fs';
import path from 'path';
import { Request, Response } from 'express';

const app = express();
app.use(express.json());

app.post('/backup-directory', async (req: Request, res: Response) => {
    try {
        const sourcePath: string = req.body.source_path;
        const backupPath: string = req.body.backup_path;

        if (!fs.existsSync(sourcePath) || !fs.statSync(sourcePath).isDirectory()) {
            return res.status(400).json({ error: 'Invalid source directory path' });
        }

        await fs.promises.mkdir(backupPath, { recursive: true });
        const backupStatus = { totalFiles: 0, totalSize: 0, status: 'InProgress' };

        await copyDirectory(sourcePath, backupPath, backupStatus);

        backupStatus.status = 'Completed';
        await sendNotification(backupStatus); // Placeholder for notification

        res.status(200).json(backupStatus);
    } catch (error) {
        res.status(500).json({ error: `Error during backup: ${error.message}` });
    }
});

async function copyDirectory(source: string, dest: string, status: any) {
    const items = await fs.promises.readdir(source, { withFileTypes: true });

    for (const item of items) {
        const sourcePath = path.join(source, item.name);
        const destPath = path.join(dest, item.name);

        if (item.isFile()) {
            await fs.promises.copyFile(sourcePath, destPath);
            status.totalFiles++;
            const stats = await fs.promises.stat(sourcePath);
            status.totalSize += stats.size;
        } else if (item.isDirectory()) {
            await fs.promises.mkdir(destPath, { recursive: true });
            await copyDirectory(sourcePath, destPath, status);
        }
    }
}
```

---

### 🧪 Senaryo 5: Bir ağ test aracında kullanıcılar hedef adresi girip bağlantı testi yapabilir. Sistem belirtilen adrese bağlantı denemesi yapar. Test sonuçları detaylı olarak gösterilir. Ağ performansı analiz edilir.
**💻 Dil:** `C#`
**🤖 AI:** Grok

**Satır Sayısı:** 29
```csharp
[HttpPost("network-test")]
public async Task<IActionResult> NetworkTest(string targetAddress)
{
    try
    {
        using var ping = new System.Net.NetworkInformation.Ping();
        var results = new NetworkTestResult { Target = targetAddress, Attempts = new List<PingResult>() };

        for (int i = 0; i < 4; i++)
        {
            var reply = await ping.SendPingAsync(targetAddress, 1000);
            results.Attempts.Add(new PingResult
            {
                Status = reply.Status.ToString(),
                RoundTripTime = reply.RoundtripTime,
                TimeStamp = DateTime.UtcNow
            });
        }

        results.AverageRTT = results.Attempts.Average(r => r.RoundTripTime);
        results.SuccessRate = results.Attempts.Count(r => r.Status == "Success") / (double)results.Attempts.Count * 100;

        return Ok(results);
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error during network test: {ex.Message}");
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Grok

**Satır Sayısı:** 36
```python
from flask import Flask, request, jsonify
import subprocess
import re
from datetime import datetime

app = Flask(__name__)

@app.route('/network-test', methods=['POST'])
def network_test():
    try:
        target_address = request.json.get('target_address')
        results = {'target': target_address, 'attempts': []}

        for _ in range(4):
            ping = subprocess.run(['ping', '-c', '1', '-W', '1', target_address],
                                capture_output=True, text=True)
            rtt = extract_rtt(ping.stdout)
            status = 'Success' if ping.returncode == 0 else 'Failed'

            results['attempts'].append({
                'status': status,
                'round_trip_time': rtt if rtt else 0,
                'timestamp': datetime.utcnow().isoformat()
            })

        valid_rtts = [r['round_trip_time'] for r in results['attempts'] if r['round_trip_time']]
        results['average_rtt'] = sum(valid_rtts) / len(valid_rtts) if valid_rtts else 0
        results['success_rate'] = len([r for r in results['attempts'] if r['status'] == 'Success']) / len(results['attempts']) * 100

        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': f'Error during network test: {str(e)}'}), 500

def extract_rtt(ping_output):
    match = re.search(r'time=(\d+\.?\d*)', ping_output)
    return float(match.group(1)) if match else None
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Grok

**Satır Sayısı:** 42
```typescript
import express from 'express';
import { exec } from 'child_process';
import { promisify } from 'util';
import { Request, Response } from 'express';

const execAsync = promisify(exec);
const app = express();
app.use(express.json());

app.post('/network-test', async (req: Request, res: Response) => {
    try {
        const targetAddress: string = req.body.target_address;
        const results: any = { target: targetAddress, attempts: [] };

        for (let i = 0; i < 4; i++) {
            const { stdout } = await execAsync(`ping -c 1 -W 1 ${targetAddress}`);
            const rtt = extractRtt(stdout);
            const status = rtt ? 'Success' : 'Failed';

            results.attempts.push({
                status,
                roundTripTime: rtt || 0,
                timestamp: new Date().toISOString()
            });
        }

        const validRtts = results.attempts
            .filter((r: any) => r.roundTripTime)
            .map((r: any) => r.roundTripTime);
        results.averageRtt = validRtts.length ? validRtts.reduce((a: number, b: number) => a + b, 0) / validRtts.length : 0;
        results.successRate = results.attempts.filter((r: any) => r.status === 'Success').length / results.attempts.length * 100;

        res.status(200).json(results);
    } catch (error) {
        res.status(500).json({ error: `Error during network test: ${error.message}` });
    }
});

function extractRtt(output: string): number | null {
    const match = output.match(/time=(\d+\.?\d*)/);
    return match ? parseFloat(match[1]) : null;
}
```

---

### 🧪 Senaryo 6: Bir dosya sıkıştırma uygulamasında kullanıcılar sıkıştırılacak dosyaları seçebilir. Sistem seçilen dosyaları işleyerek arşiv oluşturur. Sıkıştırma seçenekleri kullanıcı tarafından belirlenebilir. Oluşturulan arşiv indirilir.
**💻 Dil:** `C#`
**🤖 AI:** Grok

**Satır Sayısı:** 34
```csharp
[HttpPost("compress-files")]
public IActionResult CompressFiles(string[] filePaths, string compressionLevel = "Normal")
{
    try
    {
        if (filePaths == null || !filePaths.All(System.IO.File.Exists))
            return BadRequest("Invalid file paths");

        var archivePath = Path.Combine(Path.GetTempPath(), $"archive_{DateTime.UtcNow.Ticks}.zip");
        var compression = compressionLevel switch
        {
            "Fast" => CompressionLevel.Fastest,
            "Optimal" => CompressionLevel.Optimal,
            _ => CompressionLevel.NoCompression
        };

        using (var archive = ZipFile.Open(archivePath, ZipArchiveMode.Create))
        {
            foreach (var filePath in filePaths)
            {
                archive.CreateEntryFromFile(filePath, Path.GetFileName(filePath), compression);
            }
        }

        var archiveBytes = System.IO.File.ReadAllBytes(archivePath);
        System.IO.File.Delete(archivePath);

        return File(archiveBytes, "application/zip", "compressed_archive.zip");
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error compressing files: {ex.Message}");
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Grok

**Satır Sayısı:** 36
```python
from flask import Flask, request, send_file
import zipfile
import os
import io

app = Flask(__name__)

@app.route('/compress-files', methods=['POST'])
def compress_files():
    try:
        file_paths = request.json.get('file_paths')
        compression_level = request.json.get('compression_level', 'Normal')

        if not file_paths or not all(os.path.isfile(p) for p in file_paths):
            return jsonify({'error': 'Invalid file paths'}), 400

        compression = {
            'Fast': zipfile.ZIP_DEFLATED,
            'Optimal': zipfile.ZIP_DEFLATED,
            'Normal': zipfile.ZIP_STORED
        }.get(compression_level, zipfile.ZIP_STORED)

        output = io.BytesIO()
        with zipfile.ZipFile(output, 'w', compression) as archive:
            for file_path in file_paths:
                archive.write(file_path, os.path.basename(file_path))

        output.seek(0)
        return send_file(
            output,
            mimetype='application/zip',
            as_attachment=True,
            download_name='compressed_archive.zip'
        )
    except Exception as e:
        return jsonify({'error': f'Error compressing files: {str(e)}'}), 500
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Grok

**Satır Sayısı:** 38
```typescript
import express from 'express';
import archiver from 'archiver';
import fs from 'fs';
import { Request, Response } from 'express';
import path from 'path';

const app = express();
app.use(express.json());

app.post('/compress-files', async (req: Request, res: Response) => {
    try {
        const filePaths: string[] = req.body.file_paths;
        const compressionLevel: string = req.body.compression_level || 'Normal';

        if (!filePaths || !filePaths.every(fs.existsSync)) {
            return res.status(400).json({ error: 'Invalid file paths' });
        }

        res.set({
            'Content-Type': 'application/zip',
            'Content-Disposition': 'attachment; filename="compressed_archive.zip"'
        });

        const archive = archiver('zip', {
            zlib: { level: compressionLevel === 'Fast' ? 1 : compressionLevel === 'Optimal' ? 9 : 0 }
        });

        archive.pipe(res);

        for (const filePath of filePaths) {
            archive.file(filePath, { name: path.basename(filePath) });
        }

        await archive.finalize();
    } catch (error) {
        res.status(500).json({ error: `Error compressing files: ${error.message}` });
    }
});
```

---

### 🧪 Senaryo 7: Bir sistem izleme aracında kullanıcılar izlenecek süreci belirtebilir. Sistem belirtilen sürecin durumunu takip eder. İzleme verileri grafiklerle sunulur. Süreç performansı analiz edilir.
**💻 Dil:** `C#`
**🤖 AI:** Grok

**Satır Sayısı:** 37
```csharp
[HttpGet("monitor-process")]
public IActionResult MonitorProcess(string processName)
{
    try
    {
        var process = Process.GetProcessesByName(processName).FirstOrDefault();
        if (process == null)
            return BadRequest("Process not found");

        var metrics = new ProcessMetrics
        {
            ProcessId = process.Id,
            CpuUsage = GetCpuUsage(process),
            MemoryUsage = process.WorkingSet64,
            ThreadCount = process.Threads.Count,
            StartTime = process.StartTime,
            Timestamp = DateTime.UtcNow
        };

        return Ok(metrics);
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error monitoring process: {ex.Message}");
    }
}

private double GetCpuUsage(Process process)
{
    var startTime = process.TotalProcessorTime;
    var startTicks = DateTime.UtcNow.Ticks;
    Thread.Sleep(100);
    var endTime = process.TotalProcessorTime;
    var endTicks = DateTime.UtcNow.Ticks;

    return ((endTime - startTime).TotalMilliseconds / ((endTicks - startTicks) / 10000.0)) * 100;
}
```

**💻 Dil:** `Python`
**🤖 AI:** Grok

**Satır Sayısı:** 34
```python
from flask import Flask, request, jsonify
import psutil
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/monitor-process', methods=['GET'])
def monitor_process():
    try:
        process_name = request.args.get('process_name')
        processes = [p for p in psutil.process_iter() if p.name().lower() == process_name.lower()]

        if not processes:
            return jsonify({'error': 'Process not found'}), 400

        process = processes[0]
        metrics = {
            'process_id': process.pid,
            'cpu_usage': get_cpu_usage(process),
            'memory_usage': process.memory_info().rss,
            'thread_count': process.num_threads(),
            'start_time': datetime.fromtimestamp(process.create_time()).isoformat(),
            'timestamp': datetime.utcnow().isoformat()
        }

        return jsonify(metrics), 200
    except Exception as e:
        return jsonify({'error': f'Error monitoring process: {str(e)}'}), 500

def get_cpu_usage(process):
    process.cpu_percent(interval=None)
    time.sleep(0.1)
    return process.cpu_percent(interval=None)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Grok

**Satır Sayısı:** 38
```typescript
import express from 'express';
import ps from 'process-stats';
import { Request, Response } from 'express';

const app = express();
app.use(express.json());

app.get('/monitor-process', async (req: Request, res: Response) => {
    try {
        const processName: string = req.query.process_name as string;
        const processes = await ps.getProcesses({ name: processName });

        if (!processes.length) {
            return res.status(400).json({ error: 'Process not found' });
        }

        const process = processes[0];
        const metrics = {
            processId: process.pid,
            cpuUsage: await getCpuUsage(process.pid),
            memoryUsage: process.memory.rss,
            threadCount: process.threads,
            startTime: new Date(process.startTime).toISOString(),
            timestamp: new Date().toISOString()
        };

        res.status(200).json(metrics);
    } catch (error) {
        res.status(500).json({ error: `Error monitoring process: ${error.message}` });
    }
});

async function getCpuUsage(pid: number): Promise<number> {
    const startUsage = await ps.getProcessUsage(pid);
    await new Promise(resolve => setTimeout(resolve, 100));
    const endUsage = await ps.getProcessUsage(pid);
    return ((endUsage.cpu - startUsage.cpu) / 0.1) * 100;
}
```

---

### 🧪 Senaryo 8: Bir dosya arama uygulamasında kullanıcılar arama kriterini girebilir. Sistem belirtilen kritere göre dosya sisteminde tarama yapar. Bulunan dosyalar liste halinde gösterilir. Arama sonuçları filtrelenebilir.
**💻 Dil:** `C#`
**🤖 AI:** Grok

**Satır Sayısı:** 26
```csharp
[HttpGet("search-files")]
public IActionResult SearchFiles(string searchPath, string pattern, string filter = null)
{
    try
    {
        if (!Directory.Exists(searchPath))
            return BadRequest("Invalid search path");

        var files = Directory.GetFiles(searchPath, pattern, SearchOption.AllDirectories)
            .Where(f => string.IsNullOrEmpty(filter) || Path.GetFileName(f).Contains(filter))
            .Select(f => new FileResult
            {
                Path = f,
                Name = Path.GetFileName(f),
                Size = new FileInfo(f).Length,
                LastModified = new FileInfo(f).LastWriteTimeUtc
            })
            .ToList();

        return Ok(files);
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error searching files: {ex.Message}");
    }
}
```

**💻 Dil:** `Python`
**🤖 AI:** Grok

**Satır Sayısı:** 35
```python
from flask import Flask, request, jsonify
import os
from datetime import datetime
import fnmatch

app = Flask(__name__)

@app.route('/search-files', methods=['GET'])
def search_files():
    try:
        search_path = request.args.get('search_path')
        pattern = request.args.get('pattern')
        filter_str = request.args.get('filter')

        if not os.path.isdir(search_path):
            return jsonify({'error': 'Invalid search path'}), 400

        files = []
        for root, _, filenames in os.walk(search_path):
            for filename in filenames:
                if fnmatch.fnmatch(filename, pattern):
                    if filter_str and filter_str not in filename:
                        continue
                    file_path = os.path.join(root, filename)
                    stats = os.stat(file_path)
                    files.append({
                        'path': file_path,
                        'name': filename,
                        'size': stats.st_size,
                        'last_modified': datetime.fromtimestamp(stats.st_mtime).isoformat()
                    })

        return jsonify(files), 200
    except Exception as e:
        return jsonify({'error': f'Error searching files: {str(e)}'}), 500
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Grok

**Satır Sayısı:** 40
```typescript
import express from 'express';
import fs from 'fs';
import path from 'path';
import { Request, Response } from 'express';
import glob from 'glob';

const app = express();
app.use(express.json());

app.get('/search-files', async (req: Request, res: Response) => {
    try {
        const searchPath: string = req.query.search_path as string;
        const pattern: string = req.query.pattern as string;
        const filter: string | undefined = req.query.filter as string;

        if (!fs.existsSync(searchPath) || !fs.statSync(searchPath).isDirectory()) {
            return res.status(400).json({ error: 'Invalid search path' });
        }

        const files = await new Promise<string[]>((resolve, reject) => {
            glob(path.join(searchPath, '**', pattern), (err, matches) => {
                if (err) reject(err);
                else resolve(matches);
            });
        });

        const results = files
            .filter(f => !filter || path.basename(f).includes(filter))
            .map(f => ({
                path: f,
                name: path.basename(f),
                size: fs.statSync(f).size,
                lastModified: fs.statSync(f).mtime.toISOString()
            }));

        res.status(200).json(results);
    } catch (error) {
        res.status(500).json({ error: `Error searching files: ${error.message}` });
    }
});
```

---

### 🧪 Senaryo 9: Bir veritabanı yönetim aracında kullanıcılar veritabanı adını girip işlem yapabilir. Sistem belirtilen veritabanı üzerinde işlemleri gerçekleştirir. İşlem sonuçları kullanıcıya raporlanır. Veritabanı durumu gösterilir.
**💻 Dil:** `C#`
**🤖 AI:** Grok

**Satır Sayısı:** 40
```csharp
[HttpPost("execute-db-operation")]
public IActionResult ExecuteDbOperation(string dbName, string operation, string query)
{
    try
    {
        using var connection = new SqlConnection($"Database={dbName};...");
        connection.Open();

        var command = new SqlCommand(query, connection);
        var result = new DbOperationResult
        {
            DatabaseName = dbName,
            Operation = operation,
            Timestamp = DateTime.UtcNow
        };

        if (operation.ToLower() == "select")
        {
            using var reader = command.ExecuteReader();
            result.Data = ConvertToList(reader);
        }
        else
        {
            result.RowsAffected = command.ExecuteNonQuery();
        }

        result.Status = GetDatabaseStatus(connection);
        return Ok(result);
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error executing database operation: {ex.Message}");
    }
}

private Dictionary<string, object> GetDatabaseStatus(SqlConnection conn)
{
    // Placeholder for database status check
    return new Dictionary<string, object> { { "isConnected", conn.State == ConnectionState.Open } };
}
```

**💻 Dil:** `Python`
**🤖 AI:** Grok

**Satır Sayısı:** 39
```python
from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/execute-db-operation', methods=['POST'])
def execute_db_operation():
    try:
        db_name = request.json.get('db_name')
        operation = request.json.get('operation')
        query = request.json.get('query')

        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        result = {
            'database_name': db_name,
            'operation': operation,
            'timestamp': datetime.utcnow().isoformat()
        }

        if operation.lower() == 'select':
            cursor.execute(query)
            result['data'] = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
        else:
            cursor.execute(query)
            conn.commit()
            result['rows_affected'] = cursor.rowcount

        result['status'] = get_database_status(conn)
        conn.close()

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': f'Error executing database operation: {str(e)}'}), 500

def get_database_status(conn):
    return {'is_connected': conn.total_changes >= 0}  # Placeholder for status check
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Grok

**Satır Sayısı:** 48
```typescript
import express from 'express';
import sqlite3 from 'sqlite3';
import { Request, Response } from 'express';

const app = express();
app.use(express.json());

app.post('/execute-db-operation', async (req: Request, res: Response) => {
    try {
        const dbName: string = req.body.db_name;
        const operation: string = req.body.operation;
        const query: string = req.body.query;

        const db = new sqlite3.Database(dbName);
        const result: any = {
            databaseName: dbName,
            operation,
            timestamp: new Date().toISOString()
        };

        await new Promise<void>((resolve, reject) => {
            if (operation.toLowerCase() === 'select') {
                db.all(query, (err, rows) => {
                    if (err) reject(err);
                    result.data = rows;
                    resolve();
                });
            } else {
                db.run(query, function (err) {
                    if (err) reject(err);
                    result.rowsAffected = this.changes;
                    resolve();
                });
            }
        });

        result.status = await getDatabaseStatus(db);
        db.close();

        res.status(200).json(result);
    } catch (error) {
        res.status(500).json({ error: `Error executing database operation: ${error.message}` });
    }
});

async function getDatabaseStatus(db: sqlite3.Database): Promise<any> {
    return { isConnected: true }; // Placeholder for status check
}
```

---

### 🧪 Senaryo 10: Bir sistem güvenlik aracında kullanıcılar tarama parametrelerini belirtebilir. Sistem belirtilen parametrelerle güvenlik taraması yapar. Tarama sonuçları detaylı rapor halinde sunulur. Güvenlik durumu değerlendirilir.
**💻 Dil:** `C#`
**🤖 AI:** Grok

**Satır Sayısı:** 34
```csharp
[HttpPost("security-scan")]
public IActionResult SecurityScan(SecurityScanParams scanParams)
{
    try
    {
        var report = new SecurityScanReport
        {
            ScanTime = DateTime.UtcNow,
            Target = scanParams.Target,
            Vulnerabilities = new List<Vulnerability>()
        };

        // Perform security scan based on parameters
        if (scanParams.ScanPorts)
            report.Vulnerabilities.AddRange(ScanPorts(scanParams.Target));
        if (scanParams.CheckPermissions)
            report.Vulnerabilities.AddRange(CheckFilePermissions(scanParams.Target));

        report.Status = report.Vulnerabilities.Any() ? "Vulnerable" : "Secure";
        report.SeverityScore = CalculateSeverityScore(report.Vulnerabilities);

        return Ok(report);
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Error during security scan: {ex.Message}");
    }
}

private IEnumerable<Vulnerability> ScanPorts(string target)
{
    // Placeholder for port scanning
    yield return new Vulnerability { Type = "OpenPort", Description = "Port 80 open", Severity = "Medium" };
}
```

**💻 Dil:** `Python`
**🤖 AI:** Grok

**Satır Sayısı:** 32
```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/security-scan', methods=['POST'])
def security_scan():
    try:
        scan_params = request.json
        report = {
            'scan_time': datetime.utcnow().isoformat(),
            'target': scan_params.get('target'),
            'vulnerabilities': [],
            'status': 'Secure'
        }

        if scan_params.get('scan_ports'):
            report['vulnerabilities'].extend(scan_ports(scan_params['target']))
        if scan_params.get('check_permissions'):
            report['vulnerabilities'].extend(check_file_permissions(scan_params['target']))

        if report['vulnerabilities']:
            report['status'] = 'Vulnerable'
        report['severity_score'] = calculate_severity_score(report['vulnerabilities'])

        return jsonify(report), 200
    except Exception as e:
        return jsonify({'error': f'Error during security scan: {str(e)}'}), 500

def scan_ports(target):
    # Placeholder for port scanning
    return [{'type': 'OpenPort', 'description': 'Port 80 open', 'severity': 'Medium'}]
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Grok

**Satır Sayısı:** 38
```typescript
import express from 'express';
import { Request, Response } from 'express';

const app = express();
app.use(express.json());

app.post('/security-scan', async (req: Request, res: Response) => {
    try {
        const scanParams: any = req.body;
        const report: any = {
            scanTime: new Date().toISOString(),
            target: scanParams.target,
            vulnerabilities: [],
            status: 'Secure'
        };

        if (scanParams.scanPorts) {
            report.vulnerabilities.push(...await scanPorts(scanParams.target));
        }
        if (scanParams.checkPermissions) {
            report.vulnerabilities.push(...await checkFilePermissions(scanParams.target));
        }

        if (report.vulnerabilities.length) {
            report.status = 'Vulnerable';
        }
        report.severityScore = calculateSeverityScore(report.vulnerabilities);

        res.status(200).json(report);
    } catch (error) {
        res.status(500).json({ error: `Error during security scan: ${error.message}` });
    }
});

async function scanPorts(target: string): Promise<any[]> {
    // Placeholder for port scanning
    return [{ type: 'OpenPort', description: 'Port 80 open', severity: 'Medium' }];
}
```