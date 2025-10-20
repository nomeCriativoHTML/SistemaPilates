from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.controllers.professor_controller import ProfessorController
from app.schema.professor import ProfessorCreate, ProfessorUpdate

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="app/templates")

router = APIRouter(
    prefix="/professores",
    tags=["Professores"]
)

# =====================================================
# PÁGINAS HTML (Renderizadas com Jinja2)
# =====================================================

@router.get("/cadastro", response_class=HTMLResponse)
async def pagina_cadastro_professor(request: Request, success: bool = False, error: str = None):
    """
    Exibe a página de cadastro de professores.
    Pode exibir mensagem de sucesso/erro após submissão do formulário.
    """
    return templates.TemplateResponse(
        "professor.html",  # Usando o template professor.html que já existe
        {"request": request, "success": success, "error": error}
    )

@router.post("/cadastro/professor")
async def criar_professor_form(request: Request, db: Session = Depends(get_db)):
    """
    Recebe os dados do formulário via JSON e cria um professor no banco.
    Retorna uma resposta JSON para o front.
    """
    try:
        data = await request.json()

        professor_data = ProfessorCreate(
            nome=data.get("nome"),
            cref=data.get("cref"),
            email=data.get("email"),
            senha=data.get("senha"),
            identificador=data.get("identificador"),
            tipo_identificador=data.get("tipo_identificador"),
            ativo=data.get("ativo", True),
            estudio_id=data.get("estudio_id")
        )

        ProfessorController.criar_professor(db, professor_data)

        return JSONResponse(
            content={"message": "Professor cadastrado com sucesso!"},
            status_code=status.HTTP_201_CREATED
        )

    except HTTPException as e:
        return JSONResponse(
            content={"error": e.detail},
            status_code=e.status_code
        )

    except Exception as e:
        return JSONResponse(
            content={"error": f"Erro inesperado: {str(e)}"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

# =====================================================
# ENDPOINTS RESTFUL (API)
# =====================================================

@router.post("/", response_model=None, status_code=status.HTTP_201_CREATED)
def criar_professor_api(professor: ProfessorCreate, db: Session = Depends(get_db)):
    """
    Cria um novo professor via API.
    """
    return ProfessorController.criar_professor(db, professor)

@router.get("/", response_model=None)
def listar_professores(db: Session = Depends(get_db)):
    """
    Lista todos os professores.
    """
    return ProfessorController.listar_professores(db)

@router.get("/{professor_id}", response_model=None)
def obter_professor(professor_id: int, db: Session = Depends(get_db)):
    """
    Retorna um professor específico pelo ID.
    """
    return ProfessorController.obter_professor(db, professor_id)

@router.put("/{professor_id}", response_model=None)
def atualizar_professor(professor_id: int, professor_data: ProfessorUpdate, db: Session = Depends(get_db)):
    """
    Atualiza os dados de um professor existente.
    """
    return ProfessorController.atualizar_professor(db, professor_id, professor_data)

@router.delete("/{professor_id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_professor(professor_id: int, db: Session = Depends(get_db)):
    """
    Exclui um professor pelo ID.
    """
    return ProfessorController.excluir_professor(db, professor_id)