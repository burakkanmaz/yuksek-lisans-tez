import os
import re
from pathlib import Path

def clean_standalone_language_lines(content):
    """Remove standalone language lines that appear before code blocks"""
    lines = content.split('\n')
    cleaned_lines = []
    i = 0
    lines_removed = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a standalone language line
        standalone_languages = ['C#', 'Python', 'TypeScript', 'JavaScript', 'Java', 'Go', 'Rust', 'PHP', 'Ruby', 'C++', 'C']
        
        if line.strip() in standalone_languages:
            # Check if the next line is a code block start
            if i + 1 < len(lines) and lines[i + 1].strip().startswith('```'):
                # This is a standalone language line before a code block, skip it
                lines_removed += 1
                i += 1
                continue
            else:
                # This is not before a code block, keep it
                cleaned_lines.append(line)
                i += 1
        else:
            cleaned_lines.append(line)
            i += 1
    
    return '\n'.join(cleaned_lines), lines_removed

def process_gemini_file(file_path):
    """Process a single gemini markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            original_content = file.read()
        
        # Clean standalone language lines
        cleaned_content, lines_removed = clean_standalone_language_lines(original_content)
        
        # Check if content changed
        content_changed = original_content != cleaned_content
        
        if content_changed:
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_content)
            
            return {
                'modified': True,
                'lines_removed': lines_removed
            }
        else:
            return {
                'modified': False,
                'lines_removed': 0
            }
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return {
            'modified': False,
            'lines_removed': 0,
            'error': str(e)
        }

def clean_gemini_standalone_languages():
    """Main function to clean standalone language lines in gemini folder"""
    gemini_folder = Path("sonuçlar/gemini")
    
    if not gemini_folder.exists():
        print(f"❌ Gemini folder not found: {gemini_folder}")
        return
    
    # Find all markdown files in gemini folder
    md_files = list(gemini_folder.glob("*.md"))
    
    if not md_files:
        print("❌ No markdown files found in gemini folder")
        return
    
    print(f"🔍 Cleaning standalone language lines in {len(md_files)} markdown files...")
    print("=" * 80)
    
    # Process all files
    total_files_modified = 0
    total_lines_removed = 0
    modified_files = []
    
    for md_file in md_files:
        filename = md_file.name
        result = process_gemini_file(md_file)
        
        if result['modified']:
            modified_files.append({
                'filename': filename,
                'lines_removed': result['lines_removed']
            })
            
            total_files_modified += 1
            total_lines_removed += result['lines_removed']
    
    # Display results
    if total_files_modified == 0:
        print("✅ No standalone language lines found to clean!")
        return
    
    print(f"📊 Processing completed! Modified {total_files_modified} files:\n")
    
    print("📁 GEMINI:")
    for file_info in modified_files:
        filename = file_info['filename']
        lines_removed = file_info['lines_removed']
        
        print(f"  • {filename:<15} | {lines_removed} tek başına dil satırı temizlendi")
    
    print()
    print("=" * 80)
    print(f"📈 ÖZET:")
    print(f"  • Toplam işlenen dosya: {len(md_files)}")
    print(f"  • Değiştirilen dosya: {total_files_modified}")
    print(f"  • Toplam temizlenen satır: {total_lines_removed}")
    print(f"  • Başarı oranı: {(total_files_modified / len(md_files) * 100):.1f}%")

if __name__ == "__main__":
    clean_gemini_standalone_languages() 