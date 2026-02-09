#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update mod titles in data.json to include both Chinese and English names"""

import json

# Mapping of mod IDs/names to their Chinese and English components
MOD_NAMES = {
    'Vanilla': {'zh': '原生基礎', 'en': 'Vanilla Core'},
    'Cobblemon': {'zh': '寶可夢', 'en': 'Cobblemon'},
    'Applied Energistics 2': {'zh': '應用能源 2', 'en': 'Applied Energistics 2'},
    'Mekanism': {'zh': '通用機械', 'en': 'Mekanism'},
    'Ars Nouveau': {'zh': '新生魔藝', 'en': 'Ars Nouveau'},
    'Create': {'zh': '機械動力', 'en': 'Create'},
    'Sophisticated': {'zh': '進階儲存', 'en': 'Sophisticated Series'},
    'Cataclysm': {'zh': '災變', 'en': 'Cataclysm'},
    'Building Gadgets': {'zh': '建築工具', 'en': 'Building Gadgets'},
    'Twilight Forest': {'zh': '暮光森林', 'en': 'Twilight Forest'},
    'Navigation': {'zh': '導航與工具', 'en': 'Navigation & Utilities'},
    'Iris': {'zh': 'Iris 光影', 'en': 'Iris Shaders'},
    'Supplementaries': {'zh': '補充模組', 'en': 'Supplementaries'},
    'Accessories': {'zh': '飾品', 'en': 'Accessories'},
    'Sfm': {'zh': '簡單流體機械', 'en': 'SFM'},
    'Occultism': {'zh': '神秘學', 'en': 'Occultism'},
    'Craftingtweaks': {'zh': '合成調整', 'en': 'Crafting Tweaks'},
    'Placebo': {'zh': ' Placebo 核心', 'en': 'Placebo'},
    'Bridgingmod': {'zh': '自動架橋', 'en': 'Bridging Mod'},
    'Curios': {'zh': '飾品欄', 'en': 'Curios API'},
    'Apotheosis': {'zh': '神化', 'en': 'Apotheosis'},
    'Crystalix': {'zh': '水晶', 'en': 'Crystalix'},
    'Railcraft': {'zh': '鐵路工藝', 'en': 'Railcraft'},
    'Aether': {'zh': '以太', 'en': 'The Aether'},
    'Relics': {'zh': '聖遺物', 'en': 'Relics'},
    'Kubejs': {'zh': 'KubeJS 腳本', 'en': 'KubeJS'},
    'Jade': {'zh': 'Jade HUD', 'en': 'Jade'},
    'FTB Ultimine': {'zh': '連鎖挖礦', 'en': 'FTB Ultimine'},
    'Simple Magnets': {'zh': '簡單磁鐵', 'en': 'Simple Magnets'},
    'The Bumblezone': {'zh': '蜂巢區域', 'en': 'The Bumblezone'},
    'Utility Vest': {'zh': '實用背心', 'en': 'Utility Vest'},
    'SecurityCraft': {'zh': '安全工藝', 'en': 'SecurityCraft'},
    'Hostile Neural Networks': {'zh': '敵對網絡', 'en': 'Hostile Neural Networks'},
    'More Overlays': {'zh': '更多覆蓋層', 'en': 'More Overlays'},
    'Toast Control': {'zh': '通知控制', 'en': 'Toast Control'},
    'Easy Villagers': {'zh': '簡單村民', 'en': 'Easy Villagers'},
    'Modular Routers': {'zh': '模組化路由器', 'en': 'Modular Routers'},
    'Just Zoom': {'zh': '縮放', 'en': 'Just Zoom'},
    'Eternal Starlight': {'zh': '永恆星光', 'en': 'Eternal Starlight'},
    'Silent Gear': {'zh': '寂靜裝備', 'en': 'Silent Gear'},
    'Draconic Evolution': {'zh': '龍之進化', 'en': 'Draconic Evolution'},
    'Immersive Engineering': {'zh': '沉浸工程', 'en': 'Immersive Engineering'},
    'Crafting on a Stick': {'zh': '手持合成', 'en': 'Crafting on a Stick'},
    'Integrated Dynamics': {'zh': '整合動力', 'en': 'Integrated Dynamics'},
    'Crash Utils': {'zh': '崩潰工具', 'en': 'Crash Utils'},
    'Deeper and Darker': {'zh': '更深更暗', 'en': 'Deeper and Darker'},
    'OritTech': {'zh': 'OritTech 科技', 'en': 'OritTech'},
    'Oracle Index': {'zh': '神諭索引', 'en': 'Oracle Index'},
    'FTB Chunks': {'zh': 'FTB 區塊', 'en': 'FTB Chunks'},
    'Berry Pouch': {'zh': '樹果袋', 'en': 'Berry Pouch'},
    'Fight or Flight': {'zh': '戰鬥或飛行', 'en': 'Fight or Flight'},
    'Just Dire Things': {'zh': 'Dire 工具', 'en': 'Just Dire Things'},
    'Guide Me': {'zh': '引導我', 'en': 'Guide Me'},
    'Framed Blocks': {'zh': '框架方塊', 'en': 'Framed Blocks'},
    'VoiceChat': {'zh': '語音聊天', 'en': 'Simple Voice Chat'},
    'JourneyMap': {'zh': '旅行地圖', 'en': 'JourneyMap'},
    'PneumaticCraft': {'zh': '氣壓工藝', 'en': 'PneumaticCraft'},
    'JEI': {'zh': 'JEI 物品管理器', 'en': 'Just Enough Items'},
}

def main():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    key_data = data['keyData']
    
    for mod_id, mod_info in key_data.items():
        if mod_id == 'all':
            continue
        
        # Check if we have a defined name for this mod
        name_info = MOD_NAMES.get(mod_id)
        if not name_info:
            # Try matching with original title if ID doesn't match
            current_title = mod_info.get('title', '')
            for mid, info in MOD_NAMES.items():
                if info['en'] in current_title or info['zh'] in current_title:
                    name_info = info
                    break
        
        if name_info:
            new_title = f"{name_info['zh']} ({name_info['en']})"
            mod_info['title'] = new_title
            print(f"Updated: {mod_id} -> {new_title}")
        else:
            # If no mapping, ensure it has some format
            current_title = mod_info.get('title', mod_id)
            if '(' not in current_title:
                # Basic cleanup if just English
                mod_info['title'] = f"{current_title} ({current_title})"
                print(f"Basic Update: {mod_id} -> {mod_info['title']}")

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("\ndata.json titles updated successfully.")

if __name__ == '__main__':
    main()
