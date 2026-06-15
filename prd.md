# 📄 Ürün Gereksinim Dokümanı (PRD) - SubCentral

**Sürüm:** 1.0  
**Durum:** Tamamlandı (Ödev Kapsamında)  
**Rol:** Kıdemli Proje Geliştirici  

## 1. Giriş ve Problem Tanımı
Günümüzde dijital dönüşümle birlikte eğlence, yazılım, bulut depolama ve iş araçları gibi birçok servis abonelik modeline (SaaS) geçmiştir. Kullanıcılar birden fazla platforma abone olmakta, fatura kesim tarihlerini unutmakta ve farkında olmadan kullanmadıkları servislere ödeme yapmaya devam etmektedir. Mevcut finans uygulamaları bu abonelikleri kategorize etmekte yetersiz kalmakta ve geleceğe dönük bütçe analizi sunmamaktadır.

## 2. Kullanıcı Hikayeleri (User Stories)
- **US1:** Bir kullanıcı olarak, tüm aboneliklerimi bir listede görmek istiyorum ki aylık nakit akışımı planlayabileyim.
- **US2:** Bir öğrenci olarak, dövizle ödediğim servislerin TL maliyetini görmek istiyorum ki sürpriz kur farklarıyla karşılaşmayayım.
- **US3:** Bir deneme sürümü kullanıcısı olarak, kartımdan para çekilmeden önce bildirim almak istiyorum ki istemediğim servisi iptal edebileyim.

## 3. Fonksiyonel Gereksinimler (FR)
- **FR1:** Sistem, kullanıcı girişine göre aylık ve yıllık toplam harcama projeksiyonu oluşturmalıdır.
- **FR2:** Her abonelik için kategori etiketi (Eğlence, İş/Yazılım, Eğitim, Sağlık, Depolama) atanabilmelidir.
- **FR3:** Kullanıcı mevcut bir aboneliği düzenleyebilmeli veya silebilmelidir.
- **FR4:** Sistem, entegre yapay zeka (LLM) servisleri aracılığıyla kullanıcının mevcut abonelik yapısını inceleyerek Türkçe bütçe optimizasyonu ve tasarruf tavsiyeleri sunmalıdır.

## 4. Fonksiyonel Olmayan Gereksinimler (NFR)
- **NFR1 (Mimari):** Frontend ve Backend birbirinden bağımsız (Decoupled) çalışmalı; backend ileride mobil platformlara da hizmet verebilecek API yapısında olmalıdır.
- **NFR2 (Kullanılabilirlik):** Arayüz, mobil öncelikli (responsive), sade ve anlaşılır bir finansal kontrol paneli sunmalıdır.

## 5. Başarı Metrikleri (KPI)
- **Aktif Kullanım:** Kullanıcıların haftada en az 1 kez dashboard'u kontrol etmesi.
- **Tasarruf Oranı:** Kullanıcıların uygulama ve AI tavsiyeleri sayesinde iptal ettiği "hayalet abonelik" sayısı.
