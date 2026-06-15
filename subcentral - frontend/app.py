import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="SubCentral - Abonelik Takip Paneli", layout="wide")

st.title("💎 SubCentral v1.0")
st.write("Dijital Abonelik ve Yapay Zeka Destekli Bütçe Yönetimi")

# ---------------------------------------------------------
# GEÇİCİ TEST VERİLERİ (Backend bağlanana kadar arayüzü görmek için)
# ---------------------------------------------------------
if "mock_db" not in st.session_state:
    st.session_state.mock_db = [
        {"id": 1, "name": "Netflix", "price": 149.99, "currency": "TRY", "period": "Aylık", "category": "Eğlence", "next_payment_date": "2026-06-20", "is_free_trial": False, "monthly_cost_tl": 149.99},
        {"id": 2, "name": "Spotify", "price": 59.99, "currency": "TRY", "period": "Aylık", "category": "Eğlence", "next_payment_date": "2026-06-17", "is_free_trial": False, "monthly_cost_tl": 59.99},
        {"id": 3, "name": "GitHub Copilot", "price": 10.00, "currency": "USD", "period": "Aylık", "category": "İş/Yazılım", "next_payment_date": "2026-07-01", "is_free_trial": False, "monthly_cost_tl": 325.00} # 1 USD = 32.5 TL varsayıldı
    ]

# ---------------------------------------------------------
# SOL MENÜ: YENİ ABONELİK EKLEME FORMU & POPÜLER ŞABLONLAR
# ---------------------------------------------------------
st.sidebar.header("➕ Yeni Abonelik Ekle")

template = st.sidebar.selectbox("Hazır Şablon Seçin (Opsiyonel)", ["Manuel Giriş", "Netflix", "Spotify", "YouTube Premium", "GitHub Copilot", "iCloud"])
template_defaults = {
    "Netflix": {"price": 149.99, "currency": "TRY", "category": "Eğlence"},
    "Spotify": {"price": 59.99, "currency": "TRY", "category": "Eğlence"},
    "YouTube Premium": {"price": 79.99, "currency": "TRY", "category": "Eğlence"},
    "GitHub Copilot": {"price": 10.00, "currency": "USD", "category": "İş/Yazılım"},
    "iCloud": {"price": 39.99, "currency": "TRY", "category": "Depolama"}
}

default_vals = template_defaults.get(template, {"price": 0.0, "currency": "TRY", "category": "Eğlence"})

name = st.sidebar.text_input("Abonelik Adı", value="" if template == "Manuel Giriş" else template)
price = st.sidebar.number_input("Ücret", value=default_vals["price"])
currency = st.sidebar.selectbox("Döviz Cinsi", ["TRY", "USD", "EUR"], index=["TRY", "USD", "EUR"].index(default_vals["currency"]))
period = st.sidebar.selectbox("Ödeme Periyodu", ["Aylık", "Yıllık"])
category = st.sidebar.selectbox("Kategori", ["Eğlence", "İş/Yazılım", "Eğitim", "Sağlık", "Depolama"])
next_payment = st.sidebar.date_input("Sonraki Ödeme Tarihi", datetime.now())
is_free_trial = st.sidebar.checkbox("Bu bir Ücretsiz Deneme (Free Trial) sürümüdür")

if st.sidebar.button("Sisteme Kaydet"):
    # Yeni eklenen aboneliği geçici hafızaya ekle
    rate = 32.5 if currency == "USD" else (35.0 if currency == "EUR" else 1.0)
    cost_tl = price * rate
    m_cost = cost_tl if period == "Aylık" else cost_tl / 12
    
    new_sub = {
        "id": len(st.session_state.mock_db) + 1,
        "name": name,
        "price": price,
        "currency": currency,
        "period": period,
        "category": category,
        "next_payment_date": str(next_payment),
        "is_free_trial": is_free_trial,
        "monthly_cost_tl": m_cost
    }
    st.session_state.mock_db.append(new_sub)
    st.sidebar.success("Abonelik başarıyla eklendi! (Geçici Hafıza)")
    st.rerun()

# ---------------------------------------------------------
# ANA PANEL: METRİKLER, GRAFİKLER VE LİSTELEME
# ---------------------------------------------------------
df = pd.DataFrame(st.session_state.mock_db)

if not df.empty:
    # 1. Metrik Kartları
    total_monthly_tl = df["monthly_cost_tl"].sum()
    col1, col2 = st.columns(2)
    col1.metric(label="📊 Toplam Aylık Gider (TL Projeksiyonu)", value=f"{total_monthly_tl:.2f} TL")
    col2.metric(label="📦 Aktif Abonelik Sayısı", value=len(df))
    
    # 2. Hatırlatıcı ve Uyarı Sistemi (Ödeme gününe 2 gün kalanlar)
    critical_alerts = []
    for sub in st.session_state.mock_db:
        if sub["is_free_trial"]:
            critical_alerts.append(f"🔔 **{sub['name']}** deneme sürümü takibinde. Son gün: {sub['next_payment_date']}")

    if critical_alerts:
        st.warning("### 🚨 Kritik Hatırlatıcılar ve Uyarılar")
        for alert in critical_alerts:
            st.write(alert)

    st.write("---")
    g1, g2 = st.columns(2)
    
    # 3. Grafik Katmanı (Pasta Grafik Dağılımı)
    with g1:
        st.write("### 🍰 Kategorilere Göre Dağılım (Aylık TL)")
        fig = px.pie(df, values="monthly_cost_tl", names="category", hole=0.3)
        st.plotly_chart(fig, use_container_width=True)
        
    # 4. Yapay Zeka Alanı Şablonu
    with g2:
        st.write("### 🤖 Yapay Zeka Bütçe Analisti")
        if st.button("AI Analiz Raporu Oluştur"):
            st.info("Backend entegrasyonu tamamlandığında, Gemini API buraya canlı bütçe tasarruf raporu üretecek!")

    # 5. Listeleme ve Silme (CRUD)
    st.write("---")
    st.write("### 📋 Mevcut Abonelikleriniz")
    for idx, sub in enumerate(st.session_state.mock_db):
        c_name, c_price, c_per, c_del = st.columns([3, 3, 3, 1])
        c_name.write(f"**{sub['name']}** ({sub['category']})")
        c_price.write(f"{sub['price']} {sub['currency']} ({sub['period']}) -> ~{sub['monthly_cost_tl']:.2f} TL/Ay")
        c_per.write(f"Fatura Tarihi: {sub['next_payment_date']}")
        if c_del.button("Sil", key=f"del_{idx}"):
            st.session_state.mock_db.pop(idx)
            st.success(f"{sub['name']} silindi.")
            st.rerun()