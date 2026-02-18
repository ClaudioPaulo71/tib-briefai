from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.models.request_model import RequestModel
from app.core.prompt_engine import build_prompt
from app.core.text_generator import generate_text
from app.core.identity_engine import get_identity_profile

app = FastAPI(title="BriefAI - Corporate Communication Engine")

# Serve o index.html na raiz
@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/gerar")
def gerar_texto(request: RequestModel):
    profile = get_identity_profile(request.perfil)
    prompt = build_prompt(
        tipo=request.tipo,
        publico=request.publico,
        tom=request.tom,
        topicos=request.topicos,
        identity_profile=profile,
        language=request.language  # novo parâmetro
    )
    texto, tokens = generate_text(prompt)
    return {"texto": texto, "tokens_usados": tokens}

# Monta pasta estática (caso precise de CSS/JS futuro)
app.mount("/static", StaticFiles(directory="frontend"), name="static")