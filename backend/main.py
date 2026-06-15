from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="SubCentral Backend API")

# Frontend ile backend'in güvenli haberleşmesi için CORS ayarı
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Geçici veri tabanı (Hafızada tutulan basit bir liste)
fake_db = [
    {"id": 1, "name": "Netflix", "price": 149.99, "currency": "TRY", "period": "Aylık", "category": "Eğlence", "next_payment_date": "2026-06-20", "is_free_trial": False},
    {"id": 2, "name": "Spotify", "price": 59.99, "currency": "TRY", "period": "Aylık", "category": "Eğlence", "next_payment_date": "2026-06-17", "is_free_trial": False}
]

class Subscription(BaseModel):
    name: str
    price: float
    currency: str
    period: str
    category: str
    next_payment_date: str
    is_free_trial: bool

# 1. Tüm abonelikleri getiren API uç noktası
@app.get("/subscriptions")
def get_subscriptions():
    return fake_db

# 2. Yeni abonelik ekleyen API uç noktası
@app.post("/subscriptions")
def create_subscription(sub: Subscription):
    new_sub = sub.dict()
    new_sub["id"] = len(fake_db) + 1
    fake_db.append(new_sub)
    return {"status": "success", "message": "Abonelik backend listesine eklendi."}

# 3. Yapay zeka analiz şablonu (İleride Gemini buraya bağlanacak)
@app.post("/ai-analyze")
def ai_analyze():
    return {"analysis": "SubCentral AI Önerisi: Eğlence kategorisinde birden fazla aboneliğiniz bulunuyor. Tasarruf etmek için Spotify veya Netflix ürünlerinden birini askıya almayı düşünebilirsiniz."}