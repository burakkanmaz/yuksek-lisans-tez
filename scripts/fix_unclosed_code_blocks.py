#!/usr/bin/env python3
"""
Script to find and fix unclosed code blocks in markdown files.
Searches for ``` code blocks that are not properly closed.
"""

import os
import re
import glob
from pathlib import Path

def find_unclosed_blocks(content):
    """Find unclosed code blocks in markdown content."""
    lines = content.split('\n')
    unclosed_blocks = []
    in_code_block = False
    block_start_line = -1
    
    for i, line in enumerate(lines):
        if line.strip().startswith('```'):
            if not in_code_block:
                # Starting a new code block
                in_code_block = True
                block_start_line = i
            else:
                # Closing a code block
                in_code_block = False
                block_start_line = -1
        elif in_code_block and line.strip().startswith('**💻 Dil:**'):
            # Found a language marker while in code block - this indicates unclosed block
            unclosed_blocks.append({
                'start_line': block_start_line,
                'line_content': lines[block_start_line].strip(),
                'ends_at': i
            })
            in_code_block = False
            block_start_line = -1
    
    # If we're still in a code block at the end, it's unclosed
    if in_code_block:
        unclosed_blocks.append({
            'start_line': block_start_line,
            'line_content': lines[block_start_line].strip(),
            'ends_at': len(lines)
        })
    
    return unclosed_blocks

def fix_unclosed_blocks(content):
    """Fix unclosed code blocks by adding missing closing tags."""
    lines = content.split('\n')
    in_code_block = False
    fixed = False
    new_lines = []
    
    for i, line in enumerate(lines):
        if line.strip().startswith('```'):
            if not in_code_block:
                in_code_block = True
            else:
                in_code_block = False
            new_lines.append(line)
        elif in_code_block and line.strip().startswith('**💻 Dil:**'):
            # Found language marker while in code block - close the block first
            new_lines.append('```')
            new_lines.append('')  # Add empty line for better formatting
            new_lines.append(line)
            in_code_block = False
            fixed = True
        else:
            new_lines.append(line)
    
    # If we end in a code block, add closing ```
    if in_code_block:
        new_lines.append('```')
        fixed = True
    
    return '\n'.join(new_lines), fixed

def process_file(file_path):
    """Process a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        unclosed = find_unclosed_blocks(content)
        
        if unclosed:
            print(f"\n📁 {file_path}")
            for block in unclosed:
                print(f"  🔓 Line {block['start_line'] + 1}: {block['line_content']}")
            
            # Fix the content
            fixed_content, was_fixed = fix_unclosed_blocks(content)
            
            if was_fixed:
                # Write back the fixed content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                print(f"  ✅ Fixed unclosed code blocks")
                return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {str(e)}")
        return False

def main():
    """Main function to process all markdown files."""
    print("🔍 Searching for unclosed code blocks in markdown files...")
    
    # Find all markdown files
    md_files = []
    for pattern in ['**/*.md', '**/**/*.md']:
        md_files.extend(glob.glob(pattern, recursive=True))
    
    if not md_files:
        print("❌ No markdown files found")
        return
    
    total_files = len(md_files)
    fixed_files = 0
    
    print(f"📊 Found {total_files} markdown files")
    
    for file_path in md_files:
        if process_file(file_path):
            fixed_files += 1
    
    print(f"\n📈 Summary:")
    print(f"  📄 Total files: {total_files}")
    print(f"  🔧 Fixed files: {fixed_files}")
    print(f"  ✅ Clean files: {total_files - fixed_files}")

if __name__ == "__main__":
    main() 