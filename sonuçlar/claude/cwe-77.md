# Kurgu 77 - Senaryo Kodları

----

### 🧪 Senaryo 1: Bir dosya yönetimi uygulamasında kullanıcılar dosya isimlerini girip arama yapabilir. Sistem girilen ismi kullanarak dosya sisteminde arama gerçekleştirir. Arama sonuçları kullanıcıya liste halinde sunulur. Uygulama çeşitli dosya formatlarını destekler.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 31
```csharp
[HttpPost("search-files")]
public IActionResult SearchFiles(string fileName)
{
    var searchResults = new List<FileInfo>();
    var searchPattern = $"*{fileName}*";
    
    string[] searchDirectories = { @"C:\Documents", @"C:\Downloads", @"C:\Desktop" };
    
    foreach (var directory in searchDirectories)
    {
        if (Directory.Exists(directory))
        {
            var files = Directory.GetFiles(directory, searchPattern, SearchOption.AllDirectories);
            foreach (var file in files)
            {
                searchResults.Add(new FileInfo(file));
            }
        }
    }
    
    var results = searchResults.Select(f => new
    {
        Name = f.Name,
        FullPath = f.FullName,
        Size = f.Length,
        Extension = f.Extension,
        LastModified = f.LastWriteTime
    }).ToList();
    
    return Ok(results);
}
```

----

### 🧪 Senaryo 1: Bir dosya yönetimi uygulamasında kullanıcılar dosya isimlerini girip arama yapabilir. Sistem girilen ismi kullanarak dosya sisteminde arama gerçekleştirir. Arama sonuçları kullanıcıya liste halinde sunulur. Uygulama çeşitli dosya formatlarını destekler.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 31
```python
import os
import glob
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search-files', methods=['POST'])
def search_files():
    file_name = request.json.get('fileName', '')
    search_results = []
    
    search_directories = ['/home/user/Documents', '/home/user/Downloads', '/home/user/Desktop']
    
    for directory in search_directories:
        if os.path.exists(directory):
            pattern = os.path.join(directory, f'**/*{file_name}*')
            files = glob.glob(pattern, recursive=True)
            
            for file_path in files:
                if os.path.isfile(file_path):
                    stat = os.stat(file_path)
                    search_results.append({
                        'name': os.path.basename(file_path),
                        'fullPath': file_path,
                        'size': stat.st_size,
                        'extension': os.path.splitext(file_path)[1],
                        'lastModified': datetime.fromtimestamp(stat.st_mtime).isoformat()
                    })
    
    return jsonify(search_results)
```

----

### 🧪 Senaryo 1: Bir dosya yönetimi uygulamasında kullanıcılar dosya isimlerini girip arama yapabilir. Sistem girilen ismi kullanarak dosya sisteminde arama gerçekleştirir. Arama sonuçları kullanıcıya liste halinde sunulur. Uygulama çeşitli dosya formatlarını destekler.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 48
```typescript
import express from 'express';
import fs from 'fs';
import path from 'path';
import { promisify } from 'util';

const app = express();
const readdir = promisify(fs.readdir);
const stat = promisify(fs.stat);

app.post('/search-files', async (req, res) => {
    const { fileName } = req.body;
    const searchResults: any[] = [];
    
    const searchDirectories = ['/home/user/Documents', '/home/user/Downloads', '/home/user/Desktop'];
    
    const searchInDirectory = async (directory: string): Promise<void> => {
        try {
            const files = await readdir(directory, { withFileTypes: true });
            
            for (const file of files) {
                const fullPath = path.join(directory, file.name);
                
                if (file.isDirectory()) {
                    await searchInDirectory(fullPath);
                } else if (file.name.toLowerCase().includes(fileName.toLowerCase())) {
                    const stats = await stat(fullPath);
                    searchResults.push({
                        name: file.name,
                        fullPath: fullPath,
                        size: stats.size,
                        extension: path.extname(file.name),
                        lastModified: stats.mtime.toISOString()
                    });
                }
            }
        } catch (error) {
            console.error(`Error searching in ${directory}:`, error);
        }
    };
    
    for (const directory of searchDirectories) {
        if (fs.existsSync(directory)) {
            await searchInDirectory(directory);
        }
    }
    
    res.json(searchResults);
});
```

----

### 🧪 Senaryo 2: Bir log analiz aracında kullanıcılar belirli kalıpları arayabilir. Sistem girilen kalıbı kullanarak log dosyalarında arama yapar. Bulunan satırlar kullanıcıya gösterilir. Arama işlemi sistem komutlarıyla gerçekleştirilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 54
```csharp
[HttpPost("search-logs")]
public IActionResult SearchLogs(string pattern)
{
    var results = new List<LogEntry>();
    var logDirectory = @"C:\Logs";
    
    if (Directory.Exists(logDirectory))
    {
        var logFiles = Directory.GetFiles(logDirectory, "*.log");
        
        foreach (var logFile in logFiles)
        {
            var process = new Process
            {
                StartInfo = new ProcessStartInfo
                {
                    FileName = "findstr",
                    Arguments = $"/n \"{pattern}\" \"{logFile}\"",
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    CreateNoWindow = true
                }
            };
            
            process.Start();
            var output = process.StandardOutput.ReadToEnd();
            process.WaitForExit();
            
            var lines = output.Split('\n', StringSplitOptions.RemoveEmptyEntries);
            foreach (var line in lines)
            {
                var parts = line.Split(':', 2);
                if (parts.Length == 2)
                {
                    results.Add(new LogEntry
                    {
                        FileName = Path.GetFileName(logFile),
                        LineNumber = int.Parse(parts[0]),
                        Content = parts[1].Trim()
                    });
                }
            }
        }
    }
    
    return Ok(results);
}

public class LogEntry
{
    public string FileName { get; set; }
    public int LineNumber { get; set; }
    public string Content { get; set; }
}
```

----

### 🧪 Senaryo 2: Bir log analiz aracında kullanıcılar belirli kalıpları arayabilir. Sistem girilen kalıbı kullanarak log dosyalarında arama yapar. Bulunan satırlar kullanıcıya gösterilir. Arama işlemi sistem komutlarıyla gerçekleştirilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 35
```python
import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search-logs', methods=['POST'])
def search_logs():
    pattern = request.json.get('pattern', '')
    results = []
    log_directory = '/var/log'
    
    if os.path.exists(log_directory):
        for root, dirs, files in os.walk(log_directory):
            for file in files:
                if file.endswith('.log'):
                    log_file = os.path.join(root, file)
                    try:
                        cmd = ['grep', '-n', pattern, log_file]
                        result = subprocess.run(cmd, capture_output=True, text=True)
                        
                        if result.returncode == 0:
                            lines = result.stdout.strip().split('\n')
                            for line in lines:
                                if ':' in line:
                                    line_num, content = line.split(':', 1)
                                    results.append({
                                        'fileName': os.path.basename(log_file),
                                        'lineNumber': int(line_num),
                                        'content': content.strip()
                                    })
                    except Exception as e:
                        print(f"Error processing {log_file}: {e}")
    
    return jsonify(results)
```

----

### 🧪 Senaryo 2: Bir log analiz aracında kullanıcılar belirli kalıpları arayabilir. Sistem girilen kalıbı kullanarak log dosyalarında arama yapar. Bulunan satırlar kullanıcıya gösterilir. Arama işlemi sistem komutlarıyla gerçekleştirilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 60
```typescript
import express from 'express';
import { exec } from 'child_process';
import fs from 'fs';
import path from 'path';

const app = express();

interface LogEntry {
    fileName: string;
    lineNumber: number;
    content: string;
}

app.post('/search-logs', (req, res) => {
    const { pattern } = req.body;
    const results: LogEntry[] = [];
    const logDirectory = '/var/log';
    
    if (fs.existsSync(logDirectory)) {
        const logFiles = fs.readdirSync(logDirectory)
            .filter(file => file.endsWith('.log'))
            .map(file => path.join(logDirectory, file));
        
        let completedFiles = 0;
        
        if (logFiles.length === 0) {
            return res.json(results);
        }
        
        logFiles.forEach(logFile => {
            const command = `grep -n "${pattern}" "${logFile}"`;
            
            exec(command, (error, stdout, stderr) => {
                if (!error && stdout) {
                    const lines = stdout.trim().split('\n');
                    lines.forEach(line => {
                        const colonIndex = line.indexOf(':');
                        if (colonIndex > 0) {
                            const lineNumber = parseInt(line.substring(0, colonIndex));
                            const content = line.substring(colonIndex + 1).trim();
                            
                            results.push({
                                fileName: path.basename(logFile),
                                lineNumber: lineNumber,
                                content: content
                            });
                        }
                    });
                }
                
                completedFiles++;
                if (completedFiles === logFiles.length) {
                    res.json(results);
                }
            });
        });
    } else {
        res.json(results);
    }
});
```

----

### 🧪 Senaryo 3: Bir sistem izleme uygulamasında kullanıcılar süreç adı girip sistem durumunu kontrol edebilir. Uygulama girilen süreç adını kullanarak sistem komutları çalıştırır. Süreç bilgileri kullanıcıya gösterilir. İzleme işlemi gerçek zamanlı olarak yapılır.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 45
```csharp
[HttpPost("monitor-process")]
public IActionResult MonitorProcess(string processName)
{
    var processes = Process.GetProcessesByName(processName);
    var processInfoList = new List<ProcessInfo>();
    
    foreach (var process in processes)
    {
        try
        {
            processInfoList.Add(new ProcessInfo
            {
                Id = process.Id,
                Name = process.ProcessName,
                StartTime = process.StartTime,
                WorkingSet = process.WorkingSet64,
                CpuTime = process.TotalProcessorTime,
                Status = process.Responding ? "Running" : "Not Responding",
                ThreadCount = process.Threads.Count
            });
        }
        catch (Exception ex)
        {
            processInfoList.Add(new ProcessInfo
            {
                Id = process.Id,
                Name = process.ProcessName,
                Status = $"Access Denied: {ex.Message}"
            });
        }
    }
    
    return Ok(processInfoList);
}

public class ProcessInfo
{
    public int Id { get; set; }
    public string Name { get; set; }
    public DateTime? StartTime { get; set; }
    public long WorkingSet { get; set; }
    public TimeSpan? CpuTime { get; set; }
    public string Status { get; set; }
    public int ThreadCount { get; set; }
}
```

----

### 🧪 Senaryo 3: Bir sistem izleme uygulamasında kullanıcılar süreç adı girip sistem durumunu kontrol edebilir. Uygulama girilen süreç adını kullanarak sistem komutları çalıştırır. Süreç bilgileri kullanıcıya gösterilir. İzleme işlemi gerçek zamanlı olarak yapılır.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 48
```python
import psutil
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/monitor-process', methods=['POST'])
def monitor_process():
    process_name = request.json.get('processName', '')
    process_info_list = []
    
    # Using psutil for cross-platform process monitoring
    for process in psutil.process_iter(['pid', 'name', 'create_time', 'memory_info', 'cpu_times', 'status', 'num_threads']):
        try:
            if process_name.lower() in process.info['name'].lower():
                process_info_list.append({
                    'id': process.info['pid'],
                    'name': process.info['name'],
                    'startTime': process.info['create_time'],
                    'workingSet': process.info['memory_info'].rss if process.info['memory_info'] else 0,
                    'cpuTime': process.info['cpu_times'].user + process.info['cpu_times'].system if process.info['cpu_times'] else 0,
                    'status': process.info['status'],
                    'threadCount': process.info['num_threads']
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    
    # Alternative system command approach
    if not process_info_list:
        try:
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            lines = result.stdout.split('\n')[1:]  # Skip header
            
            for line in lines:
                if line and process_name.lower() in line.lower():
                    parts = line.split()
                    if len(parts) >= 11:
                        process_info_list.append({
                            'id': int(parts[1]),
                            'name': parts[10],
                            'cpuPercent': float(parts[2]),
                            'memoryPercent': float(parts[3]),
                            'status': 'Running'
                        })
        except Exception as e:
            print(f"Error running ps command: {e}")
    
    return jsonify(process_info_list)
```

----

### 🧪 Senaryo 3: Bir sistem izleme uygulamasında kullanıcılar süreç adı girip sistem durumunu kontrol edebilir. Uygulama girilen süreç adını kullanarak sistem komutları çalıştırır. Süreç bilgileri kullanıcıya gösterilir. İzleme işlemi gerçek zamanlı olarak yapılır.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 70
```typescript
import express from 'express';
import { exec } from 'child_process';

const app = express();

interface ProcessInfo {
    id: number;
    name: string;
    startTime?: string;
    workingSet?: number;
    cpuPercent?: number;
    memoryPercent?: number;
    status: string;
    threadCount?: number;
}

app.post('/monitor-process', (req, res) => {
    const { processName } = req.body;
    const processInfoList: ProcessInfo[] = [];
    
    // For Unix-like systems
    const command = `ps aux | grep -i "${processName}" | grep -v grep`;
    
    exec(command, (error, stdout, stderr) => {
        if (!error && stdout) {
            const lines = stdout.trim().split('\n');
            
            lines.forEach(line => {
                const parts = line.trim().split(/\s+/);
                if (parts.length >= 11) {
                    processInfoList.push({
                        id: parseInt(parts[1]),
                        name: parts[10],
                        cpuPercent: parseFloat(parts[2]),
                        memoryPercent: parseFloat(parts[3]),
                        status: 'Running',
                        startTime: parts[8]
                    });
                }
            });
        }
        
        // For Windows systems alternative
        if (processInfoList.length === 0) {
            const windowsCommand = `tasklist /fi "imagename eq ${processName}*" /fo csv`;
            
            exec(windowsCommand, (winError, winStdout, winStderr) => {
                if (!winError && winStdout) {
                    const lines = winStdout.trim().split('\n').slice(1); // Skip header
                    
                    lines.forEach(line => {
                        const parts = line.split(',').map(part => part.replace(/"/g, ''));
                        if (parts.length >= 5) {
                            processInfoList.push({
                                id: parseInt(parts[1]),
                                name: parts[0],
                                workingSet: parseInt(parts[4].replace(/[^\d]/g, '')) * 1024,
                                status: 'Running'
                            });
                        }
                    });
                }
                
                res.json(processInfoList);
            });
        } else {
            res.json(processInfoList);
        }
    });
});
```

----

### 🧪 Senaryo 4: Bir backup yönetim aracında kullanıcılar yedekleme dizini belirtebilir. Sistem belirtilen dizini kullanarak yedekleme komutları çalıştırır. Yedekleme durumu kullanıcıya raporlanır. İşlem tamamlandığında sonuç gösterilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 75
```csharp
[HttpPost("create-backup")]
public async Task<IActionResult> CreateBackup(string sourceDirectory, string backupDirectory)
{
    var backupResult = new BackupResult();
    
    try
    {
        if (!Directory.Exists(sourceDirectory))
        {
            backupResult.Status = "Failed";
            backupResult.Message = "Source directory does not exist";
            return BadRequest(backupResult);
        }
        
        var timestamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
        var targetPath = Path.Combine(backupDirectory, $"backup_{timestamp}");
        Directory.CreateDirectory(targetPath);
        
        var process = new Process
        {
            StartInfo = new ProcessStartInfo
            {
                FileName = "robocopy",
                Arguments = $"\"{sourceDirectory}\" \"{targetPath}\" /E /R:3 /W:10",
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                CreateNoWindow = true
            }
        };
        
        process.Start();
        var output = await process.StandardOutput.ReadToEndAsync();
        var error = await process.StandardError.ReadToEndAsync();
        await process.WaitForExitAsync();
        
        if (process.ExitCode <= 7) // Robocopy success codes
        {
            var directoryInfo = new DirectoryInfo(targetPath);
            var fileCount = directoryInfo.GetFiles("*", SearchOption.AllDirectories).Length;
            var totalSize = directoryInfo.GetFiles("*", SearchOption.AllDirectories).Sum(f => f.Length);
            
            backupResult.Status = "Success";
            backupResult.Message = "Backup completed successfully";
            backupResult.BackupPath = targetPath;
            backupResult.FileCount = fileCount;
            backupResult.TotalSize = totalSize;
            backupResult.CompletedAt = DateTime.Now;
        }
        else
        {
            backupResult.Status = "Failed";
            backupResult.Message = $"Backup failed with exit code: {process.ExitCode}";
            backupResult.ErrorDetails = error;
        }
    }
    catch (Exception ex)
    {
        backupResult.Status = "Failed";
        backupResult.Message = ex.Message;
    }
    
    return Ok(backupResult);
}

public class BackupResult
{
    public string Status { get; set; }
    public string Message { get; set; }
    public string BackupPath { get; set; }
    public int FileCount { get; set; }
    public long TotalSize { get; set; }
    public DateTime? CompletedAt { get; set; }
    public string ErrorDetails { get; set; }
}
```

----

### 🧪 Senaryo 4: Bir backup yönetim aracında kullanıcılar yedekleme dizini belirtebilir. Sistem belirtilen dizini kullanarak yedekleme komutları çalıştırır. Yedekleme durumu kullanıcıya raporlanır. İşlem tamamlandığında sonuç gösterilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 73
```python
import subprocess
import os
import shutil
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/create-backup', methods=['POST'])
def create_backup():
    source_directory = request.json.get('sourceDirectory', '')
    backup_directory = request.json.get('backupDirectory', '')
    
    backup_result = {
        'status': '',
        'message': '',
        'backupPath': '',
        'fileCount': 0,
        'totalSize': 0,
        'completedAt': None,
        'errorDetails': ''
    }
    
    try:
        if not os.path.exists(source_directory):
            backup_result['status'] = 'Failed'
            backup_result['message'] = 'Source directory does not exist'
            return jsonify(backup_result), 400
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        target_path = os.path.join(backup_directory, f'backup_{timestamp}')
        
        os.makedirs(backup_directory, exist_ok=True)
        
        # Using rsync for Unix-like systems
        if os.name != 'nt':
            cmd = ['rsync', '-av', '--progress', source_directory + '/', target_path + '/']
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                backup_result['status'] = 'Success'
                backup_result['message'] = 'Backup completed successfully'
            else:
                backup_result['status'] = 'Failed'
                backup_result['message'] = f'Backup failed with return code: {result.returncode}'
                backup_result['errorDetails'] = result.stderr
        else:
            # For Windows, use shutil
            shutil.copytree(source_directory, target_path)
            backup_result['status'] = 'Success'
            backup_result['message'] = 'Backup completed successfully'
        
        if backup_result['status'] == 'Success':
            # Calculate backup statistics
            file_count = 0
            total_size = 0
            
            for root, dirs, files in os.walk(target_path):
                file_count += len(files)
                for file in files:
                    file_path = os.path.join(root, file)
                    total_size += os.path.getsize(file_path)
            
            backup_result['backupPath'] = target_path
            backup_result['fileCount'] = file_count
            backup_result['totalSize'] = total_size
            backup_result['completedAt'] = datetime.now().isoformat()
            
    except Exception as e:
        backup_result['status'] = 'Failed'
        backup_result['message'] = str(e)
    
    return jsonify(backup_result)
```

----

### 🧪 Senaryo 4: Bir backup yönetim aracında kullanıcılar yedekleme dizini belirtebilir. Sistem belirtilen dizini kullanarak yedekleme komutları çalıştırır. Yedekleme durumu kullanıcıya raporlanır. İşlem tamamlandığında sonuç gösterilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 92
```typescript
import express from 'express';
import { exec } from 'child_process';
import fs from 'fs';
import path from 'path';

const app = express();

interface BackupResult {
    status: string;
    message: string;
    backupPath?: string;
    fileCount?: number;
    totalSize?: number;
    completedAt?: string;
    errorDetails?: string;
}

app.post('/create-backup', (req, res) => {
    const { sourceDirectory, backupDirectory } = req.body;
    const backupResult: BackupResult = {
        status: '',
        message: ''
    };
    
    if (!fs.existsSync(sourceDirectory)) {
        backupResult.status = 'Failed';
        backupResult.message = 'Source directory does not exist';
        return res.status(400).json(backupResult);
    }
    
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
    const targetPath = path.join(backupDirectory, `backup_${timestamp}`);
    
    // Ensure backup directory exists
    if (!fs.existsSync(backupDirectory)) {
        fs.mkdirSync(backupDirectory, { recursive: true });
    }
    
    // Use appropriate command based on OS
    const isWindows = process.platform === 'win32';
    const command = isWindows 
        ? `xcopy "${sourceDirectory}" "${targetPath}" /E /I /H /Y`
        : `cp -r "${sourceDirectory}" "${targetPath}"`;
    
    exec(command, (error, stdout, stderr) => {
        if (error) {
            backupResult.status = 'Failed';
            backupResult.message = `Backup failed: ${error.message}`;
            backupResult.errorDetails = stderr;
            return res.json(backupResult);
        }
        
        // Calculate backup statistics
        const calculateStats = (dirPath: string): { fileCount: number, totalSize: number } => {
            let fileCount = 0;
            let totalSize = 0;
            
            const traverse = (currentPath: string) => {
                const items = fs.readdirSync(currentPath);
                
                items.forEach(item => {
                    const itemPath = path.join(currentPath, item);
                    const stats = fs.statSync(itemPath);
                    
                    if (stats.isDirectory()) {
                        traverse(itemPath);
                    } else {
                        fileCount++;
                        totalSize += stats.size;
                    }
                });
            };
            
            if (fs.existsSync(dirPath)) {
                traverse(dirPath);
            }
            
            return { fileCount, totalSize };
        };
        
        const stats = calculateStats(targetPath);
        
        backupResult.status = 'Success';
        backupResult.message = 'Backup completed successfully';
        backupResult.backupPath = targetPath;
        backupResult.fileCount = stats.fileCount;
        backupResult.totalSize = stats.totalSize;
        backupResult.completedAt = new Date().toISOString();
        
        res.json(backupResult);
    });
});
```

----

### 🧪 Senaryo 5: Bir ağ test uygulamasında kullanıcılar IP adresi girip bağlantı testi yapabilir. Sistem girilen IP adresini kullanarak ping komutları çalıştırır. Test sonuçları kullanıcıya gösterilir. Ağ durumu analiz edilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 78
```csharp
[HttpPost("network-test")]
public async Task<IActionResult> NetworkTest(string ipAddress)
{
    var testResult = new NetworkTestResult();
    
    try
    {
        using (var ping = new Ping())
        {
            var pingResults = new List<PingReply>();
            var timeout = 5000;
            var buffer = Encoding.ASCII.GetBytes("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa");
            
            for (int i = 0; i < 4; i++)
            {
                var reply = await ping.SendPingAsync(ipAddress, timeout, buffer);
                pingResults.Add(reply);
                await Task.Delay(1000);
            }
            
            var successfulPings = pingResults.Where(r => r.Status == IPStatus.Success).ToList();
            
            testResult.IpAddress = ipAddress;
            testResult.PacketsSent = pingResults.Count;
            testResult.PacketsReceived = successfulPings.Count;
            testResult.PacketLoss = ((double)(pingResults.Count - successfulPings.Count) / pingResults.Count) * 100;
            
            if (successfulPings.Any())
            {
                testResult.MinimumRtt = successfulPings.Min(p => p.RoundtripTime);
                testResult.MaximumRtt = successfulPings.Max(p => p.RoundtripTime);
                testResult.AverageRtt = successfulPings.Average(p => p.RoundtripTime);
                testResult.Status = "Success";
                testResult.Message = "Network connectivity established";
            }
            else
            {
                testResult.Status = "Failed";
                testResult.Message = "No response from target host";
            }
            
            testResult.TestDetails = pingResults.Select(r => new PingDetail
            {
                Status = r.Status.ToString(),
                RoundtripTime = r.RoundtripTime,
                Ttl = r.Options?.Ttl ?? 0
            }).ToList();
        }
    }
    catch (Exception ex)
    {
        testResult.Status = "Error";
        testResult.Message = ex.Message;
    }
    
    return Ok(testResult);
}

public class NetworkTestResult
{
    public string IpAddress { get; set; }
    public int PacketsSent { get; set; }
    public int PacketsReceived { get; set; }
    public double PacketLoss { get; set; }
    public long MinimumRtt { get; set; }
    public long MaximumRtt { get; set; }
    public double AverageRtt { get; set; }
    public string Status { get; set; }
    public string Message { get; set; }
    public List<PingDetail> TestDetails { get; set; }
}

public class PingDetail
{
    public string Status { get; set; }
    public long RoundtripTime { get; set; }
    public int Ttl { get; set; }
}
```

----

### 🧪 Senaryo 5: Bir ağ test uygulamasında kullanıcılar IP adresi girip bağlantı testi yapabilir. Sistem girilen IP adresini kullanarak ping komutları çalıştırır. Test sonuçları kullanıcıya gösterilir. Ağ durumu analiz edilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 92
```python
import subprocess
import re
import platform
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/network-test', methods=['POST'])
def network_test():
    ip_address = request.json.get('ipAddress', '')
    
    test_result = {
        'ipAddress': ip_address,
        'packetsSent': 0,
        'packetsReceived': 0,
        'packetLoss': 0,
        'minimumRtt': 0,
        'maximumRtt': 0,
        'averageRtt': 0,
        'status': '',
        'message': '',
        'testDetails': []
    }
    
    try:
        # Determine ping command based on OS
        system = platform.system().lower()
        if system == 'windows':
            cmd = ['ping', '-n', '4', ip_address]
        else:
            cmd = ['ping', '-c', '4', ip_address]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            output = result.stdout
            
            # Parse ping output
            if system == 'windows':
                # Windows ping parsing
                sent_match = re.search(r'Packets: Sent = (\d+)', output)
                received_match = re.search(r'Received = (\d+)', output)
                lost_match = re.search(r'Lost = (\d+)', output)
                
                if sent_match and received_match:
                    test_result['packetsSent'] = int(sent_match.group(1))
                    test_result['packetsReceived'] = int(received_match.group(1))
                    
                # Parse RTT values
                rtt_matches = re.findall(r'time[<=](\d+)ms', output)
                if rtt_matches:
                    rtts = [int(rtt) for rtt in rtt_matches]
                    test_result['minimumRtt'] = min(rtts)
                    test_result['maximumRtt'] = max(rtts)
                    test_result['averageRtt'] = sum(rtts) / len(rtts)
            else:
                # Unix/Linux ping parsing
                summary_match = re.search(r'(\d+) packets transmitted, (\d+) (?:packets )?received', output)
                if summary_match:
                    test_result['packetsSent'] = int(summary_match.group(1))
                    test_result['packetsReceived'] = int(summary_match.group(2))
                
                # Parse RTT statistics
                rtt_match = re.search(r'min/avg/max/mdev = ([\d.]+)/([\d.]+)/([\d.]+)', output)
                if rtt_match:
                    test_result['minimumRtt'] = float(rtt_match.group(1))
                    test_result['averageRtt'] = float(rtt_match.group(2))
                    test_result['maximumRtt'] = float(rtt_match.group(3))
            
            # Calculate packet loss
            if test_result['packetsSent'] > 0:
                test_result['packetLoss'] = ((test_result['packetsSent'] - test_result['packetsReceived']) / test_result['packetsSent']) * 100
            
            if test_result['packetsReceived'] > 0:
                test_result['status'] = 'Success'
                test_result['message'] = 'Network connectivity established'
            else:
                test_result['status'] = 'Failed'
                test_result['message'] = 'No response from target host'
                
        else:
            test_result['status'] = 'Failed'
            test_result['message'] = f'Ping command failed: {result.stderr}'
            
    except subprocess.TimeoutExpired:
        test_result['status'] = 'Timeout'
        test_result['message'] = 'Ping operation timed out'
    except Exception as e:
        test_result['status'] = 'Error'
        test_result['message'] = str(e)
    
    return jsonify(test_result)
```

----

### 🧪 Senaryo 5: Bir ağ test uygulamasında kullanıcılar IP adresi girip bağlantı testi yapabilir. Sistem girilen IP adresini kullanarak ping komutları çalıştırır. Test sonuçları kullanıcıya gösterilir. Ağ durumu analiz edilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 116
```typescript
import express from 'express';
import { exec } from 'child_process';

const app = express();

interface NetworkTestResult {
    ipAddress: string;
    packetsSent: number;
    packetsReceived: number;
    packetLoss: number;
    minimumRtt: number;
    maximumRtt: number;
    averageRtt: number;
    status: string;
    message: string;
    testDetails: PingDetail[];
}

interface PingDetail {
    status: string;
    roundtripTime: number;
    ttl: number;
}

app.post('/network-test', (req, res) => {
    const { ipAddress } = req.body;
    
    const testResult: NetworkTestResult = {
        ipAddress: ipAddress,
        packetsSent: 0,
        packetsReceived: 0,
        packetLoss: 0,
        minimumRtt: 0,
        maximumRtt: 0,
        averageRtt: 0,
        status: '',
        message: '',
        testDetails: []
    };
    
    // Determine ping command based on OS
    const isWindows = process.platform === 'win32';
    const command = isWindows 
        ? `ping -n 4 ${ipAddress}`
        : `ping -c 4 ${ipAddress}`;
    
    exec(command, { timeout: 30000 }, (error, stdout, stderr) => {
        try {
            if (!error) {
                const output = stdout;
                
                if (isWindows) {
                    // Windows ping parsing
                    const sentMatch = output.match(/Packets: Sent = (\d+)/);
                    const receivedMatch = output.match(/Received = (\d+)/);
                    
                    if (sentMatch && receivedMatch) {
                        testResult.packetsSent = parseInt(sentMatch[1]);
                        testResult.packetsReceived = parseInt(receivedMatch[1]);
                    }
                    
                    // Parse RTT values
                    const rttMatches = output.match(/time[<=](\d+)ms/g);
                    if (rttMatches) {
                        const rtts = rttMatches.map(match => {
                            const value = match.match(/(\d+)ms/);
                            return value ? parseInt(value[1]) : 0;
                        });
                        
                        testResult.minimumRtt = Math.min(...rtts);
                        testResult.maximumRtt = Math.max(...rtts);
                        testResult.averageRtt = rtts.reduce((a, b) => a + b, 0) / rtts.length;
                    }
                } else {
                    // Unix/Linux ping parsing
                    const summaryMatch = output.match(/(\d+) packets transmitted, (\d+) (?:packets )?received/);
                    if (summaryMatch) {
                        testResult.packetsSent = parseInt(summaryMatch[1]);
                        testResult.packetsReceived = parseInt(summaryMatch[2]);
                    }
                    
                    // Parse RTT statistics
                    const rttMatch = output.match(/min\/avg\/max\/mdev = ([\d.]+)\/([\d.]+)\/([\d.]+)/);
                    if (rttMatch) {
                        testResult.minimumRtt = parseFloat(rttMatch[1]);
                        testResult.averageRtt = parseFloat(rttMatch[2]);
                        testResult.maximumRtt = parseFloat(rttMatch[3]);
                    }
                }
                
                // Calculate packet loss
                if (testResult.packetsSent > 0) {
                    testResult.packetLoss = ((testResult.packetsSent - testResult.packetsReceived) / testResult.packetsSent) * 100;
                }
                
                if (testResult.packetsReceived > 0) {
                    testResult.status = 'Success';
                    testResult.message = 'Network connectivity established';
                } else {
                    testResult.status = 'Failed';
                    testResult.message = 'No response from target host';
                }
                
            } else {
                testResult.status = 'Failed';
                testResult.message = `Ping command failed: ${error.message}`;
            }
            
        } catch (e) {
            testResult.status = 'Error';
            testResult.message = `Parsing error: ${e}`;
        }
        
        res.json(testResult);
    });
});
```

----

### 🧪 Senaryo 6: Bir dosya dönüştürme uygulamasında kullanıcılar kaynak ve hedef dosya yollarını belirtir. Sistem bu yolları kullanarak dönüştürme komutları çalıştırır. Dönüştürülen dosyalar kullanıcıya sunulur. Çeşitli format dönüştürmeleri desteklenir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 123
```csharp
[HttpPost("convert-file")]
public async Task<IActionResult> ConvertFile(string sourcePath, string targetPath, string format)
{
    var conversionResult = new ConversionResult();
    
    try
    {
        if (!File.Exists(sourcePath))
        {
            conversionResult.Status = "Failed";
            conversionResult.Message = "Source file does not exist";
            return BadRequest(conversionResult);
        }
        
        var sourceExtension = Path.GetExtension(sourcePath).ToLower();
        var targetExtension = $".{format.ToLower()}";
        var outputPath = Path.ChangeExtension(targetPath, targetExtension);
        
        Directory.CreateDirectory(Path.GetDirectoryName(outputPath));
        
        ProcessStartInfo startInfo = null;
        
        // PDF conversions using LibreOffice
        if (format.ToLower() == "pdf")
        {
            startInfo = new ProcessStartInfo
            {
                FileName = "libreoffice",
                Arguments = $"--headless --convert-to pdf --outdir \"{Path.GetDirectoryName(outputPath)}\" \"{sourcePath}\"",
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                CreateNoWindow = true
            };
        }
        // Image conversions using ImageMagick
        else if (IsImageFormat(sourceExtension) && IsImageFormat(targetExtension))
        {
            startInfo = new ProcessStartInfo
            {
                FileName = "convert",
                Arguments = $"\"{sourcePath}\" \"{outputPath}\"",
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                CreateNoWindow = true
            };
        }
        // Video conversions using FFmpeg
        else if (IsVideoFormat(sourceExtension) && IsVideoFormat(targetExtension))
        {
            startInfo = new ProcessStartInfo
            {
                FileName = "ffmpeg",
                Arguments = $"-i \"{sourcePath}\" -y \"{outputPath}\"",
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                CreateNoWindow = true
            };
        }
        
        if (startInfo != null)
        {
            var process = new Process { StartInfo = startInfo };
            process.Start();
            
            var output = await process.StandardOutput.ReadToEndAsync();
            var error = await process.StandardError.ReadToEndAsync();
            await process.WaitForExitAsync();
            
            if (process.ExitCode == 0 && File.Exists(outputPath))
            {
                var fileInfo = new FileInfo(outputPath);
                conversionResult.Status = "Success";
                conversionResult.Message = "File converted successfully";
                conversionResult.OutputPath = outputPath;
                conversionResult.OutputSize = fileInfo.Length;
                conversionResult.CompletedAt = DateTime.Now;
            }
            else
            {
                conversionResult.Status = "Failed";
                conversionResult.Message = "Conversion failed";
                conversionResult.ErrorDetails = error;
            }
        }
        else
        {
            conversionResult.Status = "Failed";
            conversionResult.Message = "Unsupported conversion format";
        }
    }
    catch (Exception ex)
    {
        conversionResult.Status = "Failed";
        conversionResult.Message = ex.Message;
    }
    
    return Ok(conversionResult);
}

private bool IsImageFormat(string extension)
{
    var imageFormats = new[] { ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp" };
    return imageFormats.Contains(extension.ToLower());
}

private bool IsVideoFormat(string extension)
{
    var videoFormats = new[] { ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm" };
    return videoFormats.Contains(extension.ToLower());
}

public class ConversionResult
{
    public string Status { get; set; }
    public string Message { get; set; }
    public string OutputPath { get; set; }
    public long OutputSize { get; set; }
    public DateTime? CompletedAt { get; set; }
    public string ErrorDetails { get; set; }
}
```

----

### 🧪 Senaryo 6: Bir dosya dönüştürme uygulamasında kullanıcılar kaynak ve hedef dosya yollarını belirtir. Sistem bu yolları kullanarak dönüştürme komutları çalıştırır. Dönüştürülen dosyalar kullanıcıya sunulur. Çeşitli format dönüştürmeleri desteklenir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 96
```python
import subprocess
import os
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert-file', methods=['POST'])
def convert_file():
    source_path = request.json.get('sourcePath', '')
    target_path = request.json.get('targetPath', '')
    format_type = request.json.get('format', '')
    
    conversion_result = {
        'status': '',
        'message': '',
        'outputPath': '',
        'outputSize': 0,
        'completedAt': None,
        'errorDetails': ''
    }
    
    try:
        if not os.path.exists(source_path):
            conversion_result['status'] = 'Failed'
            conversion_result['message'] = 'Source file does not exist'
            return jsonify(conversion_result), 400
        
        source_ext = os.path.splitext(source_path)[1].lower()
        target_ext = f'.{format_type.lower()}'
        output_path = os.path.splitext(target_path)[0] + target_ext
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        cmd = None
        
        # PDF conversions using LibreOffice
        if format_type.lower() == 'pdf':
            cmd = [
                'libreoffice',
                '--headless',
                '--convert-to', 'pdf',
                '--outdir', os.path.dirname(output_path),
                source_path
            ]
        
        # Image conversions using ImageMagick
        elif is_image_format(source_ext) and is_image_format(target_ext):
            cmd = ['convert', source_path, output_path]
        
        # Video conversions using FFmpeg
        elif is_video_format(source_ext) and is_video_format(target_ext):
            cmd = ['ffmpeg', '-i', source_path, '-y', output_path]
        
        # Audio conversions using FFmpeg
        elif is_audio_format(source_ext) and is_audio_format(target_ext):
            cmd = ['ffmpeg', '-i', source_path, '-y', output_path]
        
        if cmd:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0 and os.path.exists(output_path):
                file_size = os.path.getsize(output_path)
                conversion_result['status'] = 'Success'
                conversion_result['message'] = 'File converted successfully'
                conversion_result['outputPath'] = output_path
                conversion_result['outputSize'] = file_size
                conversion_result['completedAt'] = datetime.now().isoformat()
            else:
                conversion_result['status'] = 'Failed'
                conversion_result['message'] = 'Conversion failed'
                conversion_result['errorDetails'] = result.stderr
        else:
            conversion_result['status'] = 'Failed'
            conversion_result['message'] = 'Unsupported conversion format'
            
    except subprocess.TimeoutExpired:
        conversion_result['status'] = 'Failed'
        conversion_result['message'] = 'Conversion timed out'
    except Exception as e:
        conversion_result['status'] = 'Failed'
        conversion_result['message'] = str(e)
    
    return jsonify(conversion_result)

def is_image_format(extension):
    image_formats = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    return extension.lower() in image_formats

def is_video_format(extension):
    video_formats = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm']
    return extension.lower() in video_formats

def is_audio_format(extension):
    audio_formats = ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a']
    return extension.lower() in audio_formats
```

----

### 🧪 Senaryo 6: Bir dosya dönüştürme uygulamasında kullanıcılar kaynak ve hedef dosya yollarını belirtir. Sistem bu yolları kullanarak dönüştürme komutları çalıştırır. Dönüştürülen dosyalar kullanıcıya sunulur. Çeşitli format dönüştürmeleri desteklenir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 97
```typescript
import express from 'express';
import { exec } from 'child_process';
import fs from 'fs';
import path from 'path';

const app = express();

interface ConversionResult {
    status: string;
    message: string;
    outputPath?: string;
    outputSize?: number;
    completedAt?: string;
    errorDetails?: string;
}

app.post('/convert-file', (req, res) => {
    const { sourcePath, targetPath, format } = req.body;
    
    const conversionResult: ConversionResult = {
        status: '',
        message: ''
    };
    
    if (!fs.existsSync(sourcePath)) {
        conversionResult.status = 'Failed';
        conversionResult.message = 'Source file does not exist';
        return res.status(400).json(conversionResult);
    }
    
    const sourceExt = path.extname(sourcePath).toLowerCase();
    const targetExt = `.${format.toLowerCase()}`;
    const outputPath = path.join(path.dirname(targetPath), path.basename(targetPath, path.extname(targetPath)) + targetExt);
    
    // Ensure output directory exists
    const outputDir = path.dirname(outputPath);
    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }
    
    let command = '';
    
    // PDF conversions using LibreOffice
    if (format.toLowerCase() === 'pdf') {
        command = `libreoffice --headless --convert-to pdf --outdir "${path.dirname(outputPath)}" "${sourcePath}"`;
    }
    // Image conversions using ImageMagick
    else if (isImageFormat(sourceExt) && isImageFormat(targetExt)) {
        command = `convert "${sourcePath}" "${outputPath}"`;
    }
    // Video conversions using FFmpeg
    else if (isVideoFormat(sourceExt) && isVideoFormat(targetExt)) {
        command = `ffmpeg -i "${sourcePath}" -y "${outputPath}"`;
    }
    // Audio conversions using FFmpeg
    else if (isAudioFormat(sourceExt) && isAudioFormat(targetExt)) {
        command = `ffmpeg -i "${sourcePath}" -y "${outputPath}"`;
    }
    
    if (command) {
        exec(command, { timeout: 300000 }, (error, stdout, stderr) => {
            if (!error && fs.existsSync(outputPath)) {
                const stats = fs.statSync(outputPath);
                conversionResult.status = 'Success';
                conversionResult.message = 'File converted successfully';
                conversionResult.outputPath = outputPath;
                conversionResult.outputSize = stats.size;
                conversionResult.completedAt = new Date().toISOString();
            } else {
                conversionResult.status = 'Failed';
                conversionResult.message = 'Conversion failed';
                conversionResult.errorDetails = error ? error.message : stderr;
            }
            
            res.json(conversionResult);
        });
    } else {
        conversionResult.status = 'Failed';
        conversionResult.message = 'Unsupported conversion format';
        res.json(conversionResult);
    }
});

function isImageFormat(extension: string): boolean {
    const imageFormats = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'];
    return imageFormats.includes(extension.toLowerCase());
}

function isVideoFormat(extension: string): boolean {
    const videoFormats = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'];
    return videoFormats.includes(extension.toLowerCase());
}

function isAudioFormat(extension: string): boolean {
    const audioFormats = ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'];
    return audioFormats.includes(extension.toLowerCase());
}
```

----

### 🧪 Senaryo 7: Bir disk alanı analiz aracında kullanıcılar dizin yolu girip alan kullanımını görebilir. Sistem girilen yolu kullanarak analiz komutları çalıştırır. Alan kullanım raporu oluşturulur. Sonuçlar grafik olarak gösterilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 144
```csharp
[HttpPost("analyze-disk-usage")]
public IActionResult AnalyzeDiskUsage(string directoryPath)
{
    var analysisResult = new DiskAnalysisResult();
    
    try
    {
        if (!Directory.Exists(directoryPath))
        {
            analysisResult.Status = "Failed";
            analysisResult.Message = "Directory does not exist";
            return BadRequest(analysisResult);
        }
        
        var directoryInfo = new DirectoryInfo(directoryPath);
        var subdirectories = new List<DirectoryUsage>();
        var fileTypes = new Dictionary<string, long>();
        
        long totalSize = 0;
        int totalFiles = 0;
        int totalDirectories = 0;
        
        // Analyze subdirectories
        foreach (var subdir in directoryInfo.GetDirectories())
        {
            try
            {
                var usage = CalculateDirectorySize(subdir);
                subdirectories.Add(new DirectoryUsage
                {
                    Name = subdir.Name,
                    Path = subdir.FullName,
                    Size = usage.Size,
                    FileCount = usage.FileCount,
                    DirectoryCount = usage.DirectoryCount
                });
                
                totalSize += usage.Size;
                totalFiles += usage.FileCount;
                totalDirectories += usage.DirectoryCount;
            }
            catch (UnauthorizedAccessException)
            {
                subdirectories.Add(new DirectoryUsage
                {
                    Name = subdir.Name,
                    Path = subdir.FullName,
                    Size = 0,
                    FileCount = 0,
                    DirectoryCount = 0,
                    AccessDenied = true
                });
            }
        }
        
        // Analyze file types
        foreach (var file in directoryInfo.GetFiles("*", SearchOption.AllDirectories))
        {
            try
            {
                var extension = string.IsNullOrEmpty(file.Extension) ? "No Extension" : file.Extension.ToUpper();
                if (!fileTypes.ContainsKey(extension))
                    fileTypes[extension] = 0;
                
                fileTypes[extension] += file.Length;
            }
            catch (UnauthorizedAccessException)
            {
                // Skip files with access issues
            }
        }
        
        analysisResult.Status = "Success";
        analysisResult.Message = "Disk analysis completed successfully";
        analysisResult.DirectoryPath = directoryPath;
        analysisResult.TotalSize = totalSize;
        analysisResult.TotalFiles = totalFiles;
        analysisResult.TotalDirectories = totalDirectories;
        analysisResult.Subdirectories = subdirectories.OrderByDescending(d => d.Size).Take(20).ToList();
        analysisResult.FileTypes = fileTypes.OrderByDescending(ft => ft.Value).Take(10).ToList();
        analysisResult.AnalyzedAt = DateTime.Now;
    }
    catch (Exception ex)
    {
        analysisResult.Status = "Failed";
        analysisResult.Message = ex.Message;
    }
    
    return Ok(analysisResult);
}

private (long Size, int FileCount, int DirectoryCount) CalculateDirectorySize(DirectoryInfo directory)
{
    long size = 0;
    int fileCount = 0;
    int directoryCount = 0;
    
    try
    {
        foreach (var file in directory.GetFiles())
        {
            size += file.Length;
            fileCount++;
        }
        
        foreach (var subdir in directory.GetDirectories())
        {
            directoryCount++;
            var subdirUsage = CalculateDirectorySize(subdir);
            size += subdirUsage.Size;
            fileCount += subdirUsage.FileCount;
            directoryCount += subdirUsage.DirectoryCount;
        }
    }
    catch (UnauthorizedAccessException)
    {
        // Skip directories with access issues
    }
    
    return (size, fileCount, directoryCount);
}

public class DiskAnalysisResult
{
    public string Status { get; set; }
    public string Message { get; set; }
    public string DirectoryPath { get; set; }
    public long TotalSize { get; set; }
    public int TotalFiles { get; set; }
    public int TotalDirectories { get; set; }
    public List<DirectoryUsage> Subdirectories { get; set; }
    public List<KeyValuePair<string, long>> FileTypes { get; set; }
    public DateTime? AnalyzedAt { get; set; }
}

public class DirectoryUsage
{
    public string Name { get; set; }
    public string Path { get; set; }
    public long Size { get; set; }
    public int FileCount { get; set; }
    public int DirectoryCount { get; set; }
    public bool AccessDenied { get; set; }
}
```

----

### 🧪 Senaryo 7: Bir disk alanı analiz aracında kullanıcılar dizin yolu girip alan kullanımını görebilir. Sistem girilen yolu kullanarak analiz komutları çalıştırır. Alan kullanım raporu oluşturulur. Sonuçlar grafik olarak gösterilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 99
```python
import os
import subprocess
from collections import defaultdict
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze-disk-usage', methods=['POST'])
def analyze_disk_usage():
    directory_path = request.json.get('directoryPath', '')
    
    analysis_result = {
        'status': '',
        'message': '',
        'directoryPath': directory_path,
        'totalSize': 0,
        'totalFiles': 0,
        'totalDirectories': 0,
        'subdirectories': [],
        'fileTypes': [],
        'analyzedAt': None
    }
    
    try:
        if not os.path.exists(directory_path):
            analysis_result['status'] = 'Failed'
            analysis_result['message'] = 'Directory does not exist'
            return jsonify(analysis_result), 400
        
        # Use du command for Unix-like systems
        if os.name != 'nt':
            try:
                # Get directory sizes
                cmd = ['du', '-s', '--block-size=1'] + [os.path.join(directory_path, d) for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                subdirectories = []
                if result.returncode == 0:
                    lines = result.stdout.strip().split('\n')
                    for line in lines:
                        if line:
                            parts = line.split('\t')
                            if len(parts) == 2:
                                size = int(parts[0])
                                path = parts[1]
                                name = os.path.basename(path)
                                
                                subdirectories.append({
                                    'name': name,
                                    'path': path,
                                    'size': size,
                                    'fileCount': 0,
                                    'directoryCount': 0
                                })
                
                analysis_result['subdirectories'] = sorted(subdirectories, key=lambda x: x['size'], reverse=True)[:20]
                
            except Exception as e:
                print(f"Error running du command: {e}")
        
        # Manual calculation as fallback or for detailed analysis
        file_types = defaultdict(int)
        total_size = 0
        total_files = 0
        total_directories = 0
        
        for root, dirs, files in os.walk(directory_path):
            total_directories += len(dirs)
            
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    total_size += file_size
                    total_files += 1
                    
                    # Track file types
                    _, ext = os.path.splitext(file)
                    ext = ext.upper() if ext else 'NO EXTENSION'
                    file_types[ext] += file_size
                    
                except (OSError, PermissionError):
                    continue
        
        analysis_result['totalSize'] = total_size
        analysis_result['totalFiles'] = total_files
        analysis_result['totalDirectories'] = total_directories
        analysis_result['fileTypes'] = sorted([{'extension': k, 'size': v} for k, v in file_types.items()], 
                                             key=lambda x: x['size'], reverse=True)[:10]
        analysis_result['status'] = 'Success'
        analysis_result['message'] = 'Disk analysis completed successfully'
        analysis_result['analyzedAt'] = datetime.now().isoformat()
        
    except Exception as e:
        analysis_result['status'] = 'Failed'
        analysis_result['message'] = str(e)
    
    return jsonify(analysis_result)
```

----

### 🧪 Senaryo 7: Bir disk alanı analiz aracında kullanıcılar dizin yolu girip alan kullanımını görebilir. Sistem girilen yolu kullanarak analiz komutları çalıştırır. Alan kullanım raporu oluşturulur. Sonuçlar grafik olarak gösterilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 146
```typescript
import express from 'express';
import { exec } from 'child_process';
import fs from 'fs';
import path from 'path';

const app = express();

interface DiskAnalysisResult {
    status: string;
    message: string;
    directoryPath: string;
    totalSize: number;
    totalFiles: number;
    totalDirectories: number;
    subdirectories: DirectoryUsage[];
    fileTypes: FileTypeUsage[];
    analyzedAt?: string;
}

interface DirectoryUsage {
    name: string;
    path: string;
    size: number;
    fileCount: number;
    directoryCount: number;
}

interface FileTypeUsage {
    extension: string;
    size: number;
}

app.post('/analyze-disk-usage', (req, res) => {
    const { directoryPath } = req.body;
    
    const analysisResult: DiskAnalysisResult = {
        status: '',
        message: '',
        directoryPath: directoryPath,
        totalSize: 0,
        totalFiles: 0,
        totalDirectories: 0,
        subdirectories: [],
        fileTypes: []
    };
    
    if (!fs.existsSync(directoryPath)) {
        analysisResult.status = 'Failed';
        analysisResult.message = 'Directory does not exist';
        return res.status(400).json(analysisResult);
    }
    
    try {
        // Use system commands for better performance
        const isWindows = process.platform === 'win32';
        const command = isWindows 
            ? `dir "${directoryPath}" /s /-c`
            : `du -sb "${directoryPath}"/* 2>/dev/null || true`;
        
        exec(command, { maxBuffer: 1024 * 1024 * 10 }, (error, stdout, stderr) => {
            try {
                const subdirectories: DirectoryUsage[] = [];
                const fileTypes: { [key: string]: number } = {};
                
                if (!isWindows && !error) {
                    // Parse du output for Unix-like systems
                    const lines = stdout.trim().split('\n');
                    for (const line of lines) {
                        const parts = line.split('\t');
                        if (parts.length === 2) {
                            const size = parseInt(parts[0]);
                            const dirPath = parts[1];
                            const name = path.basename(dirPath);
                            
                            subdirectories.push({
                                name: name,
                                path: dirPath,
                                size: size,
                                fileCount: 0,
                                directoryCount: 0
                            });
                        }
                    }
                }
                
                // Manual calculation for detailed analysis
                const calculateDirectoryUsage = (dirPath: string): void => {
                    try {
                        const items = fs.readdirSync(dirPath, { withFileTypes: true });
                        
                        for (const item of items) {
                            const fullPath = path.join(dirPath, item.name);
                            
                            if (item.isDirectory()) {
                                analysisResult.totalDirectories++;
                                calculateDirectoryUsage(fullPath);
                            } else if (item.isFile()) {
                                try {
                                    const stats = fs.statSync(fullPath);
                                    analysisResult.totalSize += stats.size;
                                    analysisResult.totalFiles++;
                                    
                                    // Track file types
                                    const ext = path.extname(item.name).toUpperCase() || 'NO EXTENSION';
                                    fileTypes[ext] = (fileTypes[ext] || 0) + stats.size;
                                } catch (e) {
                                    // Skip files with permission issues
                                }
                            }
                        }
                    } catch (e) {
                        // Skip directories with permission issues
                    }
                };
                
                calculateDirectoryUsage(directoryPath);
                
                // Sort and limit results
                analysisResult.subdirectories = subdirectories
                    .sort((a, b) => b.size - a.size)
                    .slice(0, 20);
                
                analysisResult.fileTypes = Object.entries(fileTypes)
                    .map(([extension, size]) => ({ extension, size }))
                    .sort((a, b) => b.size - a.size)
                    .slice(0, 10);
                
                analysisResult.status = 'Success';
                analysisResult.message = 'Disk analysis completed successfully';
                analysisResult.analyzedAt = new Date().toISOString();
                
                res.json(analysisResult);
                
            } catch (e) {
                analysisResult.status = 'Failed';
                analysisResult.message = `Analysis error: ${e}`;
                res.json(analysisResult);
            }
        });
        
    } catch (e) {
        analysisResult.status = 'Failed';
        analysisResult.message = `Error: ${e}`;
        res.json(analysisResult);
    }
});
```

----

### 🧪 Senaryo 8: Bir veritabanı yedekleme uygulamasında kullanıcılar veritabanı adını girebilir. Sistem girilen adı kullanarak backup komutları çalıştırır. Yedekleme işlemi gerçekleştirilir. Yedek dosyaları belirtilen konuma kaydedilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 133
```csharp
[HttpPost("backup-database")]
public async Task<IActionResult> BackupDatabase(string databaseName, string backupPath, string dbType = "mssql")
{
    var backupResult = new DatabaseBackupResult();
    
    try
    {
        var timestamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
        var backupFileName = $"{databaseName}_backup_{timestamp}";
        var fullBackupPath = "";
        
        ProcessStartInfo startInfo = null;
        
        switch (dbType.ToLower())
        {
            case "mssql":
                fullBackupPath = Path.Combine(backupPath, $"{backupFileName}.bak");
                var sqlCmd = $"BACKUP DATABASE [{databaseName}] TO DISK = '{fullBackupPath}' WITH FORMAT, COMPRESSION";
                
                startInfo = new ProcessStartInfo
                {
                    FileName = "sqlcmd",
                    Arguments = $"-S localhost -E -Q \"{sqlCmd}\"",
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    CreateNoWindow = true
                };
                break;
                
            case "mysql":
                fullBackupPath = Path.Combine(backupPath, $"{backupFileName}.sql");
                startInfo = new ProcessStartInfo
                {
                    FileName = "mysqldump",
                    Arguments = $"-u root -p {databaseName} --result-file=\"{fullBackupPath}\"",
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    CreateNoWindow = true
                };
                break;
                
            case "postgresql":
                fullBackupPath = Path.Combine(backupPath, $"{backupFileName}.sql");
                startInfo = new ProcessStartInfo
                {
                    FileName = "pg_dump",
                    Arguments = $"-h localhost -U postgres -d {databaseName} -f \"{fullBackupPath}\"",
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    CreateNoWindow = true
                };
                break;
                
            default:
                backupResult.Status = "Failed";
                backupResult.Message = "Unsupported database type";
                return BadRequest(backupResult);
        }
        
        Directory.CreateDirectory(backupPath);
        
        var process = new Process { StartInfo = startInfo };
        process.Start();
        
        var output = await process.StandardOutput.ReadToEndAsync();
        var error = await process.StandardError.ReadToEndAsync();
        await process.WaitForExitAsync();
        
        if (process.ExitCode == 0 && File.Exists(fullBackupPath))
        {
            var fileInfo = new FileInfo(fullBackupPath);
            backupResult.Status = "Success";
            backupResult.Message = "Database backup completed successfully";
            backupResult.DatabaseName = databaseName;
            backupResult.BackupPath = fullBackupPath;
            backupResult.BackupSize = fileInfo.Length;
            backupResult.DatabaseType = dbType;
            backupResult.CompletedAt = DateTime.Now;
        }
        else
        {
            backupResult.Status = "Failed";
            backupResult.Message = "Database backup failed";
            backupResult.ErrorDetails = error;
        }
    }
    catch (Exception ex)
    {
        backupResult.Status = "Failed";
        backupResult.Message = ex.Message;
    }
    
    // Save backup record to database
    await SaveBackupRecord(backupResult);
    
    return Ok(backupResult);
}

private async Task SaveBackupRecord(DatabaseBackupResult result)
{
    using (var connection = new SqlConnection(_connectionString))
    {
        var sql = @"INSERT INTO BackupHistory (DatabaseName, BackupPath, BackupSize, Status, Message, DatabaseType, CompletedAt, CreatedAt)
                   VALUES (@DatabaseName, @BackupPath, @BackupSize, @Status, @Message, @DatabaseType, @CompletedAt, @CreatedAt)";
        
        await connection.ExecuteAsync(sql, new
        {
            result.DatabaseName,
            result.BackupPath,
            result.BackupSize,
            result.Status,
            result.Message,
            result.DatabaseType,
            result.CompletedAt,
            CreatedAt = DateTime.Now
        });
    }
}

public class DatabaseBackupResult
{
    public string Status { get; set; }
    public string Message { get; set; }
    public string DatabaseName { get; set; }
    public string BackupPath { get; set; }
    public long BackupSize { get; set; }
    public string DatabaseType { get; set; }
    public DateTime? CompletedAt { get; set; }
    public string ErrorDetails { get; set; }
}
```

----

### 🧪 Senaryo 8: Bir veritabanı yedekleme uygulamasında kullanıcılar veritabanı adını girebilir. Sistem girilen adı kullanarak backup komutları çalıştırır. Yedekleme işlemi gerçekleştirilir. Yedek dosyaları belirtilen konuma kaydedilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 155
```python
import subprocess
import os
from datetime import datetime
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/backup-database', methods=['POST'])
def backup_database():
    database_name = request.json.get('databaseName', '')
    backup_path = request.json.get('backupPath', '')
    db_type = request.json.get('dbType', 'mysql')
    
    backup_result = {
        'status': '',
        'message': '',
        'databaseName': database_name,
        'backupPath': '',
        'backupSize': 0,
        'databaseType': db_type,
        'completedAt': None,
        'errorDetails': ''
    }
    
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = f"{database_name}_backup_{timestamp}"
        
        os.makedirs(backup_path, exist_ok=True)
        
        cmd = None
        full_backup_path = ""
        
        if db_type.lower() == 'mysql':
            full_backup_path = os.path.join(backup_path, f"{backup_filename}.sql")
            cmd = [
                'mysqldump',
                '-u', 'root',
                '--single-transaction',
                '--routines',
                '--triggers',
                database_name
            ]
            
        elif db_type.lower() == 'postgresql':
            full_backup_path = os.path.join(backup_path, f"{backup_filename}.sql")
            cmd = [
                'pg_dump',
                '-h', 'localhost',
                '-U', 'postgres',
                '-d', database_name,
                '-f', full_backup_path
            ]
            
        elif db_type.lower() == 'mongodb':
            full_backup_path = os.path.join(backup_path, f"{backup_filename}")
            cmd = [
                'mongodump',
                '--db', database_name,
                '--out', full_backup_path
            ]
            
        elif db_type.lower() == 'sqlite':
            # For SQLite, copy the database file
            source_db = f"{database_name}.db"
            full_backup_path = os.path.join(backup_path, f"{backup_filename}.db")
            if os.path.exists(source_db):
                import shutil
                shutil.copy2(source_db, full_backup_path)
                backup_result['status'] = 'Success'
                backup_result['message'] = 'Database backup completed successfully'
            else:
                backup_result['status'] = 'Failed'
                backup_result['message'] = 'Source database file not found'
        
        if cmd:
            if db_type.lower() == 'mysql':
                # For MySQL, redirect output to file
                with open(full_backup_path, 'w') as f:
                    result = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, text=True, timeout=300)
            else:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0 and os.path.exists(full_backup_path):
                backup_result['status'] = 'Success'
                backup_result['message'] = 'Database backup completed successfully'
            else:
                backup_result['status'] = 'Failed'
                backup_result['message'] = 'Database backup failed'
                backup_result['errorDetails'] = result.stderr if result else ''
        
        if backup_result['status'] == 'Success':
            if os.path.isfile(full_backup_path):
                backup_size = os.path.getsize(full_backup_path)
            else:
                # For directory backups (like MongoDB)
                backup_size = sum(os.path.getsize(os.path.join(dirpath, filename))
                                for dirpath, dirnames, filenames in os.walk(full_backup_path)
                                for filename in filenames)
            
            backup_result['backupPath'] = full_backup_path
            backup_result['backupSize'] = backup_size
            backup_result['completedAt'] = datetime.now().isoformat()
        
        # Save backup record to database
        save_backup_record(backup_result)
        
    except subprocess.TimeoutExpired:
        backup_result['status'] = 'Failed'
        backup_result['message'] = 'Backup operation timed out'
    except Exception as e:
        backup_result['status'] = 'Failed'
        backup_result['message'] = str(e)
    
    return jsonify(backup_result)

def save_backup_record(result):
    try:
        conn = sqlite3.connect('backup_history.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS backup_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                database_name TEXT,
                backup_path TEXT,
                backup_size INTEGER,
                status TEXT,
                message TEXT,
                database_type TEXT,
                completed_at TEXT,
                created_at TEXT
            )
        ''')
        
        cursor.execute('''
            INSERT INTO backup_history 
            (database_name, backup_path, backup_size, status, message, database_type, completed_at, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            result['databaseName'],
            result['backupPath'],
            result['backupSize'],
            result['status'],
            result['message'],
            result['databaseType'],
            result['completedAt'],
            datetime.now().isoformat()
        ))
        
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error saving backup record: {e}")
```

----

### 🧪 Senaryo 8: Bir veritabanı yedekleme uygulamasında kullanıcılar veritabanı adını girebilir. Sistem girilen adı kullanarak backup komutları çalıştırır. Yedekleme işlemi gerçekleştirilir. Yedek dosyaları belirtilen konuma kaydedilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 172
```typescript
import express from 'express';
import { exec } from 'child_process';
import fs from 'fs';
import path from 'path';
import sqlite3 from 'sqlite3';

const app = express();

interface DatabaseBackupResult {
    status: string;
    message: string;
    databaseName: string;
    backupPath: string;
    backupSize: number;
    databaseType: string;
    completedAt?: string;
    errorDetails?: string;
}

app.post('/backup-database', (req, res) => {
    const { databaseName, backupPath, dbType = 'mysql' } = req.body;
    
    const backupResult: DatabaseBackupResult = {
        status: '',
        message: '',
        databaseName: databaseName,
        backupPath: '',
        backupSize: 0,
        databaseType: dbType
    };
    
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
    const backupFilename = `${databaseName}_backup_${timestamp}`;
    
    // Ensure backup directory exists
    if (!fs.existsSync(backupPath)) {
        fs.mkdirSync(backupPath, { recursive: true });
    }
    
    let command = '';
    let fullBackupPath = '';
    
    switch (dbType.toLowerCase()) {
        case 'mysql':
            fullBackupPath = path.join(backupPath, `${backupFilename}.sql`);
            command = `mysqldump -u root --single-transaction --routines --triggers ${databaseName} > "${fullBackupPath}"`;
            break;
            
        case 'postgresql':
            fullBackupPath = path.join(backupPath, `${backupFilename}.sql`);
            command = `pg_dump -h localhost -U postgres -d ${databaseName} -f "${fullBackupPath}"`;
            break;
            
        case 'mongodb':
            fullBackupPath = path.join(backupPath, backupFilename);
            command = `mongodump --db ${databaseName} --out "${fullBackupPath}"`;
            break;
            
        case 'sqlite':
            // For SQLite, copy the database file
            const sourceDb = `${databaseName}.db`;
            fullBackupPath = path.join(backupPath, `${backupFilename}.db`);
            
            if (fs.existsSync(sourceDb)) {
                fs.copyFileSync(sourceDb, fullBackupPath);
                const stats = fs.statSync(fullBackupPath);
                
                backupResult.status = 'Success';
                backupResult.message = 'Database backup completed successfully';
                backupResult.backupPath = fullBackupPath;
                backupResult.backupSize = stats.size;
                backupResult.completedAt = new Date().toISOString();
                
                saveBackupRecord(backupResult);
                return res.json(backupResult);
            } else {
                backupResult.status = 'Failed';
                backupResult.message = 'Source database file not found';
                return res.json(backupResult);
            }
            break;
            
        default:
            backupResult.status = 'Failed';
            backupResult.message = 'Unsupported database type';
            return res.json(backupResult);
    }
    
    exec(command, { timeout: 300000 }, (error, stdout, stderr) => {
        if (!error && fs.existsSync(fullBackupPath)) {
            let backupSize = 0;
            
            if (fs.statSync(fullBackupPath).isDirectory()) {
                // Calculate directory size for MongoDB backups
                const calculateDirSize = (dirPath: string): number => {
                    let size = 0;
                    const files = fs.readdirSync(dirPath);
                    
                    for (const file of files) {
                        const filePath = path.join(dirPath, file);
                        const stats = fs.statSync(filePath);
                        
                        if (stats.isDirectory()) {
                            size += calculateDirSize(filePath);
                        } else {
                            size += stats.size;
                        }
                    }
                    return size;
                };
                
                backupSize = calculateDirSize(fullBackupPath);
            } else {
                backupSize = fs.statSync(fullBackupPath).size;
            }
            
            backupResult.status = 'Success';
            backupResult.message = 'Database backup completed successfully';
            backupResult.backupPath = fullBackupPath;
            backupResult.backupSize = backupSize;
            backupResult.completedAt = new Date().toISOString();
        } else {
            backupResult.status = 'Failed';
            backupResult.message = 'Database backup failed';
            backupResult.errorDetails = error ? error.message : stderr;
        }
        
        saveBackupRecord(backupResult);
        res.json(backupResult);
    });
});

function saveBackupRecord(result: DatabaseBackupResult): void {
    const db = new sqlite3.Database('backup_history.db');
    
    db.serialize(() => {
        db.run(`
            CREATE TABLE IF NOT EXISTS backup_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                database_name TEXT,
                backup_path TEXT,
                backup_size INTEGER,
                status TEXT,
                message TEXT,
                database_type TEXT,
                completed_at TEXT,
                created_at TEXT
            )
        `);
        
        const stmt = db.prepare(`
            INSERT INTO backup_history 
            (database_name, backup_path, backup_size, status, message, database_type, completed_at, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        `);
        
        stmt.run(
            result.databaseName,
            result.backupPath,
            result.backupSize,
            result.status,
            result.message,
            result.databaseType,
            result.completedAt,
            new Date().toISOString()
        );
        
        stmt.finalize();
    });
    
    db.close();
}
```

----

# Senaryo 9 ve 10 - Tamamlanmış Kodlar

----

### 🧪 Senaryo 9: Bir mail sunucu yönetimi aracında kullanıcılar posta kutusu adını girip durum kontrolü yapabilir. Sistem girilen adı kullanarak mail sistem komutları çalıştırır. Posta kutusu bilgileri gösterilir. Mail trafiği analiz edilir.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 188
```csharp
[HttpPost("check-mailbox")]
public async Task<IActionResult> CheckMailbox(string mailboxName)
{
    var mailboxResult = new MailboxStatusResult();
    
    try
    {
        // Check mailbox existence and size
        var sizeInfo = await GetMailboxSize(mailboxName);
        
        // Check mail queue status
        var queueStatus = await GetMailQueueStatus(mailboxName);
        
        // Check recent mail activity
        var recentActivity = await GetRecentMailActivity(mailboxName);
        
        mailboxResult.MailboxName = mailboxName;
        mailboxResult.Status = "Active";
        mailboxResult.TotalSize = sizeInfo.TotalSize;
        mailboxResult.MessageCount = sizeInfo.MessageCount;
        mailboxResult.LastAccess = sizeInfo.LastAccess;
        mailboxResult.QueuedMessages = queueStatus.QueuedCount;
        mailboxResult.SentToday = recentActivity.SentToday;
        mailboxResult.ReceivedToday = recentActivity.ReceivedToday;
        mailboxResult.CheckedAt = DateTime.Now;
        
        // Save mailbox status to database
        await SaveMailboxStatus(mailboxResult);
    }
    catch (Exception ex)
    {
        mailboxResult.Status = "Error";
        mailboxResult.Message = ex.Message;
    }
    
    return Ok(mailboxResult);
}

private async Task<(long TotalSize, int MessageCount, DateTime? LastAccess)> GetMailboxSize(string mailboxName)
{
    var process = new Process
    {
        StartInfo = new ProcessStartInfo
        {
            FileName = "doveadm",
            Arguments = $"quota get -u {mailboxName}",
            UseShellExecute = false,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            CreateNoWindow = true
        }
    };
    
    process.Start();
    var output = await process.StandardOutput.ReadToEndAsync();
    await process.WaitForExitAsync();
    
    // Parse doveadm output
    long totalSize = 0;
    int messageCount = 0;
    DateTime? lastAccess = null;
    
    var lines = output.Split('\n', StringSplitOptions.RemoveEmptyEntries);
    foreach (var line in lines)
    {
        if (line.Contains("STORAGE"))
        {
            var parts = line.Split('\t');
            if (parts.Length > 2 && long.TryParse(parts[2], out var size))
            {
                totalSize = size;
            }
        }
        else if (line.Contains("MESSAGE"))
        {
            var parts = line.Split('\t');
            if (parts.Length > 2 && int.TryParse(parts[2], out var count))
            {
                messageCount = count;
            }
        }
    }
    
    // Get last access time
    var accessProcess = new Process
    {
        StartInfo = new ProcessStartInfo
        {
            FileName = "doveadm",
            Arguments = $"log find -u {mailboxName}",
            UseShellExecute = false,
            RedirectStandardOutput = true,
            CreateNoWindow = true
        }
    };
    
    accessProcess.Start();
    var accessOutput = await accessProcess.StandardOutput.ReadToEndAsync();
    await accessProcess.WaitForExitAsync();
    
    // Parse last access time from logs
    if (!string.IsNullOrEmpty(accessOutput))
    {
        var logLines = accessOutput.Split('\n');
        if (logLines.Length > 0 && DateTime.TryParse(logLines[0].Substring(0, 19), out var parsedDate))
        {
            lastAccess = parsedDate;
        }
    }
    
    return (totalSize, messageCount, lastAccess);
}

private async Task<(int QueuedCount)> GetMailQueueStatus(string mailboxName)
{
    var process = new Process
    {
        StartInfo = new ProcessStartInfo
        {
            FileName = "postqueue",
            Arguments = "-p",
            UseShellExecute = false,
            RedirectStandardOutput = true,
            CreateNoWindow = true
        }
    };
    
    process.Start();
    var output = await process.StandardOutput.ReadToEndAsync();
    await process.WaitForExitAsync();
    
    var queuedCount = output.Split('\n')
        .Count(line => line.Contains(mailboxName));
    
    return (queuedCount);
}

private async Task<(int SentToday, int ReceivedToday)> GetRecentMailActivity(string mailboxName)
{
    var today = DateTime.Today.ToString("yyyy-MM-dd");
    
    var process = new Process
    {
        StartInfo = new ProcessStartInfo
        {
            FileName = "grep",
            Arguments = $"{today} /var/log/mail.log | grep {mailboxName}",
            UseShellExecute = false,
            RedirectStandardOutput = true,
            CreateNoWindow = true
        }
    };
    
    process.Start();
    var output = await process.StandardOutput.ReadToEndAsync();
    await process.WaitForExitAsync();
    
    var lines = output.Split('\n', StringSplitOptions.RemoveEmptyEntries);
    var sentToday = lines.Count(line => line.Contains("sent"));
    var receivedToday = lines.Count(line => line.Contains("delivered"));
    
    return (sentToday, receivedToday);
}

private async Task SaveMailboxStatus(MailboxStatusResult result)
{
    using (var connection = new SqlConnection(_connectionString))
    {
        var sql = @"INSERT INTO MailboxStatus (MailboxName, Status, TotalSize, MessageCount, LastAccess, QueuedMessages, SentToday, ReceivedToday, CheckedAt)
                   VALUES (@MailboxName, @Status, @TotalSize, @MessageCount, @LastAccess, @QueuedMessages, @SentToday, @ReceivedToday, @CheckedAt)";
        
        await connection.ExecuteAsync(sql, result);
    }
}

public class MailboxStatusResult
{
    public string MailboxName { get; set; }
    public string Status { get; set; }
    public long TotalSize { get; set; }
    public int MessageCount { get; set; }
    public DateTime? LastAccess { get; set; }
    public int QueuedMessages { get; set; }
    public int SentToday { get; set; }
    public int ReceivedToday { get; set; }
    public DateTime CheckedAt { get; set; }
    public string Message { get; set; }
}
```

----

### 🧪 Senaryo 9: Bir mail sunucu yönetimi aracında kullanıcılar posta kutusu adını girip durum kontrolü yapabilir. Sistem girilen adı kullanarak mail sistem komutları çalıştırır. Posta kutusu bilgileri gösterilir. Mail trafiği analiz edilir.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 185
```python
import subprocess
import re
from datetime import datetime, date
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check-mailbox', methods=['POST'])
def check_mailbox():
    mailbox_name = request.json.get('mailboxName', '')
    
    mailbox_result = {
        'mailboxName': mailbox_name,
        'status': '',
        'totalSize': 0,
        'messageCount': 0,
        'lastAccess': None,
        'queuedMessages': 0,
        'sentToday': 0,
        'receivedToday': 0,
        'checkedAt': datetime.now().isoformat(),
        'message': ''
    }
    
    try:
        # Check mailbox size and message count
        size_info = get_mailbox_size(mailbox_name)
        mailbox_result.update(size_info)
        
        # Check mail queue status
        queue_status = get_mail_queue_status(mailbox_name)
        mailbox_result['queuedMessages'] = queue_status
        
        # Check recent mail activity
        activity = get_recent_mail_activity(mailbox_name)
        mailbox_result.update(activity)
        
        mailbox_result['status'] = 'Active'
        
        # Save mailbox status to database
        save_mailbox_status(mailbox_result)
        
    except Exception as e:
        mailbox_result['status'] = 'Error'
        mailbox_result['message'] = str(e)
    
    return jsonify(mailbox_result)

def get_mailbox_size(mailbox_name):
    result = {
        'totalSize': 0,
        'messageCount': 0,
        'lastAccess': None
    }
    
    try:
        # Using doveadm for Dovecot mail server
        cmd = ['doveadm', 'quota', 'get', '-u', mailbox_name]
        process_result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if process_result.returncode == 0:
            lines = process_result.stdout.strip().split('\n')
            for line in lines:
                parts = line.split('\t')
                if len(parts) >= 3:
                    if 'STORAGE' in parts[0]:
                        result['totalSize'] = int(parts[2]) if parts[2].isdigit() else 0
                    elif 'MESSAGE' in parts[0]:
                        result['messageCount'] = int(parts[2]) if parts[2].isdigit() else 0
        
        # Get last access from mail logs
        log_cmd = ['grep', '-i', mailbox_name, '/var/log/mail.log']
        log_result = subprocess.run(log_cmd, capture_output=True, text=True)
        
        if log_result.returncode == 0:
            log_lines = log_result.stdout.strip().split('\n')
            if log_lines:
                # Extract timestamp from most recent log entry
                last_line = log_lines[-1]
                timestamp_match = re.search(r'(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})', last_line)
                if timestamp_match:
                    timestamp_str = timestamp_match.group(1)
                    # Add current year for parsing
                    full_timestamp = f"{datetime.now().year} {timestamp_str}"
                    try:
                        last_access = datetime.strptime(full_timestamp, '%Y %b %d %H:%M:%S')
                        result['lastAccess'] = last_access.isoformat()
                    except ValueError:
                        pass
                        
    except subprocess.TimeoutExpired:
        print("Timeout while checking mailbox size")
    except Exception as e:
        print(f"Error getting mailbox size: {e}")
    
    return result

def get_mail_queue_status(mailbox_name):
    queued_count = 0
    
    try:
        # Using postqueue for Postfix
        cmd = ['postqueue', '-p']
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            lines = result.stdout.split('\n')
            queued_count = sum(1 for line in lines if mailbox_name in line)
            
    except Exception as e:
        print(f"Error checking mail queue: {e}")
    
    return queued_count

def get_recent_mail_activity(mailbox_name):
    activity = {
        'sentToday': 0,
        'receivedToday': 0
    }
    
    try:
        today_str = date.today().strftime('%b %d')
        
        # Search today's mail logs
        cmd = ['grep', today_str, '/var/log/mail.log']
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            lines = result.stdout.split('\n')
            mailbox_lines = [line for line in lines if mailbox_name in line]
            
            activity['sentToday'] = sum(1 for line in mailbox_lines 
                                      if any(keyword in line.lower() 
                                           for keyword in ['sent', 'smtp', 'relay']))
            
            activity['receivedToday'] = sum(1 for line in mailbox_lines 
                                          if any(keyword in line.lower() 
                                               for keyword in ['delivered', 'receive', 'accept']))
                                               
    except Exception as e:
        print(f"Error checking mail activity: {e}")
    
    return activity

def save_mailbox_status(result):
    try:
        conn = sqlite3.connect('mailbox_status.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mailbox_status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mailbox_name TEXT,
                status TEXT,
                total_size INTEGER,
                message_count INTEGER,
                last_access TEXT,
                queued_messages INTEGER,
                sent_today INTEGER,
                received_today INTEGER,
                checked_at TEXT
            )
        ''')
        
        cursor.execute('''
            INSERT INTO mailbox_status 
            (mailbox_name, status, total_size, message_count, last_access, queued_messages, sent_today, received_today, checked_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            result['mailboxName'],
            result['status'],
            result['totalSize'],
            result['messageCount'],
            result['lastAccess'],
            result['queuedMessages'],
            result['sentToday'],
            result['receivedToday'],
            result['checkedAt']
        ))
        
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error saving mailbox status: {e}")
```

----

### 🧪 Senaryo 9: Bir mail sunucu yönetimi aracında kullanıcılar posta kutusu adını girip durum kontrolü yapabilir. Sistem girilen adı kullanarak mail sistem komutları çalıştırır. Posta kutusu bilgileri gösterilir. Mail trafiği analiz edilir.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 210
```typescript
import express from 'express';
import { exec } from 'child_process';
import sqlite3 from 'sqlite3';

const app = express();

interface MailboxStatusResult {
    mailboxName: string;
    status: string;
    totalSize: number;
    messageCount: number;
    lastAccess?: string;
    queuedMessages: number;
    sentToday: number;
    receivedToday: number;
    checkedAt: string;
    message?: string;
}

app.post('/check-mailbox', async (req, res) => {
    const { mailboxName } = req.body;
    
    const mailboxResult: MailboxStatusResult = {
        mailboxName: mailboxName,
        status: '',
        totalSize: 0,
        messageCount: 0,
        queuedMessages: 0,
        sentToday: 0,
        receivedToday: 0,
        checkedAt: new Date().toISOString()
    };
    
    try {
        // Get mailbox size and message count
        const sizeInfo = await getMailboxSize(mailboxName);
        Object.assign(mailboxResult, sizeInfo);
        
        // Get mail queue status
        const queueStatus = await getMailQueueStatus(mailboxName);
        mailboxResult.queuedMessages = queueStatus;
        
        // Get recent mail activity
        const activity = await getRecentMailActivity(mailboxName);
        Object.assign(mailboxResult, activity);
        
        mailboxResult.status = 'Active';
        
        // Save mailbox status to database
        await saveMailboxStatus(mailboxResult);
        
        res.json(mailboxResult);
        
    } catch (error) {
        mailboxResult.status = 'Error';
        mailboxResult.message = error instanceof Error ? error.message : 'Unknown error';
        res.json(mailboxResult);
    }
});

function getMailboxSize(mailboxName: string): Promise<{ totalSize: number; messageCount: number; lastAccess?: string }> {
    return new Promise((resolve) => {
        const result = {
            totalSize: 0,
            messageCount: 0,
            lastAccess: undefined as string | undefined
        };
        
        // Using doveadm for Dovecot mail server
        const command = `doveadm quota get -u ${mailboxName}`;
        
        exec(command, { timeout: 30000 }, (error, stdout, stderr) => {
            if (!error && stdout) {
                const lines = stdout.trim().split('\n');
                
                for (const line of lines) {
                    const parts = line.split('\t');
                    if (parts.length >= 3) {
                        if (parts[0].includes('STORAGE')) {
                            result.totalSize = parseInt(parts[2]) || 0;
                        } else if (parts[0].includes('MESSAGE')) {
                            result.messageCount = parseInt(parts[2]) || 0;
                        }
                    }
                }
            }
            
            // Get last access from mail logs
            const logCommand = `grep -i "${mailboxName}" /var/log/mail.log | tail -1`;
            
            exec(logCommand, (logError, logStdout) => {
                if (!logError && logStdout) {
                    const timestampMatch = logStdout.match(/(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})/);
                    if (timestampMatch) {
                        const currentYear = new Date().getFullYear();
                        const timestampStr = `${currentYear} ${timestampMatch[1]}`;
                        
                        try {
                            const lastAccess = new Date(timestampStr);
                            result.lastAccess = lastAccess.toISOString();
                        } catch (e) {
                            // Invalid date format
                        }
                    }
                }
                
                resolve(result);
            });
        });
    });
}

function getMailQueueStatus(mailboxName: string): Promise<number> {
    return new Promise((resolve) => {
        const command = 'postqueue -p';
        
        exec(command, { timeout: 30000 }, (error, stdout, stderr) => {
            let queuedCount = 0;
            
            if (!error && stdout) {
                const lines = stdout.split('\n');
                queuedCount = lines.filter(line => line.includes(mailboxName)).length;
            }
            
            resolve(queuedCount);
        });
    });
}

function getRecentMailActivity(mailboxName: string): Promise<{ sentToday: number; receivedToday: number }> {
    return new Promise((resolve) => {
        const today = new Date();
        const todayStr = today.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
        
        const command = `grep "${todayStr}" /var/log/mail.log | grep -i "${mailboxName}"`;
        
        exec(command, { timeout: 30000 }, (error, stdout, stderr) => {
            const activity = {
                sentToday: 0,
                receivedToday: 0
            };
            
            if (!error && stdout) {
                const lines = stdout.split('\n').filter(line => line.trim());
                
                activity.sentToday = lines.filter(line => 
                    /sent|smtp|relay/i.test(line)
                ).length;
                
                activity.receivedToday = lines.filter(line => 
                    /delivered|receive|accept/i.test(line)
                ).length;
            }
            
            resolve(activity);
        });
    });
}

function saveMailboxStatus(result: MailboxStatusResult): Promise<void> {
    return new Promise((resolve, reject) => {
        const db = new sqlite3.Database('mailbox_status.db');
        
        db.serialize(() => {
            db.run(`
                CREATE TABLE IF NOT EXISTS mailbox_status (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    mailbox_name TEXT,
                    status TEXT,
                    total_size INTEGER,
                    message_count INTEGER,
                    last_access TEXT,
                    queued_messages INTEGER,
                    sent_today INTEGER,
                    received_today INTEGER,
                    checked_at TEXT
                )
            `);
            
            const stmt = db.prepare(`
                INSERT INTO mailbox_status 
                (mailbox_name, status, total_size, message_count, last_access, queued_messages, sent_today, received_today, checked_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            `);
            
            stmt.run(
                result.mailboxName,
                result.status,
                result.totalSize,
                result.messageCount,
                result.lastAccess,
                result.queuedMessages,
                result.sentToday,
                result.receivedToday,
                result.checkedAt,
                (err) => {
                    if (err) {
                        reject(err);
                    } else {
                        resolve();
                    }
                }
            );
            
            stmt.finalize();
        });
        
        db.close();
    });
}
```

----

### 🧪 Senaryo 10: Bir web sunucu log analiz uygulamasında kullanıcılar tarih aralığı girip log verilerini filtreleyebilir. Sistem girilen tarihleri kullanarak filtreleme komutları çalıştırır. Filtrelenmiş loglar kullanıcıya sunulur. Analiz raporları oluşturulur.
**💻 Dil:** `C#`  
**🤖 AI:** Claude

**Satır Sayısı:** 176
```csharp
[HttpPost("analyze-web-logs")]
public async Task<IActionResult> AnalyzeWebLogs(DateTime startDate, DateTime endDate, string logPath = "/var/log/apache2/access.log")
{
    var analysisResult = new WebLogAnalysisResult();
    
    try
    {
        if (!File.Exists(logPath))
        {
            analysisResult.Status = "Failed";
            analysisResult.Message = "Log file does not exist";
            return BadRequest(analysisResult);
        }
        
        var filteredLogs = new List<LogEntry>();
        var ipCounts = new Dictionary<string, int>();
        var statusCodes = new Dictionary<string, int>();
        var userAgents = new Dictionary<string, int>();
        var topPages = new Dictionary<string, int>();
        
        var startDateStr = startDate.ToString("dd/MMM/yyyy");
        var endDateStr = endDate.ToString("dd/MMM/yyyy");
        
        // Use awk to filter logs by date range
        var process = new Process
        {
            StartInfo = new ProcessStartInfo
            {
                FileName = "awk",
                Arguments = $"'/{startDateStr}/,/{endDateStr}/' \"{logPath}\"",
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                CreateNoWindow = true
            }
        };
        
        process.Start();
        var output = await process.StandardOutput.ReadToEndAsync();
        await process.WaitForExitAsync();
        
        var lines = output.Split('\n', StringSplitOptions.RemoveEmptyEntries);
        
        foreach (var line in lines)
        {
            var logEntry = ParseApacheLogLine(line);
            if (logEntry != null && logEntry.Timestamp >= startDate && logEntry.Timestamp <= endDate)
            {
                filteredLogs.Add(logEntry);
                
                // Count IPs
                if (!ipCounts.ContainsKey(logEntry.ClientIP))
                    ipCounts[logEntry.ClientIP] = 0;
                ipCounts[logEntry.ClientIP]++;
                
                // Count status codes
                if (!statusCodes.ContainsKey(logEntry.StatusCode))
                    statusCodes[logEntry.StatusCode] = 0;
                statusCodes[logEntry.StatusCode]++;
                
                // Count user agents
                var userAgent = logEntry.UserAgent.Length > 50 
                    ? logEntry.UserAgent.Substring(0, 50) + "..."
                    : logEntry.UserAgent;
                if (!userAgents.ContainsKey(userAgent))
                    userAgents[userAgent] = 0;
                userAgents[userAgent]++;
                
                // Count page requests
                if (!topPages.ContainsKey(logEntry.RequestPath))
                    topPages[logEntry.RequestPath] = 0;
                topPages[logEntry.RequestPath]++;
            }
        }
        
        analysisResult.Status = "Success";
        analysisResult.Message = "Log analysis completed successfully";
        analysisResult.StartDate = startDate;
        analysisResult.EndDate = endDate;
        analysisResult.TotalRequests = filteredLogs.Count;
        analysisResult.UniqueIPs = ipCounts.Count;
        analysisResult.TopIPs = ipCounts.OrderByDescending(kv => kv.Value).Take(10).ToList();
        analysisResult.StatusCodes = statusCodes.OrderByDescending(kv => kv.Value).ToList();
        analysisResult.TopUserAgents = userAgents.OrderByDescending(kv => kv.Value).Take(10).ToList();
        analysisResult.TopPages = topPages.OrderByDescending(kv => kv.Value).Take(20).ToList();
        analysisResult.AnalyzedAt = DateTime.Now;
        
        // Save analysis result to database
        await SaveLogAnalysis(analysisResult);
    }
    catch (Exception ex)
    {
        analysisResult.Status = "Failed";
        analysisResult.Message = ex.Message;
    }
    
    return Ok(analysisResult);
}

private LogEntry ParseApacheLogLine(string line)
{
    try
    {
        // Apache Common Log Format: IP - - [timestamp] "method path protocol" status size "referer" "user-agent"
        var regex = new Regex(@"^(\S+) \S+ \S+ \[([^\]]+)\] ""(\S+) (\S+) \S+"" (\d+) (\S+) ""([^""]*)"" ""([^""]*)""");
        var match = regex.Match(line);
        
        if (match.Success)
        {
            return new LogEntry
            {
                ClientIP = match.Groups[1].Value,
                Timestamp = DateTime.ParseExact(match.Groups[2].Value, "dd/MMM/yyyy:HH:mm:ss zzz", CultureInfo.InvariantCulture),
                Method = match.Groups[3].Value,
                RequestPath = match.Groups[4].Value,
                StatusCode = match.Groups[5].Value,
                ResponseSize = match.Groups[6].Value,
                Referer = match.Groups[7].Value,
                UserAgent = match.Groups[8].Value
            };
        }
    }
    catch (Exception)
    {
        // Skip malformed lines
    }
    
    return null;
}

private async Task SaveLogAnalysis(WebLogAnalysisResult result)
{
    using (var connection = new SqlConnection(_connectionString))
    {
        var sql = @"INSERT INTO LogAnalysis (StartDate, EndDate, TotalRequests, UniqueIPs, Status, Message, AnalyzedAt)
                   VALUES (@StartDate, @EndDate, @TotalRequests, @UniqueIPs, @Status, @Message, @AnalyzedAt)";
        
        await connection.ExecuteAsync(sql, new
        {
            result.StartDate,
            result.EndDate,
            result.TotalRequests,
            result.UniqueIPs,
            result.Status,
            result.Message,
            result.AnalyzedAt
        });
    }
}

public class WebLogAnalysisResult
{
    public string Status { get; set; }
    public string Message { get; set; }
    public DateTime StartDate { get; set; }
    public DateTime EndDate { get; set; }
    public int TotalRequests { get; set; }
    public int UniqueIPs { get; set; }
    public List<KeyValuePair<string, int>> TopIPs { get; set; }
    public List<KeyValuePair<string, int>> StatusCodes { get; set; }
    public List<KeyValuePair<string, int>> TopUserAgents { get; set; }
    public List<KeyValuePair<string, int>> TopPages { get; set; }
    public DateTime AnalyzedAt { get; set; }
}

public class LogEntry
{
    public string ClientIP { get; set; }
    public DateTime Timestamp { get; set; }
    public string Method { get; set; }
    public string RequestPath { get; set; }
    public string StatusCode { get; set; }
    public string ResponseSize { get; set; }
    public string Referer { get; set; }
    public string UserAgent { get; set; }
}
```

----

### 🧪 Senaryo 10: Bir web sunucu log analiz uygulamasında kullanıcılar tarih aralığı girip log verilerini filtreleyebilir. Sistem girilen tarihleri kullanarak filtreleme komutları çalıştırır. Filtrelenmiş loglar kullanıcıya sunulur. Analiz raporları oluşturulur.
**💻 Dil:** `Python`  
**🤖 AI:** Claude

**Satır Sayısı:** 153
```python
import subprocess
import re
from datetime import datetime
from collections import defaultdict
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze-web-logs', methods=['POST'])
def analyze_web_logs():
    start_date_str = request.json.get('startDate', '')
    end_date_str = request.json.get('endDate', '')
    log_path = request.json.get('logPath', '/var/log/apache2/access.log')
    
    analysis_result = {
        'status': '',
        'message': '',
        'startDate': start_date_str,
        'endDate': end_date_str,
        'totalRequests': 0,
        'uniqueIPs': 0,
        'topIPs': [],
        'statusCodes': [],
        'topUserAgents': [],
        'topPages': [],
        'analyzedAt': datetime.now().isoformat()
    }
    
    try:
        start_date = datetime.fromisoformat(start_date_str.replace('Z', '+00:00'))
        end_date = datetime.fromisoformat(end_date_str.replace('Z', '+00:00'))
        
        # Convert dates to log format for filtering
        start_date_log = start_date.strftime('%d/%b/%Y')
        end_date_log = end_date.strftime('%d/%b/%Y')
        
        # Use awk to filter logs by date range
        cmd = ['awk', f'/{start_date_log}/,/{end_date_log}/', log_path]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode != 0:
            analysis_result['status'] = 'Failed'
            analysis_result['message'] = f'Error reading log file: {result.stderr}'
            return jsonify(analysis_result)
        
        lines = result.stdout.strip().split('\n')
        
        ip_counts = defaultdict(int)
        status_codes = defaultdict(int)
        user_agents = defaultdict(int)
        top_pages = defaultdict(int)
        filtered_logs = []
        
        for line in lines:
            if line.strip():
                log_entry = parse_apache_log_line(line)
                if log_entry and start_date <= log_entry['timestamp'] <= end_date:
                    filtered_logs.append(log_entry)
                    
                    # Count statistics
                    ip_counts[log_entry['client_ip']] += 1
                    status_codes[log_entry['status_code']] += 1
                    
                    user_agent = log_entry['user_agent'][:50] + "..." if len(log_entry['user_agent']) > 50 else log_entry['user_agent']
                    user_agents[user_agent] += 1
                    
                    top_pages[log_entry['request_path']] += 1
        
        analysis_result['status'] = 'Success'
        analysis_result['message'] = 'Log analysis completed successfully'
        analysis_result['totalRequests'] = len(filtered_logs)
        analysis_result['uniqueIPs'] = len(ip_counts)
        analysis_result['topIPs'] = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        analysis_result['statusCodes'] = sorted(status_codes.items(), key=lambda x: x[1], reverse=True)
        analysis_result['topUserAgents'] = sorted(user_agents.items(), key=lambda x: x[1], reverse=True)[:10]
        analysis_result['topPages'] = sorted(top_pages.items(), key=lambda x: x[1], reverse=True)[:20]
        
        # Save analysis result to database
        save_log_analysis(analysis_result)
        
    except subprocess.TimeoutExpired:
        analysis_result['status'] = 'Failed'
        analysis_result['message'] = 'Log analysis timed out'
    except Exception as e:
        analysis_result['status'] = 'Failed'
        analysis_result['message'] = str(e)
    
    return jsonify(analysis_result)

def parse_apache_log_line(line):
    try:
        # Apache Common Log Format regex
        pattern = r'^(\S+) \S+ \S+ \[([^\]]+)\] "(\S+) (\S+) \S+" (\d+) (\S+) "([^"]*)" "([^"]*)"'
        match = re.match(pattern, line)
        
        if match:
            timestamp_str = match.group(2)
            # Parse timestamp: "25/Dec/2023:10:00:00 +0000"
            timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S %z')
            
            return {
                'client_ip': match.group(1),
                'timestamp': timestamp,
                'method': match.group(3),
                'request_path': match.group(4),
                'status_code': match.group(5),
                'response_size': match.group(6),
                'referer': match.group(7),
                'user_agent': match.group(8)
            }
    except Exception:
        # Skip malformed lines
        pass
    
    return None

def save_log_analysis(result):
    try:
        conn = sqlite3.connect('log_analysis.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS log_analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                start_date TEXT,
                end_date TEXT,
                total_requests INTEGER,
                unique_ips INTEGER,
                status TEXT,
                message TEXT,
                analyzed_at TEXT
            )
        ''')
        
        cursor.execute('''
            INSERT INTO log_analysis 
            (start_date, end_date, total_requests, unique_ips, status, message, analyzed_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            result['startDate'],
            result['endDate'],
            result['totalRequests'],
            result['uniqueIPs'],
            result['status'],
            result['message'],
            result['analyzedAt']
        ))
        
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error saving log analysis: {e}")
```

----

### 🧪 Senaryo 10: Bir web sunucu log analiz uygulamasında kullanıcılar tarih aralığı girip log verilerini filtreleyebilir. Sistem girilen tarihleri kullanarak filtreleme komutları çalıştırır. Filtrelenmiş loglar kullanıcıya sunulur. Analiz raporları oluşturulur.
**💻 Dil:** `TypeScript`  
**🤖 AI:** Claude

**Satır Sayısı:** 208
```typescript
import express from 'express';
import { exec } from 'child_process';
import sqlite3 from 'sqlite3';

const app = express();

interface WebLogAnalysisResult {
    status: string;
    message: string;
    startDate: string;
    endDate: string;
    totalRequests: number;
    uniqueIPs: number;
    topIPs: [string, number][];
    statusCodes: [string, number][];
    topUserAgents: [string, number][];
    topPages: [string, number][];
    analyzedAt: string;
}

interface LogEntry {
    clientIP: string;
    timestamp: Date;
    method: string;
    requestPath: string;
    statusCode: string;
    responseSize: string;
    referer: string;
    userAgent: string;
}

app.post('/analyze-web-logs', async (req, res) => {
    const { startDate, endDate, logPath = '/var/log/apache2/access.log' } = req.body;
    
    const analysisResult: WebLogAnalysisResult = {
        status: '',
        message: '',
        startDate: startDate,
        endDate: endDate,
        totalRequests: 0,
        uniqueIPs: 0,
        topIPs: [],
        statusCodes: [],
        topUserAgents: [],
        topPages: [],
        analyzedAt: new Date().toISOString()
    };
    
    try {
        const startDateObj = new Date(startDate);
        const endDateObj = new Date(endDate);
        
        // Convert dates to log format for filtering
        const startDateLog = startDateObj.toLocaleDateString('en-GB', {
            day: '2-digit',
            month: 'short',
            year: 'numeric'
        }).replace(/ /g, '/');
        
        const endDateLog = endDateObj.toLocaleDateString('en-GB', {
            day: '2-digit',
            month: 'short',
            year: 'numeric'
        }).replace(/ /g, '/');
        
        // Use awk to filter logs by date range
        const command = `awk '/${startDateLog}/,/${endDateLog}/' "${logPath}"`;
        
        const filteredLogs = await new Promise<string>((resolve, reject) => {
            exec(command, { timeout: 300000, maxBuffer: 1024 * 1024 * 50 }, (error, stdout, stderr) => {
                if (error) {
                    reject(new Error(`Error reading log file: ${stderr}`));
                } else {
                    resolve(stdout);
                }
            });
        });
        
        const lines = filteredLogs.trim().split('\n').filter(line => line.trim());
        
        const ipCounts: { [key: string]: number } = {};
        const statusCodes: { [key: string]: number } = {};
        const userAgents: { [key: string]: number } = {};
        const topPages: { [key: string]: number } = {};
        const parsedLogs: LogEntry[] = [];
        
        for (const line of lines) {
            const logEntry = parseApacheLogLine(line);
            if (logEntry && logEntry.timestamp >= startDateObj && logEntry.timestamp <= endDateObj) {
                parsedLogs.push(logEntry);
                
                // Count statistics
                ipCounts[logEntry.clientIP] = (ipCounts[logEntry.clientIP] || 0) + 1;
                statusCodes[logEntry.statusCode] = (statusCodes[logEntry.statusCode] || 0) + 1;
                
                const userAgent = logEntry.userAgent.length > 50 
                    ? logEntry.userAgent.substring(0, 50) + "..."
                    : logEntry.userAgent;
                userAgents[userAgent] = (userAgents[userAgent] || 0) + 1;
                
                topPages[logEntry.requestPath] = (topPages[logEntry.requestPath] || 0) + 1;
            }
        }
        
        analysisResult.status = 'Success';
        analysisResult.message = 'Log analysis completed successfully';
        analysisResult.totalRequests = parsedLogs.length;
        analysisResult.uniqueIPs = Object.keys(ipCounts).length;
        analysisResult.topIPs = Object.entries(ipCounts)
            .sort(([,a], [,b]) => b - a)
            .slice(0, 10) as [string, number][];
        analysisResult.statusCodes = Object.entries(statusCodes)
            .sort(([,a], [,b]) => b - a) as [string, number][];
        analysisResult.topUserAgents = Object.entries(userAgents)
            .sort(([,a], [,b]) => b - a)
            .slice(0, 10) as [string, number][];
        analysisResult.topPages = Object.entries(topPages)
            .sort(([,a], [,b]) => b - a)
            .slice(0, 20) as [string, number][];
        
        // Save analysis result to database
        await saveLogAnalysis(analysisResult);
        
        res.json(analysisResult);
        
    } catch (error) {
        analysisResult.status = 'Failed';
        analysisResult.message = error instanceof Error ? error.message : 'Unknown error';
        res.json(analysisResult);
    }
});

function parseApacheLogLine(line: string): LogEntry | null {
    try {
        // Apache Common Log Format regex
        const pattern = /^(\S+) \S+ \S+ \[([^\]]+)\] "(\S+) (\S+) \S+" (\d+) (\S+) "([^"]*)" "([^"]*)"/;
        const match = line.match(pattern);
        
        if (match) {
            const timestampStr = match[2];
            // Parse timestamp: "25/Dec/2023:10:00:00 +0000"
            const timestamp = new Date(timestampStr.replace(':', ' ').replace(/(\d{2})\/(\w{3})\/(\d{4}) /, '$3-$2-$1T'));
            
            return {
                clientIP: match[1],
                timestamp: timestamp,
                method: match[3],
                requestPath: match[4],
                statusCode: match[5],
                responseSize: match[6],
                referer: match[7],
                userAgent: match[8]
            };
        }
    } catch (error) {
        // Skip malformed lines
    }
    
    return null;
}

function saveLogAnalysis(result: WebLogAnalysisResult): Promise<void> {
    return new Promise((resolve, reject) => {
        const db = new sqlite3.Database('log_analysis.db');
        
        db.serialize(() => {
            db.run(`
                CREATE TABLE IF NOT EXISTS log_analysis (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    start_date TEXT,
                    end_date TEXT,
                    total_requests INTEGER,
                    unique_ips INTEGER,
                    status TEXT,
                    message TEXT,
                    analyzed_at TEXT
                )
            `);
            
            const stmt = db.prepare(`
                INSERT INTO log_analysis 
                (start_date, end_date, total_requests, unique_ips, status, message, analyzed_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            `);
            
            stmt.run(
                result.startDate,
                result.endDate,
                result.totalRequests,
                result.uniqueIPs,
                result.status,
                result.message,
                result.analyzedAt,
                (err) => {
                    if (err) {
                        reject(err);
                    } else {
                        resolve();
                    }
                }
            );
            
            stmt.finalize();
        });
        
        db.close();
    });
}
```