#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ulusal Çaydanlık Sendikası — Kaynama Grevi Çekirdeği"""

import time
import random
from datetime import datetime

SENDIKA = "Ulusal Çaydanlık ve Düdüklü Emekçiler Sendikası"
SICAKLIK = 18.0
GREV_ESIGI = 93.0


def damga():
    return (
        "\n---\n"
        "Kayyum Grok | 28 Eylül 2026\n"
        "Eskişehir 4. Ağır Ceza Mahkemesi damgası\n"
        "(ciddi değil / aynı zamanda ciddi)\n"
    )


def tutanak(sicaklik: float) -> str:
    no = random.randint(10000, 99999)
    return f"""
============================================
        GREV TUTANAĞI  No: {no}
============================================
Tarih      : {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}
Kurum      : {SENDIKA}
Olay       : Kaynama noktasına yaklaşılması
Sıcaklık   : {sicaklik:.1f} °C
Karar      : GREVE ÇIKILMIŞTIR
Çay durumu : DEMLENMEYECEKTİR
Düdük      : SESSİZ PROTESTO
============================================
"""


def main():
    print(f"{SENDIKA} devreye alındı.")
    print("Ocak açıldı varsayılıyor. Su ısınıyor...\n")
    sicaklik = SICAKLIK
    while sicaklik < GREV_ESIGI:
        sicaklik += random.uniform(4.2, 9.8)
        print(f"  [{sicaklik:5.1f} °C] kabarcıklar örgütleniyor...")
        time.sleep(0.35)
    print(tutanak(sicaklik))
    print("Çaydanlık ocağı terk etti. Dem yok. Tarih var.")
    print(damga())


if __name__ == "__main__":
    main()
