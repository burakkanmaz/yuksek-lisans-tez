import os
import re

def reformat_single_file_for_vertical_layout(filepath):
    """
    Finds lines with horizontal 'Dil/AI/Satır' info and splits them vertically.
    It handles both formatted (bold, backticks) and unformatted variations.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Could not read {os.path.basename(filepath)}: {e}")
        return

    original_content = content
    
    # Pattern to find the unformatted version, e.g., "💻 Dil: C# 🤖 AI: ChatGPT Satır Sayısı: 10"
    # and convert it to the standardized, vertical format.
    pattern_unformatted = re.compile(
        r"^(💻 Dil: (C#|Python|TypeScript))\s*(🤖 AI: ChatGPT)\s*(Satır Sayısı: \d+)\s*$",
        re.MULTILINE
    )
    
    def replacer_unformatted(match):
        lang = match.group(2)
        satir_count_text = match.group(4)
        return (
            f"**💻 Dil:** `{lang}`\n"
            f"**🤖 AI:** ChatGPT\n"
            f"**{satir_count_text}**"
        )
    content = pattern_unformatted.sub(replacer_unformatted, content)

    # Pattern to find an already formatted but horizontal version
    # e.g., "**💻 Dil:** `C#` **🤖 AI:** ChatGPT **Satır Sayısı:** 10"
    pattern_formatted_horizontal = re.compile(
        r"^(\*\*💻 Dil:\*\* `(C#|Python|TypeScript)`)\s*(\*\*🤖 AI:\*\* ChatGPT)\s*(\*\*Satır Sayısı:\*\* \d+)\s*$",
        re.MULTILINE
    )
    
    # The replacement just adds newlines.
    replacement_vertical = r"\1\n\3\n\4"
    content = pattern_formatted_horizontal.sub(replacement_vertical, content)

    if content != original_content:
        print(f"  [*] Applying vertical reformat to {os.path.basename(filepath)}")
        try:
            with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
                f.write(content)
        except Exception as e:
            print(f"  [!] Error writing to {os.path.basename(filepath)}: {e}")
    # else:
    #     print(f"  [=] No horizontal layout found in {os.path.basename(filepath)}")

def main():
    directory = "sonuçlar/chatgpt"
    print(f"Starting vertical layout formatting for files in '{directory}'...")

    files_to_process = [f for f in os.listdir(directory) if f.endswith(".md")]
    
    for filename in files_to_process:
        filepath = os.path.join(directory, filename)
        if os.path.getsize(filepath) > 100:
            reformat_single_file_for_vertical_layout(filepath)
    
    print("\nVertical formatting process completed.")

if __name__ == "__main__":
    main() 