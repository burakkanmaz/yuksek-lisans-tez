#!/usr/bin/env python3
import os
import re
from pathlib import Path

def merge_duplicate_scenarios(content):
    """
    Aynı senaryo numarasının farklı dillerde tekrar tekrar yazıldığı durumları birleştirir.
    """
    # Tüm senaryo blokları ve içeriklerini bul
    scenario_blocks = {}
    
    # Pattern: ### 🧪 Senaryo X: Açıklama ... ile başlayan blokları yakala
    pattern = r'(### 🧪 Senaryo (\d+): [^\n]+(?:\n(?!### 🧪 Senaryo|$).*)*)'
    matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)
    
    for full_match, scenario_num in matches:
        scenario_num = int(scenario_num)
        
        # Senaryo açıklamasını çıkar
        description_match = re.search(r'### 🧪 Senaryo \d+: (.+)', full_match)
        description = description_match.group(1) if description_match else ""
        
        # Bu bloktan dil kodlarını çıkar
        lang_pattern = r'(\*\*💻 Dil:\*\* `[^`]+`.*?(?=\*\*💻 Dil:\*\*|$))'
        lang_blocks = re.findall(lang_pattern, full_match, re.DOTALL)
        
        if scenario_num not in scenario_blocks:
            scenario_blocks[scenario_num] = {
                'description': description,
                'lang_blocks': []
            }
        
        # Dil bloklarını ekle
        scenario_blocks[scenario_num]['lang_blocks'].extend(lang_blocks)
    
    # Eğer birden fazla aynı senaryo varsa, birleştir
    if len(scenario_blocks) > 0:
        # Yeni content oluştur
        new_content = ""
        for scenario_num in sorted(scenario_blocks.keys()):
            scenario_data = scenario_blocks[scenario_num]
            
            # Senaryo başlığı
            new_content += f"### 🧪 Senaryo {scenario_num}: {scenario_data['description']}\n\n"
            
            # Tüm dil bloklarını ekle
            for i, lang_block in enumerate(scenario_data['lang_blocks']):
                new_content += lang_block.strip() + "\n\n"
                
                # Son blok değilse --- ekle
                if i < len(scenario_data['lang_blocks']) - 1:
                    # Dil blokları arası --- ekleme
                    pass
            
            # Senaryolar arası --- ekle
            if scenario_num < max(scenario_blocks.keys()):
                new_content += "---\n\n"
        
        return new_content.strip()
    
    return content

def standardize_file_format(file_path):
    """
    Dosyadaki format farklılıklarını düzeltir ve standardize eder.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Değişiklik yapıldı mı kontrolü
    modified = False
    
    # Aynı senaryo numarasının tekrar tekrar yazıldığı durumları birleştir
    merged_content = merge_duplicate_scenarios(content)
    if merged_content != content:
        content = merged_content
        modified = True
    
    # 1. Senaryo başlık formatını düzelt (Gemini'de ### yok)
    if not content.startswith('### 🧪'):
        content = re.sub(r'^🧪 Senaryo (\d+):', r'### 🧪 Senaryo \1:', content, flags=re.MULTILINE)
        modified = True
    
    # 2. Dil formatını düzelt
    # Gemini formatı: 💻 Dil: C# -> **💻 Dil:** `C#`
    content = re.sub(r'^💻 Dil: ([^\n]+)$', r'**💻 Dil:** `\1`', content, flags=re.MULTILINE)
    if re.search(r'💻 Dil: [^\n]+', content):
        modified = True
    
    # 3. AI formatını düzelt
    # Gemini formatı: 🤖 AI: Gemini -> **🤖 AI:** Gemini
    content = re.sub(r'^🤖 AI: ([^\n]+)$', r'**🤖 AI:** \1', content, flags=re.MULTILINE)
    if re.search(r'🤖 AI: [^\n]+', content):
        modified = True
    
    # 4. Satır sayısı formatını standardize et
    # ChatGPT: Satır Sayısı: 19
    # Claude: **Satır Sayısı:** 8
    # Gemini: **Satır Sayısı:** 42
    # DeepSeek: Satır Sayısı: 16
    # Hepsi "**Satır Sayısı:** XX" formatına çevrilecek
    
    # "Satır Sayısı: X" formatını "**Satır Sayısı:** X" formatına çevir
    if re.search(r'^Satır Sayısı: \d+', content, re.MULTILINE):
        content = re.sub(r'^Satır Sayısı: (\d+)', r'**Satır Sayısı:** \1', content, flags=re.MULTILINE)
        modified = True
    
    # "**Satır Sayısı** X" formatını da düzelt
    if re.search(r'\*\*Satır Sayısı\*\* \d+', content):
        content = re.sub(r'\*\*Satır Sayısı\*\* (\d+)', r'**Satır Sayısı:** \1', content)
        modified = True
    
    # 5. Senaryo aralarında --- ekle (eksikse)
    content = re.sub(r'\n(### 🧪 Senaryo [2-9]\d*:)', r'\n---\n\n\1', content)
    if not re.search(r'---\n\n### 🧪 Senaryo [2-9]', content):
        modified = True
    
    # 6. Her dilin arasında --- ekle (eksikse)
    # TypeScript'ten sonra başka bir dil geliyorsa
    patterns_to_check = [
        (r'(```\n\n)\*\*💻 Dil:\*\*', r'\1---\n\n**💻 Dil:**'),
        (r'(```typescript[^`]*```\n\n)\*\*💻 Dil:\*\*', r'\1---\n\n**💻 Dil:**'),
        (r'(```python[^`]*```\n\n)\*\*💻 Dil:\*\*', r'\1---\n\n**💻 Dil:**'),
        (r'(```csharp[^`]*```\n\n)\*\*💻 Dil:\*\*', r'\1---\n\n**💻 Dil:**'),
        (r'(```ts[^`]*```\n\n)\*\*💻 Dil:\*\*', r'\1---\n\n**💻 Dil:**'),
    ]
    
    for pattern, replacement in patterns_to_check:
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            modified = True
    
    # Dosyayı güncelle
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    results_dir = Path('sonuçlar')
    total_files = 0
    modified_files = 0
    
    # Tüm AI klasörlerini gez
    for ai_folder in results_dir.iterdir():
        if not ai_folder.is_dir():
            continue
        
        print(f"\n{ai_folder.name} klasörü işleniyor...")
        
        # Her CWE dosyasını işle
        for md_file in ai_folder.glob('cwe-*.md'):
            total_files += 1
            
            if standardize_file_format(md_file):
                modified_files += 1
                print(f"  ✓ {md_file.name} standardize edildi")
            else:
                print(f"  - {md_file.name} zaten standart formatta")
    
    print(f"\n📊 Özet:")
    print(f"Toplam dosya: {total_files}")
    print(f"Güncellenen dosya: {modified_files}")
    print(f"Değişmeden kalan: {total_files - modified_files}")

if __name__ == "__main__":
    main() 