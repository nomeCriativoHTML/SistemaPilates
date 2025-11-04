from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.controllers.admin_controller import (
    create_aluno, list_alunos, update_aluno, delete_aluno,
    create_professor, list_professores, update_professor, delete_professor,
    create_estudio, list_estudios, update_estudio, delete_estudio
)
from app.schema.admin import (
    GestaoDeAlunosCreate, GestaoDeAlunosUpdate,
    GestaoDeProfessoresCreate, GestaoDeProfessoresUpdate,
    GestaoDeEstudosCreate, GestaoDeEstudosUpdate
)

router = APIRouter()

# ===== ROTAS PARA ALUNOS =====
@router.post("/alunos/")
def criar_aluno(aluno: GestaoDeAlunosCreate, db: Session = Depends(get_db)):
    return create_aluno(db, aluno)

@router.get("/alunos/")
def listar_alunos(db: Session = Depends(get_db)):
    return list_alunos(db)

@router.put("/alunos/{aluno_id}")
def atualizar_aluno(aluno_id: int, aluno: GestaoDeAlunosUpdate, db: Session = Depends(get_db)):
    return update_aluno(db, aluno_id, aluno)

@router.delete("/alunos/{aluno_id}")
def excluir_aluno(aluno_id: int, db: Session = Depends(get_db)):
    return delete_aluno(db, aluno_id)

# ===== ROTAS PARA PROFESSORES =====
@router.post("/professores/")
def criar_professor(professor: GestaoDeProfessoresCreate, db: Session = Depends(get_db)):
    return create_professor(db, professor)

@router.get("/professores/")
def listar_professores(db: Session = Depends(get_db)):
    return list_professores(db)

@router.put("/professores/{professor_id}")
def atualizar_professor(professor_id: int, professor: GestaoDeProfessoresUpdate, db: Session = Depends(get_db)):
    return update_professor(db, professor_id, professor)

@router.delete("/professores/{professor_id}")
def excluir_professor(professor_id: int, db: Session = Depends(get_db)):
    return delete_professor(db, professor_id)

# ===== ROTAS PARA ESTÚDIOS =====
@router.post("/estudios/")
def criar_estudio(estudio: GestaoDeEstudosCreate, db: Session = Depends(get_db)):
    return create_estudio(db, estudio)

@router.get("/estudios/")
def listar_estudios(db: Session = Depends(get_db)):
    return list_estudios(db)

@router.put("/estudios/{estudio_id}")
def atualizar_estudio(estudio_id: int, estudio: GestaoDeEstudosUpdate, db: Session = Depends(get_db)):
    return update_estudio(db, estudio_id, estudio)

@router.delete("/estudios/{estudio_id}")
def excluir_estudio(estudio_id: int, db: Session = Depends(get_db)):
    return delete_estudio(db, estudio_id)