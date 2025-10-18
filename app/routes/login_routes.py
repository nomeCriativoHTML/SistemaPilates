from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from app.main import templates

router = APIRouter()

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...)
):
    if email and password:
        return RedirectResponse(url="/home", status_code=303)
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")