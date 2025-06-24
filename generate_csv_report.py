import os
import re
import csv
from pathlib import Path

def extract_scenario_number(text):
    """Extract scenario number from text"""
    match = re.search(r'Senaryo (\d+):', text)
    if match:
        return int(match.group(1))
    return None

def analyze_markdown_file(file_path):
    """Analyze a markdown file and return statistics"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        lines = content.split('\n')
        
        # Count scenarios
        scenarios = set()
        code_blocks = 0
        
        for line in lines:
            # Count scenarios
            if '🧪 Senaryo' in line:
                scenario_num = extract_scenario_number(line)
                if scenario_num:
                    scenarios.add(scenario_num)
            
            # Count code blocks (lines starting with ```)
            if line.strip().startswith('```') and not line.strip() == '```':
                code_blocks += 1
        
        scenario_count = len(scenarios)
        
        return {
            'file_path': str(file_path),
            'filename': file_path.name,
            'ai_folder': file_path.parent.name,
            'scenario_count': scenario_count,
            'code_block_count': code_blocks
        }
        
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return {
            'file_path': str(file_path),
            'filename': file_path.name,
            'ai_folder': file_path.parent.name,
            'scenario_count': 0,
            'code_block_count': 0
        }

def generate_csv_report():
    """Generate CSV report for all markdown files"""
    results_folder = Path("sonuçlar")
    
    if not results_folder.exists():
        print(f"❌ Results folder not found: {results_folder}")
        return
    
    # Find all markdown files
    md_files = list(results_folder.rglob("*.md"))
    
    if not md_files:
        print("❌ No markdown files found")
        return
    
    print(f"Found {len(md_files)} markdown files")
    print("Analyzing files...")
    
    # Analyze all files
    data = []
    for md_file in md_files:
        analysis = analyze_markdown_file(md_file)
        data.append(analysis)
        print(f"  Processed: {analysis['ai_folder']}/{analysis['filename']} - Scenarios: {analysis['scenario_count']}, Code blocks: {analysis['code_block_count']}")
    
    # Sort data by AI folder and filename
    data.sort(key=lambda x: (x['ai_folder'], x['filename']))
    
    # Write CSV file
    csv_filename = "file_analysis_report.csv"
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['AI_Klasörü', 'Dosya_Adı', 'Senaryo_Sayısı', 'Kod_Bloğu_Sayısı', 'Tam_Yol']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header
        writer.writeheader()
        
        # Write data
        for item in data:
            writer.writerow({
                'AI_Klasörü': item['ai_folder'],
                'Dosya_Adı': item['filename'],
                'Senaryo_Sayısı': item['scenario_count'],
                'Kod_Bloğu_Sayısı': item['code_block_count'],
                'Tam_Yol': item['file_path']
            })
    
    print(f"\n✅ CSV report generated: {csv_filename}")
    
    # Print summary statistics
    print("\n📊 Summary Statistics:")
    print("=" * 50)
    
    ai_folders = {}
    total_scenarios = 0
    total_code_blocks = 0
    
    for item in data:
        ai_folder = item['ai_folder']
        if ai_folder not in ai_folders:
            ai_folders[ai_folder] = {
                'files': 0,
                'scenarios': 0,
                'code_blocks': 0
            }
        
        ai_folders[ai_folder]['files'] += 1
        ai_folders[ai_folder]['scenarios'] += item['scenario_count']
        ai_folders[ai_folder]['code_blocks'] += item['code_block_count']
        
        total_scenarios += item['scenario_count']
        total_code_blocks += item['code_block_count']
    
    for ai_folder, stats in sorted(ai_folders.items()):
        print(f"{ai_folder:>10}: {stats['files']:>3} files, {stats['scenarios']:>3} scenarios, {stats['code_blocks']:>4} code blocks")
    
    print("-" * 50)
    print(f"{'TOPLAM':>10}: {len(data):>3} files, {total_scenarios:>3} scenarios, {total_code_blocks:>4} code blocks")

if __name__ == "__main__":
    generate_csv_report() 