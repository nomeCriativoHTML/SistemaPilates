from sqlalchemy.orm import Session
from app.models.admin import GestaoDeAlunos, GestaoDeProfessores, GestaoDeEstudos
from app.schema.admin import (
    GestaoDeAlunosCreate, GestaoDeAlunosUpdate,
    GestaoDeProfessoresCreate, GestaoDeProfessoresUpdate,  
    GestaoDeEstudosCreate, GestaoDeEstudosUpdate           
)
from fastapi import HTTPException

# --- Alunos ---
def create_aluno(db: Session, aluno: GestaoDeAlunosCreate):
    # Verificar se email já existe
    existing_aluno = db.query(GestaoDeAlunos).filter(GestaoDeAlunos.email == aluno.email).first()
    if existing_aluno:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    db_aluno = GestaoDeAlunos(**aluno.model_dump()) 
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

def list_alunos(db: Session):
    return db.query(GestaoDeAlunos).all()

def update_aluno(db: Session, aluno_id: int, aluno: GestaoDeAlunosUpdate):
    db_aluno = db.query(GestaoDeAlunos).filter(GestaoDeAlunos.id == aluno_id).first()
    if not db_aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    update_data = aluno.model_dump(exclude_unset=True)  
    for key, value in update_data.items():
        setattr(db_aluno, key, value)
    
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

def delete_aluno(db: Session, aluno_id: int):
    db_aluno = db.query(GestaoDeAlunos).filter(GestaoDeAlunos.id == aluno_id).first()
    if not db_aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    db.delete(db_aluno)
    db.commit()
    return {"detail": "Aluno removido com sucesso"}

# --- Professores ---
def create_professor(db: Session, professor: GestaoDeProfessoresCreate):
    # Verificar se email já existe
    existing_prof = db.query(GestaoDeProfessores).filter(GestaoDeProfessores.email == professor.email).first()
    if existing_prof:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    db_prof = GestaoDeProfessores(**professor.model_dump())
    db.add(db_prof)
    db.commit()
    db.refresh(db_prof)
    return db_prof

def list_professores(db: Session):
    return db.query(GestaoDeProfessores).all()

def update_professor(db: Session, professor_id: int, professor: GestaoDeProfessoresUpdate):
    db_prof = db.query(GestaoDeProfessores).filter(GestaoDeProfessores.id == professor_id).first()
    if not db_prof:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    
    update_data = professor.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_prof, key, value)
    
    db.commit()
    db.refresh(db_prof)
    return db_prof

def delete_professor(db: Session, professor_id: int):
    db_prof = db.query(GestaoDeProfessores).filter(GestaoDeProfessores.id == professor_id).first()
    if not db_prof:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    db.delete(db_prof)
    db.commit()
    return {"detail": "Professor removido com sucesso"}

# --- Estúdios ---
def create_estudio(db: Session, estudio: GestaoDeEstudosCreate):
    db_est = GestaoDeEstudos(**estudio.model_dump())
    db.add(db_est)
    db.commit()
    db.refresh(db_est)
    return db_est

def list_estudios(db: Session):
    return db.query(GestaoDeEstudos).all()

def update_estudio(db: Session, estudio_id: int, estudio: GestaoDeEstudosUpdate):
    db_est = db.query(GestaoDeEstudos).filter(GestaoDeEstudos.id == estudio_id).first()
    if not db_est:
        raise HTTPException(status_code=404, detail="Estúdio não encontrado")
    
    update_data = estudio.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_est, key, value)
    
    db.commit()
    db.refresh(db_est)
    return db_est

def delete_estudio(db: Session, estudio_id: int):
    db_est = db.query(GestaoDeEstudos).filter(GestaoDeEstudos.id == estudio_id).first()
    if not db_est:
        raise HTTPException(status_code=404, detail="Estúdio não encontrado")
    db.delete(db_est)
    db.commit()
    return {"detail": "Estúdio removido com sucesso"}