from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from datetime import datetime

from app.database.connection import get_db
from app.schema.login.professor_login import ProfessorLogin
from app.controllers.login.professor_login import ProfessorLoginController
from app.utils.security import get_current_professor

templates = Jinja2Templates(directory="app/templates")
router = APIRouter(prefix="/login/professor", tags=["Login Professor"])

# ==========================
# Página de login professor
# ==========================
@router.get("/", response_class=HTMLResponse)
async def pagina_login_professor(request: Request, error: str = None):
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": error}
    )

# ==========================
# Login via formulário / JS
# ==========================
@router.post("/")
async def login_professor_form(request: Request, db: Session = Depends(get_db)):
    try:
        data = await request.form()
        email = data.get("email")
        senha = data.get("password")

        # Chamar controller
        login_result = ProfessorLoginController.login_professor(
            db, ProfessorLogin(email=email, senha=senha)
        )

        token = login_result["token"]

        # Criar resposta JSON com redirecionamento
        response = JSONResponse({
            "message": login_result["message"],
            "redirect": "/login/professor/dashboard"
        })

        # Gravar cookie HTTP-only
        response.set_cookie(
            key="professor_access_token",
            value=token,
            httponly=True,
            secure=False,   # coloque True em HTTPS
            samesite="lax",
            max_age=60 * 60 * 24,  # 1 dia
        )

        return response

    except HTTPException as e:
        return JSONResponse(content={"error": e.detail}, status_code=e.status_code)

    except Exception as e:
        return JSONResponse(
            content={"error": f"Erro inesperado: {str(e)}"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

# ==============================
# Página do professor pós-login
# ==============================
@router.get("/dashboard", response_class=HTMLResponse)
async def pagina_professor(
    request: Request,
    professor = Depends(get_current_professor)
):
    data_formatada = datetime.now().strftime("%d/%m/%Y")

    return templates.TemplateResponse(
        "professor.html",
        {
            "request": request,
            "professor": professor,
            "data_atual": data_formatada
        }
    )

