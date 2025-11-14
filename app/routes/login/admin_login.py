from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.controllers.gestao_controller import GestaoController
from app.controllers.login.admin_login import AdminLoginController
from app.schema.login.admin_login import AdminLogin
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
router = APIRouter(prefix="/login", tags=["Login Admin"])

# Página HTML de login 
@router.get("/", response_class=HTMLResponse)
async def pagina_login(request: Request, error: str = None):
    return templates.TemplateResponse("login.html", {"request": request, "error": error})


# ==========================
# LOGIN VIA FORM HTML
# ==========================
@router.post("/admin")
async def login_admin_form(request: Request, db: Session = Depends(get_db)):
    try:
        data = await request.form()
        email = data.get("email")
        senha = data.get("password")

        resultado = AdminLoginController.login_admin(
            db, AdminLogin(email=email, senha=senha)
        )

        return JSONResponse(content=resultado)

    except HTTPException as e:
        return JSONResponse(content={"error": e.detail}, status_code=e.status_code)

    except Exception as e:
        return JSONResponse(
            content={"error": f"Erro inesperado: {str(e)}"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# ==========================
# LOGIN VIA API JSON
# ==========================
@router.post("/admin/api")
def login_admin_api(dados: AdminLogin, db: Session = Depends(get_db)):
    return AdminLoginController.login_admin(db, dados)


# ==========================
# PÁGINA PRINCIPAL APÓS LOGIN
# ==========================

@router.get("/admin", response_class=HTMLResponse)
async def pagina_admin(request: Request, db: Session = Depends(get_db)):
    
    dados = GestaoController.obter_dados_dashboard(db)

    return templates.TemplateResponse(
        "admin.html",
        {
            "request": request,
            **dados
        }
    )
