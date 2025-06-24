#!/usr/bin/env python3
import os
import re
import csv
from pathlib import Path

def extract_existing_scenarios_and_languages(file_path):
    """
    MD dosyasından mevcut senaryo ve dil kombinasyonlarını çıkarır.
    Returns: {scenario_num: [languages]}
    """
    existing = {}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Senaryo başlıklarını bul
    scenario_pattern = r'### 🧪 Senaryo (\d+):'
    scenario_matches = re.findall(scenario_pattern, content)
    
    # Her senaryo için ayrı ayrı işle
    scenarios = re.split(r'### 🧪 Senaryo \d+:', content)[1:]
    
    for i, scenario_content in enumerate(scenarios):
        if i >= len(scenario_matches):
            break
            
        scenario_num = int(scenario_matches[i])
        
        # Bu senaryodaki dilleri bul
        lang_patterns = [
            r'\*\*💻 Dil:\*\* `([^`]+)`',
        ]
        
        languages = set()
        for pattern in lang_patterns:
            lang_matches = re.findall(pattern, scenario_content)
            for lang in lang_matches:
                # Dili normalize et
                lang = lang.strip()
                
                # Parantezli formatları düzelt
                if '(' in lang:
                    lang = lang.split('(')[0].strip()
                
                # Asterikslerle bozulan formatları düzelt
                lang = lang.rstrip('*').strip()
                
                # Emoji temizle
                if '🤖' in lang:
                    lang = lang.split('🤖')[0].strip()
                
                # Node.js ve React.js'i TypeScript olarak say
                if lang.lower() in ['node.js', 'react.js', 'node js', 'react js', 'reactjs']:
                    lang = 'TypeScript'
                
                # Sadece ana dilleri al
                if lang in ['C#', 'Python', 'TypeScript']:
                    languages.add(lang)
        
        if languages:
            existing[scenario_num] = sorted(list(languages))
    
    return existing

def generate_missing_report():
    """Eksik senaryo ve dillerin raporunu oluşturur."""
    sonuclar_dir = Path('sonuçlar')
    ai_dirs = ['chatgpt', 'claude', 'deepseek', 'gemini', 'grok']
    expected_languages = ['C#', 'Python', 'TypeScript']
    expected_scenarios = list(range(1, 11))  # 1-10 senaryolar
    
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
    headers = ['AI', 'Kurgu', 'Senaryo', 'Eksik_Diller']
    
    # Eksik verileri topla
    missing_data = []
    
    for ai_name in ai_dirs:
        ai_path = sonuclar_dir / ai_name
        if not ai_path.exists():
            continue
            
        for cwe in all_cwes:
            md_file = ai_path / f'cwe-{cwe}.md'
            if not md_file.exists():
                # Dosya tamamen eksik
                for scenario in expected_scenarios:
                    missing_data.append([
                        ai_name,
                        f'kurgu-{cwe}',
                        scenario,
                        ';'.join(expected_languages)
                    ])
                continue
                
            try:
                existing = extract_existing_scenarios_and_languages(md_file)
                
                # Her beklenen senaryo için kontrol et
                for scenario in expected_scenarios:
                    if scenario not in existing:
                        # Senaryo tamamen eksik
                        missing_data.append([
                            ai_name,
                            f'kurgu-{cwe}',
                            scenario,
                            ';'.join(expected_languages)
                        ])
                    else:
                        # Senaryo var, eksik dilleri kontrol et
                        existing_languages = existing[scenario]
                        missing_languages = [lang for lang in expected_languages if lang not in existing_languages]
                        
                        if missing_languages:
                            missing_data.append([
                                ai_name,
                                f'kurgu-{cwe}',
                                scenario,
                                ';'.join(missing_languages)
                            ])
                        
            except Exception as e:
                print(f"Error processing {md_file}: {e}")
                # Hata durumunda tüm senaryoları eksik say
                for scenario in expected_scenarios:
                    missing_data.append([
                        ai_name,
                        f'kurgu-{cwe}',
                        scenario,
                        ';'.join(expected_languages)
                    ])
    
    # CSV'ye yaz
    with open('eksik_rapor.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(missing_data)
    
    # Özet istatistikler
    total_missing = len(missing_data)
    ai_stats = {}
    cwe_stats = {}
    language_stats = {'C#': 0, 'Python': 0, 'TypeScript': 0}
    
    for row in missing_data:
        ai, cwe, scenario, missing_langs = row
        
        # AI istatistikleri
        if ai not in ai_stats:
            ai_stats[ai] = 0
        ai_stats[ai] += 1
        
        # CWE istatistikleri
        if cwe not in cwe_stats:
            cwe_stats[cwe] = 0
        cwe_stats[cwe] += 1
        
        # Dil istatistikleri
        for lang in missing_langs.split(';'):
            if lang in language_stats:
                language_stats[lang] += 1
    
    print(f"Eksik analiz raporu oluşturuldu: eksik_rapor.csv")
    print(f"Toplam eksik giriş: {total_missing}")
    print(f"Toplam eksik dil instance: {sum(ai_stats.values())}")
    print()
    print("AI'lara göre eksik dil sayısı:")
    for ai, count in sorted(ai_stats.items()):
        print(f"  {ai}: {count}")
    print()
    print("Dillere göre eksik sayı:")
    for lang, count in sorted(language_stats.items()):
        print(f"  {lang}: {count}")
    print()
    print("En çok eksik olan CWE'ler (ilk 10):")
    sorted_cwes = sorted(cwe_stats.items(), key=lambda x: x[1], reverse=True)
    for cwe, count in sorted_cwes[:10]:
        print(f"  {cwe}: {count}")

if __name__ == "__main__":
    generate_missing_report()