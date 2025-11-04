from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.controllers.login.aluno_login import AlunoLoginController
from app.schema.login.aluno_login import AlunoLogin
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
router = APIRouter(prefix="/login", tags=["Login Aluno"])

# =======================
# Página HTML de login
# =======================
@router.get("/", response_class=HTMLResponse)
async def pagina_login(request: Request, error: str = None):
    """
    Renderiza a página de login de aluno.
    """
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": error}
    )

# =======================
# Login via formulário HTML
# =======================
@router.post("/aluno")
async def login_aluno_form(request: Request, db: Session = Depends(get_db)):
    """
    Recebe os dados do formulário HTML e realiza login.
    Retorna JSON com mensagem e token.
    """
    try:
        data = await request.form()
        email = data.get("email")
        senha = data.get("password")  # id do input na tela

        resultado = AlunoLoginController.login_aluno(
            db, AlunoLogin(email=email, senha=senha)
        )

        return JSONResponse(content=resultado)

    except HTTPException as e:
        return JSONResponse(content={"error": e.detail}, status_code=e.status_code)

    except Exception as e:
        return JSONResponse(
            content={"error": f"Erro inesperado: {str(e)}"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

# =======================
# Login via API (JSON)
# =======================
@router.post("/aluno/api")
def login_aluno_api(dados: AlunoLogin, db: Session = Depends(get_db)):
    """
    Endpoint para login via API JSON.
    """
    return AlunoLoginController.login_aluno(db, dados)


#RENDERIZA A PAGINA DE ALUNO APÓS O LOGIN
@router.get("/aluno", response_class=HTMLResponse)
async def pagina_aluno(request: Request):
    """
    Página principal do aluno após login.
    """
    return templates.TemplateResponse("aluno.html", {"request": request})
