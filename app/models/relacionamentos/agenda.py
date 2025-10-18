from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base
from app.models.enums import StatusAula

class Agenda(Base):
    __tablename__ = "agendas"

    id = Column(Integer, primary_key=True, index=True)
    professor_id = Column(Integer, ForeignKey("professores.id"), nullable=False)
    estudio_id = Column(Integer, ForeignKey("estudios.id"), nullable=True)
    data_hora = Column(DateTime, nullable=False)
    tipo_aula = Column(String(50))
    estudo = Column(String(100))
    alunos_confirmados = Column(Integer, default=0)
    max_alunos = Column(Integer, default=3)
    status = Column(Enum(StatusAula), default=StatusAula.disponivel)

    # 🔗 Relacionamentos
    professor = relationship("Professor", back_populates="agendas")
    estudio = relationship("Estudio", back_populates="agendas")
    agendamentos = relationship("Agendamento", back_populates="aula", cascade="all, delete-orphan")
    alunos = relationship("AlunoNaAula", back_populates="agenda", cascade="all, delete-orphan")
    evolucoes = relationship("MinhaEvolucao", back_populates="agenda", cascade="all, delete-orphan")
