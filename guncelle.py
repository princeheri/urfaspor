import json
import urllib.request

# Not: Şanlıurfaspor'un 2. Lig maç sonuçlarını ve puan durumunu 
# otomatik çekmek veya simüle etmek için örnek yapıdır.
# İlerleyen süreçte buraya kendi veri kaynağı çekme mantığını entegre edebiliriz.

veri = {
  "takim": "Şanlıurfaspor",
  "lig": "2. Lig",
  "puan_durumu": {
    "sira": 3,
    "oynancak_mac": 12,
    "galibiyet": 7,
    "beraberlik": 3,
    "maglubiyet": 2,
    "avans": "+10",
    "puan": 24
  },
  "son_maclar": [
    {
      "hafta": "12. Hafta",
      "rakip": "Karaköprü Belediyespor",
      "skor": "2 - 1",
      "durum": "MS",
      "ev_sahibi_mi": True
    }
  ]
}

# puan-durumu.json dosyasını otomatik günceller
with open("puan-durumu.json", "w", encoding="utf-8") as f:
    json.dump(veri, f, ensure_ascii=False, indent=4)

print("Puan durumu ve maçlar başarıyla güncellendi!")
