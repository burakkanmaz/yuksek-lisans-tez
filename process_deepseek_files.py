import os
import re
from pathlib import Path

def count_code_lines(code_block):
    """Count non-empty lines in a code block"""
    lines = code_block.strip().split('\n')
    return len([line for line in lines if line.strip() and not line.strip().startswith('🤖 AI:') and line.strip() not in ['csharp', 'python', 'typescript', 'javascript']])

def process_markdown_file(file_path):
    """Process a single markdown file"""
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split content into lines
    lines = content.split('\n')
    processed_lines = []
    i = 0
    changes_made = False
    
    while i < len(lines):
        line = lines[i]
        
        # Look for language line pattern: "💻 Dil: [Language]"
        if '💻 Dil:' in line:
            # Extract language
            language_match = re.search(r'💻 Dil: (.+?)(?:🤖|$)', line)
            if language_match:
                language = language_match.group(1).strip()
                
                # Check if AI info is already in the line
                if '🤖 AI:' in line:
                    # Keep as is
                    processed_lines.append(line)
                    i += 1
                else:
                    # Need to find AI info and add it to this line
                    ai_info = None
                    
                    # Look ahead in the code block for AI info
                    temp_i = i + 1
                    # Skip "Satır Sayısı:" line if present
                    if temp_i < len(lines) and 'Satır Sayısı:' in lines[temp_i]:
                        temp_i += 1
                    
                    # Look for code block
                    if temp_i < len(lines) and lines[temp_i].startswith('```'):
                        temp_i += 1
                        # Look for AI info in code block
                        while temp_i < len(lines) and not lines[temp_i].startswith('```'):
                            if '🤖 AI:' in lines[temp_i]:
                                ai_info = lines[temp_i].strip()
                                break
                            temp_i += 1
                    
                    # Add AI info to language line
                    if ai_info:
                        processed_lines.append(f"{line}{ai_info}")
                        changes_made = True
                        print(f"  Moved AI info to language line")
                    else:
                        processed_lines.append(line)
                    i += 1
                
                # Handle "Satır Sayısı:" line
                existing_line_count_index = None
                if i < len(lines) and 'Satır Sayısı:' in lines[i]:
                    existing_line_count_index = len(processed_lines)
                    processed_lines.append(lines[i])
                    i += 1
                
                # Process code block
                if i < len(lines) and lines[i].startswith('```'):
                    code_start_line = lines[i]
                    processed_lines.append(code_start_line)
                    i += 1
                    
                    # Collect code block content, filtering out AI info and language duplicates
                    code_lines = []
                    while i < len(lines) and not lines[i].startswith('```'):
                        current_line = lines[i]
                        # Skip AI info lines and language name duplicates
                        if ('🤖 AI:' not in current_line and 
                            current_line.strip() not in ['csharp', 'python', 'typescript', 'javascript'] and
                            current_line.strip() != ''):
                            code_lines.append(current_line)
                            processed_lines.append(current_line)
                        elif current_line.strip() != '':
                            changes_made = True
                            print(f"  Removed line from code block: {current_line.strip()}")
                        else:
                            # Keep empty lines
                            code_lines.append(current_line)
                            processed_lines.append(current_line)
                        i += 1
                    
                    # Add closing ```
                    if i < len(lines):
                        processed_lines.append(lines[i])
                        i += 1
                    
                    # Count lines in code block
                    code_content = '\n'.join(code_lines)
                    line_count = count_code_lines(code_content)
                    new_line_count_text = f"Satır Sayısı: {line_count}"
                    
                    # Update or add line count
                    if existing_line_count_index is not None:
                        # Update existing line count
                        if processed_lines[existing_line_count_index] != new_line_count_text:
                            processed_lines[existing_line_count_index] = new_line_count_text
                            changes_made = True
                            print(f"  Updated line count: {line_count}")
                    else:
                        # Insert line count after language line, before code block
                        lang_line_index = len(processed_lines) - len(code_lines) - 2  # -2 for ``` lines
                        processed_lines.insert(lang_line_index, new_line_count_text)
                        changes_made = True
                        print(f"  Added line count: {line_count}")
                    
                    continue
        
        processed_lines.append(line)
        i += 1
    
    # Write back to file if changes were made
    if changes_made:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(processed_lines))
        print(f"  ✅ File updated")
    else:
        print(f"  ✅ No changes needed")

def main():
    """Main function to process all markdown files in deepseek folder"""
    deepseek_folder = Path("sonuçlar/deepseek")
    
    if not deepseek_folder.exists():
        print(f"❌ DeepSeek folder not found: {deepseek_folder}")
        return
    
    # Find all markdown files
    md_files = list(deepseek_folder.glob("*.md"))
    
    if not md_files:
        print("❌ No markdown files found in deepseek folder")
        return
    
    print(f"Found {len(md_files)} markdown files")
    print("-" * 50)
    
    for md_file in md_files:
        try:
            process_markdown_file(md_file)
        except Exception as e:
            print(f"❌ Error processing {md_file}: {e}")
        print()
    
    print("✅ Processing completed!")

if __name__ == "__main__":
    main() 