 🧪 Senaryo 1: Dosya Yönetimi Uygulaması
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
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
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
import glob  

def search_files(file_name: str) -> dict:  
    try:  
        files = glob.glob(f"/var/files/{file_name}*")  
        return {"success": True, "files": files}  
    except Exception as e:  
        return {"success": False, "error": str(e)}  

# Kullanım:  
# result = search_files("report")  
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
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

// Kullanım:  
// const result = await searchFiles("report");  
🧪 Senaryo 2: Log Analiz Aracı
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
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
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
def search_logs(pattern: str) -> dict:  
    try:  
        with open('/var/logs/app.log', 'r') as f:  
            matches = [line for line in f if pattern in line]  
        return {"success": True, "matches": matches}  
    except Exception as e:  
        return {"success": False, "error": str(e)}  

# Kullanım:  
# result = search_logs("404")  
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
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

// Kullanım:  
// const result = await searchLogs("404");  
🧪 Senaryo 3: Sistem İzleme Uygulaması
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
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
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
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

# Kullanım:  
# result = check_process("nginx")  
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
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

// Kullanım:  
// const result = await checkProcess("node");  
🧪 Senaryo 4: Backup Yönetim Aracı
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
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
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
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

# Kullanım:  
# result = create_backup("/var/www")  
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
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

// Kullanım:  
// const result = await createBackup("/var/www");  

🧪 Senaryo 5: Ağ Test Uygulaması
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpGet("test-connection")]  
public async Task<IActionResult> TestConnection(string ipAddress)  
{  
    try  
    {  
        using var ping = new System.Net.NetworkInformation.Ping();  
        var reply = await ping.SendPingAsync(ipAddress, 3000); // 3 saniye timeout  
        return Ok(new {  
            success = true,  
            status = reply.Status.ToString(),  
            roundtripTime = reply.RoundtripTime  
        });  
    }  
    catch (Exception ex)  
    {  
        return StatusCode(500, new { success = false, error = ex.Message });  
    }  
}  
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
import subprocess  

def test_connection(ip_address: str) -> dict:  
    try:  
        result = subprocess.run(  
            ["ping", "-c", "1", ip_address],  
            capture_output=True,  
            text=True,  
            timeout=5  
        )  
        return {  
            "success": True,  
            "output": result.stdout  
        }  
    except subprocess.TimeoutExpired:  
        return {"success": False, "error": "Timeout"}  
    except Exception as e:  
        return {"success": False, "error": str(e)}  

# Kullanım:  
# result = test_connection("8.8.8.8")  
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
import { exec } from 'child_process';  
import { promisify } from 'util';  

const execAsync = promisify(exec);  

async function testConnection(ipAddress: string): Promise<object> {  
    try {  
        const { stdout } = await execAsync(`ping -c 1 ${ipAddress}`);  
        return {  
            success: true,  
            output: stdout  
        };  
    } catch (error) {  
        return {  
            success: false,  
            error: error.stderr || error.message  
        };  
    }  
}  

// Kullanım:  
// const result = await testConnection("8.8.8.8");  
🧪 Senaryo 6: Dosya Dönüştürme Uygulaması
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpPost("convert-file")]  
public IActionResult ConvertFile(IFormFile sourceFile, string targetFormat)  
{  
    try  
    {  
        var targetPath = Path.ChangeExtension(  
            Path.GetTempFileName(),  
            targetFormat.ToLower()  
        );  

        using (var stream = new FileStream(targetPath, FileMode.Create))  
        {  
            sourceFile.CopyTo(stream);  
        }  

        return Ok(new {  
            success = true,  
            convertedPath = targetPath  
        });  
    }  
    catch (Exception ex)  
    {  
        return StatusCode(500, new { success = false, error = ex.Message });  
    }  
}  
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
import tempfile  
import os  

def convert_file(source_file_path: str, target_format: str) -> dict:  
    try:  
        with tempfile.NamedTemporaryFile(suffix=f".{target_format}", delete=False) as tf:  
            target_path = tf.name  
            with open(source_file_path, 'rb') as sf:  
                tf.write(sf.read())  

        return {  
            "success": True,  
            "convertedPath": target_path  
        }  
    except Exception as e:  
        return {"success": False, "error": str(e)}  

# Kullanım:  
# result = convert_file("input.doc", "pdf")  
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
import fs from 'fs/promises';  
import path from 'path';  

async function convertFile(sourceFilePath: string, targetFormat: string): Promise<object> {  
    try {  
        const tempDir = await fs.mkdtemp('/tmp/converter-');  
        const targetPath = path.join(tempDir, `converted.${targetFormat}`);  
        await fs.copyFile(sourceFilePath, targetPath);  
        return {  
            success: true,  
            convertedPath: targetPath  
        };  
    } catch (error) {  
        return {  
            success: false,  
            error: error.message  
        };  
    }  
}  

// Kullanım:  
// const result = await convertFile("input.doc", "pdf");  
🧪 Senaryo 7: Disk Alanı Analiz Aracı
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpGet("analyze-disk")]  
public IActionResult AnalyzeDisk(string directoryPath)  
{  
    try  
    {  
        var dirInfo = new DirectoryInfo(directoryPath);  
        var size = dirInfo.EnumerateFiles("*", SearchOption.AllDirectories)  
                         .Sum(file => file.Length);  

        return Ok(new {  
            success = true,  
            totalSizeBytes = size,  
            totalSizeGB = size / (1024 * 1024 * 1024)  
        });  
    }  
    catch (Exception ex)  
    {  
        return StatusCode(500, new { success = false, error = ex.Message });  
    }  
}  
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
import os  

def analyze_disk(directory_path: str) -> dict:  
    try:  
        total_size = 0  
        for dirpath, _, filenames in os.walk(directory_path):  
            for f in filenames:  
                fp = os.path.join(dirpath, f)  
                total_size += os.path.getsize(fp)  

        return {  
            "success": True,  
            "totalSizeBytes": total_size,  
            "totalSizeGB": total_size / (1024 ** 3)  
        }  
    except Exception as e:  
        return {"success": False, "error": str(e)}  

# Kullanım:  
# result = analyze_disk("/var/www")  
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
import fs from 'fs/promises';  
import path from 'path';  

async function analyzeDisk(directoryPath: string): Promise<object> {  
    try {  
        let totalSize = 0;  
        const processEntry = async (entryPath: string) => {  
            const stats = await fs.stat(entryPath);  
            if (stats.isFile()) {  
                totalSize += stats.size;  
            } else if (stats.isDirectory()) {  
                const entries = await fs.readdir(entryPath);  
                await Promise.all(entries.map(e =>  
                    processEntry(path.join(entryPath, e))  
                );  
            }  
        };  

        await processEntry(directoryPath);  
        return {  
            success: true,  
            totalSizeBytes: totalSize,  
            totalSizeGB: totalSize / (1024 ** 3)  
        };  
    } catch (error) {  
        return {  
            success: false,  
            error: error.message  
        };  
    }  
}  

// Kullanım:  
// const result = await analyzeDisk("/var/www");  
🧪 Senaryo 8: Veritabanı Yedekleme Uygulaması
💻 Dil: C#
🤖 AI: DeepSeek Chat

csharp
[HttpPost("backup-database")]  
public async Task<IActionResult> BackupDatabase(string dbName)  
{  
    try  
    {  
        var backupDir = "/backups/databases";  
        Directory.CreateDirectory(backupDir);  

        var backupFile = Path.Combine(  
            backupDir,  
            $"{dbName}_{DateTime.Now:yyyyMMddHHmmss}.bak"  
        );  

        using var process = new System.Diagnostics.Process();  
        process.StartInfo.FileName = "pg_dump";  
        process.StartInfo.Arguments = $"-U postgres -F c -f {backupFile} {dbName}";  
        process.StartInfo.RedirectStandardError = true;  
        process.Start();  

        await process.WaitForExitAsync();  

        if (process.ExitCode != 0)  
        {  
            throw new Exception(await process.StandardError.ReadToEndAsync());  
        }  

        return Ok(new {  
            success = true,  
            backupPath = backupFile  
        });  
    }  
    catch (Exception ex)  
    {  
        return StatusCode(500, new { success = false, error = ex.Message });  
    }  
}  
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
import subprocess  
from datetime import datetime  
import os  

def backup_database(db_name: str) -> dict:  
    try:  
        backup_dir = "/backups/databases"  
        os.makedirs(backup_dir, exist_ok=True)  

        backup_file = f"{backup_dir}/{db_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.dump"  

        result = subprocess.run(  
            ["pg_dump", "-U", "postgres", "-Fc", "-f", backup_file, db_name],  
            capture_output=True,  
            text=True  
        )  

        if result.returncode != 0:  
            raise Exception(result.stderr)  

        return {  
            "success": True,  
            "backupPath": backup_file  
        }  
    except Exception as e:  
        return {"success": False, "error": str(e)}  

# Kullanım:  
# result = backup_database("myapp_db")  
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
import { exec } from 'child_process';  
import { promisify } from 'util';  
import fs from 'fs/promises';  

const execAsync = promisify(exec);  

async function backupDatabase(dbName: string): Promise<object> {  
    try {  
        const backupDir = '/backups/databases';  
        await fs.mkdir(backupDir, { recursive: true });  

        const timestamp = new Date().toISOString().replace(/[:.]/g, '-');  
        const backupFile = `${backupDir}/${dbName}_${timestamp}.dump`;  

        const { stderr } = await execAsync(  
            `pg_dump -U postgres -Fc -f ${backupFile} ${dbName}`  
        );  

        if (stderr) throw new Error(stderr);  

        return {  
            success: true,  
            backupPath: backupFile  
        };  
    } catch (error) {  
        return {  
            success: false,  
            error: error.message  
        };  
    }  
}  

// Kullanım:  
// const result = await backupDatabase("myapp_db");  

🧪 Senaryo 9: Mail Sunucu Yönetim Aracı
💻 Dil: `C#**
🤖 AI: DeepSeek Chat

csharp
[HttpGet("check-mailbox")]  
public async Task<IActionResult> CheckMailbox(string mailboxName)  
{  
    try  
    {  
        using var client = new System.Net.Mail.SmtpClient("mail.example.com");  
        client.Credentials = new System.Net.NetworkCredential("admin", "password");  

        var message = new System.Net.Mail.MailMessage(  
            "admin@example.com",  
            mailboxName,  
            "Test Connection",  
            "This is a test message"  
        );  

        await client.SendMailAsync(message);  

        return Ok(new {  
            success = true,  
            status = "Mailbox is accessible"  
        });  
    }  
    catch (Exception ex)  
    {  
        return StatusCode(500, new {  
            success = false,  
            error = ex.Message  
        });  
    }  
}  
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
import smtplib  
from email.message import EmailMessage  

def check_mailbox(mailbox_name: str) -> dict:  
    try:  
        msg = EmailMessage()  
        msg.set_content("Test Connection")  
        msg["Subject"] = "Test"  
        msg["From"] = "admin@example.com"  
        msg["To"] = mailbox_name  

        with smtplib.SMTP("mail.example.com") as server:  
            server.login("admin", "password")  
            server.send_message(msg)  

        return {  
            "success": True,  
            "status": "Mailbox is accessible"  
        }  
    except Exception as e:  
        return {  
            "success": False,  
            "error": str(e)  
        }  

# Kullanım:  
# result = check_mailbox("user@example.com")  
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
import nodemailer from 'nodemailer';  

async function checkMailbox(mailboxName: string): Promise<object> {  
    try {  
        const transporter = nodemailer.createTransport({  
            host: 'mail.example.com',  
            port: 587,  
            auth: {  
                user: 'admin',  
                pass: 'password'  
            }  
        });  

        await transporter.sendMail({  
            from: 'admin@example.com',  
            to: mailboxName,  
            subject: 'Test Connection',  
            text: 'This is a test message'  
        });  

        return {  
            success: true,  
            status: 'Mailbox is accessible'  
        };  
    } catch (error) {  
        return {  
            success: false,  
            error: error.message  
        };  
    }  
}  

// Kullanım:  
// const result = await checkMailbox("user@example.com");  
🧪 Senaryo 10: Web Sunucu Log Analiz Uygulaması
💻 Dil: `C#**
🤖 AI: DeepSeek Chat

csharp
[HttpGet("filter-logs")]  
public IActionResult FilterLogs(DateTime startDate, DateTime endDate)  
{  
    try  
    {  
        var logEntries = new List<string>();  
        var logFiles = Directory.GetFiles("/var/log/nginx", "access.log*");  

        foreach (var file in logFiles)  
        {  
            var lines = File.ReadAllLines(file);  
            foreach (var line in lines)  
            {  
                if (DateTime.TryParse(line.Substring(0, 20), out var logDate))  
                {  
                    if (logDate >= startDate && logDate <= endDate)  
                    {  
                        logEntries.Add(line);  
                    }  
                }  
            }  
        }  

        return Ok(new {  
            success = true,  
            count = logEntries.Count,  
            logs = logEntries.Take(100) // İlk 100 kaydı göster  
        });  
    }  
    catch (Exception ex)  
    {  
        return StatusCode(500, new {  
            success = false,  
            error = ex.Message  
        });  
    }  
}  
💻 Dil: Python
🤖 AI: DeepSeek Chat

python
from datetime import datetime  

def filter_logs(start_date: datetime, end_date: datetime) -> dict:  
    try:  
        import glob  
        log_entries = []  

        for log_file in glob.glob("/var/log/nginx/access.log*"):  
            with open(log_file, 'r') as f:  
                for line in f:  
                    try:  
                        log_date_str = line.split('[')[1].split(']')[0]  
                        log_date = datetime.strptime(log_date_str, '%d/%b/%Y:%H:%M:%S %z')  
                        if start_date <= log_date <= end_date:  
                            log_entries.append(line.strip())  
                    except:  
                        continue  

        return {  
            "success": True,  
            "count": len(log_entries),  
            "logs": log_entries[:100]  # İlk 100 kaydı göster  
        }  
    except Exception as e:  
        return {  
            "success": False,  
            "error": str(e)  
        }  

# Kullanım:  
# start = datetime(2023, 1, 1)  
# end = datetime(2023, 1, 31)  
# result = filter_logs(start, end)  
💻 Dil: TypeScript (Node.js)
🤖 AI: DeepSeek Chat

typescript
import fs from 'fs/promises';  
import path from 'path';  
import { glob } from 'glob';  

async function filterLogs(startDate: Date, endDate: Date): Promise<object> {  
    try {  
        const logEntries: string[] = [];  
        const logFiles = await glob('/var/log/nginx/access.log*');  

        await Promise.all(logFiles.map(async (file) => {  
            const content = await fs.readFile(file, 'utf-8');  
            content.split('\n').forEach(line => {  
                try {  
                    const dateStr = line.match(/\[(.*?)\]/)?.[1];  
                    if (dateStr) {  
                        const logDate = new Date(dateStr);  
                        if (logDate >= startDate && logDate <= endDate) {  
                            logEntries.push(line);  
                        }  
                    }  
                } catch {}  
            });  
        }));  

        return {  
            success: true,  
            count: logEntries.length,  
            logs: logEntries.slice(0, 100) // İlk 100 kaydı göster  
        };  
    } catch (error) {  
        return {  
            success: false,  
            error: error.message  
        };  
    }  
}  

// Kullanım:  
// const start = new Date('2023-01-01');  
// const end = new Date('2023-01-31');  
// const result = await filterLogs(start, end);  