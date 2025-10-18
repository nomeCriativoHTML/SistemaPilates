from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.database.connection import Base
from app.models.enums import Presenca

class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    professor_id = Column(Integer, ForeignKey("professores.id"), nullable=False)
    aula_id = Column(Integer, ForeignKey("agendas.id"), nullable=False)
    data_hora = Column(DateTime, nullable=False)
    minha_presenca = Column(
        Enum(Presenca, name="presenca_enum"),
        default=Presenca.indefinido,
        nullable=False
    )

    # 🔗 Relacionamentos
    aluno = relationship("Aluno", back_populates="agendamentos")
    professor = relationship("Professor", back_populates="agendamentos")
    aula = relationship("Agenda", back_populates="agendamentos")
