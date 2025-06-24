#!/usr/bin/env python3
import re

def debug_cwe125():
    output = []
    
    with open('sonuçlar/chatgpt/cwe-125.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    output.append("=== SENARYO SPLIT TEST ===")
    scenario_pattern = r'### 🧪 Senaryo (\d+):'
    scenario_matches = re.findall(scenario_pattern, content)
    output.append(f"Bulunan senaryolar: {scenario_matches}")
    
    scenarios = re.split(r'### 🧪 Senaryo \d+:', content)[1:]
    output.append(f"Split sonucu {len(scenarios)} senaryo")
    
    output.append("\n=== İLK SENARYO ANALIZI ===")
    if scenarios:
        first_scenario = scenarios[0]
        output.append(f"İlk senaryo uzunluğu: {len(first_scenario)} karakter")
        output.append(f"İlk 500 karakter:\n{first_scenario[:500]}...")
        
        # Dil bloklarını bul
        lang_pattern = r'\*\*💻 Dil:\*\* `([^`]+)`[^*]*?\*\*Satır Sayısı:\*\* (\d+)'
        lang_blocks = re.findall(lang_pattern, first_scenario, re.DOTALL)
        output.append(f"\nBulunan dil blokları: {lang_blocks}")
        
        # Alternatif regex dene
        alt_pattern = r'\*\*💻 Dil:\*\* `([^`]+)`.*?\*\*Satır Sayısı:\*\* (\d+)'
        alt_blocks = re.findall(alt_pattern, first_scenario, re.DOTALL)
        output.append(f"Alternatif regex ile bulunan: {alt_blocks}")
        
        # Daha geniş pattern
        wide_pattern = r'\*\*💻 Dil:\*\* `([^`]+)`[\s\S]*?\*\*Satır Sayısı:\*\* (\d+)'
        wide_blocks = re.findall(wide_pattern, first_scenario)
        output.append(f"Geniş regex ile bulunan: {wide_blocks}")
    
    # Çıktıyı dosyaya yaz
    with open('debug_output.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))
    
    print("Debug tamamlandı. debug_output.txt dosyasını kontrol et.")

if __name__ == "__main__":
    debug_cwe125() 