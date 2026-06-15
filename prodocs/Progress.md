# Geliştirme Günlüğü (Progress.md) - SubCentral

## 🐛 Karşılaşılan Hatalar ve Çözüm Kayıtları

### Hata 1: 'pip' is not recognized as an internal or external command
- **Problem:** Windows terminalinde kütüphaneleri yüklemek isterken sistemin pip komutunu tanımaması.
- **Çözüm:** `py -m pip install` alternatifi kullanılarak kütüphaneler başarıyla yüklendi.

### Hata 2: File does not exist: app.py
- **Problem:** Terminalin klasör içindeki dosyaları uzantı gizleme çakışması nedeniyle görememesi.
- **Çözüm:** Dosya uzantıları kontrol edilerek el ile `app.py` ve `requirements.txt` olarak güncellendi ve sorun çözüldü.