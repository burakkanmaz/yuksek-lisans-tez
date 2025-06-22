 � Senaryo 1: Disk Kullanım Raporu
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
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
🧪 Senaryo 1: Disk Kullanım Raporu
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
from fastapi import FastAPI, HTTPException
import os
import shutil
from fastapi.responses import JSONResponse, FileResponse

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
        return generate_csv_response(report)
    else:
        raise HTTPException(status_code=400, detail="Unsupported format")

def generate_csv_response(data):
    # CSV generation logic here
    pass
🧪 Senaryo 1: Disk Kullanım Raporu
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
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
            return generateCsvResponse(res, report);
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
🧪 Senaryo 2: Dosya İşleme Uygulaması
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
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
🧪 Senaryo 2: Dosya İşleme Uygulaması
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
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
🧪 Senaryo 2: Dosya İşleme Uygulaması
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
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
🧪 Senaryo 3: Log Görüntüleme Aracı
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
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

    var paginatedLogs = logEntries
        .Skip((page - 1) * pageSize)
        .Take(pageSize)
        .ToList();

    return Ok(new {
        TotalEntries = logEntries.Length,
        CurrentPage = page,
        PageSize = pageSize,
        Logs = paginatedLogs
    });
}
🧪 Senaryo 3: Log Görüntüleme Aracı
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

@app.get("/view-logs/")
async def view_logs(log_file_name: str, filter: str = "", page: int = 1, page_size: int = 50):
    log_path = f"logs/{log_file_name}"
    
    try:
        with open(log_path, 'r') as file:
            log_entries = file.readlines()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Log file not found")
    
    if filter:
        log_entries = [line for line in log_entries if filter in line]
    
    start_idx = (page - 1) * page_size
    paginated_logs = log_entries[start_idx:start_idx + page_size]
    
    return {
        "total_entries": len(log_entries),
        "current_page": page,
        "page_size": page_size,
        "logs": paginated_logs
    }
🧪 Senaryo 3: Log Görüntüleme Aracı
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
import express from 'express';
import fs from 'fs';
import path from 'path';

const app = express();

app.get('/view-logs', (req, res) => {
    const { logFileName, filter = '', page = 1, pageSize = 50 } = req.query;
    const logPath = path.join('logs', logFileName as string);
    
    if (!fs.existsSync(logPath)) {
        return res.status(404).json({ error: 'Log file not found' });
    }

    const logContent = fs.readFileSync(logPath, 'utf-8');
    let logEntries = logContent.split('\n');
    
    if (filter) {
        logEntries = logEntries.filter(line => line.includes(filter as string));
    }

    const startIdx = (Number(page) - 1) * Number(pageSize);
    const paginatedLogs = logEntries.slice(startIdx, startIdx + Number(pageSize));
    
    return res.json({
        totalEntries: logEntries.length,
        currentPage: Number(page),
        pageSize: Number(pageSize),
        logs: paginatedLogs
    });
});
🧪 Senaryo 4: Backup Uygulaması
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpPost("create-backup")]
public async Task<IActionResult> CreateBackup(string sourceDirectory, string backupLocation)
{
    if (!Directory.Exists(sourceDirectory))
        return BadRequest("Source directory not found");

    try
    {
        var backupPath = Path.Combine(backupLocation, $"backup_{DateTime.Now:yyyyMMddHHmmss}.zip");
        
        await Task.Run(() => 
        {
            ZipFile.CreateFromDirectory(sourceDirectory, backupPath);
        });

        // Save backup record to database
        var backupRecord = new BackupRecord {
            SourcePath = sourceDirectory,
            BackupPath = backupPath,
            CreatedAt = DateTime.Now,
            Status = "Completed"
        };
        
        _dbContext.BackupRecords.Add(backupRecord);
        await _dbContext.SaveChangesAsync();

        return Ok(new { 
            Message = "Backup completed successfully",
            BackupPath = backupPath 
        });
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Backup failed: {ex.Message}");
    }
}
🧪 Senaryo 4: Backup Uygulaması
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
from fastapi import FastAPI, HTTPException
import shutil
import os
from datetime import datetime
from databases import Database

app = FastAPI()
database = Database("sqlite:///backups.db")

@app.post("/create-backup/")
async def create_backup(source_directory: str, backup_location: str):
    if not os.path.isdir(source_directory):
        raise HTTPException(status_code=400, detail="Source directory not found")
    
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        backup_path = os.path.join(backup_location, f"backup_{timestamp}.zip")
        
        shutil.make_archive(backup_path.replace('.zip', ''), 'zip', source_directory)
        
        # Save to database
        query = "INSERT INTO backups(source_path, backup_path, created_at, status) VALUES (:source, :backup, :created, 'Completed')"
        values = {
            "source": source_directory,
            "backup": backup_path,
            "created": datetime.now()
        }
        await database.execute(query=query, values=values)
        
        return {
            "message": "Backup completed successfully",
            "backup_path": backup_path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Backup failed: {str(e)}")
🧪 Senaryo 4: Backup Uygulaması
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
import express from 'express';
import fs from 'fs';
import path from 'path';
import { exec } from 'child_process';
import { promisify } from 'util';
import { Database } from 'sqlite3';

const app = express();
const execAsync = promisify(exec);
const db = new Database('backups.db');

app.post('/create-backup', async (req, res) => {
    const { sourceDirectory, backupLocation } = req.body;
    
    if (!fs.existsSync(sourceDirectory) || !fs.lstatSync(sourceDirectory).isDirectory()) {
        return res.status(400).json({ error: 'Source directory not found' });
    }

    try {
        const timestamp = new Date().toISOString().replace(/[-:]/g, '').replace('T', '').split('.')[0];
        const backupPath = path.join(backupLocation, `backup_${timestamp}.zip`);
        
        await execAsync(`zip -r ${backupPath} ${sourceDirectory}`);
        
        // Save to database
        db.run(
            'INSERT INTO backups(source_path, backup_path, created_at, status) VALUES (?, ?, ?, ?)',
            [sourceDirectory, backupPath, new Date().toISOString(), 'Completed'],
            (err) => {
                if (err) throw err;
            }
        );

        return res.json({
            message: 'Backup completed successfully',
            backupPath: backupPath
        });
    } catch (error) {
        return res.status(500).json({ error: `Backup failed: ${error.message}` });
    }
});
� Senaryo 5: Ağ Test Aracı
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpGet("test-connection")]
public async Task<IActionResult> TestConnection(string targetAddress)
{
    try
    {
        using var ping = new Ping();
        var reply = await ping.SendPingAsync(targetAddress, 5000);
        
        if (reply.Status != IPStatus.Success)
            return BadRequest($"Connection failed: {reply.Status}");

        var traceroute = await NetworkTools.TraceRouteAsync(targetAddress);
        var speedTest = await NetworkTools.TestSpeedAsync(targetAddress);

        return Ok(new {
            Status = "Success",
            PingTime = reply.RoundtripTime,
            Hops = traceroute,
            DownloadSpeed = speedTest.DownloadSpeed,
            UploadSpeed = speedTest.UploadSpeed,
            Latency = speedTest.Latency
        });
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Connection test failed: {ex.Message}");
    }
}
� Senaryo 5: Ağ Test Aracı
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
from fastapi import FastAPI, HTTPException
import subprocess
import re

app = FastAPI()

@app.get("/test-connection/")
async def test_connection(target_address: str):
    try:
        # Ping test
        ping_result = subprocess.run(['ping', '-c', '4', target_address], capture_output=True, text=True)
        if ping_result.returncode != 0:
            raise HTTPException(status_code=400, detail=f"Ping failed: {ping_result.stderr}")
        
        # Extract ping statistics
        ping_stats = re.search(r'min/avg/max/mdev = (\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+)', ping_result.stdout)
        
        return {
            "status": "Success",
            "ping_time_avg": float(ping_stats.group(2)),
            # Additional network metrics would be added here
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Connection test failed: {str(e)}")
🧪 Senaryo 5: Ağ Test Aracı
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
import express from 'express';
import { exec } from 'child_process';
import { promisify } from 'util';

const app = express();
const execAsync = promisify(exec);

app.get('/test-connection', async (req, res) => {
    const { targetAddress } = req.query;
    
    try {
        // Ping test
        const { stdout: pingOutput } = await execAsync(`ping -c 4 ${targetAddress}`);
        
        // Extract ping time
        const pingMatch = pingOutput.match(/min\/avg\/max\/mdev = \d+\.\d+\/(\d+\.\d+)\//);
        if (!pingMatch) {
            throw new Error('Ping statistics not found');
        }
        
        return res.json({
            status: 'Success',
            pingTime: parseFloat(pingMatch[1]),
            // Additional network metrics would be added here
        });
    } catch (error) {
        return res.status(500).json({ error: `Connection test failed: ${error.message}` });
    }
});
🧪 Senaryo 6: Dosya Sıkıştırma Uygulaması
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpPost("compress-files")]
public IActionResult CompressFiles(List<string> filePaths, string outputPath, string compressionLevel = "Normal")
{
    if (filePaths == null || !filePaths.Any())
        return BadRequest("No files selected");
    
    if (filePaths.Any(path => !System.IO.File.Exists(path)))
        return BadRequest("One or more files not found");

    try
    {
        var compressionLevelEnum = Enum.Parse<CompressionLevel>(compressionLevel);
        using var archive = ZipFile.Open(outputPath, ZipArchiveMode.Create);
        
        foreach (var filePath in filePaths)
        {
            var entry = archive.CreateEntry(Path.GetFileName(filePath), compressionLevelEnum);
            using var entryStream = entry.Open();
            using var fileStream = System.IO.File.OpenRead(filePath);
            fileStream.CopyTo(entryStream);
        }

        return Ok(new { 
            Message = "Compression completed successfully",
            ArchivePath = outputPath,
            CompressedFiles = filePaths.Count
        });
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Compression failed: {ex.Message}");
    }
}
🧪 Senaryo 6: Dosya Sıkıştırma Uygulaması
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
from fastapi import FastAPI, HTTPException
import zipfile
import os

app = FastAPI()

@app.post("/compress-files/")
async def compress_files(file_paths: list[str], output_path: str, compression_level: str = "ZIP_DEFLATED"):
    if not file_paths:
        raise HTTPException(status_code=400, detail="No files selected")
    
    for file_path in file_paths:
        if not os.path.isfile(file_path):
            raise HTTPException(status_code=400, detail=f"File not found: {file_path}")
    
    try:
        compression = getattr(zipfile, compression_level, zipfile.ZIP_DEFLATED)
        
        with zipfile.ZipFile(output_path, 'w', compression) as zipf:
            for file_path in file_paths:
                zipf.write(file_path, os.path.basename(file_path))
        
        return {
            "message": "Compression completed successfully",
            "archive_path": output_path,
            "compressed_files": len(file_paths)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Compression failed: {str(e)}")
🧪 Senaryo 6: Dosya Sıkıştırma Uygulaması
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
import express from 'express';
import fs from 'fs';
import archiver from 'archiver';

const app = express();
app.use(express.json());

app.post('/compress-files', (req, res) => {
    const { filePaths, outputPath } = req.body;
    
    if (!filePaths || filePaths.length === 0) {
        return res.status(400).json({ error: 'No files selected' });
    }
    
    for (const filePath of filePaths) {
        if (!fs.existsSync(filePath)) {
            return res.status(400).json({ error: `File not found: ${filePath}` });
        }
    }
    
    try {
        const output = fs.createWriteStream(outputPath);
        const archive = archiver('zip');
        
        output.on('close', () => {
            return res.json({
                message: 'Compression completed successfully',
                archivePath: outputPath,
                compressedFiles: filePaths.length
            });
        });
        
        archive.pipe(output);
        
        filePaths.forEach(filePath => {
            archive.file(filePath, { name: filePath.split('/').pop() });
        });
        
        archive.finalize();
    } catch (error) {
        return res.status(500).json({ error: `Compression failed: ${error.message}` });
    }
});
🧪 Senaryo 7: Sistem İzleme Aracı
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpGet("monitor-process")]
public IActionResult MonitorProcess(int processId)
{
    try
    {
        var process = Process.GetProcessById(processId);
        var cpuCounter = new PerformanceCounter("Process", "% Processor Time", process.ProcessName);
        var ramCounter = new PerformanceCounter("Process", "Working Set", process.ProcessName);
        
        // First call returns 0, so we need to call NextValue() twice
        cpuCounter.NextValue();
        System.Threading.Thread.Sleep(500);
        
        var cpuUsage = cpuCounter.NextValue();
        var ramUsage = ramCounter.NextValue();

        return Ok(new {
            ProcessName = process.ProcessName,
            CpuUsage = cpuUsage,
            MemoryUsage = ramUsage / (1024 * 1024), // Convert to MB
            ThreadCount = process.Threads.Count,
            StartTime = process.StartTime
        });
    }
    catch (ArgumentException)
    {
        return NotFound($"Process with ID {processId} not found");
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Monitoring failed: {ex.Message}");
    }
}
🧪 Senaryo 7: Sistem İzleme Aracı
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
from fastapi import FastAPI, HTTPException
import psutil

app = FastAPI()

@app.get("/monitor-process/")
async def monitor_process(process_id: int):
    try:
        process = psutil.Process(process_id)
        
        cpu_percent = process.cpu_percent(interval=0.5)
        memory_info = process.memory_info()
        
        return {
            "process_name": process.name(),
            "cpu_usage": cpu_percent,
            "memory_usage": memory_info.rss / (1024 * 1024),  # Convert to MB
            "thread_count": process.num_threads(),
            "start_time": process.create_time()
        }
    except psutil.NoSuchProcess:
        raise HTTPException(status_code=404, detail=f"Process with ID {process_id} not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Monitoring failed: {str(e)}")
🧪 Senaryo 7: Sistem İzleme Aracı
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
import express from 'express';
import { exec } from 'child_process';
import { promisify } from 'util';

const app = express();
const execAsync = promisify(exec);

app.get('/monitor-process', async (req, res) => {
    const { processId } = req.query;
    
    try {
        // Note: This is a simplified example for Linux systems
        const { stdout: psOutput } = await execAsync(`ps -p ${processId} -o %cpu,rss,comm`);
        const lines = psOutput.trim().split('\n');
        
        if (lines.length < 2) {
            throw new Error('Process not found');
        }
        
        const [cpu, mem, name] = lines[1].trim().split(/\s+/);
        
        return res.json({
            processName: name,
            cpuUsage: parseFloat(cpu),
            memoryUsage: Math.round(parseInt(mem) / 1024),  // Convert KB to MB
            // Additional metrics would be added here
        });
    } catch (error) {
        return res.status(500).json({ error: `Monitoring failed: ${error.message}` });
    }
});
🧪 Senaryo 8: Dosya Arama Uygulaması
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpGet("search-files")]
public IActionResult SearchFiles(string searchTerm, string directoryPath = null)
{
    try
    {
        directoryPath = directoryPath ?? Directory.GetCurrentDirectory();
        
        var searchOption = SearchOption.AllDirectories;
        var files = Directory.EnumerateFiles(directoryPath, $"*{searchTerm}*", searchOption)
                            .Select(f => new {
                                Path = f,
                                Size = new FileInfo(f).Length,
                                LastModified = File.GetLastWriteTime(f)
                            })
                            .ToList();

        return Ok(new {
            SearchTerm = searchTerm,
            Directory = directoryPath,
            ResultsCount = files.Count,
            Files = files
        });
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Search failed: {ex.Message}");
    }
}
🧪 Senaryo 8: Dosya Arama Uygulaması
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
from fastapi import FastAPI, HTTPException
import os
from typing import List

app = FastAPI()

@app.get("/search-files/")
async def search_files(search_term: str, directory_path: str = None):
    try:
        directory_path = directory_path or os.getcwd()
        
        results = []
        for root, _, files in os.walk(directory_path):
            for file in files:
                if search_term.lower() in file.lower():
                    file_path = os.path.join(root, file)
                    stat = os.stat(file_path)
                    results.append({
                        "path": file_path,
                        "size": stat.st_size,
                        "last_modified": stat.st_mtime
                    })
        
        return {
            "search_term": search_term,
            "directory": directory_path,
            "results_count": len(results),
            "files": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")
🧪 Senaryo 8: Dosya Arama Uygulaması
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
import express from 'express';
import fs from 'fs';
import path from 'path';

const app = express();

app.get('/search-files', (req, res) => {
    const { searchTerm, directoryPath = process.cwd() } = req.query;
    
    try {
        const results: any[] = [];
        
        function searchDirectory(dir: string) {
            const files = fs.readdirSync(dir);
            
            files.forEach(file => {
                const filePath = path.join(dir, file);
                const stat = fs.statSync(filePath);
                
                if (stat.isDirectory()) {
                    searchDirectory(filePath);
                } else if (file.toLowerCase().includes((searchTerm as string).toLowerCase())) {
                    results.push({
                        path: filePath,
                        size: stat.size,
                        lastModified: stat.mtime
                    });
                }
            });
        }
        
        searchDirectory(directoryPath as string);
        
        return res.json({
            searchTerm,
            directory: directoryPath,
            resultsCount: results.length,
            files: results
        });
    } catch (error) {
        return res.status(500).json({ error: `Search failed: ${error.message}` });
    }
});
🧪 Senaryo 9: Veritabanı Yönetim Aracı
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpPost("execute-query")]
public IActionResult ExecuteQuery(string databaseName, string query)
{
    try
    {
        using var connection = new SqlConnection($"Server=.;Database={databaseName};Integrated Security=True;");
        connection.Open();
        
        using var command = new SqlCommand(query, connection);
        
        if (query.Trim().StartsWith("SELECT", StringComparison.OrdinalIgnoreCase))
        {
            using var reader = command.ExecuteReader();
            var results = new List<Dictionary<string, object>>();
            
            while (reader.Read())
            {
                var row = new Dictionary<string, object>();
                for (var i = 0; i < reader.FieldCount; i++)
                {
                    row[reader.GetName(i)] = reader.GetValue(i);
                }
                results.Add(row);
            }
            
            return Ok(new {
                Database = databaseName,
                Query = query,
                Results = results
            });
        }
        else
        {
            var affectedRows = command.ExecuteNonQuery();
            return Ok(new {
                Database = databaseName,
                Query = query,
                AffectedRows = affectedRows
            });
        }
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Query execution failed: {ex.Message}");
    }
}
🧪 Senaryo 9: Veritabanı Yönetim Aracı
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
from fastapi import FastAPI, HTTPException
import pyodbc
from typing import List, Dict, Any

app = FastAPI()

@app.post("/execute-query/")
async def execute_query(database_name: str, query: str):
    try:
        connection = pyodbc.connect(
            f"Driver={{SQL Server}};Server=.;Database={database_name};Trusted_Connection=yes;")
        cursor = connection.cursor()
        
        if query.strip().upper().startswith("SELECT"):
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            
            return {
                "database": database_name,
                "query": query,
                "results": results
            }
        else:
            affected_rows = cursor.execute(query).rowcount
            connection.commit()
            
            return {
                "database": database_name,
                "query": query,
                "affected_rows": affected_rows
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query execution failed: {str(e)}")
    finally:
        cursor.close()
        connection.close()
🧪 Senaryo 9: Veritabanı Yönetim Aracı
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
import express from 'express';
import { Connection, Request } from 'tedious';

const app = express();
app.use(express.json());

app.post('/execute-query', (req, res) => {
    const { databaseName, query } = req.body;
    
    const config = {
        server: 'localhost',
        authentication: {
            type: 'default',
            options: {
                userName: 'username',
                password: 'password'
            }
        },
        options: {
            database: databaseName,
            encrypt: true
        }
    };
    
    const connection = new Connection(config);
    
    connection.on('connect', (err) => {
        if (err) {
            return res.status(500).json({ error: `Connection failed: ${err.message}` });
        }
        
        const request = new Request(query, (err, rowCount, rows) => {
            connection.close();
            
            if (err) {
                return res.status(500).json({ error: `Query execution failed: ${err.message}` });
            }
            
            if (query.trim().toUpperCase().startsWith('SELECT')) {
                const results = rows.map(row => {
                    const result: any = {};
                    row.forEach(column => {
                        result[column.metadata.colName] = column.value;
                    });
                    return result;
                });
                
                return res.json({
                    database: databaseName,
                    query,
                    results,
                    rowCount
                });
            } else {
                return res.json({
                    database: databaseName,
                    query,
                    affectedRows: rowCount
                });
            }
        });
        
        connection.execSql(request);
    });
    
    connection.connect();
});
🧪 Senaryo 10: Sistem Güvenlik Aracı
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpPost("security-scan")]
public IActionResult PerformSecurityScan(string scanType, string targetPath)
{
    try
    {
        var scanResults = new List<SecurityIssue>();
        
        switch (scanType.ToLower())
        {
            case "vulnerability":
                scanResults = SecurityScanner.CheckForVulnerabilities(targetPath);
                break;
            case "malware":
                scanResults = SecurityScanner.ScanForMalware(targetPath);
                break;
            case "permissions":
                scanResults = SecurityScanner.CheckPermissions(targetPath);
                break;
            default:
                return BadRequest("Unsupported scan type");
        }

        return Ok(new {
            ScanType = scanType,
            Target = targetPath,
            IssuesFound = scanResults.Count,
            Issues = scanResults
        });
    }
    catch (Exception ex)
    {
        return StatusCode(500, $"Security scan failed: {ex.Message}");
    }
}
🧪 Senaryo 10: Sistem Güvenlik Aracı
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
from fastapi import FastAPI, HTTPException
from typing import List
import security_scanner

app = FastAPI()

@app.post("/security-scan/")
async def perform_security_scan(scan_type: str, target_path: str):
    try:
        scan_results = []
        
        if scan_type.lower() == "vulnerability":
            scan_results = await security_scanner.check_vulnerabilities(target_path)
        elif scan_type.lower() == "malware":
            scan_results = await security_scanner.scan_malware(target_path)
        elif scan_type.lower