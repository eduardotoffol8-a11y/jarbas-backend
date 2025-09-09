from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Jarbas API", version="0.1.0")

# CORS liberado para facilitar o front (ajuste depois)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"ok": True, "service": "jarbas-backend"}

@app.get("/health")
def health():
    return {"status": "ok"}

# Endpoints mínimos que o front espera
@app.get("/dashboard/summary")
def dashboard_summary():
    return {"cards": [{"title": "Tudo certo", "value": 1}]}

@app.get("/email/inbox")
def email_inbox():
    return {"inbox": []}

@app.post("/api/chat")
def chat():
    return {"reply": "Jarbas está online."}

@app.get("/whatsapp/status")
def whatsapp_status():
    return {"connected": False}

@app.get("/calendar/events")
def calendar_events():
    return {"events": []}

# NFSe e Treinamento placeholders
@app.get("/nfse/status")
def nfse_status():
    return {"status": "idle"}

@app.get("/training/list")
def training_list():
    return {"files": []}
