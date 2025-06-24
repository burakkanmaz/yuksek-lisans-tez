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

def find_problematic_files():
    """Find files that don't have exactly 10 scenarios and 30 code blocks"""
    results_folder = Path("sonuçlar")
    
    if not results_folder.exists():
        print(f"❌ Results folder not found: {results_folder}")
        return
    
    # Find all markdown files
    md_files = list(results_folder.rglob("*.md"))
    
    if not md_files:
        print("❌ No markdown files found")
        return
    
    print(f"Analyzing {len(md_files)} markdown files...")
    print("=" * 80)
    
    # Analyze all files and find problematic ones
    problematic_files = []
    
    for md_file in md_files:
        analysis = analyze_markdown_file(md_file)
        
        # Check if file has exactly 10 scenarios and 30 code blocks
        if analysis['scenario_count'] != 10 or analysis['code_block_count'] != 30:
            problematic_files.append(analysis)
    
    # Sort by AI folder and filename
    problematic_files.sort(key=lambda x: (x['ai_folder'], x['filename']))
    
    # Print results
    if not problematic_files:
        print("✅ All files have exactly 10 scenarios and 30 code blocks!")
        return
    
    print(f"⚠️  Found {len(problematic_files)} problematic files:")
    print()
    
    # Group by AI folder for better readability
    current_ai = None
    total_missing_scenarios = 0
    total_missing_code_blocks = 0
    
    for file_info in problematic_files:
        ai_folder = file_info['ai_folder']
        filename = file_info['filename']
        scenarios = file_info['scenario_count']
        code_blocks = file_info['code_block_count']
        
        # Calculate missing/extra
        scenario_diff = scenarios - 10
        code_block_diff = code_blocks - 30
        
        total_missing_scenarios += abs(scenario_diff)
        total_missing_code_blocks += abs(code_block_diff)
        
        # Print AI folder header if changed
        if ai_folder != current_ai:
            if current_ai is not None:
                print()
            print(f"📁 {ai_folder.upper()}:")
            current_ai = ai_folder
        
        # Format scenario info
        if scenario_diff == 0:
            scenario_info = f"{scenarios} ✅"
        elif scenario_diff > 0:
            scenario_info = f"{scenarios} (+{scenario_diff}) 📈"
        else:
            scenario_info = f"{scenarios} ({scenario_diff}) 📉"
        
        # Format code block info
        if code_block_diff == 0:
            code_block_info = f"{code_blocks} ✅"
        elif code_block_diff > 0:
            code_block_info = f"{code_blocks} (+{code_block_diff}) 📈"
        else:
            code_block_info = f"{code_blocks} ({code_block_diff}) 📉"
        
        print(f"  • {filename:<15} | Scenarios: {scenario_info:<12} | Code blocks: {code_block_info}")
    
    print()
    print("=" * 80)
    print(f"📊 SUMMARY:")
    print(f"  • Total problematic files: {len(problematic_files)}")
    print(f"  • Total files analyzed: {len(md_files)}")
    print(f"  • Success rate: {((len(md_files) - len(problematic_files)) / len(md_files) * 100):.1f}%")
    
    # Count by AI
    ai_counts = {}
    for file_info in problematic_files:
        ai = file_info['ai_folder']
        if ai not in ai_counts:
            ai_counts[ai] = 0
        ai_counts[ai] += 1
    
    print(f"\n📈 Problematic files by AI:")
    for ai, count in sorted(ai_counts.items()):
        total_files = len([f for f in md_files if f.parent.name == ai])
        percentage = (count / total_files * 100) if total_files > 0 else 0
        print(f"  • {ai:<10}: {count:>2}/{total_files} files ({percentage:>5.1f}%)")

if __name__ == "__main__":
    find_problematic_files() 