import os
import re
from pathlib import Path

def fix_code_blocks_in_content(content):
    """Fix code blocks that are not properly wrapped in ``` markers and standardize language names"""
    lines = content.split('\n')
    fixed_lines = []
    i = 0
    code_blocks_fixed = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this line contains a programming language name (standalone line)
        language_pattern = r'^(C#|Python|TypeScript|JavaScript|Java|Go|Rust|PHP|Ruby|C\+\+|C)$'
        
        if re.match(language_pattern, line.strip()):
            # This is a language declaration line
            language = line.strip()
            fixed_lines.append(line)  # Keep the language line as is
            i += 1
            
            # Check if next line starts a code block properly
            if i < len(lines):
                next_line = lines[i]
                if not next_line.strip().startswith('```'):
                    # Code block is not properly started, add ```
                    # Use standard language names for syntax highlighting
                    lang_map = {
                        'C#': 'csharp',
                        'Python': 'python', 
                        'TypeScript': 'typescript',
                        'JavaScript': 'javascript',
                        'Java': 'java',
                        'Go': 'go',
                        'Rust': 'rust',
                        'PHP': 'php',
                        'Ruby': 'ruby',
                        'C++': 'cpp',
                        'C': 'c'
                    }
                    lang_code = lang_map.get(language, language.lower())
                    fixed_lines.append(f'```{lang_code}')
                    
                    # Now collect all code lines until next scenario or end
                    code_lines = []
                    while i < len(lines):
                        current_line = lines[i]
                        
                        # Check if we've reached the next scenario or end
                        if (current_line.strip().startswith('🧪 Senaryo') or 
                            current_line.strip().startswith('### 🧪 Senaryo') or
                            current_line.strip().startswith('💻 Dil:') or
                            current_line.strip().startswith('**💻 Dil:**') or
                            i == len(lines) - 1):
                            
                            # End the code block
                            if code_lines:
                                # Remove trailing empty lines from code
                                while code_lines and code_lines[-1].strip() == '':
                                    code_lines.pop()
                                
                                fixed_lines.extend(code_lines)
                                fixed_lines.append('```')
                                code_blocks_fixed += 1
                            
                            # Don't increment i here, let the main loop handle this line
                            break
                        else:
                            code_lines.append(current_line)
                            i += 1
                else:
                    # Code block is already properly started
                    fixed_lines.append(next_line)
                    i += 1
        else:
            # Also fix existing code blocks with wrong language names
            if line.strip().startswith('```'):
                if line.strip() == '```c#':
                    fixed_lines.append('```csharp')
                    code_blocks_fixed += 1
                elif line.strip() == '```typescript (node.js)':
                    fixed_lines.append('```typescript')
                    code_blocks_fixed += 1
                else:
                    fixed_lines.append(line)
            else:
                fixed_lines.append(line)
            i += 1
    
    return '\n'.join(fixed_lines), code_blocks_fixed

def process_gemini_file(file_path):
    """Process a single gemini markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            original_content = file.read()
        
        # Fix code blocks
        fixed_content, code_blocks_fixed = fix_code_blocks_in_content(original_content)
        
        # Check if content changed
        content_changed = original_content != fixed_content
        
        if content_changed:
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(fixed_content)
            
            return {
                'modified': True,
                'code_blocks_fixed': code_blocks_fixed
            }
        else:
            return {
                'modified': False,
                'code_blocks_fixed': 0
            }
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return {
            'modified': False,
            'code_blocks_fixed': 0,
            'error': str(e)
        }

def fix_gemini_code_blocks():
    """Main function to fix code blocks in gemini folder"""
    gemini_folder = Path("sonuçlar/gemini")
    
    if not gemini_folder.exists():
        print(f"❌ Gemini folder not found: {gemini_folder}")
        return
    
    # Find all markdown files in gemini folder
    md_files = list(gemini_folder.glob("*.md"))
    
    if not md_files:
        print("❌ No markdown files found in gemini folder")
        return
    
    print(f"🔍 Processing {len(md_files)} markdown files in gemini folder...")
    print("=" * 80)
    print()
    
    # Process all files
    total_files_modified = 0
    total_code_blocks_fixed = 0
    modified_files = []
    
    for md_file in md_files:
        filename = md_file.name
        result = process_gemini_file(md_file)
        
        if result['modified']:
            modified_files.append({
                'filename': filename,
                'code_blocks_fixed': result['code_blocks_fixed']
            })
            
            total_files_modified += 1
            total_code_blocks_fixed += result['code_blocks_fixed']
    
    # Display results
    if total_files_modified == 0:
        print("✅ No files needed code block fixes!")
        return
    
    print(f"📊 Processing completed! Modified {total_files_modified} files:\n")
    
    print("📁 GEMINI:")
    for file_info in modified_files:
        filename = file_info['filename']
        code_blocks_fixed = file_info['code_blocks_fixed']
        
        print(f"  • {filename:<15} | {code_blocks_fixed} kod bloğu düzeltildi")
    
    print()
    print("=" * 80)
    print(f"📈 ÖZET:")
    print(f"  • Toplam işlenen dosya: {len(md_files)}")
    print(f"  • Değiştirilen dosya: {total_files_modified}")
    print(f"  • Toplam düzeltilen kod bloğu: {total_code_blocks_fixed}")
    print(f"  • Başarı oranı: {(total_files_modified / len(md_files) * 100):.1f}%")

if __name__ == "__main__":
    fix_gemini_code_blocks() 