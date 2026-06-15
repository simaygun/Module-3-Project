# Technical Stack & AI Usage - SubCentral

## 1. Kullanılan Teknolojiler ve Seçim Gerekçeleri

### Frontend: Streamlit
- **Gerekçe:** Veri odaklı arayüzleri ve dashboard tasarımlarını çok hızlı bir şekilde prototipleyip canlandırmayı sağladığı için tercih edilmiştir. State yönetimi ve grafik bileşenleri entegre olarak geldiğinden kullanıcı etkileşimi yüksek bir frontend deneyimi sunar.

### Backend: FastAPI
- **Gerekçe:** Frontend ve backend mimarisini tamamen birbirinden ayırmak (decoupling) ve ileride mobil (iOS/Android) veya farklı web arayüzlerine hizmet verebilecek modüler bir API yapısı kurmak amacıyla FastAPI seçilmiştir.

### Yapay Zeka Motoru: Google Gemini API
- **Gerekçe:** Gelişmiş Türkçe dil desteği, bağlamı (context) kaybetmeden finansal/bütçe analizleri yapabilme yeteneği nedeniyle uygulamanın çekirdek mantığına (core logic) API üzerinden entegre edilmesi planlanmıştır.

---

## 2. Geliştirme Sürecinde Yapay Zeka (AI) Kullanımı
SubCentral projesinin geliştirme maratonunda yapay zeka, bir "Copilot" ve "Pair Programmer" olarak sürecin her aşamasında aktif rol oynamıştır:

1. **Mimari Dönüşüm:** Monolitik yapılabilecek yapının, jüri kriterlerine uygun olarak FastAPI backend ve Streamlit frontend olarak iki ayrı servise bölünmesi aşamasındaki refactoring süreçleri AI yönlendirmeleriyle yapılmıştır.
2. **Hata Ayıklama (Debugging):** Windows ortamında yaşanan 'pip' ve 'python' çevre değişkeni (PATH) hatalarının çözülmesi ve terminal dosya okuma problemlerinin aşılmasında yapay zeka destekli hata analizi kullanılmıştır.