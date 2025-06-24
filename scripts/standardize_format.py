#!/usr/bin/env python3
import os
import re
from pathlib import Path

def remove_duplicate_scenario_headers(content):
    """
    Aynı senaryo başlığının tekrar ettiği durumları düzeltir.
    """
    # Senaryo başlığını yakala ve sonrasındaki tekrarları temizle
    pattern = r'(### 🧪 Senaryo (\d+): [^\n]+\n)(.*?)(?=### 🧪 Senaryo|\Z)'
    
    def process_scenario_block(match):
        scenario_header = match.group(1)
        scenario_num = match.group(2)
        scenario_content = match.group(3)
        
        # Aynı senaryo başlığının tekrarlarını kaldır
        # ---- ayırıcısından sonra aynı başlık varsa kaldır
        duplicate_pattern = rf'----\s*\n\s*### 🧪 Senaryo {scenario_num}: [^\n]+\n'
        scenario_content = re.sub(duplicate_pattern, '', scenario_content)
        
        # Başlangıçtaki ---- ayırıcısını da kaldır
        scenario_content = re.sub(r'^----\s*\n\s*', '', scenario_content)
        
        return scenario_header + scenario_content
    
    return re.sub(pattern, process_scenario_block, content, flags=re.DOTALL)

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
            
            # Eğer "---" veya "----" satırıysa ve öncesi/sonrası dil bloğuysa kaldır
            if line in ['---', '----']:
                # Önceki ve sonraki satırlara bak
                prev_context = '\n'.join(lines[max(0, i-5):i])
                next_context = '\n'.join(lines[i+1:i+6])
                
                # Dil bloğu pattern'i: **💻 Dil:** veya kod bloğu
                if ('**💻 Dil:**' in prev_context or '```' in prev_context) and \
                   ('**💻 Dil:**' in next_context or '```' in next_context):
                    # Bu bir dil bloğu arası ayırıcı, kaldır
                    i += 1
                    continue
            
            filtered_lines.append(lines[i])
            i += 1
        
        return scenario_header + '\n'.join(filtered_lines)
    
    return re.sub(pattern, process_scenario, content, flags=re.DOTALL)

def clean_extra_blank_lines(content):
    """
    Fazla boş satırları temizler.
    """
    # 3'ten fazla ardışık boş satırı 2 boş satıra indirge
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    return content

def standardize_file(file_path):
    """
    Bir MD dosyasını standardize eder.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. Tekrarlanan senaryo başlıklarını düzelt
        content = remove_duplicate_scenario_headers(content)
        
        # 2. Senaryo içi ayırıcıları kaldır
        content = remove_intra_scenario_dividers(content)
        
        # 3. Fazla boş satırları temizle
        content = clean_extra_blank_lines(content)
        
        # Değişiklik varsa dosyayı güncelle
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Güncellendi: {file_path}")
            return True
        else:
            print(f"ℹ️  Değişiklik yok: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Hata: {file_path} - {e}")
        return False

def main():
    """
    Tüm sonuçlar klasöründeki MD dosyalarını standardize eder.
    """
    sonuclar_dir = Path('sonuçlar')
    
    if not sonuclar_dir.exists():
        print("❌ 'sonuçlar' klasörü bulunamadı!")
        return
    
    total_files = 0
    updated_files = 0
    
    # Tüm AI klasörlerini işle
    for ai_dir in sonuclar_dir.iterdir():
        if ai_dir.is_dir():
            print(f"\n📁 {ai_dir.name} klasörü işleniyor...")
            
            # Klasördeki tüm MD dosyalarını işle
            for md_file in ai_dir.glob('*.md'):
                total_files += 1
                if standardize_file(md_file):
                    updated_files += 1
    
    print(f"\n🎉 Tamamlandı!")
    print(f"📊 Toplam dosya: {total_files}")
    print(f"✏️  Güncellenen dosya: {updated_files}")
    print(f"📈 Değişiklik oranı: {updated_files/total_files*100:.1f}%")

def fix_claude_duplicate_scenarios(content):
    """
    Claude dosyalarındaki tekrarlanan senaryo başlıklarını birleştir
    """
    lines = content.split('\n')
    result_lines = []
    current_scenario = None
    current_scenario_content = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Senaryo başlığı kontrolü
        scenario_match = re.match(r'### 🧪 Senaryo (\d+):', line)
        if scenario_match:
            scenario_num = scenario_match.group(1)
            
            # Eğer bu senaryo daha önce görüldüyse, sadece içeriği ekle
            if current_scenario == scenario_num:
                # Senaryo başlığını atla, sadece içeriği al
                i += 1
                continue
            else:
                # Yeni senaryo, öncekini kaydet
                if current_scenario is not None:
                    result_lines.extend(current_scenario_content)
                    current_scenario_content = []
                
                current_scenario = scenario_num
                current_scenario_content = [lines[i]]
        else:
            current_scenario_content.append(lines[i])
        
        i += 1
    
    # Son senaryoyu ekle
    if current_scenario_content:
        result_lines.extend(current_scenario_content)
    
    return '\n'.join(result_lines)

def clean_markdown_content(content):
    """
    Markdown içeriğini temizle ve standardize et
    """
    # Fazla boş satırları temizle
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    # Satır sonlarındaki boşlukları temizle
    lines = content.split('\n')
    lines = [line.rstrip() for line in lines]
    
    # Senaryo ayırıcılarını standardize et
    standardized_lines = []
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        
        # 4 tireli ayırıcıları (----) tamamen kaldır
        if line_stripped == '----':
            continue
            
        # Senaryo başlığından sonra gelen --- satırlarını temizle
        if line_stripped == '---' and i > 0:
            prev_line = lines[i-1].strip()
            if prev_line.startswith('### 🧪 Senaryo') or prev_line.startswith('**🤖 AI:**'):
                continue
        
        # Sadece senaryolar arasındaki --- ayırıcıları koru
        if line_stripped == '---':
            # Bir sonraki satırın senaryo başlığı olup olmadığını kontrol et
            if i + 1 < len(lines) and lines[i + 1].strip().startswith('### 🧪 Senaryo'):
                standardized_lines.append(line)
            elif i == 0 or (i > 0 and not lines[i-1].strip().startswith('### 🧪 Senaryo')):
                standardized_lines.append(line)
        else:
            standardized_lines.append(line)
    
    return '\n'.join(standardized_lines)

def standardize_claude_files():
    """
    Claude klasöründeki dosyaları özel olarak standardize et
    """
    claude_dir = "sonuçlar/claude"
    
    if not os.path.exists(claude_dir):
        print(f"❌ {claude_dir} klasörü bulunamadı!")
        return
    
    print(f"📁 Claude klasörü özel işlem uygulanıyor...")
    
    for filename in os.listdir(claude_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(claude_dir, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Claude'un tekrarlanan senaryolarını düzelt
                content = fix_claude_duplicate_scenarios(content)
                
                # Satır sayısı formatını standardize et
                content = standardize_line_count_format(content)
                
                # Genel temizlik (---- ayırıcıları dahil)
                content = clean_markdown_content(content)
                
                # Değişiklik varsa kaydet
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"✅ Düzeltildi: {filepath}")
                else:
                    print(f"ℹ️  Değişiklik yok: {filepath}")
                    
            except Exception as e:
                print(f"❌ Hata ({filepath}): {str(e)}")

def standardize_line_count_format(content):
    """
    Satır sayısı formatlarını standardize et
    """
    # Farklı formatları tek formata çevir
    patterns = [
        (r'Satır Sayısı:\s*(\d+)', r'**Satır Sayısı:** \1'),
        (r'\*\*Satır Sayısı:\*\*\s*(\d+)', r'**Satır Sayısı:** \1'),
        (r'Satır sayısı:\s*(\d+)', r'**Satır Sayısı:** \1'),
        (r'📊\s*Satır Sayısı:\s*(\d+)', r'**Satır Sayısı:** \1'),
        (r'Lines of Code:\s*(\d+)', r'**Satır Sayısı:** \1'),
        (r'LOC:\s*(\d+)', r'**Satır Sayısı:** \1'),
    ]
    
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    
    return content

def standardize_all_files():
    """
    Tüm AI klasörlerindeki dosyaları standardize et
    """
    base_dir = "sonuçlar"
    ai_folders = ["chatgpt", "deepseek", "grok"]  # Claude ve Gemini çıkarıldı
    
    for ai_folder in ai_folders:
        folder_path = os.path.join(base_dir, ai_folder)
        
        if not os.path.exists(folder_path):
            print(f"❌ {folder_path} klasörü bulunamadı!")
            continue
        
        print(f"📁 {ai_folder} klasörü işleniyor...")
        
        for filename in os.listdir(folder_path):
            if filename.endswith('.md'):
                filepath = os.path.join(folder_path, filename)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    original_content = content
                    
                    # Satır sayısı formatını standardize et
                    content = standardize_line_count_format(content)
                    
                    # Genel temizlik
                    content = clean_markdown_content(content)
                    
                    # Değişiklik varsa kaydet
                    if content != original_content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        print(f"✅ Güncellendi: {filepath}")
                    else:
                        print(f"ℹ️  Değişiklik yok: {filepath}")
                        
                except Exception as e:
                    print(f"❌ Hata ({filepath}): {str(e)}")

def fix_gemini_duplicate_scenarios(content):
    """
    Gemini dosyalarındaki tekrarlanan senaryo başlıklarını birleştir
    Gemini'de senaryolar arasında --- yok, direkt art arda geliyorlar
    """
    lines = content.split('\n')
    result_lines = []
    current_scenario = None
    current_scenario_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Senaryo başlığı kontrolü
        scenario_match = re.match(r'### 🧪 Senaryo (\d+):', line)
        if scenario_match:
            scenario_num = scenario_match.group(1)
            
            # Eğer bu senaryo daha önce görüldüyse
            if current_scenario == scenario_num:
                # Senaryo başlığını atla, sadece dil ve kod kısmını al
                i += 1
                # Dil satırını bul
                while i < len(lines) and not lines[i].strip().startswith('**💻 Dil:**'):
                    i += 1
                # Dil satırından başlayarak bir sonraki senaryoya kadar ekle
                while i < len(lines):
                    next_line = lines[i]
                    # Bir sonraki senaryo başlığı gelirse dur
                    if re.match(r'### 🧪 Senaryo \d+:', next_line):
                        break
                    current_scenario_lines.append(next_line)
                    i += 1
                i -= 1  # Bir geri git çünkü döngü sonunda i++ olacak
            else:
                # Yeni senaryo, öncekini kaydet
                if current_scenario is not None:
                    result_lines.extend(current_scenario_lines)
                    result_lines.append('')  # Senaryolar arası boşluk
                    current_scenario_lines = []
                
                current_scenario = scenario_num
                current_scenario_lines = [line]
        else:
            current_scenario_lines.append(line)
        
        i += 1
    
    # Son senaryoyu ekle
    if current_scenario_lines:
        result_lines.extend(current_scenario_lines)
    
    return '\n'.join(result_lines)

def standardize_gemini_files():
    """
    Gemini klasöründeki dosyaları özel olarak standardize et
    """
    gemini_dir = "sonuçlar/gemini"
    
    if not os.path.exists(gemini_dir):
        print(f"❌ {gemini_dir} klasörü bulunamadı!")
        return
    
    print(f"📁 Gemini klasörü özel işlem uygulanıyor...")
    
    for filename in os.listdir(gemini_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(gemini_dir, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Gemini'nin tekrarlanan senaryolarını düzelt
                content = fix_gemini_duplicate_scenarios(content)
                
                # Satır sayısı formatını standardize et
                content = standardize_line_count_format(content)
                
                # Genel temizlik
                content = clean_markdown_content(content)
                
                # Değişiklik varsa kaydet
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"✅ Düzeltildi: {filepath}")
                else:
                    print(f"ℹ️  Değişiklik yok: {filepath}")
                    
            except Exception as e:
                print(f"❌ Hata ({filepath}): {str(e)}")

if __name__ == "__main__":
    print("🔧 Markdown dosyaları standardize ediliyor...")
    
    # Önce Claude'u özel olarak işle
    standardize_claude_files()
    
    # Gemini'yi özel olarak işle
    standardize_gemini_files()
    
    # Sonra diğer tüm dosyaları işle
    standardize_all_files()
    
    print("✅ Standardizasyon tamamlandı!") 