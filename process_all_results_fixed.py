import os
import re
from pathlib import Path

def count_code_lines(code_block):
    """Count non-empty lines in a code block"""
    lines = code_block.strip().split('\n')
    return len([line for line in lines if line.strip()])

def remove_extra_blank_lines(lines):
    """Remove consecutive blank lines, keeping maximum 1 blank line"""
    result = []
    blank_count = 0
    
    for line in lines:
        if line.strip() == '':
            blank_count += 1
            if blank_count == 1:
                result.append(line)
        else:
            blank_count = 0
            result.append(line)
    
    return result

def extract_scenario_number(text):
    """Extract scenario number from text"""
    # Look for "Senaryo X:" pattern
    match = re.search(r'Senaryo (\d+):', text)
    if match:
        return int(match.group(1))
    return None

def validate_file_structure(lines, file_path):
    """Validate that file has 10 scenarios with 3 languages each"""
    scenarios = []
    current_scenario = None
    languages_in_scenario = []
    
    for line in lines:
        # Check for scenario
        if '🧪 Senaryo' in line:
            # Save previous scenario if exists
            if current_scenario is not None:
                scenarios.append({
                    'number': current_scenario,
                    'languages': languages_in_scenario.copy()
                })
            
            # Start new scenario
            current_scenario = extract_scenario_number(line)
            languages_in_scenario = []
        
        # Check for language - count unique language occurrences per scenario
        elif '💻 Dil:' in line:
            if 'C#' in line and 'C#' not in languages_in_scenario:
                languages_in_scenario.append('C#')
            elif 'Python' in line and 'Python' not in languages_in_scenario:
                languages_in_scenario.append('Python')
            elif 'TypeScript' in line and 'TypeScript' not in languages_in_scenario:
                languages_in_scenario.append('TypeScript')
    
    # Add last scenario
    if current_scenario is not None:
        scenarios.append({
            'number': current_scenario,
            'languages': languages_in_scenario.copy()
        })
    
    # Validate structure
    issues = []
    
    # Check scenario count
    if len(scenarios) != 10:
        issues.append(f"Expected 10 scenarios, found {len(scenarios)}")
    
    # Check scenario numbering and languages
    for i, scenario in enumerate(scenarios):
        expected_number = i + 1
        if scenario['number'] != expected_number:
            issues.append(f"Scenario {i+1} has wrong number: {scenario['number']}")
        
        if len(scenario['languages']) != 3:
            issues.append(f"Scenario {scenario['number']} has {len(scenario['languages'])} languages instead of 3: {scenario['languages']}")
        
        expected_languages = ['C#', 'Python', 'TypeScript']
        missing_languages = [lang for lang in expected_languages if lang not in scenario['languages']]
        if missing_languages:
            issues.append(f"Scenario {scenario['number']} missing languages: {missing_languages}")
    
    return issues

def process_markdown_file(file_path):
    """Process a single markdown file - ONLY update line counts and remove extra blank lines"""
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split content into lines
    lines = content.split('\n')
    
    # Remove extra blank lines
    lines = remove_extra_blank_lines(lines)
    
    # Validate file structure (just report, don't change)
    issues = validate_file_structure(lines, file_path)
    if issues:
        print(f"  ⚠️  Structure issues found:")
        for issue in issues:
            print(f"    - {issue}")
    
    # Process lines ONLY for updating line counts
    processed_lines = []
    i = 0
    changes_made = False
    
    while i < len(lines):
        line = lines[i]
        processed_lines.append(line)
        
        # Look for "Satır Sayısı:" line followed by code block
        if 'Satır Sayısı:' in line:
            i += 1
            
            # Check if next line is a code block start
            if i < len(lines) and lines[i].startswith('```'):
                code_start_line = lines[i]
                processed_lines.append(code_start_line)
                i += 1
                
                # Collect code block content
                code_lines = []
                while i < len(lines) and not lines[i].startswith('```'):
                    code_lines.append(lines[i])
                    processed_lines.append(lines[i])
                    i += 1
                
                # Add closing ```
                if i < len(lines):
                    processed_lines.append(lines[i])
                    i += 1
                
                # Count lines in code block and update line count
                code_content = '\n'.join(code_lines)
                actual_line_count = count_code_lines(code_content)
                new_line_count_text = f"Satır Sayısı: {actual_line_count}"
                
                # Update the line count if different
                if processed_lines[-len(code_lines)-2] != new_line_count_text:  # -2 for ``` lines
                    # Find and update the "Satır Sayısı:" line
                    for j in range(len(processed_lines)-1, -1, -1):
                        if 'Satır Sayısı:' in processed_lines[j]:
                            processed_lines[j] = new_line_count_text
                            changes_made = True
                            print(f"  Updated line count: {actual_line_count}")
                            break
                
                continue
        
        i += 1
    
    # Check if content changed (either from blank line removal or line count updates)
    new_content = '\n'.join(processed_lines)
    if new_content != content:
        changes_made = True
    
    # Write back to file if changes were made
    if changes_made:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"  ✅ File updated")
    else:
        print(f"  ✅ No changes needed")

def check_scenario_ordering(lines):
    """Check if scenarios are ordered from 1 to 10"""
    scenario_numbers = []
    
    for line in lines:
        if '🧪 Senaryo' in line:
            number = extract_scenario_number(line)
            if number:
                scenario_numbers.append(number)
    
    expected_order = list(range(1, 11))
    if scenario_numbers != expected_order:
        return f"Scenarios not in order. Found: {scenario_numbers}, Expected: {expected_order}"
    
    return None

def main():
    """Main function to process all markdown files in sonuçlar folder"""
    results_folder = Path("sonuçlar")
    
    if not results_folder.exists():
        print(f"❌ Results folder not found: {results_folder}")
        return
    
    # Find all markdown files in all subdirectories
    md_files = list(results_folder.rglob("*.md"))
    
    if not md_files:
        print("❌ No markdown files found in results folder")
        return
    
    print(f"Found {len(md_files)} markdown files")
    print("=" * 60)
    
    total_issues = 0
    
    for md_file in md_files:
        try:
            # Read file to check scenario ordering
            with open(md_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            ordering_issue = check_scenario_ordering(lines)
            if ordering_issue:
                print(f"📁 {md_file}")
                print(f"  ⚠️  {ordering_issue}")
                total_issues += 1
                print()
                continue
            
            process_markdown_file(md_file)
            
        except Exception as e:
            print(f"❌ Error processing {md_file}: {e}")
            total_issues += 1
        print()
    
    print("=" * 60)
    if total_issues > 0:
        print(f"⚠️  Total files with issues: {total_issues}")
    else:
        print("✅ All files processed successfully!")

if __name__ == "__main__":
    main() 