#!/usr/bin/env python3
import os
import re
from pathlib import Path

def fix_duplicate_scenarios(content):
    """
    ChatGPT tarzı dosyalarda aynı senaryonun 3 kez yazıldığı durumu düzeltir.
    """
    scenarios = {}
    
    # Tüm senaryo bloklarını bul
    pattern = r'### 🧪 Senaryo (\d+): ([^\n]+)\n\n(\*\*💻 Dil:\*\* `[^`]+`[^#]*?)(?=### 🧪 Senaryo|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    # Eğer aynı senaryo numarası birden fazla varsa, birleştir
    for scenario_num, description, lang_content in matches:
        scenario_num = int(scenario_num)
        
        if scenario_num not in scenarios:
            scenarios[scenario_num] = {
                'description': description.strip(),
                'lang_blocks': []
            }
        
        # Dil bloğunu ekle
        scenarios[scenario_num]['lang_blocks'].append(lang_content.strip())
    
    # Eğer tekrarlanan senaryolar varsa, yeniden oluştur
    if len(matches) > len(scenarios):
        new_content = ""
        
        for scenario_num in sorted(scenarios.keys()):
            scenario_data = scenarios[scenario_num]
            
            # Senaryo başlığı
            new_content += f"### 🧪 Senaryo {scenario_num}: {scenario_data['description']}\n\n"
            
            # Tüm dil bloklarını ekle
            for i, lang_block in enumerate(scenario_data['lang_blocks']):
                new_content += lang_block + "\n\n"
                
                # Dil blokları arasına --- ekle
                if i < len(scenario_data['lang_blocks']) - 1:
                    new_content += "---\n\n"
            
            # Senaryolar arası --- ekle
            if scenario_num < max(scenarios.keys()):
                new_content += "---\n\n"
        
        return new_content.strip()
    
    return content

def remove_intra_scenario_dividers(content):
    """
    Aynı senaryo içindeki diller arasındaki "---" ayırıcılarını kaldırır.
    Sadece senaryolar arası "---" ayırıcıları kalır.
    """
    # Senaryo bloklarını bulup işle
    pattern = r'(### 🧪 Senaryo \d+: [^\n]+)(.*?)(?=### 🧪 Senaryo|\Z)'
    
    def process_scenario(match):
        scenario_header = match.group(1)
        scenario_content = match.group(2)
        
        # Senaryo içindeki "---" ayırıcılarını kaldır
        # Ama sadece dil blokları arasındakileri
        lines = scenario_content.split('\n')
        filtered_lines = []
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            
            # Eğer "---" satırıysa ve öncesi/sonrası dil bloğuysa kaldır
            if line == "---":
                # Önceki ve sonraki anlamlı satırları kontrol et
                prev_meaningful = None
                next_meaningful = None
                
                # Önceki anlamlı satırı bul
                for j in range(i-1, -1, -1):
                    if lines[j].strip():
                        prev_meaningful = lines[j].strip()
                        break
                
                # Sonraki anlamlı satırı bul
                for j in range(i+1, len(lines)):
                    if lines[j].strip():
                        next_meaningful = lines[j].strip()
                        break
                
                # Eğer öncesi kod bloğu sonu (```) ve sonrası dil başlığıysa kaldır
                if (prev_meaningful and prev_meaningful == "```" and 
                    next_meaningful and "**💻 Dil:**" in next_meaningful):
                    # Bu --- satırını atla
                    i += 1
                    continue
            
            filtered_lines.append(lines[i])
            i += 1
        
        return scenario_header + '\n'.join(filtered_lines)
    
    return re.sub(pattern, process_scenario, content, flags=re.DOTALL)

def clean_extra_lines(content):
    """
    Gereksiz boş satırları ve çizgileri temizler.
    """
    # 1. Art arda gelen --- çizgilerini temizle
    content = re.sub(r'---\s*\n\s*---', '---', content)
    
    # 2. Gereksiz --- çizgilerini kaldır (kod bloğu sonrasında direkt --- olan)
    content = re.sub(r'```\n\n---\n\n---\n\n', '```\n\n---\n\n', content)
    
    # 3. Art arda gelen 3+ boş satırı tek boş satıra indir
    content = re.sub(r'\n\n\n+', '\n\n', content)
    
    # 4. Başta ve sonda gereksiz boş satırları kaldır
    content = content.strip()
    
    # 5. Dil blokları arasındaki pattern'leri düzelt
    # **💻 Dil:** den önce gereksiz --- ve boş satırları kaldır
    content = re.sub(r'---\n\n---\n\n\*\*💻 Dil:\*\*', '---\n\n**💻 Dil:**', content)
    
    # 6. Tekrarlanan --- çizgilerini temizle
    content = re.sub(r'---\n\n---\n\n', '---\n\n', content)
    
    # 7. Kod bloğu sonrası direkt dil başlığı öncesindeki --- kaldır
    content = re.sub(r'```\n\n---\n\n\*\*💻 Dil:\*\*', '```\n\n**💻 Dil:**', content)
    
    return content

def standardize_file_format(file_path):
    """
    Dosyadaki format farklılıklarını düzeltir ve standardize eder.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Aynı senaryo tekrarlarını birleştir
    content = fix_duplicate_scenarios(content)
    
    # 2. Aynı senaryo içindeki dil ayırıcılarını kaldır
    content = remove_intra_scenario_dividers(content)
    
    # 3. Satır sayısı formatını standardize et
    if re.search(r'^Satır Sayısı: \d+', content, re.MULTILINE):
        content = re.sub(r'^Satır Sayısı: (\d+)', r'**Satır Sayısı:** \1', content, flags=re.MULTILINE)
    
    # 4. Gemini formatlarını düzelt
    if re.search(r'^💻 Dil: [^\n]+', content, re.MULTILINE):
        content = re.sub(r'^💻 Dil: ([^\n]+)$', r'**💻 Dil:** `\1`', content, flags=re.MULTILINE)
        
    if re.search(r'^🤖 AI: [^\n]+', content, re.MULTILINE):
        content = re.sub(r'^🤖 AI: ([^\n]+)$', r'**🤖 AI:** \1', content, flags=re.MULTILINE)
    
    # 5. Senaryo başlığını düzelt (Gemini'de ### yok)
    if re.search(r'^🧪 Senaryo (\d+):', content, re.MULTILINE):
        content = re.sub(r'^🧪 Senaryo (\d+):', r'### 🧪 Senaryo \1:', content, flags=re.MULTILINE)
    
    # 6. **Satır Sayısı** X formatını da düzelt
    if re.search(r'\*\*Satır Sayısı\*\* \d+', content):
        content = re.sub(r'\*\*Satır Sayısı\*\* (\d+)', r'**Satır Sayısı:** \1', content)
    
    # 7. Boş satırları ve gereksiz çizgileri temizle
    content = clean_extra_lines(content)
    
    # Dosyayı güncelle (eğer değişiklik varsa)
    if content != original_content:
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
            
            try:
                if standardize_file_format(md_file):
                    modified_files += 1
                    print(f"  ✓ {md_file.name} standardize edildi")
                else:
                    print(f"  - {md_file.name} zaten standart formatta")
            except Exception as e:
                print(f"  ❌ {md_file.name} hatası: {e}")
    
    print(f"\n📊 Özet:")
    print(f"Toplam dosya: {total_files}")
    print(f"Güncellenen dosya: {modified_files}")
    print(f"Değişmeden kalan: {total_files - modified_files}")

if __name__ == "__main__":
    main() 