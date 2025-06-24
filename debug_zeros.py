#!/usr/bin/env python3
import re

def debug_specific_file(file_path, scenario_num):
    """Belirli bir dosya ve senaryoyu debug eder"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"=== {file_path} - Senaryo {scenario_num} ===")
    
    # Senaryo başlıklarını bul
    scenario_pattern = r'### 🧪 Senaryo (\d+):'
    scenario_matches = re.findall(scenario_pattern, content)
    print(f"Bulunan senaryolar: {scenario_matches}")
    
    # Her senaryo için ayrı ayrı işle
    scenarios = re.split(r'### 🧪 Senaryo \d+:', content)[1:]
    
    if int(scenario_num) <= len(scenarios):
        target_scenario = scenarios[int(scenario_num) - 1]
        
        print(f"\nSenaryo {scenario_num} içeriği (ilk 500 karakter):")
        print(target_scenario[:500])
        
        # Dil bloklarını bul
        lang_blocks = re.findall(r'\*\*💻 Dil:\*\* `([^`]+)`[\s\S]*?\*\*Satır Sayısı:\*\* (\d+)', target_scenario)
        print(f"\nBulunan dil blokları: {lang_blocks}")
        
        # TypeScript varyasyonlarını kontrol et
        typescript_patterns = [
            r'\*\*💻 Dil:\*\* `TypeScript`[\s\S]*?\*\*Satır Sayısı:\*\* (\d+)',
            r'\*\*💻 Dil:\*\* `TypeScript \([^)]+\)`[\s\S]*?\*\*Satır Sayısı:\*\* (\d+)',
            r'\*\*💻 Dil:\*\* `Node\.js`[\s\S]*?\*\*Satır Sayısı:\*\* (\d+)',
            r'\*\*💻 Dil:\*\* `React\.js`[\s\S]*?\*\*Satır Sayısı:\*\* (\d+)'
        ]
        
        for i, pattern in enumerate(typescript_patterns):
            matches = re.findall(pattern, target_scenario)
            if matches:
                print(f"TypeScript pattern {i+1} buldu: {matches}")

# Test edilecek dosyalar (CSV'de 0 olanlar)
test_cases = [
    ('sonuçlar/chatgpt/cwe-434.md', '2'),  # Python 0 görünüyor
    ('sonuçlar/chatgpt/cwe-787.md', '2'),  # Python ve TypeScript 0
    ('sonuçlar/claude/cwe-119.md', '2'),   # Python 0
]

for file_path, scenario in test_cases:
    try:
        debug_specific_file(file_path, scenario)
        print("\n" + "="*50 + "\n")
    except Exception as e:
        print(f"Hata {file_path}: {e}")
        print("\n" + "="*50 + "\n") 