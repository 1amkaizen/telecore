# telecore/telegram/generate_group.py

import os
from telecore import config  



def generate_grup_markdown() -> str:
      
    total_grup = config.GROUP_COUNT
    grup_per_baris = config.GROUP_PER_BARIS
    
    grup_md_list = []

    for i in range(1, total_grup + 1):
        nama = os.getenv(f"GRUP_{i}_NAMA", f"Grup {i}")
        link = os.getenv(f"GRUP_{i}_LINK", "#")
        grup_md_list.append(f"[{nama}]({link})")

    baris_md = []
    for i in range(0, len(grup_md_list), grup_per_baris):
        baris = grup_md_list[i:i+grup_per_baris]
        baris_md.append(" | ".join(baris))

    return "\n".join(baris_md)  

