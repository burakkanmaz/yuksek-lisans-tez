import os
import re
from pathlib import Path

def count_lines_in_code_block(code_content):
    """Count lines in code block content"""
    if not code_content.strip():
        return 0
    return len(code_content.split('\n'))

def clean_excessive_blank_lines(content):
    """Remove excessive blank lines, keep maximum 1 blank line between content"""
    lines = content.split('\n')
    cleaned_lines = []
    blank_count = 0
    
    for line in lines:
        if line.strip() == '':
            blank_count += 1
            if blank_count <= 1:  # Keep maximum 1 blank line
                cleaned_lines.append(line)
        else:
            blank_count = 0
            cleaned_lines.append(line)
    
    # Remove trailing blank lines
    while cleaned_lines and cleaned_lines[-1].strip() == '':
        cleaned_lines.pop()
    
    return '\n'.join(cleaned_lines)

def remove_duplicate_line_counts(content):
    """Remove duplicate 'Satır Sayısı' lines that appear consecutively"""
    lines = content.split('\n')
    cleaned_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Check if this is a "Satır Sayısı" line
        if 'Satır Sayısı:' in line:
            # Add this line
            cleaned_lines.append(lines[i])
            
            # Skip any duplicate "Satır Sayısı" lines that follow
            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                if 'Satır Sayısı:' in next_line:
                    # Skip this duplicate
                    j += 1
                elif next_line == '':
                    # Skip blank lines between duplicates
                    j += 1
                else:
                    # Non-duplicate line found, stop skipping
                    break
            i = j
        else:
            cleaned_lines.append(lines[i])
            i += 1
    
    return '\n'.join(cleaned_lines)

def add_line_count_to_code_blocks(content):
    """Add line count information to code blocks that don't have it"""
    lines = content.split('\n')
    modified_lines = []
    i = 0
    code_blocks_fixed = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a code block start
        if line.strip().startswith('```') and len(line.strip()) > 3:
            # This is a code block start
            code_block_start = i
            language = line.strip()[3:].strip()
            
            # Find the end of code block
            code_block_end = None
            code_content_lines = []
            
            for j in range(i + 1, len(lines)):
                if lines[j].strip() == '```':
                    code_block_end = j
                    break
                code_content_lines.append(lines[j])
            
            if code_block_end is not None:
                # Check if any of the previous lines (up to 3 lines back) contains "Satır Sayısı" info
                has_line_count = False
                for check_line_idx in range(max(0, code_block_start - 3), code_block_start):
                    check_line = lines[check_line_idx].strip()
                    if 'Satır Sayısı' in check_line or 'satır sayısı' in check_line.lower():
                        has_line_count = True
                        break
                
                # If no line count info, add it
                if not has_line_count:
                    line_count = len(code_content_lines)
                    line_count_info = f"**Satır Sayısı:** {line_count}"
                    
                    # Add the line count info before the code block
                    if code_block_start > 0 and lines[code_block_start - 1].strip() != '':
                        modified_lines.append('')  # Add blank line before line count
                    modified_lines.append(line_count_info)
                    modified_lines.append('')  # Add blank line after line count
                    code_blocks_fixed += 1
                
                # Add the code block
                modified_lines.extend(lines[code_block_start:code_block_end + 1])
                i = code_block_end + 1
            else:
                # Malformed code block, just add the line
                modified_lines.append(line)
                i += 1
        else:
            modified_lines.append(line)
            i += 1
    
    return '\n'.join(modified_lines), code_blocks_fixed

def process_markdown_file(file_path):
    """Process a single markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            original_content = file.read()
        
        # Clean excessive blank lines
        cleaned_content = clean_excessive_blank_lines(original_content)
        lines_removed = original_content.count('\n') - cleaned_content.count('\n')
        
        # Remove duplicate line counts
        cleaned_content = remove_duplicate_line_counts(cleaned_content)
        
        # Add line count to code blocks
        final_content, code_blocks_fixed = add_line_count_to_code_blocks(cleaned_content)
        
        # Check if content changed
        content_changed = original_content != final_content
        
        if content_changed:
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(final_content)
            
            return {
                'modified': True,
                'lines_removed': max(0, lines_removed),  # Ensure non-negative
                'code_blocks_fixed': code_blocks_fixed
            }
        else:
            return {
                'modified': False,
                'lines_removed': 0,
                'code_blocks_fixed': 0
            }
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return {
            'modified': False,
            'lines_removed': 0,
            'code_blocks_fixed': 0,
            'error': str(e)
        }

def clean_and_fix_markdown_files():
    """Main function to clean and fix all markdown files"""
    results_folder = Path("sonuçlar")
    
    if not results_folder.exists():
        print(f"❌ Results folder not found: {results_folder}")
        return
    
    # Find all markdown files
    md_files = list(results_folder.rglob("*.md"))
    
    if not md_files:
        print("❌ No markdown files found")
        return
    
    print(f"🔍 Processing {len(md_files)} markdown files...")
    print("=" * 80)
    print()  # Add extra line for better visibility
    
    # Process all files
    total_files_modified = 0
    total_lines_removed = 0
    total_code_blocks_fixed = 0
    
    # Group results by AI folder
    ai_results = {}
    
    for md_file in md_files:
        ai_folder = md_file.parent.name
        filename = md_file.name
        
        if ai_folder not in ai_results:
            ai_results[ai_folder] = []
        
        result = process_markdown_file(md_file)
        
        if result['modified']:
            ai_results[ai_folder].append({
                'filename': filename,
                'lines_removed': result['lines_removed'],
                'code_blocks_fixed': result['code_blocks_fixed']
            })
            
            total_files_modified += 1
            total_lines_removed += result['lines_removed']
            total_code_blocks_fixed += result['code_blocks_fixed']
    
    # Display results
    if total_files_modified == 0:
        print("✅ No files needed modification!")
        return
    
    print(f"📊 Processing completed! Modified {total_files_modified} files:\n")
    
    # Show results by AI folder
    for ai_folder in sorted(ai_results.keys()):
        if ai_results[ai_folder]:  # Only show if there are modified files
            print(f"📁 {ai_folder.upper()}:")
            
            for file_info in ai_results[ai_folder]:
                filename = file_info['filename']
                lines_removed = file_info['lines_removed']
                code_blocks_fixed = file_info['code_blocks_fixed']
                
                # Format output
                changes = []
                if lines_removed > 0:
                    changes.append(f"{lines_removed} satır silindi")
                if code_blocks_fixed > 0:
                    changes.append(f"{code_blocks_fixed} kod bloğuna satır sayısı eklendi")
                
                if changes:
                    changes_str = ", ".join(changes)
                    print(f"  • {filename:<15} | {changes_str}")
            
            print()
    
    print("=" * 80)
    print(f"📈 ÖZET:")
    print(f"  • Toplam işlenen dosya: {len(md_files)}")
    print(f"  • Değiştirilen dosya: {total_files_modified}")
    print(f"  • Toplam silinen satır: {total_lines_removed}")
    print(f"  • Satır sayısı eklenen kod bloğu: {total_code_blocks_fixed}")
    print(f"  • Başarı oranı: {(total_files_modified / len(md_files) * 100):.1f}%")

if __name__ == "__main__":
    clean_and_fix_markdown_files() 