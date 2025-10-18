from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.connection import Base  


class Estudio(Base):
    __tablename__ = "estudios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    endereco = Column(String(255), nullable=False)
    cep = Column(String(9), nullable=False)  
    telefone = Column(String(20), nullable=True)
    email = Column(String(120), nullable=True)
    capacidade_maxima = Column(Integer, default=3)
    criado_em = Column(DateTime, default=datetime.utcnow)

    #  Relacionamentos
    agendas = relationship("Agenda", back_populates="estudio", cascade="all, delete-orphan")
    professores = relationship("Professor", back_populates="estudio")

    def __repr__(self):
        return f"<Estudio(nome='{self.nome}', cep='{self.cep}', capacidade={self.capacidade_maxima})>"
