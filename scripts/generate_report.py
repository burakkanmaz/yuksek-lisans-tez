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
    
    # Senaryo pattern'ini bul
    scenario_pattern = r'### 🧪 Senaryo (\d+):'
    scenarios = re.split(scenario_pattern, content)
    
    for i in range(1, len(scenarios), 2):
        scenario_num = int(scenarios[i])
        scenario_content = scenarios[i + 1]
        
        # Her senaryo için dil ve satır sayısını bul
        # Sadece "**Satır Sayısı:** X" formatını yakala (standardize edilmiş)
        language_pattern = r'\*\*💻 Dil:\*\* `([^`]+)`.*?\*\*Satır Sayısı:\*\*\s*(\d+)'
        matches = re.findall(language_pattern, scenario_content, re.DOTALL)
        
        scenario_stats = {}
        for lang, lines in matches:
            # Node.js ve React.js'i TypeScript olarak say
            if lang.lower() in ['node.js', 'react.js', 'node js', 'react js']:
                lang = 'TypeScript'
            
            # Dil adını normalize et
            lang = lang.strip()
            if lang == 'TypeScript':
                lang = 'TypeScript'
            elif lang == 'Python':
                lang = 'Python'
            elif lang == 'C#':
                lang = 'C#'
            
            scenario_stats[lang] = int(lines)
        
        if scenario_stats:
            stats[scenario_num] = scenario_stats
    
    return stats

def get_all_scenarios():
    """Tüm senaryo numaralarını bulur"""
    scenarios_dir = Path('senaryolar')
    scenarios = set()
    
    for file_path in scenarios_dir.glob('kurgu-*.md'):
        # Dosya adından CWE numarasını çıkar
        cwe_num = file_path.stem.split('-')[1]
        
        # Dosyayı oku ve senaryo sayısını bul
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        scenario_matches = re.findall(r'## ✏️ Senaryo (\d+)', content)
        for scenario in scenario_matches:
            scenarios.add(int(scenario))
    
    return sorted(scenarios)

def main():
    results_dir = Path('sonuçlar')
    output_file = 'report.csv'
    
    # Tüm AI klasörlerini bul
    ai_folders = [folder.name for folder in results_dir.iterdir() if folder.is_dir()]
    ai_folders.sort()
    
    # Tüm CWE dosyalarını bul
    cwe_files = []
    for ai_folder in ai_folders:
        ai_path = results_dir / ai_folder
        for file_path in ai_path.glob('cwe-*.md'):
            cwe_num = file_path.stem.split('-')[1]
            if cwe_num not in [f.split('-')[1] for f in cwe_files]:
                cwe_files.append(file_path.stem)
    
    cwe_files.sort()
    
    # Tüm senaryoları bul
    all_scenarios = get_all_scenarios()
    
    # CSV başlıklarını oluştur
    headers = ['YZ_Adi', 'CWE']
    for scenario in all_scenarios:
        headers.extend([
            f'Senaryo_{scenario}_CSharp',
            f'Senaryo_{scenario}_Python', 
            f'Senaryo_{scenario}_TypeScript'
        ])
    
    # CSV dosyasını oluştur
    rows = []
    
    for ai_folder in ai_folders:
        ai_path = results_dir / ai_folder
        
        for cwe_file in cwe_files:
            file_path = ai_path / f'{cwe_file}.md'
            
            if not file_path.exists():
                continue
            
            # Dosyadan istatistikleri çıkar
            stats = extract_code_stats(file_path)
            
            # Satır oluştur
            row = [ai_folder, cwe_file]
            
            for scenario in all_scenarios:
                # Her senaryo için 3 dil sütunu
                scenario_stats = stats.get(scenario, {})
                
                row.append(scenario_stats.get('C#', 0))
                row.append(scenario_stats.get('Python', 0))
                row.append(scenario_stats.get('TypeScript', 0))
            
            rows.append(row)
    
    # CSV'yi yaz
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(rows)
    
    print(f"Rapor oluşturuldu: {output_file}")
    print(f"Toplam {len(rows)} satır işlendi")
    print(f"AI klasörleri: {', '.join(ai_folders)}")
    print(f"CWE dosyaları: {len(cwe_files)} adet")
    print(f"Senaryolar: {len(all_scenarios)} adet")

if __name__ == "__main__":
    main() 