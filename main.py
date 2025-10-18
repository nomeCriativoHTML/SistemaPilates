from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import uvicorn

# =========================================================
# Inicialização do app
# =========================================================
app = FastAPI(
    title="Sistema Pilates",
    description="API do Sistema de Gestão de Alunos e Aulas",
    version="1.0.0"
)

# =========================================================
# Configuração de templates e arquivos estáticos
# =========================================================
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# =========================================================
# Middleware CORS
# =========================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================================
# Importação e inclusão de rotas
# =========================================================
from app.routes import aluno_routes
app.include_router(aluno_routes.router)

# =========================================================
# Rotas básicas
# =========================================================
@app.get("/", include_in_schema=False)
async def root():
    """Redireciona para a página de cadastro"""
    return RedirectResponse(url="/alunos/cadastro")

# =========================================================
# Inicialização do servidor
# =========================================================
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


