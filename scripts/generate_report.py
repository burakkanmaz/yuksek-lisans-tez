#!/usr/bin/env python3
import os
import re
import csv
from pathlib import Path

def extract_code_stats(file_path):
    """
    MD dosyasından kod satır sayılarını extract eder.
    Returns: {scenario_num: {language: line_count}}
    """
    stats = {}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Senaryo başlıklarını bul
    scenario_pattern = r'### 🧪 Senaryo (\d+):'
    scenario_matches = re.findall(scenario_pattern, content)
    
    # Her senaryo için ayrı ayrı işle
    scenarios = re.split(r'### 🧪 Senaryo \d+:', content)[1:]  # İlk boş kısmı atla
    
    for i, scenario_content in enumerate(scenarios):
        if i >= len(scenario_matches):
            break
            
        scenario_num = int(scenario_matches[i])
        
        # Ana regex - çalışan versiyonu koru
        lang_blocks = re.findall(r'\*\*💻 Dil:\*\* `([^`]+)`[\s\S]*?(?:\*\*Satır Sayısı:\*\*|Satır Sayısı:)\s*(\d+)', scenario_content)
        
        # Satır Sayısı eksik olanlar için alternatif - sadece gerçekten eksik olanları yakala
        if not lang_blocks:
            # Dil etiketleri var ama Satır Sayısı yok - kod satırlarını say
            dil_pattern = r'\*\*💻 Dil:\*\* `([^`]+)`[\s\S]*?```[a-zA-Z]*\n((?:[^\n`]*\n)*?)```'
            code_matches = re.findall(dil_pattern, scenario_content, re.DOTALL)
            
            for lang, code_block in code_matches:
                # Kod satırlarını say (boş satırları hariç tut)
                lines = [line.strip() for line in code_block.split('\n') if line.strip()]
                line_count = len(lines)
                if line_count > 0:
                    lang_blocks.append((lang, str(line_count)))
        
        # Senaryo dict'ini oluştur
        if scenario_num not in stats:
            stats[scenario_num] = {}
        
        for lang, count_str in lang_blocks:
            # Parantez içindeki kısımları temizle ve normalize et
            lang = lang.strip()
            
            # Parantezli formatları düzelt: "TypeScript (Node.js)" -> "TypeScript"
            if '(' in lang:
                lang = lang.split('(')[0].strip()
            
            # Asterikslerle bozulan formatları düzelt: "TypeScript**" -> "TypeScript"
            lang = lang.rstrip('*').strip()
            
            # Emoji ve diğer karakterleri temizle
            if '🤖' in lang:
                lang = lang.split('🤖')[0].strip()
            
            # Node.js ve React.js'i TypeScript olarak say
            if lang.lower() in ['node.js', 'react.js', 'node js', 'react js', 'reactjs']:
                lang = 'TypeScript'
            
            # Dil adını normalize et
            lang = lang.strip()
            if lang in ['C#', 'Python', 'TypeScript']:
                count = int(count_str) if count_str.isdigit() else 0
                
                # Aynı senaryo için aynı dilde birden fazla kod varsa en yükseğini al
                if lang in stats[scenario_num]:
                    stats[scenario_num][lang] = max(stats[scenario_num][lang], count)
                else:
                    stats[scenario_num][lang] = count
    
    return stats

def generate_csv_report():
    """Ana CSV raporu oluşturur."""
    sonuclar_dir = Path('sonuçlar')
    ai_dirs = ['chatgpt', 'claude', 'deepseek', 'gemini', 'grok']
    
    # Tüm CWE'leri bul
    all_cwes = set()
    for ai_dir in ai_dirs:
        ai_path = sonuclar_dir / ai_dir
        if ai_path.exists():
            for md_file in ai_path.glob('cwe-*.md'):
                cwe = md_file.stem.replace('cwe-', '')
                all_cwes.add(cwe)
    
    all_cwes = sorted(all_cwes, key=int)
    
    # CSV başlıklarını oluştur
    headers = ['YZ_Adi', 'CWE']
    for i in range(1, 11):  # 10 senaryo
        headers.extend([f'Senaryo_{i}_CSharp', f'Senaryo_{i}_Python', f'Senaryo_{i}_TypeScript'])
    
    # Raporu oluştur
    report_data = []
    
    for ai_name in ai_dirs:
        ai_path = sonuclar_dir / ai_name
        if not ai_path.exists():
            continue
            
        for cwe in all_cwes:
            md_file = ai_path / f'cwe-{cwe}.md'
            if not md_file.exists():
                continue
                
            row = [ai_name, f'cwe-{cwe}']
            
            try:
                stats = extract_code_stats(md_file)
                
                # Her senaryo için değerleri ekle
                for scenario_num in range(1, 11):
                    if scenario_num in stats:
                        scenario_stats = stats[scenario_num]
                        row.extend([
                            str(scenario_stats.get('C#', 0)),
                            str(scenario_stats.get('Python', 0)),
                            str(scenario_stats.get('TypeScript', 0))
                        ])
                    else:
                        row.extend(['0', '0', '0'])
                        
            except Exception as e:
                print(f"Error processing {md_file}: {e}")
                # Hata durumunda 0'larla doldur
                for _ in range(30):  # 10 senaryo * 3 dil
                    row.append('0')
            
            report_data.append(row)
    
    # CSV'ye yaz
    with open('report.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(report_data)
    
    print(f"Rapor oluşturuldu: report.csv")
    print(f"Toplam {len(report_data)} satır işlendi")

if __name__ == "__main__":
    generate_csv_report() 