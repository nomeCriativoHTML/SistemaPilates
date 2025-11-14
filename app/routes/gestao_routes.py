from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.aluno import Aluno
from app.models.professor import Professor
from app.models.estudio import Estudio

router = APIRouter(
    prefix="/gestao",
    tags=["Gestão / Dashboard"]
)

# ================================
# Listar alunos
# ================================
@router.get("/dados/alunos")
def api_listar_alunos(db: Session = Depends(get_db)):
    alunos = db.query(Aluno).all()
    return [
        {
            "id": a.id,
            "nome": a.nome,
            "cpf": a.cpf,
            "email": a.email,
            "status_pagamento": a.status_pagamento.value
        }
        for a in alunos
    ]


# ================================
# Listar professores
# ================================
@router.get("/dados/professores")
def api_listar_professores(db: Session = Depends(get_db)):
    profs = db.query(Professor).all()
    return [
        {
            "id": p.id,
            "nome": p.nome
        }
        for p in profs
    ]


# ================================
# Listar estúdios
# ================================
@router.get("/dados/estudios")
def api_listar_estudios(db: Session = Depends(get_db)):
    estudios = db.query(Estudio).all()
    return [
        {
            "id": e.id,
            "nome": e.nome,
            "endereco": e.endereco
        }
        for e in estudios
    ]


# ================================
# Pagamentos atrasados
# ================================
@router.get("/dados/pagamentos_atrasados")
def api_pagamentos_atrasados(db: Session = Depends(get_db)):
    atrasados = db.query(Aluno).filter(
        Aluno.status_pagamento.in_(["pendente", "atrasado"])
    ).all()

    return [
        {
            "id": a.id,
            "nome": a.nome,
            "cpf": a.cpf,
            "email": a.email,
            "status_pagamento": a.status_pagamento.value
        }
        for a in atrasados
    ]
