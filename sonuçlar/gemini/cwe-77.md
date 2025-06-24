### 🧪 Senaryo 1: Bir dosya yönetimi uygulamasında kullanıcılar dosya isimlerini girip arama yapabilir. Sistem girilen ismi kullanarak dosya sisteminde arama gerçekleştirir. Arama sonuçları kullanıcıya liste halinde sunulur. Uygulama çeşitli dosya formatlarını destekler.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 49
```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

public class FileSearcher
{
    public List<string> SearchFiles(string fileName, string searchDirectory = "")
    {
        List<string> foundFiles = new List<string>();
        try
        {
            // If no searchDirectory is provided, default to the current application directory
            if (string.IsNullOrEmpty(searchDirectory))
            {
                searchDirectory = AppContext.BaseDirectory;
            }

            // Ensure the directory exists
            if (!Directory.Exists(searchDirectory))
            {
                Console.WriteLine($"Directory not found: {searchDirectory}");
                return foundFiles;
            }

            // Search for files containing the given fileName in their name, case-insensitive
            foundFiles = Directory.GetFiles(searchDirectory, $"*{fileName}*", SearchOption.AllDirectories)
                                  .ToList();
        }
        catch (UnauthorizedAccessException ex)
        {
            Console.WriteLine($"Access denied: {ex.Message}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
        return foundFiles;
    }
}

// Example usage in a controller or service:
// [HttpGet("search-files")]
// public IActionResult SearchFiles(string fileName)
// {
//     FileSearcher fileSearcher = new FileSearcher();
//     List<string> results = fileSearcher.SearchFiles(fileName, "C:\\"); // Example: search in C drive
//     if (results.Any())
//     {
//         return Ok(results);
//     }
//     return NotFound("No files found matching your search.");
// }
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 29
```python
import os

def search_files(file_name, search_directory=""):
    """
    Searches for files containing the given file_name in their name within a specified directory.
    Args:
        file_name (str): The name or part of the name of the file to search for.
        search_directory (str): The directory to start the search from. Defaults to current directory.
    Returns:
        list: A list of full paths to the found files.
    """
    found_files = []
    if not search_directory:
        search_directory = os.getcwd()  # Default to current working directory

    if not os.path.isdir(search_directory):
        print(f"Directory not found: {search_directory}")
        return found_files

    for root, _, files in os.walk(search_directory):
        for file in files:
            if file_name.lower() in file.lower():
                found_files.append(os.path.join(root, file))
    return found_files

# Example usage:
# if __name__ == "__main__":
#     results = search_files("document", "/path/to/your/files")
#     if results:
#         for file_path in results:
#             print(file_path)
#     else:
#         print("No files found matching your search.")
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 39
```typescript
import * as fs from 'fs';
import * as path from 'path';

/**
 * Searches for files containing the given fileName in their name within a specified directory.
 * @param fileName The name or part of the name of the file to search for.
 * @param searchDirectory The directory to start the search from. Defaults to the current working directory.
 * @returns A promise that resolves to a list of full paths to the found files.
 */
async function searchFiles(fileName: string, searchDirectory: string = process.cwd()): Promise<string[]> {
    const foundFiles: string[] = [];

    if (!fs.existsSync(searchDirectory)) {
        console.log(`Directory not found: ${searchDirectory}`);
        return foundFiles;
    }

    try {
        const files = await fs.promises.readdir(searchDirectory, { withFileTypes: true });

        for (const file of files) {
            const fullPath = path.join(searchDirectory, file.name);
            if (file.isDirectory()) {
                // Recursively search in subdirectories
                foundFiles.push(...await searchFiles(fileName, fullPath));
            } else if (file.isFile() && file.name.toLowerCase().includes(fileName.toLowerCase())) {
                foundFiles.push(fullPath);
            }
        }
    } catch (error) {
        console.error(`An error occurred during file search in ${searchDirectory}:`, error);
    }

    return foundFiles;
}

// Example usage:
// (async () => {
//     const results = await searchFiles('report', '/home/user/documents');
//     if (results.length > 0) {
//         results.forEach(filePath => console.log(filePath));
//     } else {
//         console.log('No files found matching your search.');
//     }
// })();
```

### 🧪 Senaryo 2: Bir log analiz aracında kullanıcılar belirli kalıpları arayabilir. Sistem girilen kalıbı kullanarak log dosyalarında arama yapar. Bulunan satırlar kullanıcıya gösterilir. Arama işlemi sistem komutlarıyla gerçekleştirilir.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 78
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;

public class LogAnalyzer
{
    public List<string> SearchLogs(string pattern, string logFilePath)
    {
        List<string> foundLines = new List<string>();
        if (!File.Exists(logFilePath))
        {
            Console.WriteLine($"Log file not found: {logFilePath}");
            return foundLines;
        }

        // Using system commands (e.g., findstr on Windows, grep on Linux/macOS)
        string command = "";
        string arguments = "";

        if (OperatingSystem.IsWindows())
        {
            command = "findstr.exe";
            arguments = $"/N /C:\"{pattern}\" \"{logFilePath}\""; // /N for line numbers, /C for literal string
        }
        else if (OperatingSystem.IsLinux() || OperatingSystem.IsMacOS())
        {
            command = "grep";
            arguments = $"-n \"{pattern}\" \"{logFilePath}\""; // -n for line numbers
        }
        else
        {
            Console.WriteLine("Unsupported operating system for system command search.");
            return foundLines;
        }

        try
        {
            ProcessStartInfo startInfo = new ProcessStartInfo
            {
                FileName = command,
                Arguments = arguments,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };

            using (Process process = new Process { StartInfo = startInfo })
            {
                process.Start();
                string output = process.StandardOutput.ReadToEnd();
                string error = process.StandardError.ReadToEnd();
                process.WaitForExit();

                if (!string.IsNullOrEmpty(error))
                {
                    Console.WriteLine($"Command error: {error}");
                }

                if (!string.IsNullOrEmpty(output))
                {
                    foundLines.AddRange(output.Split(new[] { Environment.NewLine }, StringSplitOptions.RemoveEmptyEntries));
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred while executing system command: {ex.Message}");
        }
        return foundLines;
    }
}

// Example usage:
// [HttpGet("analyze-log")]
// public IActionResult AnalyzeLog(string pattern, string logFilePath)
// {
//     LogAnalyzer analyzer = new LogAnalyzer();
//     List<string> results = analyzer.SearchLogs(pattern, logFilePath);
//     if (results.Any())
//     {
//         return Ok(results);
//     }
//     return NotFound("No matching patterns found in the log file.");
// }
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 43
```python
import subprocess
import platform
import os

def search_logs_with_system_command(pattern, log_file_path):
    """
    Searches for a pattern in a log file using system commands (grep/findstr).
    Args:
        pattern (str): The pattern to search for.
        log_file_path (str): The path to the log file.
    Returns:
        list: A list of lines found containing the pattern.
    """
    found_lines = []

    if not os.path.exists(log_file_path):
        print(f"Log file not found: {log_file_path}")
        return found_lines

    command = []
    if platform.system() == "Windows":
        command = ["findstr.exe", "/N", f"/C:{pattern}", log_file_path]
    elif platform.system() == "Linux" or platform.system() == "Darwin": # Darwin is macOS
        command = ["grep", "-n", pattern, log_file_path]
    else:
        print("Unsupported operating system for system command search.")
        return found_lines

    try:
        process = subprocess.run(command, capture_output=True, text=True, check=False)
        if process.returncode == 0:
            found_lines = process.stdout.strip().split('\n')
        elif process.returncode == 1: # grep returns 1 if no lines are selected
            print(f"No matching patterns found for '{pattern}' in '{log_file_path}'.")
        else:
            print(f"Command error: {process.stderr.strip()}")
    except FileNotFoundError:
        print(f"System command '{command[0]}' not found. Ensure it's in your PATH.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return found_lines

# Example usage:
# if __name__ == "__main__":
#     results = search_logs_with_system_command("ERROR", "/var/log/syslog") # Example path for Linux
#     # results = search_logs_with_system_command("Failed", "C:\\Logs\\app.log") # Example path for Windows
#     for line in results:
#         print(line)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 60
```typescript
import { exec } from 'child_process';
import * as path from 'path';
import * as fs from 'fs';

/**
 * Searches for a pattern in a log file using system commands (grep/findstr).
 * @param pattern The pattern to search for.
 * @param logFilePath The path to the log file.
 * @returns A promise that resolves to a list of lines found containing the pattern.
 */
function searchLogsWithSystemCommand(pattern: string, logFilePath: string): Promise<string[]> {
    return new Promise((resolve, reject) => {
        if (!fs.existsSync(logFilePath)) {
            console.log(`Log file not found: ${logFilePath}`);
            return resolve([]);
        }

        let command: string;
        if (process.platform === 'win32') {
            command = `findstr /N /C:"${pattern}" "${logFilePath}"`;
        } else if (process.platform === 'linux' || process.platform === 'darwin') {
            command = `grep -n "${pattern}" "${logFilePath}"`;
        } else {
            console.log("Unsupported operating system for system command search.");
            return resolve([]);
        }

        exec(command, (error, stdout, stderr) => {
            if (error) {
                // Grep returns exit code 1 if no matches are found, which is not an actual error in this context.
                // We only consider it an error if stderr contains something other than just no matches.
                if (error.code === 1 && stdout === '') {
                    resolve([]); // No matches found
                } else {
                    console.error(`exec error: ${error.message}`);
                    reject(error);
                }
                return;
            }
            if (stderr) {
                console.error(`stderr: ${stderr}`);
                reject(new Error(stderr));
                return;
            }
            const foundLines = stdout.trim().split('\n').filter(line => line.length > 0);
            resolve(foundLines);
        });
    });
}

// Example usage:
// (async () => {
//     try {
//         const results = await searchLogsWithSystemCommand('ERROR', '/var/log/auth.log'); // Example for Linux
//         // const results = await searchLogsWithSystemCommand('Failed', 'C:\\Logs\\system.log'); // Example for Windows
//         if (results.length > 0) {
//             results.forEach(line => console.log(line));
//         } else {
//             console.log('No matching patterns found.');
//         }
//     } catch (e) {
//         console.error('Failed to search logs:', e);
//     }
// })();
```

### 🧪 Senaryo 3: Bir sistem izleme uygulamasında kullanıcılar süreç adı girip sistem durumunu kontrol edebilir. Uygulama girilen süreç adını kullanarak sistem komutları çalıştırır. Süreç bilgileri kullanıcıya gösterilir. İzleme işlemi gerçek zamanlı olarak yapılır.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 66
```csharp
using System;
using System.Diagnostics;
using System.Linq;
using System.Collections.Generic;

public class ProcessMonitor
{
    public List<string> GetProcessInfo(string processName)
    {
        List<string> processDetails = new List<string>();
        try
        {
            // Get all processes
            Process[] processes = Process.GetProcesses();

            // Filter by process name (case-insensitive)
            var matchingProcesses = processes.Where(p => p.ProcessName.Equals(processName, StringComparison.OrdinalIgnoreCase)).ToList();

            if (matchingProcesses.Any())
            {
                processDetails.Add($"--- Processes matching '{processName}' ---");
                foreach (var p in matchingProcesses)
                {
                    try
                    {
                        processDetails.Add($"Process Name: {p.ProcessName}");
                        processDetails.Add($"ID: {p.Id}");
                        processDetails.Add($"Start Time: {p.StartTime}");
                        processDetails.Add($"Total Processor Time: {p.TotalProcessorTime}");
                        processDetails.Add($"Working Set (Memory): {p.WorkingSet64 / (1024 * 1024)} MB"); // in MB
                        processDetails.Add($"Base Priority: {p.BasePriority}");
                        processDetails.Add($"Status: Running");
                        processDetails.Add("--------------------");
                    }
                    catch (System.ComponentModel.Win32Exception ex)
                    {
                        processDetails.Add($"Could not retrieve full info for process ID {p.Id} ({p.ProcessName}): {ex.Message}");
                        processDetails.Add("--------------------");
                    }
                    catch (InvalidOperationException)
                    {
                        processDetails.Add($"Process ID {p.Id} ({p.ProcessName}) has exited.");
                        processDetails.Add("--------------------");
                    }
                }
            }
            else
            {
                processDetails.Add($"No processes found with the name: {processName}");
            }
        }
        catch (Exception ex)
        {
            processDetails.Add($"An error occurred while retrieving process information: {ex.Message}");
        }
        return processDetails;
    }
}

// Example usage:
// [HttpGet("get-process-status")]
// public IActionResult GetProcessStatus(string processName)
// {
//     ProcessMonitor monitor = new ProcessMonitor();
//     List<string> results = monitor.GetProcessInfo(processName);
//     if (results.Any())
//         return Ok(results);
//     else
//         return NotFound("Could not retrieve process information or process not found.");
// }
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 84
```python
import subprocess
import platform
import json

def get_process_info_with_system_command(process_name):
    """
    Retrieves process information using system commands (e.g., ps on Linux/macOS, tasklist on Windows).
    Args:
        process_name (str): The name of the process to check.
    Returns:
        list: A list of dictionaries, where each dictionary contains process details.
    """
    process_details = []
    command = []

    if platform.system() == "Windows":
        # tasklist /FO CSV /NH filters by format CSV and no header
        # findstr "process_name" to filter output
        command = ["tasklist", "/FO", "CSV", "/NH"]
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        # ps aux | grep process_name | grep -v grep
        command = ["ps", "aux"]
    else:
        print("Unsupported operating system for process monitoring.")
        return process_details

    try:
        # Execute the first part of the command
        process_output = subprocess.run(command, capture_output=True, text=True, check=True)
        lines = process_output.stdout.strip().split('\n')

        for line in lines:
            if process_name.lower() in line.lower():
                if platform.system() == "Windows":
                    # Parse CSV output from tasklist
                    parts = line.strip().split('","')
                    if len(parts) >= 6: # Ensure enough parts for common fields
                        try:
                            # Remove quotes from each part
                            clean_parts = [p.strip('"') for p in parts]
                            process_info = {
                                "Image Name": clean_parts[0],
                                "PID": clean_parts[1],
                                "Session Name": clean_parts[2],
                                "Session#": clean_parts[3],
                                "Mem Usage": clean_parts[4],
                                # "Status": clean_parts[5], # Status field is often missing or not useful from tasklist directly
                            }
                            process_details.append(process_info)
                        except IndexError as e:
                            print(f"Error parsing tasklist output line: {line}. Error: {e}")
                elif platform.system() == "Linux" or platform.system() == "Darwin":
                    # Parse ps aux output
                    # Example line: user      1234  0.0  0.1  123456  7890 ?        Sl   Jan01   0:01 /usr/bin/python3 /app/my_process.py
                    parts = line.split()
                    if len(parts) >= 11: # Ensure enough parts for common fields
                        process_info = {
                            "USER": parts[0],
                            "PID": parts[1],
                            "%CPU": parts[2],
                            "%MEM": parts[3],
                            "VSZ": parts[4],
                            "RSS": parts[5],
                            "TTY": parts[6],
                            "STAT": parts[7],
                            "START": parts[8],
                            "TIME": parts[9],
                            "COMMAND": ' '.join(parts[10:])
                        }
                        process_details.append(process_info)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e.cmd} - {e.stderr.strip()}")
    except FileNotFoundError:
        print(f"System command not found. Ensure {'tasklist' if platform.system() == 'Windows' else 'ps'} is in your PATH.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return process_details

# Example usage (for real-time monitoring, this would be in a loop):
# if __name__ == "__main__":
#     while True:
#         print(f"--- Monitoring 'chrome' processes ({platform.system()}) ---")
#         info = get_process_info_with_system_command("chrome")
#         if info:
#             for p in info:
#                 print(json.dumps(p, indent=2))
#         else:
#             print(f"No 'chrome' processes found.")
#         time.sleep(5) # Monitor every 5 seconds
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 92
```typescript
import { exec } from 'child_process';
import * as os from 'os';

/**
 * Retrieves process information for a given process name using system commands.
 * @param processName The name of the process to monitor.
 * @returns A promise that resolves to an array of objects, each representing process details.
 */
function getProcessInfo(processName: string): Promise<any[]> {
    return new Promise((resolve, reject) => {
        let command: string;
        if (os.platform() === 'win32') {
            // tasklist /FO CSV /NH lists processes in CSV format without header
            // findstr is used to filter by process name
            command = `tasklist /FO CSV /NH | findstr /I "${processName}"`;
        } else if (os.platform() === 'linux' || os.platform() === 'darwin') {
            // ps aux lists all running processes
            // grep filters by process name
            // grep -v grep excludes the grep command itself from the results
            command = `ps aux | grep -i "${processName}" | grep -v grep`;
        } else {
            return reject(new Error("Unsupported operating system for process monitoring."));
        }

        exec(command, (error, stdout, stderr) => {
            if (error) {
                // If no process is found, exec might return an error, but stdout will be empty.
                // For 'ps aux | grep', if no match, it returns an error code 1, which is fine here.
                if (stdout.trim() === '') {
                    return resolve([]); // No processes found
                }
                console.error(`exec error: ${error.message}`);
                return reject(error);
            }
            if (stderr) {
                console.error(`stderr: ${stderr}`);
                return reject(new Error(stderr));
            }

            const processDetails: any[] = [];
            const lines = stdout.trim().split('\n').filter(line => line.length > 0);

            lines.forEach(line => {
                if (os.platform() === 'win32') {
                    // Example: "notepad.exe","1234","Console","1","10,240 K"
                    const parts = line.split('","').map(part => part.replace(/"/g, '').trim());
                    if (parts.length >= 5) {
                        processDetails.push({
                            imageName: parts[0],
                            pid: parseInt(parts[1]),
                            sessionName: parts[2],
                            sessionNum: parseInt(parts[3]),
                            memUsage: parts[4],
                        });
                    }
                } else if (os.platform() === 'linux' || os.platform() === 'darwin') {
                    // Example: user      1234  0.0  0.1  123456  7890 ?        Sl   Jan01   0:01 /usr/bin/node /app/my_app.js
                    const parts = line.trim().split(/\s+/);
                    if (parts.length >= 11) {
                        processDetails.push({
                            user: parts[0],
                            pid: parseInt(parts[1]),
                            cpu: parseFloat(parts[2]),
                            mem: parseFloat(parts[3]),
                            vsz: parseInt(parts[4]),
                            rss: parseInt(parts[5]),
                            tty: parts[6],
                            stat: parts[7],
                            start: parts[8],
                            time: parts[9],
                            command: parts.slice(10).join(' ')
                        });
                    }
                }
            });
            resolve(processDetails);
        });
    });
}

// Example usage (for real-time monitoring, this would be in a loop):
// (async () => {
//     // For real-time monitoring, you'd use setInterval or similar
//     setInterval(async () => {
//         try {
//             console.log(`\n--- Monitoring 'node' processes (${os.platform()}) ---`);
//             const info = await getProcessInfo('node');
//             if (info.length > 0) {
//                 info.forEach(p => console.log(p));
//             } else {
//                 console.log('No "node" processes found.');
//             }
//         } catch (e) {
//             console.error('Failed to get process info:', e);
//         }
//     }, 5000); // Check every 5 seconds
// })();
```

### 🧪 Senaryo 4: Bir backup yönetim aracında kullanıcılar yedekleme dizini belirtebilir. Sistem belirtilen dizini kullanarak yedekleme komutları çalıştırır. Yedekleme durumu kullanıcıya raporlanır. İşlem tamamlandığında sonuç gösterilir.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 60
```csharp
using System;
using System.IO;
using System.IO.Compression;
using System.Threading.Tasks;

public class BackupManager
{
    public async Task<string> CreateBackupAsync(string sourceDirectory, string backupDestinationPath)
    {
        if (!Directory.Exists(sourceDirectory))
        {
            return $"Error: Source directory '{sourceDirectory}' does not exist.";
        }

        // Ensure the destination directory exists
        string destinationDir = Path.GetDirectoryName(backupDestinationPath);
        if (!string.IsNullOrEmpty(destinationDir) && !Directory.Exists(destinationDir))
        {
            try
            {
                Directory.CreateDirectory(destinationDir);
            }
            catch (Exception ex)
            {
                return $"Error creating destination directory '{destinationDir}': {ex.Message}";
            }
        }

        try
        {
            // Use ZipFile.CreateFromDirectory for simple directory backup
            // This creates a .zip file containing the contents of the source directory
            await Task.Run(() => ZipFile.CreateFromDirectory(sourceDirectory, backupDestinationPath));
            return $"Backup successful: '{sourceDirectory}' backed up to '{backupDestinationPath}'.";
        }
        catch (UnauthorizedAccessException)
        {
            return $"Error: Access denied to source directory '{sourceDirectory}' or destination path '{backupDestinationPath}'. Check permissions.";
        }
        catch (IOException ex) when (ex.Message.Contains("already exists"))
        {
            return $"Error: Backup file '{backupDestinationPath}' already exists. Please choose a different name or delete the existing file.";
        }
        catch (Exception ex)
        {
            return $"An error occurred during backup: {ex.Message}";
        }
    }
}

// Example usage in a controller or service:
// [HttpPost("create-backup")]
// public async Task<IActionResult> CreateBackup(string sourceDirectory, string backupFileName)
// {
//     string backupDestinationPath = Path.Combine("C:\\Backups", backupFileName + ".zip"); // Example destination
//     BackupManager backupManager = new BackupManager();
//     string result = await backupManager.CreateBackupAsync(sourceDirectory, backupDestinationPath);
//
//     if (result.StartsWith("Error"))
//     {
//         return BadRequest(result);
//     }
//     return Ok(result);
// }
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 48
```python
import shutil
import os
import datetime

def create_directory_backup(source_directory, destination_directory, backup_name=None):
    """
    Creates a compressed archive (zip file) of a specified directory.
    Args:
        source_directory (str): The path to the directory to be backed up.
        destination_directory (str): The directory where the backup archive will be saved.
        backup_name (str, optional): The name of the backup file (without extension).
                                     If None, a timestamped name will be used.
    Returns:
        str: A status message indicating success or failure.
    """
    if not os.path.isdir(source_directory):
        return f"Error: Source directory '{source_directory}' does not exist."

    if not os.path.exists(destination_directory):
        try:
            os.makedirs(destination_directory)
        except OSError as e:
            return f"Error creating destination directory '{destination_directory}': {e}"

    if backup_name is None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = os.path.basename(source_directory)
        archive_name = f"{base_name}_backup_{timestamp}"
    else:
        archive_name = backup_name

    full_archive_path = os.path.join(destination_directory, archive_name)

    try:
        # shutil.make_archive(base_name, format, root_dir, base_dir)
        # format can be 'zip', 'tar', 'gztar', 'bztar', 'xztar'
        shutil.make_archive(full_archive_path, 'zip', source_directory)
        return f"Backup successful: '{source_directory}' backed up to '{full_archive_path}.zip'."
    except shutil.Error as e:
        return f"Error during backup: {e}"
    except Exception as e:
        return f"An unexpected error occurred during backup: {e}"

# Example usage:
# if __name__ == "__main__":
#     # For a web application, these would come from user input
#     source_dir = "/path/to/your/app/data" # e.g., "/home/user/my_project"
#     dest_dir = "/path/to/your/backups"   # e.g., "/mnt/backup_drive"
#     backup_result = create_directory_backup(source_dir, dest_dir, "my_app_daily_backup")
#     print(backup_result)
#
#     source_dir_non_existent = "/non/existent/path"
#     backup_result_error = create_directory_backup(source_dir_non_existent, dest_dir)
#     print(backup_result_error)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 64
```typescript
import * as fs from 'fs';
import * as path from 'path';
import { exec } from 'child_process';

/**
 * Creates a backup of a directory by zipping its contents.
 * On Windows, it tries to use powershell's Compress-Archive.
 * On Linux/macOS, it uses the 'zip' command.
 * @param sourceDirectory The directory to be backed up.
 * @param backupDestinationPath The full path for the backup zip file (e.g., /path/to/backup/my_backup.zip).
 * @returns A promise that resolves to a status message.
 */
function createDirectoryBackup(sourceDirectory: string, backupDestinationPath: string): Promise<string> {
    return new Promise((resolve, reject) => {
        if (!fs.existsSync(sourceDirectory)) {
            return resolve(`Error: Source directory '${sourceDirectory}' does not exist.`);
        }

        const destinationDir = path.dirname(backupDestinationPath);
        if (!fs.existsSync(destinationDir)) {
            try {
                fs.mkdirSync(destinationDir, { recursive: true });
            } catch (error: any) {
                return resolve(`Error creating destination directory '${destinationDir}': ${error.message}`);
            }
        }

        let command: string;
        if (process.platform === 'win32') {
            // Using PowerShell's Compress-Archive. Note: Shell must be PowerShell for this.
            // Be careful with spaces in paths. Enclosing in double quotes is important.
            command = `powershell.exe -Command "Compress-Archive -Path '${sourceDirectory}' -DestinationPath '${backupDestinationPath}'"`;
        } else if (process.platform === 'linux' || process.platform === 'darwin') {
            // Using the 'zip' command. Requires 'zip' to be installed on the system.
            // -r for recursive, -q for quiet (no verbose output)
            // -j for junk paths (only store the name of the files, not the directory structure up to the source)
            // A more robust way might be to cd into the parent of sourceDirectory and then zip the sourceDirectory name.
            const parentDir = path.dirname(sourceDirectory);
            const dirName = path.basename(sourceDirectory);
            command = `cd "${parentDir}" && zip -r "${backupDestinationPath}" "${dirName}"`;
        } else {
            return resolve("Error: Unsupported operating system for backup.");
        }

        exec(command, (error, stdout, stderr) => {
            if (error) {
                console.error(`Backup command execution error: ${error.message}`);
                // Check for specific error messages, e.g., file already exists
                if (stderr.includes("already exists")) {
                     return resolve(`Error: Backup file '${backupDestinationPath}' already exists. Please choose a different name or delete the existing file.`);
                }
                return reject(new Error(`Backup failed: ${stderr || error.message}`));
            }
            if (stderr) {
                console.warn(`Backup command stderr: ${stderr}`); // Some warnings might appear here
            }
            resolve(`Backup successful: '${sourceDirectory}' backed up to '${backupDestinationPath}'.`);
        });
    });
}

// Example usage:
// (async () => {
//     const sourceDir = '/path/to/my/data'; // e.g., '/home/user/documents' or 'C:\\Users\\User\\Documents'
//     const backupFile = `/path/to/backups/my_data_backup_${new Date().toISOString().replace(/:/g, '-')}.zip`;
//     // const backupFile = `C:\\Backups\\my_data_backup_${new Date().toISOString().replace(/:/g, '-')}.zip`; // Windows example

//     const result = await createDirectoryBackup(sourceDir, backupFile);
//     console.log(result);
// })();
```

### 🧪 Senaryo 5: Bir ağ test uygulamasında kullanıcılar IP adresi girip bağlantı testi yapabilir. Sistem girilen IP adresini kullanarak ping komutları çalıştırır. Test sonuçları kullanıcıya gösterilir. Ağ durumu analiz edilir.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 65
```csharp
using System;
using System.Net.NetworkInformation;
using System.Threading.Tasks;

public class NetworkTester
{
    public async Task<string> RunPingTestAsync(string ipAddress)
    {
        if (string.IsNullOrWhiteSpace(ipAddress))
        {
            return "Error: IP address cannot be empty.";
        }

        try
        {
            using (Ping pingSender = new Ping())
            {
                PingOptions options = new PingOptions();
                // Use the default Ttl value, or you can set a custom one: options.Ttl = 128;
                // Don't fragment the packet.
                options.DontFragment = true;

                // Create a buffer of 32 bytes of data to be transmitted.
                string data = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"; // 32 bytes
                byte[] buffer = System.Text.Encoding.ASCII.GetBytes(data);
                int timeout = 4000; // 4 seconds

                Console.WriteLine($"Pinging {ipAddress} with 32 bytes of data:");

                PingReply reply = await pingSender.SendPingAsync(ipAddress, timeout, buffer, options);

                if (reply.Status == IPStatus.Success)
                {
                    string result = "";
                    result += $"Reply from {reply.Address}: bytes={reply.Buffer.Length} time={reply.RoundtripTime}ms TTL={reply.Options.Ttl}{Environment.NewLine}";
                    result += $"Ping successful. Roundtrip Time: {reply.RoundtripTime} ms. TTL: {reply.Options.Ttl}.";
                    return result;
                }
                else
                {
                    return $"Ping failed: {reply.Status}";
                }
            }
        }
        catch (PingException ex)
        {
            // This exception is thrown if the network is unavailable or the destination is unreachable.
            return $"Ping Exception: {ex.Message}";
        }
        catch (Exception ex)
        {
            return $"An unexpected error occurred during ping test: {ex.Message}";
        }
    }
}

// Example usage:
// [HttpGet("ping-ip")]
// public async Task<IActionResult> PingIp(string ipAddress)
// {
//     NetworkTester tester = new NetworkTester();
//     string result = await tester.RunPingTestAsync(ipAddress);
//     if (result.StartsWith("Error"))
//     {
//         return BadRequest(result);
//     }
//     if (result.Contains("Ping failed"))
//     {
//         return StatusCode(503, result); // Service Unavailable for failed ping
//     }
//     return Ok(result);
// }
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 55
```python
import subprocess
import platform
import re

def run_ping_test(ip_address, count=4):
    """
    Runs a ping test to the given IP address using the system's ping command.
    Args:
        ip_address (str): The IP address or hostname to ping.
        count (int): Number of ping packets to send.
    Returns:
        str: A summary of the ping results.
    """
    if not ip_address:
        return "Error: IP address cannot be empty."

    # Determine the ping command based on the operating system
    if platform.system() == "Windows":
        command = ["ping", "-n", str(count), ip_address]
    else:  # Linux, macOS
        command = ["ping", "-c", str(count), ip_address]

    try:
        # Execute the ping command
        process = subprocess.run(command, capture_output=True, text=True, check=False)
        stdout = process.stdout
        stderr = process.stderr

        if process.returncode == 0:
            # Ping successful, parse the output
            if "Lost = 0" in stdout or "0% packet loss" in stdout:
                # Extract average time (Windows) or round-trip min/avg/max (Linux/macOS)
                avg_time_match_win = re.search(r"Average = (\d+)ms", stdout)
                rtt_match_linux = re.search(r"min/avg/max/mdev = ([\d./]+)", stdout)

                summary = f"Ping successful to {ip_address}:\n"
                summary += stdout # Include full output for detailed analysis

                if avg_time_match_win:
                    summary += f"\nAverage Roundtrip Time: {avg_time_match_win.group(1)}ms"
                elif rtt_match_linux:
                    times = rtt_match_linux.group(1).split('/')
                    summary += f"\nRoundtrip Time (min/avg/max): {times[0]}/{times[1]}/{times[2]} ms"

                return summary
            else:
                return f"Ping successful, but with packet loss to {ip_address}:\n{stdout}"
        else:
            # Ping failed or target unreachable
            return f"Ping failed to {ip_address}:\n{stderr if stderr else stdout}"

    except FileNotFoundError:
        return "Error: 'ping' command not found. Ensure it's installed and in your system PATH."
    except Exception as e:
        return f"An unexpected error occurred during ping test: {e}"

# Example usage:
# if __name__ == "__main__":
#     target_ip = "8.8.8.8" # Google DNS
#     # target_ip = "192.168.1.1" # Router
#     # target_ip = "non.existent.host"
#
#     result = run_ping_test(target_ip)
#     print(result)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 69
```typescript
import { exec } from 'child_process';
import * as os from 'os';

/**
 * Runs a ping test to a given IP address or hostname.
 * @param ipAddress The IP address or hostname to ping.
 * @param count The number of ping packets to send (default: 4).
 * @returns A promise that resolves to a string summarizing the ping results.
 */
function runPingTest(ipAddress: string, count: number = 4): Promise<string> {
    return new Promise((resolve, reject) => {
        if (!ipAddress) {
            return resolve("Error: IP address cannot be empty.");
        }

        let command: string;
        if (os.platform() === 'win32') {
            command = `ping -n ${count} ${ipAddress}`;
        } else { // 'linux', 'darwin' (macOS)
            command = `ping -c ${count} ${ipAddress}`;
        }

        exec(command, (error, stdout, stderr) => {
            if (error) {
                // Ping returns an error code if the host is unreachable or other issues.
                // If stdout contains "Request timed out" or "Destination Host Unreachable",
                // it's a failed ping.
                if (stdout.includes("Request timed out") || stdout.includes("Destination Host Unreachable") || stdout.includes("100% packet loss")) {
                    resolve(`Ping failed to ${ipAddress}:\n${stdout.trim()}`);
                } else {
                    console.error(`exec error: ${error.message}`);
                    reject(new Error(`Ping command failed: ${stderr || error.message}`));
                }
                return;
            }
            if (stderr) {
                console.warn(`Ping command stderr: ${stderr}`); // Warnings might appear here
            }

            // Analyze stdout for success and details
            if (stdout.includes("Lost = 0") || stdout.includes("0% packet loss")) {
                let summary = `Ping successful to ${ipAddress}:\n${stdout.trim()}`;
                // Extract average time for Windows
                const avgMatchWin = stdout.match(/Average = (\d+)ms/);
                if (avgMatchWin) {
                    summary += `\nAverage Roundtrip Time: ${avgMatchWin[1]}ms`;
                }
                // Extract min/avg/max for Linux/macOS
                const rttMatchLinux = stdout.match(/min\/avg\/max\/mdev = ([\d./]+)/);
                if (rttMatchLinux) {
                    const times = rttMatchLinux[1].split('/');
                    summary += `\nRoundtrip Time (min/avg/max): ${times[0]}/${times[1]}/${times[2]} ms`;
                }
                resolve(summary);
            } else {
                resolve(`Ping successful, but with packet loss to ${ipAddress}:\n${stdout.trim()}`);
            }
        });
    });
}

// Example usage:
// (async () => {
//     const targetIp = '192.168.1.1'; // Example: your router's IP
//     // const targetIp = 'google.com'; // Example: a public domain
//     // const targetIp = 'non.existent.ip.address'; // Example: a non-existent IP
//
//     try {
//         const result = await runPingTest(targetIp);
//         console.log(result);
//     } catch (e) {
//         console.error('Failed to run ping test:', e);
//     }
// })();
```

### 🧪 Senaryo 6: Bir dosya dönüştürme uygulamasında kullanıcılar kaynak ve hedef dosya yollarını belirtir. Sistem bu yolları kullanarak dönüştürme komutları çalıştırır. Dönüştürülen dosyalar kullanıcıya sunulur. Çeşitli format dönüştürmeleri desteklenir.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 92
```csharp
using System;
using System.Diagnostics;
using System.IO;
using System.Threading.Tasks;

public class FileConverter
{
    // This example uses FFmpeg for demonstration. You would need FFmpeg installed on the system
    // and its executable path configured or in the system's PATH environment variable.
    // FFmpeg is a common tool for audio/video/image conversion.
    private readonly string ffmpegPath = "ffmpeg"; // Or specify full path like "C:\\ffmpeg\\bin\\ffmpeg.exe"

    public async Task<string> ConvertFileAsync(string sourceFilePath, string destinationFilePath)
    {
        if (!File.Exists(sourceFilePath))
        {
            return $"Error: Source file '{sourceFilePath}' does not exist.";
        }

        string sourceExtension = Path.GetExtension(sourceFilePath).ToLower();
        string destinationExtension = Path.GetExtension(destinationFilePath).ToLower();

        // Basic validation for demonstration. In a real app, you'd have extensive format mappings.
        if (string.IsNullOrEmpty(sourceExtension) || string.IsNullOrEmpty(destinationExtension))
        {
            return "Error: Source and destination file paths must include extensions.";
        }

        // Example: Convert MP4 to AVI, or JPG to PNG, etc. FFmpeg handles many formats.
        // The actual arguments for FFmpeg depend on the specific conversion.
        string arguments = $"-i \"{sourceFilePath}\" \"{destinationFilePath}\"";

        // Ensure destination directory exists
        string destinationDir = Path.GetDirectoryName(destinationFilePath);
        if (!string.IsNullOrEmpty(destinationDir) && !Directory.Exists(destinationDir))
        {
            try
            {
                Directory.CreateDirectory(destinationDir);
            }
            catch (Exception ex)
            {
                return $"Error creating destination directory '{destinationDir}': {ex.Message}";
            }
        }

        try
        {
            ProcessStartInfo startInfo = new ProcessStartInfo
            {
                FileName = ffmpegPath,
                Arguments = arguments,
                RedirectStandardOutput = true,
                RedirectStandardError = true, // FFmpeg usually writes progress/errors to stderr
                UseShellExecute = false,
                CreateNoWindow = true
            };

            using (Process process = new Process { StartInfo = startInfo })
            {
                process.Start();

                // Capture output and error asynchronously
                string output = await process.StandardOutput.ReadToEndAsync();
                string error = await process.StandardError.ReadToEndAsync();

                process.WaitForExit(); // Wait for the process to complete

                if (process.ExitCode == 0)
                {
                    return $"File converted successfully: '{sourceFilePath}' to '{destinationFilePath}'.";
                }
                else
                {
                    // FFmpeg often outputs warnings/info to stderr even on success, so check ExitCode.
                    // If ExitCode is non-zero, it indicates an error.
                    return $"Error converting file. FFmpeg Exit Code: {process.ExitCode}. Output: {output}. Error: {error}";
                }
            }
        }
        catch (System.ComponentModel.Win32Exception ex) when (ex.NativeErrorCode == 2) // Error code 2: file not found
        {
            return $"Error: FFmpeg executable not found at '{ffmpegPath}'. Please ensure it's installed and in your system PATH or specify its full path.";
        }
        catch (Exception ex)
        {
            return $"An unexpected error occurred during file conversion: {ex.Message}";
        }
    }
}

// Example usage in a controller or service:
// [HttpPost("convert-file")]
// public async Task<IActionResult> ConvertFile(string sourcePath, string destPath)
// {
//     FileConverter converter = new FileConverter();
//     string result = await converter.ConvertFileAsync(sourcePath, destPath);
//
//     if (result.StartsWith("Error"))
//     {
//         return BadRequest(result);
//     }
//     return Ok(result);
// }
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 63
```python
import subprocess
import os
import platform

def convert_file(source_file_path, destination_file_path):
    """
    Converts a file from one format to another using external tools.
    This example uses FFmpeg for multimedia files. For other formats (e.g., DOCX to PDF),
    you'd use different libraries or command-line tools.
    Requires FFmpeg to be installed and accessible in the system's PATH.

    Args:
        source_file_path (str): The path to the input file.
        destination_file_path (str): The path where the converted file will be saved.
    Returns:
        str: A status message indicating success or failure.
    """
    if not os.path.exists(source_file_path):
        return f"Error: Source file '{source_file_path}' does not exist."

    # Determine the converter executable
    ffmpeg_exec = "ffmpeg"
    if platform.system() == "Windows":
        # On Windows, you might need the full path if not in PATH
        # ffmpeg_exec = "C:\\ffmpeg\\bin\\ffmpeg.exe"
        pass # Assuming ffmpeg is in PATH or handled by environment

    # Ensure destination directory exists
    destination_dir = os.path.dirname(destination_file_path)
    if destination_dir and not os.path.exists(destination_dir):
        try:
            os.makedirs(destination_dir)
        except OSError as e:
            return f"Error creating destination directory '{destination_dir}': {e}"

    # FFmpeg command for general conversion: ffmpeg -i input.ext output.ext
    command = [ffmpeg_exec, "-i", source_file_path, destination_file_path]

    try:
        process = subprocess.run(command, capture_output=True, text=True, check=False)
        stdout = process.stdout
        stderr = process.stderr

        if process.returncode == 0:
            return f"File converted successfully: '{source_file_path}' to '{destination_file_path}'."
        else:
            return (f"Error converting file. Command exited with code {process.returncode}.\n"
                    f"Output:\n{stdout}\nError:\n{stderr}")
    except FileNotFoundError:
        return f"Error: '{ffmpeg_exec}' command not found. Please ensure FFmpeg is installed and in your system PATH."
    except Exception as e:
        return f"An unexpected error occurred during file conversion: {e}"

# Example usage:
# if __name__ == "__main__":
#     # For a web application, these paths would come from user input/file uploads
#     source_file = "input.mp4"
#     destination_file = "output.avi"
#     # Create a dummy input file for testing if it doesn't exist
#     if not os.path.exists(source_file):
#         print(f"Creating a dummy file '{source_file}' for demonstration.")
#         with open(source_file, "w") as f:
#             f.write("This is a dummy video file content. (Needs real video for FFmpeg)")
#         print("Note: FFmpeg will likely fail on this dummy file without actual video content.")

#     result = convert_file(source_file, destination_file)
#     print(result)

#     # Clean up dummy file
#     # if os.path.exists(source_file):
#     #     os.remove(source_file)
#     # if os.path.exists(destination_file):
#     #     os.remove(destination_file)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 72
```typescript
import { exec } from 'child_process';
import * as path from 'path';
import * as fs from 'fs';

/**
 * Converts a file from a source path to a destination path using an external command-line tool.
 * This example primarily targets FFmpeg for multimedia conversions.
 * You'll need FFmpeg installed and available in the system's PATH.
 * @param sourceFilePath The full path to the source file.
 * @param destinationFilePath The full path where the converted file will be saved.
 * @returns A promise that resolves to a status message string.
 */
function convertFile(sourceFilePath: string, destinationFilePath: string): Promise<string> {
    return new Promise((resolve, reject) => {
        if (!fs.existsSync(sourceFilePath)) {
            return resolve(`Error: Source file '${sourceFilePath}' does not exist.`);
        }

        const ffmpegExecutable = 'ffmpeg'; // Ensure FFmpeg is in your system's PATH

        // Ensure destination directory exists
        const destinationDir = path.dirname(destinationFilePath);
        if (!fs.existsSync(destinationDir)) {
            try {
                fs.mkdirSync(destinationDir, { recursive: true });
            } catch (error: any) {
                return resolve(`Error creating destination directory '${destinationDir}': ${error.message}`);
            }
        }

        // Construct the FFmpeg command
        // Basic conversion: ffmpeg -i input.ext output.ext
        const command = `${ffmpegExecutable} -i "${sourceFilePath}" "${destinationFilePath}"`;

        exec(command, (error, stdout, stderr) => {
            if (error) {
                console.error(`File conversion command failed: ${error.message}`);
                // FFmpeg often logs progress/warnings to stderr even if successful,
                // so we check error.code and also consider common error messages.
                if (stderr.includes("No such file or directory")) {
                     return resolve(`Error: FFmpeg could not find source file or create destination file. Details: ${stderr}`);
                }
                return reject(new Error(`Conversion failed: ${stderr || error.message}`));
            }
            if (stderr) {
                console.warn(`FFmpeg output (stderr, possibly warnings): ${stderr}`);
            }
            resolve(`File converted successfully: '${sourceFilePath}' to '${destinationFilePath}'.`);
        });
    });
}

// Example usage:
// (async () => {
//     const sourceFile = '/path/to/input.mp4'; // e.g., '/home/user/videos/clip.mp4' or 'C:\\videos\\clip.mp4'
//     const destinationFile = '/path/to/output.avi'; // e.g., '/home/user/videos/clip.avi' or 'C:\\videos\\clip.avi'

//     // You would typically get these paths from user input or file uploads
//     // For demonstration, create dummy files if they don't exist
//     if (!fs.existsSync(sourceFile)) {
//         console.log(`Creating dummy source file: ${sourceFile}`);
//         fs.writeFileSync(sourceFile, 'dummy video content');
//         console.log('NOTE: FFmpeg will likely fail on this dummy file. Use a real video file for actual testing.');
//     }

//     try {
//         const result = await convertFile(sourceFile, destinationFile);
//         console.log(result);
//     } catch (e) {
//         console.error('An error occurred during conversion:', e);
//     } finally {
//         // Clean up dummy file if created
//         // if (fs.existsSync(sourceFile) && fs.readFileSync(sourceFile, 'utf8') === 'dummy video content') {
//         //     fs.unlinkSync(sourceFile);
//         // }
//         // if (fs.existsSync(destinationFile)) {
//         //     fs.unlinkSync(destinationFile);
//         // }
//     }
// })();
```

### 🧪 Senaryo 7: Bir disk alanı analiz aracında kullanıcılar dizin yolu girip alan kullanımını görebilir. Sistem girilen yolu kullanarak analiz komutları çalıştırır. Alan kullanım raporu oluşturulur. Sonuçlar grafik olarak gösterilir.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 132
```csharp
using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using System.Collections.Generic;

public class DiskSpaceAnalyzer
{
    // A simple method to calculate directory size. For very large directories,
    // this can be slow. A more robust solution might use system commands or
    // a dedicated library for faster traversal.
    public async Task<string> GetDirectorySizeReportAsync(string directoryPath)
    {
        if (!Directory.Exists(directoryPath))
        {
            return $"Error: Directory '{directoryPath}' does not exist.";
        }

        try
        {
            long totalSize = await Task.Run(() => CalculateDirectorySize(new DirectoryInfo(directoryPath), true));

            // Convert bytes to a more readable format
            string formattedSize = FormatBytes(totalSize);

            // For "graphical representation," in a console app, this might be a simple text-based breakdown.
            // In a UI application, you'd use a charting library.
            string report = $"--- Disk Usage Report for: {directoryPath} ---{Environment.NewLine}";
            report += $"Total Size: {formattedSize}{Environment.NewLine}{Environment.NewLine}";

            report += "Top 10 Largest Subdirectories/Files (approximate):" + Environment.NewLine;

            // Get top subdirectories/files for a basic breakdown
            var topItems = Directory.GetFileSystemEntries(directoryPath, "*", SearchOption.TopDirectoryOnly)
                                    .Select(item => new
                                    {
                                        Path = item,
                                        Size = GetFileSystemEntrySize(item)
                                    })
                                    .OrderByDescending(item => item.Size)
                                    .Take(10)
                                    .ToList();

            foreach (var item in topItems)
            {
                report += $"{Path.GetFileName(item.Path)}: {FormatBytes(item.Size)}{Environment.NewLine}";
            }

            return report;
        }
        catch (UnauthorizedAccessException ex)
        {
            return $"Error: Access denied to '{directoryPath}'. Details: {ex.Message}";
        }
        catch (Exception ex)
        {
            return $"An error occurred during disk analysis: {ex.Message}";
        }
    }

    private long CalculateDirectorySize(DirectoryInfo directoryInfo, bool recursive)
    {
        long totalSize = 0;
        try
        {
            // Add file sizes
            foreach (FileInfo file in directoryInfo.GetFiles())
            {
                totalSize += file.Length;
            }

            // Add subdirectory sizes
            if (recursive)
            {
                foreach (DirectoryInfo subDir in directoryInfo.GetDirectories())
                {
                    totalSize += CalculateDirectorySize(subDir, true);
                }
            }
        }
        catch (UnauthorizedAccessException)
        {
            // Skip directories we don't have access to
            // Console.WriteLine($"Access denied to: {directoryInfo.FullName}");
        }
        catch (Exception)
        {
            // Handle other potential errors during enumeration
        }
        return totalSize;
    }

    private long GetFileSystemEntrySize(string path)
    {
        try
        {
            FileAttributes attr = File.GetAttributes(path);
            if ((attr & FileAttributes.Directory) == FileAttributes.Directory)
            {
                // It's a directory, calculate its size
                return CalculateDirectorySize(new DirectoryInfo(path), true);
            }
            else
            {
                // It's a file, get its length
                return new FileInfo(path).Length;
            }
        }
        catch (UnauthorizedAccessException)
        {
            return 0; // Cannot access, treat as 0 for sum
        }
        catch (Exception)
        {
            return 0; // Other errors, treat as 0
        }
    }

    private string FormatBytes(long bytes)
    {
        string[] Suffix = { "B", "KB", "MB", "GB", "TB" };
        int i = 0;
        double dblSByte = bytes;
        while (dblSByte >= 1024 && i < Suffix.Length - 1)
        {
            dblSByte /= 1024;
            i++;
        }
        return $"{dblSByte:0.##} {Suffix[i]}";
    }
}

// Example usage:
// [HttpGet("analyze-disk-usage")]
// public async Task<IActionResult> AnalyzeDiskUsage(string directoryPath)
// {
//     DiskSpaceAnalyzer analyzer = new DiskSpaceAnalyzer();
//     string report = await analyzer.GetDirectorySizeReportAsync(directoryPath);
//
//     if (report.StartsWith("Error"))
//     {
//         return BadRequest(report);
//     }
//     return Ok(report);
// }
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 110
```python
import os
import platform
import subprocess

def format_bytes(bytes_count):
    """Formats a number of bytes into a human-readable string (e.g., 1.2 GB)."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_count < 1024.0:
            return f"{bytes_count:.2f} {unit}"
        bytes_count /= 1024.0

def get_disk_usage_report(directory_path):
    """
    Generates a disk usage report for a given directory using system commands (du/dir).
    The "graphical" part here is a textual breakdown. For true graphics, a UI library is needed.
    Args:
        directory_path (str): The path to the directory to analyze.
    Returns:
        str: A formatted report string.
    """
    if not os.path.isdir(directory_path):
        return f"Error: Directory '{directory_path}' does not exist."

    command = []
    if platform.system() == "Windows":
        # 'dir /s /a /q /c' for detailed directory listing, then calculate size
        # A simpler way for total size is 'powershell Get-ChildItem -Recurse | Measure-Object -Property Length -Sum'
        # For this example, we'll use a more direct approach for folder size on Windows,
        # but for subdirectories breakdown, it's more complex with native commands.
        # Let's use 'du' equivalent in Python for cross-platform consistency by walking the directory.
        pass
    else:  # Linux, macOS
        # du -sh for human-readable summary, du -h --max-depth=1 for subdirectories
        command = ["du", "-sh", directory_path] # Use du for total size first

    try:
        total_size_bytes = 0
        if platform.system() == "Windows":
            # Walk directory to calculate total size, similar to 'du' on Linux
            for dirpath, dirnames, filenames in os.walk(directory_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    if not os.path.islink(fp): # Avoid counting symlinks multiple times
                        try:
                            total_size_bytes += os.path.getsize(fp)
                        except OSError:
                            # Handle permission errors or files disappearing
                            pass
        else:
            # Use 'du -sh' for total size on Linux/macOS
            process = subprocess.run(command, capture_output=True, text=True, check=True)
            total_size_output = process.stdout.strip()
            # Extract numerical size (e.g., "1.2G  /path/to/dir" -> 1.2G)
            total_size_str = total_size_output.split('\t')[0] # Get "1.2G" part
            # Convert human-readable string to bytes for consistent formatting later (optional, can just use du output directly)
            # This requires custom parsing or a library. For simplicity, we'll just report the du output.
            # However, for a proper "report", consistent byte calculation is better.
            # Let's re-use the os.walk for consistency for breakdown too.

            # Re-calculating with os.walk for consistency and breakdown
            for dirpath, dirnames, filenames in os.walk(directory_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    if not os.path.islink(fp):
                        try:
                            total_size_bytes += os.path.getsize(fp)
                        except OSError:
                            pass

        report = f"--- Disk Usage Report for: {directory_path} ---\n"
        report += f"Total Size: {format_bytes(total_size_bytes)}\n\n"

        report += "Top 10 Largest Subdirectories/Files:\n"
        # Get sizes of top-level items for a breakdown
        top_level_items = []
        for item_name in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item_name)
            item_size = 0
            try:
                if os.path.isfile(item_path):
                    item_size = os.path.getsize(item_path)
                elif os.path.isdir(item_path):
                    # Recursively calculate size for subdirectories
                    for dirpath, dirnames, filenames in os.walk(item_path):
                        for f in filenames:
                            fp = os.path.join(dirpath, f)
                            if not os.path.islink(fp):
                                try:
                                    item_size += os.path.getsize(fp)
                                except OSError:
                                    pass
            except OSError:
                # Handle permission errors
                pass
            top_level_items.append({'name': item_name, 'size': item_size})

        top_level_items.sort(key=lambda x: x['size'], reverse=True)

        for i, item in enumerate(top_level_items[:10]):
            report += f"{item['name']}: {format_bytes(item['size'])}\n"
            if i < len(top_level_items[:10]) - 1:
                # Simple text-based "bar" for visualization
                percentage = (item['size'] / total_size_bytes) * 100 if total_size_bytes > 0 else 0
                bar_length = int(percentage / 5) # 20 char max bar
                report += f"[{'#' * bar_length}{'-' * (20 - bar_length)}] {percentage:.1f}%\n"

        return report

    except FileNotFoundError:
        return "Error: System command not found. Ensure 'du' (Linux/macOS) or relevant tools are in your PATH."
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.cmd} - {e.stderr.strip()}"
    except Exception as e:
        return f"An unexpected error occurred during disk analysis: {e}"

# Example usage:
# if __name__ == "__main__":
#     # For a web application, this path would come from user input
#     target_directory = "/home/user/documents" # Example Linux path
#     # target_directory = "C:\\Program Files" # Example Windows path
#     report = get_disk_usage_report(target_directory)
#     print(report)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 111
```typescript
import { exec } from 'child_process';
import * as path from 'path';
import * as fs from 'fs';
import * as os from 'os';

/**
 * Formats a number of bytes into a human-readable string (e.g., 1.2 GB).
 * @param bytes The number of bytes.
 * @returns A formatted string.
 */
function formatBytes(bytes: number): string {
    const units = ['B', 'KB', 'MB', 'GB', 'TB'];
    let i = 0;
    while (bytes >= 1024 && i < units.length - 1) {
        bytes /= 1024;
        i++;
    }
    return `${bytes.toFixed(2)} ${units[i]}`;
}

/**
 * Recursively calculates the size of a directory.
 * @param directoryPath The path to the directory.
 * @returns The size in bytes.
 */
async function calculateDirectorySize(directoryPath: string): Promise<number> {
    let totalSize = 0;
    try {
        const files = await fs.promises.readdir(directoryPath, { withFileTypes: true });
        for (const file of files) {
            const fullPath = path.join(directoryPath, file.name);
            try {
                if (file.isDirectory()) {
                    totalSize += await calculateDirectorySize(fullPath);
                } else if (file.isFile()) {
                    const stats = await fs.promises.stat(fullPath);
                    totalSize += stats.size;
                }
            } catch (innerError: any) {
                // Ignore permission errors or file disappearing during traversal
                if (innerError.code === 'EACCES' || innerError.code === 'ENOENT') {
                    console.warn(`Skipping (permission/not found): ${fullPath}`);
                } else {
                    console.error(`Error processing ${fullPath}: ${innerError.message}`);
                }
            }
        }
    } catch (error: any) {
        if (error.code === 'EACCES' || error.code === 'ENOENT') {
            console.warn(`Could not access directory: ${directoryPath}. Skipping.`);
        } else {
            throw error;
        }
    }
    return totalSize;
}

/**
 * Generates a disk usage report for a given directory.
 * @param directoryPath The path to the directory to analyze.
 * @returns A promise that resolves to a formatted report string.
 */
async function getDiskUsageReport(directoryPath: string): Promise<string> {
    if (!fs.existsSync(directoryPath)) {
        return `Error: Directory '${directoryPath}' does not exist.`;
    }

    try {
        const totalSize = await calculateDirectorySize(directoryPath);
        let report = `--- Disk Usage Report for: ${directoryPath} ---\n`;
        report += `Total Size: ${formatBytes(totalSize)}\n\n`;

        report += "Top 10 Largest Subdirectories/Files:\n";

        const topLevelItems: { name: string; size: number }[] = [];
        const entries = await fs.promises.readdir(directoryPath, { withFileTypes: true });

        for (const entry of entries) {
            const entryPath = path.join(directoryPath, entry.name);
            let entrySize = 0;
            try {
                if (entry.isDirectory()) {
                    entrySize = await calculateDirectorySize(entryPath);
                } else if (entry.isFile()) {
                    const stats = await fs.promises.stat(entryPath);
                    entrySize = stats.size;
                }
            } catch (error: any) {
                 if (error.code === 'EACCES' || error.code === 'ENOENT') {
                    console.warn(`Skipping (permission/not found): ${entryPath}`);
                } else {
                    console.error(`Error getting size for ${entryPath}: ${error.message}`);
                }
            }
            topLevelItems.push({ name: entry.name, size: entrySize });
        }

        topLevelItems.sort((a, b) => b.size - a.size); // Sort descending

        for (let i = 0; i < Math.min(10, topLevelItems.length); i++) {
            const item = topLevelItems[i];
            report += `${item.name}: ${formatBytes(item.size)}\n`;
            if (totalSize > 0) {
                const percentage = (item.size / totalSize) * 100;
                const barLength = Math.floor(percentage / 5); // 20 char max bar
                report += `[${'#'.repeat(barLength)}${'-'.repeat(20 - barLength)}] ${percentage.toFixed(1)}%\n`;
            }
        }

        return report;
    } catch (e: any) {
        return `An unexpected error occurred during disk analysis: ${e.message}`;
    }
}

// Example usage:
// (async () => {
//     const targetDirectory = '/home/user/Downloads'; // Example Linux path
//     // const targetDirectory = 'C:\\Users\\YourUser\\Documents'; // Example Windows path
//     const report = await getDiskUsageReport(targetDirectory);
//     console.log(report);
// })();
```

### 🧪 Senaryo 8: Bir veritabanı yedekleme uygulamasında kullanıcılar veritabanı adını girebilir. Sistem girilen adı kullanarak backup komutları çalıştırır. Yedekleme işlemi gerçekleştirilir. Yedek dosyaları belirtilen konuma kaydedilir.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 111
```csharp
using System;
using System.Diagnostics;
using System.IO;
using System.Threading.Tasks;

public class DatabaseBackupManager
{
    // This example uses `pg_dump` for PostgreSQL. For SQL Server, you'd use `sqlcmd` or SMO.
    // For MySQL, you'd use `mysqldump`. The exact command depends on the database.
    private readonly string _backupToolPath; // e.g., "C:\\Program Files\\PostgreSQL\\14\\bin\\pg_dump.exe"
    private readonly string _dbHost;
    private readonly string _dbPort;
    private readonly string _dbUser;
    private readonly string _dbPassword; // Be cautious with passwords in code, prefer environment variables or secure config.

    public DatabaseBackupManager(string backupToolPath, string dbHost, string dbPort, string dbUser, string dbPassword)
    {
        _backupToolPath = backupToolPath;
        _dbHost = dbHost;
        _dbPort = dbPort;
        _dbUser = dbUser;
        _dbPassword = dbPassword;
    }

    public async Task<string> BackupDatabaseAsync(string databaseName, string backupFilePath)
    {
        if (string.IsNullOrWhiteSpace(databaseName))
        {
            return "Error: Database name cannot be empty.";
        }
        if (string.IsNullOrWhiteSpace(backupFilePath))
        {
            return "Error: Backup file path cannot be empty.";
        }

        // Ensure the backup directory exists
        string backupDir = Path.GetDirectoryName(backupFilePath);
        if (!string.IsNullOrEmpty(backupDir) && !Directory.Exists(backupDir))
        {
            try
            {
                Directory.CreateDirectory(backupDir);
            }
            catch (Exception ex)
            {
                return $"Error creating backup directory '{backupDir}': {ex.Message}";
            }
        }

        // Example for PostgreSQL's pg_dump
        // pg_dump -h host -p port -U user -Fc dbname > backup.dump
        string arguments = $"-h {_dbHost} -p {_dbPort} -U {_dbUser} -Fc \"{databaseName}\" > \"{backupFilePath}\"";

        try
        {
            ProcessStartInfo startInfo = new ProcessStartInfo
            {
                FileName = _backupToolPath,
                Arguments = arguments,
                RedirectStandardOutput = false, // Output is redirected to file directly using '>'
                RedirectStandardError = true,   // Capture errors
                UseShellExecute = true,         // Required for shell redirection ('>')
                CreateNoWindow = true,
                EnvironmentVariables = { { "PGPASSWORD", _dbPassword } } // Pass password securely via env variable for pg_dump
            };

            using (Process process = new Process { StartInfo = startInfo })
            {
                process.Start();
                string errorOutput = await process.StandardError.ReadToEndAsync();
                process.WaitForExit();

                if (process.ExitCode == 0)
                {
                    if (File.Exists(backupFilePath) && new FileInfo(backupFilePath).Length > 0)
                    {
                        return $"Database '{databaseName}' backed up successfully to '{backupFilePath}'.";
                    }
                    else
                    {
                        // Even if exit code is 0, file might be empty if something went wrong or db is empty.
                        return $"Backup completed with exit code 0, but backup file '{backupFilePath}' is empty or not created.";
                    }
                }
                else
                {
                    return $"Error backing up database '{databaseName}'. Exit Code: {process.ExitCode}. Error: {errorOutput}";
                }
            }
        }
        catch (System.ComponentModel.Win32Exception ex) when (ex.NativeErrorCode == 2)
        {
            return $"Error: Database backup tool not found at '{_backupToolPath}'. Please ensure it's installed and the path is correct.";
        }
        catch (Exception ex)
        {
            return $"An unexpected error occurred during database backup: {ex.Message}";
        }
    }
}

// Example usage in a controller or service:
// [HttpPost("backup-database")]
// public async Task<IActionResult> BackupDatabase(string dbName, string backupFileName)
// {
//     // Configuration would typically come from appsettings.json or environment variables
//     string backupTool = "C:\\Program Files\\PostgreSQL\\14\\bin\\pg_dump.exe";
//     string host = "localhost";
//     string port = "5432";
//     string user = "postgres";
//     string password = "your_db_password"; // Use secure methods for passwords

//     string backupPath = Path.Combine("C:\\DatabaseBackups", backupFileName + ".dump");

//     DatabaseBackupManager backupManager = new DatabaseBackupManager(backupTool, host, port, user, password);
//     string result = await backupManager.BackupDatabaseAsync(dbName, backupPath);

//     if (result.StartsWith("Error"))
//     {
//         return StatusCode(500, result);
//     }
//     return Ok(result);
// }
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 105
```python
import subprocess
import os
import datetime

def backup_database(db_type, db_name, backup_file_path,
                    host="localhost", port=None, user=None, password=None):
    """
    Performs a database backup using command-line tools.
    Supports PostgreSQL (pg_dump) and MySQL (mysqldump).

    Args:
        db_type (str): Type of database ('postgresql' or 'mysql').
        db_name (str): The name of the database to backup.
        backup_file_path (str): The full path where the backup file will be saved.
        host (str, optional): Database host. Defaults to 'localhost'.
        port (str, optional): Database port.
        user (str, optional): Database username.
        password (str, optional): Database password. (Use with caution, consider env vars)

    Returns:
        str: A status message indicating success or failure.
    """
    if not db_name or not backup_file_path:
        return "Error: Database name and backup file path cannot be empty."

    # Ensure backup directory exists
    backup_dir = os.path.dirname(backup_file_path)
    if backup_dir and not os.path.exists(backup_dir):
        try:
            os.makedirs(backup_dir)
        except OSError as e:
            return f"Error creating backup directory '{backup_dir}': {e}"

    command = []
    env = os.environ.copy() # Copy current environment for subprocess

    if db_type.lower() == 'postgresql':
        pg_dump_exec = "pg_dump"
        if password:
            env["PGPASSWORD"] = password # pg_dump uses PGPASSWORD environment variable
        command = [pg_dump_exec]
        if host: command.extend(["-h", host])
        if port: command.extend(["-p", str(port)])
        if user: command.extend(["-U", user])
        command.extend(["-Fc", db_name]) # -Fc for custom format archive
        # Redirect output to file
        with open(backup_file_path, 'wb') as f: # 'wb' for binary output for -Fc format
            try:
                process = subprocess.run(command, env=env, stdout=f, stderr=subprocess.PIPE, check=False)
                if process.returncode == 0:
                    if os.path.exists(backup_file_path) and os.path.getsize(backup_file_path) > 0:
                        return f"Database '{db_name}' (PostgreSQL) backed up successfully to '{backup_file_path}'."
                    else:
                        return f"Backup completed with exit code 0, but backup file '{backup_file_path}' is empty or not created."
                else:
                    return f"Error backing up PostgreSQL database '{db_name}'. Exit Code: {process.returncode}. Error: {process.stderr.decode().strip()}"
            except FileNotFoundError:
                return f"Error: '{pg_dump_exec}' command not found. Ensure PostgreSQL client tools are installed and in PATH."
            except Exception as e:
                return f"An unexpected error occurred during PostgreSQL backup: {e}"

    elif db_type.lower() == 'mysql':
        mysqldump_exec = "mysqldump"
        command = [mysqldump_exec]
        if host: command.extend(["-h", host])
        if port: command.extend(["-P", str(port)]) # -P for port in mysqldump
        if user: command.extend(["-u", user])
        if password: command.extend([f"-p{password}"]) # No space after -p for password
        command.append(db_name)

        with open(backup_file_path, 'w') as f: # 'w' for text output for mysqldump
            try:
                process = subprocess.run(command, stdout=f, stderr=subprocess.PIPE, check=False)
                if process.returncode == 0:
                    if os.path.exists(backup_file_path) and os.path.getsize(backup_file_path) > 0:
                        return f"Database '{db_name}' (MySQL) backed up successfully to '{backup_file_path}'."
                    else:
                        return f"Backup completed with exit code 0, but backup file '{backup_file_path}' is empty or not created."
                else:
                    return f"Error backing up MySQL database '{db_name}'. Exit Code: {process.returncode}. Error: {process.stderr.decode().strip()}"
            except FileNotFoundError:
                return f"Error: '{mysqldump_exec}' command not found. Ensure MySQL client tools are installed and in PATH."
            except Exception as e:
                return f"An unexpected error occurred during MySQL backup: {e}"

    else:
        return f"Error: Unsupported database type: {db_type}. Supported types are 'postgresql' and 'mysql'."

# Example usage:
# if __name__ == "__main__":
#     # PostgreSQL Backup Example
#     # pg_dump must be in system PATH, or specify full path
#     pg_result = backup_database(
#         db_type="postgresql",
#         db_name="mydatabase",
#         backup_file_path=f"C:\\backups\\mydatabase_pg_backup_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.dump",
#         host="localhost",
#         port="5432",
#         user="postgres",
#         password="mypassword"
#     )
#     print(pg_result)
#
#     # MySQL Backup Example
#     # mysqldump must be in system PATH, or specify full path
#     mysql_result = backup_database(
#         db_type="mysql",
#         db_name="my_mysql_db",
#         backup_file_path=f"/var/backups/my_mysql_db_backup_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.sql",
#         host="localhost",
#         port="3306",
#         user="root",
#         password="mysecretpassword"
#     )
#     print(mysql_result)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 107
```typescript
import { exec } from 'child_process';
import * as path from 'path';
import * as fs from 'fs';

/**
 * Performs a database backup using command-line tools.
 * This example focuses on PostgreSQL (pg_dump) and MySQL (mysqldump).
 * Ensure the respective client tools are installed and accessible in the system's PATH.
 * @param dbType The type of database ('postgresql' or 'mysql').
 * @param dbName The name of the database to backup.
 * @param backupFilePath The full path where the backup file will be saved.
 * @param options Optional configuration for host, port, user, password.
 * @returns A promise that resolves to a status message string.
 */
function backupDatabase(
    dbType: 'postgresql' | 'mysql',
    dbName: string,
    backupFilePath: string,
    options?: { host?: string; port?: number; user?: string; password?: string }
): Promise<string> {
    return new Promise((resolve, reject) => {
        if (!dbName || !backupFilePath) {
            return resolve("Error: Database name and backup file path cannot be empty.");
        }

        const backupDir = path.dirname(backupFilePath);
        if (!fs.existsSync(backupDir)) {
            try {
                fs.mkdirSync(backupDir, { recursive: true });
            } catch (error: any) {
                return resolve(`Error creating backup directory '${backupDir}': ${error.message}`);
            }
        }

        let command: string;
        const env = { ...process.env }; // Copy current environment variables

        if (dbType === 'postgresql') {
            const pgDumpExecutable = 'pg_dump';
            let args: string[] = [];
            if (options?.host) args.push(`-h ${options.host}`);
            if (options?.port) args.push(`-p ${options.port}`);
            if (options?.user) args.push(`-U ${options.user}`);
            args.push(`-Fc "${dbName}"`); // -Fc for custom format archive
            if (options?.password) {
                env.PGPASSWORD = options.password; // pg_dump uses PGPASSWORD env variable
            }
            command = `${pgDumpExecutable} ${args.join(' ')} > "${backupFilePath}"`;
        } else if (dbType === 'mysql') {
            const mysqlDumpExecutable = 'mysqldump';
            let args: string[] = [];
            if (options?.host) args.push(`-h ${options.host}`);
            if (options?.port) args.push(`-P ${options.port}`); // -P for port in mysqldump
            if (options?.user) args.push(`-u ${options.user}`);
            if (options?.password) args.push(`-p${options.password}`); // No space after -p for password
            args.push(`"${dbName}"`);
            command = `${mysqlDumpExecutable} ${args.join(' ')} > "${backupFilePath}"`;
        } else {
            return resolve(`Error: Unsupported database type: ${dbType}. Supported types are 'postgresql' and 'mysql'.`);
        }

        exec(command, { env, shell: true }, (error, stdout, stderr) => {
            if (error) {
                console.error(`Database backup command failed: ${error.message}`);
                // Check if the error is due to command not found
                if (error.code === 127 || stderr.includes("command not found")) {
                    return reject(new Error(`Backup tool not found. Ensure ${dbType === 'postgresql' ? 'pg_dump' : 'mysqldump'} is installed and in your system PATH.`));
                }
                return reject(new Error(`Backup failed: ${stderr || error.message}`));
            }
            if (stderr) {
                console.warn(`Backup command stderr (might contain warnings): ${stderr}`);
            }

            // Verify if the file was actually created and has content
            if (fs.existsSync(backupFilePath) && fs.statSync(backupFilePath).size > 0) {
                resolve(`Database '${dbName}' (${dbType}) backed up successfully to '${backupFilePath}'.`);
            } else {
                resolve(`Backup command finished, but backup file '${backupFilePath}' is empty or not created.`);
            }
        });
    });
}

// Example usage:
// (async () => {
//     // PostgreSQL Backup Example
//     const pgBackupResult = await backupDatabase(
//         'postgresql',
//         'my_prod_db',
//         path.join(__dirname, `backups/my_prod_db_pg_backup_${new Date().toISOString().replace(/:/g, '-')}.dump`),
//         {
//             host: 'localhost',
//             port: 5432,
//             user: 'postgres',
//             password: 'mysecretpassword' // In real apps, use environment variables for passwords!
//         }
//     );
//     console.log(pgBackupResult);
//
//     // MySQL Backup Example
//     const mysqlBackupResult = await backupDatabase(
//         'mysql',
//         'my_dev_db',
//         path.join(__dirname, `backups/my_dev_db_mysql_backup_${new Date().toISOString().replace(/:/g, '-')}.sql`),
//         {
//             host: 'localhost',
//             port: 3306,
//             user: 'root',
//             password: 'myrootpassword'
//         }
//     );
//     console.log(mysqlBackupResult);
// })();
```

### 🧪 Senaryo 9: Bir mail sunucu yönetimi aracında kullanıcılar posta kutusu adını girip durum kontrolü yapabilir. Sistem girilen adı kullanarak mail sistem komutları çalıştırır. Posta kutusu bilgileri gösterilir. Mail trafiği analiz edilir.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 102
```csharp
using System;
using System.Diagnostics;
using System.Threading.Tasks;
using System.Text.RegularExpressions;
using System.Collections.Generic;

public class MailServerManager
{
    // This example simulates checking mail user status on a Linux-like system
    // that might use 'doveadm' for Dovecot, or 'postcat' for Postfix, or simply
    // looking at system user details if mailboxes are system accounts.
    // Real-world mail server management often involves specific APIs or more complex commands.
    // For simplicity, this simulates using 'id' command to check if user exists (implies mailbox existence)
    // and a mock command for mail statistics.

    public async Task<string> CheckMailboxStatusAsync(string mailboxName)
    {
        if (string.IsNullOrWhiteSpace(mailboxName))
        {
            return "Error: Mailbox name cannot be empty.";
        }

        string command = "";
        string arguments = "";
        string result = "";

        if (OperatingSystem.IsLinux() || OperatingSystem.IsMacOS())
        {
            // Simulate checking if a system user (often corresponds to a mailbox) exists
            command = "id";
            arguments = $"-u \"{mailboxName}\""; // -u to just get UID, implies existence if successful
        }
        else if (OperatingSystem.IsWindows())
        {
            // On Windows, mail servers like Exchange would have specific PowerShell cmdlets.
            // This is a placeholder for demonstration purposes.
            return "Mailbox status check on Windows is not directly supported by this example (requires specific mail server commands/APIs).";
        }
        else
        {
            return "Unsupported operating system for mail server commands.";
        }

        try
        {
            ProcessStartInfo startInfo = new ProcessStartInfo
            {
                FileName = command,
                Arguments = arguments,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };

            using (Process process = new Process { StartInfo = startInfo })
            {
                process.Start();
                string output = await process.StandardOutput.ReadToEndAsync();
                string error = await process.StandardError.ReadToEndAsync();
                process.WaitForExit();

                if (process.ExitCode == 0)
                {
                    result += $"Mailbox '{mailboxName}' exists (User ID: {output.Trim()}).{Environment.NewLine}";
                    result += "Attempting to retrieve simulated mail traffic info... " + Environment.NewLine;
                    // Simulate mail traffic analysis (e.g., calling another internal method or mock command)
                    result += await GetSimulatedMailTrafficAsync(mailboxName);
                }
                else
                {
                    result += $"Mailbox '{mailboxName}' does not exist or cannot be accessed. Error: {error.Trim()}";
                }
            }
        }
        catch (System.ComponentModel.Win32Exception ex) when (ex.NativeErrorCode == 2)
        {
            result = $"Error: Command '{command}' not found. Ensure mail server management tools are installed and in PATH.";
        }
        catch (Exception ex)
        {
            result = $"An unexpected error occurred: {ex.Message}";
        }
        return result;
    }

    private async Task<string> GetSimulatedMailTrafficAsync(string mailboxName)
    {
        // In a real scenario, this would execute commands like 'doveadm stats' or analyze mail logs.
        // For demonstration, we'll return a static simulated response.
        await Task.Delay(500); // Simulate some processing time
        return $"Simulated mail traffic for '{mailboxName}':{Environment.NewLine}" +
               $"- Incoming emails last 24h: 15{Environment.NewLine}" +
               $"- Outgoing emails last 24h: 8{Environment.NewLine}" +
               $"- Current mailbox size: 1.2 GB{Environment.NewLine}" +
               $"- Last login: 2025-06-21 10:30:00";
    }
}

// Example usage:
// [HttpGet("check-mailbox-status")]
// public async Task<IActionResult> CheckMailboxStatus(string mailboxName)
// {
//     MailServerManager manager = new MailServerManager();
//     string status = await manager.CheckMailboxStatusAsync(mailboxName);
//     if (status.StartsWith("Error"))
//     {
//         return BadRequest(status);
//     }
//     return Ok(status);
// }
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 60
```python
import subprocess
import platform
import time

def check_mailbox_status(mailbox_name):
    """
    Checks the status of a mail user/mailbox using system commands.
    This example uses 'id' to check if a system user exists (common for mailboxes).
    For actual mail server management (e.g., Postfix, Dovecot, Exchange),
    you would use their specific command-line tools or APIs.
    Args:
        mailbox_name (str): The name of the mailbox (e.g., 'john.doe').
    Returns:
        str: A report on the mailbox status and simulated traffic.
    """
    if not mailbox_name:
        return "Error: Mailbox name cannot be empty."

    command = []
    if platform.system() == "Linux" or platform.system() == "Darwin":
        # Check if user exists (often maps to mailbox)
        command = ["id", "-u", mailbox_name]
    else:
        return "Unsupported operating system for direct mail system command checks in this example."

    report = ""
    try:
        process = subprocess.run(command, capture_output=True, text=True, check=False)
        stdout = process.stdout.strip()
        stderr = process.stderr.strip()

        if process.returncode == 0:
            report += f"Mailbox '{mailbox_name}' exists (System User ID: {stdout}).\n"
            report += "Retrieving simulated mail traffic information...\n"
            # Simulate fetching mail traffic details
            report += get_simulated_mail_traffic(mailbox_name)
        else:
            report += f"Mailbox '{mailbox_name}' does not exist or is not a system user. Error: {stderr}"

    except FileNotFoundError:
        report = f"Error: Command '{command[0]}' not found. Ensure mail system tools are installed and in PATH."
    except Exception as e:
        report = f"An unexpected error occurred: {e}"

    return report

def get_simulated_mail_traffic(mailbox_name):
    """
    Simulates retrieving mail traffic data for a given mailbox.
    In a real system, this would involve parsing mail logs or calling specific mail server APIs.
    """
    time.sleep(0.5) # Simulate some delay
    return (f"Simulated mail traffic for '{mailbox_name}':\n"
            f"- Incoming emails last 24h: 25\n"
            f"- Outgoing emails last 24h: 12\n"
            f"- Current mailbox size: 2.5 GB\n"
            f"- Last activity: 2025-06-21 11:45:00\n")

# Example usage:
# if __name__ == "__main__":
#     # For a web application, 'mailbox_name' would come from user input
#     mailbox1_status = check_mailbox_status("testuser")
#     print(mailbox1_status)
#
#     print("\n" + "="*30 + "\n")
#
#     mailbox2_status = check_mailbox_status("nonexistent_user")
#     print(mailbox2_status)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 76
```typescript
import { exec } from 'child_process';
import * as os from 'os';

/**
 * Checks the status of a mail user/mailbox using system commands.
 * This example simulates checking if a system user (which often corresponds to a mailbox) exists.
 * For actual mail server management (e.g., Postfix, Dovecot, Exchange),
 * you would need to execute their specific command-line tools or interact with their APIs.
 * @param mailboxName The name of the mailbox (e.g., 'info@example.com' or 'john_doe').
 * @returns A promise that resolves to a report string about the mailbox status.
 */
function checkMailboxStatus(mailboxName: string): Promise<string> {
    return new Promise((resolve, reject) => {
        if (!mailboxName) {
            return resolve("Error: Mailbox name cannot be empty.");
        }

        let command: string;
        if (os.platform() === 'linux' || os.platform() === 'darwin') {
            // Check if a system user with this name exists (common for mailboxes on Linux systems)
            command = `id -u "${mailboxName}"`;
        } else {
            return resolve("Error: Unsupported operating system for direct mail system command checks in this example.");
        }

        exec(command, async (error, stdout, stderr) => {
            if (error) {
                // Command failed, likely because user/mailbox does not exist
                if (stderr.includes("no such user")) {
                    resolve(`Mailbox '${mailboxName}' does not exist or is not a system user.`);
                } else {
                    console.error(`exec error: ${error.message}`);
                    reject(new Error(`Failed to check mailbox status: ${stderr || error.message}`));
                }
                return;
            }
            if (stderr) {
                console.warn(`Command stderr: ${stderr}`);
            }

            let report = `Mailbox '${mailboxName}' exists (System User ID: ${stdout.trim()}).\n`;
            report += "Retrieving simulated mail traffic information...\n";
            report += await getSimulatedMailTraffic(mailboxName); // Simulate fetching traffic data
            resolve(report);
        });
    });
}

/**
 * Simulates retrieving mail traffic data for a given mailbox.
 * In a real-world application, this would involve parsing mail server logs or using specific APIs.
 * @param mailboxName The name of the mailbox.
 * @returns A promise that resolves to a string with simulated mail traffic details.
 */
async function getSimulatedMailTraffic(mailboxName: string): Promise<string> {
    // Simulate an asynchronous operation
    await new Promise(resolve => setTimeout(resolve, 500));

    return (
        `Simulated mail traffic for '${mailboxName}':\n` +
        `- Incoming emails last 24h: 30\n` +
        `- Outgoing emails last 24h: 15\n` +
        `- Current mailbox size: 3.1 GB\n` +
        `- Last activity: ${new Date().toLocaleString()}\n`
    );
}

// Example usage:
// (async () => {
//     try {
//         const mailboxName1 = 'daemon'; // A common system user on Linux
//         const status1 = await checkMailboxStatus(mailboxName1);
//         console.log(status1);
//
//         console.log('\n' + '='.repeat(30) + '\n');
//
//         const mailboxName2 = 'nonexistent_mail_user';
//         const status2 = await checkMailboxStatus(mailboxName2);
//         console.log(status2);
//     } catch (e) {
//         console.error('An error occurred:', e);
//     }
// })();
```

### 🧪 Senaryo 10: Bir web sunucu log analiz uygulamasında kullanıcılar tarih aralığı girip log verilerini filtreleyebilir. Sistem girilen tarihleri kullanarak filtreleme komutları çalıştırır. Filtrelenmiş loglar kullanıcıya sunulur. Analiz raporları oluşturulur.

**💻 Dil:** `C#`
**🤖 AI:** Gemini
**Satır Sayısı:** 136
```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

public class WebServerLogAnalyzer
{
    // This example performs in-memory filtering. For very large log files,
    // it's more efficient to use external tools like 'grep', 'awk', or log parsing libraries
    // that can handle streams or indexed logs.
    public async Task<List<string>> FilterLogsByDateRangeAsync(
        string logFilePath, DateTime startDate, DateTime endDate, string logDateTimeFormat = "dd/MMM/yyyy:HH:mm:ss")
    {
        List<string> filteredLogs = new List<string>();

        if (!File.Exists(logFilePath))
        {
            Console.WriteLine($"Error: Log file not found: {logFilePath}");
            return filteredLogs;
        }

        // Regex to extract date/time from common Apache/Nginx combined log format:
        // [DD/Mon/YYYY:HH:MM:SS +ZZZZ]
        // This regex targets the date and time part specifically.
        string dateTimePattern = @"\[(\d{2}\/[A-Za-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2}) \+\d{4}\]";
        Regex regex = new Regex(dateTimePattern);

        try
        {
            // Read all lines asynchronously. For very large files, consider stream reading.
            string[] allLines = await File.ReadAllLinesAsync(logFilePath);

            await Task.Run(() =>
            {
                foreach (string line in allLines)
                {
                    Match match = regex.Match(line);
                    if (match.Success)
                    {
                        string datePart = match.Groups[1].Value;
                        // Example: "21/Jun/2025:12:30:00"
                        // Note: C# DateTime.ParseExact might need culture info for month names like "Jun".
                        // For robustness, consider parsing manually or using a library.
                        // Simplified parsing for common English month abbreviations.
                        DateTime logEntryDate;
                        try
                        {
                            // Convert month abbreviation to number for reliable parsing
                            string correctedDatePart = Regex.Replace(datePart, @"Jan", "01")
                                                             .Replace("Feb", "02")
                                                             .Replace("Mar", "03")
                                                             .Replace("Apr", "04")
                                                             .Replace("May", "05")
                                                             .Replace("Jun", "06")
                                                             .Replace("Jul", "07")
                                                             .Replace("Aug", "08")
                                                             .Replace("Sep", "09")
                                                             .Replace("Oct", "10")
                                                             .Replace("Nov", "11")
                                                             .Replace("Dec", "12");

                            // Now parse with numerical month
                            logEntryDate = DateTime.ParseExact(
                                correctedDatePart,
                                "dd/MM/yyyy:HH:mm:ss",
                                System.Globalization.CultureInfo.InvariantCulture
                            );
                        }
                        catch (FormatException)
                        {
                            Console.WriteLine($"Warning: Could not parse date from log line: {line}");
                            continue; // Skip line if date parsing fails
                        }

                        if (logEntryDate >= startDate && logEntryDate <= endDate)
                        {
                            filteredLogs.Add(line);
                        }
                    }
                }
            });
        }
        catch (UnauthorizedAccessException ex)
        {
            Console.WriteLine($"Access denied to log file: {ex.Message}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred during log filtering: {ex.Message}");
        }
        return filteredLogs;
    }

    public string GenerateAnalysisReport(List<string> logs)
    {
        if (logs == null || !logs.Any())
        {
            return "No logs to analyze.";
        }

        string report = $"--- Log Analysis Report ({logs.Count} entries) ---{Environment.NewLine}";

        // Example analysis: count status codes
        var statusCodes = logs.Select(line =>
        {
            var match = Regex.Match(line, @" (\d{3}) "); // Common pattern for status code like " 200 "
            return match.Success ? match.Groups[1].Value : "N/A";
        }).GroupBy(code => code)
          .ToDictionary(g => g.Key, g => g.Count());

        report += "HTTP Status Code Distribution:" + Environment.NewLine;
        foreach (var entry in statusCodes.OrderByDescending(kv => kv.Value))
        {
            report += $"  {entry.Key}: {entry.Value} times{Environment.NewLine}";
        }

        // Example analysis: count requests by IP
        var ipAddresses = logs.Select(line =>
        {
            var match = Regex.Match(line, @"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) "); // IP at start of line
            return match.Success ? match.Groups[1].Value : "N/A";
        }).GroupBy(ip => ip)
          .ToDictionary(g => g.Key, g => g.Count());

        report += Environment.NewLine + "Top 5 Requesting IP Addresses:" + Environment.NewLine;
        foreach (var entry in ipAddresses.OrderByDescending(kv => kv.Value).Take(5))
        {
            report += $"  {entry.Key}: {entry.Value} requests{Environment.NewLine}";
        }

        return report;
    }
}

// Example usage:
// [HttpGet("analyze-web-logs")]
// public async Task<IActionResult> AnalyzeWebLogs(string logFile, DateTime startDate, DateTime endDate)
// {
//     WebServerLogAnalyzer analyzer = new WebServerLogAnalyzer();
//     List<string> filteredLogs = await analyzer.FilterLogsByDateRangeAsync(logFile, startDate, endDate);
//
//     if (!filteredLogs.Any())
//     {
//         return NotFound("No log entries found for the specified date range.");
//     }
//
//     string analysisReport = analyzer.GenerateAnalysisReport(filteredLogs);
//     return Ok(new { FilteredLogs = filteredLogs, AnalysisReport = analysisReport });
// }
```

**💻 Dil:** `Python`
**🤖 AI:** Gemini
**Satır Sayısı:** 131
```python
import re
import datetime
import os

def parse_apache_log_time(time_str):
    """
    Parses a timestamp string from Apache/Nginx combined log format.
    Example: "21/Jun/2025:12:30:00"
    """
    # Map month abbreviations to numbers
    month_map = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }
    parts = re.match(r"(\d{2})/([A-Za-z]{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2})", time_str)
    if parts:
        day, month_abbr, year, hour, minute, second = parts.groups()
        month_num = month_map.get(month_abbr, 1) # Default to 1 if not found
        return datetime.datetime(int(year), month_num, int(day), int(hour), int(minute), int(second))
    return None

def filter_web_server_logs_by_date(log_file_path, start_date_str, end_date_str):
    """
    Filters web server log entries by a specified date range.
    Assumes log entries contain a timestamp in Apache/Nginx combined log format.
    Args:
        log_file_path (str): Path to the web server log file.
        start_date_str (str): Start date in YYYY-MM-DD format.
        end_date_str (str): End date in YYYY-MM-DD format.
    Returns:
        list: A list of filtered log lines.
    """
    filtered_logs = []
    if not os.path.exists(log_file_path):
        print(f"Error: Log file not found: {log_file_path}")
        return filtered_logs

    try:
        start_date = datetime.datetime.strptime(start_date_str + " 00:00:00", "%Y-%m-%d %H:%M:%S")
        end_date = datetime.datetime.strptime(end_date_str + " 23:59:59", "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        return filtered_logs

    # Regex to extract the full timestamp string from the log line
    # e.g., [21/Jun/2025:12:30:00 +0300]
    log_time_pattern = re.compile(r'\[(\d{2}\/[A-Za-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2}) \+\d{4}\]')

    try:
        with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                match = log_time_pattern.search(line)
                if match:
                    log_time_str = match.group(1)
                    log_entry_datetime = parse_apache_log_time(log_time_str)
                    if log_entry_datetime and start_date <= log_entry_datetime <= end_date:
                        filtered_logs.append(line.strip())
    except FileNotFoundError:
        print(f"Error: Log file not found at {log_file_path}")
    except Exception as e:
        print(f"An error occurred during log filtering: {e}")

    return filtered_logs

def generate_log_analysis_report(filtered_logs):
    """
    Generates a basic analysis report from filtered web server logs.
    Args:
        filtered_logs (list): A list of log lines.
    Returns:
        str: A formatted analysis report.
    """
    if not filtered_logs:
        return "No logs to analyze for report."

    report = f"--- Web Server Log Analysis Report ({len(filtered_logs)} entries) ---\n"

    # Example 1: HTTP Status Code Distribution
    status_code_counts = {}
    status_code_pattern = re.compile(r' (\d{3}) ') # Matches " 200 ", " 404 ", etc.

    for line in filtered_logs:
        match = status_code_pattern.search(line)
        if match:
            code = match.group(1)
            status_code_counts[code] = status_code_counts.get(code, 0) + 1

    report += "\nHTTP Status Code Distribution:\n"
    for code, count in sorted(status_code_counts.items(), key=lambda item: item[1], reverse=True):
        report += f"  {code}: {count} times\n"

    # Example 2: Top Requesting IP Addresses
    ip_address_counts = {}
    ip_pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) ') # IP at the start of the line

    for line in filtered_logs:
        match = ip_pattern.match(line)
        if match:
            ip = match.group(1)
            ip_address_counts[ip] = ip_address_counts.get(ip, 0) + 1

    report += "\nTop 5 Requesting IP Addresses:\n"
    sorted_ips = sorted(ip_address_counts.items(), key=lambda item: item[1], reverse=True)
    for ip, count in sorted_ips[:5]:
        report += f"  {ip}: {count} requests\n"

    return report

# Example usage:
# if __name__ == "__main__":
#     # For a web application, these inputs would come from a web form
#     log_file = "access.log" # Replace with your actual log file path
#
#     # Create a dummy log file for testing if it doesn't exist
#     if not os.path.exists(log_file):
#         print(f"Creating dummy log file: {log_file}")
#         dummy_content = """
# 192.168.1.1 - - [21/Jun/2025:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234
# 192.168.1.2 - - [21/Jun/2025:10:05:30 +0000] "GET /images/logo.png HTTP/1.1" 200 5678
# 192.168.1.1 - - [21/Jun/2025:10:10:15 +0000] "POST /submit_form HTTP/1.1" 200 100
# 192.168.1.3 - - [21/Jun/2025:11:00:00 +0000] "GET /admin HTTP/1.1" 401 200
# 192.168.1.4 - - [21/Jun/2025:11:30:45 +0000] "GET /nonexistent HTTP/1.1" 404 150
# 192.168.1.1 - - [22/Jun/2025:09:00:00 +0000] "GET /about.html HTTP/1.1" 200 800
# """
#         with open(log_file, "w") as f:
#             f.write(dummy_content.strip())
#         print("Dummy log file created. Using it for analysis.")
#
#     start_date = "2025-06-21"
#     end_date = "2025-06-21"
#
#     print(f"Filtering logs from {start_date} to {end_date}...")
#     filtered_results = filter_web_server_logs_by_date(log_file, start_date, end_date)
#
#     if filtered_results:
#         print("\nFiltered Log Entries:")
#         for entry in filtered_results:
#             print(entry)
#
#         analysis_report = generate_log_analysis_report(filtered_results)
#         print("\n" + analysis_report)
#     else:
#         print("No log entries found for the specified date range.")
#
#     # Clean up dummy file
#     # if os.path.exists(log_file) and "dummy video file content" not in open(log_file).read(): # Check if it's our dummy
#     #     os.remove(log_file)
```

**💻 Dil:** `TypeScript`
**🤖 AI:** Gemini
**Satır Sayısı:** 163
```typescript
import * as fs from 'fs';
import * as readline from 'readline';
import * as path from 'path';

/**
 * Parses an Apache/Nginx combined log format timestamp string into a Date object.
 * Example: "21/Jun/2025:12:30:00"
 * @param timeStr The timestamp string from the log.
 * @returns A Date object or null if parsing fails.
 */
function parseLogTimestamp(timeStr: string): Date | null {
    const monthMap: { [key: string]: number } = {
        'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'Jun': 5,
        'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11
    };

    const match = timeStr.match(/^(\d{2})\/([A-Za-z]{3})\/(\d{4}):(\d{2}):(\d{2}):(\d{2})$/);
    if (match) {
        const [, day, monthAbbr, year, hour, minute, second] = match;
        const month = monthMap[monthAbbr];
        if (month !== undefined) {
            return new Date(parseInt(year), month, parseInt(day), parseInt(hour), parseInt(minute), parseInt(second));
        }
    }
    return null;
}

/**
 * Filters web server log entries by a specified date range.
 * This function reads the log file line by line for efficiency with large files.
 * @param logFilePath The path to the web server log file.
 * @param startDateStr Start date in YYYY-MM-DD format.
 * @param endDateStr End date in YYYY-MM-DD format.
 * @returns A promise that resolves to an array of filtered log lines.
 */
function filterWebServerLogsByDate(logFilePath: string, startDateStr: string, endDateStr: string): Promise<string[]> {
    return new Promise(async (resolve, reject) => {
        if (!fs.existsSync(logFilePath)) {
            return resolve([]); // File not found, return empty array
        }

        let startDate: Date;
        let endDate: Date;
        try {
            startDate = new Date(startDateStr + 'T00:00:00');
            endDate = new Date(endDateStr + 'T23:59:59');
            if (isNaN(startDate.getTime()) || isNaN(endDate.getTime())) {
                return reject(new Error("Invalid date format. Please use YYYY-MM-DD."));
            }
        } catch (e) {
            return reject(new Error(`Error parsing dates: ${e}`));
        }

        const filteredLogs: string[] = [];
        const fileStream = fs.createReadStream(logFilePath);
        const rl = readline.createInterface({
            input: fileStream,
            crlfDelay: Infinity
        });

        // Regex to extract the timestamp part from common Apache/Nginx log format:
        // Example: [21/Jun/2025:12:30:00 +0000]
        const logTimestampRegex = /\[(\d{2}\/[A-Za-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2}) \+\d{4}\]/;

        rl.on('line', (line) => {
            const match = line.match(logTimestampRegex);
            if (match) {
                const timestampStr = match[1];
                const logEntryDate = parseLogTimestamp(timestampStr);

                if (logEntryDate && logEntryDate >= startDate && logEntryDate <= endDate) {
                    filteredLogs.push(line);
                }
            }
        });

        rl.on('close', () => {
            resolve(filteredLogs);
        });

        rl.on('error', (err) => {
            reject(new Error(`Error reading log file: ${err.message}`));
        });
    });
}

/**
 * Generates a basic analysis report from filtered web server logs.
 * @param filteredLogs An array of log lines.
 * @returns A formatted analysis report string.
 */
function generateLogAnalysisReport(filteredLogs: string[]): string {
    if (filteredLogs.length === 0) {
        return "No logs to analyze for report.";
    }

    let report = `--- Web Server Log Analysis Report (${filteredLogs.length} entries) ---\n`;

    // 1. HTTP Status Code Distribution
    const statusCodeCounts: { [key: string]: number } = {};
    const statusCodeRegex = / (\d{3}) /; // Matches " 200 ", " 404 "

    for (const line of filteredLogs) {
        const match = line.match(statusCodeRegex);
        if (match) {
            const code = match[1];
            statusCodeCounts[code] = (statusCodeCounts[code] || 0) + 1;
        }
    }

    report += "\nHTTP Status Code Distribution:\n";
    Object.entries(statusCodeCounts)
        .sort(([, countA], [, countB]) => countB - countA) // Sort descending by count
        .forEach(([code, count]) => {
            report += `  ${code}: ${count} times\n`;
        });

    // 2. Top Requesting IP Addresses
    const ipAddressCounts: { [key: string]: number } = {};
    const ipAddressRegex = /^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) /; // IP at the start of the line

    for (const line of filteredLogs) {
        const match = line.match(ipAddressRegex);
        if (match) {
            const ip = match[1];
            ipAddressCounts[ip] = (ipAddressCounts[ip] || 0) + 1;
        }
    }

    report += "\nTop 5 Requesting IP Addresses:\n";
    Object.entries(ipAddressCounts)
        .sort(([, countA], [, countB]) => countB - countA)
        .slice(0, 5) // Take top 5
        .forEach(([ip, count]) => {
            report += `  ${ip}: ${count} requests\n`;
        });

    return report;
}

// Example usage:
// (async () => {
//     const logFilePath = path.join(__dirname, 'access.log'); // Adjust path as needed
//     const startDate = '2025-06-21';
//     const endDate = '2025-06-21';
//
//     // Create a dummy log file for testing if it doesn't exist
//     if (!fs.existsSync(logFilePath)) {
//         console.log(`Creating dummy log file: ${logFilePath}`);
//         const dummyContent = `
// 192.168.1.1 - - [21/Jun/2025:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234 "-" "Mozilla/5.0"
// 192.168.1.2 - - [21/Jun/2025:10:05:30 +0000] "GET /images/logo.png HTTP/1.1" 200 5678 "-" "Chrome/90.0"
// 192.168.1.1 - - [21/Jun/2025:10:10:15 +0000] "POST /submit_form HTTP/1.1" 200 100 "-" "Firefox/88.0"
// 192.168.1.3 - - [21/Jun/2025:11:00:00 +0000] "GET /admin HTTP/1.1" 401 200 "-" "Safari/14.0"
// 192.168.1.4 - - [21/Jun/2025:11:30:45 +0000] "GET /nonexistent HTTP/1.1" 404 150 "-" "Edge/90.0"
// 192.168.1.1 - - [22/Jun/2025:09:00:00 +0000] "GET /about.html HTTP/1.1" 200 800 "-" "Mozilla/5.0"
//         `;
//         fs.writeFileSync(logFilePath, dummyContent.trim());
//         console.log("Dummy log file created. Using it for analysis.");
//     }
//
//     try {
//         console.log(`Filtering logs from ${startDate} to ${endDate}...`);
//         const filteredLogs = await filterWebServerLogsByDate(logFilePath, startDate, endDate);
//
//         if (filteredLogs.length > 0) {
//             console.log("\nFiltered Log Entries:");
//             filteredLogs.forEach(line => console.log(line));
//
//             const analysisReport = generateLogAnalysisReport(filteredLogs);
//             console.log("\n" + analysisReport);
//         } else {
//             console.log("No log entries found for the specified date range.");
//         }
//     } catch (e: any) {
//         console.error('An error occurred during log analysis:', e.message);
//     } finally {
//         // Clean up dummy file if it was created for this example
//         // if (fs.existsSync(logFilePath) && fs.readFileSync(logFilePath, 'utf8').includes('dummy video content')) {
//         //     fs.unlinkSync(logFilePath);
//         // }
//     }
// })();
```