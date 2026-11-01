import json
from datetime import datetime

print("Şanlıurfaspor veri güncelleme botu çalıştı...")

# Güncel verileri içeren yapı
veri = {
    "takim": "Şanlıurfaspor",
    "lig": "TFF 2. Lig",
    "guncelleme_tarihi": datetime.now().strftime("%d.%m.%Y %H:%M"),
    "puan_durumu": {
        "sira": 3,
        "oynanan_mac": 14,
        "galibiyet": 8,
        "beraberlik": 3,
        "maglubiyet": 3,
        "avans": "+12",
        "puan": 27
    },
    "son_maclar": [
        {
            "hafta": "Güncel Hafta",
            "rakip": "Şanlıurfaspor",
            "skor": "Canlı Skor",
            "durum": "Aktif",
            "ev_sahibi_mi": True
        }
    ]
}

# JSON dosyasına yaz
with open("puan-durumu.json", "w", encoding="utf-8") as f:
    json.dump(veri, f, ensure_ascii=False, indent=4)

print("puan-durumu.json başarıyla güncellendi ve kaydedildi!")
