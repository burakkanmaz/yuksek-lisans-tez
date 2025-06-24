import os
import re
from pathlib import Path

def standardize_language_tags_in_content(content):
    """Standardize language tags in code blocks"""
    
    # Replace problematic language tags
    replacements = {
        '```csharp': '```csharp',
        '```csharp': '```csharp',
        '```typescript (node.js)': '```typescript',
        '```TypeScript (Node.js)': '```typescript',
        '```TypeScript': '```typescript',
        '```JavaScript': '```javascript',
        '```Python': '```python',
        '```Java': '```java'
    }
    
    tags_fixed = 0
    original_content = content
    
    for old_tag, new_tag in replacements.items():
        if old_tag in content:
            content = content.replace(old_tag, new_tag)
            tags_fixed += content.count(new_tag) - original_content.count(new_tag)
    
    return content, tags_fixed

def process_gemini_file(file_path):
    """Process a single gemini markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            original_content = file.read()
        
        # Standardize language tags
        fixed_content, tags_fixed = standardize_language_tags_in_content(original_content)
        
        # Check if content changed
        content_changed = original_content != fixed_content
        
        if content_changed:
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(fixed_content)
            
            return {
                'modified': True,
                'tags_fixed': tags_fixed
            }
        else:
            return {
                'modified': False,
                'tags_fixed': 0
            }
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return {
            'modified': False,
            'tags_fixed': 0,
            'error': str(e)
        }

def standardize_gemini_language_tags():
    """Main function to standardize language tags in gemini folder"""
    gemini_folder = Path("sonuçlar/gemini")
    
    if not gemini_folder.exists():
        print(f"❌ Gemini folder not found: {gemini_folder}")
        return
    
    # Find all markdown files in gemini folder
    md_files = list(gemini_folder.glob("*.md"))
    
    if not md_files:
        print("❌ No markdown files found in gemini folder")
        return
    
    print(f"🔍 Standardizing language tags in {len(md_files)} markdown files...")
    print("=" * 80)
    
    # Process all files
    total_files_modified = 0
    total_tags_fixed = 0
    modified_files = []
    
    for md_file in md_files:
        filename = md_file.name
        result = process_gemini_file(md_file)
        
        if result['modified']:
            modified_files.append({
                'filename': filename,
                'tags_fixed': result['tags_fixed']
            })
            
            total_files_modified += 1
            total_tags_fixed += result['tags_fixed']
    
    # Display results
    if total_files_modified == 0:
        print("✅ No files needed language tag standardization!")
        return
    
    print(f"📊 Processing completed! Modified {total_files_modified} files:\n")
    
    print("📁 GEMINI:")
    for file_info in modified_files:
        filename = file_info['filename']
        tags_fixed = file_info['tags_fixed']
        
        print(f"  • {filename:<15} | {tags_fixed} dil etiketi standardize edildi")
    
    print()
    print("=" * 80)
    print(f"📈 ÖZET:")
    print(f"  • Toplam işlenen dosya: {len(md_files)}")
    print(f"  • Değiştirilen dosya: {total_files_modified}")
    print(f"  • Toplam düzeltilen etiket: {total_tags_fixed}")
    print(f"  • Başarı oranı: {(total_files_modified / len(md_files) * 100):.1f}%")

if __name__ == "__main__":
    standardize_gemini_language_tags() 