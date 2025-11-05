from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.aluno import Aluno
from app.schema.login.aluno_login import AlunoLogin
from app.utils.security import verify_senha, create_access_token  # utils: hash e JWT

class AlunoLoginController:

    @staticmethod
    def login_aluno(db: Session, dados: AlunoLogin):
        #  Verificar se o aluno existe
        aluno = db.query(Aluno).filter(Aluno.email == dados.email).first()
        if not aluno:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Email não cadastrado."
            )

        #  Verificar senha
        if not verify_senha(dados.senha, aluno.senha):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Senha incorreta."
            )

        #  Gerar token JWT
        token = create_access_token({"sub": aluno.email, "id": aluno.id})

        # Retornar dados seguros
        return {
            "mensagem": "Login realizado com sucesso.",
            "aluno_id": aluno.id,
            "nome": aluno.nome,
            "token": token
        }
