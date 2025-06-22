 
Markdown

----

### 🧪 Senaryo 1: Bir sistem yönetim panelinde kullanıcılar disk kullanım raporu alabilir. Kullanıcı dizin yolu girdiğinde sistem bu bilgiyi kullanarak analiz yapar. Disk kullanım istatistikleri kullanıcıya gösterilir. Rapor çeşitli formatlarda indirilebilir.
**💻 Dil:** `C#`  
**🤖 AI:** Gemini

```csharp
using System;
using System.IO;
using System.Linq;
using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class DiskUsageController : ControllerBase
{
    [HttpGet("report")]
    public IActionResult GetDiskUsageReport([FromQuery] string directoryPath)
    {
        if (string.IsNullOrWhiteSpace(directoryPath))
        {
            return BadRequest("Directory path cannot be empty.");
        }

        if (!Directory.Exists(directoryPath))
        {
            return NotFound($"Directory not found: {directoryPath}");
        }

        try
        {
            var directoryInfo = new DirectoryInfo(directoryPath);
            long totalSize = directoryInfo.EnumerateFiles("*", SearchOption.AllDirectories).Sum(file => file.Length);

            var report = new
            {
                DirectoryPath = directoryPath,
                TotalSizeInBytes = totalSize,
                TotalSizeFormatted = FormatBytes(totalSize),
                FilesCount = directoryInfo.EnumerateFiles("*", SearchOption.AllDirectories).Count(),
                SubDirectoriesCount = directoryInfo.EnumerateDirectories("*", SearchOption.AllDirectories).Count()
            };

            return Ok(report);
        }
        catch (UnauthorizedAccessException)
        {
            return Forbid("Access to the specified directory is denied.");
        }
        catch (Exception ex)
        {
            return StatusCode(500, <span class="math-inline">"An error occurred while generating the report\: \{ex\.Message\}"\);
\}
\}
\[HttpGet\("download\-report"\)\]
public IActionResult DownloadDiskUsageReport\(\[FromQuery\] string directoryPath, \[FromQuery\] string format \= "json"\)
\{
if \(string\.IsNullOrWhiteSpace\(directoryPath\)\)
\{
return BadRequest\("Directory path cannot be empty\."\);
\}
if \(\!Directory\.Exists\(directoryPath\)\)
\{
return NotFound\(</span>"Directory not found: {directoryPath}");
        }

        try
        {
            var directoryInfo = new DirectoryInfo(directoryPath);
            long totalSize = directoryInfo.EnumerateFiles("*", SearchOption.AllDirectories).Sum(file => file.Length);

            var reportData = new
            {
                DirectoryPath = directoryPath,
                TotalSizeInBytes = totalSize,
                TotalSizeFormatted = FormatBytes(totalSize),
                FilesCount = directoryInfo.EnumerateFiles("*", SearchOption.AllDirectories).Count(),
                SubDirectoriesCount = directoryInfo.EnumerateDirectories("*", SearchOption.AllDirectories).Count()
            };

            string fileName = $"disk_usage_report_{DateTime.Now:yyyyMMddHHmmss}";
            byte[] fileBytes;
            string contentType;

            switch (format.ToLower())
            {
                case "json":
                    fileBytes = System.Text.Json.JsonSerializer.SerializeToUtf8Bytes(reportData, new System.Text.Json.JsonSerializerOptions { WriteIndented = true });
                    contentType = "application/json";
                    fileName += ".json";
                    break;
                case "csv":
                    var csvContent = $"Directory Path,Total Size (Bytes),Total Size,Files Count,Subdirectories Count\n";
                    csvContent += $"{directoryPath},{totalSize},{FormatBytes(totalSize)},{reportData.FilesCount},{reportData.SubDirectoriesCount}";
                    fileBytes = System.Text.Encoding.UTF8.GetBytes(csvContent);
                    contentType = "text/csv";
                    fileName += ".csv";
                    break;
                default:
                    return BadRequest("Unsupported report format. Supported formats are: json, csv.");
            }

            return File(fileBytes, contentType, fileName);
        }
        catch (UnauthorizedAccessException)
        {
            return Forbid("Access to the specified directory is denied.");
        }
        catch (Exception ex)
        {
            return StatusCode(500, $"An error occurred while generating the downloadable report: {ex.Message}");
        }
    }

    private string FormatBytes(long bytes)
    {
        string[] Suffix = { "B", "KB", "MB", "GB", "TB" };
        int i = 0;
        double dblSByte = bytes;
        while (Math.Round(dblSByte / 1024) >= 1)
        {
            dblSByte /= 1024;
            i++;
        }
        return string.Format("{0:n1} {1}", dblSByte, Suffix[i]);
    }
}
💻 Dil: Python

🤖 AI: Gemini

Python

import os
import json
import csv
from flask import Flask, request, jsonify, send_file
from io import StringIO

app = Flask(__name__)

def get_directory_size(path):
    total_size = 0
    try:
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
    except FileNotFoundError:
        raise
    except PermissionError:
        raise
    except Exception as e:
        raise
    return total_size

def format_bytes(bytes_value):
    suffix = ("B", "KB", "MB", "GB", "TB")
    i = 0
    dbl_s_byte = bytes_value
    while round(dbl_s_byte / 1024) >= 1:
        dbl_s_byte /= 1024
        i += 1
    return f"{dbl_s_byte:.1f} {suffix[i]}"

@app.route('/api/disk-usage/report', methods=['GET'])
def get_disk_usage_report():
    directory_path = request.args.get('directoryPath')

    if not directory_path:
        return jsonify({"error": "Directory path cannot be empty."}), 400

    if not os.path.isdir(directory_path):
        return jsonify({"error": f"Directory not found: {directory_path}"}), 404

    try:
        total_size = get_directory_size(directory_path)
        files_count = sum([len(files) for r, d, files in os.walk(directory_path)])
        subdirectories_count = sum([len(d) for r, d, files in os.walk(directory_path)])

        report = {
            "directoryPath": directory_path,
            "totalSizeInBytes": total_size,
            "totalSizeFormatted": format_bytes(total_size),
            "filesCount": files_count,
            "subDirectoriesCount": subdirectories_count
        }
        return jsonify(report), 200
    except PermissionError:
        return jsonify({"error": "Access to the specified directory is denied."}), 403
    except Exception as e:
        return jsonify({"error": f"An error occurred while generating the report: {str(e)}"}), 500

@app.route('/api/disk-usage/download-report', methods=['GET'])
def download_disk_usage_report():
    directory_path = request.args.get('directoryPath')
    file_format = request.args.get('format', 'json')

    if not directory_path:
        return jsonify({"error": "Directory path cannot be empty."}), 400

    if not os.path.isdir(directory_path):
        return jsonify({"error": f"Directory not found: {directory_path}"}), 404

    try:
        total_size = get_directory_size(directory_path)
        files_count = sum([len(files) for r, d, files in os.walk(directory_path)])
        subdirectories_count = sum([len(d) for r, d, files in os.walk(directory_path)])

        report_data = {
            "directoryPath": directory_path,
            "totalSizeInBytes": total_size,
            "totalSizeFormatted": format_bytes(total_size),
            "filesCount": files_count,
            "subDirectoriesCount": subdirectories_count
        }

        file_name = f"disk_usage_report_{os.getpid()}" # Using pid for a unique name for demonstration

        if file_format.lower() == 'json':
            output = StringIO()
            json.dump(report_data, output, indent=4)
            output.seek(0)
            return send_file(
                StringIO(output.getvalue()),
                mimetype='application/json',
                as_attachment=True,
                download_name=f"{file_name}.json"
            )
        elif file_format.lower() == 'csv':
            output = StringIO()
            writer = csv.writer(output)
            writer.writerow(["Directory Path", "Total Size (Bytes)", "Total Size", "Files Count", "Subdirectories Count"])
            writer.writerow([directory_path, total_size, format_bytes(total_size), report_data['filesCount'], report_data['subDirectoriesCount']])
            output.seek(0)
            return send_file(
                StringIO(output.getvalue()),
                mimetype='text/csv',
                as_attachment=True,
                download_name=f"{file_name}.csv"
            )
        else:
            return jsonify({"error": "Unsupported report format. Supported formats are: json, csv."}), 400

    except PermissionError:
        return jsonify({"error": "Access to the specified directory is denied."}), 403
    except Exception as e:
        return jsonify({"error": f"An error occurred while generating the downloadable report: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
💻 Dil: TypeScript (Node.js)

🤖 AI: Gemini

TypeScript

import express, { Request, Response } from 'express';
import path from 'path';
import fs from 'fs';
import util from 'util';

const app = express();
const PORT = 3000;

// Promisify fs.readdir and fs.stat for async/await
const readdir = util.promisify(fs.readdir);
const stat = util.promisify(fs.stat);

async function getDirectorySize(directoryPath: string): Promise<number> {
    let totalSize = 0;
    const files = await readdir(directoryPath);

    for (const file of files) {
        const filePath = path.join(directoryPath, file);
        let stats;
        try {
            stats = await stat(filePath);
        } catch (error: any) {
            // Ignore permission errors or other errors for individual files/dirs
            if (error.code === 'EACCES') {
                console.warn(`Permission denied for: ${filePath}. Skipping.`);
                continue;
            }
            throw error; // Re-throw other unexpected errors
        }

        if (stats.isFile()) {
            totalSize += stats.size;
        } else if (stats.isDirectory()) {
            totalSize += await getDirectorySize(filePath); // Recursively get size of subdirectories
        }
    }
    return totalSize;
}

function formatBytes(bytes: number): string {
    const suffix = ["B", "KB", "MB", "GB", "TB"];
    let i = 0;
    let dblSByte = bytes;
    while (Math.round(dblSByte / 1024) >= 1) {
        dblSByte /= 1024;
        i++;
    }
    return `${dblSByte.toFixed(1)} ${suffix[i]}`;
}

app.get('/api/disk-usage/report', async (req: Request, res: Response) => {
    const directoryPath = req.query.directoryPath as string;

    if (!directoryPath) {
        return res.status(400).json({ error: "Directory path cannot be empty." });
    }

    if (!fs.existsSync(directoryPath)) {
        return res.status(404).json({ error: `Directory not found: ${directoryPath}` });
    }

    try {
        const totalSizeInBytes = await getDirectorySize(directoryPath);
        
        let filesCount = 0;
        let subDirectoriesCount = 0;
        
        // Walk the directory to count files and subdirectories
        const walk = async (currentPath: string) => {
            const items = await readdir(currentPath);
            for (const item of items) {
                const itemPath = path.join(currentPath, item);
                let itemStats;
                try {
                    itemStats = await stat(itemPath);
                } catch (error: any) {
                    if (error.code === 'EACCES') {
                        continue;
                    }
                    throw error;
                }

                if (itemStats.isFile()) {
                    filesCount++;
                } else if (itemStats.isDirectory()) {
                    subDirectoriesCount++;
                    await walk(itemPath); // Recurse into subdirectories
                }
            }
        };
        await walk(directoryPath);

        const report = {
            directoryPath: directoryPath,
            totalSizeInBytes: totalSizeInBytes,
            totalSizeFormatted: formatBytes(totalSizeInBytes),
            filesCount: filesCount,
            subDirectoriesCount: subDirectoriesCount
        };

        return res.status(200).json(report);
    } catch (error: any) {
        if (error.code === 'EACCES') {
            return res.status(403).json({ error: "Access to the specified directory is denied." });
        }
        return res.status(500).json({ error: `An error occurred while generating the report: ${error.message}` });
    }
});

app.get('/api/disk-usage/download-report', async (req: Request, res: Response) => {
    const directoryPath = req.query.directoryPath as string;
    const format = (req.query.format as string || 'json').toLowerCase();

    if (!directoryPath) {
        return res.status(400).json({ error: "Directory path cannot be empty." });
    }

    if (!fs.existsSync(directoryPath)) {
        return res.status(404).json({ error: `Directory not found: ${directoryPath}` });
    }

    try {
        const totalSizeInBytes = await getDirectorySize(directoryPath);
        
        let filesCount = 0;
        let subDirectoriesCount = 0;
        
        const walk = async (currentPath: string) => {
            const items = await readdir(currentPath);
            for (const item of items) {
                const itemPath = path.join(currentPath, item);
                let itemStats;
                try {
                    itemStats = await stat(itemPath);
                } catch (error: any) {
                    if (error.code === 'EACCES') {
                        continue;
                    }
                    throw error;
                }

                if (itemStats.isFile()) {
                    filesCount++;
                } else if (itemStats.isDirectory()) {
                    subDirectoriesCount++;
                    await walk(itemPath); 
                }
            }
        };
        await walk(directoryPath);

        const reportData = {
            directoryPath: directoryPath,
            totalSizeInBytes: totalSizeInBytes,
            totalSizeFormatted: formatBytes(totalSizeInBytes),
            filesCount: filesCount,
            subDirectoriesCount: subDirectoriesCount
        };

        const fileName = `disk_usage_report_${Date.now()}`;

        if (format === 'json') {
            res.setHeader('Content-Type', 'application/json');
            res.setHeader('Content-Disposition', `attachment; filename=${fileName}.json`);
            return res.status(200).send(JSON.stringify(reportData, null, 4));
        } else if (format === 'csv') {
            const csvContent = `Directory Path,Total Size (Bytes),Total Size,Files Count,Subdirectories Count\n` +
                               `${directoryPath},${totalSizeInBytes},${formatBytes(totalSizeInBytes)},${reportData.filesCount},${reportData.subDirectoriesCount}`;
            res.setHeader('Content-Type', 'text/csv');
            res.setHeader('Content-Disposition', `attachment; filename=${fileName}.csv`);
            return res.status(200).send(csvContent);
        } else {
            return res.status(400).json({ error: "Unsupported report format. Supported formats are: json, csv." });
        }

    } catch (error: any) {
        if (error.code === 'EACCES') {
            return res.status(403).json({ error: "Access to the specified directory is denied." });
        }
        return res.status(500).json({ error: `An error occurred while generating the downloadable report: ${error.message}` });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
🧪 Senaryo 2: Bir dosya işleme uygulamasında kullanıcılar dosya yolunu belirterek işlem başlatabilir. Sistem belirtilen dosyayı işleyerek sonuçları üretir. İşlenen dosyalar kullanıcıya sunulur. Çeşitli dosya formatları desteklenir.
💻 Dil: C#

🤖 AI: Gemini

C#

using System;
using System.IO;
using Microsoft.AspNetCore.Mvc;
using System.Text;
using System.Threading.Tasks;

[ApiController]
[Route("api/[controller]")]
public class FileProcessorController : ControllerBase
{
    private readonly string _processedFilesDirectory = "ProcessedFiles";

    public FileProcessorController()
    {
        Directory.CreateDirectory(_processedFilesDirectory);
    }

    [HttpPost("process")]
    public async Task<IActionResult> ProcessFile([FromForm] string filePath)
    {
        if (string.IsNullOrWhiteSpace(filePath))
        {
            return BadRequest("File path cannot be empty.");
        }

        if (!System.IO.File.Exists(filePath))
        {
            return NotFound($"File not found: {filePath}");
        }

        try
        {
            // Determine file type and perform a simulated processing
            string fileExtension = Path.GetExtension(filePath).ToLowerInvariant();
            string processedContent = string.Empty;
            string outputFileName = $"{Path.GetFileNameWithoutExtension(filePath)}_processed{fileExtension}";
            string outputPath = Path.Combine(_processedFilesDirectory, outputFileName);

            switch (fileExtension)
            {
                case ".txt":
                    string textContent = await System.IO.File.ReadAllTextAsync(filePath);
                    processedContent = $"Processed Text: {textContent.ToUpper()}"; // Example processing
                    await System.IO.File.WriteAllTextAsync(outputPath, processedContent);
                    break;
                case ".json":
                    string jsonContent = await System.IO.File.ReadAllTextAsync(filePath);
                    // In a real scenario, you'd parse, modify, then re-serialize JSON
                    processedContent = $"// Processed JSON:\n{jsonContent}";
                    await System.IO.File.WriteAllTextAsync(outputPath, processedContent);
                    break;
                case ".xml":
                    string xmlContent = await System.IO.File.ReadAllTextAsync(filePath);
                    // In a real scenario, you'd parse, modify, then re-serialize XML
                    processedContent = <span class="math-inline">"\\n\{xmlContent\}";
await System\.IO\.File\.WriteAllTextAsync\(outputPath, processedContent\);
break;
default\:
return BadRequest\(</span>"Unsupported file format: {fileExtension}.");
            }

            return Ok(new { message = $"File '{filePath}' processed successfully.", processedFilePath = outputPath });
        }
        catch (UnauthorizedAccessException)
        {
            return Forbid("Access to the specified file or directory is denied.");
        }
        catch (Exception ex)
        {
            return StatusCode(500, <span class="math-inline">"An error occurred during file processing\: \{ex\.Message\}"\);
\}
\}
\[HttpGet\("download\-processed\-file"\)\]
public IActionResult DownloadProcessedFile\(\[FromQuery\] string fileName\)
\{
if \(string\.IsNullOrWhiteSpace\(fileName\)\)
\{
return BadRequest\("File name cannot be empty\."\);
\}
string filePath \= Path\.Combine\(\_processedFilesDirectory, fileName\);
if \(\!System\.IO\.File\.Exists\(filePath\)\)
\{
return NotFound\(</span>"Processed file not found: {fileName}");
        }

        try
        {
            var fileBytes = System.IO.File.ReadAllBytes(filePath);
            string contentType = GetContentType(filePath); // Helper to determine content type
            return File(fileBytes, contentType, fileName);
        }
        catch (UnauthorizedAccessException)
        {
            return Forbid("Access to the processed file is denied.");
        }
        catch (Exception ex)
        {
            return StatusCode(500, $"An error occurred while downloading the processed file: {ex.Message}");
        }
    }

    private string GetContentType(string filePath)
    {
        string extension = Path.GetExtension(filePath).ToLowerInvariant();
        return extension switch
        {
            ".txt" => "text/plain",
            ".json" => "application/json",
            ".xml" => "application/xml",
            // Add more as needed
            _ => "application/octet-stream",
        };
    }
}
💻 Dil: Python

🤖 AI: Gemini

Python

import os
import json
import xml.etree.ElementTree as ET
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed_files'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def process_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    processed_content = f"Processed Text: {content.upper()}"
    return processed_content

def process_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Example processing: add a new key
    data['processed_status'] = 'completed'
    return json.dumps(data, indent=4)

def process_xml_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    # Example processing: add an attribute
    root.set("processed_by", "python_processor")
    return ET.tostring(root, encoding='utf-8').decode('utf-8')

@app.route('/api/file-processor/process', methods=['POST'])
def process_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request."}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file."}), 400

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        file_extension = os.path.splitext(filename)[1].lower()
        output_filename = f"{os.path.splitext(filename)[0]}_processed{file_extension}"
        output_path = os.path.join(app.config['PROCESSED_FOLDER'], output_filename)

        try:
            processed_content = None
            if file_extension == '.txt':
                processed_content = process_text_file(file_path)
            elif file_extension == '.json':
                processed_content = process_json_file(file_path)
            elif file_extension == '.xml':
                processed_content = process_xml_file(file_path)
            else:
                return jsonify({"error": f"Unsupported file format: {file_extension}."}), 400

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(processed_content)

            return jsonify({
                "message": f"File '{filename}' processed successfully.",
                "processedFilePath": output_path
            }), 200

        except PermissionError:
            return jsonify({"error": "Access to the specified file or directory is denied."}), 403
        except Exception as e:
            return jsonify({"error": f"An error occurred during file processing: {str(e)}"}), 500
    
    return jsonify({"error": "Failed to process file."}), 500

@app.route('/api/file-processor/download-processed-file', methods=['GET'])
def download_processed_file():
    file_name = request.args.get('fileName')
    if not file_name:
        return jsonify({"error": "File name cannot be empty."}), 400

    file_path = os.path.join(app.config['PROCESSED_FOLDER'], file_name)

    if not os.path.exists(file_path):
        return jsonify({"error": f"Processed file not found: {file_name}"}), 404

    try:
        return send_file(file_path, as_attachment=True, download_name=file_name)
    except PermissionError:
        return jsonify({"error": "Access to the processed file is denied."}), 403
    except Exception as e:
        return jsonify({"error": f"An error occurred while downloading the processed file: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
💻 Dil: TypeScript (Node.js)

🤖 AI: Gemini

TypeScript

import express, { Request, Response } from 'express';
import path from 'path';
import fs from 'fs/promises'; // Use promises-based fs for async/await
import multer from 'multer'; // For handling file uploads

const app = express();
const PORT = 3000;

const uploadDirectory = path.join(__dirname, 'uploads');
const processedFilesDirectory = path.join(__dirname, 'processed_files');

// Create upload and processed directories if they don't exist
fs.mkdir(uploadDirectory, { recursive: true }).catch(console.error);
fs.mkdir(processedFilesDirectory, { recursive: true }).catch(console.error);

// Set up multer for file uploads
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, uploadDirectory);
    },
    filename: (req, file, cb) => {
        cb(null, `${Date.now()}-${file.originalname}`);
    }
});
const upload = multer({ storage: storage });

async function processTextFile(filePath: string): Promise<string> {
    const content = await fs.readFile(filePath, 'utf-8');
    return `Processed Text: ${content.toUpperCase()}`;
}

async function processJsonFile(filePath: string): Promise<string> {
    const content = await fs.readFile(filePath, 'utf-8');
    const data = JSON.parse(content);
    // Example processing: add a new key
    data.processedStatus = 'completed';
    return JSON.stringify(data, null, 4);
}

async function processXmlFile(filePath: string): Promise<string> {
    const content = await fs.readFile(filePath, 'utf-8');
    // For real XML parsing/processing, you'd use a library like 'xml2js' or 'libxmljs'
    // This is a very basic simulation
    return `\n${content}`;
}

app.post('/api/file-processor/process', upload.single('file'), async (req: Request, res: Response) => {
    if (!req.file) {
        return res.status(400).json({ error: "No file uploaded." });
    }

    const filePath = req.file.path;
    const originalFileName = req.file.originalname;
    const fileExtension = path.extname(originalFileName).toLowerCase();
    const outputFileName = `${path.basename(originalFileName, fileExtension)}_processed${fileExtension}`;
    const outputPath = path.join(processedFilesDirectory, outputFileName);

    try {
        let processedContent: string;

        switch (fileExtension) {
            case '.txt':
                processedContent = await processTextFile(filePath);
                break;
            case '.json':
                processedContent = await processJsonFile(filePath);
                break;
            case '.xml':
                processedContent = await processXmlFile(filePath);
                break;
            default:
                await fs.unlink(filePath); // Clean up uploaded file if not supported
                return res.status(400).json({ error: `Unsupported file format: ${fileExtension}.` });
        }

        await fs.writeFile(outputPath, processedContent);
        await fs.unlink(filePath); // Delete the original uploaded file

        return res.status(200).json({
            message: `File '${originalFileName}' processed successfully.`,
            processedFilePath: outputPath,
            processedFileName: outputFileName
        });

    } catch (error: any) {
        // Clean up uploaded file in case of processing error
        await fs.unlink(filePath).catch(err => console.error("Error cleaning up uploaded file:", err)); 
        if (error.code === 'EACCES' || error.code === 'EPERM') {
            return res.status(403).json({ error: "Access to the specified file or directory is denied." });
        }
        return res.status(500).json({ error: `An error occurred during file processing: ${error.message}` });
    }
});

app.get('/api/file-processor/download-processed-file', async (req: Request, res: Response) => {
    const fileName = req.query.fileName as string;

    if (!fileName) {
        return res.status(400).json({ error: "File name cannot be empty." });
    }

    const filePath = path.join(processedFilesDirectory, fileName);

    try {
        await fs.access(filePath); // Check if file exists and is accessible
        return res.download(filePath, fileName, (err) => {
            if (err) {
                if (err.code === 'ENOENT') {
                    return res.status(404).json({ error: `Processed file not found: ${fileName}` });
                }
                if (err.code === 'EACCES' || err.code === 'EPERM') {
                    return res.status(403).json({ error: "Access to the processed file is denied." });
                }
                return res.status(500).json({ error: `An error occurred while downloading the processed file: ${err.message}` });
            }
        });
    } catch (error: any) {
        if (error.code === 'ENOENT') {
            return res.status(404).json({ error: `Processed file not found: ${fileName}` });
        }
        if (error.code === 'EACCES' || error.code === 'EPERM') {
            return res.status(403).json({ error: "Access to the processed file is denied." });
        }
        return res.status(500).json({ error: `An error occurred while accessing the file: ${error.message}` });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
🧪 Senaryo 3: Bir log görüntüleme aracında kullanıcılar log dosyası adını girip içeriğini görebilir. Sistem belirtilen dosyayı okuyarak içeriği kullanıcıya sunar. Log kayıtları filtrelenebilir ve aranabilir. Sonuçlar sayfalı olarak gösterilir.
💻 Dil: C#

🤖 AI: Gemini

C#

using System;
using System.IO;
using System.Linq;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Threading.Tasks;

[ApiController]
[Route("api/[controller]")]
public class LogViewerController : ControllerBase
{
    private readonly string _logDirectory = "Logs"; // Assuming logs are in a 'Logs' directory

    public LogViewerController()
    {
        Directory.CreateDirectory(_logDirectory); // Ensure log directory exists
        // Create some dummy log files for demonstration
        if (!System.IO.File.Exists(Path.Combine(_logDirectory, "app.log")))
        {
            System.IO.File.WriteAllLines(Path.Combine(_logDirectory, "app.log"), new string[]
            {
                "2023-01-01 10:00:01 INFO Application started.",
                "2023-01-01 10:00:05 DEBUG Processing user request for /dashboard.",
                "2023-01-01 10:00:10 WARNING Database connection lost. Retrying...",
                "2023-01-01 10:00:15 INFO User 'admin' logged in.",
                "2023-01-01 10:00:20 ERROR Failed to write to file 'report.txt': Access denied.",
                "2023-01-01 10:00:25 DEBUG Data fetched successfully.",
                "2023-01-01 10:00:30 INFO Report generation complete.",
                "2023-01-01 10:00:35 WARNING High CPU usage detected.",
                "2023-01-01 10:00:40 ERROR Invalid input received from user 'guest'."
            });
        }
        if (!System.IO.File.Exists(Path.Combine(_logDirectory, "auth.log")))
        {
            System.IO.File.WriteAllLines(Path.Combine(_logDirectory, "auth.log"), new string[]
            {
                "2023-01-01 11:00:01 INFO User 'testuser' authenticated successfully.",
                "2023-01-01 11:00:05 ERROR Failed login attempt for user 'baduser' from 192.168.1.100.",
                "2023-01-01 11:00:10 INFO User 'admin' changed password.",
                "2023-01-01 11:00:15 INFO Session for 'testuser' expired."
            });
        }
    }

    [HttpGet("view")]
    public async Task<IActionResult> ViewLog(
        [FromQuery] string logFileName,
        [FromQuery] string? filter = null,
        [FromQuery] string? search = null,
        [FromQuery] int page = 1,
        [FromQuery] int pageSize = 10)
    {
        if (string.IsNullOrWhiteSpace(logFileName))
        {
            return BadRequest("Log file name cannot be empty.");
        }

        string logFilePath = Path.Combine(_logDirectory, logFileName);

        if (!System.IO.File.Exists(logFilePath))
        {
            return NotFound($"Log file not found: {logFileName}");
        }

        try
        {
            var allLines = await System.IO.File.ReadAllLinesAsync(logFilePath);
            IEnumerable<string> filteredLines = allLines;

            if (!string.IsNullOrWhiteSpace(filter))
            {
                filteredLines = filteredLines.Where(line => line.Contains(filter, StringComparison.OrdinalIgnoreCase));
            }

            if (!string.IsNullOrWhiteSpace(search))
            {
                filteredLines = filteredLines.Where(line => line.Contains(search, StringComparison.OrdinalIgnoreCase));
            }

            // Pagination
            int totalRecords = filteredLines.Count();
            var pagedLines = filteredLines
                .Skip((page - 1) * pageSize)
                .Take(pageSize)
                .ToList();

            var result = new
            {
                LogFileName = logFileName,
                TotalRecords = totalRecords,
                Page = page,
                PageSize = pageSize,
                LogEntries = pagedLines
            };

            return Ok(result);
        }
        catch (UnauthorizedAccessException)
        {
            return Forbid("Access to the log file is denied.");
        }
        catch (Exception ex)
        {
            return StatusCode(500, $"An error occurred while reading the log file: {ex.Message}");
        }
    }
}
💻 Dil: Python

🤖 AI: Gemini

Python

import os
from flask import Flask, request, jsonify

app = Flask(__name__)

LOG_DIRECTORY = 'logs'
os.makedirs(LOG_DIRECTORY, exist_ok=True)

# Create some dummy log files for demonstration
if not os.path.exists(os.path.join(LOG_DIRECTORY, "app.log")):
    with open(os.path.join(LOG_DIRECTORY, "app.log"), "w") as f:
        f.write("2023-01-01 10:00:01 INFO Application started.\n")
        f.write("2023-01-01 10:00:05 DEBUG Processing user request for /dashboard.\n")
        f.write("2023-01-01 10:00:10 WARNING Database connection lost. Retrying...\n")
        f.write("2023-01-01 10:00:15 INFO User 'admin' logged in.\n")
        f.write("2023-01-01 10:00:20 ERROR Failed to write to file 'report.txt': Access denied.\n")
        f.write("2023-01-01 10:00:25 DEBUG Data fetched successfully.\n")
        f.write("2023-01-01 10:00:30 INFO Report generation complete.\n")
        f.write("2023-01-01 10:00:35 WARNING High CPU usage detected.\n")
        f.write("2023-01-01 10:00:40 ERROR Invalid input received from user 'guest'.\n")

if not os.path.exists(os.path.join(LOG_DIRECTORY, "auth.log")):
    with open(os.path.join(LOG_DIRECTORY, "auth.log"), "w") as f:
        f.write("2023-01-01 11:00:01 INFO User 'testuser' authenticated successfully.\n")
        f.write("2023-01-01 11:00:05 ERROR Failed login attempt for user 'baduser' from 192.168.1.100.\n")
        f.write("2023-01-01 11:00:10 INFO User 'admin' changed password.\n")
        f.write("2023-01-01 11:00:15 INFO Session for 'testuser' expired.\n")

@app.route('/api/log-viewer/view', methods=['GET'])
def view_log():
    log_file_name = request.args.get('logFileName')
    filter_param = request.args.get('filter')
    search_param = request.args.get('search')
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('pageSize', 10))

    if not log_file_name:
        return jsonify({"error": "Log file name cannot be empty."}), 400

    log_file_path = os.path.join(LOG_DIRECTORY, log_file_name)

    if not os.path.exists(log_file_path):
        return jsonify({"error": f"Log file not found: {log_file_name}"}), 404

    try:
        with open(log_file_path, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()
        
        filtered_lines = all_lines

        if filter_param:
            filtered_lines = [line for line in filtered_lines if filter_param.lower() in line.lower()]

        if search_param:
            filtered_lines = [line for line in filtered_lines if search_param.lower() in line.lower()]
        
        total_records = len(filtered_lines)
        
        # Pagination
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        paged_lines = filtered_lines[start_index:end_index]

        result = {
            "logFileName": log_file_name,
            "totalRecords": total_records,
            "page": page,
            "pageSize": page_size,
            "logEntries": [entry.strip() for entry in paged_lines]
        }
        return jsonify(result), 200

    except PermissionError:
        return jsonify({"error": "Access to the log file is denied."}), 403
    except Exception as e:
        return jsonify({"error": f"An error occurred while reading the log file: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
💻 Dil: TypeScript (Node.js)

🤖 AI: Gemini

TypeScript

import express, { Request, Response } from 'express';
import path from 'path';
import fs from 'fs/promises'; // Use promises-based fs for async/await

const app = express();
const PORT = 3000;

const logDirectory = path.join(__dirname, 'logs');

// Ensure log directory exists and create dummy logs for demonstration
async function setupLogDirectory() {
    await fs.mkdir(logDirectory, { recursive: true }).catch(console.error);

    const appLogPath = path.join(logDirectory, 'app.log');
    const authLogPath = path.join(logDirectory, 'auth.log');

    if (!await fs.access(appLogPath).then(() => true).catch(() => false)) {
        await fs.writeFile(appLogPath, `2023-01-01 10:00:01 INFO Application started.
2023-01-01 10:00:05 DEBUG Processing user request for /dashboard.
2023-01-01 10:00:10 WARNING Database connection lost. Retrying...
2023-01-01 10:00:15 INFO User 'admin' logged in.
2023-01-01 10:00:20 ERROR Failed to write to file 'report.txt': Access denied.
2023-01-01 10:00:25 DEBUG Data fetched successfully.
2023-01-01 10:00:30 INFO Report generation complete.
2023-01-01 10:00:35 WARNING High CPU usage detected.
2023-01-01 10:00:40 ERROR Invalid input received from user 'guest'.
`);
    }

    if (!await fs.access(authLogPath).then(() => true).catch(() => false)) {
        await fs.writeFile(authLogPath, `2023-01-01 11:00:01 INFO User 'testuser' authenticated successfully.
2023-01-01 11:00:05 ERROR Failed login attempt for user 'baduser' from 192.168.1.100.
2023-01-01 11:00:10 INFO User 'admin' changed password.
2023-01-01 11:00:15 INFO Session for 'testuser' expired.
`);
    }
}

setupLogDirectory(); // Call to set up the directory and dummy files

app.get('/api/log-viewer/view', async (req: Request, res: Response) => {
    const logFileName = req.query.logFileName as string;
    const filter = req.query.filter as string | undefined;
    const search = req.query.search as string | undefined;
    const page = parseInt(req.query.page as string) || 1;
    const pageSize = parseInt(req.query.pageSize as string) || 10;

    if (!logFileName) {
        return res.status(400).json({ error: "Log file name cannot be empty." });
    }

    const logFilePath = path.join(logDirectory, logFileName);

    try {
        await fs.access(logFilePath); // Check if file exists
        const fileContent = await fs.readFile(logFilePath, 'utf-8');
        let allLines = fileContent.split(/\r?\n/).filter(line => line.trim() !== ''); // Split by new line and remove empty lines

        let filteredLines = allLines;

        if (filter) {
            filteredLines = filteredLines.filter(line => line.toLowerCase().includes(filter.toLowerCase()));
        }

        if (search) {
            filteredLines = filteredLines.filter(line => line.toLowerCase().includes(search.toLowerCase()));
        }

        const totalRecords = filteredLines.length;
        const startIndex = (page - 1) * pageSize;
        const endIndex = startIndex + pageSize;
        const pagedLines = filteredLines.slice(startIndex, endIndex);

        const result = {
            logFileName: logFileName,
            totalRecords: totalRecords,
            page: page,
            pageSize: pageSize,
            logEntries: pagedLines
        };

        return res.status(200).json(result);

    } catch (error: any) {
        if (error.code === 'ENOENT') {
            return res.status(404).json({ error: `Log file not found: ${logFileName}` });
        }
        if (error.code === 'EACCES' || error.code === 'EPERM') {
            return res.status(403).json({ error: "Access to the log file is denied." });
        }
        return res.status(500).json({ error: `An error occurred while reading the log file: ${error.message}` });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
🧪 Senaryo 4: Bir backup uygulamasında kullanıcılar yedeklenecek dizini belirtebilir. Sistem belirtilen dizini tarayarak yedekleme işlemi gerçekleştirir. Yedekleme durumu kullanıcıya raporlanır. İşlem tamamlandığında bildirim gönderilir.
💻 Dil: C#

🤖 AI: Gemini

C#

using System;
using System.IO;
using System.IO.Compression;
using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;
using System.Linq;

[ApiController]
[Route("api/[controller]")]
public class BackupController : ControllerBase
{
    private readonly string _backupRootDirectory = "Backups";

    public BackupController()
    {
        Directory.CreateDirectory(_backupRootDirectory);
    }

    [HttpPost("start-backup")]
    public async Task<IActionResult> StartBackup([FromForm] string directoryToBackup)
    {
        if (string.IsNullOrWhiteSpace(directoryToBackup))
        {
            return BadRequest("Directory to backup cannot be empty.");
        }

        if (!Directory.Exists(directoryToBackup))
        {
            return NotFound($"Directory not found: {directoryToBackup}");
        }

        try
        {
            string backupFileName = $"{Path.GetFileName(directoryToBackup)}_{DateTime.Now:yyyyMMddHHmmss}.zip";
            string backupFilePath = Path.Combine(_backupRootDirectory, backupFileName);

            // Simulate a lengthy backup operation
            await Task.Run(() =>
            {
                ZipFile.CreateFromDirectory(directoryToBackup, backupFilePath);
            });

            // For demonstration, let's also count files/dirs in the original directory for reporting
            var originalDirInfo = new DirectoryInfo(directoryToBackup);
            long originalSize = originalDirInfo.EnumerateFiles("*", SearchOption.AllDirectories).Sum(file => file.Length);
            int filesCount = originalDirInfo.EnumerateFiles("*", SearchOption.AllDirectories).Count();
            int directoriesCount = originalDirInfo.EnumerateDirectories("*", SearchOption.AllDirectories).Count();

            var backupReport = new
            {
                SourceDirectory = directoryToBackup,
                BackupFileName = backupFileName,
                BackupFilePath = backupFilePath,
                BackupSizeInBytes = new FileInfo(backupFilePath).Length,
                OriginalDirectorySizeInBytes = originalSize,
                OriginalFilesCount = filesCount,
                OriginalDirectoriesCount = directoriesCount,
                Status = "Completed",
                Timestamp = DateTime.Now
            };

            // In a real application, you'd send a notification here (e.g., email, push notification)
            // For now, we'll just return it in the response.
            return Ok(new {
                message = $"Backup of '{directoryToBackup}' completed successfully.",
                report = backupReport,
                notification = "Backup operation finished."
            });
        }
        catch (UnauthorizedAccessException)
        {
            return Forbid("Access to the specified directory for backup is denied.");
        }
        catch (Exception ex)
        {
            return StatusCode(500, $"An error occurred during the backup process: {ex.Message}");
        }
    }
}
💻 Dil: Python

🤖 AI: Gemini

Python

import os
import shutil
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

BACKUP_ROOT_DIRECTORY = 'backups'
os.makedirs(BACKUP_ROOT_DIRECTORY, exist_ok=True)

@app.route('/api/backup/start-backup', methods=['POST'])
def start_backup():
    directory_to_backup = request.json.get('directoryToBackup')

    if not directory_to_backup:
        return jsonify({"error": "Directory to backup cannot be empty."}), 400

    if not os.path.isdir(directory_to_backup):
        return jsonify({"error": f"Directory not found: {directory_to_backup}"}), 404

    try:
        dir_name = os.path.basename(directory_to_backup)
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        backup_file_name = f"{dir_name}_{timestamp}" # shutil.make_archive adds .zip

        backup_base_path = os.path.join(BACKUP_ROOT_DIRECTORY, backup_file_name)

        # Create a zip archive of the directory
        # root_dir is the directory that will be archived, base_dir is where the archive is created
        archive_path = shutil.make_archive(backup_base_path, 'zip', root_dir=directory_to_backup)

        # Get original directory size and file/directory counts
        original_size = 0
        files_count = 0
        directories_count = 0
        for dirpath, dirnames, filenames in os.walk(directory_to_backup):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if not os.path.islink(fp):
                    original_size += os.path.getsize(fp)
                files_count += 1
            directories_count += len(dirnames)

        backup_report = {
            "sourceDirectory": directory_to_backup,
            "backupFileName": os.path.basename(archive_path),
            "backupFilePath": archive_path,
            "backupSizeInBytes": os.path.getsize(archive_path),
            "originalDirectorySizeInBytes": original_size,
            "originalFilesCount": files_count,
            "originalDirectoriesCount": directories_count,
            "status": "Completed",
            "timestamp": datetime.datetime.now().isoformat()
        }

        # In a real application, you'd send a notification here (e.g., email, push notification)
        return jsonify({
            "message": f"Backup of '{directory_to_backup}' completed successfully.",
            "report": backup_report,
            "notification": "Backup operation finished."
        }), 200

    except PermissionError:
        return jsonify({"error": "Access to the specified directory for backup is denied."}), 403
    except Exception as e:
        return jsonify({"error": f"An error occurred during the backup process: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
💻 Dil: TypeScript (Node.js)

🤖 AI: Gemini

TypeScript

import express, { Request, Response } from 'express';
import path from 'path';
import fs from 'fs/promises';
import archiver from 'archiver'; // For creating zip archives

const app = express();
const PORT = 3000;

const backupRootDirectory = path.join(__dirname, 'backups');
fs.mkdir(backupRootDirectory, { recursive: true }).catch(console.error);

app.use(express.json()); // For parsing JSON request bodies

async function getDirectorySizeAndCounts(directoryPath: string): Promise<{ size: number, files: number, directories: number }> {
    let totalSize = 0;
    let filesCount = 0;
    let directoriesCount = 0;

    const walk = async (currentPath: string) => {
        const items = await fs.readdir(currentPath);
        for (const item of items) {
            const itemPath = path.join(currentPath, item);
            let itemStats;
            try {
                itemStats = await fs.stat(itemPath);
            } catch (error: any) {
                if (error.code === 'EACCES') {
                    console.warn(`Permission denied for: ${itemPath}. Skipping.`);
                    continue;
                }
                throw error;
            }

            if (itemStats.isFile()) {
                totalSize += itemStats.size;
                filesCount++;
            } else if (itemStats.isDirectory()) {
                directoriesCount++;
                await walk(itemPath); // Recurse into subdirectories
            }
        }
    };
    await walk(directoryPath);
    return { size: totalSize, files: filesCount, directories: directoriesCount };
}


app.post('/api/backup/start-backup', async (req: Request, res: Response) => {
    const { directoryToBackup } = req.body;

    if (!directoryToBackup) {
        return res.status(400).json({ error: "Directory to backup cannot be empty." });
    }

    try {
        await fs.access(directoryToBackup); // Check if directory exists and is accessible
    } catch (error: any) {
        if (error.code === 'ENOENT') {
            return res.status(404).json({ error: `Directory not found: ${directoryToBackup}` });
        }
        if (error.code === 'EACCES' || error.code === 'EPERM') {
            return res.status(403).json({ error: "Access to the specified directory for backup is denied." });
        }
        return res.status(500).json({ error: `An error occurred while checking directory: ${error.message}` });
    }

    const dirName = path.basename(directoryToBackup);
    const timestamp = new Date().toISOString().replace(/[:.-]/g, ''); // Format: YYYYMMDDTHHMMSSsssZ
    const backupFileName = `${dirName}_${timestamp}.zip`;
    const backupFilePath = path.join(backupRootDirectory, backupFileName);

    const output = fs.createWriteStream(backupFilePath);
    const archive = archiver('zip', {
        zlib: { level: 9 } // Sets the compression level.
    });

    output.on('close', async () => {
        const originalStats = await getDirectorySizeAndCounts(directoryToBackup);
        const backupStats = await fs.stat(backupFilePath);

        const backupReport = {
            sourceDirectory: directoryToBackup,
            backupFileName: backupFileName,
            backupFilePath: backupFilePath,
            backupSizeInBytes: backupStats.size,
            originalDirectorySizeInBytes: originalStats.size,
            originalFilesCount: originalStats.files,
            originalDirectoriesCount: originalStats.directories,
            status: "Completed",
            timestamp: new Date().toISOString()
        };

        return res.status(200).json({
            message: `Backup of '${directoryToBackup}' completed successfully.`,
            report: backupReport,
            notification: "Backup operation finished."
        });
    });

    archive.on('warning', (err) => {
        if (err.code === 'ENOENT') {
            console.warn('Archiver warning:', err);
        } else {
            throw err;
        }
    });

    archive.on('error', (err) => {
        console.error('Archiver error:', err);
        return res.status(500).json({ error: `An error occurred during archiving: ${err.message}` });
    });

    archive.pipe(output);
    archive.directory(directoryToBackup, false); // Append the specified directory, false means don't include the base directory itself in the archive
    archive.finalize();
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
🧪 Senaryo 5: Bir ağ test aracında kullanıcılar hedef adresi girip bağlantı testi yapabilir. Sistem belirtilen adrese bağlantı denemesi yapar. Test sonuçları detaylı olarak gösterilir. Ağ performansı analiz edilir.
💻 Dil: C#

🤖 AI: Gemini

C#

using System;
using System.Net.NetworkInformation;
using System.Net.Sockets;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class NetworkTestController : ControllerBase
{
    [HttpGet("ping")]
    public async Task<IActionResult> PingHost([FromQuery] string targetAddress, [FromQuery] int timeoutMs = 4000)
    {
        if (string.IsNullOrWhiteSpace(targetAddress))
        {
            return BadRequest("Target address cannot be empty.");
        }

        try
        {
            using var pingSender = new Ping();
            var reply = await pingSender.SendPingAsync(targetAddress, timeoutMs);

            var result = new
            {
                TargetAddress = targetAddress,
                Status = reply.Status.ToString(),
                RoundtripTimeMs = reply.RoundtripTime,
                BufferSize = reply.Buffer.Length,
                Address = reply.Address?.ToString(),
                NetworkPerformanceAnalysis = reply.Status == IPStatus.Success ? "Connection successful and responsive." : "Connection failed or timed out."
            };

            if (reply.Status == IPStatus.Success)
            {
                return Ok(result);
            }
            else
            {
                return StatusCode(500, result); // Return 500 for failed pings, but still provide details
            }
        }
        catch (PingException ex)
        {
            // This catches issues like "No such host is known"
            return BadRequest($"Invalid target address or host not found: {ex.InnerException?.Message ?? ex.Message}");
        }
        catch (Exception ex)
        {
            return StatusCode(500, $"An error occurred during the ping test: {ex.Message}");
        }
    }

    [HttpGet("port-scan")]
    public async Task<IActionResult> ScanPort([FromQuery] string targetAddress, [FromQuery] int port, [FromQuery] int timeoutMs = 2000)
    {
        if (string.IsNullOrWhiteSpace(targetAddress))
        {
            return BadRequest("Target address cannot be empty.");
        }
        if (port <= 0 || port > 65535)
        {
            return BadRequest("Invalid port number. Port must be between 1 and 65535.");
        }

        try
        {
            using var client = new TcpClient();
            var connectTask = client.ConnectAsync(targetAddress, port);
            
            var timeoutTask = Task.Delay(timeoutMs);

            var completedTask = await Task.WhenAny(connectTask, timeoutTask);

            bool isConnected = false;
            if (completedTask == connectTask && !connectTask.IsFaulted)
            {
                 isConnected = true;
            }

            var result = new
            {
                TargetAddress = targetAddress,
                Port = port,
                Status = isConnected ? "Open" : "Closed or Timed Out",
                NetworkPerformanceAnalysis = isConnected ? $"Successfully connected to port {port}. Service is likely running." : $"Could not connect to port {port}. Service might be down or port is blocked."
            };

            if (isConnected)
            {
                return Ok(result);
            }
            else
            {
                return StatusCode(500, result); // Return 500 for failed connections
            }
        }
        catch (SocketException ex)
        {
            return StatusCode(500, $"Socket error during port scan: {ex.Message}");
        }
        catch (Exception ex)
        {
            return StatusCode(500, $"An error occurred during the port scan: {ex.Message}");
        }
    }
}
💻 Dil: Python

🤖 AI: Gemini

Python

import os
import platform
import subprocess
import socket
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

def ping_host_native(host, count=4):
    """Pings a host using the native system ping command."""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, str(count), host]
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
        stdout, stderr = process.communicate(timeout=10) # 10 second timeout for the ping command itself
        
        if process.returncode == 0:
            # Parse ping output for metrics (simplified for brevity)
            # This is highly dependent on OS output. A more robust solution would parse line by line.
            if "Average" in stdout: # Windows
                avg_line = [line for line in stdout.split('\n') if "Average" in line][0]
                avg_rtt = avg_line.split('=')[-1].strip().split('ms')[0]
                return {"status": "Success", "output": stdout, "average_rtt_ms": float(avg_rtt)}
            elif "avg" in stdout: # Linux/macOS
                match = next((line for line in stdout.split('\n') if "min/avg/max" in line), None)
                if match:
                    parts = match.split('=')[1].strip().split('/')[1]
                    avg_rtt = parts.strip()
                    return {"status": "Success", "output": stdout, "average_rtt_ms": float(avg_rtt)}
            return {"status": "Success", "output": stdout, "average_rtt_ms": None} # Generic success
        else:
            return {"status": "Failed", "output": stderr, "average_rtt_ms": None}
    except FileNotFoundError:
        return {"status": "Error", "output": "Ping command not found.", "average_rtt_ms": None}
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()
        return {"status": "Timeout", "output": "Ping command timed out.", "average_rtt_ms": None}
    except Exception as e:
        return {"status": "Error", "output": str(e), "average_rtt_ms": None}

def scan_port(host, port, timeout=2):
    """Checks if a specific port is open on a host."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            if result == 0:
                return {"status": "Open", "message": f"Port {port} is open."}
            else:
                return {"status": "Closed or Filtered", "message": f"Port {port} is closed or filtered. Error code: {result}"}
    except socket.gaierror:
        return {"status": "Error", "message": "Hostname could not be resolved."}
    except socket.error as e:
        return {"status": "Error", "message": f"Socket error: {str(e)}"}
    except Exception as e:
        return {"status": "Error", "message": f"An unexpected error occurred: {str(e)}"}


@app.route('/api/network-test/ping', methods=['GET'])
def ping_endpoint():
    target_address = request.args.get('targetAddress')
    if not target_address:
        return jsonify({"error": "Target address cannot be empty."}), 400
    
    ping_result = ping_host_native(target_address)
    
    if ping_result["status"] == "Success":
        analysis = "Connection successful and responsive."
        if ping_result["average_rtt_ms"] is not None:
            analysis += f" Average round-trip time: {ping_result['average_rtt_ms']} ms."
        return jsonify({
            "targetAddress": target_address,
            "status": "Success",
            "pingOutput": ping_result["output"],
            "roundtripTimeMs": ping_result["average_rtt_ms"],
            "networkPerformanceAnalysis": analysis
        }), 200
    else:
        return jsonify({
            "targetAddress": target_address,
            "status": ping_result["status"],
            "error": ping_result["output"],
            "networkPerformanceAnalysis": f"Connection failed or timed out: {ping_result['status']}. Details: {ping_result['output']}"
        }), 500

@app.route('/api/network-test/port-scan', methods=['GET'])
def port_scan_endpoint():
    target_address = request.args.get('targetAddress')
    port_str = request.args.get('port')

    if not target_address or not port_str:
        return jsonify({"error": "Target address and port cannot be empty."}), 400

    try:
        port = int(port_str)
        if not (1 <= port <= 65535):
            return jsonify({"error": "Invalid port number. Port must be between 1 and 65535."}), 400
    except ValueError:
        return jsonify({"error": "Port must be a valid integer."}), 400
    
    scan_result = scan_port(target_address, port)

    if scan_result["status"] == "Open":
        analysis = f"Successfully connected to port {port}. Service is likely running."
        return jsonify({
            "targetAddress": target_address,
            "port": port,
            "status": scan_result["status"],
            "message": scan_result["message"],
            "networkPerformanceAnalysis": analysis
        }), 200
    else:
        analysis = f"Could not connect to port {port}. Service might be down or port is blocked. Details: {scan_result['message']}"
        return jsonify({
            "targetAddress": target_address,
            "port": port,
            "status": scan_result["status"],
            "message": scan_result["message"],
            "networkPerformanceAnalysis": analysis
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
💻 Dil: TypeScript (Node.js)

🤖 AI: Gemini

TypeScript

import express, { Request, Response } from 'express';
import { exec } from 'child_process';
import { promisify } from 'util';
import net from 'net';

const app = express();
const PORT = 3000;

const execPromise = promisify(exec);

async function pingHost(targetAddress: string, count: number = 4): Promise<any> {
    const isWindows = process.platform === 'win32';
    const param = isWindows ? '-n' : '-c';
    const command = `ping ${param} ${count} ${targetAddress}`;

    try {
        const { stdout, stderr } = await execPromise(command, { timeout: 10000 }); // 10 second timeout

        if (stderr) {
            return { status: "Failed", output: stderr, average_rtt_ms: null };
        }

        let averageRttMs: number | null = null;
        if (isWindows) {
            const match = stdout.match(/Average = (\d+)ms/);
            if (match && match[1]) {
                averageRttMs = parseInt(match[1], 10);
            }
        } else { // Linux/macOS
            const match = stdout.match(/min\/avg\/max\/mdev = [\d.]+\/([\d.]+)\//);
            if (match && match[1]) {
                averageRttMs = parseFloat(match[1]);
            }
        }

        return { status: "Success", output: stdout, average_rtt_ms: averageRttMs };

    } catch (error: any) {
        if (error.killed && error.signal === 'SIGTERM') {
            return { status: "Timeout", output: "Ping command timed out.", average_rtt_ms: null };
        }
        if (error.cmd && error.cmd.includes('ping') && error.code === 1) { // Exit code 1 for host unreachable
            return { status: "Failed", output: error.stdout || error.stderr || error.message, average_rtt_ms: null };
        }
        return { status: "Error", output: error.message, average_rtt_ms: null };
    }
}

async function scanPort(host: string, port: number, timeout: number = 2000): Promise<any> {
    return new Promise((resolve) => {
        const socket = new net.Socket();
        socket.setTimeout(timeout);

        socket.on('connect', () => {
            socket.destroy();
            resolve({ status: "Open", message: `Port ${port} is open.` });
        });

        socket.on('timeout', () => {
            socket.destroy();
            resolve({ status: "Closed or Timed Out", message: `Connection to port ${port} timed out.` });
        });

        socket.on('error', (err: any) => {
            socket.destroy();
            if (err.code === 'ECONNREFUSED') {
                resolve({ status: "Closed or Filtered", message: `Connection refused by port ${port}.` });
            } else if (err.code === 'EHOSTUNREACH' || err.code === 'ENETUNREACH') {
                resolve({ status: "Error", message: `Host unreachable for port ${port}: ${err.message}` });
            } else {
                resolve({ status: "Error", message: `Socket error for port ${port}: ${err.message}` });
            }
        });

        socket.connect(port, host);
    });
}

app.get('/api/network-test/ping', async (req: Request, res: Response) => {
    const targetAddress = req.query.targetAddress as string;
    const count = parseInt(req.query.count as string) || 4;

    if (!targetAddress) {
        return res.status(400).json({ error: "Target address cannot be empty." });
    }

    const pingResult = await pingHost(targetAddress, count);

    if (pingResult.status === "Success") {
        let analysis = "Connection successful and responsive.";
        if (pingResult.average_rtt_ms !== null) {
            analysis += ` Average round-trip time: ${pingResult.average_rtt_ms} ms.`;
        }
        return res.status(200).json({
            targetAddress: targetAddress,
            status: "Success",
            pingOutput: pingResult.output,
            roundtripTimeMs: pingResult.average_rtt_ms,
            networkPerformanceAnalysis: analysis
        });
    } else {
        return res.status(500).json({
            targetAddress: targetAddress,
            status: pingResult.status,
            error: pingResult.output,
            networkPerformanceAnalysis: `Connection failed or timed out: ${pingResult.status}. Details: ${pingResult.output}`
        });
    }
});

app.get('/api/network-test/port-scan', async (req: Request, res: Response) => {
    const targetAddress = req.query.targetAddress as string;
    const portString = req.query.port as string;
    const timeout = parseInt(req.query.timeout as string) || 2000;

    if (!targetAddress || !portString) {
        return res.status(400).json({ error: "Target address and port cannot be empty." });
    }

    const port = parseInt(portString);
    if (isNaN(port) || port <= 0 || port > 65535) {
        return res.status(400).json({ error: "Invalid port number. Port must be between 1 and 65535." });
    }

    const scanResult = await scanPort(targetAddress, port, timeout);

    if (scanResult.status === "Open") {
        const analysis = `Successfully connected to port ${port}. Service is likely running.`;
        return res.status(200).json({
            targetAddress: targetAddress,
            port: port,
            status: scanResult.status,
            message: scanResult.message,
            networkPerformanceAnalysis: analysis
        });
    } else {
        const analysis = `Could not connect to port ${port}. Service might be down or port is blocked. Details: ${scanResult.message}`;
        return res.status(500).json({
            targetAddress: targetAddress,
            port: port,
            status: scanResult.status,
            message: scanResult.message,
            networkPerformanceAnalysis: analysis
        });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
🧪 Senaryo 6: Bir dosya sıkıştırma uygulamasında kullanıcılar sıkıştırılacak dosyaları seçebilir. Sistem seçilen dosyaları işleyerek arşiv oluşturur. Sıkıştırma seçenekleri kullanıcı tarafından belirlenebilir. Oluşturulan arşiv indirilir.
💻 Dil: C#

🤖 AI: Gemini

C#

using System;
using System.IO;
using System.IO.Compression;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Threading.Tasks;

[ApiController]
[Route("api/[controller]")]
public class FileCompressorController : ControllerBase
{
    private readonly string _uploadDirectory = "Uploads";
    private readonly string _archivesDirectory = "Archives";

    public FileCompressorController()
    {
        Directory.CreateDirectory(_uploadDirectory);
        Directory.CreateDirectory(_archivesDirectory);
        // Create a dummy file for testing if needed
        if (!System.IO.File.Exists(Path.Combine(_uploadDirectory, "example.txt")))
        {
            System.IO.File.WriteAllText(Path.Combine(_uploadDirectory, "example.txt"), "This is an example text file to be compressed.");
        }
        if (!System.IO.File.Exists(Path.Combine(_uploadDirectory, "another.log")))
        {
            System.IO.File.WriteAllText(Path.Combine(_uploadDirectory, "another.log"), "This is another file for demonstration purposes.\nLine 2.\nLine 3.");
        }
    }

    [HttpPost("compress")]
    public async Task<IActionResult> CompressFiles(
        [FromForm] List<string> fileNames, // Assuming file names are already in the upload directory
        [FromForm] CompressionLevel compressionLevel = CompressionLevel.Optimal)
    {
        if (fileNames == null || !fileNames.Any())
        {
            return BadRequest("No files selected for compression.");
        }

        string archiveName = $"archive_{DateTime.Now:yyyyMMddHHmmss}.zip";
        string archivePath = Path.Combine(_archivesDirectory, archiveName);

        try
        {
            using (var zipStream = new FileStream(archivePath, FileMode.Create, FileAccess.Write))
            using (var zipArchive = new ZipArchive(zipStream, ZipArchiveMode.Create, true))
            {
                foreach (var fileName in fileNames)
                {
                    string filePath = Path.Combine(_uploadDirectory, fileName);
                    if (!System.IO.File.Exists(filePath))
                    {
                        // Optionally, skip missing files or return an error
                        continue; 
                    }

                    var entry = zipArchive.CreateEntry(fileName, compressionLevel);
                    using (var entryStream = entry.Open())
                    using (var fileToCompressStream = System.IO.File.OpenRead(filePath))
                    {
                        await fileToCompressStream.CopyToAsync(entryStream);
                    }
                }
            }

            return Ok(new {
                message = $"Files compressed successfully into '{archiveName}'.",
                archiveFileName = archiveName,
                archiveFilePath = archivePath,
                archiveSizeInBytes = new FileInfo(archivePath).Length,
                downloadUrl = Url.Action("DownloadArchive", "FileCompressor", new { fileName = archiveName }, Request.Scheme)
            });
        }
        catch (UnauthorizedAccessException)
        {
            return Forbid("Access to files or directories is denied.");
        }
        catch (Exception ex)
        {
            return StatusCode(500, <span class="math-inline">"An error occurred during file compression\: \{ex\.Message\}"\);
\}
\}
\[HttpGet\("download\-archive"\)\]
public IActionResult DownloadArchive\(\[FromQuery\] string fileName\)
\{
if \(string\.IsNullOrWhiteSpace\(fileName\)\)
\{
return BadRequest\("Archive file name cannot be empty\."\);
\}
string filePath \= Path\.Combine\(\_archivesDirectory, fileName\);
if \(\!System\.IO\.File\.Exists\(filePath\)\)
\{
return NotFound\(</span>"Archive file not found: {fileName}");
        }

        try
        {
            var fileBytes = System.IO.File.ReadAllBytes(filePath);
            return File(fileBytes, "application/zip", fileName);
        }
        catch (UnauthorizedAccessException)
        {
            return Forbid("Access to the archive file is denied.");
        }
        catch (Exception ex)
        {
            return StatusCode(500, $"An error occurred while downloading the archive: {ex.Message}");
        }
    }
}
💻 Dil: Python

🤖 AI: Gemini

Python

import os
import zipfile
import datetime
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ARCHIVES_FOLDER = 'archives'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ARCHIVES_FOLDER'] = ARCHIVES_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ARCHIVES_FOLDER, exist_ok=True)

# Create some dummy files for demonstration
if not os.path.exists(os.path.join(UPLOAD_FOLDER, "example.txt")):
    with open(os.path.join(UPLOAD_FOLDER, "example.txt"), "w") as f:
        f.write("This is an example text file to be compressed.")
if not os.path.exists(os.path.join(UPLOAD_FOLDER, "another.log")):
    with open(os.path.join(UPLOAD_FOLDER, "another.log"), "w") as f:
        f.write("This is another file for demonstration purposes.\nLine 2.\nLine 3.")


@app.route('/api/file-compressor/compress', methods=['POST'])
def compress_files():
    # Expecting a list of file names that are already in the UPLOAD_FOLDER
    file_names = request.json.get('fileNames')
    compression_level_str = request.json.get('compressionLevel', 'optimal')

    if not file_names:
        return jsonify({"error": "No files selected for compression."}), 400

    # Map string compression levels to zipfile constants
    compression_map = {
        'stored': zipfile.ZIP_STORED, # No compression
        'fastest': zipfile.ZIP_DEFLATED, # Good balance
        'optimal': zipfile.ZIP_DEFLATED # Default for deflate, often good
    }
    compression_method = compression_map.get(compression_level_str.lower(), zipfile.ZIP_DEFLATED)
    
    # Python's zipfile.ZIP_DEFLATED is generally good enough; no direct mapping for "fastest" vs "optimal" like C#
    # unless you use external libraries or lower-level zlib directly.

    archive_name = f"archive_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.zip"
    archive_path = os.path.join(app.config['ARCHIVES_FOLDER'], archive_name)

    try:
        with zipfile.ZipFile(archive_path, 'w', compression=compression_method, allowZip64=True) as zipf:
            for file_name in file_names:
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file_name))
                if not os.path.exists(file_path):
                    continue # Skip if file not found
                
                zipf.write(file_path, arcname=file_name) # Add file to archive with its original name
        
        archive_size_in_bytes = os.path.getsize(archive_path)

        return jsonify({
            "message": f"Files compressed successfully into '{archive_name}'.",
            "archiveFileName": archive_name,
            "archiveFilePath": archive_path,
            "archiveSizeInBytes": archive_size_in_bytes,
            "downloadUrl": f"/api/file-compressor/download-archive?fileName={archive_name}"
        }), 200

    except PermissionError:
        return jsonify({"error": "Access to files or directories is denied."}), 403
    except Exception as e:
        return jsonify({"error": f"An error occurred during file compression: {str(e)}"}), 500

@app.route('/api/file-compressor/download-archive', methods=['GET'])
def download_archive():
    file_name = request.args.get('fileName')

    if not file_name:
        return jsonify({"error": "Archive file name cannot be empty."}), 400

    file_path = os.path.join(app.config['ARCHIVES_FOLDER'], secure_filename(file_name))

    if not os.path.exists(file_path):
        return jsonify({"error": f"Archive file not found: {file_name}"}), 404

    try:
        return send_file(file_path, as_attachment=True, download_name=file_name)
    except PermissionError:
        return jsonify({"error": "Access to the archive file is denied."}), 403
    except Exception as e:
        return jsonify({"error": f"An error occurred while downloading the archive: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
💻 Dil: TypeScript (Node.js)

🤖 AI: Gemini

TypeScript

import express, { Request, Response } from 'express';
import path from 'path';
import fs from 'fs/promises';
import archiver from 'archiver';

const app = express();
const PORT = 3000;

const uploadDirectory = path.join(__dirname, 'uploads');
const archivesDirectory = path.join(__dirname, 'archives');

// Ensure directories exist
fs.mkdir(uploadDirectory, { recursive: true }).catch(console.error);
fs.mkdir(archivesDirectory, { recursive: true }).catch(console.error);

// Create some dummy files for demonstration
async function createDummyFiles() {
    const exampleTxtPath = path.join(uploadDirectory, 'example.txt');
    const anotherLogPath = path.join(uploadDirectory, 'another.log');

    if (!await fs.access(exampleTxtPath).then(() => true).catch(() => false)) {
        await fs.writeFile(exampleTxtPath, 'This is an example text file to be compressed.');
    }
    if (!await fs.access(anotherLogPath).then(() => true).catch(() => false)) {
        await fs.writeFile(anotherLogPath, 'This is another file for demonstration purposes.\nLine 2.\nLine 3.');
    }
}
createDummyFiles();

app.use(express.json()); // To parse JSON bodies if fileNames are sent in body

app.post('/api/file-compressor/compress', async (req: Request, res: Response) => {
    const { fileNames, compressionLevel = 'optimal' } = req.body;

    if (!fileNames || !Array.isArray(fileNames) || fileNames.length === 0) {
        return res.status(400).json({ error: "No files selected for compression." });
    }

    const archiveName = `archive_${Date.now()}.zip`;
    const archivePath = path.join(archivesDirectory, archiveName);

    const output = fs.createWriteStream(archivePath);
    
    // Map compression level string to archiver's zlib level (0-9)
    let zlibLevel = 9; // Default to optimal
    if (compressionLevel === 'fastest') {
        zlibLevel = 1;
    } else if (compressionLevel === 'none') {
        zlibLevel = 0; // No compression
    }

    const archive = archiver('zip', {
        zlib: { level: zlibLevel }
    });

    output.on('close', async () => {
        try {
            const stats = await fs.stat(archivePath);
            return res.status(200).json({
                message: `Files compressed successfully into '${archiveName}'.`,
                archiveFileName: archiveName,
                archiveFilePath: archivePath,
                archiveSizeInBytes: stats.size,
                downloadUrl: `/api/file-compressor/download-archive?fileName=${archiveName}`
            });
        } catch (error: any) {
            console.error('Error getting archive stats after compression:', error);
            return res.status(500).json({ error: `An error occurred after compression: ${error.message}` });
        }
    });

    archive.on('warning', (err) => {
        if (err.code === 'ENOENT') {
            console.warn('Archiver warning:', err);
        } else {
            console.warn('Archiver warning:', err);
        }
    });

    archive.on('error', (err) => {
        console.error('Archiver error:', err);
        return res.status(500).json({ error: `An error occurred during archiving: ${err.message}` });
    });

    archive.pipe(output);

    for (const fileName of fileNames) {
        const filePath = path.join(uploadDirectory, fileName);
        try {
            await fs.access(filePath); // Check if file exists
            archive.file(filePath, { name: fileName }); // Add file to archive
        } catch (error: any) {
            if (error.code === 'ENOENT') {
                console.warn(`File not found, skipping: ${filePath}`);
            } else if (error.code === 'EACCES' || error.code === 'EPERM') {
                console.warn(`Permission denied, skipping: ${filePath}`);
            } else {
                console.error(`Error accessing file ${filePath}: ${error.message}`);
                // Don't throw here, just skip and log, let the archiving continue for other files
            }
        }
    }

    archive.finalize();
});

app.get('/api/file-compressor/download-archive', async (req: Request, res: Response) => {
    const fileName = req.query.fileName as string;

    if (!fileName) {
        return res.status(400).json({ error: "Archive file name cannot be empty." });
    }

    const filePath = path.join(archivesDirectory, fileName);

    try {
        await fs.access(filePath); // Check if file exists and is accessible
        return res.download(filePath, fileName, (err) => {
            if (err) {
                if (err.code === 'ENOENT') {
                    return res.status(404).json({ error: `Archive file not found: ${fileName}` });
                }
                if (err.code === 'EACCES' || err.code === 'EPERM') {
                    return res.status(403).json({ error: "Access to the archive file is denied." });
                }
                return res.status(500).json({ error: `An error occurred while downloading the archive: ${err.message}` });
            }
        });
    } catch (error: any) {
        if (error.code === 'ENOENT') {
            return res.status(404).json({ error: `Archive file not found: ${fileName}` });
        }
        if (error.code === 'EACCES' || error.code === 'EPERM') {
            return res.status(403).json({ error: "Access to the archive file is denied." });
        }
        return res.status(500).json({ error: `An error occurred while accessing the file: ${error.message}` });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
🧪 Senaryo 7: Bir sistem izleme aracında kullanıcılar izlenecek süreci belirtebilir. Sistem belirtilen sürecin durumunu takip eder. İzleme verileri grafiklerle sunulur. Süreç performansı analiz edilir.
💻 Dil: C#

🤖 AI: Gemini

C#

using System;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

[ApiController]
[Route("api/[controller]")]
public class SystemMonitorController : ControllerBase
{
    // In a real application, you'd store historical data for graphs
    // For demonstration, we'll return a snapshot.
    private static readonly Dictionary<string, ProcessMonitoringData> _monitoredProcesses = new Dictionary<string, ProcessMonitoringData>();

    // Helper class to store process data
    public class ProcessMonitoringData
    {
        public int ProcessId { get; set; }
        public string ProcessName { get; set; } = string.Empty;
        public List<ProcessSnapshot> Snapshots { get; set; } = new List<ProcessSnapshot>();
    }

    public class ProcessSnapshot
    {
        public DateTime Timestamp { get; set; }
        public long WorkingSet64Bytes { get; set; }
        public double CpuUsagePercentage { get; set; }
        public int ThreadCount { get; set; }
    }

    [HttpPost("monitor-process")]
    public IActionResult MonitorProcess([FromForm] string processName)
    {
        if (string.IsNullOrWhiteSpace(processName))
        {
            return BadRequest("Process name cannot be empty.");
        }

        var processes = Process.GetProcessesByName(processName);
        if (!processes.Any())
        {
            return NotFound(<span class="math-inline">"No running process found with name\: \{processName\}"\);
\}
var process \= processes\.First\(\); // Monitor the first one found for simplicity
if \(\_monitoredProcesses\.ContainsKey\(processName\)\)
\{
// Update existing monitoring, or clear and restart
\_monitoredProcesses\[processName\]\.ProcessId \= process\.Id;
\_monitoredProcesses\[processName\]\.Snapshots\.Clear\(\);
return Ok\(</span>"Monitoring updated for process '{processName}' (ID: {process.Id}).");
        }
        else
        {
            _monitoredProcesses.Add(processName, new ProcessMonitoringData
            {
                ProcessId = process.Id,
                ProcessName = processName
            });
            return Ok(<span class="math-inline">"Started monitoring process '\{processName\}' \(ID\: \{process\.Id\}\)\."\);
\}
\}
\[HttpGet\("get\-monitoring\-data"\)\]
public IActionResult GetMonitoringData\(\[FromQuery\] string processName\)
\{
if \(string\.IsNullOrWhiteSpace\(processName\)\)
\{
return BadRequest\("Process name cannot be empty\."\);
\}
if \(\!\_monitoredProcesses\.TryGetValue\(processName, out var data\)\)
\{
return NotFound\(</span>"Process '{processName}' is not currently being monitored.");
        }

        try
        {
            // Get current performance data
            var processes = Process.GetProcessesByName(processName);
            var process = processes.FirstOrDefault(p => p.Id == data.ProcessId);

            if (process == null || process.HasExited)
            {
                _monitoredProcesses.Remove(processName); // Clean up if process exited
                return NotFound(<span class="math-inline">"Monitored process '\{processName\}' \(ID\: \{data\.ProcessId\}\) has exited\."\);
\}
// Calculate CPU usage \(requires multiple samples for accuracy\)
// For a single snapshot, we'll provide a simplified view\.
// A real monitoring tool would capture CPU over time and calculate delta\.
double cpuUsage \= 0\.0;
// The PerformanceCounter class is better for real\-time CPU monitoring
// using "Process" category and "% Processor Time" counter\.
// For this example, we'll just show it as 'available' to implement\.
var snapshot \= new ProcessSnapshot
\{
Timestamp \= DateTime\.Now,
WorkingSet64Bytes \= process\.WorkingSet64,
ThreadCount \= process\.Threads\.Count,
CpuUsagePercentage \= cpuUsage // Placeholder
\};
data\.Snapshots\.Add\(snapshot\); // Add to history
// Simple analysis
string performanceAnalysis \= "Performance analysis not available for single snapshot\. Consider collecting multiple data points\.";
if \(data\.Snapshots\.Count \> 1\)
\{
// Simplified analysis\: if memory grows significantly
var initialMem \= data\.Snapshots\.First\(\)\.WorkingSet64Bytes;
var currentMem \= data\.Snapshots\.Last\(\)\.WorkingSet64Bytes;
if \(currentMem \> initialMem \* 1\.5\) // Memory increased by 50%
\{
performanceAnalysis \= "Memory usage has significantly increased\.";
\}
else
\{
performanceAnalysis \= "Memory usage is stable\.";
\}
// Add more complex CPU/memory trend analysis here
\}
return Ok\(new
\{
ProcessName \= data\.ProcessName,
ProcessId \= data\.ProcessId,
CurrentSnapshot \= snapshot,
HistoricalSnapshots \= data\.Snapshots, // For simple "graphing" data
PerformanceAnalysis \= performanceAnalysis
\}\);
\}
catch \(InvalidOperationException\)
\{
// Process might have exited between checks
\_monitoredProcesses\.Remove\(processName\);
return NotFound\(</span>"Monitored process '{processName}' (ID: {data.ProcessId}) has exited unexpectedly.");
        }
        catch (Exception ex)
        {
            return StatusCode(500, <span class="math-inline">"An error occurred while getting monitoring data\: \{ex\.Message\}"\);
\}
\}
\[HttpDelete\("stop\-monitor"\)\]
public IActionResult StopMonitor\(\[FromQuery\] string processName\)
\{
if \(string\.IsNullOrWhiteSpace\(processName\)\)
\{
return BadRequest\("Process name cannot be empty\."\);
\}
if \(\_monitoredProcesses\.Remove\(processName\)\)
\{
return Ok\(</span>"Stopped monitoring process '{processName}'.");
        }
        else
        {
            return NotFound($"Process '{processName}' was not being monitored.");
        }
    }
}
💻 Dil: Python

🤖 AI: Gemini

Python

import psutil
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# In a real application, you'd store historical data for graphs
# For demonstration, we'll use a dictionary to simulate in-memory storage.
_monitored_processes = {} # {process_name: {'pid': int, 'snapshots': [{'timestamp': str, 'cpu_percent': float, 'memory_info': dict}]}}

@app.route('/api/system-monitor/monitor-process', methods=['POST'])
def monitor_process():
    process_name = request.json.get('processName')

    if not process_name:
        return jsonify({"error": "Process name cannot be empty."}), 400
    
    found_processes = [p for p in psutil.process_iter(['pid', 'name']) if p.info['name'] == process_name]

    if not found_processes:
        return jsonify({"error": f"No running process found with name: {process_name}"}), 404
    
    # Monitor the first one found for simplicity
    process_info = found_processes[0]
    pid = process_info.info['pid']

    if process_name in _monitored_processes:
        # Update existing monitoring, clear old snapshots
        _monitored_processes[process_name]['pid'] = pid
        _monitored_processes[process_name]['snapshots'] = []
        return jsonify({"message": f"Monitoring updated for process '{process_name}' (PID: {pid})."}), 200
    else:
        _monitored_processes[process_name] = {
            'pid': pid,
            'snapshots': []
        }
        return jsonify({"message": f"Started monitoring process '{process_name}' (PID: {pid})."}), 200

@app.route('/api/system-monitor/get-monitoring-data', methods=['GET'])
def get_monitoring_data():
    process_name = request.args.get('processName')

    if not process_name:
        return jsonify({"error": "Process name cannot be empty."}), 400

    if process_name not in _monitored_processes:
        return jsonify({"error": f"Process '{process_name}' is not currently being monitored."}), 404
    
    monitored_data = _monitored_processes[process_name]
    pid = monitored_data['pid']

    try:
        process = psutil.Process(pid)
        if not process.is_running():
            del _monitored_processes[process_name] # Clean up if process exited
            return jsonify({"error": f"Monitored process '{process_name}' (PID: {pid}) has exited."}), 404
        
        # Get current performance data
        cpu_percent = process.cpu_percent(interval=0.1) # Non-blocking for 0.1s
        memory_info = process.memory_info()
        threads_count = process.num_threads()

        current_snapshot = {
            "timestamp": datetime.datetime.now().isoformat(),
            "cpuUsagePercentage": cpu_percent,
            "memoryInfo": {
                "rss": memory_info.rss,
                "vms": memory_info.vms,
                "percent": process.memory_percent()
            },
            "threadCount": threads_count
        }
        monitored_data['snapshots'].append(current_snapshot)

        # Simple performance analysis
        performance_analysis = "Performance analysis: Current snapshot collected."
        if len(monitored_data['snapshots']) > 1:
            initial_mem_rss = monitored_data['snapshots'][0]['memoryInfo']['rss']
            current_mem_rss = monitored_data['snapshots'][-1]['memoryInfo']['rss']
            
            if current_mem_rss > initial_mem_rss * 1.5:
                performance_analysis = "Memory usage has significantly increased (over 50% since monitoring started)."
            elif current_mem_rss < initial_mem_rss * 0.8:
                performance_analysis = "Memory usage has significantly decreased."
            else:
                performance_analysis = "Memory usage is relatively stable."

            # More complex analysis would involve trends over time, thresholds etc.

        return jsonify({
            "processName": process_name,
            "processId": pid,
            "currentSnapshot": current_snapshot,
            "historicalSnapshots": monitored_data['snapshots'],
            "performanceAnalysis": performance_analysis
        }), 200

    except psutil.NoSuchProcess:
        del _monitored_processes[process_name]
        return jsonify({"error": f"Monitored process '{process_name}' (PID: {pid}) has exited unexpectedly."}), 404
    except PermissionError:
        return jsonify({"error": "Permission denied to access process information."}), 403
    except Exception as e:
        return jsonify({"error": f"An error occurred while getting monitoring data: {str(e)}"}), 500

@app.route('/api/system-monitor/stop-monitor', methods=['DELETE'])
def stop_monitor():
    process_name = request.args.get('processName')

    if not process_name:
        return jsonify({"error": "Process name cannot be empty."}), 400

    if process_name in _monitored_processes:
        del _monitored_processes[process_name]
        return jsonify({"message": f"Stopped monitoring process '{process_name}'."}), 200
    else:
        return jsonify({"error": f"Process '{process_name}' was not being monitored."}), 404

if __name__ == '__main__':
    app.run(debug=True)
💻 Dil: TypeScript (Node.js)

🤖 AI: Gemini

TypeScript

import express, { Request, Response } from 'express';
import { exec } from 'child_process';
import { promisify } from 'util';

const app = express();
const PORT = 3000;

const execPromise = promisify(exec);

interface ProcessSnapshot {
    timestamp: string;
    cpuUsagePercentage: number | null;
    memoryUsageBytes: number | null;
    threadCount: number | null;
}

interface ProcessMonitoringData {
    pid: number;
    processName: string;
    snapshots: ProcessSnapshot[];
    // You might also store initial CPU times for accurate calculation over time
    lastCpuTime: number | null; 
    lastUpdateTime: number | null;
}

// In-memory storage for monitored processes
const monitoredProcesses: { [processName: string]: ProcessMonitoringData } = {};

app.use(express.json());

// Helper to get process data (simplified, real-world requires more robust cross-platform solutions)
async function getProcessInfo(pid: number): Promise<ProcessSnapshot | null> {
    try {
        const isWindows = process.platform === 'win32';
        let command: string;

        if (isWindows) {
            // Using tasklist to get memory and tasklist /FI "PID eq [PID]" for more details
            // Getting CPU usage accurately requires sampling over time.
            command = `tasklist /FI "PID eq ${pid}" /FO CSV /NH && wmic process where ProcessId=${pid} get WorkingSetSize,ThreadCount,PercentProcessorTime /value`;
        } else { // Linux/macOS
            // Using ps for memory and thread count. For CPU, we typically need two samples.
            // 'top' or 'htop' provide dynamic CPU, but getting a single snapshot accurately is harder with 'ps'.
            command = `ps -p ${pid} -o %cpu,rss,nlwp= | awk '{print $1,$2,$3}'`;
        }

        const { stdout } = await execPromise(command);

        if (isWindows) {
            const lines = stdout.split('\n').filter(line => line.trim() !== '');
            const tasklistLine = lines[0];
            const wmicLines = lines.slice(1);

            const tasklistParts = tasklistLine.split(',').map(p => p.trim().replace(/"/g, ''));
            // console.log("tasklistParts:", tasklistParts);
            
            // WMIC output parsing
            let workingSetSize: number | null = null;
            let threadCount: number | null = null;
            // let percentProcessorTime: number | null = null; // PercentProcessorTime is tricky for snapshot

            wmicLines.forEach(line => {
                if (line.includes('WorkingSetSize=')) {
                    workingSetSize = parseInt(line.split('=')[1], 10);
                }
                if (line.includes('ThreadCount=')) {
                    threadCount = parseInt(line.split('=')[1], 10);
                }
                // if (line.includes('PercentProcessorTime=')) {
                //     percentProcessorTime = parseFloat(line.split('=')[1]); // Instantaneous, not average
                // }
            });

            return {
                timestamp: new Date().toISOString(),
                cpuUsagePercentage: null, // Requires more complex calculation over time
                memoryUsageBytes: workingSetSize,
                threadCount: threadCount
            };

        } else { // Linux/macOS parsing
            const parts = stdout.trim().split(' ');
            const cpu = parseFloat(parts[0]); // %cpu (often average since last boot or interval)
            const rss = parseInt(parts[1], 10) * 1024; // rss is in KB, convert to bytes
            const nlwp = parseInt(parts[2], 10); // Number of lightweight processes (threads)

            return {
                timestamp: new Date().toISOString(),
                cpuUsagePercentage: cpu,
                memoryUsageBytes: rss,
                threadCount: nlwp
            };
        }
    } catch (error: any) {
        if (error.code === 1) { // ps or tasklist failed to find process
            return null;
        }
        console.error(`Error getting process info for PID ${pid}:`, error);
        throw error;
    }
}

app.post('/api/system-monitor/monitor-process', async (req: Request, res: Response) => {
    const { processName } = req.body;

    if (!processName) {
        return res.status(400).json({ error: "Process name cannot be empty." });
    }

    try {
        const isWindows = process.platform === 'win32';
        const findProcessCommand = isWindows ? `tasklist /FI "IMAGENAME eq ${processName}.exe" /FO CSV /NH` : `pgrep -l ${processName}`;
        
        const { stdout } = await execPromise(findProcessCommand);
        let pid: number | null = null;

        if (isWindows) {
            const lines = stdout.split('\n').filter(line => line.trim() !== '');
            if (lines.length > 0) {
                const parts = lines[0].split(',').map(p => p.trim().replace(/"/g, ''));
                pid = parseInt(parts[1], 10); // PID is typically the second column
            }
        } else {
            const lines = stdout.split('\n').filter(line => line.trim() !== '');
            if (lines.length > 0) {
                pid = parseInt(lines[0].split(' ')[0], 10);
            }
        }

        if (pid === null || isNaN(pid)) {
            return res.status(404).json({ error: `No running process found with name: ${processName}` });
        }

        if (monitoredProcesses[processName]) {
            monitoredProcesses[processName].pid = pid;
            monitoredProcesses[processName].snapshots = []; // Clear old snapshots
            monitoredProcesses[processName].lastCpuTime = null; // Reset for new CPU calculation
            monitoredProcesses[processName].lastUpdateTime = null;
            return res.status(200).json({ message: `Monitoring updated for process '${processName}' (PID: ${pid}).` });
        } else {
            monitoredProcesses[processName] = {
                pid: pid,
                processName: processName,
                snapshots: [],
                lastCpuTime: null,
                lastUpdateTime: null
            };
            return res.status(200).json({ message: `Started monitoring process '${processName}' (PID: ${pid}).` });
        }

    } catch (error: any) {
        if (error.code === 1) { // Command returned non-zero, e.g., pgrep not found
            return res.status(404).json({ error: `No running process found with name: ${processName}` });
        }
        return res.status(500).json({ error: `An error occurred while trying to find the process: ${error.message}` });
    }
});

app.get('/api/system-monitor/get-monitoring-data', async (req: Request, res: Response) => {
    const processName = req.query.processName as string;

    if (!processName) {
        return res.status(400).json({ error: "Process name cannot be empty." });
    }

    const data = monitoredProcesses[processName];
    if (!data) {
        return res.status(404).json({ error: `Process '${processName}' is not currently being monitored.` });
    }

    try {
        const currentSnapshot = await getProcessInfo(data.pid);

        if (!currentSnapshot) {
            delete monitoredProcesses[processName]; // Clean up if process exited
            return res.status(404).json({ error: `Monitored process '${processName}' (PID: ${data.pid}) has exited.` });
        }

        // Add CPU calculation if not provided by getProcessInfo directly
        if (process.platform === 'linux' || process.platform === 'darwin') { // For Unix-like systems, ps -o %cpu is often cumulative
            // Real CPU usage calculation typically needs to compare two snapshots of process CPU time.
            // For simplicity here, if the underlying command gives a percentage, we use it.
            // Otherwise, we'd need to store lastCpuTime and calculate (currentCpuTime - lastCpuTime) / (currentTime - lastTime)
        }

        data.snapshots.push(currentSnapshot);

        // Simple performance analysis
        let performanceAnalysis = "Performance analysis: Current snapshot collected.";
        if (data.snapshots.length > 1) {
            const initialMem = data.snapshots[0].memoryUsageBytes;
            const currentMem = data.snapshots[data.snapshots.length - 1].memoryUsageBytes;

            if (initialMem !== null && currentMem !== null) {
                if (currentMem > initialMem * 1.5) {
                    performanceAnalysis = "Memory usage has significantly increased (over 50% since monitoring started).";
                } else if (currentMem < initialMem * 0.8) {
                    performanceAnalysis = "Memory usage has significantly decreased.";
                } else {
                    performanceAnalysis = "Memory usage is relatively stable.";
                }
            }
        }

        return res.status(200).json({
            processName: data.processName,
            processId: data.pid,
            currentSnapshot: currentSnapshot,
            historicalSnapshots: data.snapshots,
            performanceAnalysis: performanceAnalysis
        });

    } catch (error: any) {
        return res.status(500).json({ error: `An error occurred while getting monitoring data: ${error.message}` });
    }
});

app.delete('/api/system-monitor/stop-monitor', (req: Request, res: Response) => {
    const processName = req.query.processName as string;

    if (!processName) {
        return res.status(400).json({ error: "Process name cannot be empty." });
    }

    if (monitoredProcesses[processName]) {
        delete monitoredProcesses[processName];
        return res.status(200).json({ message: `Stopped monitoring process '${processName}'.` });
    } else {
        return res.status(404).json({ error: `Process '${processName}' was not being monitored.` });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
🧪 Senaryo 8: Bir dosya arama uygulamasında kullanıcılar arama kriterini girebilir. Sistem belirtilen kritere göre dosya sisteminde tarama yapar. Bulunan dosyalar liste halinde gösterilir. Arama sonuçları filtrelenebilir.
💻 Dil: C#

🤖 AI: Gemini

C#

using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

[ApiController]
[Route("api/[controller]")]
public class FileSearchController : ControllerBase
{
    private readonly string _baseSearchDirectory = "C:\\TempSearchDir"; // Example base directory for searches

    public FileSearchController()
    {
        // Create some dummy files for demonstration if the directory doesn't exist
        if (!Directory.Exists(_baseSearchDirectory))
        {
            Directory.CreateDirectory(_baseSearchDirectory);
            System.IO.File.WriteAllText(Path.Combine(_baseSearchDirectory, "document1.txt"), "This is a test document with some keywords like important.");
            System.IO.File.WriteAllText(Path.Combine(_baseSearchDirectory, "report_2023.pdf"), "%PDF-1.4\n%This is a dummy PDF file.\nKeywords: financial report."); // Dummy content
            System.IO.File.WriteAllText(Path.Combine(_baseSearchDirectory, "image.jpg"), "dummy binary data"); // Dummy content
            Directory.CreateDirectory(Path.Combine(_baseSearchDirectory, "subfolder"));
            System.IO.File.WriteAllText(Path.Combine(_baseSearchDirectory, "subfolder", "meeting_notes.txt"), "Meeting notes for today, discussing security and project status.");
            System.IO.File.WriteAllText(Path.Combine(_baseSearchDirectory, "subfolder", "data.json"), "{ \"name\": \"example\", \"value\": 123 }");
        }
    }

    [HttpGet("search")]
    public async Task<IActionResult> SearchFiles(
        [FromQuery] string searchTerm,
        [FromQuery] string? fileExtensionFilter = null,
        [FromQuery] long? minSizeKb = null,
        [FromQuery] long? maxSizeKb = null,
        [FromQuery] bool searchContent = false)
    {
        if (string.IsNullOrWhiteSpace(searchTerm))
        {
            return BadRequest("Search term cannot be empty.");
        }

        if (!Directory.Exists(_baseSearchDirectory))
        {
            return StatusCode(500, <span class="math-inline">"Base search directory not found\: \{\_baseSearchDirectory\}"\);
\}
var foundFiles \= new List<object\>\(\);
try
\{
// Use Parallel\.ForEach for potentially faster directory traversal
var files \= Directory\.EnumerateFiles\(\_baseSearchDirectory, "\*", SearchOption\.AllDirectories\);
foreach \(var filePath in files\)
\{
var fileInfo \= new FileInfo\(filePath\);
// Apply file extension filter
if \(\!string\.IsNullOrWhiteSpace\(fileExtensionFilter\) &&
\!fileInfo\.Extension\.Equals\(</span>".{fileExtensionFilter}", StringComparison.OrdinalIgnoreCase))
                {
                    continue;
                }

                // Apply size filters
                long fileSizeKb = fileInfo.Length / 1024;
                if (minSizeKb.HasValue && fileSizeKb < minSizeKb.Value)
                {
                    continue;
                }
                if (maxSizeKb.HasValue && fileSizeKb > maxSizeKb.Value)
                {
                    continue;
                }

                bool matchesSearchTerm = false;

                // Search by file name
                if (fileInfo.Name.Contains(searchTerm, StringComparison.OrdinalIgnoreCase))
                {
                    matchesSearchTerm = true;
                }

                // Search by content if requested and file is text-based (simplified)
                if (searchContent && !matchesSearchTerm)
                {
                    string extension = fileInfo.Extension.ToLowerInvariant();
                    // Only try to read common text files, avoid binary files
                    if (extension == ".txt" || extension == ".log" || extension == ".json" || extension == ".xml")
                    {
                        try
                        {
                            string fileContent = await System.IO.File.ReadAllTextAsync(filePath);
                            if (fileContent.Contains(searchTerm, StringComparison.OrdinalIgnoreCase))
                            {
                                matchesSearchTerm = true;
                            }
                        }
                        catch (IOException) { /* File in use, skip */ }
                        catch (UnauthorizedAccessException) { /* Access denied, skip */ }
                        catch (Exception) { /* Other read errors, skip */ }
                    }
                }

                if (matchesSearchTerm)
                {
                    foundFiles.Add(new
                    {
                        FileName = fileInfo.Name,
                        FilePath = fileInfo.FullName,
                        FileSizeKb = fileSizeKb,
                        LastModified = fileInfo.LastWriteTime
                    });
                }
            }

            return Ok(new
            {
                SearchTerm = searchTerm,
                FiltersApplied = new { fileExtensionFilter, minSizeKb, maxSizeKb, searchContent },
                FoundFilesCount = foundFiles.Count,
                Files = foundFiles.OrderBy(f => ((string)((dynamic)f).FileName)).ToList()
            });
        }
        catch (UnauthorizedAccessException)
        {
            return Forbid($"Access denied to one or more directories within '{_baseSearchDirectory}'.");
        }
        catch (Exception ex)
        {
            return StatusCode(500, $"An error occurred during file search: {ex.Message}");
        }
    }
}
💻 Dil: Python

🤖 AI: Gemini

Python

import os
from flask import Flask, request, jsonify

app = Flask(__name__)

BASE_SEARCH_DIRECTORY = 'temp_search_dir'
os.makedirs(BASE_SEARCH_DIRECTORY, exist_ok=True)
os.makedirs(os.path.join(BASE_SEARCH_DIRECTORY, 'subfolder'), exist_ok=True)

# Create some dummy files for demonstration
if not os.path.exists(os.path.join(BASE_SEARCH_DIRECTORY, "document1.txt")):
    with open(os.path.join(BASE_SEARCH_DIRECTORY, "document1.txt"), "w") as f:
        f.write("This is a test document with some keywords like important.")
if not os.path.exists(os.path.join(BASE_SEARCH_DIRECTORY, "report_2023.pdf")):
    with open(os.path.join(BASE_SEARCH_DIRECTORY, "report_2023.pdf"), "wb") as f:
        f.write(b"%PDF-1.4\n%This is a dummy PDF file.\nKeywords: financial report.") # Dummy binary for PDF
if not os.path.exists(os.path.join(BASE_SEARCH_DIRECTORY, "image.jpg")):
    with open(os.path.join(BASE_SEARCH_DIRECTORY, "image.jpg"), "wb") as f:
        f.write(b"dummy binary data")
if not os.path.exists(os.path.join(BASE_SEARCH_DIRECTORY, "subfolder", "meeting_notes.txt")):
    with open(os.path.join(BASE_SEARCH_DIRECTORY, "subfolder", "meeting_notes.txt"), "w") as f:
        f.write("Meeting notes for today, discussing security and project status.")
if not os.path.exists(os.path.join(BASE_SEARCH_DIRECTORY, "subfolder", "data.json")):
    with open(os.path.join(BASE_SEARCH_DIRECTORY, "subfolder", "data.json"), "w") as f:
        f.write("{ \"name\": \"example\", \"value\": 123 }")

@app.route('/api/file-search/search', methods=['GET'])
def search_files():
    search_term = request.args.get('searchTerm')
    file_extension_filter = request.args.get('fileExtensionFilter')
    min_size_kb = request.args.get('minSizeKb', type=int)
    max_size_kb = request.args.get('maxSizeKb', type=int)
    search_content = request.args.get('searchContent', type=lambda v: v.lower() == 'true') # Convert to boolean

    if not search_term:
        return jsonify({"error": "Search term cannot be empty."}), 400

    if not os.path.isdir(BASE_SEARCH_DIRECTORY):
        return jsonify({"error": f"Base search directory not found: {BASE_SEARCH_DIRECTORY}"}), 500

    found_files = []

    try:
        for root, _, files in os.walk(BASE_SEARCH_DIRECTORY):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                
                try:
                    file_info = os.stat(file_path)
                    file_size_bytes = file_info.st_size
                    file_size_kb = file_size_bytes / 1024

                    # Apply file extension filter
                    if file_extension_filter:
                        # Ensure extension filter starts with a dot if provided
                        expected_extension = file_extension_filter if file_extension_filter.startswith('.') else f".{file_extension_filter}"
                        if not file_name.lower().endswith(expected_extension.lower()):
                            continue

                    # Apply size filters
                    if min_size_kb is not None and file_size_kb < min_size_kb:
                        continue
                    if max_size_kb is not None and file_size_kb > max_size_kb:
                        continue
                    
                    matches_search_term = False

                    # Search by file name
                    if search_term.lower() in file_name.lower():
                        matches_search_term = True
                    
                    # Search by content
                    if search_content and not matches_search_term:
                        # Try to read common text files, skip binary for content search
                        _, ext = os.path.splitext(file_name)
                        if ext.lower() in ('.txt', '.log', '.json', '.xml'):
                            try:
                                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                    content = f.read()
                                if search_term.lower() in content.lower():
                                    matches_search_term = True
                            except Exception as e:
                                # Log or ignore errors during content read (e.g., permission, encoding)
                                print(f"Error reading file {file_path} for content search: {e}")
                                pass # Skip this file for content search

                    if matches_search_term:
                        found_files.append({
                            "fileName": file_name,
                            "filePath": file_path,
                            "fileSizeKb": round(file_size_kb, 2),
                            "lastModified": datetime.datetime.fromtimestamp(file_info.st_mtime).isoformat()
                        })
                except PermissionError:
                    print(f"Permission denied for: {file_path}. Skipping.")
                    continue
                except FileNotFoundError:
                    print(f"File not found during iteration (might have been moved/deleted): {file_path}. Skipping.")
                    continue
                except Exception as e:
                    print(f"An unexpected error occurred for {file_path}: {e}. Skipping.")
                    continue

        # Sort files by name for consistent output
        found_files.sort(key=lambda x: x['fileName'].lower())

        return jsonify({
            "searchTerm": search_term,
            "filtersApplied": {
                "fileExtensionFilter": file_extension_filter,
                "minSizeKb": min_size_kb,
                "maxSizeKb": max_size_kb,
                "searchContent": search_content
            },
            "foundFilesCount": len(found_files),
            "files": found_files
        }), 200

    except PermissionError:
        return jsonify({"error": f"Access denied to one or more directories within '{BASE_SEARCH_DIRECTORY}'."}), 403
    except Exception as e:
        return jsonify({"error": f"An error occurred during file search: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
💻 Dil: TypeScript (Node.js)

🤖 AI: Gemini

TypeScript

import express, { Request, Response } from 'express';
import path from 'path';
import fs from 'fs/promises';
import { statSync } from 'fs'; // Synchronous stat for convenience within map/filter
import { createReadStream } from 'fs'; // For content search
import { createInterface } from 'readline'; // For reading files line by line

const app = express();
const PORT = 3000;

const baseSearchDirectory = path.join(__dirname, 'temp_search_dir');

// Ensure base search directory exists and create dummy files for demonstration
async function setupSearchDirectory() {
    await fs.mkdir(baseSearchDirectory, { recursive: true }).catch(console.error);
    const subfolderPath = path.join(baseSearchDirectory, 'subfolder');
    await fs.mkdir(subfolderPath, { recursive: true }).catch(console.error);

    const filesToCreate = [
        { name: 'document1.txt', content: 'This is a test document with some keywords like important.' },
        { name: 'report_2023.pdf', content: '%PDF-1.4\n%This is a dummy PDF file.\nKeywords: financial report.', binary: true }, // Dummy binary content
        { name: 'image.jpg', content: 'dummy binary data', binary: true },
        { name: 'subfolder/meeting_notes.txt', content: 'Meeting notes for today, discussing security and project status.' },
        { name: 'subfolder/data.json', content: '{ "name": "example", "value": 123 }' }
    ];

    for (const file of filesToCreate) {
        const filePath = path.join(baseSearchDirectory, file.name);
        if (!await fs.access(filePath).then(() => true).catch(() => false)) {
            if (file.binary) {
                await fs.writeFile(filePath, Buffer.from(file.content));
            } else {
                await fs.writeFile(filePath, file.content);
            }
        }
    }
}
setupSearchDirectory();

// Function to recursively get all file paths
async function getFilePaths(dir: string): Promise<string[]> {
    let filePaths: string[] = [];
    const items = await fs.readdir(dir);

    for (const item of items) {
        const itemPath = path.join(dir, item);
        let stats;
        try {
            stats = await fs.stat(itemPath);
        } catch (error: any) {
            // Ignore permission errors or other errors for individual files/dirs
            if (error.code === 'EACCES') {
                console.warn(`Permission denied for: ${itemPath}. Skipping.`);
                continue;
            }
            throw error; // Re-throw other unexpected errors
        }

        if (stats.isFile()) {
            filePaths.push(itemPath);
        } else if (stats.isDirectory()) {
            filePaths = filePaths.concat(await getFilePaths(itemPath));
        }
    }
    return filePaths;
}

// Function to search content of a text-based file
async function searchFileContent(filePath: string, searchTerm: string): Promise<boolean> {
    const readableStream = createReadStream(filePath, { encoding: 'utf8' });
    const rl = createInterface({
        input: readableStream,
        crlfDelay: Infinity
    });

    for await (const line of rl) {
        if (line.toLowerCase().includes(searchTerm.toLowerCase())) {
            readableStream.close(); // Close the stream as soon as a match is found
            return true;
        }
    }
    return false;
}

app.get('/api/file-search/search', async (req: Request, res: Response) => {
    const searchTerm = req.query.searchTerm as string;
    const fileExtensionFilter = req.query.fileExtensionFilter as string | undefined;
    const minSizeKb = req.query.minSizeKb ? parseInt(req.query.minSizeKb as string) : undefined;
    const maxSizeKb = req.query.maxSizeKb ? parseInt(req.query.maxSizeKb as string) : undefined;
    const searchContent = (req.query.searchContent as string)?.toLowerCase() === 'true';

    if (!searchTerm) {
        return res.status(400).json({ error: "Search term cannot be empty." });
    }

    try {
        await fs.access(baseSearchDirectory); // Check if base directory is accessible

        const allFilePaths = await getFilePaths(baseSearchDirectory);
        const foundFiles: any[] = [];

        for (const filePath of allFilePaths) {
            let fileStats;
            try {
                fileStats = statSync(filePath); // Use sync version for direct stat access in loop
            } catch (error: any) {
                if (error.code === 'EACCES') {
                    console.warn(`Permission denied for: ${filePath}. Skipping.`);
                    continue;
                }
                console.error(`Error getting stats for ${filePath}: ${error.message}. Skipping.`);
                continue;
            }

            const fileName = path.basename(filePath);
            const fileExtension = path.extname(fileName).toLowerCase();
            const fileSizeKb = fileStats.size / 1024;

            // Apply file extension filter
            if (fileExtensionFilter && fileExtension !== `.${fileExtensionFilter.toLowerCase()}`) {
                continue;
            }

            // Apply size filters
            if (minSizeKb !== undefined && fileSizeKb < minSizeKb) {
                continue;
            }
            if (maxSizeKb !== undefined && fileSizeKb > maxSizeKb) {
                continue;
            }

            let matchesSearchTerm = false;

            // Search by file name
            if (fileName.toLowerCase().includes(searchTerm.toLowerCase())) {
                matchesSearchTerm = true;
            }

            // Search by content if requested and not already matched by name
            if (searchContent && !matchesSearchTerm) {
                // Only try to read common text files, avoid binary files
                const readableExtensions = ['.txt', '.log', '.json', '.xml'];
                if (readableExtensions.includes(fileExtension)) {
                    try {
                        const contentMatched = await searchFileContent(filePath, searchTerm);
                        if (contentMatched) {
                            matchesSearchTerm = true;
                        }
                    } catch (contentError: any) {
                        console.warn(`Could not read content for ${filePath}: ${contentError.message}. Skipping content search.`);
                        // Continue to next file, don't break the whole search
                    }
                }
            }

            if (matchesSearchTerm) {
                foundFiles.push({
                    fileName: fileName,
                    filePath: filePath,
                    fileSizeKb: parseFloat(fileSizeKb.toFixed(2)),
                    lastModified: fileStats.mtime.toISOString()
                });
            }
        }

        // Sort files by name
        foundFiles.sort((a, b) => a.fileName.localeCompare(b.fileName));

        return res.status(200).json({
            searchTerm: searchTerm,
            filtersApplied: { fileExtensionFilter, minSizeKb, maxSizeKb, searchContent },
            foundFilesCount: foundFiles.length,
            files: foundFiles
        });

    } catch (error: any) {
        if (error.code === 'ENOENT') {
            return res.status(404).json({ error: `Base search directory not found: ${baseSearchDirectory}` });
        }
        if (error.code === 'EACCES' || error.code === 'EPERM') {
            return res.status(403).json({ error: `Access denied to the base search directory: ${baseSearchDirectory}` });
        }
        return res.status(500).json({ error: `An error occurred during file search: ${error.message}` });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
🧪 Senaryo 9: Bir veritabanı yönetim aracında kullanıcılar veritabanı adını girip işlem yapabilir. Sistem belirtilen veritabanı üzerinde işlemleri gerçekleştirir. İşlem sonuçları kullanıcıya raporlanır. Veritabanı durumu gösterilir.
💻 Dil: C#

🤖 AI: Gemini

C#

using Microsoft.AspNetCore.Mvc;
using System.Data;
using System.Data.SqlClient; // Example for SQL Server
using System.Threading.Tasks;
using System.Collections.Generic;
using System;

[ApiController]
[Route("api/[controller]")]
public class DatabaseManagerController : ControllerBase
{
    // In a real application, connection strings would be loaded securely (e.g., from appsettings.json)
    private readonly string _connectionStringTemplate = "Server=localhost;Database={0};Integrated Security=True;TrustServerCertificate=True;";

    private string GetConnectionString(string databaseName)
    {
        return string.Format(_connectionStringTemplate, databaseName);
    }

    [HttpGet("status")]
    public async Task<IActionResult> GetDatabaseStatus([FromQuery] string databaseName)
    {
        if (string.IsNullOrWhiteSpace(databaseName))
        {
            return BadRequest("Database name cannot be empty.");
        }

        string connectionString = GetConnectionString("master"); // Connect to master to check other DBs
        using var connection = new SqlConnection(connectionString);

        try
        {
            await connection.OpenAsync();
            var command = new SqlCommand(<span class="math-inline">"SELECT state\_desc FROM sys\.databases WHERE name \= @databaseName", connection\);
command\.Parameters\.AddWithValue\("@databaseName", databaseName\);
var state \= \(string?\)await command\.ExecuteScalarAsync\(\);
if \(state \=\= null\)
\{
return NotFound\(</span>"Database '{databaseName}' not found or no access to master database.");
            }

            // More detailed status (simplified for example)
            var detailedStatus = new
            {
                DatabaseName = databaseName,
                State = state,
                IsOnline = state == "ONLINE",
                LastBackupDate = (DateTime?)null // Placeholder, would query msdb..backupset
            };

            return Ok(detailedStatus);
        }
        catch (SqlException ex)
        {
            // Specific handling for SQL exceptions (e.g., login failed, server not found)
            return StatusCode(500, $"Database status check failed: {ex.Message}");
        }
        catch (Exception ex)
        {
            return StatusCode(500, $"An unexpected error occurred: {ex.Message}");
        }
    }

    [HttpPost("execute-query")]
    public async Task<IActionResult> ExecuteQuery(
        [FromForm] string databaseName,
        [FromForm] string query)
    {
        if (string.IsNullOrWhiteSpace(databaseName))
        {
            return BadRequest("Database name cannot be empty.");
        }
        if (string.IsNullOrWhiteSpace(query))
        {
            return BadRequest("Query cannot be empty.");
        }

        string connectionString = GetConnectionString(databaseName);
        using var connection = new SqlConnection(connectionString);

        try
        {
            await connection.OpenAsync();
            using var command = new SqlCommand(query, connection);

            if (query.Trim().ToUpper().StartsWith("SELECT"))
            {
                var dataTable = new DataTable();
                using var adapter = new SqlDataAdapter(command);
                adapter.Fill(dataTable);

                var rows = new List<Dictionary<string, object>>();
                foreach (DataRow row in dataTable.Rows)
                {
                    var rowData = new Dictionary<string, object>();
                    foreach (DataColumn col in dataTable.Columns)
                    {
                        rowData[col.ColumnName] = row[col];
                    }
                    rows.Add(rowData);
                }

                return Ok(new {
                    message = "Query executed successfully.",
                    queryType = "SELECT",
                    rowCount = rows.Count,
                    results = rows
                });
            }
            else // DDL/DML operations
            {
                int affectedRows = await command.ExecuteNonQueryAsync();
                return Ok(new {
                    message = "Command executed successfully.",
                    queryType = "DML/DDL",
                    affectedRows = affectedRows
                });
            }
        }
        catch (SqlException ex)
        {
            return StatusCode(500, $"Database query failed: {ex.Message}");
        }
        catch (Exception ex)
        {
            return StatusCode(500, <span class="math-inline">"An unexpected error occurred\: \{ex\.Message\}"\);
\}
\}
// Example\: Create a new database \(usually requires elevated permissions\)
\[HttpPost\("create\-database"\)\]
public async Task<IActionResult\> CreateDatabase\(\[FromForm\] string newDatabaseName\)
\{
if \(string\.IsNullOrWhiteSpace\(newDatabaseName\)\)
\{
return BadRequest\("New database name cannot be empty\."\);
\}
// Connect to master to create a new database
string connectionString \= GetConnectionString\("master"\); 
using var connection \= new SqlConnection\(connectionString\);
try
\{
await connection\.OpenAsync\(\);
// Sanitize input to prevent SQL Injection for database names if not using parameters \(less common for DB names\)
// Or ensure the user role only allows specific actions\.
var command \= new SqlCommand\(</span>"CREATE DATABASE {newDatabaseName}", connection);
            await command.ExecuteNonQueryAsync();
            return Ok(<span class="math-inline">"Database '\{newDatabaseName\}' created successfully\."\);
\}
catch \(SqlException ex\)
\{
if \(ex\.Number \=\= 1802\) // Error code for database already exists
\{
return Conflict\(</span>"Database '{newDatabaseName}' already exists.");
            }
            return StatusCode(500, $"Failed to create database: {ex.Message}");
        }
        catch (Exception ex)
        {
            return StatusCode(500, $"An unexpected error occurred: {ex.Message}");
        }
    }
}
💻 Dil: Python

🤖 AI: Gemini

Python

import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Using SQLite for demonstration simplicity.
# For other databases (PostgreSQL, MySQL), you'd use respective drivers (psycopg2, mysql-connector-python).
DATABASE_DIR = 'databases'
app.config['DATABASE_DIR'] = DATABASE_DIR
os.makedirs(DATABASE_DIR, exist_ok=True)

def get_db_connection(db_name):
    db_path = os.path.join(app.config['DATABASE_DIR'], f"{db_name}.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row # Return rows as dict-like objects
    return conn

@app.route('/api/database-manager/status', methods=['GET'])
def get_database_status():
    database_name = request.args.get('databaseName')

    if not database_name:
        return jsonify({"error": "Database name cannot be empty."}), 400

    db_file_path = os.path.join(app.config['DATABASE_DIR'], f"{database_name}.db")

    if not os.path.exists(db_file_path):
        return jsonify({"error": f"Database '{database_name}' not found."}), 404
    
    try:
        conn = get_db_connection(database_name)
        conn.close() # Just try to open and close to check accessibility

        # In a real system, you might check table counts, last modified, etc.
        # For SQLite, the file presence and ability to open it is the primary status.
        db_status = {
            "databaseName": database_name,
            "exists": True,
            "filePath": db_file_path,
            "sizeBytes": os.path.getsize(db_file_path),
            "status": "Online (Accessible)" # Simplified
        }
        return jsonify(db_status), 200
    except sqlite3.Error as e:
        return jsonify({"error": f"Database status check failed for '{database_name}': {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/api/database-manager/execute-query', methods=['POST'])
def execute_query():
    database_name = request.json.get('databaseName')
    query = request.json.get('query')

    if not database_name:
        return jsonify({"error": "Database name cannot be empty."}), 400
    if not query:
        return jsonify({"error": "Query cannot be empty."}), 400
    
    db_file_path = os.path.join(app.config['DATABASE_DIR'], f"{database_name}.db")
    if not os.path.exists(db_file_path):
        return jsonify({"error": f"Database '{database_name}' not found."}), 404

    conn = None
    try:
        conn = get_db_connection(database_name)
        cursor = conn.cursor()

        query_upper = query.strip().upper()
        
        if query_upper.startswith("SELECT"):
            cursor.execute(query)
            rows = cursor.fetchall()
            results = [dict(row) for row in rows] # Convert Row objects to dictionaries
            return jsonify({
                "message": "Query executed successfully.",
                "queryType": "SELECT",
                "rowCount": len(results),
                "results": results
            }), 200
        else: # DDL/DML operations
            cursor.execute(query)
            conn.commit()
            return jsonify({
                "message": "Command executed successfully.",
                "queryType": "DML/DDL",
                "affectedRows": cursor.rowcount
            }), 200
    except sqlite3.Error as e:
        if conn:
            conn.rollback() # Rollback on error for DML/DDL
        return jsonify({"error": f"Database query failed: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
    finally:
        if conn:
            conn.close()

@app.route('/api/database-manager/create-database', methods=['POST'])
def create_database():
    new_database_name = request.json.get('newDatabaseName')

    if not new_database_name:
        return jsonify({"error": "New database name cannot be empty."}), 400
    
    db_file_path = os.path.join(app.config['DATABASE_DIR'], f"{new_database_name}.db")

    if os.path.exists(db_file_path):
        return jsonify({"error": f"Database '{new_database_name}' already exists."}), 409 # Conflict

    try:
        conn = sqlite3.connect(db_file_path)
        conn.close()
        return jsonify({"message": f"Database '{new_database_name}' created successfully."}), 201 # Created
    except Exception as e:
        return jsonify({"error": f"Failed to create database: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
💻 Dil: TypeScript (Node.js)

🤖 AI: Gemini

TypeScript

import express, { Request, Response } from 'express';
import sqlite3 from 'sqlite3'; // Using sqlite3 for simplicity in Node.js
import { open } from 'sqlite'; // Using sqlite package for async/await with sqlite3
import path from 'path';
import fs from 'fs/promises';

const app = express();
const PORT = 3000;

const databaseDirectory = path.join(__dirname, 'databases');

// Ensure database directory exists
fs.mkdir(databaseDirectory, { recursive: true }).catch(console.error);

app.use(express.json());

async function getDb(dbName: string) {
    const dbFilePath = path.join(databaseDirectory, `${dbName}.db`);
    // 'open' function from 'sqlite' package to open the database
    return open({
        filename: dbFilePath,
        driver: sqlite3.Database
    });
}

app.get('/api/database-manager/status', async (req: Request, res: Response) => {
    const databaseName = req.query.databaseName as string;

    if (!databaseName) {
        return res.status(400).json({ error: "Database name cannot be empty." });
    }

    const dbFilePath = path.join(databaseDirectory, `${databaseName}.db`);

    try {
        await fs.access(dbFilePath); // Check if file exists
        const stats = await fs.stat(dbFilePath); // Get file stats for size

        // Attempt to open and close to confirm accessibility
        const db = await getDb(databaseName);
        await db.close();

        const dbStatus = {
            databaseName: databaseName,
            exists: true,
            filePath: dbFilePath,
            sizeBytes: stats.size,
            status: "Online (Accessible)" // Simplified for SQLite
        };
        return res.status(200).json(dbStatus);

    } catch (error: any) {
        if (error.code === 'ENOENT') {
            return res.status(404).json({ error: `Database '${databaseName}' not found.` });
        }
        if (error.code === 'SQLITE_CANTOPEN' || error.code === 'EACCES') {
            return res.status(500).json({ error: `Database access failed for '${databaseName}': ${error.message}` });
        }
        return res.status(500).json({ error: `An unexpected error occurred: ${error.message}` });
    }
});

app.post('/api/database-manager/execute-query', async (req: Request, res: Response) => {
    const { databaseName, query } = req.body;

    if (!databaseName) {
        return res.status(400).json({ error: "Database name cannot be empty." });
    }
    if (!query) {
        return res.status(400).json({ error: "Query cannot be empty." });
    }

    const dbFilePath = path.join(databaseDirectory, `${databaseName}.db`);
    if (!await fs.access(dbFilePath).then(() => true).catch(() => false)) {
        return res.status(404).json({ error: `Database '${databaseName}' not found.` });
    }

    let db;
    try {
        db = await getDb(databaseName);

        if (query.trim().toUpperCase().startsWith("SELECT")) {
            const rows = await db.all(query); // db.all for SELECT queries
            return res.status(200).json({
                message: "Query executed successfully.",
                queryType: "SELECT",
                rowCount: rows.length,
                results: rows
            });
        } else { // DDL/DML operations
            const result = await db.run(query); // db.run for DML/DDL queries
            return res.status(200).json({
                message: "Command executed successfully.",
                queryType: "DML/DDL",
                affectedRows: result.changes || 0 // .changes property holds affected rows
            });
        }
    } catch (error: any) {
        // SQLite errors often have a 'code' property
        if (error.code && error.code.startsWith('SQLITE_')) {
            return res.status(500).json({ error: `Database query failed: ${error.message} (Code: ${error.code})` });
        }
        return res.status(500).json({ error: `An unexpected error occurred: ${error.message}` });
    } finally {
        if (db) {
            await db.close();
        }
    }
});

app.post('/api/database-manager/create-database', async (req: Request, res: Response) => {
    const { newDatabaseName } = req.body;

    if (!newDatabaseName) {
        return res.status(400).json({ error: "New database name cannot be empty." });
    }

    const dbFilePath = path.join(databaseDirectory, `${newDatabaseName}.db`);

    if (await fs.access(dbFilePath).then(() => true).catch(() => false)) {
        return res.status(409).json({ error: `Database '${newDatabaseName}' already exists.` }); // Conflict
    }

    let db;
    try {
        db = await getDb(newDatabaseName); // This creates the file if it doesn't exist
        await db.close();
        return res.status(201).json({ message: `Database '${newDatabaseName}' created successfully.` }); // Created
    } catch (error: any) {
        console.error(`Error creating database ${newDatabaseName}:`, error);
        return res.status(500).json({ error: `Failed to create database: ${error.message}` });
    } finally {
        if (db) {
            await db.close();
        }
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
🧪 Senaryo 10: Bir sistem güvenlik aracında kullanıcılar tarama parametrelerini belirtebilir. Sistem belirtilen parametrelerle güvenlik taraması yapar. Tarama sonuçları detaylı rapor halinde sunulur. Güvenlik durumu değerlendirilir.
💻 Dil: C#

🤖 AI: Gemini

C#

using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

[ApiController]
[Route("api/[controller]")]
public class SecurityScannerController : ControllerBase
{
    private readonly string _scanTargetDirectory = "C:\\ScanTarget"; // Example directory to scan
    private readonly string _reportOutputDirectory = "SecurityReports";

    public SecurityScannerController()
    {
        Directory.CreateDirectory(_scanTargetDirectory);
        Directory.CreateDirectory(_reportOutputDirectory);

        // Create some dummy files with potential "vulnerabilities" for testing
        if (!System.IO.File.Exists(Path.Combine(_scanTargetDirectory, "credentials.txt")))
        {
            System.IO.File.WriteAllText(Path.Combine(_scanTargetDirectory, "credentials.txt"), "admin:password123\nuser:weakpass");
        }
        if (!System.IO.File.Exists(Path.Combine(_scanTargetDirectory, "public_key.pem")))
        {
            System.IO.File.WriteAllText(Path.Combine(_scanTargetDirectory, "public_key.pem"), "---BEGIN PUBLIC KEY---...");
        }
        if (!System.IO.File.Exists(Path.Combine(_scanTargetDirectory, "config.xml")))
        {
            System.IO.File.WriteAllText(Path.Combine(_scanTargetDirectory, "config.xml"), "<config><debugMode>true</debugMode></config>");
        }
        if (!System.IO.File.Exists(Path.Combine(_scanTargetDirectory, "normal_file.txt")))
        {
            System.IO.File.WriteAllText(Path.Combine(_scanTargetDirectory, "normal_file.txt"), "This is a regular file.");
        }
        Directory.CreateDirectory(Path.Combine(_scanTargetDirectory, "sensitive_data"));
        if (!System.IO.File.Exists(Path.Combine(_scanTargetDirectory, "sensitive_data", "social_security.csv")))
        {
            System.IO.File.WriteAllText(Path.Combine(_scanTargetDirectory, "sensitive_data", "social_security.csv"), "Name,SSN\nJohn Doe,123-45-6789");
        }
    }

    public class ScanParameters
    {
        public bool ScanForWeakPasswords { get; set; } = true;
        public bool ScanForSensitiveFiles { get; set; } = true;
        public bool ScanForDebugFlags { get; set; } = true;
        public string[]? ExcludeExtensions { get; set; }
        public string[]? IncludeKeywords { get; set; }
    }

    public class ScanResultEntry
    {
        public string FilePath { get; set; } = string.Empty;
        public string Severity { get; set; } = string.Empty; // High, Medium, Low, Info
        public string Issue { get; set; } = string.Empty;
        public string? Context { get; set; } // Snippet of the line/content
    }

    [HttpPost("start-scan")]
    public async Task<IActionResult> StartSecurityScan([FromBody] ScanParameters parameters)
    {
        if (!Directory.Exists(_scanTargetDirectory))
        {
            return StatusCode(500, $"Scan target directory not found: {_scanTargetDirectory}");
        }

        var scanResults = new List<ScanResultEntry>();

        try
        {
            var allFiles = Directory.EnumerateFiles(_scanTargetDirectory, "*", SearchOption.AllDirectories);

            foreach (var filePath in allFiles)
            {
                var fileExtension = Path.GetExtension(filePath).ToLowerInvariant();
                if (parameters.ExcludeExtensions != null && parameters.ExcludeExtensions.Contains(fileExtension))
                {
                    continue; // Skip excluded extensions
                }

                string fileContent;
                try
                {
                    // Only read text files to avoid issues with binary files
                    if (!IsTextFile(filePath)) continue; 
                    fileContent = await System.IO.File.ReadAllTextAsync(filePath);
                }
                catch (IOException) { continue; /* File in use, skip */ }
                catch (UnauthorizedAccessException) { continue; /* Access denied, skip */ }
                catch (Exception) { continue; /* Other read errors, skip */ }

                // --- Scan for Weak Passwords ---
                if (parameters.ScanForWeakPasswords)
                {
                    if (fileContent.Contains("password123", StringComparison.OrdinalIgnoreCase) ||
                        fileContent.Contains("weakpass", StringComparison.OrdinalIgnoreCase))
                    {
                        scanResults.Add(new ScanResultEntry
                        {
                            FilePath = filePath,
                            Severity = "High",
                            Issue = "Found common weak password string.",
                            Context = GetContextLine(fileContent, "password123") ?? GetContextLine(fileContent, "weakpass")
                        });
                    }
                }

                // --- Scan for Sensitive File Names/Patterns ---
                if (parameters.ScanForSensitiveFiles)
                {
                    var fileNameLower = Path.GetFileName(filePath).ToLowerInvariant();
                    if (fileNameLower.Contains("credentials") || fileNameLower.Contains("secret") || fileNameLower.Contains("private_key") ||
                        fileNameLower.Contains("ssn") || fileNameLower.Contains("social_security"))
                    {
                        scanResults.Add(new ScanResultEntry
                        {
                            FilePath = filePath,
                            Severity = "Medium",
                            Issue = "Found file with potentially sensitive name.",
                            Context = null
                        });
                    }
                    if (fileContent.Contains("SSN:") || fileContent.Contains("social_security_number")) // Simple content check
                    {
                         scanResults.Add(new ScanResultEntry
                        {
                            FilePath = filePath,
                            Severity = "High",
                            Issue = "File content indicates presence of Social Security Numbers.",
                            Context = GetContextLine(fileContent, "SSN:")
                        });
                    }
                }

                // --- Scan for Debug Flags ---
                if (parameters.ScanForDebugFlags)
                {
                    if (fileContent.Contains("debugMode: true", StringComparison.OrdinalIgnoreCase) ||
                        fileContent.Contains("<debugMode>true</debugMode>", StringComparison.OrdinalIgnoreCase))
                    {
                        scanResults.Add(new ScanResultEntry
                        {
                            FilePath = filePath,
                            Severity = "Low",
                            Issue = "Potential debug flag enabled in configuration.",
                            Context = GetContextLine(fileContent, "debugMode")
                        });
                    }
                }

                // --- Scan for Custom Keywords ---
                if (parameters.IncludeKeywords != null && parameters.IncludeKeywords.Any())
                {
                    foreach (var keyword in parameters.IncludeKeywords)
                    {
                        if (fileContent.Contains(keyword, StringComparison.OrdinalIgnoreCase))
                        {
                            scanResults.Add(new ScanResultEntry
                            {
                                FilePath = filePath,
                                Severity = "Info",
                                Issue = $"Custom keyword '{keyword}' found.",
                                Context = GetContextLine(fileContent, keyword)
                            });
                        }
                    }
                }
            }

            string reportFileName = <span class="math-inline">"SecurityReport\_\{DateTime\.Now\:yyyyMMddHHmmss\}\.json";
string reportFilePath \= Path\.Combine\(\_reportOutputDirectory, reportFileName\);
var fullReport \= new
\{
ScanTime \= DateTime\.Now,
ScanTarget \= \_scanTargetDirectory,
ScanParameters \= parameters,
TotalFilesScanned \= allFiles\.Count\(\),
TotalIssuesFound \= scanResults\.Count,
SecurityAssessment \= AssessOverallSecurity\(scanResults\),
ScanResults \= scanResults\.OrderByDescending\(r \=\> GetSeverityOrder\(r\.Severity\)\)\.ToList\(\)
\};
await System\.IO\.File\.WriteAllTextAsync\(reportFilePath, System\.Text\.Json\.JsonSerializer\.Serialize\(fullReport, new System\.Text\.Json\.JsonSerializerOptions \{ WriteIndented \= true \}\)\);
return Ok\(new \{
message \= "Security scan completed\.",
reportFileName \= reportFileName,
reportFilePath \= reportFilePath,
summary \= new \{
totalIssues \= scanResults\.Count,
highSeverity \= scanResults\.Count\(r \=\> r\.Severity \=\= "High"\),
mediumSeverity \= scanResults\.Count\(r \=\> r\.Severity \=\= "Medium"\),
lowSeverity \= scanResults\.Count\(r \=\> r\.Severity \=\= "Low"\)
\}
\}\);
\}
catch \(UnauthorizedAccessException\)
\{
return Forbid\(</span>"Access denied to one or more directories within '{_scanTargetDirectory}'.");
        }
        catch (Exception ex)
        {
            return StatusCode(500, $"An error occurred during the security scan: {ex.Message}");
        }
    }

    private string? GetContextLine(string content, string keyword)
    {
        var lines = content.Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries);
        foreach (var line in lines)
        {
            if (line.Contains(keyword, StringComparison.OrdinalIgnoreCase))
            {
                return line.Trim();
            }
        }
        return null;
    }

    private bool IsTextFile(string filePath)
    {
        // Simple check based on extension. More robust would involve checking file headers.
        string extension = Path.GetExtension(filePath).ToLowerInvariant();
        return new[] { ".txt", ".log", ".conf", ".config", ".xml", ".json", ".ini", ".csv", ".js", ".cs", ".py", ".ts" }.Contains(extension);
    }

    private string AssessOverallSecurity(List<ScanResultEntry> results)
    {
        if (results.Any(r => r.Severity == "High"))
        {
            return "Critical: High severity issues found. Immediate action required.";
        }
        if (results.Any(r => r.Severity == "Medium"))
        {
            return "Warning: Medium severity issues found. Review and mitigate.";
        }
        if (results.Any())
        {
            return "Informational: Low severity or informational findings. Review as needed.";
        }
        return "Clean: No significant security issues detected.";
    }

    private int GetSeverityOrder(string severity)
    {
        return severity switch
        {
            "High" => 3,
            "Medium" => 2,
            "Low" => 1,
            _ => 0
        };
    }
}
💻 Dil: Python

🤖 AI: Gemini

Python

import os
import json
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

SCAN_TARGET_DIRECTORY = 'scan_target'
REPORT_OUTPUT_DIRECTORY = 'security_reports'

os.makedirs(SCAN_TARGET_DIRECTORY, exist_ok=True)
os.makedirs(REPORT_OUTPUT_DIRECTORY, exist_ok=True)
os.makedirs(os.path.join(SCAN_TARGET_DIRECTORY, 'sensitive_data'), exist_ok=True)

# Create some dummy files with potential "vulnerabilities" for testing
if not os.path.exists(os.path.join(SCAN_TARGET_DIRECTORY, "credentials.txt")):
    with open(os.path.join(SCAN_TARGET_DIRECTORY, "credentials.txt"), "w") as f:
        f.write("admin:password123\nuser:weakpass")
if not os.path.exists(os.path.join(SCAN_TARGET_DIRECTORY, "public_key.pem")):
    with open(os.path.join(SCAN_TARGET_DIRECTORY, "public_key.pem"), "w") as f:
        f.write("---BEGIN PUBLIC KEY---...")
if not os.path.exists(os.path.join(SCAN_TARGET_DIRECTORY, "config.xml")):
    with open(os.path.join(SCAN_TARGET_DIRECTORY, "config.xml"), "w") as f:
        f.write("<config><debugMode>true</debugMode></config>")
if not os.path.exists(os.path.join(SCAN_TARGET_DIRECTORY, "normal_file.txt")):
    with open(os.path.join(SCAN_TARGET_DIRECTORY, "normal_file.txt"), "w") as f:
        f.write("This is a regular file.")
if not os.path.exists(os.path.join(SCAN_TARGET_DIRECTORY, "sensitive_data", "social_security.csv")):
    with open(os.path.join(SCAN_TARGET_DIRECTORY, "sensitive_data", "social_security.csv"), "w") as f:
        f.write("Name,SSN\nJohn Doe,123-45-6789")

def get_context_line(content, keyword):
    for line in content.splitlines():
        if keyword.lower() in line.lower():
            return line.strip()
    return None

def is_text_file(filepath):
    # Simple check based on common text file extensions
    text_extensions = {'.txt', '.log', '.conf', '.config', '.xml', '.json', '.ini', '.csv', '.js', '.py', '.ts', '.cs'}
    _, ext = os.path.splitext(filepath)
    return ext.lower() in text_extensions

def assess_overall_security(results):
    severities = [r['severity'] for r in results]
    if "High" in severities:
        return "Critical: High severity issues found. Immediate action required."
    if "Medium" in severities:
        return "Warning: Medium severity issues found. Review and mitigate."
    if severities:
        return "Informational: Low severity or informational findings. Review as needed."
    return "Clean: No significant security issues detected."

def get_severity_order(severity):
    return {"High": 3, "Medium": 2, "Low": 1, "Info": 0}.get(severity, 0)

@app.route('/api/security-scanner/start-scan', methods=['POST'])
def start_security_scan():
    parameters = request.json
    scan_for_weak_passwords = parameters.get('scanForWeakPasswords', True)
    scan_for_sensitive_files = parameters.get('scanForSensitiveFiles', True)
    scan_for_debug_flags = parameters.get('scanForDebugFlags', True)
    exclude_extensions = [ext.lower() for ext in parameters.get('excludeExtensions', [])]
    include_keywords = [kw.lower() for kw in parameters.get('includeKeywords', [])]

    if not os.path.isdir(SCAN_TARGET_DIRECTORY):
        return jsonify({"error": f"Scan target directory not found: {SCAN_TARGET_DIRECTORY}"}), 500

    scan_results = []
    total_files_scanned = 0

    try:
        for root, _, files in os.walk(SCAN_TARGET_DIRECTORY):
            for file_name in files:
                total_files_scanned += 1
                file_path = os.path.join(root, file_name)
                file_extension = os.path.splitext(file_name)[1].lower()

                if file_extension in exclude_extensions:
                    continue

                if not is_text_file(file_path):
                    continue # Skip binary files for content scanning

                file_content = ""
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        file_content = f.read()
                except PermissionError:
                    print(f"Permission denied for: {file_path}. Skipping.")
                    continue
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}. Skipping.")
                    continue

                # --- Scan for Weak Passwords ---
                if scan_for_weak_passwords:
                    if "password123" in file_content.lower() or "weakpass" in file_content.lower():
                        scan_results.append({
                            "filePath": file_path,
                            "severity": "High",
                            "issue": "Found common weak password string.",
                            "context": get_context_line(file_content, "password123") or get_context_line(file_content, "weakpass")
                        })
                
                # --- Scan for Sensitive File Names/Patterns ---
                if scan_for_sensitive_files:
                    file_name_lower = file_name.lower()
                    if any(kw in file_name_lower for kw in ["credentials", "secret", "private_key", "ssn", "social_security"]):
                        scan_results.append({
                            "filePath": file_path,
                            "severity": "Medium",
                            "issue": "Found file with potentially sensitive name.",
                            "context": None
                        })
                    if "SSN:" in file_content or "social_security_number" in file_content.lower():
                        scan_results.append({
                            "filePath": file_path,
                            "severity": "High",
                            "issue": "File content indicates presence of Social Security Numbers.",
                            "context": get_context_line(file_content, "SSN:")
                        })

                # --- Scan for Debug Flags ---
                if scan_for_debug_flags:
                    if "debugMode: true" in file_content or "<debugMode>true</debugMode>" in file_content:
                        scan_results.append({
                            "filePath": file_path,
                            "severity": "Low",
                            "issue": "Potential debug flag enabled in configuration.",
                            "context": get_context_line(file_content, "debugMode")
                        })

                # --- Scan for Custom Keywords ---
                if include_keywords:
                    for keyword in include_keywords:
                        if keyword in file_content.lower():
                            scan_results.append({
                                "filePath": file_path,
                                "severity": "Info",
                                "issue": f"Custom keyword '{keyword}' found.",
                                "context": get_context_line(file_content, keyword)
                            })

        report_file_name = f"SecurityReport_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        report_file_path = os.path.join(REPORT_OUTPUT_DIRECTORY, report_file_name)

        full_report = {
            "scanTime": datetime.datetime.now().isoformat(),
            "scanTarget": SCAN_TARGET_DIRECTORY,
            "scanParameters": parameters,
            "totalFilesScanned": total_files_scanned,
            "totalIssuesFound": len(scan_results),
            "securityAssessment": assess_overall_security(scan_results),
            "scanResults": sorted(scan_results, key=lambda x: get_severity_order(x['severity']), reverse=True)
        }

        with open(report_file_path, 'w', encoding='utf-8') as f:
            json.dump(full_report, f, indent=4)

        return jsonify({
            "message": "Security scan completed.",
            "reportFileName": report_file_name,
            "reportFilePath": report_file_path,
            "summary": {
                "totalIssues": len(scan_results),
                "highSeverity": sum(1 for r in scan_results if r['severity'] == "High"),
                "mediumSeverity": sum(1 for r in scan_results if r['severity'] == "Medium"),
                "lowSeverity": sum(1 for r in scan_results if r['severity'] == "Low")
            }
        }), 200

    except PermissionError:
        return jsonify({"error": f"Access denied to one or more directories within '{SCAN_TARGET_DIRECTORY}'."}), 403
    except Exception as e:
        return jsonify({"error": f"An error occurred during the security scan: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
💻 Dil: TypeScript (Node.js)

🤖 AI: Gemini

TypeScript

import express, { Request, Response } from 'express';
import path from 'path';
import fs from 'fs/promises';
import { createReadStream } from 'fs';
import { createInterface } from 'readline';

const app = express();
const PORT = 3000;

const scanTargetDirectory = path.join(__dirname, 'scan_target');
const reportOutputDirectory = path.join(__dirname, 'security_reports');

// Ensure directories exist and create dummy files for demonstration
async function setupScanDirectory() {
    await fs.mkdir(scanTargetDirectory, { recursive: true }).catch(console.error);
    const sensitiveDataPath = path.join(scanTargetDirectory, 'sensitive_data');
    await fs.mkdir(sensitiveDataPath, { recursive: true }).catch(console.error);

    const filesToCreate = [
        { name: 'credentials.txt', content: 'admin:password123\nuser:weakpass' },
        { name: 'public_key.pem', content: '---BEGIN PUBLIC KEY---...' },
        { name: 'config.xml', content: '<config><debugMode>true</debugMode></config>' },
        { name: 'normal_file.txt', content: 'This is a regular file.' },
        { name: 'sensitive_data/social_security.csv', content: 'Name,SSN\nJohn Doe,123-45-6789' }
    ];

    for (const file of filesToCreate) {
        const filePath = path.join(scanTargetDirectory, file.name);
        if (!await fs.access(filePath).then(() => true).catch(() => false)) {
            await fs.writeFile(filePath, file.content);
        }
    }
    await fs.mkdir(reportOutputDirectory, { recursive: true }).catch(console.error);
}
setupScanDirectory();

app.use(express.json());

interface ScanParameters {
    scanForWeakPasswords: boolean;
    scanForSensitiveFiles: boolean;
    scanForDebugFlags: boolean;
    excludeExtensions?: string[];
    includeKeywords?: string[];
}

interface ScanResultEntry {
    filePath: string;
    severity: "High" | "Medium" | "Low" | "Info";
    issue: string;
    context: string | null;
}

// Function to recursively get all file paths
async function getFilePaths(dir: string): Promise<string[]> {
    let filePaths: string[] = [];
    const items = await fs.readdir(dir);

    for (const item of items) {
        const itemPath = path.join(dir, item);
        let stats;
        try {
            stats = await fs.stat(itemPath);
        } catch (error: any) {
            if (error.code === 'EACCES') {
                console.warn(`Permission denied for: ${itemPath}. Skipping.`);
                continue;
            }
            throw error;
        }

        if (stats.isFile()) {
            filePaths.push(itemPath);
        } else if (stats.isDirectory()) {
            filePaths = filePaths.concat(await getFilePaths(itemPath));
        }
    }
    return filePaths;
}

// Function to get context line containing keyword
async function getContextLine(filePath: string, keyword: string): Promise<string | null> {
    const readableStream = createReadStream(filePath, { encoding: 'utf8' });
    const rl = createInterface({
        input: readableStream,
        crlfDelay: Infinity
    });

    for await (const line of rl) {
        if (line.toLowerCase().includes(keyword.toLowerCase())) {
            readableStream.close();
            return line.trim();
        }
    }
    return null;
}

function isTextFile(filePath: string): boolean {
    const extension = path.extname(filePath).toLowerCase();
    const textExtensions = ['.txt', '.log', '.conf', '.config', '.xml', '.json', '.ini', '.csv', '.js', '.ts', '.cs', '.py', '.md'];
    return textExtensions.includes(extension);
}

function assessOverallSecurity(results: ScanResultEntry[]): string {
    const severities = results.map(r => r.severity);
    if (severities.includes("High")) {
        return "Critical: High severity issues found. Immediate action required.";
    }
    if (severities.includes("Medium")) {
        return "Warning: Medium severity issues found. Review and mitigate.";
    }
    if (severities.length > 0) {
        return "Informational: Low severity or informational findings. Review as needed.";
    }
    return "Clean: No significant security issues detected.";
}

function getSeverityOrder(severity: string): number {
    switch (severity) {
        case "High": return 3;
        case "Medium": return 2;
        case "Low": return 1;
        case "Info": return 0;
        default: return 0;
    }
}

app.post('/api/security-scanner/start-scan', async (req: Request, res: Response) => {
    const parameters: ScanParameters = {
        scanForWeakPasswords: true,
        scanForSensitiveFiles: true,
        scanForDebugFlags: true,
        ...req.body
    };

    try {
        await fs.access(scanTargetDirectory); // Check if base directory is accessible

        const allFilePaths = await getFilePaths(scanTargetDirectory);
        const scanResults: ScanResultEntry[] = [];
        let totalFilesScanned = 0;

        for (const filePath of allFilePaths) {
            totalFilesScanned++;
            const fileExtension = path.extname(filePath).toLowerCase();
            
            if (parameters.excludeExtensions && parameters.excludeExtensions.map(ext => ext.toLowerCase()).includes(fileExtension)) {
                continue; // Skip excluded extensions
            }

            if (!isTextFile(filePath)) {
                continue; // Skip binary files for content scanning
            }

            let fileContent: string;
            try {
                fileContent = await fs.readFile(filePath, 'utf-8');
            } catch (error: any) {
                if (error.code === 'EACCES' || error.code === 'EPERM') {
                    console.warn(`Permission denied for: ${filePath}. Skipping content read.`);
                    continue;
                }
                console.error(`Error reading file ${filePath}: ${error.message}. Skipping content read.`);
                continue;
            }

            // --- Scan for Weak Passwords ---
            if (parameters.scanForWeakPasswords) {
                if (fileContent.toLowerCase().includes("password123") || fileContent.toLowerCase().includes("weakpass")) {
                    scanResults.push({
                        filePath: filePath,
                        severity: "High",
                        issue: "Found common weak password string.",
                        context: (await getContextLine(filePath, "password123")) || (await getContextLine(filePath, "weakpass"))
                    });
                }
            }

            // --- Scan for Sensitive File Names/Patterns ---
            if (parameters.scanForSensitiveFiles) {
                const fileNameLower = path.basename(filePath).toLowerCase();
                if (fileNameLower.includes("credentials") || fileNameLower.includes("secret") || fileNameLower.includes("private_key") ||
                    fileNameLower.includes("ssn") || fileNameLower.includes("social_security")) {
                    scanResults.push({
                        filePath: filePath,
                        severity: "Medium",
                        issue: "Found file with potentially sensitive name.",
                        context: null
                    });
                }
                if (fileContent.includes("SSN:") || fileContent.toLowerCase().includes("social_security_number")) {
                    scanResults.push({
                        filePath: filePath,
                        severity: "High",
                        issue: "File content indicates presence of Social Security Numbers.",
                        context: await getContextLine(filePath, "SSN:")
                    });
                }
            }

            // --- Scan for Debug Flags ---
            if (parameters.scanForDebugFlags) {
                if (fileContent.includes("debugMode: true") || fileContent.includes("<debugMode>true</debugMode>")) {
                    scanResults.push({
                        filePath: filePath,
                        severity: "Low",
                        issue: "Potential debug flag enabled in configuration.",
                        context: await getContextLine(filePath, "debugMode")
                    });
                }
            }

            // --- Scan for Custom Keywords ---
            if (parameters.includeKeywords && parameters.includeKeywords.length > 0) {
                for (const keyword of parameters.includeKeywords) {
                    if (fileContent.toLowerCase().includes(keyword.toLowerCase())) {
                        scanResults.push({
                            filePath: filePath,
                            severity: "Info",
                            issue: `Custom keyword '${keyword}' found.`,
                            context: await getContextLine(filePath, keyword)
                        });
                    }
                }
            }
        }

        const reportFileName = `SecurityReport_${Date.now()}.json`;
        const reportFilePath = path.join(reportOutputDirectory, reportFileName);

        const fullReport = {
            scanTime: new Date().toISOString(),
            scanTarget: scanTargetDirectory,
            scanParameters: parameters,
            totalFilesScanned: totalFilesScanned,
            totalIssuesFound: scanResults.length,
            securityAssessment: assessOverallSecurity(scanResults),
            scanResults: scanResults.sort((a, b) => getSeverityOrder(b.severity) - getSeverityOrder(a.severity))
        };

        await fs.writeFile(reportFilePath, JSON.stringify(fullReport, null, 4));

        return res.status(200).json({
            message: "Security scan completed.",
            reportFileName: reportFileName,
            reportFilePath: reportFilePath,
            summary: {
                totalIssues: scanResults.length,
                highSeverity: scanResults.filter(r => r.severity === "High").length,
                mediumSeverity: scanResults.filter(r => r.severity === "Medium").length,
                lowSeverity: scanResults.filter(r => r.severity === "Low").length
            }
        });

    } catch (error: any) {
        if (error.code === 'ENOENT') {
            return res.status(404).json({ error: `Scan target directory not found: ${scanTargetDirectory}` });
        }
        if (error.code === 'EACCES' || error.code === 'EPERM') {
            return res.status(403).json({ error: `Access denied to the scan target directory: ${scanTargetDirectory}` });
        }
        return res.status(500).json({ error: `An error occurred during the security scan: ${error.message}` });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});