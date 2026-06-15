# 💎 SubCentral v1.0

SubCentral, kullanıcıların dijital aboneliklerini tek bir panelden yönetmelerini, döviz bazlı harcamalarının TL projeksiyonlarını görmelerini ve yapay zeka (Gemini API) desteğiyle bütçe tasarruf analizleri almalarını sağlayan modern bir finansal takip uygulamasıdır.

🚀 SubCentral Canlı Uygulama Linki: [https://module-3-project-gitwch2rnokdihc5jcxuhj.streamlit.app/]

## 📂 Proje Yapısı (Directory Structure)
- `/subcentral-frontend`: Streamlit ile geliştirilmiş dinamik kullanıcı arayüzü.
- `/backend`: FastAPI mimarisi üzerine kurulu modüler API katmanı.
- `/prodocs`: Geliştirme referansları, teknoloji seçim gerekçeleri ve ilerleme günlükleri.

## 🚀 Yerel Kurulum ve Çalıştırma (Local Setup)

### 1. Frontend Çalıştırma
```bash
cd subcentral-frontend
py -m pip install -r requirements.txt
py -m streamlit run app.py
