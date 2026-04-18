# 📄 Ürün Gereksinim Dokümanı (PRD) - SubCentral

**Sürüm:** 1.0  
**Durum:** Taslak (Ödev Kapsamında)  
**Rol:** Kıdemli Proje Geliştirici

## 1. Giriş ve Problem Tanımı
Kullanıcılar birden fazla dijital servise abonedir ve aylık toplam giderlerini takip etmekte zorlanmaktadır. Bu durum bütçe yönetimini zorlaştırmakta ve kullanılmayan servisler için gereksiz ödemelere neden olmaktadır.

## 2. Kullanıcı Hikayeleri (User Stories)
- **US1:** Bir kullanıcı olarak, tüm aboneliklerimi bir listede görmek istiyorum ki aylık nakit akışımı planlayabileyim.
- **US2:** Bir öğrenci olarak, dövizle ödediğim servislerin TL maliyetini görmek istiyorum ki sürpriz kur farklarıyla karşılaşmayayım.
- **US3:** Bir deneme sürümü kullanıcısı olarak, kartımdan para çekilmeden önce bildirim almak istiyorum ki istemediğim servisi iptal edebileyim.

## 3. Fonksiyonel Gereksinimler (FR)
- **FR1:** Sistem, kullanıcı girişine göre aylık ve yıllık toplam harcama projeksiyonu oluşturmalıdır.
- **FR2:** Her abonelik için kategori etiketi (Eğlence, İş, Sağlık vb.) atanabilmelidir.
- **FR3:** Kullanıcı mevcut bir aboneliği düzenleyebilmeli veya silebilmelidir.

## 4. Fonksiyonel Olmayan Gereksinimler (NFR)
- **NFR1 (Güvenlik):** Kullanıcı verileri yerel ortamda güvenli şekilde saklanmalıdır.
- **NFR2 (Kullanılabilirlik):** Arayüz, mobil öncelikli (responsive) ve sade bir tasarım diline sahip olmalıdır.

## 5. Başarı Metrikleri (KPI)
- **Aktif Kullanım:** Kullanıcıların haftada en az 1 kez dashboard'u kontrol etmesi.
- **Tasarruf Oranı:** Kullanıcıların uygulama sayesinde iptal ettiği "hayalet abonelik" sayısı.
